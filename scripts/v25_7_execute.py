"""Execute V25.7 changes — approved by Roian Atwood 2026-04-04."""
import pandas as pd
import shutil
from datetime import datetime

# Paths
src_path = r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V25_6.xlsx"
dst_path = r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V25_7.xlsx"
report_path = "scripts/audit_reports/v25_7_change_report.csv"

# Load
df = pd.read_excel(src_path)
changes = pd.read_csv(report_path)
print(f"Loaded V25.6: {len(df)} rows")
print(f"Changes to apply: {len(changes)}")

# Track changes for verification
applied = 0
skipped = 0
deleted_rows = []

for _, c in changes.iterrows():
    idx = int(c["Excel_Row"]) - 2  # Convert Excel row to 0-based index

    if idx < 0 or idx >= len(df):
        print(f"  SKIP: Row {c['Excel_Row']} out of range")
        skipped += 1
        continue

    row = df.loc[idx]

    if c["Field"] == "DELETE ROW":
        deleted_rows.append(idx)
        print(f"  DELETE: Row {c['Excel_Row']} {row['Facility_Name']} ({row['City']}, {row['State']})")
        applied += 1
        continue

    field = c["Field"]
    new_val = c["New"]
    old_val = str(row[field]) if pd.notna(row[field]) else "null"
    expected_old = str(c["Current"])

    # Verify current value matches expected (loose match for null/nan)
    old_check = old_val.lower().strip()
    expected_check = expected_old.lower().strip()

    if old_check == "nan":
        old_check = "null"

    if old_check != expected_check and expected_check != "null":
        # Check if it's close enough (case differences, whitespace)
        if old_check.replace(" ", "") != expected_check.replace(" ", ""):
            print(f"  MISMATCH Row {c['Excel_Row']}: expected '{expected_old}' but found '{old_val}' — applying anyway (field: {field})")

    df.at[idx, field] = new_val
    applied += 1

# Delete phantom rows
if deleted_rows:
    df = df.drop(deleted_rows).reset_index(drop=True)
    print(f"\nDeleted {len(deleted_rows)} rows")

print(f"\nApplied: {applied}")
print(f"Skipped: {skipped}")
print(f"Final row count: {len(df)}")
print(f"Expected: {25508 - len(deleted_rows)} (25508 - {len(deleted_rows)} deletes)")

# Verify counts
assert len(df) == 25508 - len(deleted_rows), f"Row count mismatch! Expected {25508 - len(deleted_rows)}, got {len(df)}"

# Save
df.to_excel(dst_path, index=False)
print(f"\nSaved to: {dst_path}")

# Verification summary
print("\n=== VERIFICATION ===")
print(f"V25.6 rows: 25508")
print(f"V25.7 rows: {len(df)}")
print(f"Deletes: {len(deleted_rows)}")
print(f"Recodes: {applied - len(deleted_rows)}")

# Spot check key recodes
print("\n=== SPOT CHECKS ===")
spot_checks = [
    ("BROOKDALE ALLIANCE", "OH", "BROOKDALE SENIOR LIVING"),
    ("BOYD NURSING AND REHABILITATION", "KY", "MAJESTIC / BLUEGRASS CONSULTING GROUP"),
    ("MAJESTIC CARE OF AVON", "IN", "MAJESTIC / MAJESTIC CARE"),
    ("MCCOY MEMORIAL NURSING CENTER", "SC", "CARLYLE SENIOR CARE"),
    ("ELKHORN HEALTH & REHABILITATION", "KY", "LYON HEALTHCARE"),
    ("HARMONY AT ELKHART", "IN", "HARMONY SENIOR SERVICES"),
    ("HARMONY HALL NURSING AND REHABILITATION CENTER", "NC", "PRINCIPLE LONG TERM CARE"),
    ("CAMELLIA GARDENS", "NC", "ALLIANCE HEALTH GROUP"),
    ("ELWOOD HEALTH AND LIVING", "IN", "ESSENTIAL SENIOR HEALTH AND LIVING"),
    ("CENTURY VILLA HEALTH CARE", "IN", "EXCEPTIONAL LIVING CENTERS"),
    ("RICHLAND BEAN BLOSSOM HEALTH CARE CENTER", "IN", "HUTSONWOOD"),
    ("PROVIDENCE HEALTH CARE CENTER", "IN", "SISTERS OF PROVIDENCE"),
    ("HUTSONWOOD AT BRAZIL", "IN", "HUTSONWOOD"),
    ("OWEN VALLEY REHABILITATION AND HEALTHCARE CENTER", "IN", "CLAYSHIRE LLC"),
]

all_pass = True
for fac, state, expected_corp in spot_checks:
    mask = (df["Facility_Name"] == fac) & (df["State"] == state)
    if mask.sum() == 0:
        print(f"  NOT FOUND: {fac} ({state})")
        all_pass = False
        continue
    actual = df.loc[mask, "Corporate_Name"].values[0]
    status = "PASS" if actual == expected_corp else "FAIL"
    if status == "FAIL":
        all_pass = False
    print(f"  {status}: {fac} ({state}) = {actual}")

# Check phantom ALF is deleted
mask_phantom = (df["Facility_Name"].str.contains("HARMONY HALL", na=False, case=False)) & (df["City"].str.contains("KINSTON", na=False, case=False))
phantom_count = mask_phantom.sum()
print(f"\n  Harmony Hall Kinston rows remaining: {phantom_count} (should be 1 — SNF only)")

if all_pass and phantom_count == 1:
    print("\n=== ALL SPOT CHECKS PASSED ===")
else:
    print("\n=== SOME CHECKS FAILED — REVIEW BEFORE USING ===")
