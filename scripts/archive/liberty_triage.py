#!/usr/bin/env python3
"""Triage Liberty crosswalk matches into actionable cleanup buckets."""

import sys
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # archive: find utils.py
sys.path.insert(0, ".")
from utils import load_db, norm_addr, norm, safe, VAULT, FOOTPRINT

DB = VAULT / "Current" / "1_Combined_Database_FINAL_V22_1.xlsx"
headers, rows = load_db(DB)

# ── Build address index ──
db_by_addr = {}
for r in rows:
    akey = norm_addr(safe(r.get("Address", ""))) + "|" + norm(safe(r.get("City", ""))) + "|" + norm(safe(r.get("State", "")))
    db_by_addr.setdefault(akey, []).append(r)

def addr_lookup(address, city, state):
    akey = norm_addr(address) + "|" + norm(city) + "|" + norm(state)
    return db_by_addr.get(akey, [])

# ── Collect all Liberty-related DB rows ──
liberty_all = [r for r in rows if "LIBERTY" in safe(r.get("Corporate_Name", "")).upper()]

print("=" * 80)
print("LIBERTY TRIAGE — ACTIONABLE CLEANUP BUCKETS")
print("=" * 80)

# ────────────────────────────────────────────────────────
# BUCKET 1: Not Liberty Health at all — different companies
# ────────────────────────────────────────────────────────
NOT_LIBERTY_HEALTH = {
    "SEACOAST AT LIBERTY RIDGE",
    "LIBERTY RIDGE SENIOR LIVING INC",
    "LIBERTY RETIREMENT PROPERTIES OF LIMA LTD",
    "WEST LIBERTY GARDEN APARTMENTS",
}
# Liberty Village is separate company (IL-based)
LIBERTY_VILLAGE_CORPS = {
    "LIBERTY VILLAGE",
    "Liberty Village of Freeport", "Liberty Village of Geneseo",
    "Liberty Village of Jerseyville", "Liberty Village of Peoria",
    "Liberty Village of Peru", "Liberty Village of Rochelle",
    "Liberty Village of Streator",
}

not_lhm = [r for r in liberty_all if safe(r.get("Corporate_Name", "")) in NOT_LIBERTY_HEALTH]
lib_village = [r for r in liberty_all if safe(r.get("Corporate_Name", "")) in LIBERTY_VILLAGE_CORPS]

print(f"\n{'-'*80}")
print(f"BUCKET 1: NOT LIBERTY HEALTH — LEAVE ALONE ({len(not_lhm)} rows)")
print(f"{'-'*80}")
print("These are different companies. No action needed in Liberty remediation.")
for r in not_lhm:
    served = safe(r.get("Do_We_Serve", ""))
    print(f"  Row {r['_excel_row']:>5}: {safe(r.get('Corporate_Name','')):45s} | {safe(r.get('Source_Type',''))} | {safe(r.get('City',''))}, {safe(r.get('State',''))} | Served={served}")

print(f"\n{'-'*80}")
print(f"BUCKET 2: LIBERTY VILLAGE — SEPARATE COMPANY ({len(lib_village)} rows)")
print(f"{'-'*80}")
print("Illinois-based. Not Liberty Health Management. Phase 1c already planned to consolidate names.")
for r in lib_village:
    served = safe(r.get("Do_We_Serve", ""))
    print(f"  Row {r['_excel_row']:>5}: {safe(r.get('Corporate_Name','')):45s} | {safe(r.get('Source_Type',''))} | {safe(r.get('City',''))}, {safe(r.get('State',''))} | Served={served}")

# ────────────────────────────────────────────────────────
# BUCKET 3: LHR SNFs matched — what Corporate_Name do they have now?
# ────────────────────────────────────────────────────────
lhr_addresses = [
    ("791 Boone Station Drive", "Burlington", "NC"),
    ("1403 Connor Ave.", "Windsor", "NC"),
    ("208 Mercer Road", "Elizabethtown", "NC"),
    ("630 N Fodale Ave", "Southport", "NC"),
    ("104 Holcombe Cove Road", "Candler", "NC"),
    ("1402 Pinckney Street", "Whiteville", "NC"),
    ("200 Flowers-Pridgen Drive", "Whiteville", "NC"),
    ("7348 North West Street", "Falcon", "NC"),
    ("400 Pelt Drive", "Fayetteville", "NC"),
    ("1700 Pamalee Dr.", "Fayetteville", "NC"),
    ("316 NC Highway 801 South", "Advance", "NC"),
    ("6041 Piedmont Row Drive", "Charlotte", "NC"),
    ("5680 Windy Hill Drive", "Winston-Salem", "NC"),
    ("901 Bethesda Road", "Winston-Salem", "NC"),
    ("485 Veteran's Way", "Kernersville", "NC"),
    ("202 Smoketree Way", "Louisburg", "NC"),
    ("101 Caroline Avenue", "Weldon", "NC"),
    ("100 Silver Bluff Dr.", "Canton", "NC"),
    ("2315 Highway 242 North", "Benson", "NC"),
    ("310 Commerce Drive", "Sanford", "NC"),
    ("3100 Tramway Road", "Sanford", "NC"),
    ("2700 Royal Commons Lane", "Matthews", "NC"),
    ("10011 Providence Road West", "Charlotte", "NC"),
    ("300 Blake Road", "Pinehurst", "NC"),
    ("155 Blake Road", "Pinehurst", "NC"),
    ("740 Diamond Shoals Road", "Wilmington", "NC"),
    ("121 Racine Drive", "Wilmington", "NC"),
    ("1718 Legion Road", "Chapel Hill", "NC"),
    ("901 Ridge Road", "Roxboro", "NC"),
    ("1150 Pine Run Dr.", "Lumberton", "NC"),
    ("4412 South Main Street", "Salisbury", "NC"),
    ("120 Southwood Drive", "Clinton", "NC"),
    ("180 Southwood Drive", "Clinton", "NC"),
    ("3000 Holston Lane", "Raleigh", "NC"),
    ("2750 Oberlin Road", "Raleigh", "NC"),
    ("221 Brightmore Drive", "Cary", "NC"),
    ("864 US Hwy. 158 Business West", "Warrenton", "NC"),
    ("621 Chestnut Ridge Parkway", "Blowing Rock", "NC"),
    ("903 W. Main Street", "Yadkinville", "NC"),
    ("194 Spring Street", "Charleston", "SC"),
    ("100 Samaritan Way", "Crossville", "TN"),
]

print(f"\n{'-'*80}")
print(f"BUCKET 3: LHR SNFs — CORPORATE_NAME AUDIT")
print(f"{'-'*80}")
lhr_matched_rows = []
lhr_not_found = []
lhr_wrong_corp = []
lhr_correct = []
lhr_served = []

for (addr, city, state) in lhr_addresses:
    matches = addr_lookup(addr, city, state)
    if not matches:
        lhr_not_found.append((addr, city, state))
    else:
        for m in matches:
            lhr_matched_rows.append(m)
            corp = safe(m.get("Corporate_Name", "")).upper()
            served = safe(m.get("Do_We_Serve", ""))
            stype = safe(m.get("Source_Type", ""))
            if served.upper() in ("YES", "Y", "TRUE", "1"):
                lhr_served.append(m)
            if "LIBERTY" in corp and "PROPERTIES" not in corp:
                lhr_correct.append(m)
            else:
                lhr_wrong_corp.append(m)

print(f"  LHR addresses searched: {len(lhr_addresses)}")
print(f"  DB rows matched:        {len(lhr_matched_rows)}")
print(f"  Not found in DB:        {len(lhr_not_found)}")
print(f"  SERVED:                 {len(lhr_served)}")

if lhr_not_found:
    print(f"\n  NOT FOUND:")
    for (a, c, s) in lhr_not_found:
        print(f"    {a}, {c}, {s}")

# Show corporate name distribution for LHR matches
from collections import Counter
lhr_corps = Counter(safe(r.get("Corporate_Name", "")) for r in lhr_matched_rows)
print(f"\n  Current Corporate_Name distribution for LHR-matched rows:")
for corp, cnt in lhr_corps.most_common(20):
    print(f"    {corp}: {cnt}")

if lhr_wrong_corp:
    print(f"\n  WRONG CORPORATE NAME ({len(lhr_wrong_corp)} rows — need rename to LHR entity):")
    for r in lhr_wrong_corp[:10]:
        print(f"    Row {r['_excel_row']:>5}: Corp={safe(r.get('Corporate_Name','')):40s} | {safe(r.get('Facility_Name',''))} | Served={safe(r.get('Do_We_Serve',''))}")
    if len(lhr_wrong_corp) > 10:
        print(f"    ... and {len(lhr_wrong_corp) - 10} more")

# ────────────────────────────────────────────────────────
# BUCKET 4: LSL matches — check for IL contamination and PROPCO issues
# ────────────────────────────────────────────────────────
lsl_addresses = [
    ("Brightmore of South Charlotte", "10225 Old Ardrey Kell Road", "Charlotte", "NC", "IL, AL, Memory Support, Rehab, Skilled Care"),
    ("Brightmore of Wilmington", "2124 41st Street", "Wilmington", "NC", "IL, AL, Living Smart"),
    ("Carlisle Palm Beach", "450 East Ocean Avenue", "Lantana", "FL", "IL, AL, Memory Care"),
    ("Carolina Bay at Autumn Hall", "620 Carolina Bay Drive", "Wilmington", "NC", "IL, AL, Memory Care, Skilled Nursing"),
    ("Hayes Barton Place", "2600 Yettington Drive", "Raleigh", "NC", "IL, AL, Memory Support, Rehab, Skilled Care"),
    ("Inspire Briar Chapel", "152 Market Chapel Road", "Pittsboro", "NC", "Senior 55+ Rental Apartments"),
    ("Inspire Brunswick Forest", "6146 Liberty Hall Drive", "Leland", "NC", "Senior 55+ Rental Apartments"),
    ("Inspire Royal Park", "4101 Glenloch Circle", "Matthews", "NC", "55+ Rental Apartments"),
    ("Inspire Sandhill", "440 Town Center Place", "Columbia", "SC", "Active Senior 55+ Rental Apartments"),
    ("Kempton of Charleston", "194 Spring Street", "Charleston", "SC", "AL, Memory Support, Skilled Nursing, Rehab"),
    ("Kempton of Jacksonville", "3045 Henderson Drive Extension", "Jacksonville", "NC", "AL, Memory Support"),
    ("The Kempton of Hermitage", "3778 Central Pike", "Hermitage", "TN", "AL, Memory Support"),
    ("Kempton of Rockhill", "1611 Constitution Boulevard", "Rock Hill", "SC", "AL, Memory Support"),
    ("Oakleaf Village of Lexington", "800 N Lake Drive", "Lexington", "SC", "AL, Memory Support"),
    ("Pisgah Valley", "95 Holcombe Cove Road", "Candler", "NC", "IL, AL, Rehab, Skilled Care"),
    ("Quail Haven Village", "155 Blake Boulevard", "Pinehurst", "NC", "IL, AL, Memory Support, Rehab, Skilled Care"),
    ("South Bay at Mount Pleasant", "1400 Liberty Midtown Drive", "Mount Pleasant", "SC", "IL, AL, Memory Support"),
    ("The Barclay at SouthPark", "4801 Barclay Downs Drive", "Charlotte", "NC", "IL, AL, Memory Support, Rehab, Skilled Care"),
    ("The Peninsula of Charleston", "625 King Street", "Charleston", "SC", "IL, AL, Memory Support, Rehab, Skilled Care"),
    ("The Preserve at Fairfield Glade", "100 Samaritan Way", "Crossville", "TN", "IL, AL, Rehab, Skilled Care"),
    ("The Templeton of Cary", "125 Brightmore Drive", "Cary", "NC", "IL, AL, Memory Support, Rehab, Skilled Care"),
    ("Wellington Bay", "10430 Stable Lane", "Wellington", "FL", "IL, AL, Memory Care"),
]

print(f"\n{'-'*80}")
print(f"BUCKET 4: LSL FACILITIES — DB STATUS")
print(f"{'-'*80}")

lsl_pure_il = []
lsl_has_al = []

for (name, addr, city, state, care) in lsl_addresses:
    in_fp = state.upper() in FOOTPRINT
    if not in_fp:
        continue
    matches = addr_lookup(addr, city, state)
    is_55_plus = "55+" in care
    has_il = "IL" in care or "Independent" in care
    has_al = "AL" in care or "Assisted" in care or "Memory" in care

    if matches:
        for m in matches:
            stype = safe(m.get("Source_Type", ""))
            corp = safe(m.get("Corporate_Name", ""))
            served = safe(m.get("Do_We_Serve", ""))
            flag = ""
            if is_55_plus and stype == "ALF":
                flag = "** 55+ listed as ALF — should be ILF **"
                lsl_pure_il.append(m)
            elif is_55_plus and stype == "SNF":
                flag = "(55+ but SNF in DB — check)"
            elif has_il and not has_al and stype == "ALF":
                flag = "** Pure IL listed as ALF — should be ILF **"
                lsl_pure_il.append(m)

            if has_al:
                lsl_has_al.append(m)

            print(f"  {name:40s} | DB: {stype} | Corp: {corp:35s} | Served: {served} {flag}")
    else:
        print(f"  {name:40s} | NOT IN DB")

# ────────────────────────────────────────────────────────
# BUCKET 5: Bare "LIBERTY" remaining orphans
# ────────────────────────────────────────────────────────
bare = [r for r in liberty_all
        if safe(r.get("Corporate_Name", "")) == "LIBERTY"
        and r["_excel_row"] not in set(m["_excel_row"] for m in lhr_matched_rows)]

print(f"\n{'-'*80}")
print(f"BUCKET 5: BARE 'LIBERTY' — STILL UNMATCHED ({len(bare)} rows)")
print(f"{'-'*80}")
print("These didn't match any LHR or LSL website address. May be different companies entirely.")
for r in bare:
    served = safe(r.get("Do_We_Serve", ""))
    print(f"  Row {r['_excel_row']:>5}: {safe(r.get('Facility_Name','')):40s} | {safe(r.get('Source_Type',''))} | {safe(r.get('Address',''))}, {safe(r.get('City',''))}, {safe(r.get('State',''))} | Served={served}")

# ────────────────────────────────────────────────────────
# BUCKET 6: PROPCO-named rows at Liberty addresses
# ────────────────────────────────────────────────────────
propco_at_liberty = [r for r in lhr_matched_rows + lsl_has_al
                     if "LIBERTY" not in safe(r.get("Corporate_Name", "")).upper()]
print(f"\n{'-'*80}")
print(f"BUCKET 6: PROPCO NAMES AT LIBERTY ADDRESSES ({len(propco_at_liberty)} rows)")
print(f"{'-'*80}")
print("DB rows at confirmed Liberty addresses but under a PROPCO/wrong Corporate_Name.")
propco_corps = Counter(safe(r.get("Corporate_Name", "")) for r in propco_at_liberty)
for corp, cnt in propco_corps.most_common(20):
    served_in_corp = sum(1 for r in propco_at_liberty
                         if safe(r.get("Corporate_Name", "")) == corp
                         and safe(r.get("Do_We_Serve", "")).upper() in ("YES", "Y", "TRUE", "1"))
    print(f"  {corp}: {cnt} rows ({served_in_corp} served)")

# ────────────────────────────────────────────────────────
# SUMMARY
# ────────────────────────────────────────────────────────
print(f"\n{'='*80}")
print("SUMMARY — IMMEDIATE ACTIONS")
print(f"{'='*80}")
print(f"""
1. LEAVE ALONE: {len(not_lhm)} rows — not Liberty Health (Liberty Ridge, Liberty Retirement, etc.)
2. LIBERTY VILLAGE: {len(lib_village)} rows — separate IL company. Phase 1c rename already planned.
3. LHR SNF CORPORATE FIX: {len(lhr_wrong_corp)} rows at confirmed LHR addresses have wrong Corporate_Name.
4. IL CONTAMINATION: {len(lsl_pure_il)} rows — website says 55+/pure IL but DB has them as ALF. Reclassify to ILF.
5. BARE 'LIBERTY' ORPHANS: {len(bare)} rows — didn't match any website. Investigate if truly Liberty Health.
6. PROPCO AT LIBERTY: {len(propco_at_liberty)} rows — confirmed Liberty addresses under PROPCO names. Rename.
7. SERVED FACILITIES: {len(lhr_served)} LHR rows are served — cross-ref with Facility DB if unclear.
""")
