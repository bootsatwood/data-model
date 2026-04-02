import sys
sys.stdout.reconfigure(encoding="utf-8")

items = [
    ("EST - Signature HC of Terre Haute", "Adam Sabie", "01", 56838.6, True, "New Facility Leads"),
    ("Chandler Park Assisted Living", "Samantha Roark", "03", 75484.8, False, "Consenting"),
    ("EST- Waters of Wakarusa", "Jami Patterson", "03", 97437.6, True, "Consenting"),
    ("1019 Belles Place of Crawfordsville", "Gunner Grider", "03", 37968, False, "Consenting"),
    ("EST-PruittHealth - Durham", "Tonya Hoffman", "03", 135916.8, True, "Consenting"),
    ("Bickford of Carmel", "Gunner Grider", "03", 41764.8, False, "Scheduling"),
    ("The Cardinal at North Hills SNF", "Tonya Hoffman", "03", 79026.36, False, "Scheduling"),
    ("Forest Ridge ALF", "Chad Vukelich", "03", 37968, False, "Scheduling"),
    ("ALG Mount Pleasant House Cross Sell", "Chad Vukelich", "03", 47460, True, "Scheduling"),
    ("Legacy Heights Senior Living Cross Sell", "Chad Vukelich", "03", 53155.2, True, "Scheduling"),
    ("Arbors At Fairlawn", "Adam Sabie", "03", 97437.6, False, "Scheduling"),
    ("OAKVIEW NURSING & REHAB CENTER", "Adam Sabie", "03", 84948, False, "Scheduling"),
    ("EST -Grey Stone Health & Rehab", "Jami Patterson", "03", 33979.2, True, "Scheduling"),
    ("McCoy Memorial Nursing Center", "Chad Vukelich", "01", 113677.2, False, "Established"),
    ("Rehabilitation Center of Cheraw", "Chad Vukelich", "01", 120173.04, False, "Established"),
    ("Seven Acres Senior Living", "Adam Sabie", "01", 48718.8, False, "Established"),
    ("Green Meadows Health and Rehab", "Adam Sabie", "01", 73078.2, False, "Established"),
    ("Signature HC of Terre Haute", "Adam Sabie", "01", 239875.2, False, "Established"),
    ("Richland Bean-Blossom HC Center", "Adam Sabie", "01", 120948, False, "Established"),
    ("Pinewood Nursing Care", "Chad Vukelich", "01", 73078.2, False, "Established"),
    ("ADDITIONAL CONSENTS- Trinity Grove", "Tonya Hoffman", "01", 45470.88, True, "Established"),
    ("Elderwood Rehab and Nursing Center", "Chad Vukelich", "01", 56838.6, False, "Established"),
    ("Elkhorn Health & Rehabilitation", "Adam Sabie", "01", 185010.6, False, "Established"),
    ("EST - Belmont Terrace", "Adam Sabie", "01", 146156.4, True, "Established"),
    ("EST - PruittHealth - Raleigh", "Tonya Hoffman", "01", 169896, True, "Established"),
    ("EST Gabriel Manor", "Tonya Hoffman", "01", 37968, True, "Established"),
    ("JAG Healthcare Mansfield", "Adam Sabie", "02", 126044.88, False, "Established"),
    ("EST - Elliott Nursing and Rehab", "Adam Sabie", "02", 146432.4, True, "Established"),
    ("Trinity Ridge PCP / NO MD", "Chad Vukelich", "02", 176691.84, False, "Established"),
    ("EST-Franklin Manor", "Tonya Hoffman", "02", 47460, True, "Established"),
    ("EST- Marquette Manor- Memory Care", "Gunner Grider", "02", 37516.8, True, "Established"),
    ("Lutheran Life Villages at Kendallville", "Jami Patterson", "02", 224859.6, False, "Established"),
    ("Brookdale Harrisonburg", "Melissa Been", "02", 47460, False, "Established"),
    ("Brookdale Lakeview Crossing", "Adam Sabie", "02", 84412.8, False, "Established"),
    ("Terra Bella- Little Ave", "Chad Vukelich", "02", 96141.6, False, "Established"),
    ("EST-Cardinal Landing Memory Care", "Samantha Roark", "02", 46896, True, "Established"),
    ("Willowbrook Healthcare Center", "Adam Sabie", "03", 40599, False, "Established"),
    ("Magnolia Springs Florence", "Adam Sabie", "03", 37516.8, False, "Established"),
    ("EST-Green Leaf Care Center", "Tonya Hoffman", "03", 66444, True, "Established"),
    ("EST - JAG Healthcare Shelby", "Jami Patterson", "03", 56838.6, True, "Established"),
]

months = {"01": 0.0, "02": 0.0, "03": 0.0}
for name, ae, m, ar, is_est, stage in items:
    months[m] += ar

total = sum(months.values())
ref = {"01": 1770000, "02": 1410000, "03": 1160000}

print("=== COMPLETE Q1 PULL (all groups, consent date) ===")
print(f"  Items: {len(items)}")
print()
labels = {"01": "January", "02": "February", "03": "March"}
for m in ["01", "02", "03"]:
    gap = ref[m] - months[m]
    pct = gap / ref[m] * 100
    print(f"  {labels[m]:<12} ${months[m]:>11,.0f}  ref ${ref[m]:>11,.0f}  gap ${gap:>9,.0f} ({pct:.0f}%)")
print(f"  {'Q1 Total':<12} ${total:>11,.0f}  ref ${sum(ref.values()):>11,.0f}  gap ${sum(ref.values())-total:>9,.0f}")

print()
missing = [
    ("Gallatin Nursing and Rehab", 205896),
    ("Trinity Village (LUTHERAN HOME)", 84445.92),
    ("Onslow House", 37968),
    ("EST- PruittHealth - Neuse", 146432.4),
    ("EST- PruittHealth - Trent", 160024.08),
    ("EST - JAG Healthcare Union City", 32479.2),
    ("Trinity Ridge (LUTHERAN HOME)", 64958.4),
    ("EST - Brookdale Wooster", 37968),
]
missing_ar = sum(x[1] for x in missing)

print("=== 8 ITEMS WITH NO CONSENT DATE (have op start in Q1) ===")
for x in missing:
    print(f"  {x[0]:<45} ${x[1]:>10,.0f}")
print(f"  {'Subtotal':<45} ${missing_ar:>10,.0f}")
print()
print(f"  Combined total: ${total + missing_ar:>11,.0f}")
print(f"  Reference:      ${sum(ref.values()):>11,.0f}")
print(f"  Final gap:      ${sum(ref.values()) - total - missing_ar:>11,.0f}")
