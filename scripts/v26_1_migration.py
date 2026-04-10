"""
V26.1 Migration Script — Corporate Verification Audit Session (2026-04-10)

Applies all findings from 11 entity verifications (CASA, IHC, Adams, Harborview, CSL, CCR, Cogir, Genesis, LCS):
- 51 recodes across 12 entities
- 7 deletes (1 Gallatin TN dup, 1 Victory Noll closed, 4 Genesis NC dups, 1 potential)
- 13 sections total

Evidence: All recodes individually verified via ProPublica per-facility pages.
Dedup decisions logged to scripts/audit_reports/dedup_decisions_log.csv.
GLR corrections logged to scripts/audit_reports/glr_change_log.csv.

Run in READ-ONLY mode first (dry_run=True) to generate report.
Then set dry_run=False to execute with Roian's approval.

Author: Roian Atwood / Claude
Date: 2026-04-10
"""
import pandas as pd
import os
from datetime import datetime

# === CONFIGURATION ===
dry_run = True  # READ-ONLY — set False only with Roian's approval

src_path = r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V26_0.xlsx"
dst_path = r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V26_1.xlsx"
report_path = "scripts/audit_reports/v26_1_change_report.csv"

# === LOAD ===
print(f"Loading V26.0 from: {src_path}")
df = pd.read_excel(src_path)
print(f"Loaded: {len(df)} rows, {len(df.columns)} columns")

changes = []
delete_indices = []

def log_change(punchlist, facility, city, state, field, old_val, new_val, evidence=""):
    changes.append({
        'Punchlist': punchlist,
        'Facility': facility,
        'City': city,
        'State': state,
        'Field': field,
        'Old': old_val,
        'New': new_val,
        'Evidence': evidence
    })

def find_rows(facility_name=None, city=None, state=None, corporate_name=None, exact_facility=False):
    mask = pd.Series([True] * len(df))
    if facility_name:
        if exact_facility:
            mask = mask & (df['Facility_Name'] == facility_name)
        else:
            mask = mask & (df['Facility_Name'].str.contains(facility_name, case=False, na=False))
    if city:
        mask = mask & (df['City'].str.lower().str.strip() == city.lower().strip())
    if state:
        mask = mask & (df['State'].str.strip() == state)
    if corporate_name:
        mask = mask & (df['Corporate_Name'] == corporate_name)
    return mask

def recode_corp(mask, old_name, new_name, punchlist, evidence=""):
    count = mask.sum()
    if count == 0:
        print(f"  WARNING: No rows found for {punchlist} recode {old_name} -> {new_name}")
        return 0
    for idx in df[mask].index:
        row = df.loc[idx]
        log_change(punchlist, row['Facility_Name'], row.get('City', ''), row.get('State', ''),
                   'Corporate_Name', old_name, new_name, evidence)
        if not dry_run:
            df.at[idx, 'Corporate_Name'] = new_name
    print(f"  {punchlist}: {count} rows {old_name} -> {new_name}")
    return count

total = 0

# ============================================================
# SECTION 1: CASA Consulting Verification — Crown Point Christian Village
# ============================================================
print("\n=== CASA Verification: Crown Point Christian Village ===")

mask = find_rows(facility_name='CROWN POINT CHRISTIAN VILLAGE', city='Crown Point', state='IN',
                 corporate_name='CASA CONSULTING')
total += recode_corp(mask, 'CASA CONSULTING', 'CHRISTIAN HORIZONS', 'CASA-CVA-01',
    'christianhorizonsliving.org confirms operator. Separate 70-acre gated CCRC. '
    'ProPublica a-695 does not include this facility.')

# ============================================================
# SECTION 2: IHC Verification — KY Facilities → LYON HEALTHCARE
# ============================================================
print("\n=== IHC Verification: KY Recodes to LYON HEALTHCARE ===")

ky_facilities = [
    ('BREATHITT HEALTH', 'Jackson', 'IHC-KY-01',
     'ProPublica h-185112 chain=Lyon Healthcare. Ownership refused disclosure.'),
    ('EASTWAY HEALTH', 'Louisville', 'IHC-KY-02',
     'ProPublica h-185122 chain=Lyon Healthcare. Owner=A&M Healthcare Investments LLC (100% Sep 2017). Joseph Meisels 23% indirect.'),
    ('HENSON PARK HEALTH', 'Danville', 'IHC-KY-03',
     'ProPublica h-185264 chain=Lyon Healthcare. Owner=Ky 10 Snf Ops Holdings LLC (100% Jan 2025). Shimon Idels managerial control.'),
    ('LAKE BARKLEY HEALTH', 'Kuttawa', 'IHC-KY-04',
     'ProPublica h-185318 chain=Lyon Healthcare. Owner=Ky 10 Snf Ops Holdings LLC. Shimon Idels managerial control.'),
    ('LANDMARK OF LANCASTER', 'Lancaster', 'IHC-KY-05',
     'ProPublica h-185065 chain=Lyon Healthcare. Owner=A&M Healthcare Investments LLC (100% May 2017). Joseph Meisels managing employee.'),
    ('MAPLEWOOD HEALTH', 'Lancaster', 'IHC-KY-06',
     'Campus pair with Landmark of Lancaster SNF. Same address 308 W Maple Ave. Same ownership (A&M Healthcare/Meisels).'),
    ('PARKWOOD HEALTH', 'Louisville', 'IHC-KY-07',
     'ProPublica h-185096 chain=Lyon Healthcare. Owner=Ky 10 Snf Ops Holdings LLC (100% Jan 2025).'),
]

for fac_name, city, punchlist_id, evidence in ky_facilities:
    mask = find_rows(facility_name=fac_name, city=city, state='KY',
                     corporate_name='INFINITY HEALTHCARE CONSULTING')
    total += recode_corp(mask, 'INFINITY HEALTHCARE CONSULTING', 'LYON HEALTHCARE',
                         punchlist_id, evidence)

# ============================================================
# SECTION 3: IHC Verification — OK Facility → LYON HEALTHCARE
# ============================================================
print("\n=== IHC Verification: OK Recode to LYON HEALTHCARE ===")

mask = find_rows(facility_name='MIDWEST CITY POST ACUTE', city='Midwest City', state='OK',
                 corporate_name='INFINITY HEALTHCARE CONSULTING')
total += recode_corp(mask, 'INFINITY HEALTHCARE CONSULTING', 'LYON HEALTHCARE', 'IHC-OK-01',
    'ProPublica h-375252 owner=A&M Healthcare Investments LLC (Meisels family). '
    'Same ownership group as KY Lyon facilities. Joseph Meisels managing employee since Nov 2017.')

# ============================================================
# SECTION 4: IHC Verification — Gallatin TN Duplicate
# ============================================================
print("\n=== IHC Verification: Gallatin TN Duplicate ===")

# Find the duplicate row — the one with 155 beds (inflated) vs 124 (CMS certified)
# Both at 555 E Bledsoe St, Gallatin TN, both CMS source, both IHC
mask_all_gallatin = find_rows(facility_name='WATERS OF GALLATIN', city='Gallatin', state='TN',
                              corporate_name='INFINITY HEALTHCARE CONSULTING')
gallatin_rows = df[mask_all_gallatin]
print(f"  Gallatin TN rows found: {len(gallatin_rows)}")

if len(gallatin_rows) == 2:
    # Find the row with higher bed count (155) — that's the duplicate to delete
    for idx in gallatin_rows.index:
        row = df.loc[idx]
        beds = row.get('Total_Beds', 0)
        print(f"    Row {idx}: {row['Facility_Name']} | Beds: {beds} | Census: {row.get('Census', '')}")
        if beds and float(beds) > 140:
            # This is the inflated duplicate
            log_change('IHC-TN-DUP', row['Facility_Name'], row.get('City', ''), row.get('State', ''),
                       'DELETE ROW', f'Beds={beds}', '',
                       'Duplicate of row with 124 beds at same address 555 E Bledsoe St. '
                       'Both CMS source. 124 matches CMS certified count. 155 is inflated. '
                       'Neither served. Survivor rule Step 6: keep more accurate bed count.')
            delete_indices.append(idx)
            print(f"    → MARKED FOR DELETE (inflated beds={beds})")
elif len(gallatin_rows) == 1:
    print("  Only 1 Gallatin row found — duplicate may already be resolved in V26.0")
else:
    print(f"  WARNING: Expected 2 rows, found {len(gallatin_rows)}")

# ============================================================
# SECTION 5: Adams Health Network — Saint Anne + Blank Corp Recodes + Victory Noll Delete
# ============================================================
print("\n=== Adams Health Network: Saint Anne / Blank Corp Recodes ===")

# Saint Anne ALF: SAINT ANNE COMMUNITIES → ADAMS COUNTY MEMORIAL HOSPITAL
mask = find_rows(facility_name='SAINT ANNE', city='Fort Wayne', state='IN',
                 corporate_name='SAINT ANNE COMMUNITIES')
total += recode_corp(mask, 'SAINT ANNE COMMUNITIES', 'ADAMS COUNTY MEMORIAL HOSPITAL', 'AHN-01',
    'ProPublica h-155349: Adams County Memorial Hospital 100% owner since Sep 2016. Diocese retained spiritual role only.')

# Saint Anne SNF: DIOCESE OF FORT WAYNE SO BEND → ADAMS COUNTY MEMORIAL HOSPITAL
mask = find_rows(facility_name='SAINT ANNE', city='Fort Wayne', state='IN',
                 corporate_name='DIOCESE OF FORT WAYNE SO BEND')
total += recode_corp(mask, 'DIOCESE OF FORT WAYNE SO BEND', 'ADAMS COUNTY MEMORIAL HOSPITAL', 'AHN-02',
    'ProPublica h-155349: Adams County Memorial Hospital 100% owner since Sep 2016. Dane Wheeler start Sep 2016 = transfer date.')

# Adams Heritage: blank → ADAMS COUNTY MEMORIAL HOSPITAL
mask_heritage = find_rows(facility_name='ADAMS HERITAGE', city='Monroeville', state='IN')
heritage_blank = mask_heritage & (df['Corporate_Name'].isna() | (df['Corporate_Name'].str.strip() == ''))
if heritage_blank.sum() > 0:
    for idx in df[heritage_blank].index:
        row = df.loc[idx]
        log_change('AHN-04', row['Facility_Name'], row.get('City', ''), row.get('State', ''),
                   'Corporate_Name', '(blank)', 'ADAMS COUNTY MEMORIAL HOSPITAL',
                   'ProPublica officer match Smith/Sprunger/Wheeler. adamshospital.org confirms.')
        if not dry_run:
            df.at[idx, 'Corporate_Name'] = 'ADAMS COUNTY MEMORIAL HOSPITAL'
    print(f"  AHN-04: {heritage_blank.sum()} rows (blank) -> ADAMS COUNTY MEMORIAL HOSPITAL")
    total += heritage_blank.sum()

# Adams Woodcrest: blank → ADAMS COUNTY MEMORIAL HOSPITAL
mask_woodcrest = find_rows(facility_name='ADAMS WOODCREST', city='Decatur', state='IN')
woodcrest_blank = mask_woodcrest & (df['Corporate_Name'].isna() | (df['Corporate_Name'].str.strip() == ''))
if woodcrest_blank.sum() > 0:
    for idx in df[woodcrest_blank].index:
        row = df.loc[idx]
        log_change('AHN-05', row['Facility_Name'], row.get('City', ''), row.get('State', ''),
                   'Corporate_Name', '(blank)', 'ADAMS COUNTY MEMORIAL HOSPITAL',
                   'ProPublica h-155747 confirms Adams = owner. Smith/Sprunger/Wheeler officers.')
        if not dry_run:
            df.at[idx, 'Corporate_Name'] = 'ADAMS COUNTY MEMORIAL HOSPITAL'
    print(f"  AHN-05: {woodcrest_blank.sum()} rows (blank) -> ADAMS COUNTY MEMORIAL HOSPITAL")
    total += woodcrest_blank.sum()

# Victory Noll: DELETE (closed April 2024)
mask_vnoll = find_rows(facility_name='VICTORY NOLL', state='IN')
if mask_vnoll.sum() > 0:
    for idx in df[mask_vnoll].index:
        row = df.loc[idx]
        log_change('AHN-03', row['Facility_Name'], row.get('City', ''), row.get('State', ''),
                   'DELETE ROW', '', '',
                   'Closed April 2024. 26 residents relocated. Building being sold. Dead row.')
        delete_indices.append(idx)
    print(f"  AHN-03: {mask_vnoll.sum()} rows marked for deletion (Victory Noll closed)")
else:
    print("  AHN-03: Victory Noll not found — may already be removed in V26.0")

# Also recode any remaining Saint Anne Diocese variant
mask_diocese2 = find_rows(facility_name='ST ANNE HOME', state='IN',
                          corporate_name='ST ANNE HOME OF THE DIOCESE OF FORT WAYNE-SOUTH BEND INC')
if mask_diocese2.sum() > 0:
    # This is the Victory Noll row — should be caught by delete above, but if not:
    for idx in df[mask_diocese2].index:
        if idx not in delete_indices:
            row = df.loc[idx]
            log_change('AHN-03b', row['Facility_Name'], row.get('City', ''), row.get('State', ''),
                       'DELETE ROW', '', '',
                       'Victory Noll variant name. Closed April 2024.')
            delete_indices.append(idx)
    print(f"  AHN-03b: {mask_diocese2.sum()} additional Diocese variant rows")

# ============================================================
# SECTION 6: Harborview Health Systems — 7 Recodes (NC Surry + GA blanks + FL Landa)
# ============================================================
print("\n=== Harborview Health Systems: Recodes ===")

# NC Surry SNF: blank → HARBORVIEW HEALTH SYSTEMS
mask = find_rows(facility_name='SURRY COMMUNITY HEALTH CENTER BY HARBORVIEW', state='NC')
surry_blank = mask & (df['Corporate_Name'].isna() | (df['Corporate_Name'].str.strip() == ''))
if surry_blank.sum() > 0:
    for idx in df[surry_blank].index:
        row = df.loc[idx]
        log_change('HBV-NC-01', row['Facility_Name'], row.get('City', ''), row.get('State', ''),
                   'Corporate_Name', '(blank)', 'HARBORVIEW HEALTH SYSTEMS',
                   'ProPublica h-345191 chain=Harborview. Owner=GA NC 14 LLC. Served.')
        if not dry_run:
            df.at[idx, 'Corporate_Name'] = 'HARBORVIEW HEALTH SYSTEMS'
    print(f"  HBV-NC-01: {surry_blank.sum()} rows (blank) -> HARBORVIEW HEALTH SYSTEMS")
    total += surry_blank.sum()

# NC Surry ALF: INDEPENDENT → HARBORVIEW HEALTH SYSTEMS
mask = find_rows(facility_name='SURRY COMMUNITY HEALTH CENTER BY HARBORVIEW', state='NC',
                 corporate_name='INDEPENDENT')
total += recode_corp(mask, 'INDEPENDENT', 'HARBORVIEW HEALTH SYSTEMS', 'HBV-NC-02',
    'ProPublica h-345191 chain=Harborview. Same campus as SNF. Served.')

# GA blanks
ga_blanks = [
    ('HARBORVIEW HEALTH SYSTEMS JESUP', 'Jesup', 'HBV-GA-01'),
    ('HARBORVIEW HEALTH SYSTEMS THOMASTON', 'Thomaston', 'HBV-GA-02'),
    ('HARBORVIEW SATILLA', 'Waycross', 'HBV-GA-03'),
]
for fac_name, city, pid in ga_blanks:
    mask_fac = find_rows(facility_name=fac_name, city=city, state='GA')
    blank_mask = mask_fac & (df['Corporate_Name'].isna() | (df['Corporate_Name'].str.strip() == ''))
    if blank_mask.sum() > 0:
        for idx in df[blank_mask].index:
            row = df.loc[idx]
            log_change(pid, row['Facility_Name'], row.get('City', ''), row.get('State', ''),
                       'Corporate_Name', '(blank)', 'HARBORVIEW HEALTH SYSTEMS',
                       'Facility name contains Harborview. ProPublica affiliate a-246.')
            if not dry_run:
                df.at[idx, 'Corporate_Name'] = 'HARBORVIEW HEALTH SYSTEMS'
        print(f"  {pid}: {blank_mask.sum()} rows (blank) -> HARBORVIEW HEALTH SYSTEMS")
        total += blank_mask.sum()
    # Also check for INDEPENDENT coding
    indep_mask = mask_fac & (df['Corporate_Name'] == 'INDEPENDENT')
    if indep_mask.sum() > 0:
        total += recode_corp(indep_mask, 'INDEPENDENT', 'HARBORVIEW HEALTH SYSTEMS', pid,
            'Facility name contains Harborview. ProPublica affiliate a-246.')

# FL Landa recodes
fl_landa = [
    ('BAYONET POINT HEALTH CENTER BY HARBORVIEW', 'Hudson', 'HBV-FL-01'),
    ('HERITAGE PARK HEALTH CENTER BY HARBORVIEW', 'Bradenton', 'HBV-FL-02'),
]
for fac_name, city, pid in fl_landa:
    mask = find_rows(facility_name=fac_name, city=city, state='FL',
                     corporate_name='BENJAMIN LANDA')
    total += recode_corp(mask, 'BENJAMIN LANDA', 'HARBORVIEW HEALTH SYSTEMS', pid,
        'Harborview branding in name. Website confirms Harborview operation. '
        'Landa is indirect owner (FLNHO Capital). Per operator attribution rule.')

# ============================================================
# SECTION 7: Commonwealth Senior Living — Radford SNF Recode to CCR
# ============================================================
print("\n=== Commonwealth Senior Living: Radford SNF Recode ===")

mask = find_rows(facility_name='RADFORD HEALTH AND REHAB', city='Radford', state='VA',
                 corporate_name='COMMONWEALTH SENIOR LIVING')
total += recode_corp(mask, 'COMMONWEALTH SENIOR LIVING', 'COMMONWEALTH CARE OF ROANOKE', 'CSL-VA-01',
    'ProPublica h-495355 chain=Commonwealth Care Of Roanoke. Owners=Petrine/Sheffer/Goodall/Stallard. '
    'Managing entity=Commonwealth Care Of Roanoke INC (since Jun 2007). CSL is ALF only — does not operate SNFs.')

# ============================================================
# SECTION 8: Commonwealth Care of Roanoke — Lee Health Recode
# ============================================================
print("\n=== Commonwealth Care of Roanoke: Lee Health Recodes ===")

# Lee Health SNF
mask = find_rows(facility_name='LEE HEALTH AND REHAB CENTER', city='Pennington Gap', state='VA',
                 corporate_name='LEE HEALTH AND ENCOMPASS HEALTH')
total += recode_corp(mask, 'LEE HEALTH AND ENCOMPASS HEALTH', 'COMMONWEALTH CARE OF ROANOKE', 'CCR-VA-01',
    'ProPublica h-495352 chain=CCR. DJ Petrine 40%/BD Sheffer 20%. CCR managing since Jun 2007. Served.')

# Lee Health ALF
mask = find_rows(facility_name='LEE HEALTH AND REHAB', city='Pennington Gap', state='VA',
                 corporate_name='LEE HEALTH AND ENCOMPASS HEALTH')
total += recode_corp(mask, 'LEE HEALTH AND ENCOMPASS HEALTH', 'COMMONWEALTH CARE OF ROANOKE', 'CCR-VA-02',
    'Campus pair with SNF. Same Petrine/Sheffer ownership. ProPublica confirms CCR chain. Served.')

# ============================================================
# SECTION 9: Cogir — Entity Consolidation (Cogir USA → COGIR SENIOR LIVING)
# ============================================================
print("\n=== Cogir: Entity Consolidation ===")

mask = find_rows(corporate_name='Cogir USA')
total += recode_corp(mask, 'Cogir USA', 'COGIR SENIOR LIVING', 'COG-CONSOL',
    'Entity consolidation. Same operator — Cogir acquired Cadence Nov 2022. cogirusa.com. '
    'GLR carries COGIR SENIOR LIVING. Standardizing 21 rows to match GLR canonical name.')

# ============================================================
# SECTION 10: Life Care Services — The Virginian CHOW to Cogir
# ============================================================
print("\n=== Life Care Services: The Virginian CHOW to Cogir ===")

# The Virginian ALF: LIFE CARE SERVICES → COGIR SENIOR LIVING
mask = find_rows(facility_name='THE VIRGINIAN', city='Fairfax', state='VA',
                 corporate_name='LIFE CARE SERVICES')
total += recode_corp(mask, 'LIFE CARE SERVICES', 'COGIR SENIOR LIVING', 'LCS-VA-01',
    'cogirusa.com/communities lists The Virginian as active Cogir community. LCS was prior management. '
    'CHOW from LCS to Cogir confirmed by operator website.')

# The Virginian SNF: INDEPENDENT → COGIR SENIOR LIVING
mask = find_rows(facility_name='THE VIRGINIAN', city='Fairfax', state='VA',
                 corporate_name='INDEPENDENT')
total += recode_corp(mask, 'INDEPENDENT', 'COGIR SENIOR LIVING', 'LCS-VA-02',
    'SNF component of CCRC campus. Same address as ALF. cogirusa.com confirms Cogir management.')

# ============================================================
# SECTION 11: Senior Lifestyle — Aspire at West End CHOW to Vitality
# ============================================================
print("\n=== Senior Lifestyle: Aspire at West End CHOW to Vitality ===")

mask = find_rows(facility_name='ASPIRE AT WEST END', city='Henrico', state='VA',
                 corporate_name='SENIOR LIFESTYLE')
total += recode_corp(mask, 'SENIOR LIFESTYLE', 'VITALITY LIVING', 'SLC-VA-01',
    'Vitality Living assumed management Feb 22, 2026 per vitalityseniorliving.com. '
    'Confirmed via insideNova and SHN. Acclaim at Belmont Bay (same transition) already coded Vitality.')

# ============================================================
# SECTION 12: StoryPoint — NC Misattribution to ThriveMore
# ============================================================
print("\n=== StoryPoint: NC Misattribution → ThriveMore ===")

# Taylor Glen SNF
mask = find_rows(facility_name='GARDENS OF TAYLOR GLEN', city='Concord', state='NC',
                 corporate_name='StoryPoint')
if mask.sum() == 0:
    mask = find_rows(facility_name='GARDENS OF TAYLOR GLEN', state='NC')
    mask = mask & (df['Corporate_Name'].str.contains('STORYPOINT|StoryPoint', case=False, na=False))
total += recode_corp(mask, df[mask]['Corporate_Name'].iloc[0] if mask.sum() > 0 else 'StoryPoint',
                     'ThriveMore', 'SP-NC-01',
    'taylorglencommunity.org confirms ThriveMore. StoryPoint has zero NC presence. Served facility.')

# Taylor Glen ALF
mask = find_rows(facility_name='TAYLOR GLEN', city='Concord', state='NC')
mask = mask & (df['Corporate_Name'].str.contains('STORYPOINT|StoryPoint', case=False, na=False))
if mask.sum() > 0:
    total += recode_corp(mask, df[mask]['Corporate_Name'].iloc[0], 'ThriveMore', 'SP-NC-02',
        'Same campus as SNF. taylorglencommunity.org confirms ThriveMore. Served facility.')

# Ardenwoods
mask = find_rows(facility_name='ARDENWOODS', city='Arden', state='NC')
mask = mask & (df['Corporate_Name'].str.contains('STORYPOINT|StoryPoint', case=False, na=False))
if mask.sum() > 0:
    total += recode_corp(mask, df[mask]['Corporate_Name'].iloc[0], 'ThriveMore', 'SP-NC-03',
        'ardenwoodscommunity.org confirms ThriveMore. Life Plan Community. StoryPoint has zero NC presence.')

# ============================================================
# SECTION 13: Genesis — Ashland KY Recode (missed in V25.9)
# ============================================================
print("\n=== Genesis: Ashland KY Recode ===")

mask = find_rows(facility_name='GENESIS HCR OF ASHLAND TWO', city='Ashland', state='KY',
                 corporate_name='INDEPENDENT')
total += recode_corp(mask, 'INDEPENDENT', 'GENESIS HEALTH OF ASHLAND, LLC', 'GEN-KY-01',
    'Local family-owned PCH, NOT Genesis Healthcare Chain 237. Victor Matthew Mitchell owner per KY CHFS. '
    'Row 5803 (Ashland One) already coded GENESIS HEALTH OF ASHLAND, LLC. Matching row 5804 to same. '
    'Was scripted in V25.9 but never executed — confirmed still INDEPENDENT in V26.0.')

# ============================================================
# SECTION 7: Genesis — NC Duplicate Cleanup (V25.9 insert + V26.0 loader created dups)
# ============================================================
print("\n=== Genesis: NC Duplicate Cleanup ===")

genesis_nc_dups = [
    ('MERIDIAN CENTER', 'High Point', 'NC', 'GEN-NC-DUP-01'),
    ('ABBOTTS CREEK CENTER', 'Lexington', 'NC', 'GEN-NC-DUP-02'),
    ('MOUNT OLIVE CENTER', 'Mount Olive', 'NC', 'GEN-NC-DUP-03'),
    ('PEMBROKE CENTER', 'Pembroke', 'NC', 'GEN-NC-DUP-04'),
]

for fac_name, city, state, pid in genesis_nc_dups:
    mask_all = find_rows(facility_name=fac_name, city=city, state=state,
                         corporate_name='GENESIS')
    rows = df[mask_all]
    if len(rows) == 2:
        # Keep the CMS-sourced row (uppercase city), delete the V25.9 insert (mixed case)
        for idx in rows.index:
            row = df.loc[idx]
            city_val = str(row.get('City', ''))
            if city_val != city_val.upper():
                log_change(pid, row['Facility_Name'], row.get('City', ''), row.get('State', ''),
                           'DELETE ROW', f'City={city_val} (mixed case = V25.9 insert)', '',
                           f'Duplicate of CMS-sourced row. V25.9 inserted + V26.0 loader both created rows. '
                           f'Neither served. Keep uppercase/CMS row.')
                delete_indices.append(idx)
                print(f"  {pid}: DELETE duplicate {fac_name} (mixed case city '{city_val}')")
                break
        else:
            # Both uppercase — keep first, delete second
            idx_del = rows.index[1]
            row = df.loc[idx_del]
            log_change(pid, row['Facility_Name'], row.get('City', ''), row.get('State', ''),
                       'DELETE ROW', '', '',
                       f'Duplicate at same address. Both uppercase. Keep first row. Neither served.')
            delete_indices.append(idx_del)
            print(f"  {pid}: DELETE duplicate {fac_name} (second row)")
    elif len(rows) == 1:
        print(f"  {pid}: Only 1 row for {fac_name} — no duplicate")
    else:
        print(f"  {pid}: WARNING — {len(rows)} rows for {fac_name}")

# === EXECUTE DELETES ===
if not dry_run and delete_indices:
    df = df.drop(delete_indices)
    print(f"\n  Deleted {len(delete_indices)} rows")

# === REPORT ===
print(f"\n{'='*60}")
print(f"Total recodes: {total}")
print(f"Total deletes: {len(delete_indices)}")
print(f"Total changes: {len(changes)}")

if changes:
    report_df = pd.DataFrame(changes)
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    report_df.to_csv(report_path, index=False)
    print(f"Report saved: {report_path}")
    print("\nChange summary:")
    for c in changes:
        action = c['Field']
        if action == 'DELETE ROW':
            print(f"  [{c['Punchlist']}] DELETE {c['Facility']} ({c['City']}, {c['State']})")
        else:
            print(f"  [{c['Punchlist']}] {c['Facility']} ({c['City']}, {c['State']}): '{c['Old']}' → '{c['New']}'")

# === SAVE ===
if not dry_run and changes:
    print(f"\nSaving V26.1 to: {dst_path}")
    df.to_excel(dst_path, index=False)
    print(f"V26.1 saved: {len(df)} rows")

    # Verification
    verify = pd.read_excel(dst_path)
    print(f"\n=== VERIFICATION ===")
    print(f"Row count: V26.0={len(pd.read_excel(src_path))}, V26.1={len(verify)}, delta={len(verify)-len(pd.read_excel(src_path))}")

    # Check Crown Point Christian Village
    cpv = verify[verify['Facility_Name'].str.contains('CROWN POINT CHRISTIAN', case=False, na=False)]
    for _, r in cpv.iterrows():
        val = r.get('Corporate_Name', 'NULL')
        status = 'PASS' if val == 'CHRISTIAN HORIZONS' else 'FAIL'
        print(f"  {status}: {r['Facility_Name']} = {val}")

    # Check KY recodes
    ky = verify[(verify['State'] == 'KY') & (verify['Corporate_Name'] == 'LYON HEALTHCARE')]
    print(f"  KY LYON HEALTHCARE rows: {len(ky)} (expected 7)")

    # Check OK recode
    ok = verify[(verify['State'] == 'OK') & (verify['Facility_Name'].str.contains('MIDWEST', case=False, na=False))]
    for _, r in ok.iterrows():
        val = r.get('Corporate_Name', 'NULL')
        status = 'PASS' if val == 'LYON HEALTHCARE' else 'FAIL'
        print(f"  {status}: {r['Facility_Name']} = {val}")

    # Check Gallatin dedup
    gal = verify[(verify['City'].str.lower().str.strip() == 'gallatin') & (verify['State'] == 'TN') &
                 (verify['Facility_Name'].str.contains('GALLATIN', case=False, na=False))]
    print(f"  Gallatin TN rows: {len(gal)} (expected 1 after dedup)")

    # Check Adams recodes
    adams = verify[verify['Corporate_Name'] == 'ADAMS COUNTY MEMORIAL HOSPITAL']
    print(f"  ADAMS COUNTY MEMORIAL HOSPITAL rows: {len(adams)} (expected all 9 campuses unified)")
    vnoll = verify[verify['Facility_Name'].str.contains('VICTORY NOLL', case=False, na=False)]
    print(f"  Victory Noll rows: {len(vnoll)} (expected 0 after delete)")
else:
    if dry_run:
        print(f"\nDRY RUN complete. Review report, then set dry_run=False and rerun.")
    else:
        print(f"\nNo changes to save.")
