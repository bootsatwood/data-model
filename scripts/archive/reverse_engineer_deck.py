import sys
from itertools import combinations
sys.stdout.reconfigure(encoding="utf-8")

# Deck targets (swapped labels)
target_nl = 480599    # What deck calls "New Door" = actually New Logo
target_nd = 1936026   # What deck calls "New Logo" = actually New Door
target_ig = 737788    # Integration

# Jan+Feb items: (name, ar_new_assumptions, ar_estimated, is_est, proposed_type)
items = [
    ("Signature HC of Terre Haute", 405307.2, 239875.2, False, "New Door"),
    ("EST - PruittHealth - Raleigh", 307756.0, 169896.0, True, "Integration"),
    ("Elkhorn Health & Rehabilitation", 291876.1, 185010.6, False, "New Logo"),
    ("Richland Bean-Blossom HC Center", 189878.0, 120948.0, False, "New Logo"),
    ("EST - Belmont Terrace", 109020.6, 146156.4, True, "Integration"),
    ("Rehabilitation Center of Cheraw", 89639.16, 120173.04, False, "New Door"),
    ("McCoy Memorial Nursing Center", 84793.8, 113677.2, False, "New Door"),
    ("Green Meadows Health and Rehab", 54510.3, 73078.2, False, "New Door"),
    ("Pinewood Nursing Care", 54510.3, 73078.2, False, "New Logo"),
    ("EST - Signature HC of Terre Haute", 42396.9, 56838.6, True, "Integration"),
    ("Elderwood Rehab and Nursing Ctr", 42396.9, 56838.6, False, "New Door"),
    ("Seven Acres Senior Living", 36340.2, 48718.8, False, "New Logo"),
    ("ADDITIONAL CONSENTS- Trinity Grove", 33917.52, 45470.88, True, "Integration"),
    ("EST Gabriel Manor", 28629.2, 37968.0, True, "Integration"),
    ("Trinity Ridge PCP / NO MD", 320066.24, 176691.84, False, "New Door"),
    ("Lutheran Life Villages Kendallville", 303497.4, 224859.6, False, "New Door"),
    ("EST - Elliott Nursing and Rehab", 236041.4, 146432.4, True, "Integration"),
    ("JAG Healthcare Mansfield", 199110.68, 126044.88, False, "New Door"),
    ("Brookdale Lakeview Crossing", 93788.1, 84412.8, False, "New Door"),
    ("Terra Bella- Little Ave", 92586.06, 96141.6, False, "New Door"),
    ("EST-Cardinal Landing Memory Care", 52104.5, 46896.0, True, "Integration"),
    ("EST- Marquette Manor- Memory Care", 41683.6, 37516.8, True, "Integration"),
    ("Brookdale Harrisonburg", 35786.5, 47460.0, False, "New Door"),
    ("EST-Franklin Manor", 35786.5, 47460.0, True, "Integration"),
]

print("=" * 100)
print("SCENARIO ANALYSIS: REVERSE ENGINEERING THE DECK NUMBERS")
print("=" * 100)

# SCENARIO 1: Use Estimated AR (old formula) with our proposed classification
print("\n--- SCENARIO 1: Estimated AR (old formula) + Our Classification ---")
s1 = {"New Logo": 0, "New Door": 0, "Integration": 0}
for name, ar_new, ar_est, is_est, ptype in items:
    s1[ptype] += ar_est
print(f"  New Logo:     ${s1['New Logo']:>12,.0f}   target ${target_nl:>12,.0f}   delta ${s1['New Logo']-target_nl:>10,.0f}")
print(f"  New Door:     ${s1['New Door']:>12,.0f}   target ${target_nd:>12,.0f}   delta ${s1['New Door']-target_nd:>10,.0f}")
print(f"  Integration:  ${s1['Integration']:>12,.0f}   target ${target_ig:>12,.0f}   delta ${s1['Integration']-target_ig:>10,.0f}")

# SCENARIO 2: Use Estimated AR + swap Independents to New Door
print("\n--- SCENARIO 2: Estimated AR + Independents coded as New Door ---")
s2 = {"New Logo": 0, "New Door": 0, "Integration": 0}
for name, ar_new, ar_est, is_est, ptype in items:
    if ptype == "New Logo" and "Independent" in name or "Bean-Blossom" in name or "Seven Acres" in name:
        s2["New Door"] += ar_est
    else:
        s2[ptype] += ar_est
print(f"  New Logo:     ${s2['New Logo']:>12,.0f}   target ${target_nl:>12,.0f}   delta ${s2['New Logo']-target_nl:>10,.0f}")
print(f"  New Door:     ${s2['New Door']:>12,.0f}   target ${target_nd:>12,.0f}   delta ${s2['New Door']-target_nd:>10,.0f}")
print(f"  Integration:  ${s2['Integration']:>12,.0f}   target ${target_ig:>12,.0f}   delta ${s2['Integration']-target_ig:>10,.0f}")

# SCENARIO 3: Estimated AR + Trinity Grove and Gabriel Manor as New Door instead of Integration
print("\n--- SCENARIO 3: Estimated AR + Trinity Grove & Gabriel Manor as New Door ---")
s3 = {"New Logo": 0, "New Door": 0, "Integration": 0}
for name, ar_new, ar_est, is_est, ptype in items:
    if name in ("ADDITIONAL CONSENTS- Trinity Grove", "EST Gabriel Manor"):
        s3["New Door"] += ar_est
    else:
        s3[ptype] += ar_est
print(f"  New Logo:     ${s3['New Logo']:>12,.0f}   target ${target_nl:>12,.0f}   delta ${s3['New Logo']-target_nl:>10,.0f}")
print(f"  New Door:     ${s3['New Door']:>12,.0f}   target ${target_nd:>12,.0f}   delta ${s3['New Door']-target_nd:>10,.0f}")
print(f"  Integration:  ${s3['Integration']:>12,.0f}   target ${target_ig:>12,.0f}   delta ${s3['Integration']-target_ig:>10,.0f}")

# SCENARIO 4: Estimated AR + Independents as New Door + Trinity Grove/Gabriel as New Door
print("\n--- SCENARIO 4: Estimated AR + Indep as New Door + Trinity Grove/Gabriel as New Door ---")
s4 = {"New Logo": 0, "New Door": 0, "Integration": 0}
for name, ar_new, ar_est, is_est, ptype in items:
    if "Bean-Blossom" in name or "Seven Acres" in name:
        s4["New Door"] += ar_est
    elif name in ("ADDITIONAL CONSENTS- Trinity Grove", "EST Gabriel Manor"):
        s4["New Door"] += ar_est
    else:
        s4[ptype] += ar_est
print(f"  New Logo:     ${s4['New Logo']:>12,.0f}   target ${target_nl:>12,.0f}   delta ${s4['New Logo']-target_nl:>10,.0f}")
print(f"  New Door:     ${s4['New Door']:>12,.0f}   target ${target_nd:>12,.0f}   delta ${s4['New Door']-target_nd:>10,.0f}")
print(f"  Integration:  ${s4['Integration']:>12,.0f}   target ${target_ig:>12,.0f}   delta ${s4['Integration']-target_ig:>10,.0f}")

# SCENARIO 5: Estimated AR + Elkhorn as New Door (maybe they see A&M as served?)
print("\n--- SCENARIO 5: Estimated AR + Elkhorn as New Door ---")
s5 = {"New Logo": 0, "New Door": 0, "Integration": 0}
for name, ar_new, ar_est, is_est, ptype in items:
    if "Elkhorn" in name:
        s5["New Door"] += ar_est
    else:
        s5[ptype] += ar_est
print(f"  New Logo:     ${s5['New Logo']:>12,.0f}   target ${target_nl:>12,.0f}   delta ${s5['New Logo']-target_nl:>10,.0f}")
print(f"  New Door:     ${s5['New Door']:>12,.0f}   target ${target_nd:>12,.0f}   delta ${s5['New Door']-target_nd:>10,.0f}")
print(f"  Integration:  ${s5['Integration']:>12,.0f}   target ${target_ig:>12,.0f}   delta ${s5['Integration']-target_ig:>10,.0f}")

# SCENARIO 6: Estimated AR + EST Signature Terre Haute as New Door (cross-sell but in leads group)
print("\n--- SCENARIO 6: Estimated AR + EST Signature TH as New Door (not Integration) ---")
s6 = {"New Logo": 0, "New Door": 0, "Integration": 0}
for name, ar_new, ar_est, is_est, ptype in items:
    if name == "EST - Signature HC of Terre Haute":
        s6["New Door"] += ar_est
    else:
        s6[ptype] += ar_est
print(f"  New Logo:     ${s6['New Logo']:>12,.0f}   target ${target_nl:>12,.0f}   delta ${s6['New Logo']-target_nl:>10,.0f}")
print(f"  New Door:     ${s6['New Door']:>12,.0f}   target ${target_nd:>12,.0f}   delta ${s6['New Door']-target_nd:>10,.0f}")
print(f"  Integration:  ${s6['Integration']:>12,.0f}   target ${target_ig:>12,.0f}   delta ${s6['Integration']-target_ig:>10,.0f}")

# SCENARIO 7: Brute force — try moving each non-EST item between NL/ND using Estimated AR
# to find a combination that gets closest to deck targets
print("\n--- SCENARIO 7: BRUTE FORCE — Best fit using Estimated AR ---")
non_est = [(name, ar_est, ptype) for name, ar_new, ar_est, is_est, ptype in items if not is_est]
est_items = [(name, ar_est) for name, ar_new, ar_est, is_est, ptype in items if is_est]
est_total = sum(x[1] for x in est_items)

# Integration is fixed (EST items)
# We need to split non-EST items into NL and ND to match targets
# target_ig = 737,788 vs est_total — check if some EST items are in a different bucket

# Try all possible NL subsets of non-EST items
best_score = float("inf")
best_nl_set = None
non_est_names = [x[0] for x in non_est]
non_est_ars = [x[1] for x in non_est]
n = len(non_est)

# Check each possible subset size for NL
for size in range(0, n + 1):
    for combo in combinations(range(n), size):
        nl_total = sum(non_est_ars[i] for i in combo)
        nd_total = sum(non_est_ars[i] for i in range(n) if i not in combo)
        # Score = distance from targets (NL and ND only, integration is separate)
        score = abs(nl_total - target_nl) + abs(nd_total - target_nd)
        if score < best_score:
            best_score = score
            best_nl_set = combo
            best_nl_total = nl_total
            best_nd_total = nd_total

print(f"  Best fit (score = ${best_score:,.0f}):")
print(f"  New Logo:     ${best_nl_total:>12,.0f}   target ${target_nl:>12,.0f}   delta ${best_nl_total-target_nl:>10,.0f}")
print(f"  New Door:     ${best_nd_total:>12,.0f}   target ${target_nd:>12,.0f}   delta ${best_nd_total-target_nd:>10,.0f}")
print(f"  Integration:  ${est_total:>12,.0f}   target ${target_ig:>12,.0f}   delta ${est_total-target_ig:>10,.0f}")
print(f"\n  New Logo facilities in best fit:")
for i in best_nl_set:
    print(f"    {non_est_names[i]:<45} ${non_est_ars[i]:>11,.0f}")
print(f"\n  New Door facilities in best fit:")
for i in range(n):
    if i not in best_nl_set:
        print(f"    {non_est_names[i]:<45} ${non_est_ars[i]:>11,.0f}")
