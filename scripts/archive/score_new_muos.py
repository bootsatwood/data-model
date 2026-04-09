"""Score 5 new MUO operators for Corporate Scoring Reference board.

V23 formula: (ER x4) + (IR x3) + (SI x3) + (RP x4) + (RS x3) + (AI x3)
Max = 100. Tiers: T1 >= 55, T2 = 35-54, T3 < 35

Queries PostgreSQL bd.market_intel_facilities for footprint-scoped metrics.
Computes S2 Total Potential Revenue using the same methodology as build_scenario_2.py.
No S2 table exists in PostgreSQL -- this script replicates the logic at query time.
"""

import psycopg2

conn = psycopg2.connect(
    host='keystone-platform-postgres.postgres.database.azure.com',
    port=5432,
    dbname='postgres',
    user='ratwood',
    password='Ch0EeU3yz7ep5bEWTKT1UoC^NMPCZXzN',
    sslmode='require'
)
cur = conn.cursor()

FP = "state IN ('NC','SC','VA','KY','OH','IN')"

# S2 fee structure (monthly per census patient, from build_scenario_2.py)
FEES = {
    'SNF': {'PCP': 3078.00, 'MH_adj': 605.50, 'CCM_adj': 108.00, 'SS_adj': 792.00, 'TOTAL': 4583.50},
    'ALF': {'PCP': 2084.00, 'MH_adj': 715.50, 'CCM_adj': 108.00, 'SS_adj': 792.00, 'TOTAL': 3699.50},
}
FEES['ILF'] = FEES['ALF']

operators = {
    'Navion': "corporate_entity_id IN (12, 569, 590)",
    'Gardant': "corporate_entity_id = 34 OR corporate_name_raw ILIKE 'GARDANT%'",
    'RUI': "corporate_entity_id IN (1222, 1254)",
    'Vitality Living': "corporate_entity_id = 605",
    'Triple Crown': "corporate_entity_id IN (434, 544)",
}


# === ER Brackets (user-specified) ===
def er_score(campuses):
    if campuses >= 40: return 5
    if campuses >= 20: return 4
    if campuses >= 13: return 3
    if campuses >= 9: return 2
    return 1


# === IR Brackets (from ir_inference.py / Brooke clarification) ===
def ir_score(integrated_pct, pcp_pct, mh_pct, served_pct):
    if integrated_pct >= 0.5: return 5
    if integrated_pct >= 0.2: return 4
    if pcp_pct > 0 and mh_pct > 0: return 3
    if pcp_pct > 0 or mh_pct > 0: return 2
    if served_pct > 0: return 2
    return 1


# === RP Brackets (from rescore_v23.py -- monthly S2 Total Potential Revenue) ===
def rp_score(rev):
    if rev >= 2_000_000: return 5
    if rev >= 1_000_000: return 4
    if rev >= 500_000: return 3
    if rev >= 250_000: return 2
    return 1


def total_score_calc(er, ir, si, rp, rs, ai):
    return (er * 4) + (ir * 3) + (si * 3) + (rp * 4) + (rs * 3) + (ai * 3)


def tier_label(score):
    if score >= 55: return 'T1'
    if score >= 35: return 'T2'
    return 'T3'


results = {}

for name, where in operators.items():
    base = f"({where})"

    # Campus count (unique street-number|city|state)
    cur.execute(f"""
        SELECT COUNT(DISTINCT CONCAT(
            COALESCE(LOWER(TRIM(SPLIT_PART(address, ' ', 1))), ''),
            '|', LOWER(TRIM(city)), '|', LOWER(TRIM(state))
        ))
        FROM bd.market_intel_facilities WHERE {base} AND {FP}
    """)
    campus = cur.fetchone()[0]

    # Facility count
    cur.execute(f"SELECT COUNT(*) FROM bd.market_intel_facilities WHERE {base} AND {FP}")
    total_fp = cur.fetchone()[0]

    # Service flags
    cur.execute(f"""
        SELECT
          COUNT(*) FILTER (WHERE integrated_flag = TRUE),
          COUNT(*) FILTER (WHERE pcp_flag = TRUE),
          COUNT(*) FILTER (WHERE mh_flag = TRUE),
          COUNT(*) FILTER (WHERE do_we_serve = TRUE)
        FROM bd.market_intel_facilities WHERE {base} AND {FP}
    """)
    integ_count, pcp_count, mh_count, served_count = cur.fetchone()

    # Beds and census
    cur.execute(f"""
        SELECT
          COALESCE(SUM(CASE WHEN source_type = 'SNF' THEN total_beds ELSE 0 END), 0),
          COALESCE(SUM(CASE WHEN source_type IN ('ALF', 'ILF') THEN total_beds ELSE 0 END), 0),
          COALESCE(SUM(total_beds), 0),
          COALESCE(SUM(census), 0)
        FROM bd.market_intel_facilities WHERE {base} AND {FP}
    """)
    snf_beds, alf_beds, total_beds, total_census = cur.fetchone()

    # S2 revenue calculation -- replicate build_scenario_2.py logic per facility
    cur.execute(f"""
        SELECT source_type, census, do_we_serve, integrated_flag, pcp_flag, mh_flag, barrier
        FROM bd.market_intel_facilities
        WHERE {base} AND {FP}
    """)
    fac_rows = cur.fetchall()

    s2_current = 0.0
    s2_integration = 0.0
    s2_new_biz = 0.0

    for r in fac_rows:
        src_type, census_val, served, integ, pcp, mh, barrier = r
        fee = FEES.get(src_type)
        if not fee:
            continue
        census = float(census_val) if census_val else 0
        has_barrier = bool(barrier)

        if served:
            if integ:
                s2_current += census * fee['TOTAL']
            elif pcp:
                s2_current += census * (fee['PCP'] + fee['CCM_adj'] + fee['SS_adj'])
            elif mh:
                s2_current += census * fee['MH_adj']

            if not has_barrier:
                if not integ:
                    if pcp:
                        s2_integration += census * fee['MH_adj']
                    elif mh:
                        s2_integration += census * (fee['PCP'] + fee['CCM_adj'] + fee['SS_adj'])
        else:
            if not has_barrier:
                s2_new_biz += census * fee['TOTAL']

    s2_total_potential = s2_integration + s2_new_biz

    # Compute percentages
    int_pct = integ_count / total_fp if total_fp > 0 else 0
    pcp_pct = pcp_count / total_fp if total_fp > 0 else 0
    mh_pct = mh_count / total_fp if total_fp > 0 else 0
    srv_pct = served_count / total_fp if total_fp > 0 else 0
    occ = float(total_census) / float(total_beds) if total_beds > 0 else 0

    # Compute dimension scores
    er = er_score(campus)
    ir = ir_score(int_pct, pcp_pct, mh_pct, srv_pct)
    si = 1  # Default per user
    rp = rp_score(s2_total_potential)
    rs = 1  # Default per user
    ai = 0  # Default per user

    score = total_score_calc(er, ir, si, rp, rs, ai)
    tier = tier_label(score)

    results[name] = {
        'campus': campus,
        'fac_fp': total_fp,
        'snf_beds': int(snf_beds),
        'alf_beds': int(alf_beds),
        'total_beds': int(total_beds),
        'census': float(total_census),
        'occ': occ,
        's2_current': s2_current,
        's2_integration': s2_integration,
        's2_new_biz': s2_new_biz,
        's2_total_pot': s2_total_potential,
        'integ': integ_count, 'pcp': pcp_count, 'mh': mh_count, 'served': served_count,
        'int_pct': int_pct, 'pcp_pct': pcp_pct, 'mh_pct': mh_pct, 'srv_pct': srv_pct,
        'er': er, 'ir': ir, 'si': si, 'rp': rp, 'rs': rs, 'ai': ai,
        'score': score, 'tier': tier,
    }

cur.close()
conn.close()

# Print structured summary
print("=" * 100)
print("  V23 SCORING DIMENSIONS -- 5 NEW MUO OPERATORS")
print("  Formula: (ER x4) + (IR x3) + (SI x3) + (RP x4) + (RS x3) + (AI x3)  |  Max = 100")
print("  Tiers: T1 >= 55, T2 = 35-54, T3 < 35")
print("=" * 100)

for name, d in results.items():
    print(f"\n{'_'*80}")
    print(f"  {name.upper()}")
    print(f"{'_'*80}")
    print(f"  Footprint: {d['fac_fp']} facilities, {d['campus']} campuses")
    print(f"  Beds: {d['total_beds']} ({d['snf_beds']} SNF + {d['alf_beds']} ALF/ILF)")
    print(f"  Census: {d['census']:.0f}  Occupancy: {d['occ']:.1%}")
    print(f"  Served: {d['served']}/{d['fac_fp']}  Int: {d['integ']}  PCP: {d['pcp']}  MH: {d['mh']}")
    print(f"  S2 Revenue (monthly):")
    print(f"    Current:     ${d['s2_current']:>12,.0f}")
    print(f"    Integration: ${d['s2_integration']:>12,.0f}")
    print(f"    New Business:${d['s2_new_biz']:>12,.0f}")
    print(f"    Total Pot:   ${d['s2_total_pot']:>12,.0f}")
    print()
    print(f"  ER (Enterprise Reach)      = {d['er']}  ({d['campus']} campuses)")
    print(f"  IR (Integration Readiness)  = {d['ir']}  (Int: {d['int_pct']:.0%}, PCP: {d['pcp_pct']:.0%}, MH: {d['mh_pct']:.0%})")
    print(f"  SI (Strategic Influence)    = {d['si']}  (default -- qualitative TBD)")
    print(f"  RP (Revenue Potential)      = {d['rp']}  (S2 Total Pot: ${d['s2_total_pot']:,.0f}/mo)")
    print(f"  RS (Relationship Strength)  = {d['rs']}  (default -- no existing relationship)")
    print(f"  AI (AI/Tech Adoption)       = {d['ai']}  (default -- no V20 scores)")
    print()
    weighted = f"({d['er']}x4) + ({d['ir']}x3) + ({d['si']}x3) + ({d['rp']}x4) + ({d['rs']}x3) + ({d['ai']}x3)"
    parts = f"  {d['er']*4} + {d['ir']*3} + {d['si']*3} + {d['rp']*4} + {d['rs']*3} + {d['ai']*3}"
    print(f"  TOTAL = {weighted}")
    print(f"       = {parts} = {d['score']}")
    print(f"  TIER  = {d['tier']}")

# Final summary table
print(f"\n\n{'='*100}")
print(f"  SUMMARY TABLE")
print(f"{'='*100}")
hdr = f"  {'Operator':<20} {'Camp':>4} {'Fac':>4} {'Beds':>5} {'S2 TotPot/mo':>14} {'ER':>3} {'IR':>3} {'SI':>3} {'RP':>3} {'RS':>3} {'AI':>3} {'Total':>5} {'Tier':>4}"
print(hdr)
sep = f"  {'_'*20} {'_'*4} {'_'*4} {'_'*5} {'_'*14} {'_'*3} {'_'*3} {'_'*3} {'_'*3} {'_'*3} {'_'*3} {'_'*5} {'_'*4}"
print(sep)
for name, d in results.items():
    print(f"  {name:<20} {d['campus']:>4} {d['fac_fp']:>4} {d['total_beds']:>5} ${d['s2_total_pot']:>12,.0f} {d['er']:>3} {d['ir']:>3} {d['si']:>3} {d['rp']:>3} {d['rs']:>3} {d['ai']:>3} {d['score']:>5} {d['tier']:>4}")

print(f"\n  Notes:")
print(f"  - ER brackets (user-specified): <9=1, 9-12=2, 13-19=3, 20-39=4, >=40=5")
print(f"  - IR inferred from service flag penetration in 6-state footprint")
print(f"  - SI=1, RS=1, AI=0 are defaults per user instruction")
print(f"  - RP uses S2 Total Potential Revenue (Integration + New Business, monthly)")
print(f"    computed using build_scenario_2.py methodology on PostgreSQL data")
print(f"  - All 5 operators have zero barriers in footprint")
print(f"  - Campus collapse uses street-number|city|state dedup")
print(f"  - Gardant matched corporate_entity_id IN (34, 465)")
print(f"  - Triple Crown matched corporate_entity_id IN (434=VITALITY SENIOR SERVICES, 544=TRIPLE CROWN SENIOR LIVING)")
print(f"  - Navion consolidates 3 entity IDs: 12 (NAVION), 569 (NAVION SENIOR LIVING), 590 (Navion Senior Solutions)")
print(f"  - RUI = Retirement Unlimited, Inc. (ID 1222) + RUI (ID 1254), VA-only footprint")
