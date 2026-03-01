"""Deep dive: Unserved facilities we classify as Independent but CMS assigns to a chain.
Footprint states only."""

import csv, openpyxl, re
from collections import defaultdict

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
            'chain': row['Chain Name'].strip(),
            'chain_id': row['Chain ID'].strip(),
            'fac_in_chain': row['Number of Facilities in Chain'].strip(),
        }

# Load DB — pass 1: collect our Corporate name universe
wb = openpyxl.load_workbook(DB_FILE, read_only=True, data_only=True)
ws = wb.active
headers = [c.value for c in next(ws.iter_rows(min_row=1, max_row=1))]

def col(name):
    return headers.index(name)

our_corps = set()
for row in ws.iter_rows(min_row=2, values_only=True):
    corp = str(row[col('Corporate_Name')] or '').strip()
    if corp and row[col('Ownership_Type')] == 'Corporate':
        our_corps.add(norm(corp))
wb.close()

# Load DB — pass 2: find Independent SNFs in footprint that CMS says are chained
wb = openpyxl.load_workbook(DB_FILE, read_only=True, data_only=True)
ws = wb.active
next(ws.iter_rows(min_row=1, max_row=1))  # skip header

results = []
for row in ws.iter_rows(min_row=2, values_only=True):
    source = row[col('Source_Type')]
    state = str(row[col('State')] or '').strip()
    ownership = str(row[col('Ownership_Type')] or '').strip()
    serve = str(row[col('Do_We_Serve')] or '').strip()

    if source != 'SNF' or state not in FOOTPRINT or ownership != 'Independent':
        continue
    if serve == 'Yes':
        continue  # served handled separately

    addr = str(row[col('Address')] or '')
    city = str(row[col('City')] or '')
    key = norm_addr(addr) + '|' + norm(city) + '|' + norm(state)

    if key not in cms:
        continue
    c = cms[key]
    if not c['chain']:
        continue

    corp_name = str(row[col('Corporate_Name')] or '').strip()
    results.append({
        'fac': str(row[col('Facility_Name')] or '').strip(),
        'city': city,
        'state': state,
        'our_corp': corp_name,
        'cms_chain': c['chain'],
        'chain_id': c['chain_id'],
        'chain_size': int(c['fac_in_chain']) if c['fac_in_chain'] else 0,
    })

wb.close()

# Group by CMS chain
by_chain = defaultdict(list)
for r in results:
    by_chain[r['cms_chain']].append(r)

# Sort: chains where we already have them as Corporate first, then by our facility count
chain_list = sorted(by_chain.items(),
                    key=lambda x: (-int(norm(x[0]) in our_corps), -len(x[1]), -x[1][0]['chain_size']))

# Stats
already_known = sum(1 for name, _ in chain_list if norm(name) in our_corps)
new_chains = len(chain_list) - already_known
total_fac_known = sum(len(facs) for name, facs in chain_list if norm(name) in our_corps)
total_fac_new = sum(len(facs) for name, facs in chain_list if norm(name) not in our_corps)

print('=== UNSERVED INDEPENDENT SNFs WITH CMS CHAIN -- FOOTPRINT STATES ===')
print()
print('Total: %d facilities across %d CMS chains' % (len(results), len(by_chain)))
print()
print('Chains we already track as Corporate elsewhere: %d (%d facilities)' % (already_known, total_fac_known))
print('Chains new to us (not in our Corporate taxonomy): %d (%d facilities)' % (new_chains, total_fac_new))
print()

print('=' * 70)
print('SECTION A: Chains we ALREADY have as Corporate (reclassification candidates)')
print('=' * 70)
print()

for chain_name, facs in chain_list:
    if norm(chain_name) not in our_corps:
        continue
    chain_id = facs[0]['chain_id']
    chain_size = facs[0]['chain_size']
    states = sorted(set(f['state'] for f in facs))

    print('%s (CMS ID:%s, %d nationally)' % (chain_name, chain_id, chain_size))
    print('  %d of our facilities in %s -- ALREADY IN OUR CORPORATE LIST' % (len(facs), ', '.join(states)))
    for f in sorted(facs, key=lambda x: (x['state'], x['fac'])):
        note = ''
        if f['our_corp']:
            note = ' [Corp_Name: %s]' % f['our_corp']
        print('    %s, %s %s%s' % (f['fac'], f['city'], f['state'], note))
    print()

print('=' * 70)
print('SECTION B: Chains NOT in our Corporate taxonomy (new chain candidates)')
print('=' * 70)
print()

for chain_name, facs in chain_list:
    if norm(chain_name) in our_corps:
        continue
    chain_id = facs[0]['chain_id']
    chain_size = facs[0]['chain_size']
    states = sorted(set(f['state'] for f in facs))

    print('%s (CMS ID:%s, %d nationally)' % (chain_name, chain_id, chain_size))
    print('  %d of our facilities in %s' % (len(facs), ', '.join(states)))
    for f in sorted(facs, key=lambda x: (x['state'], x['fac'])):
        note = ''
        if f['our_corp']:
            note = ' [Corp_Name: %s]' % f['our_corp']
        print('    %s, %s %s%s' % (f['fac'], f['city'], f['state'], note))
    print()
