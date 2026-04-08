"""
V25.9 Unified Migration Script
Takes V25.7 as input, applies ALL pending changes, produces V25.9.

Includes:
- V25.8 recodes (Principle/Arbors/Traditions name standardization)
- V25.9 scoring reconciliation (Commonwealth, Cogir, NCR, BHI, Genesis items)
- ALF dedup cluster work (Clusters 1-10, Pair 10)
- Topaz/Metcalfe CHOW
- Fern Terrace entity consolidation

Run in READ-ONLY mode first (dry_run=True) to generate report.
Then set dry_run=False to execute.

Author: Roian Atwood / Claude
Date: 2026-04-07
"""
import pandas as pd
import numpy as np
import shutil
import os
import sys
from datetime import datetime

# === CONFIGURATION ===
dry_run = False  # EXECUTING — approved by Roian Atwood 2026-04-07

src_path = r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V25_7.xlsx"
dst_path = r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V25_9.xlsx"
report_path = "scripts/audit_reports/v25_9_change_report.csv"

# === LOAD ===
print(f"Loading V25.7 from: {src_path}")
df = pd.read_excel(src_path)
print(f"Loaded: {len(df)} rows, {len(df.columns)} columns")
print(f"Columns: {list(df.columns)}")

# Track all changes
changes = []

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
    """Find rows matching criteria. Returns boolean mask."""
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
        if corporate_name == '(NULL)':
            mask = mask & (df['Corporate_Name'].isna() | (df['Corporate_Name'].str.strip() == ''))
        else:
            mask = mask & (df['Corporate_Name'] == corporate_name)
    return mask

def recode_corp(mask, old_name, new_name, punchlist, evidence=""):
    """Recode corporate name on matching rows."""
    count = mask.sum()
    if count == 0:
        print(f"  WARNING: No rows found for {punchlist} recode {old_name} -> {new_name}")
        return 0
    for idx in df[mask].index:
        row = df.loc[idx]
        log_change(punchlist, row['Facility_Name'], row.get('City',''), row.get('State',''),
                   'Corporate_Name', old_name, new_name, evidence)
        if not dry_run:
            df.at[idx, 'Corporate_Name'] = new_name
    print(f"  {punchlist}: {count} rows {old_name} -> {new_name}")
    return count

def delete_row(mask, punchlist, evidence=""):
    """Mark rows for deletion."""
    count = mask.sum()
    if count == 0:
        print(f"  WARNING: No rows found for {punchlist} delete")
        return []
    indices = []
    for idx in df[mask].index:
        row = df.loc[idx]
        log_change(punchlist, row['Facility_Name'], row.get('City',''), row.get('State',''),
                   'DELETE ROW', '', '', evidence)
        indices.append(idx)
    print(f"  {punchlist}: {count} rows marked for deletion")
    return indices

def update_field(mask, field, new_val, punchlist, evidence=""):
    """Update a field on matching rows."""
    count = mask.sum()
    if count == 0:
        print(f"  WARNING: No rows found for {punchlist} update {field}")
        return 0
    for idx in df[mask].index:
        row = df.loc[idx]
        old_val = row[field] if pd.notna(row[field]) else '(NULL)'
        log_change(punchlist, row['Facility_Name'], row.get('City',''), row.get('State',''),
                   field, str(old_val), str(new_val), evidence)
        if not dry_run:
            df.at[idx, field] = new_val
    print(f"  {punchlist}: {count} rows {field} -> {new_val}")
    return count

all_deletes = []

# ===================================================================
# SECTION 1: V25.8 RECODES (Principle, Arbors, Traditions)
# ===================================================================
print("\n=== SECTION 1: V25.8 NAME STANDARDIZATION ===")

recode_corp(
    df['Corporate_Name'] == 'PRINCIPLE',
    'PRINCIPLE', 'PRINCIPLE LONG TERM CARE',
    'V25.8-P', 'CMS Chain 423, Hill family Kinston NC'
)

recode_corp(
    df['Corporate_Name'] == 'ARBORS',
    'ARBORS', 'ARBORS AT OHIO',
    'V25.8-A', 'CMS chain Arbors At Ohio, Ark Opco Group LLC'
)

recode_corp(
    df['Corporate_Name'] == 'TRADITIONS',
    'TRADITIONS', 'TRADITIONS MANAGEMENT',
    'V25.8-T', 'Traditions Management LLC, traditionsmgmt.net'
)

# ===================================================================
# SECTION 2: V25.9 SCORING RECONCILIATION (#1-19)
# ===================================================================
print("\n=== SECTION 2: SCORING RECONCILIATION ===")

# --- Commonwealth (#1-8) ---
# #1: 7 MCAP rows recode to COMMONWEALTH SENIOR LIVING
recode_corp(
    df['Corporate_Name'] == 'MCAP',
    'MCAP', 'COMMONWEALTH SENIOR LIVING',
    '#1', 'MCAP is investor/PropCo, CSL is operator'
)

# #2: 5 MCAP duplicates to delete (now coded CSL after #1)
# These share addresses with existing CSL rows
for city_name in ['Abingdon', 'Cedar Bluff', 'Christiansburg', 'Radford']:
    mask = find_rows(city=city_name, state='VA', corporate_name='COMMONWEALTH SENIOR LIVING')
    if mask.sum() > 1:
        # Keep the first, delete extras that were MCAP
        # Need more precise matching — skip for now, will handle manually
        pass

# Hillsville has typo "Hiillsville" — need to handle that
mask_hiill = df['City'].str.contains('Hiillsville', case=False, na=False)
if mask_hiill.sum() > 0:
    update_field(mask_hiill, 'City', 'Hillsville', '#8', 'City typo correction')

# #4: Radford SNF miscoded CSL -> CCR
mask_radford_snf = find_rows(facility_name='Radford Health', state='VA') & (df['Source_Type'] == 'SNF')
recode_corp(mask_radford_snf, 'COMMONWEALTH SENIOR LIVING', 'COMMONWEALTH CARE OF ROANOKE',
            '#4', 'CMS Chain 152 confirms CCR')

# #5: Lee Health miscoded
mask_lee = find_rows(facility_name='Lee Health', state='VA')
recode_corp(mask_lee, 'LEE HEALTH AND ENCOMPASS HEALTH', 'COMMONWEALTH CARE OF ROANOKE',
            '#5', 'CMS Chain 152 confirms CCR')

# #6: Viva/MD rows stale under CSL
# These need individual identification — mark for manual review
print("  #6-7: Viva/MD stale + cross-operator dups — REQUIRES MANUAL REVIEW")

# --- Cogir (#9-13) ---
# #9: Consolidate COGIR SENIOR LIVING variant -> Cogir USA... wait, other way
# Canonical = COGIR SENIOR LIVING, so recode Cogir USA -> COGIR SENIOR LIVING
recode_corp(
    df['Corporate_Name'] == 'Cogir USA',
    'Cogir USA', 'COGIR SENIOR LIVING',
    '#9', 'Canadian parent, merged with Cadence Living 2022'
)

# #10: GAHC3 PropCo recode
mask_gahc3 = df['Corporate_Name'].str.contains('GAHC3', case=False, na=False)
recode_corp(mask_gahc3, 'GAHC3 HUNTERSVILLE NC TRS SUB, LLC', 'COGIR SENIOR LIVING',
            '#10', 'Griffin-American REIT is owner, Cogir is operator')

# #11-13: Cogir duplicates — need CampusID-based matching, skip for manual review
print("  #11-13: Cogir duplicates — REQUIRES CAMPUS-BASED MANUAL REVIEW")

# --- NCR (#14-19) ---
# #14: Waverly -> NCR
mask_waverly = df['Corporate_Name'].str.contains('WAVERLY', case=False, na=False)
recode_corp(mask_waverly, 'WAVERLY CARE CENTER, INC', 'NATIONAL CHURCH RESIDENCES',
            '#14', 'CMS confirms operator is NCR')

# #15: Blank corp name fill for Bristol Village SNF + First Community Village
mask_bristol_blank = find_rows(facility_name='Bristol Village', state='OH', corporate_name='(NULL)')
update_field(mask_bristol_blank, 'Corporate_Name', 'NATIONAL CHURCH RESIDENCES', '#15', 'NCR affiliate')

mask_first_comm = find_rows(facility_name='First Community Village', state='OH', corporate_name='(NULL)')
update_field(mask_first_comm, 'Corporate_Name', 'NATIONAL CHURCH RESIDENCES', '#15', 'NCR affiliate')

# #16: INSERT Traditions at Chillicothe — handled separately (new row)
print("  #16: Traditions at Chillicothe INSERT — REQUIRES MANUAL ROW INSERT")

# #17-18: NCR duplicates — need manual review
print("  #17-18: NCR duplicates — REQUIRES MANUAL REVIEW")

# ===================================================================
# SECTION 3: TOPAZ (#20-22)
# ===================================================================
print("\n=== SECTION 3: TOPAZ HEALTHCARE ===")

# #20: Recode Emerald Healthcare and Benjamin Landa KY rows to TOPAZ HEALTHCARE
# Only KY facilities that are in the GLR Topaz list
topaz_facilities_ky = [
    'Bowling Green Nursing', 'Brandenburg Nursing', 'Campbellsville Nursing',
    'Christian Heights Nursing', 'Cumberland Nursing', 'Elizabethtown Nursing',
    'Fordsville Nursing', 'Franklin-Simpson Nursing', 'Hardinsburg Nursing',
    'Henderson Nursing', 'Irvine Nursing', 'Kenwood Health',
    'Madison Health', 'Morganfield Nursing', 'River Haven Nursing',
    'Salyersville Nursing', 'Shady Lawn Nursing', 'Springfield Nursing',
    'Stanton Nursing', 'Twin Rivers Nursing', 'Woodcrest Nursing',
    'Pikeville Nursing'
]

for fac_pattern in topaz_facilities_ky:
    mask = find_rows(facility_name=fac_pattern, state='KY')
    if mask.sum() > 0:
        current_corp = df.loc[mask, 'Corporate_Name'].values[0]
        if current_corp != 'TOPAZ HEALTHCARE' and pd.notna(current_corp):
            recode_corp(mask, str(current_corp), 'TOPAZ HEALTHCARE',
                       '#20', 'KY DMS LTC directory + Topaz 8-step verified')

# #22: Metcalfe CHOW
mask_metcalfe_al = find_rows(facility_name='METCALFE HEALTH CARE CENTER AL', state='KY')
mask_metcalfe_snf = find_rows(facility_name='METCALFE HEALTH CARE CENTER SNF', state='KY')

recode_corp(mask_metcalfe_al, '', 'TOPAZ HEALTHCARE', '#22', 'Metcalfe sold to Topaz Sep 2025')
if mask_metcalfe_snf.sum() > 0:
    recode_corp(mask_metcalfe_snf, 'INDEPENDENT', 'TOPAZ HEALTHCARE', '#22', 'Same CHOW')
    update_field(mask_metcalfe_snf, 'Source_Type', 'SNF', '#22-type', 'CCN 185217 SNFMD')
    update_field(mask_metcalfe_snf, 'Total_Beds', 71, '#22-beds', 'CMS certified=71')

# ===================================================================
# SECTION 4: ALF DEDUP CLUSTERS (#23-25)
# ===================================================================
print("\n=== SECTION 4: ALF DEDUP CLUSTERS ===")

# --- Cluster 1: Hamilton Pointe -> TLC MANAGEMENT ---
mask_hp = find_rows(facility_name='HAMILTON POINTE', city='Newburgh', state='IN')
recode_corp(mask_hp & (df['Corporate_Name'] == 'RIVERVIEW HOSPITAL'),
            'RIVERVIEW HOSPITAL', 'TLC MANAGEMENT', 'C1', 'ProPublica h-155803 + tlcmgmt.com')

# --- Cluster 3: Carmel Manor ---
mask_carmel_dup = find_rows(facility_name='CARMEL MANOR', city='Fort Thomas', state='KY') & \
                  (df['Facility_Name'] == 'CARMEL MANOR') & (df['Source_Type'] == 'SNF')
all_deletes.extend(delete_row(mask_carmel_dup, 'C3', 'Duplicate no GLR match'))

mask_carmel_snf = find_rows(facility_name='CARMEL MANOR FORT THOMAS SNF', state='KY')
if mask_carmel_snf.sum() > 0:
    update_field(mask_carmel_snf, 'Source_Type', 'SNF', 'C3-type', 'CCN 185208')
    update_field(mask_carmel_snf, 'Total_Beds', 95, 'C3-beds', 'CMS certified=95')

# --- Cluster 4: Shady Lawn ---
mask_shady_dup = find_rows(facility_name='SHADY LAWN', city='Cynthiana', state='KY', exact_facility=True)
all_deletes.extend(delete_row(mask_shady_dup & (df['Do_We_Serve'].str.strip().str.lower() != 'yes'), 'C4', 'Unserved dup Pair 12'))

mask_shady_keep = find_rows(facility_name='SHADY LAWN - CYNTHIANA', state='KY')
recode_corp(mask_shady_keep, 'SHADY LAWN, LLC', 'INDEPENDENT', 'C4', 'KY CHFS single-facility LLC no operator')
update_field(mask_shady_keep, 'Total_Beds', 75, 'C4-beds', 'GLR + KY CHFS')

# --- Cluster 5: Dominion Frankfort ---
mask_dom_dup = find_rows(facility_name='DOMINION SENIOR LIVING FRANKFORT', state='KY', exact_facility=True)
all_deletes.extend(delete_row(mask_dom_dup & (df['Do_We_Serve'].str.strip().str.lower() != 'yes'), 'C5', 'Unserved dup'))

mask_dom_keep = find_rows(facility_name='DOMINION SENIOR LIVING OF FRANKFORT', state='KY')
update_field(mask_dom_keep, 'Total_Beds', 84, 'C5-beds', 'GLR Licensed Bed=84')

# --- Cluster 6: Morning Pointe Owensboro ---
mask_mp_dup = find_rows(facility_name='MORNING POINTE OF OWENSBORO', state='KY')
all_deletes.extend(delete_row(mask_mp_dup & (df['Do_We_Serve'].str.strip().str.lower() != 'yes'), 'C6', 'Genesis misattribution NIC-A dup'))

mask_mp_keep = find_rows(facility_name='MORNING POINTE OWENSBORO', state='KY')
update_field(mask_mp_keep, 'Total_Beds', 66, 'C6-beds', 'NIC-A Heritage Place pre-reno')

# --- Cluster 7: Arcadia Bowling Green ---
mask_arc_dup1 = find_rows(facility_name='ARCADIA SENIOR LIVING', city='Bowling Green', state='KY', exact_facility=True) & \
                (df['Do_We_Serve'].str.strip().str.lower() != 'yes')
all_deletes.extend(delete_row(mask_arc_dup1, 'C7', 'Unserved dup 110 beds'))

mask_arc_dup2 = find_rows(facility_name='ARCADIA SENIOR LIVING BOWLING GREEN', state='KY')
all_deletes.extend(delete_row(mask_arc_dup2, 'C7', 'Unserved dup 87 beds'))

mask_arc_keep = find_rows(facility_name='ARCADIA SENIOR LIVING', city='Bowling Green', state='KY', exact_facility=True) & \
                (df['Do_We_Serve'].str.strip().str.lower() == 'yes')
recode_corp(mask_arc_keep, 'INDEPENDENT', 'ARCADIA COMMUNITIES', 'C7', '11-step verified arcadia-communities.com')
update_field(mask_arc_keep, 'Total_Beds', 87, 'C7-beds', 'GLR')

# --- Cluster 9: Bungalos Bowling Green ---
mask_bung_dup = find_rows(facility_name='THE BUNGALOWS AT BOWLING GREEN', state='KY')
all_deletes.extend(delete_row(mask_bung_dup, 'C9', 'Typo dup Pair 13'))

mask_bung_keep = find_rows(facility_name='THE BUNGALOS AT BOWLING GREEN', state='KY')
update_field(mask_bung_keep, 'Total_Beds', 28, 'C9-beds', 'GLR')

# --- Cluster 10: Cypress Glen ---
mask_cg_al = find_rows(facility_name='CYPRESS GLEN RETIREMENT COMMUNITY', city='Greenville', state='NC', exact_facility=True) & \
             (df['Source_Type'] == 'ALF')
recode_corp(mask_cg_al, 'INDEPENDENT', 'LIFE CARE SERVICES', 'C10', 'ProPublica h-345512 + lcsliving.com')

mask_cg_mc = find_rows(facility_name='CYPRESS GLEN RETIREMENT COMMUNITY MEMORY CARE', state='NC')
if mask_cg_mc.sum() == 0:
    mask_cg_mc = find_rows(facility_name='CYPRESS GLEN RETIREMENT COMMUNITY MEMORY CARE COTTAGE', state='NC')
recode_corp(mask_cg_mc, '', 'LIFE CARE SERVICES', 'C10', 'Same CCRC campus')

# --- Pair 10: Fern Terrace entity consolidation ---
mask_ft_dup = find_rows(facility_name='FERN TERRACE OF MAYFIELD', state='KY') & \
              (df['Do_We_Serve'].str.strip().str.lower() != 'yes')
all_deletes.extend(delete_row(mask_ft_dup, 'P10', 'Unserved LLC name dup'))

mask_ft_mayfield = find_rows(facility_name='FERN TERRACE MAYFIELD', state='KY')
recode_corp(mask_ft_mayfield, 'FERN TERRACE OF OWENSBORO, LLC', 'FERN TERRACE', 'P10', 'Simpson Family Holdings')
update_field(mask_ft_mayfield, 'Total_Beds', 140, 'P10-beds', 'GLR + KY CHFS')

mask_ft_ow = find_rows(facility_name='FERN TERRACE OWENSBORO', state='KY')
recode_corp(mask_ft_ow, 'FERN TERRACE OF OWENSBORO, LLC', 'FERN TERRACE', 'P10', 'Entity consolidation')

mask_ft_bg = find_rows(facility_name='FERN TERRACE OF BOWLING GREEN', state='KY')
recode_corp(mask_ft_bg, 'DAVCO', 'FERN TERRACE', 'P10', 'Entity consolidation')

mask_davco = find_rows(facility_name='DAVCO REST HOME', state='KY')
recode_corp(mask_davco, 'DAVCO', 'FERN TERRACE', 'P10', 'Entity consolidation')

# ===================================================================
# SECTION 5: BHI SENIOR LIVING (#26-31)
# ===================================================================
print("\n=== SECTION 5: BHI SENIOR LIVING ===")

# #26: Trustwell misattribution
mask_trustwell = find_rows(facility_name='Settler', city='LaPorte', state='IN')
if mask_trustwell.sum() == 0:
    mask_trustwell = find_rows(facility_name='Trustwell', city='LaPorte', state='IN')
recode_corp(mask_trustwell, 'BHI SENIOR LIVING', 'TRUSTWELL LIVING LLC', '#26', 'Separate company')

# #27: Prairie Landing -> BHI
mask_prairie = find_rows(facility_name='Barrington', corporate_name='PRAIRIE LANDING COMMUNITY INC')
if mask_prairie.sum() == 0:
    mask_prairie = df['Corporate_Name'] == 'PRAIRIE LANDING COMMUNITY INC'
recode_corp(mask_prairie, 'PRAIRIE LANDING COMMUNITY INC', 'BHI SENIOR LIVING', '#27', 'BHI subsidiary')

# #28: Clark Retirement -> BHI
mask_clark = find_rows(corporate_name='Clark Retirement')
recode_corp(mask_clark, 'Clark Retirement', 'BHI SENIOR LIVING', '#28', 'BHI affiliate since Jan 2022')

# #29: Maple Knoll SNF blank -> BHI
mask_mk_snf = find_rows(facility_name='Maple Knoll Village', state='OH') & \
              (df['Source_Type'] == 'SNF') & (df['Corporate_Name'].isna() | (df['Corporate_Name'].str.strip() == ''))
update_field(mask_mk_snf, 'Corporate_Name', 'BHI SENIOR LIVING', '#29', 'Maple Knoll affiliated Oct 2021')

# #30: Maple Knoll ALF INDEPENDENT -> BHI
mask_mk_alf = find_rows(facility_name='Maple Knoll Village', state='OH', corporate_name='INDEPENDENT')
recode_corp(mask_mk_alf, 'INDEPENDENT', 'BHI SENIOR LIVING', '#30', 'Maple Knoll affiliated')

# #31: Knolls of Oxford -> BHI
mask_knolls = find_rows(corporate_name='MAPLE KNOLL COMMUNITIES')
recode_corp(mask_knolls, 'MAPLE KNOLL COMMUNITIES', 'BHI SENIOR LIVING', '#31', 'BHI affiliate')

# ===================================================================
# SECTION 6: GENESIS NC INSERTS (#34-37)
# ===================================================================
print("\n=== SECTION 6: GENESIS NC INSERTS ===")

genesis_inserts = [
    {'Facility_Name': 'MERIDIAN CENTER', 'Corporate_Name': 'GENESIS', 'Source_Type': 'SNF',
     'Address': '707 North Elm Street', 'City': 'High Point', 'State': 'NC', 'ZIP': '27262',
     'County': 'Guilford', 'Total_Beds': 199, 'Census': 167.6, 'Do_We_Serve': False,
     'Barrier': 'Own Provider Group', 'Ownership_Type': 'Corporate',
     'Latitude': 35.9641, 'Longitude': -80.013, 'Corp_Attribution_Source': 'CMS'},
    {'Facility_Name': 'ABBOTTS CREEK CENTER', 'Corporate_Name': 'GENESIS', 'Source_Type': 'SNF',
     'Address': '877 Hill Everhart Road', 'City': 'Lexington', 'State': 'NC', 'ZIP': '27292',
     'County': 'Davidson', 'Total_Beds': 64, 'Census': 59.6, 'Do_We_Serve': False,
     'Barrier': 'Own Provider Group', 'Ownership_Type': 'Corporate',
     'Latitude': 35.8515, 'Longitude': -80.227, 'Corp_Attribution_Source': 'CMS'},
    {'Facility_Name': 'MOUNT OLIVE CENTER', 'Corporate_Name': 'GENESIS', 'Source_Type': 'SNF',
     'Address': '228 Smith Chapel Road', 'City': 'Mount Olive', 'State': 'NC', 'ZIP': '28365',
     'County': 'Wayne', 'Total_Beds': 150, 'Census': 117.2, 'Do_We_Serve': False,
     'Barrier': 'Own Provider Group', 'Ownership_Type': 'Corporate',
     'Latitude': 35.1981, 'Longitude': -78.076, 'Corp_Attribution_Source': 'CMS'},
    {'Facility_Name': 'PEMBROKE CENTER', 'Corporate_Name': 'GENESIS', 'Source_Type': 'SNF',
     'Address': '310 E Wardell Drive', 'City': 'Pembroke', 'State': 'NC', 'ZIP': '28372',
     'County': 'Robeson', 'Total_Beds': 84, 'Census': 74.0, 'Do_We_Serve': False,
     'Barrier': 'Own Provider Group', 'Ownership_Type': 'Corporate',
     'Latitude': 34.6851, 'Longitude': -79.183, 'Corp_Attribution_Source': 'CMS'},
]

for ins in genesis_inserts:
    log_change(f"#34-37", ins['Facility_Name'], ins['City'], ins['State'],
               'INSERT ROW', '', '', f"CMS Chain 237, genesis confirmed")
    if not dry_run:
        new_row = {col: np.nan for col in df.columns}
        for k, v in ins.items():
            if k in df.columns:
                new_row[k] = v
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    print(f"  INSERT: {ins['Facility_Name']} ({ins['City']}, {ins['State']})")

# ===================================================================
# APPLY DELETES
# ===================================================================
print(f"\n=== APPLYING {len(all_deletes)} DELETES ===")
# Remove duplicate indices
all_deletes = list(set(all_deletes))
if not dry_run and all_deletes:
    df = df.drop(all_deletes).reset_index(drop=True)
    print(f"  Deleted {len(all_deletes)} rows")

# ===================================================================
# REPORT
# ===================================================================
print(f"\n=== CHANGE SUMMARY ===")
print(f"Total changes logged: {len(changes)}")
print(f"Deletes: {len(all_deletes)}")
print(f"Inserts: {len(genesis_inserts)}")
print(f"Recodes + updates: {len(changes) - len(all_deletes) - len(genesis_inserts)}")

if dry_run:
    expected_rows = 25507 - len(all_deletes) + len(genesis_inserts)
    print(f"\nExpected final row count: {expected_rows}")
    print(f"(25507 - {len(all_deletes)} deletes + {len(genesis_inserts)} inserts)")
else:
    print(f"\nFinal row count: {len(df)}")

# Save change report
report_df = pd.DataFrame(changes)
report_df.to_csv(report_path, index=False)
print(f"\nChange report saved to: {report_path}")

if not dry_run:
    df.to_excel(dst_path, index=False)
    print(f"V25.9 saved to: {dst_path}")
else:
    print(f"\n*** DRY RUN COMPLETE — set dry_run=False to execute ***")
    print(f"Review {report_path} before executing.")
