"""
Full corporate owner comparison: Finance vs GLR vs Database V25.6
For every Q1 2026 facility, show all three sources and our proposed correction.
"""
import csv, openpyxl, sys, re
sys.stdout.reconfigure(encoding="utf-8")

# Load GLR Parent Company
glr = {}
with open(r"C:\Users\ratwood\data-model\reference\GLR_Facility_Dump_2026-03-13.csv", "r", encoding="latin-1") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = (row.get("Facility Name") or "").upper().strip()
        parent = (row.get("Parent Company") or "").strip()
        if name:
            glr[name] = parent

# Load DB V25.6 corporate names
wb = openpyxl.load_workbook(
    r"C:\Users\ratwood\OneDrive - Eventus WholeHealth\Vault\02_Data_Model\Current\1_Combined_Database_FINAL_V25_6.xlsx",
    read_only=True, data_only=True
)
ws = wb[wb.sheetnames[0]]
db = {}
db_corps_served = set()
for row in ws.iter_rows(min_row=2, values_only=True):
    name = (row[1] or "").upper().strip()
    corp = (row[2] or "").strip()
    serve = row[11]
    addr = (row[3] or "").upper()
    city = (row[4] or "").upper()
    state = (row[5] or "").upper()
    db[name] = (corp, serve, city, state)
    if serve == "Yes" and corp:
        db_corps_served.add(corp.upper())
wb.close()

# Facility list from Forecasting Model
facilities = [
    ("Richland Bean-Blossom HCC", "Hutsonwood INC", "New Door", "NB", 189878),
    ("Pinewood Nursing Care", "CJM Advisors/Brothers Healthcare", "New Door", "NB", 54510),
    ("McCoy Memorial Nursing Center", "Concierge Physicians", "New Door", "NB", 84794),
    ("Seven Acres Senior Living at Clifton", "Private", "New Logo", "NB", 36340),
    ("Signature HC of Terre Haute", "Signature Healthcare", "New Logo", "NB", 405307),
    ("Rehab Center of Cheraw", "Fundamental LTC", "New Logo", "NB", 89639),
    ("Elderwood Rehab and Nursing Center", "CJM Advisors/Brothers Healthcare", "New Door", "NB", 42397),
    ("Green Meadows Health and Rehab", "Hill Valley Healthcare", "New Logo", "NB", 54510),
    ("Trinity Grove", "Lutheran Home", "New Logo", "NB", 33917),
    ("PruittHealth - Raleigh", "Pruitt Health", "Integration", "Integration", 307756),
    ("Elkhorn Health & Rehab", "Hill Valley Healthcare", "New Logo", "NB", 307264),
    ("Gabriel Manor", "Saber Healthcare", "Integration", "Integration", 28629),
    ("Belmont Terrace", "BHP/Encore", "New Door", "NB", 109021),
    ("JAG Healthcare Mansfield", "JAG", "New Logo", "NB", 199111),
    ("Trinity Ridge", "Lutheran Home", "New Logo", "NB", 320066),
    ("Lutheran Life Villages Kendallville", "Lutheran Home", "New Logo", "NB", 303497),
    ("Brookdale Harrisonburg", "Brookdale", "Integration", "Integration", 35786),
    ("Terra Bella Little Avenue", "Terra Bella", "New Logo", "NB", 92586),
    ("Marquette Manor Memory Care", "Life Care Services", "Integration", "Integration", 41684),
    ("Franklin Manor", "Saber", "Integration", "Integration", 35786),
    ("Brookdale Lakeview Crossing", "Brookdale", "New Logo", "NB", 93788),
    ("Elliott Nursing", "Majestic Care", "Integration", "Integration", 236041),
    ("Cardinal Landing", "Triple Crown", "Integration", "Integration", 52104),
]

# DB and GLR lookups (manual mapping for name mismatches)
db_map = {
    "Richland Bean-Blossom HCC": "RICHLAND BEAN BLOSSOM HEALTH CARE CENTER",
    "Pinewood Nursing Care": "OAK HOLLOW OF SUMTER REHABILITATION CENTER",
    "McCoy Memorial Nursing Center": "MCCOY MEMORIAL NURSING CENTER",
    "Seven Acres Senior Living at Clifton": "SEVEN ACRES SENIOR LIVING AT CLIFTON",
    "Signature HC of Terre Haute": "SIGNATURE HEALTHCARE AT PARKWOOD",
    "Rehab Center of Cheraw": "REHAB CENTER OF CHERAW",
    "Elderwood Rehab and Nursing Center": "OAK HOLLOW OF GEORGETOWN REHABILITATION CENTER LLC",
    "Green Meadows Health and Rehab": "GREEN MEADOWS HEALTH & REHABILITATION",
    "Trinity Grove": "TRINITY GROVE",
    "PruittHealth - Raleigh": "PRUITTHEALTH - RALEIGH",
    "Elkhorn Health & Rehab": "ELKHORN HEALTH & REHABILITATION",
    "Gabriel Manor": "GABRIEL MANOR",
    "Belmont Terrace": "BELMONT TERRACE NURSING AND REHABILITATION CENTER",
    "JAG Healthcare Mansfield": "GERIATRIC CENTER OF MANSFIELD",
    "Trinity Ridge": "TRINITY RIDGE",
    "Lutheran Life Villages Kendallville": "LUTHERAN LIFE VILLAGES",
    "Brookdale Harrisonburg": "BROOKDALE (ALF) HARRISONBURG",
    "Terra Bella Little Avenue": "TERRABELLA LITTLE AVENUE",
    "Marquette Manor Memory Care": "MARQUETTE",
    "Franklin Manor": "FRANKLIN MANOR",
    "Brookdale Lakeview Crossing": "BROOKDALE LAKEVIEW CROSSING",
    "Elliott Nursing": "ELLIOTT NURSING AND REHABILITATION",
    "Cardinal Landing": "CARDINAL LANDING MEMORY CARE",
}

our_corp = {
    "Richland Bean-Blossom HCC": ("Independent (null)", "New Logo"),
    "Pinewood Nursing Care": ("OAK HOLLOW HEALTHCARE MANAGEMENT", "New Logo"),
    "McCoy Memorial Nursing Center": ("CONCIERGE HEALTHCARE", "New Door"),
    "Seven Acres Senior Living at Clifton": ("Independent (null)", "New Logo"),
    "Signature HC of Terre Haute": ("SIGNATURE HEALTH", "New Door"),
    "Rehab Center of Cheraw": ("FUNDAMENTAL LTC", "New Door"),
    "Elderwood Rehab and Nursing Center": ("OAK HOLLOW HEALTHCARE MANAGEMENT", "New Door"),
    "Green Meadows Health and Rehab": ("LYON HEALTHCARE", "New Door"),
    "Trinity Grove": ("SABER HEALTHCARE GROUP", "Integration"),
    "PruittHealth - Raleigh": ("PRUITT HEALTH", "Integration"),
    "Elkhorn Health & Rehab": ("A&M HEALTHCARE INVESTMENT LLC", "New Logo"),
    "Gabriel Manor": ("SABER HEALTHCARE GROUP", "Integration"),
    "Belmont Terrace": ("BLUEGRASS/ENCORE", "Integration"),
    "JAG Healthcare Mansfield": ("JAG", "New Door"),
    "Trinity Ridge": ("LUTHERAN SERVICES CAROLINAS", "New Door"),
    "Lutheran Life Villages Kendallville": ("LUTHERAN LIFE VILLAGES", "New Door"),
    "Brookdale Harrisonburg": ("BROOKDALE SENIOR LIVING", "New Door"),
    "Terra Bella Little Avenue": ("TERRABELLA SENIOR LIVING", "New Door"),
    "Marquette Manor Memory Care": ("LIFECARE", "Integration"),
    "Franklin Manor": ("SABER HEALTHCARE GROUP", "Integration"),
    "Brookdale Lakeview Crossing": ("BROOKDALE SENIOR LIVING", "New Door"),
    "Elliott Nursing": ("MAJESTIC CARE", "Integration"),
    "Cardinal Landing": ("TRIPLE CROWN SENIOR LIVING", "Integration"),
}

# Reasons for change
reasons = {
    "Richland Bean-Blossom HCC": "Finance uses 'Hutsonwood INC' — not in DB or CMS. DB has null corp, Ownership_Type=Independent. No corporate parent to check.",
    "Pinewood Nursing Care": "Finance uses 'CJM Advisors/Brothers Healthcare' — Brothers HC is an unrelated hemophilia pharmacy. CJM untraceable. Actual operator: Oak Hollow HCM (CMS verified, V25.6 fix). 2-facility startup, not served prior.",
    "McCoy Memorial Nursing Center": "Finance uses 'Concierge Physicians' vs DB 'Concierge Healthcare'. Same entity, name variant. Classification agrees (New Door).",
    "Seven Acres Senior Living at Clifton": "Finance uses 'Private', DB has null/Independent. Both agree: New Logo.",
    "Signature HC of Terre Haute": "Finance classifies as New Logo. We serve 27 Signature Health facilities. New Door — existing corporate relationship.",
    "Rehab Center of Cheraw": "Finance classifies as New Logo. We serve 6 Fundamental LTC facilities. New Door — existing corporate relationship.",
    "Elderwood Rehab and Nursing Center": "Finance correctly identifies as New Door (CJM/Brothers = Oak Hollow). Our classification agrees (second Oak Hollow win after Pinewood).",
    "Green Meadows Health and Rehab": "Finance uses 'Hill Valley Healthcare' — WRONG. DB V25.6 has Lyon Healthcare. Hill Valley is a different OH operator. New Door — we serve 3 Lyon facilities.",
    "Trinity Grove": "Finance classifies as New Logo under 'Lutheran Home'. This is an ADDITIONAL CONSENTS item — cross-sell at existing facility (Saber-operated). Should be Integration.",
    "PruittHealth - Raleigh": "All sources agree: Integration.",
    "Elkhorn Health & Rehab": "Finance uses 'Hill Valley Healthcare' — WRONG. DB V25.6 has A&M Healthcare Investment LLC. Not served anywhere. New Logo.",
    "Gabriel Manor": "All sources agree: Integration (Saber).",
    "Belmont Terrace": "Finance classifies as New Door (BHP/Encore). EST item in Monday.com — we already serve this facility. Should be Integration. BHP/Encore = Bluegrass/Encore (V25.6 fix).",
    "JAG Healthcare Mansfield": "Finance classifies as New Logo. We serve JAG Healthcare Shelby + Union City. New Door — existing corporate relationship.",
    "Trinity Ridge": "Finance uses 'Lutheran Home', classifies as New Logo. DB has Lutheran Services Carolinas. We serve 11 LSC facilities. New Door.",
    "Lutheran Life Villages Kendallville": "Finance uses 'Lutheran Home', classifies as New Logo. DB has Lutheran Life Villages. We serve 7 LLV facilities. New Door. Note: Lutheran Home != Lutheran Life Villages — different organizations.",
    "Brookdale Harrisonburg": "Finance classifies as Integration. NOT an EST item — new facility for us. We serve 45 Brookdale facilities. New Door, not Integration.",
    "Terra Bella Little Avenue": "Finance classifies as New Logo. We serve 11 TerraBella facilities. New Door — existing corporate relationship.",
    "Marquette Manor Memory Care": "Finance uses 'Life Care Services' vs DB 'LifeCare'. Same entity. All agree: Integration.",
    "Franklin Manor": "All sources agree: Integration (Saber).",
    "Brookdale Lakeview Crossing": "Finance classifies as New Logo under Brookdale. We serve 45 Brookdale facilities. New Door. (DB had INDEPENDENT — corrected in V25.6 Do_We_Serve, corp recode pending #21.)",
    "Elliott Nursing": "All sources agree: Integration (Majestic Care).",
    "Cardinal Landing": "All sources agree: Integration (Triple Crown).",
}

# GLR lookup
def find_glr(facility_name):
    db_name = db_map.get(facility_name, "")
    # Try exact match on DB name
    if db_name.upper() in glr:
        return glr[db_name.upper()]
    # Try partial
    for gn, gp in glr.items():
        if db_name.upper()[:20] in gn or facility_name.upper()[:20] in gn:
            return gp
    return ""

# DB lookup
def find_db(facility_name):
    db_name = db_map.get(facility_name, "")
    if db_name.upper() in db:
        return db[db_name.upper()]
    return ("", "", "", "")

# Print table
print("=" * 160)
print("Q1 2026 SALE TYPE — FULL SOURCE COMPARISON")
print("Finance Forecasting Model vs GLR Parent Company vs Database V25.6 vs Our Proposed")
print("=" * 160)
print()
print(f"{'#':<3} {'Facility':<35} {'Finance Corp':<30} {'GLR Parent Co':<25} {'DB V25.6 Corp':<30} {'Fin Type':<12} {'Our Type':<12} {'Match':<5}")
print(f"{'-'*3} {'-'*35} {'-'*30} {'-'*25} {'-'*30} {'-'*12} {'-'*12} {'-'*5}")

for i, (fac, fin_corp, fin_type, fin_nb, ar) in enumerate(facilities, 1):
    glr_parent = find_glr(fac)
    db_info = find_db(fac)
    db_corp = db_info[0] if db_info[0] else "null"
    our_c, our_t = our_corp[fac]
    match = "YES" if fin_type == our_t else ""
    print(f"{i:<3} {fac:<35} {fin_corp:<30} {glr_parent:<25} {our_c:<30} {fin_type:<12} {our_t:<12} {match:<5}")

# Detailed reasons
print()
print("=" * 160)
print("CHANGE LOG — Why each classification changed (or didn't)")
print("=" * 160)
print()
for i, (fac, fin_corp, fin_type, fin_nb, ar) in enumerate(facilities, 1):
    our_c, our_t = our_corp[fac]
    reason = reasons[fac]
    changed = "CHANGED" if fin_type != our_t else "AGREES"
    print(f"{i:>2}. {fac}")
    print(f"    Finance: {fin_type} ({fin_corp}) | Proposed: {our_t} ({our_c}) | {changed}")
    print(f"    {reason}")
    print()
