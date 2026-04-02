import sys
sys.stdout.reconfigure(encoding="utf-8")

mar = [
    ("EST-PruittHealth - Durham", "Tonya Hoffman", 246204.8, True, "Consenting"),
    ("OAKVIEW NURSING & REHAB CENTER", "Adam Sabie", 153878.0, False, "Scheduling"),
    ("The Cardinal at North Hills SNF", "Tonya Hoffman", 90355.46, False, "Scheduling"),
    ("EST- Waters of Wakarusa", "Jami Patterson", 72680.4, True, "Consenting"),
    ("Arbors At Fairlawn", "Adam Sabie", 72680.4, False, "Scheduling"),
    ("Chandler Park Assisted Living", "Samantha Roark", 70312.8, False, "Consenting"),
    ("EST -Grey Stone Health & Rehab", "Jami Patterson", 61551.2, True, "Scheduling"),
    ("EST-Green Leaf Care Center", "Tonya Hoffman", 50101.1, True, "Established"),
    ("EST - JAG Healthcare Shelby", "Jami Patterson", 42396.9, True, "Established"),
    ("Magnolia Springs Florence", "Adam Sabie", 41683.6, False, "Established"),
    ("Legacy Heights Senior Living Cross Sell", "Chad Vukelich", 40080.88, True, "Scheduling"),
    ("ALG Mount Pleasant House Cross Sell", "Chad Vukelich", 35786.5, True, "Scheduling"),
    ("EST -Grey Stone Health & Rehab", "Jami Patterson", 33979.2, True, "Scheduling"),
    ("Bickford of Carmel", "Gunner Grider", 31492.12, False, "Scheduling"),
    ("Willowbrook Healthcare Center", "Adam Sabie", 30283.5, False, "Established"),
    ("1019 Belles Place of Crawfordsville", "Gunner Grider", 28629.2, False, "Consenting"),
    ("Forest Ridge ALF", "Chad Vukelich", 28629.2, False, "Scheduling"),
]

total = sum(x[2] for x in mar)

print("=== MARCH — AR with New Assumptions ===")
print()
print(f"  {'Facility':<45} {'AE':<20} {'AR':>12} {'Stage':<12}")
print(f"  {'-'*45} {'-'*20} {'-'*12} {'-'*12}")
for name, ae, ar, is_est, stage in mar:
    est = " [EST]" if is_est else ""
    print(f"  {name + est:<45} {ae:<20} ${ar:>11,.0f} {stage:<12}")
print(f"  {'-'*45} {'-'*20} {'-'*12}")
print(f"  {'March Total':<45} {'':<20} ${total:>11,.0f}")
print(f"  {'Reference':<45} {'':<20} ${1160000:>11,.0f}")
print(f"  {'Gap':<45} {'':<20} ${1160000-total:>11,.0f}")
