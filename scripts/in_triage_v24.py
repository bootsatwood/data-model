import openpyxl
import sys
from collections import defaultdict

DB_PATH = r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V24.xlsx"

# Column indices (1-based for openpyxl)
COL = {
    'Source_Type': 1,
    'Facility_Name': 2,
    'Corporate_Name': 3,
    'Address': 4,
    'City': 5,
    'State': 6,
    'ZIP': 7,
    'County': 8,
    'Ownership_Type': 9,
    'Total_Beds': 10,
    'Census': 11,
    'Do_We_Serve': 12,
    'Integrated_Flag': 13,
    'PCP_Flag': 14,
    'MH_Flag': 15,
    'Barrier': 16,
    'Latitude': 17,
    'Longitude': 18,
    'Data_Quality_Flag': 19,
    'Contract_Status': 20,
    'Geographic_Tier': 21,
}

print("Loading workbook...")
wb = openpyxl.load_workbook(DB_PATH, read_only=True, data_only=True)
ws = wb.active
print(f"Sheet: {ws.title}")

# Read all rows, skip header (row 1)
rows_in = []  # list of (row_number, row_data_as_list)
header = None
for i, row in enumerate(ws.iter_rows(min_row=1, values_only=False), start=1):
    vals = [cell.value for cell in row]
    if i == 1:
        header = vals
        print(f"Header row ({len(vals)} columns): {vals[:22]}")
        continue
    state_val = vals[COL['State'] - 1]  # 0-based index into vals list
    if state_val is not None and str(state_val).strip().upper() == 'IN':
        rows_in.append((i, vals))

wb.close()

# Helper: get value from row by column name
def g(row_vals, col_name):
    return row_vals[COL[col_name] - 1]

def blank(v):
    return v is None or str(v).strip() == ''

# ============================================================
# 1. Total IN row count and breakdown by Source_Type
# ============================================================
print("\n" + "=" * 70)
print("1. TOTAL IN ROW COUNT & SOURCE_TYPE BREAKDOWN")
print("=" * 70)
print(f"Total IN rows: {len(rows_in)}")
src_counts = defaultdict(int)
for _, vals in rows_in:
    st = g(vals, 'Source_Type')
    src_counts[str(st).strip() if st else '(blank)'] += 1
for k in sorted(src_counts.keys()):
    print(f"  {k}: {src_counts[k]}")

# ============================================================
# 2. SNF mistype candidates: State=IN, Source_Type=ALF, name contains "SNF"
# ============================================================
print("\n" + "=" * 70)
print("2. SNF MISTYPE CANDIDATES (Source_Type=ALF, Name contains 'SNF')")
print("=" * 70)
mistype = []
for row_num, vals in rows_in:
    st = g(vals, 'Source_Type')
    name = g(vals, 'Facility_Name')
    if st and str(st).strip().upper() == 'ALF' and name and 'SNF' in str(name).upper():
        mistype.append((row_num, vals))

if mistype:
    for row_num, vals in mistype:
        print(f"  Row {row_num}:")
        print(f"    Name:    {g(vals, 'Facility_Name')}")
        print(f"    Address: {g(vals, 'Address')}")
        print(f"    City:    {g(vals, 'City')}")
        print(f"    Beds:    {g(vals, 'Total_Beds')}")
        print(f"    Served:  {g(vals, 'Do_We_Serve')}")
        print()
else:
    print("  None found.")

# ============================================================
# 3. Data quality flags in IN
# ============================================================
print("=" * 70)
print("3. DATA QUALITY FLAGS IN IN (Data_Quality_Flag not blank)")
print("=" * 70)
flagged = []
for row_num, vals in rows_in:
    dqf = g(vals, 'Data_Quality_Flag')
    if not blank(dqf):
        flagged.append((row_num, vals))

if flagged:
    for row_num, vals in flagged:
        print(f"  Row {row_num}:")
        print(f"    Name:    {g(vals, 'Facility_Name')}")
        print(f"    Flag:    {g(vals, 'Data_Quality_Flag')}")
        print(f"    Type:    {g(vals, 'Source_Type')}")
        print(f"    Address: {g(vals, 'Address')}, {g(vals, 'City')}")
        print()
else:
    print("  None found.")

# ============================================================
# 4. Same-address clusters in IN
# ============================================================
print("=" * 70)
print("4. SAME-ADDRESS CLUSTERS IN IN (2+ rows at same address+city)")
print("=" * 70)
addr_map = defaultdict(list)
for row_num, vals in rows_in:
    addr = g(vals, 'Address')
    city = g(vals, 'City')
    if blank(addr):
        continue
    key = (str(addr).strip().upper(), str(city).strip().upper() if city else '')
    addr_map[key].append((row_num, vals))

clusters = {k: v for k, v in addr_map.items() if len(v) >= 2}
if clusters:
    print(f"  Total clusters: {len(clusters)}")
    print()
    for (addr, city), entries in sorted(clusters.items()):
        print(f"  Address: {addr}, City: {city}  [{len(entries)} rows]")
        for row_num, vals in entries:
            print(f"    Row {row_num}: {g(vals, 'Facility_Name')} | Type: {g(vals, 'Source_Type')} | Beds: {g(vals, 'Total_Beds')} | Served: {g(vals, 'Do_We_Serve')}")
        print()
else:
    print("  None found.")

# ============================================================
# 5. Blank county in IN
# ============================================================
print("=" * 70)
print("5. BLANK COUNTY IN IN")
print("=" * 70)
blank_county = []
for row_num, vals in rows_in:
    county = g(vals, 'County')
    if blank(county):
        blank_county.append((row_num, vals))

if blank_county:
    print(f"  Total with blank county: {len(blank_county)}")
    print()
    for row_num, vals in blank_county:
        print(f"    Row {row_num}: {g(vals, 'Facility_Name')} | {g(vals, 'Address')}, {g(vals, 'City')} | Type: {g(vals, 'Source_Type')}")
else:
    print("  None found.")

# ============================================================
# 6. Blank corporate name for served IN facilities
# ============================================================
print("\n" + "=" * 70)
print("6. BLANK CORPORATE NAME FOR SERVED IN FACILITIES (Do_We_Serve=Yes)")
print("=" * 70)
blank_corp = []
for row_num, vals in rows_in:
    served = g(vals, 'Do_We_Serve')
    corp = g(vals, 'Corporate_Name')
    if served and str(served).strip().upper() == 'YES' and blank(corp):
        blank_corp.append((row_num, vals))

if blank_corp:
    print(f"  Total: {len(blank_corp)}")
    print()
    for row_num, vals in blank_corp:
        print(f"    Row {row_num}: {g(vals, 'Facility_Name')} | {g(vals, 'City')} | Type: {g(vals, 'Source_Type')} | Beds: {g(vals, 'Total_Beds')}")
else:
    print("  None found.")

# ============================================================
# 7. Census anomalies in IN
# ============================================================
print("\n" + "=" * 70)
print("7. CENSUS ANOMALIES IN IN (None, 0, or Census > Total_Beds)")
print("=" * 70)
census_issues = []
for row_num, vals in rows_in:
    census = g(vals, 'Census')
    beds = g(vals, 'Total_Beds')
    issue = None

    if census is None or (isinstance(census, str) and census.strip() == ''):
        issue = "Census is None/blank"
    else:
        try:
            c = float(census)
            if c == 0:
                issue = "Census is 0"
            else:
                if beds is not None:
                    try:
                        b = float(beds)
                        if c > b:
                            issue = f"Census ({census}) > Total_Beds ({beds})"
                    except (ValueError, TypeError):
                        pass
        except (ValueError, TypeError):
            issue = f"Census not numeric: {census}"

    if issue:
        census_issues.append((row_num, vals, issue))

if census_issues:
    # Summarize by issue type
    issue_counts = defaultdict(int)
    for _, _, iss in census_issues:
        if 'None' in iss or 'blank' in iss:
            issue_counts['None/Blank'] += 1
        elif 'is 0' in iss:
            issue_counts['Zero'] += 1
        elif '>' in iss:
            issue_counts['Census > Beds'] += 1
        else:
            issue_counts['Other'] += 1
    print(f"  Total census anomalies: {len(census_issues)}")
    for k, v in sorted(issue_counts.items()):
        print(f"    {k}: {v}")
    print()

    # Print Census > Beds in full
    gt_beds = [(r, v, i) for r, v, i in census_issues if '>' in i]
    null_zero = [(r, v, i) for r, v, i in census_issues if '>' not in i]

    if gt_beds:
        print("  --- Census > Total_Beds ---")
        for row_num, vals, issue in gt_beds:
            print(f"    Row {row_num}: {g(vals, 'Facility_Name')} | {issue} | City: {g(vals, 'City')} | Type: {g(vals, 'Source_Type')}")
        print()

    if null_zero:
        print(f"  --- None/Blank/Zero Census (showing up to 50 of {len(null_zero)}) ---")
        for row_num, vals, issue in null_zero[:50]:
            print(f"    Row {row_num}: {g(vals, 'Facility_Name')} | {issue} | City: {g(vals, 'City')} | Type: {g(vals, 'Source_Type')} | Beds: {g(vals, 'Total_Beds')}")
        if len(null_zero) > 50:
            print(f"    ... and {len(null_zero) - 50} more")
else:
    print("  None found.")

# ============================================================
# 8. Geographic tier distribution in IN
# ============================================================
print("\n" + "=" * 70)
print("8. GEOGRAPHIC TIER DISTRIBUTION IN IN")
print("=" * 70)
tier_counts = defaultdict(int)
for _, vals in rows_in:
    tier = g(vals, 'Geographic_Tier')
    tier_counts[str(tier).strip() if not blank(tier) else '(blank)'] += 1

for k in sorted(tier_counts.keys()):
    print(f"  {k}: {tier_counts[k]}")

print("\n" + "=" * 70)
print("TRIAGE COMPLETE")
print("=" * 70)
