"""
Q1 2026 — Current vs Proposed Sale Type Classification
Current: Facility-level (non-EST = New Logo, EST = Integration)
Proposed: Corporate relationship level (check Do_We_Serve across corporate owner)
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

# (name, ae, month, ar, is_est, proposed_type, corp)
items = [
    # JANUARY
    ("Signature HC of Terre Haute", "Adam Sabie", "Jan", 405307.2, False, "New Door", "SIGNATURE HEALTH"),
    ("EST - PruittHealth - Raleigh", "Tonya Hoffman", "Jan", 307756.0, True, "Integration", "PRUITT HEALTH"),
    ("Elkhorn Health & Rehabilitation", "Adam Sabie", "Jan", 291876.1, False, "New Logo", "A&M HEALTHCARE"),
    ("Richland Bean-Blossom HC Center", "Adam Sabie", "Jan", 189878.0, False, "New Logo", "Independent"),
    ("EST - Belmont Terrace", "Adam Sabie", "Jan", 109020.6, True, "Integration", "BLUEGRASS/ENCORE"),
    ("Rehabilitation Center of Cheraw", "Chad Vukelich", "Jan", 89639.16, False, "New Door", "FUNDAMENTAL LTC"),
    ("McCoy Memorial Nursing Center", "Chad Vukelich", "Jan", 84793.8, False, "New Door", "CONCIERGE HC"),
    ("Green Meadows Health and Rehab", "Adam Sabie", "Jan", 54510.3, False, "New Door", "LYON HEALTHCARE"),
    ("Pinewood Nursing Care", "Chad Vukelich", "Jan", 54510.3, False, "New Logo", "OAK HOLLOW HCM"),
    ("EST - Signature HC of Terre Haute", "Adam Sabie", "Jan", 42396.9, True, "Integration", "SIGNATURE HEALTH"),
    ("Elderwood Rehab and Nursing Ctr", "Chad Vukelich", "Jan", 42396.9, False, "New Door", "OAK HOLLOW HCM"),
    ("Seven Acres Senior Living", "Adam Sabie", "Jan", 36340.2, False, "New Logo", "Independent"),
    ("ADDITIONAL CONSENTS- Trinity Grove", "Tonya Hoffman", "Jan", 33917.52, True, "Integration", "SABER HC GROUP"),
    ("EST Gabriel Manor", "Tonya Hoffman", "Jan", 28629.2, True, "Integration", "SABER HC GROUP"),
    # FEBRUARY
    ("Trinity Ridge PCP / NO MD", "Chad Vukelich", "Feb", 320066.24, False, "New Door", "LUTHERAN SVCS CAROLINAS"),
    ("Lutheran Life Villages Kendallville", "Jami Patterson", "Feb", 303497.4, False, "New Door", "LUTHERAN LIFE VILLAGES"),
    ("EST - Elliott Nursing and Rehab", "Adam Sabie", "Feb", 236041.4, True, "Integration", "MAJESTIC CARE"),
    ("JAG Healthcare Mansfield", "Adam Sabie", "Feb", 199110.68, False, "New Door", "JAG"),
    ("Brookdale Lakeview Crossing", "Adam Sabie", "Feb", 93788.1, False, "New Door", "BROOKDALE"),
    ("Terra Bella- Little Ave", "Chad Vukelich", "Feb", 92586.06, False, "New Door", "TERRABELLA"),
    ("EST-Cardinal Landing Memory Care", "Samantha Roark", "Feb", 52104.5, True, "Integration", "TRIPLE CROWN"),
    ("EST- Marquette Manor- Memory Care", "Gunner Grider", "Feb", 41683.6, True, "Integration", "LIFECARE"),
    ("Brookdale Harrisonburg", "Melissa Been", "Feb", 35786.5, False, "New Door", "BROOKDALE"),
    ("EST-Franklin Manor", "Tonya Hoffman", "Feb", 35786.5, True, "Integration", "SABER HC GROUP"),
    # MARCH
    ("EST-PruittHealth - Durham", "Tonya Hoffman", "Mar", 246204.8, True, "Integration", "PRUITT HEALTH"),
    ("OAKVIEW NURSING & REHAB CENTER", "Adam Sabie", "Mar", 153878.0, False, "New Door", "OAKDALE SR ALLIANCE"),
    ("The Cardinal at North Hills SNF", "Tonya Hoffman", "Mar", 90355.46, False, "New Door", "CARDINAL"),
    ("EST- Waters of Wakarusa", "Jami Patterson", "Mar", 72680.4, True, "Integration", "GREENCROFT"),
    ("Arbors At Fairlawn", "Adam Sabie", "Mar", 72680.4, False, "New Door", "ARBORS AT OHIO"),
    ("Chandler Park Assisted Living", "Samantha Roark", "Mar", 70312.8, False, "New Door", "CARDON & ASSOC"),
    ("EST -Grey Stone Health & Rehab", "Jami Patterson", "Mar", 61551.2, True, "Integration", "MAJESTIC CARE"),
    ("EST-Green Leaf Care Center", "Tonya Hoffman", "Mar", 50101.1, True, "Integration", "SABER HC GROUP"),
    ("EST - JAG Healthcare Shelby", "Jami Patterson", "Mar", 42396.9, True, "Integration", "JAG"),
    ("Magnolia Springs Florence", "Adam Sabie", "Mar", 41683.6, False, "New Door", "MAGNOLIA SPRINGS"),
    ("Legacy Heights Sr Living XSell", "Chad Vukelich", "Mar", 40080.88, True, "Integration", "ALG SENIOR"),
    ("ALG Mt Pleasant House XSell", "Chad Vukelich", "Mar", 35786.5, True, "Integration", "ALG SENIOR"),
    ("Bickford of Carmel", "Gunner Grider", "Mar", 31492.12, False, "New Door", "BICKFORD"),
    ("Willowbrook Healthcare Center", "Adam Sabie", "Mar", 30283.5, False, "New Door", "CONTINUING HC SOLUTIONS"),
    ("1019 Belles Place of Crawfordsville", "Gunner Grider", "Mar", 28629.2, False, "New Door", "1019 HEALTHCARE"),
    ("Forest Ridge ALF", "Chad Vukelich", "Mar", 28629.2, False, "New Door", "NAVION SR SOLUTIONS"),
]

# Current classification: non-EST = New Logo, EST = Integration
# (this is how the deck appears to be reporting it)
print("=" * 130)
print("Q1 2026 SALE TYPE CLASSIFICATION — CURRENT vs PROPOSED")
print("=" * 130)
print()
print(f"  {'#':<3} {'Facility':<40} {'AE':<18} {'Mo':<4} {'AR':>12} {'Current':<14} {'Proposed':<14} {'Change?':<8} {'Corporate Owner'}")
print(f"  {'-'*3} {'-'*40} {'-'*18} {'-'*4} {'-'*12} {'-'*14} {'-'*14} {'-'*8} {'-'*25}")

changed_count = 0
changed_ar = 0

for i, (name, ae, month, ar, is_est, proposed, corp) in enumerate(items, 1):
    # Current logic: EST = Integration, non-EST = New Logo
    if is_est:
        current = "Integration"
    else:
        current = "New Logo"

    if current != proposed:
        flag = "<<<<"
        changed_count += 1
        changed_ar += ar
    else:
        flag = ""

    print(f"  {i:<3} {name:<40} {ae:<18} {month:<4} ${ar:>11,.0f} {current:<14} {proposed:<14} {flag:<8} {corp}")

# Summary
total_ar = sum(x[3] for x in items)
print()
print("=" * 130)
print("SUMMARY")
print("=" * 130)

# Current totals
cur_nl = sum(x[3] for x in items if not x[4])
cur_ig = sum(x[3] for x in items if x[4])

# Proposed totals
prop_nl = sum(x[3] for x in items if x[5] == "New Logo")
prop_nd = sum(x[3] for x in items if x[5] == "New Door")
prop_ig = sum(x[3] for x in items if x[5] == "Integration")

print()
print(f"  {'Sale Type':<20} {'Current':>14} {'Current %':>10} {'Proposed':>14} {'Proposed %':>10} {'Delta':>14}")
print(f"  {'-'*20} {'-'*14} {'-'*10} {'-'*14} {'-'*10} {'-'*14}")
print(f"  {'New Logo':<20} ${cur_nl:>13,.0f} {cur_nl/total_ar*100:>9.1f}% ${prop_nl:>13,.0f} {prop_nl/total_ar*100:>9.1f}% ${prop_nl-cur_nl:>13,.0f}")
print(f"  {'New Door':<20} ${'0':>13} {'0.0%':>10} ${prop_nd:>13,.0f} {prop_nd/total_ar*100:>9.1f}% ${prop_nd:>13,.0f}")
print(f"  {'Integration':<20} ${cur_ig:>13,.0f} {cur_ig/total_ar*100:>9.1f}% ${prop_ig:>13,.0f} {prop_ig/total_ar*100:>9.1f}% ${prop_ig-cur_ig:>13,.0f}")
print(f"  {'-'*20} {'-'*14} {'-'*10} {'-'*14} {'-'*10} {'-'*14}")
print(f"  {'TOTAL':<20} ${total_ar:>13,.0f} {'100.0%':>10} ${total_ar:>13,.0f} {'100.0%':>10}")

print()
print(f"  Items that change classification: {changed_count} of {len(items)}")
print(f"  AR that changes classification:   ${changed_ar:,.0f}")
print()
print(f"  Key shift: ${cur_nl - prop_nl:,.0f} moves OUT of New Logo into New Door")
print(f"  This is revenue from facilities where we already serve another building")
print(f"  under the same corporate owner — existing relationships, not new ones.")
