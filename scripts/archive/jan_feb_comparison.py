import sys
sys.stdout.reconfigure(encoding="utf-8")

# Jan+Feb items only with proposed classification
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
]

# Deck values (from Slide 2 chart)
deck = {"New Door": 480599, "New Logo": 1936026, "Integration": 737788}

# Our proposed
prop = {"New Logo": 0.0, "New Door": 0.0, "Integration": 0.0}
for name, ae, mo, ar, is_est, ptype, corp in items:
    prop[ptype] += ar

total = sum(prop.values())

print("=" * 85)
print("JAN + FEB SALE TYPE — DECK vs PROPOSED")
print("=" * 85)
print()
print(f"  {'Sale Type':<14} {'Deck':>14} {'Deck %':>8} {'Proposed':>14} {'Proposed %':>8} {'Delta':>14}")
print(f"  {'-'*14} {'-'*14} {'-'*8} {'-'*14} {'-'*8} {'-'*14}")
for st in ["New Logo", "New Door", "Integration"]:
    d = deck[st]
    p = prop[st]
    dp = d / sum(deck.values()) * 100
    pp = p / total * 100
    print(f"  {st:<14} ${d:>13,.0f} {dp:>7.1f}% ${p:>13,.0f} {pp:>7.1f}% ${p-d:>13,.0f}")
print(f"  {'-'*14} {'-'*14} {'-'*8} {'-'*14} {'-'*8}")
print(f"  {'TOTAL':<14} ${sum(deck.values()):>13,.0f}          ${total:>13,.0f}")

# Issue 1: Are New Door and New Logo inverted?
print()
print("=" * 85)
print("ISSUE 1: ARE NEW DOOR AND NEW LOGO INVERTED IN THE DECK?")
print("=" * 85)
print()
print(f"  Deck says:     New Logo = ${deck['New Logo']:>12,.0f}   New Door = ${deck['New Door']:>12,.0f}")
print(f"  Our analysis:  New Logo = ${prop['New Logo']:>12,.0f}   New Door = ${prop['New Door']:>12,.0f}")
print()
# What if we swap the deck labels?
print(f"  If deck labels are SWAPPED:")
print(f"    Deck 'New Logo' ${deck['New Logo']:>12,.0f}  vs  Our 'New Door' ${prop['New Door']:>12,.0f}  delta ${prop['New Door']-deck['New Logo']:>10,.0f}")
print(f"    Deck 'New Door' ${deck['New Door']:>12,.0f}  vs  Our 'New Logo' ${prop['New Logo']:>12,.0f}  delta ${prop['New Logo']-deck['New Door']:>10,.0f}")

# Issue 2: Independents inflating New Logo
print()
print("=" * 85)
print("ISSUE 2: INDEPENDENTS INFLATING NEW LOGO")
print("=" * 85)
print()
indep = [(n, ar) for n, ae, mo, ar, est, pt, corp in items if corp == "Independent"]
indep_ar = sum(x[1] for x in indep)
print(f"  Independent facilities classified as New Logo:")
for n, ar in indep:
    print(f"    {n:<45} ${ar:>11,.0f}")
print(f"    {'Subtotal':<45} ${indep_ar:>11,.0f}")
print()
print(f"  New Logo with Independents:    ${prop['New Logo']:>11,.0f} ({prop['New Logo']/total*100:.1f}%)")
print(f"  New Logo without Independents: ${prop['New Logo']-indep_ar:>11,.0f} ({(prop['New Logo']-indep_ar)/total*100:.1f}%)")
print()
print(f"  If Independents are excluded from New Logo (treated as their own category):")
print(f"    New Logo (corp):   ${prop['New Logo']-indep_ar:>11,.0f}  ({(prop['New Logo']-indep_ar)/total*100:.1f}%)")
print(f"    Independent:       ${indep_ar:>11,.0f}  ({indep_ar/total*100:.1f}%)")
print(f"    New Door:          ${prop['New Door']:>11,.0f}  ({prop['New Door']/total*100:.1f}%)")
print(f"    Integration:       ${prop['Integration']:>11,.0f}  ({prop['Integration']/total*100:.1f}%)")

# Detail: the 20 non-EST items and how they map
print()
print("=" * 85)
print("NON-EST ITEMS — WHERE THE CLASSIFICATION MATTERS")
print("=" * 85)
print()
non_est = [(n, ae, mo, ar, pt, corp) for n, ae, mo, ar, est, pt, corp in items if not est]
non_est_total = sum(x[3] for x in non_est)
print(f"  {'Facility':<40} {'AR':>12} {'Proposed':<10} {'Corporate Owner'}")
print(f"  {'-'*40} {'-'*12} {'-'*10} {'-'*25}")
for n, ae, mo, ar, pt, corp in non_est:
    print(f"  {n:<40} ${ar:>11,.0f} {pt:<10} {corp}")
print(f"  {'-'*40} {'-'*12}")
print(f"  {'Non-EST Total':<40} ${non_est_total:>11,.0f}")
print(f"  Deck calls all of this:  New Logo + New Door = ${deck['New Logo']+deck['New Door']:>11,.0f}")
print(f"  Our split:               New Logo ${prop['New Logo']:>11,.0f} + New Door ${prop['New Door']:>11,.0f} = ${prop['New Logo']+prop['New Door']:>11,.0f}")
