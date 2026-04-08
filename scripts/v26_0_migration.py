"""
V26.0 Migration Script
Takes V25.9 as input, applies deferred manual review items.

9 changes: 5 deletes, 2 recodes, 1 corp fill, 1 retype flag.
All HIGH confidence — verified via NC DHSR, NCR website, SHN news.

Author: Roian Atwood / Claude
Date: 2026-04-08
"""
import pandas as pd
import numpy as np
import os
import sys

# === CONFIGURATION ===
dry_run = False  # EXECUTING — approved by Roian Atwood 2026-04-08

src_path = r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V25_9.xlsx"
dst_path = r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V26_0.xlsx"
report_path = "scripts/audit_reports/v26_0_change_report.csv"

# === LOAD ===
print(f"Loading V25.9 from: {src_path}")
df = pd.read_excel(src_path)
print(f"Loaded: {len(df)} rows")

changes = []
all_deletes = []

def log_change(item, facility, city, state, field, old_val, new_val, evidence=""):
    changes.append({
        'Item': item, 'Facility': facility, 'City': city, 'State': state,
        'Field': field, 'Old': old_val, 'New': new_val, 'Evidence': evidence
    })

def find_by_name_city_state(name, city, state, exact=True):
    if exact:
        mask = (df['Facility_Name'] == name) & (df['City'].str.lower().str.strip() == city.lower()) & (df['State'].str.strip() == state)
    else:
        mask = df['Facility_Name'].str.contains(name, case=False, na=False) & (df['City'].str.lower().str.strip() == city.lower()) & (df['State'].str.strip() == state)
    return mask

# ===================================================================
# #6: Hagerstown + Salisbury CSL → VIVA SENIOR LIVING
# ===================================================================
print("\n=== #6: VIVA RECODES ===")

mask_hag = find_by_name_city_state('Viva Memory Care At Hagerstown', 'Hagerstown', 'MD')
if mask_hag.sum() == 1:
    idx = df[mask_hag].index[0]
    old = df.at[idx, 'Corporate_Name']
    log_change('#6', 'Viva Memory Care At Hagerstown', 'Hagerstown', 'MD', 'Corporate_Name', old, 'VIVA SENIOR LIVING', 'Logos/Viva 8-community deal Oct 2024 (SHN)')
    df.at[idx, 'Corporate_Name'] = 'VIVA SENIOR LIVING'
    print(f"  Hagerstown: {old} -> VIVA SENIOR LIVING")
else:
    print(f"  WARNING: Hagerstown match count = {mask_hag.sum()}")

mask_sal = find_by_name_city_state('Commonwealth Senior Living At Salisbury', 'Salisbury', 'MD')
if mask_sal.sum() == 1:
    idx = df[mask_sal].index[0]
    old = df.at[idx, 'Corporate_Name']
    log_change('#6', 'Commonwealth Senior Living At Salisbury', 'Salisbury', 'MD', 'Corporate_Name', old, 'VIVA SENIOR LIVING', 'Same Logos/Viva deal (SHN)')
    df.at[idx, 'Corporate_Name'] = 'VIVA SENIOR LIVING'
    print(f"  Salisbury: {old} -> VIVA SENIOR LIVING")
else:
    print(f"  WARNING: Salisbury match count = {mask_sal.sum()}")

# ===================================================================
# #7: Bel Air + Cockeysville CSL cross-operator dups — DELETE
# ===================================================================
print("\n=== #7: CROSS-OPERATOR DUP DELETES ===")

mask_bel = find_by_name_city_state('Viva Senior Living At Bel Air', 'Bel Air', 'MD')
if mask_bel.sum() == 1:
    idx = df[mask_bel].index[0]
    log_change('#7', df.at[idx, 'Facility_Name'], 'Bel Air', 'MD', 'DELETE ROW', '', '', 'CSL cross-operator dup, Viva row survives')
    all_deletes.append(idx)
    print(f"  DELETE: Bel Air CSL dup (row idx {idx})")
else:
    print(f"  WARNING: Bel Air CSL dup match count = {mask_bel.sum()}")

mask_cock = find_by_name_city_state('Viva Senior Living At Cockeysville', 'Cockeysville', 'MD')
if mask_cock.sum() == 1:
    idx = df[mask_cock].index[0]
    log_change('#7', df.at[idx, 'Facility_Name'], 'Cockeysville', 'MD', 'DELETE ROW', '', '', 'CSL cross-operator dup, Viva row survives')
    all_deletes.append(idx)
    print(f"  DELETE: Cockeysville CSL dup (row idx {idx})")
else:
    print(f"  WARNING: Cockeysville CSL dup match count = {mask_cock.sum()}")

# ===================================================================
# #11: Wake Forest Cogir dup — DELETE 60-bed row
# ===================================================================
print("\n=== #11: WAKE FOREST COGIR DUP ===")

mask_wf = find_by_name_city_state('CADENCE  ASSISTED LIVING OF WAKE FOREST', 'Wake Forest', 'NC')
if mask_wf.sum() == 1:
    idx = df[mask_wf].index[0]
    log_change('#11', df.at[idx, 'Facility_Name'], 'Wake Forest', 'NC', 'DELETE ROW', '', '', 'NC DHSR HAL-092-213: 1 license 96 beds. This row has 60.')
    all_deletes.append(idx)
    print(f"  DELETE: Wake Forest 60-bed dup")
else:
    # Try fuzzy
    mask_wf = df['Facility_Name'].str.contains('CADENCE', case=False, na=False) & \
              df['Facility_Name'].str.contains('WAKE FOREST', case=False, na=False) & \
              (df['Total_Beds'] == 60) & (df['State'] == 'NC')
    if mask_wf.sum() == 1:
        idx = df[mask_wf].index[0]
        log_change('#11', df.at[idx, 'Facility_Name'], 'Wake Forest', 'NC', 'DELETE ROW', '', '', 'NC DHSR: 1 license 96 beds')
        all_deletes.append(idx)
        print(f"  DELETE: Wake Forest 60-bed dup (fuzzy match)")
    else:
        print(f"  WARNING: Wake Forest dup match count = {mask_wf.sum()}")

# ===================================================================
# #12: Garner Cogir dup — DELETE wrong-address row
# ===================================================================
print("\n=== #12: GARNER COGIR DUP ===")

mask_gar = df['Facility_Name'].str.contains('CADENCE', case=False, na=False) & \
           df['Facility_Name'].str.contains('GARNER', case=False, na=False) & \
           df['Address'].str.contains('Aversboro', case=False, na=False) & \
           (df['State'] == 'NC')
if mask_gar.sum() == 1:
    idx = df[mask_gar].index[0]
    log_change('#12', df.at[idx, 'Facility_Name'], 'Garner', 'NC', 'DELETE ROW', '', '', 'NC DHSR HAL-092-215: 1 license 84 beds at 200 Minglewood only. Aversboro is wrong address.')
    all_deletes.append(idx)
    print(f"  DELETE: Garner Aversboro dup")
else:
    print(f"  WARNING: Garner Aversboro dup match count = {mask_gar.sum()}")

# ===================================================================
# #13: Huntersville Cogir dup — DELETE 60-bed row
# ===================================================================
print("\n=== #13: HUNTERSVILLE COGIR DUP ===")

mask_hunt = df['Facility_Name'].str.contains('CADENCE', case=False, na=False) & \
            df['Facility_Name'].str.contains('HUNTERSVILLE', case=False, na=False) & \
            (df['Total_Beds'] == 60) & (df['State'] == 'NC')
if mask_hunt.sum() == 1:
    idx = df[mask_hunt].index[0]
    log_change('#13', df.at[idx, 'Facility_Name'], 'Huntersville', 'NC', 'DELETE ROW', '', '', 'NC DHSR HAL-060-160: 1 license 96 beds. This row has 60.')
    all_deletes.append(idx)
    print(f"  DELETE: Huntersville 60-bed dup")
else:
    print(f"  WARNING: Huntersville dup match count = {mask_hunt.sum()}")

# ===================================================================
# #16: NCR Chillicothe corp name fill
# ===================================================================
print("\n=== #16: NCR CHILLICOTHE CORP FILL ===")

mask_ncr_chil = (df['Facility_Name'] == 'NATIONAL CHURCH RESIDENCES CHILLICOTHE') & (df['State'] == 'OH')
if mask_ncr_chil.sum() == 1:
    idx = df[mask_ncr_chil].index[0]
    old = df.at[idx, 'Corporate_Name'] if pd.notna(df.at[idx, 'Corporate_Name']) else '(NULL)'
    log_change('#16', 'NATIONAL CHURCH RESIDENCES CHILLICOTHE', 'Chillicothe', 'OH', 'Corporate_Name', old, 'NATIONAL CHURCH RESIDENCES', 'CMS CCN 366338, same campus as ALF row')
    df.at[idx, 'Corporate_Name'] = 'NATIONAL CHURCH RESIDENCES'
    print(f"  Fill: {old} -> NATIONAL CHURCH RESIDENCES")
else:
    print(f"  WARNING: NCR Chillicothe match count = {mask_ncr_chil.sum()}")

# ===================================================================
# #17: Hopeton Village dup — DELETE name variant
# ===================================================================
print("\n=== #17: HOPETON VILLAGE DUP ===")

mask_hop = (df['Facility_Name'] == 'NATIONAL CHURCH RESIDENCES AT HOPETON VILLAGE') & (df['State'] == 'OH')
if mask_hop.sum() == 1:
    idx = df[mask_hop].index[0]
    log_change('#17', df.at[idx, 'Facility_Name'], 'Chillicothe', 'OH', 'DELETE ROW', '', '', 'Name variant dup of NCR HOPETON VILLAGE at same address (153 University Dr)')
    all_deletes.append(idx)
    print(f"  DELETE: NCR AT HOPETON VILLAGE (name variant dup)")
else:
    print(f"  WARNING: Hopeton Village dup match count = {mask_hop.sum()}")

# #17b: Hopeton Terrace — flag as ILF (affordable housing, not serviceable)
print("\n=== #17b: HOPETON TERRACE RETYPE ===")

mask_terr = (df['Facility_Name'] == 'HOPETON TERRACE') & (df['State'] == 'OH')
if mask_terr.sum() == 1:
    idx = df[mask_terr].index[0]
    old_type = df.at[idx, 'Source_Type']
    log_change('#17b', 'HOPETON TERRACE', 'Chillicothe', 'OH', 'Source_Type', old_type, 'ILF', 'HUD-subsidized affordable housing 62+, 45 units, 55 Sun Rush Blvd. Not serviceable.')
    df.at[idx, 'Source_Type'] = 'ILF'
    print(f"  Retype: {old_type} -> ILF (affordable housing)")
else:
    print(f"  WARNING: Hopeton Terrace match count = {mask_terr.sum()}")

# ===================================================================
# APPLY DELETES
# ===================================================================
all_deletes = list(set(all_deletes))
print(f"\n=== APPLYING {len(all_deletes)} DELETES ===")
if all_deletes:
    df = df.drop(all_deletes).reset_index(drop=True)
    print(f"  Deleted {len(all_deletes)} rows")

# ===================================================================
# SUMMARY + SAVE
# ===================================================================
print(f"\n=== CHANGE SUMMARY ===")
print(f"Total changes: {len(changes)}")
print(f"Deletes: {len(all_deletes)}")
print(f"Recodes: 2 (Hagerstown + Salisbury)")
print(f"Corp fills: 1 (NCR Chillicothe)")
print(f"Retypes: 1 (Hopeton Terrace ALF -> ILF)")
print(f"Final row count: {len(df)}")
print(f"Expected: {25503 - len(all_deletes)}")

assert len(df) == 25503 - len(all_deletes), f"Row count mismatch!"

# Save report
pd.DataFrame(changes).to_csv(report_path, index=False)
print(f"\nChange report: {report_path}")

# Save Excel
df.to_excel(dst_path, index=False)
print(f"V26.0 saved to: {dst_path}")
