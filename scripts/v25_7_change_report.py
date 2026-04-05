"""Generate V25.7 change report — read-only, no modifications to DB."""
import pandas as pd

db_path = r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V25_6.xlsx"
df = pd.read_excel(db_path)
print(f"Loaded {len(df)} rows from V25.6")

changes = []

# === RECODE 1: Brookdale Ohio 9 ALFs (#21) ===
brookdale_names = [
    "BROOKDALE ALLIANCE", "BROOKDALE BEAVERCREEK", "BROOKDALE CAMELOT MEDINA",
    "BROOKDALE CENTENNIAL PARK", "BROOKDALE GREENVILLE", "BROOKDALE LAKEVIEW CROSSING",
    "BROOKDALE SPRINGDALE ASSISTED LIVING", "BROOKDALE SPRINGDALE MEMORY CARE",
    "BROOKDALE TRILLIUM CROSSING"
]
mask = df["Facility_Name"].isin(brookdale_names) & (df["State"] == "OH")
for idx in df[mask].index:
    row = df.loc[idx]
    changes.append({
        "Punchlist": "#21", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
        "City": row["City"], "State": row["State"],
        "Field": "Corporate_Name", "Current": row["Corporate_Name"],
        "New": "BROOKDALE SENIOR LIVING"
    })
# Lakeview Crossing Do_We_Serve
mask_lv = (df["Facility_Name"] == "BROOKDALE LAKEVIEW CROSSING") & (df["State"] == "OH")
for idx in df[mask_lv].index:
    row = df.loc[idx]
    changes.append({
        "Punchlist": "#21", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
        "City": row["City"], "State": row["State"],
        "Field": "Do_We_Serve", "Current": str(row["Do_We_Serve"]),
        "New": "Yes"
    })

# === RECODE 2: Majestic/Bluegrass (#27) ===
# KY: MAJESTIC CARE + DAVID MARX -> MAJESTIC / BLUEGRASS CONSULTING GROUP
mask_ky = ((df["Corporate_Name"] == "MAJESTIC CARE") | (df["Corporate_Name"] == "DAVID MARX")) & (df["State"] == "KY")
for idx in df[mask_ky].index:
    row = df.loc[idx]
    changes.append({
        "Punchlist": "#27", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
        "City": row["City"], "State": row["State"],
        "Field": "Corporate_Name", "Current": row["Corporate_Name"],
        "New": "MAJESTIC / BLUEGRASS CONSULTING GROUP"
    })
# Non-KY MAJESTIC CARE -> MAJESTIC / MAJESTIC CARE
mask_nonky = (df["Corporate_Name"] == "MAJESTIC CARE") & (df["State"] != "KY")
for idx in df[mask_nonky].index:
    row = df.loc[idx]
    changes.append({
        "Punchlist": "#27", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
        "City": row["City"], "State": row["State"],
        "Field": "Corporate_Name", "Current": row["Corporate_Name"],
        "New": "MAJESTIC / MAJESTIC CARE"
    })
# MAJESTIC MANAGEMENT variants
mask_mgmt = df["Corporate_Name"].str.contains("MAJESTIC MANAGEMENT", na=False, case=False)
for idx in df[mask_mgmt].index:
    row = df.loc[idx]
    changes.append({
        "Punchlist": "#27", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
        "City": row["City"], "State": row["State"],
        "Field": "Corporate_Name", "Current": row["Corporate_Name"],
        "New": "MAJESTIC / MAJESTIC CARE"
    })

# === RECODE 3: McCoy/Carlyle (#24) ===
mask_mccoy = df["Facility_Name"].str.contains("MCCOY MEMORIAL", na=False, case=False)
for idx in df[mask_mccoy].index:
    row = df.loc[idx]
    if "CONCIERGE" in str(row["Corporate_Name"]).upper():
        changes.append({
            "Punchlist": "#24", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
            "City": row["City"], "State": row["State"],
            "Field": "Corporate_Name", "Current": row["Corporate_Name"],
            "New": "CARLYLE SENIOR CARE"
        })

# === RECODE 4: Elkhorn/Lyon (#22) ===
mask_elk = df["Facility_Name"].str.contains("ELKHORN", na=False, case=False) & (df["State"] == "KY")
for idx in df[mask_elk].index:
    row = df.loc[idx]
    corp = str(row["Corporate_Name"]).upper()
    if "A&M" in corp or "A & M" in corp or "A&M" in corp:
        changes.append({
            "Punchlist": "#22", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
            "City": row["City"], "State": row["State"],
            "Field": "Corporate_Name", "Current": row["Corporate_Name"],
            "New": "LYON HEALTHCARE"
        })

# === RECODE 5: Harmony Elkhart (#13) ===
mask_elkhart = df["Corporate_Name"].str.contains("ELKHART AL INVESTORS", na=False, case=False)
for idx in df[mask_elkhart].index:
    row = df.loc[idx]
    changes.append({
        "Punchlist": "#13", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
        "City": row["City"], "State": row["State"],
        "Field": "Corporate_Name", "Current": row["Corporate_Name"],
        "New": "HARMONY SENIOR SERVICES"
    })

# === RECODE 6: Harmony Hall Kinston (#14) ===
mask_hh = df["City"].str.contains("KINSTON", na=False, case=False) & df["Facility_Name"].str.contains("HARMONY HALL", na=False, case=False)
for idx in df[mask_hh].index:
    row = df.loc[idx]
    src = str(row["Source_Type"]).upper()
    beds = row["Total_Beds"] if pd.notna(row["Total_Beds"]) else 0
    if src == "ALF" or beds <= 60:
        changes.append({
            "Punchlist": "#14", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
            "City": row["City"], "State": row["State"],
            "Field": "DELETE ROW", "Current": f"Type={row['Source_Type']}, Beds={beds}, Corp={row['Corporate_Name']}",
            "New": "PHANTOM - no NC DHSR ALF license at 312 Warren Ave"
        })
    else:
        changes.append({
            "Punchlist": "#14", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
            "City": row["City"], "State": row["State"],
            "Field": "Corporate_Name", "Current": row["Corporate_Name"],
            "New": "PRINCIPLE LONG TERM CARE"
        })

# === RECODE 7: Camellia Gardens (#18) ===
mask_cam = df["Facility_Name"].str.contains("CAMELLIA GARDENS", na=False, case=False) & df["Corporate_Name"].str.contains("PELICAN", na=False, case=False)
for idx in df[mask_cam].index:
    row = df.loc[idx]
    changes.append({
        "Punchlist": "#18", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
        "City": row["City"], "State": row["State"],
        "Field": "Corporate_Name", "Current": row["Corporate_Name"],
        "New": "ALLIANCE HEALTH GROUP"
    })

# === RECODE 8: Putnam County Hospital multi-operator (#23) ===
pch_facilities = {
    "RICHLAND BEAN": "HUTSONWOOD",
    "HUTSONWOOD": "HUTSONWOOD",
    "TOWNE PARK": "HUTSONWOOD",
    "MILL POND": "TRILOGY HEALTH SERVICES",
    "COBBLESTONE CROSSING": "TRILOGY HEALTH SERVICES",
    "HARRISON": "TRILOGY HEALTH SERVICES",
    "NORTHVIEW HEALTH": "ESSENTIAL SENIOR HEALTH AND LIVING",
    "ELWOOD": "ESSENTIAL SENIOR HEALTH AND LIVING",
    "SUMMIT HEALTH": "ESSENTIAL SENIOR HEALTH AND LIVING",
    "CENTURY VILLA": "EXCEPTIONAL LIVING CENTERS",
    "PROVIDENCE HEALTH CARE": "SISTERS OF PROVIDENCE",
    "OWEN VALLEY": "CLAYSHIRE LLC",
    "WATERS OF PRINCETON": "INFINITY HEALTHCARE CONSULTING",
    "WATERS OF MARTINSVILLE": "INFINITY HEALTHCARE CONSULTING",
    "WATERS OF GREENCASTLE": "INFINITY HEALTHCARE CONSULTING",
    "WATERS OF HUNTINGBURG": "INFINITY HEALTHCARE CONSULTING",
    "WATERS OF SCOTTSBURG": "INFINITY HEALTHCARE CONSULTING",
}

mask_pch = df["Corporate_Name"].str.contains("PUTNAM COUNTY HOSPITAL", na=False, case=False)
phantom_names = ["GREENTOWN VOLUNTEER FIRE COMPANY", "ESSENTIAL", "CASTLE HEALTHCARE",
                 "INFINITY HEALTHCARE CONSULTING", "BRAZIL FACILITY CO LLC"]
mask_phantom = df["Corporate_Name"].isin(phantom_names)

for idx in df[mask_pch | mask_phantom].index:
    row = df.loc[idx]
    fac_upper = str(row["Facility_Name"]).upper()
    new_corp = None
    for key, val in pch_facilities.items():
        if key in fac_upper:
            new_corp = val
            break
    if new_corp and new_corp != str(row["Corporate_Name"]):
        changes.append({
            "Punchlist": "#23", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
            "City": row["City"], "State": row["State"],
            "Field": "Corporate_Name", "Current": row["Corporate_Name"],
            "New": new_corp
        })

# Paoli misattribution
mask_paoli = df["Facility_Name"].str.contains("PAOLI HEALTH", na=False, case=False)
for idx in df[mask_paoli].index:
    row = df.loc[idx]
    if "PUTNAM" in str(row["Corporate_Name"]).upper():
        changes.append({
            "Punchlist": "#23", "Excel_Row": idx+2, "Facility": row["Facility_Name"],
            "City": row["City"], "State": row["State"],
            "Field": "Corporate_Name", "Current": row["Corporate_Name"],
            "New": "CARDON MANAGEMENT (pending owner-vs-mgmt decision)"
        })

# === OUTPUT REPORT ===
change_df = pd.DataFrame(changes)
print(f"\n=== V25.7 CHANGE REPORT ===")
print(f"Total changes: {len(change_df)}")
print(f"\nBy punchlist item:")
for pl, count in change_df.groupby("Punchlist").size().items():
    print(f"  {pl}: {count} changes")
print(f"\nBy field:")
for field, count in change_df.groupby("Field").size().items():
    print(f"  {field}: {count}")
print(f"\nDeletes: {len(change_df[change_df['Field'] == 'DELETE ROW'])}")
print(f"\n=== FULL CHANGE LIST ===\n")
for _, c in change_df.iterrows():
    print(f"[{c['Punchlist']}] Row {c['Excel_Row']}: {c['Facility']} ({c['City']}, {c['State']})")
    print(f"  {c['Field']}: {c['Current']} -> {c['New']}")
    print()

change_df.to_csv("scripts/audit_reports/v25_7_change_report.csv", index=False)
print(f"Report saved to scripts/audit_reports/v25_7_change_report.csv")
