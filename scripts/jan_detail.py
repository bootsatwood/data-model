import sys
sys.stdout.reconfigure(encoding="utf-8")

jan = [
    ("Signature HC of Terre Haute", "Adam Sabie", 405307.2, False),
    ("EST - PruittHealth - Raleigh", "Tonya Hoffman", 307756.0, True),
    ("Elkhorn Health & Rehabilitation", "Adam Sabie", 291876.1, False),
    ("Richland Bean-Blossom HC Center", "Adam Sabie", 189878.0, False),
    ("EST - Belmont Terrace", "Adam Sabie", 109020.6, True),
    ("Rehabilitation Center of Cheraw", "Chad Vukelich", 89639.16, False),
    ("McCoy Memorial Nursing Center", "Chad Vukelich", 84793.8, False),
    ("Green Meadows Health and Rehab", "Adam Sabie", 54510.3, False),
    ("Pinewood Nursing Care", "Chad Vukelich", 54510.3, False),
    ("EST - Signature HC of Terre Haute", "Adam Sabie", 42396.9, True),
    ("Elderwood Rehab and Nursing Center", "Chad Vukelich", 42396.9, False),
    ("Seven Acres Senior Living", "Adam Sabie", 36340.2, False),
    ("ADDITIONAL CONSENTS- Trinity Grove", "Tonya Hoffman", 33917.52, True),
    ("EST Gabriel Manor", "Tonya Hoffman", 28629.2, True),
]

total = sum(x[2] for x in jan)

print("=== JANUARY — AR with New Assumptions ===")
print()
print(f"  {'Facility':<45} {'AE':<20} {'AR':>12}")
print(f"  {'-'*45} {'-'*20} {'-'*12}")
for name, ae, ar, is_est in jan:
    est = " [EST]" if is_est else ""
    print(f"  {name + est:<45} {ae:<20} ${ar:>11,.0f}")
print(f"  {'-'*45} {'-'*20} {'-'*12}")
print(f"  {'January Total':<45} {'':<20} ${total:>11,.0f}")
print(f"  {'Reference':<45} {'':<20} ${1770000:>11,.0f}")
print(f"  {'Gap':<45} {'':<20} ${1770000-total:>11,.0f}")
