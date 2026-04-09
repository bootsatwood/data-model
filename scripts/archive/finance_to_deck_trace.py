"""
Full trace: Finance Revenue Detail → Deck Chart
Shows where numbers come from, where they diverge, and where classifications break.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

# Finance Revenue Detail items (Jan+Feb only, from workbook)
# (facility, finance_type, booking_month)
finance_items = [
    ("Richland Bean-Blossom", "NB", "Jan"),
    ("McCoy Memorial Nursing Center", "NB", "Jan"),
    ("Rehabilitation Center of Cheraw", "NB", "Jan"),
    ("Pinewood Nursing Care", "NB", "Jan"),
    ("Seven Acres Senior Living", "NB", "Jan"),
    ("Signature HC of Terre Haute", "NB", "Jan"),
    ("Green Meadows Health and Rehab", "NB", "Jan"),
    ("Elderwood Rehab and Nursing Ctr", "NB", "Jan"),
    ("PruittHealth - Raleigh", "Integration", "Jan"),
    ("Elkhorn Health & Rehab", "NB", "Jan"),
    ("Belmont Terrace", "NB", "Jan"),
    ("Gabriel Manor", "Integration", "Jan"),
    ("JAG Healthcare Mansfield", "NB", "Feb"),
    ("Trinity Ridge", "NB", "Feb"),
    ("Brookdale Harrisonburg", "Integration", "Feb"),
    ("Franklin Manor", "Integration", "Feb"),
    ("Elliott Nursing", "Integration", "Feb"),
]

# Monday.com items with consent date in Jan+Feb (our full universe, 24 items)
# (facility, monday_ar, is_est, our_type, corporate_owner)
monday_items = [
    ("Signature HC of Terre Haute", 405307.2, False, "New Door", "SIGNATURE HEALTH"),
    ("EST - PruittHealth - Raleigh", 307756.0, True, "Integration", "PRUITT HEALTH"),
    ("Elkhorn Health & Rehabilitation", 291876.1, False, "New Logo", "A&M HEALTHCARE"),
    ("Richland Bean-Blossom HC Center", 189878.0, False, "New Logo", "Independent"),
    ("EST - Belmont Terrace", 109020.6, True, "Integration", "BLUEGRASS/ENCORE"),
    ("Rehabilitation Center of Cheraw", 89639.16, False, "New Door", "FUNDAMENTAL LTC"),
    ("McCoy Memorial Nursing Center", 84793.8, False, "New Door", "CONCIERGE HC"),
    ("Green Meadows Health and Rehab", 54510.3, False, "New Door", "LYON HEALTHCARE"),
    ("Pinewood Nursing Care", 54510.3, False, "New Logo", "OAK HOLLOW HCM"),
    ("EST - Signature HC of Terre Haute", 42396.9, True, "Integration", "SIGNATURE HEALTH"),
    ("Elderwood Rehab and Nursing Ctr", 42396.9, False, "New Door", "OAK HOLLOW HCM"),
    ("Seven Acres Senior Living", 36340.2, False, "New Logo", "Independent"),
    ("ADDITIONAL CONSENTS- Trinity Grove", 33917.52, True, "Integration", "SABER HC GROUP"),
    ("EST Gabriel Manor", 28629.2, True, "Integration", "SABER HC GROUP"),
    ("Trinity Ridge PCP / NO MD", 320066.24, False, "New Door", "LUTHERAN SVCS CAROLINAS"),
    ("Lutheran Life Villages Kendallville", 303497.4, False, "New Door", "LUTHERAN LIFE VILLAGES"),
    ("EST - Elliott Nursing and Rehab", 236041.4, True, "Integration", "MAJESTIC CARE"),
    ("JAG Healthcare Mansfield", 199110.68, False, "New Door", "JAG"),
    ("Brookdale Lakeview Crossing", 93788.1, False, "New Door", "BROOKDALE"),
    ("Terra Bella- Little Ave", 92586.06, False, "New Door", "TERRABELLA"),
    ("EST-Cardinal Landing Memory Care", 52104.5, True, "Integration", "TRIPLE CROWN"),
    ("EST- Marquette Manor- Memory Care", 41683.6, True, "Integration", "LIFECARE"),
    ("Brookdale Harrisonburg", 35786.5, False, "New Door", "BROOKDALE"),
    ("EST-Franklin Manor", 35786.5, True, "Integration", "SABER HC GROUP"),
]

# Deck chart values (from Slide 2, as presented)
deck = {"New Logo": 1936026, "New Door": 480599, "Integration": 737788}

# =========================================================
print("=" * 100)
print("STEP 1: FINANCE SOURCE DATA")
print("What Finance has in Revenue Detail (17 items, 2 categories)")
print("=" * 100)
print()

fin_nb = [f for f in finance_items if f[1] == "NB"]
fin_ig = [f for f in finance_items if f[1] == "Integration"]

print(f"  NB ({len(fin_nb)} items):")
for f in fin_nb:
    print(f"    {f[0]:<50} {f[2]}")
print(f"\n  Integration ({len(fin_ig)} items):")
for f in fin_ig:
    print(f"    {f[0]:<50} {f[2]}")

# =========================================================
print()
print("=" * 100)
print("STEP 2: MONDAY.COM SOURCE DATA")
print("What Monday.com has (24 items, consent date Jan+Feb)")
print("=" * 100)
print()

# Items in Monday.com but NOT in Finance
finance_names = set()
for f in finance_items:
    finance_names.add(f[0].upper().replace("EST ", "").replace("EST-", "").replace("- ", " ").strip())

monday_only = []
for m in monday_items:
    clean = m[0].upper().replace("EST ", "").replace("EST-", "").replace("EST ", "").replace("- ", " ").strip()
    clean = clean.replace("ADDITIONAL CONSENTS ", "").replace(" PCP / NO MD", "").replace(" HC CENTER", "").replace(" HEALTH REHABILITATION", " HEALTH AND REHAB")
    found = False
    for fn in finance_names:
        if fn[:15] in clean or clean[:15] in fn:
            found = True
            break
    if not found:
        monday_only.append(m)

print(f"  Items in Monday.com but MISSING from Finance Revenue Detail ({len(monday_only)}):")
for m in monday_only:
    est = " [EST]" if m[2] else ""
    print(f"    {m[0] + est:<50} ${m[1]:>11,.0f}  {m[3]}")
missing_ar = sum(m[1] for m in monday_only)
print(f"    {'TOTAL MISSING':<50} ${missing_ar:>11,.0f}")

# =========================================================
print()
print("=" * 100)
print("STEP 3: CLASSIFICATION MISMATCHES")
print("Where Finance and our corporate-level analysis disagree")
print("=" * 100)
print()
print(f"  {'Facility':<45} {'Finance':<14} {'Ours':<14} {'Issue'}")
print(f"  {'-'*45} {'-'*14} {'-'*14} {'-'*40}")

# Belmont Terrace
print(f"  {'Belmont Terrace':<45} {'NB':<14} {'Integration':<14} EST in Monday.com, new MH service at")
print(f"  {'':<45} {'':<14} {'':<14} existing facility. Finance treats as NB.")

# Brookdale Harrisonburg
print(f"  {'Brookdale Harrisonburg':<45} {'Integration':<14} {'New Door':<14} NOT EST in Monday.com. New facility")
print(f"  {'':<45} {'':<14} {'':<14} for us. Finance treats as Integration.")

# =========================================================
print()
print("=" * 100)
print("STEP 4: DECK CHART — WHERE DO THE 3 BUCKETS COME FROM?")
print("=" * 100)
print()
print(f"  Deck chart shows:")
print(f"    New Logo:     ${deck['New Logo']:>12,.0f}  (61.4%)")
print(f"    New Door:     ${deck['New Door']:>12,.0f}  (15.2%)")
print(f"    Integration:  ${deck['Integration']:>12,.0f}  (23.4%)")
print(f"    Total:        ${sum(deck.values()):>12,.0f}")
print()
print(f"  Finance source has 2 categories:")
print(f"    NB:           12 items (no $ from this sheet — it tracks realized revenue, not AR)")
print(f"    Integration:   5 items")
print()
print(f"  The deck's 3-way split MUST be derived somewhere between Finance and the chart.")
print(f"  Someone is splitting Finance's 'NB' bucket into 'New Logo' and 'New Door.'")
print(f"  That split is not in the Finance workbook.")

# =========================================================
print()
print("=" * 100)
print("STEP 5: OUR PROPOSED CLASSIFICATION (Jan+Feb, AR with New Assumptions)")
print("=" * 100)
print()

our = {"New Logo": 0.0, "New Door": 0.0, "Integration": 0.0}
for m in monday_items:
    our[m[3]] += m[1]

print(f"  {'Category':<20} {'Deck':>14} {'Our Analysis':>14} {'Delta':>14}")
print(f"  {'-'*20} {'-'*14} {'-'*14} {'-'*14}")
for cat in ["New Logo", "New Door", "Integration"]:
    print(f"  {cat:<20} ${deck[cat]:>13,.0f} ${our[cat]:>13,.0f} ${our[cat]-deck[cat]:>13,.0f}")
print(f"  {'-'*20} {'-'*14} {'-'*14} {'-'*14}")
print(f"  {'TOTAL':<20} ${sum(deck.values()):>13,.0f} ${sum(our.values()):>13,.0f} ${sum(our.values())-sum(deck.values()):>13,.0f}")

# =========================================================
print()
print("=" * 100)
print("STEP 6: ROOT CAUSES")
print("=" * 100)
print()
print("  1. MISSING NEW DOOR CATEGORY IN FINANCE")
print("     Finance uses NB vs Integration. There is no New Door concept.")
print("     The deck's 3-way split is applied downstream without a defined methodology.")
print()
print("  2. BELMONT TERRACE MISCODED")
print("     Finance: NB. Monday.com: EST (Integration). We serve this facility.")
print("     Adds ~$109K to NB that should be Integration.")
print()
print("  3. BROOKDALE HARRISONBURG MISCODED")
print("     Finance: Integration. Monday.com: NOT EST. New facility for us.")
print("     Removes ~$36K from NB that should be there (as New Door).")
print()
print("  4. SEVEN ITEMS MISSING FROM FINANCE")
print("     7 Monday.com items ($694K) with Q1 consent dates are not in Revenue Detail.")
print("     These are being counted in the deck's AR totals but not tracked in Finance's")
print("     facility-level classification. Includes EST-Signature Terre Haute ($42K),")
print("     Additional Consents-Trinity Grove ($34K), Lutheran Life Villages ($303K),")
print("     Brookdale Lakeview Crossing ($94K), Terra Bella ($93K), EST-Cardinal Landing")
print("     ($52K), EST-Marquette Manor ($42K).")
print()
print("  5. INDEPENDENTS TREATED AS NEW LOGO")
print("     Richland Bean-Blossom and Seven Acres are Independent (no corporate parent).")
print("     They default to New Logo under any method, but they're not 'new corporate")
print("     relationships' — they're standalone buildings. $226K classified as New Logo")
print("     that is structurally different from a true new corporate logo win.")
print()
print("  6. LABEL INVERSION LIKELY")
print("     The deck's New Logo ($1.94M) is closer to our New Door ($1.72M) and vice versa.")
print("     If swapped, the deltas shrink from $1.4M to ~$215K. The remaining delta is")
print("     explained by AR formula differences and the missing/miscoded items above.")
