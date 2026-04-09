"""Chain classification cross-reference: Our Corporate_Name vs CMS Chain Name/ID.
Filtered to footprint states only (existing + expansion)."""

import csv, openpyxl, re
from collections import Counter
from itertools import groupby

FOOTPRINT = {'IN','KY','NC','OH','SC','VA','MI','IL','WI','MN','FL','MD','GA','MO'}

VAULT = '../OneDrive - Eventus WholeHealth/Vault/02_Data_Model'
CMS_FILE = f'{VAULT}/Reference/Source_CMS_NH_ProviderInfo_Feb2026.csv'
DB_FILE = f'{VAULT}/Current/1_Combined_Database_FINAL_V21_1.xlsx'

def norm(s):
    if not s:
        return ''
    return re.sub(r'[^a-z0-9]', '', s.lower())

def norm_addr(s):
    if not s:
        return ''
    s = s.lower().strip()
    for word, abbr in [('street','st'),('road','rd'),('drive','dr'),('avenue','ave'),
                        ('boulevard','blvd'),('lane','ln'),('court','ct'),
                        ('north','n'),('south','s'),('east','e'),('west','w')]:
        s = re.sub(r'\b' + word + r'\b', abbr, s)
    return re.sub(r'[^a-z0-9]', '', s)

# Load CMS
cms = {}
with open(CMS_FILE, 'r', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f):
        addr = row.get('Provider Address', '')
        city = row.get('City/Town', '')
        state = row.get('State', '')
        key = norm_addr(addr) + '|' + norm(city) + '|' + norm(state)
        cms[key] = {
            'name': row['Provider Name'],
            'chain': row['Chain Name'].strip(),
            'chain_id': row['Chain ID'].strip(),
            'cms_ownership': row['Ownership Type'],
            'fac_in_chain': row['Number of Facilities in Chain'].strip(),
            'changed_ownership': row['Provider Changed Ownership in Last 12 Months'],
        }

# Load our DB (SNFs in footprint only)
wb = openpyxl.load_workbook(DB_FILE, read_only=True, data_only=True)
ws = wb.active
headers = [c.value for c in next(ws.iter_rows(min_row=1, max_row=1))]

def col(name):
    return headers.index(name)

matched = 0
unmatched = 0
both_chain = 0
we_corp_cms_blank = 0
we_ind_cms_chain = 0
both_blank = 0
name_match = 0
name_mismatch = 0

mismatch_served = []
mismatch_unserved = []
we_ind_cms_chain_served = []
we_ind_cms_chain_unserved = []
chain_name_pairs = Counter()
chain_name_pairs_served = Counter()

for row in ws.iter_rows(min_row=2, values_only=True):
    source = row[col('Source_Type')]
    state = str(row[col('State')] or '').strip()
    if source != 'SNF' or state not in FOOTPRINT:
        continue

    addr = str(row[col('Address')] or '')
    city = str(row[col('City')] or '')
    key = norm_addr(addr) + '|' + norm(city) + '|' + norm(state)

    if key not in cms:
        unmatched += 1
        continue

    matched += 1
    c = cms[key]
    our_corp = str(row[col('Corporate_Name')] or '').strip()
    our_type = str(row[col('Ownership_Type')] or '').strip()
    our_serve = str(row[col('Do_We_Serve')] or '').strip()
    fac_name = str(row[col('Facility_Name')] or '').strip()
    cms_chain = c['chain']
    served = (our_serve == 'Yes')

    if our_type == 'Corporate' and cms_chain:
        both_chain += 1
        if norm(our_corp) == norm(cms_chain):
            name_match += 1
        else:
            name_mismatch += 1
            chain_name_pairs[(our_corp, cms_chain)] += 1
            if served:
                chain_name_pairs_served[(our_corp, cms_chain)] += 1
                mismatch_served.append((fac_name, our_corp, cms_chain, c['chain_id'], state))
            else:
                mismatch_unserved.append((fac_name, our_corp, cms_chain, c['chain_id'], state))
    elif our_type == 'Corporate' and not cms_chain:
        we_corp_cms_blank += 1
    elif our_type == 'Independent' and cms_chain:
        we_ind_cms_chain += 1
        if served:
            we_ind_cms_chain_served.append((fac_name, cms_chain, c['chain_id'], c['fac_in_chain'], state))
        else:
            we_ind_cms_chain_unserved.append((fac_name, cms_chain, c['chain_id'], c['fac_in_chain'], state))
    else:
        both_blank += 1

wb.close()

# --- Output ---

print('=== CHAIN CROSS-REFERENCE: FOOTPRINT STATES ONLY ===')
print('States: %s' % sorted(FOOTPRINT))
print()
print('SNFs matched to CMS: %d' % matched)
print('SNFs not matched:    %d' % unmatched)
print()
print('--- Ownership Agreement ---')
print('Both Corporate:              %d (%.1f%%)' % (both_chain, both_chain/matched*100))
if both_chain > 0:
    print('  Chain name matches:        %d (%.1f%%)' % (name_match, name_match/both_chain*100))
    print('  Chain name differs:        %d (%.1f%%)' % (name_mismatch, name_mismatch/both_chain*100))
print('Both Independent:            %d (%.1f%%)' % (both_blank, both_blank/matched*100))
total_agree = both_chain + both_blank
print('TOTAL AGREEMENT:             %d (%.1f%%)' % (total_agree, total_agree/matched*100))
print()
print('--- Ownership Disagreement ---')
print('We=Corporate, CMS=no chain:  %d' % we_corp_cms_blank)
print('We=Independent, CMS=chain:   %d' % we_ind_cms_chain)
print()

# Served chain name mismatches
print('=== CHAIN NAME DIFFERS -- SERVED (%d) ===' % len(mismatch_served))
print()
mismatch_served.sort(key=lambda x: (x[1], x[4]))
for corp, group in groupby(mismatch_served, key=lambda x: x[1]):
    items = list(group)
    cms_names = sorted(set(x[2] for x in items))
    cms_ids = sorted(set(x[3] for x in items))
    states = sorted(set(x[4] for x in items))
    print('  Ours: %s' % corp)
    print('  CMS:  %s (ID: %s)' % (', '.join(cms_names), ', '.join(cms_ids)))
    print('  %d facilities in %s' % (len(items), ', '.join(states)))
    show = items[:5] if len(items) > 5 else items
    for it in show:
        print('    - %s (%s)' % (it[0], it[4]))
    if len(items) > 5:
        print('    ... and %d more' % (len(items) - 5))
    print()

# Served facilities we call Independent but CMS has a chain
print('=== WE=INDEPENDENT, CMS=CHAIN -- SERVED (%d) ===' % len(we_ind_cms_chain_served))
print()
for ex in we_ind_cms_chain_served:
    print('  %s (%s) -- CMS: %s (ID:%s, %s fac)' % (ex[0], ex[4], ex[1], ex[2], ex[3]))

print()
print('=== TOP CHAIN NAME MISMATCHES -- ALL (BY FREQUENCY) ===')
print()
for (ours, theirs), cnt in chain_name_pairs.most_common(25):
    tag = ' *SERVED*' if (ours, theirs) in chain_name_pairs_served else ''
    print('  %dx: Ours=[%s] CMS=[%s]%s' % (cnt, ours, theirs, tag))

print()
print('=== WE=INDEPENDENT, CMS=CHAIN -- UNSERVED (top chains, %d total) ===' % len(we_ind_cms_chain_unserved))
print()
chain_groups = Counter(x[1] for x in we_ind_cms_chain_unserved)
for chain, cnt in chain_groups.most_common(20):
    items = [x for x in we_ind_cms_chain_unserved if x[1] == chain]
    states = sorted(set(x[4] for x in items))
    chain_id = items[0][2]
    fac_ct = items[0][3]
    print('  %s (ID:%s, %s in chain) -- %d of ours in %s' % (chain, chain_id, fac_ct, cnt, states))
