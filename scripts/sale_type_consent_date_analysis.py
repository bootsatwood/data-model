"""
Sale Type AR Analysis — Q1 2026
Using Expected Consent Date (date_mktmmhbq) as the bucketing column.
Pulls from ALL stages, not just Established.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

# ALL items with Q1 expected consent dates, across ALL stages
items = [
    # ESTABLISHED (consent date in Jan)
    ("McCoy Memorial Nursing Center", "Chad Vukelich", "2026-01-05", 113677.2, False, "Established"),
    ("Rehabilitation Center of Cheraw", "Chad Vukelich", "2026-01-05", 120173.04, False, "Established"),
    ("Seven Acres Senior Living", "Adam Sabie", "2026-01-06", 48718.8, False, "Established"),
    ("Green Meadows Health and Rehabilitation", "Adam Sabie", "2026-01-08", 73078.2, False, "Established"),
    ("Signature Health Care of Terre Haute", "Adam Sabie", "2026-01-02", 239875.2, False, "Established"),
    ("Richland Bean-Blossom Health Care Center", "Adam Sabie", "2026-01-02", 120948, False, "Established"),
    ("Pinewood Nursing Care", "Chad Vukelich", "2026-01-02", 73078.2, False, "Established"),
    ("ADDITIONAL CONSENTS- Trinity Grove", "Tonya Hoffman", "2026-01-15", 45470.88, True, "Established"),
    ("Elderwood Rehabilitation and Nursing Center", "Chad Vukelich", "2026-01-16", 56838.6, False, "Established"),
    ("Elkhorn Health & Rehabilitation", "Adam Sabie", "2026-01-13", 185010.6, False, "Established"),
    ("EST - Belmont Terrace", "Adam Sabie", "2026-01-30", 146156.4, True, "Established"),
    ("EST - PruittHealth - Raleigh", "Tonya Hoffman", "2026-01-20", 169896, True, "Established"),
    ("EST Gabriel Manor", "Tonya Hoffman", "2026-01-15", 37968, True, "Established"),
    # ESTABLISHED (consent date in Feb)
    ("JAG Healthcare Mansfield", "Adam Sabie", "2026-02-02", 126044.88, False, "Established"),
    ("EST - Elliott Nursing and Rehabilitation", "Adam Sabie", "2026-02-19", 146432.4, True, "Established"),
    ("Trinity Ridge PCP / NO MD", "Chad Vukelich", "2026-02-16", 176691.84, False, "Established"),
    ("EST-Franklin Manor", "Tonya Hoffman", "2026-02-20", 47460, True, "Established"),
    ("EST- Marquette Manor- Memory Care", "Gunner Grider", "2026-02-26", 37516.8, True, "Established"),
    ("Lutheran Life Villages at Kendallville", "Jami Patterson", "2026-02-18", 224859.6, False, "Established"),
    ("Brookdale Harrisonburg", "Melissa Been", "2026-02-19", 47460, False, "Established"),
    ("Brookdale Lakeview Crossing", "Adam Sabie", "2026-02-16", 84412.8, False, "Established"),
    ("Terra Bella- Little Ave", "Chad Vukelich", "2026-02-26", 96141.6, False, "Established"),
    ("EST-Cardinal Landing Memory Care", "Samantha Roark", "2026-02-19", 46896, True, "Established"),
    # ESTABLISHED (consent date in Mar)
    ("Willowbrook Healthcare Center", "Adam Sabie", "2026-03-23", 40599, False, "Established"),
    ("Magnolia Springs Florence", "Adam Sabie", "2026-03-09", 37516.8, False, "Established"),
    ("EST-Green Leaf Care Center", "Tonya Hoffman", "2026-03-11", 66444, True, "Established"),
    ("EST - JAG Healthcare Shelby", "Jami Patterson", "2026-03-04", 56838.6, True, "Established"),
    # SCHEDULING
    ("Bickford of Carmel", "Gunner Grider", "2026-03-10", 41764.8, False, "Scheduling"),
    ("The Cardinal at North Hills SNF", "Tonya Hoffman", "2026-03-09", 79026.36, False, "Scheduling"),
    ("Forest Ridge ALF", "Chad Vukelich", "2026-03-05", 37968, False, "Scheduling"),
    ("ALG Mount Pleasant House Cross Sell", "Chad Vukelich", "2026-03-20", 47460, True, "Scheduling"),
    ("Legacy Heights Senior Living - Cross Sell", "Chad Vukelich", "2026-03-19", 53155.2, True, "Scheduling"),
    ("Arbors At Fairlawn", "Adam Sabie", "2026-03-10", 97437.6, False, "Scheduling"),
    ("OAKVIEW NURSING & REHAB CENTER", "Adam Sabie", "2026-03-16", 84948, False, "Scheduling"),
    ("EST -Grey Stone Health & Rehab", "Jami Patterson", "2026-03-20", 33979.2, True, "Scheduling"),
    # CONSENTING
    ("Chandler Park Assisted Living", "Samantha Roark", "2026-03-10", 75484.8, False, "Consenting"),
    ("EST- Waters of Wakarusa", "Jami Patterson", "2026-03-23", 97437.6, True, "Consenting"),
    ("1019 Belles Place of Crawfordsville", "Gunner Grider", "2026-03-27", 37968, False, "Consenting"),
    ("EST-PruittHealth - Durham", "Tonya Hoffman", "2026-03-30", 135916.8, True, "Consenting"),
]

# Items with operational start in Q1 but NO expected consent date populated
no_consent_date = [
    ("Gallatin Nursing and Rehab", "Adam Sabie", 205896, False),
    ("Trinity Village (LUTHERAN HOME)", "Chad Vukelich", 84445.92, False),
    ("Onslow House", "Tonya Hoffman", 37968, False),
    ("EST- PruittHealth - Neuse", "Tonya Hoffman", 146432.4, True),
    ("EST- PruittHealth - Trent", "Tonya Hoffman", 160024.08, True),
    ("EST - JAG Healthcare Union City", "Jami Patterson", 32479.2, True),
    ("Trinity Ridge (LUTHERAN HOME)", "Chad Vukelich", 64958.4, False),
    ("EST - Brookdale Wooster", "Adam Sabie", 37968, True),
]

# Monthly totals
months = {"01": 0.0, "02": 0.0, "03": 0.0}
for name, ae, date, ar, is_est, stage in items:
    m = date[5:7]
    months[m] += ar

total = sum(months.values())
ref = {"01": 1770000, "02": 1410000, "03": 1160000}
ref_total = sum(ref.values())
no_consent_ar = sum(x[2] for x in no_consent_date)

print("=== MONTHLY AR BY EXPECTED CONSENT DATE ===")
print(f"  January:  ${months['01']:>12,.0f}")
print(f"  February: ${months['02']:>12,.0f}")
print(f"  March:    ${months['03']:>12,.0f}")
print(f"  Q1 Total: ${total:>12,.0f}")
print()
print("=== YOUR REFERENCE ===")
print(f"  January:  $  1,770,000")
print(f"  February: $  1,410,000")
print(f"  March:    $  1,160,000")
print(f"  Q1 Total: $  4,340,000")
print()
print("=== GAP ===")
for m in ["01", "02", "03"]:
    gap = ref[m] - months[m]
    pct = gap / ref[m] * 100 if ref[m] else 0
    label = ["Jan", "Feb", "Mar"][int(m) - 1]
    print(f"  {label}: ${gap:>10,.0f} ({pct:.0f}%)")
print(f"  Total gap: ${ref_total - total:>10,.0f}")
print()

print("=== 8 ITEMS WITH NO CONSENT DATE (have op start in Q1) ===")
for x in no_consent_date:
    est = " [EST]" if x[3] else ""
    print(f"  {x[0]}{est} | {x[1]} | AR: ${x[2]:,.0f}")
print(f"  Subtotal: ${no_consent_ar:,.0f}")
print(f"  If added: ${total + no_consent_ar:,.0f} (vs ref ${ref_total:,.0f})")
print(f"  Remaining gap: ${ref_total - total - no_consent_ar:,.0f}")
print()

print("=== BY STAGE ===")
for stage in ["Established", "Scheduling", "Consenting"]:
    si = [i for i in items if i[5] == stage]
    print(f"  {stage}: {len(si)} items, ${sum(i[3] for i in si):,.0f}")
print(f"  No consent date: {len(no_consent_date)} items, ${no_consent_ar:,.0f}")
print(f"  Grand total: {len(items) + len(no_consent_date)} items")
