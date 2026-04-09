"""Heritage Hall V23 Rescore -- READ-ONLY

Consolidates 3 entity IDs:
  37: HERITAGE HALL (10 SNF rows)
  1219: AMERICAN HEALTHCARE, LLC (11 rows: 6 SNF + 5 ALF)
  1220: AHC (2 rows: 1 ALF + 1 SNF, South Roanoke)

V23 formula: (ER x4) + (IR x3) + (SI x3) + (RP x4) + (RS x3) + (AI x3)
Max = 100. Tiers: T1 >= 55, T2 = 35-54, T3 < 35
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
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

HH = "corporate_entity_id IN (37, 1219, 1220)"
FP = "state IN ('NC','SC','VA','KY','OH','IN')"

# ==========================================
# 0. Raw facility listing
# ==========================================
print("=" * 120)
print("HERITAGE HALL - ALL FACILITIES (Entity IDs 37, 1219, 1220)")
print("=" * 120)
cur.execute(f"""
    SELECT
        corporate_entity_id,
        corporate_name_raw,
        facility_name,
        address,
        SPLIT_PART(address, ' ', 1) as street_num,
        city,
        state,
        source_type,
        total_beds,
        census,
        do_we_serve,
        integrated_flag,
        pcp_flag,
        mh_flag,
        barrier,
        geographic_tier
    FROM bd.market_intel_facilities
    WHERE {HH}
    ORDER BY corporate_entity_id, city, facility_name
""")
rows = cur.fetchall()
print(f"  Total rows: {len(rows)}")
print()
fmt = "{:>4} {:<28} {:<35} {:<8} {:<20} {:<3} {:<4} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:<20} {:<10}"
print(fmt.format("ID", "Corp Name", "Facility", "St#", "City", "ST", "Type", "Beds", "Cen", "Serve", "Int", "PCP", "MH", "Barrier", "GeoTier"))
print("-" * 200)
for r in rows:
    eid, corp, fac, addr, snum, city, st, stype, beds, cen, serve, integ, pcp, mh, barrier, geo = r
    print(fmt.format(
        eid,
        str(corp or "")[:28],
        str(fac or "")[:35],
        str(snum or "")[:8],
        str(city or "")[:20],
        str(st or ""),
        str(stype or ""),
        str(beds or 0),
        str(cen or 0),
        str(serve),
        str(integ),
        str(pcp),
        str(mh),
        str(barrier or "")[:20],
        str(geo or "")[:10]
    ))

# ==========================================
# 1. ER (Enterprise Reach) - Campus count
# ==========================================
print()
print("=" * 120)
print("1. ENTERPRISE REACH (ER) -- Campus Collapse by Street-Number + City")
print("=" * 120)

cur.execute(f"""
    SELECT
        LOWER(TRIM(SPLIT_PART(address, ' ', 1))) as street_num,
        LOWER(TRIM(city)) as city_norm,
        COUNT(*) as fac_count,
        STRING_AGG(DISTINCT source_type, ', ') as types,
        SUM(total_beds) as total_beds,
        STRING_AGG(DISTINCT facility_name, ' | ') as names
    FROM bd.market_intel_facilities
    WHERE {HH} AND {FP} AND total_beds > 15
    GROUP BY LOWER(TRIM(SPLIT_PART(address, ' ', 1))), LOWER(TRIM(city))
    ORDER BY city_norm
""")
campus_rows = cur.fetchall()
print(f"  Campuses (street_num + city, beds>15, footprint): {len(campus_rows)}")
print()
for i, cr in enumerate(campus_rows, 1):
    snum, city, fcount, types, beds, names = cr
    print(f"  Campus {i:>2}: {snum:<8} {city:<20} -- {fcount} fac(s), types={types}, beds={beds}")
    print(f"             {names}")

campus_count = len(campus_rows)
if campus_count >= 40:
    er = 5
elif campus_count >= 20:
    er = 4
elif campus_count >= 13:
    er = 3
elif campus_count >= 9:
    er = 2
else:
    er = 1
print(f"\n  Campus Count = {campus_count}  -->  ER Score = {er}")
print(f"  Brackets: <9=1, 9-12=2, 13-19=3, 20-39=4, >=40=5")

# ==========================================
# 2. IR (Integration Readiness)
# ==========================================
print()
print("=" * 120)
print("2. INTEGRATION READINESS (IR) -- Service Flag Counts")
print("=" * 120)
cur.execute(f"""
    SELECT
        COUNT(*) as total,
        COUNT(*) FILTER (WHERE integrated_flag = TRUE) as integ,
        COUNT(*) FILTER (WHERE pcp_flag = TRUE) as pcp,
        COUNT(*) FILTER (WHERE mh_flag = TRUE) as mh,
        COUNT(*) FILTER (WHERE do_we_serve = TRUE) as served
    FROM bd.market_intel_facilities
    WHERE {HH} AND {FP}
""")
total_fp, integ_c, pcp_c, mh_c, served_c = cur.fetchone()
print(f"  Footprint facilities: {total_fp}")
print(f"  Integrated: {integ_c} ({integ_c/total_fp:.0%})" if total_fp else "  N/A")
print(f"  PCP: {pcp_c} ({pcp_c/total_fp:.0%})" if total_fp else "  N/A")
print(f"  MH: {mh_c} ({mh_c/total_fp:.0%})" if total_fp else "  N/A")
print(f"  Served: {served_c} ({served_c/total_fp:.0%})" if total_fp else "  N/A")

flags_present = sum([integ_c > 0, pcp_c > 0, mh_c > 0])
int_pct = integ_c / total_fp if total_fp > 0 else 0
pcp_pct = pcp_c / total_fp if total_fp > 0 else 0
mh_pct = mh_c / total_fp if total_fp > 0 else 0
srv_pct = served_c / total_fp if total_fp > 0 else 0

if int_pct >= 0.5:
    ir = 5
elif int_pct >= 0.2:
    ir = 4
elif pcp_pct > 0 and mh_pct > 0:
    ir = 3
elif pcp_pct > 0 or mh_pct > 0:
    ir = 2
elif srv_pct > 0:
    ir = 2
else:
    ir = 1

print(f"\n  Flags present across portfolio: {flags_present} (integrated={integ_c>0}, pcp={pcp_c>0}, mh={mh_c>0})")
print(f"  IR Score = {ir}")

# ==========================================
# 3. RP (Revenue Potential) -- S2 Calculation
# ==========================================
print()
print("=" * 120)
print("3. REVENUE POTENTIAL (RP) -- S2 Fee Schedule")
print("=" * 120)

FEES_DETAIL = {
    'SNF': {'PCP': 3078.00, 'MH_adj': 605.50, 'CCM_adj': 108.00, 'SS_adj': 792.00, 'TOTAL': 4583.50},
    'ALF': {'PCP': 2084.00, 'MH_adj': 715.50, 'CCM_adj': 108.00, 'SS_adj': 792.00, 'TOTAL': 3699.50},
}
FEES_DETAIL['ILF'] = FEES_DETAIL['ALF']

cur.execute(f"""
    SELECT source_type, census, do_we_serve, integrated_flag, pcp_flag, mh_flag, barrier,
           facility_name, city
    FROM bd.market_intel_facilities
    WHERE {HH} AND {FP}
    ORDER BY city, facility_name
""")
fac_rows = cur.fetchall()

s2_current = 0.0
s2_integration = 0.0
s2_new_biz = 0.0

print(f"  Fee Schedule: SNF = $4,583.50/mo, ALF = $3,699.50/mo")
print()
fmt2 = "  {:<35} {:<18} {:<4} {:>5} {:>5} {:>4} {:>4} {:>4} {:<15} {:>12} {:>12} {:>12}"
print(fmt2.format("Facility", "City", "Type", "Cen", "Serve", "Int", "PCP", "MH", "Barrier", "Current", "Integ", "NewBiz"))
print("  " + "-" * 150)

for r in fac_rows:
    src_type, census_val, served, integ, pcp, mh, barrier, fac_name, city = r
    fee = FEES_DETAIL.get(src_type)
    if not fee:
        continue
    census = float(census_val) if census_val else 0
    has_barrier = bool(barrier)

    row_current = 0.0
    row_integ = 0.0
    row_newbiz = 0.0

    if served:
        if integ:
            row_current = census * fee['TOTAL']
        elif pcp:
            row_current = census * (fee['PCP'] + fee['CCM_adj'] + fee['SS_adj'])
        elif mh:
            row_current = census * fee['MH_adj']

        if not has_barrier:
            if not integ:
                if pcp:
                    row_integ = census * fee['MH_adj']
                elif mh:
                    row_integ = census * (fee['PCP'] + fee['CCM_adj'] + fee['SS_adj'])
    else:
        if not has_barrier:
            row_newbiz = census * fee['TOTAL']

    s2_current += row_current
    s2_integration += row_integ
    s2_new_biz += row_newbiz

    print(fmt2.format(
        str(fac_name or "")[:35],
        str(city or "")[:18],
        str(src_type),
        f"{census:.0f}",
        str(served),
        str(integ),
        str(pcp),
        str(mh),
        str(barrier or "")[:15],
        f"${row_current:,.0f}",
        f"${row_integ:,.0f}",
        f"${row_newbiz:,.0f}"
    ))

s2_total_pot = s2_integration + s2_new_biz
print("  " + "-" * 150)
print(f"  TOTALS:{' '*90} ${s2_current:>10,.0f} ${s2_integration:>10,.0f} ${s2_new_biz:>10,.0f}")
print(f"  Total Opportunity (Integration + New Biz) = ${s2_total_pot:,.0f}/mo")
print(f"  Annualized Total Opportunity = ${s2_total_pot*12:,.0f}/yr")

# RP brackets (user-specified)
rev = s2_total_pot
if rev >= 10_000_000:
    rp = 5
elif rev >= 5_000_000:
    rp = 4
elif rev >= 2_500_000:
    rp = 3
elif rev >= 1_000_000:
    rp = 2
else:
    rp = 1

print(f"\n  RP Score = {rp}")
print(f"  Brackets: <$1M=1, $1M-$2.5M=2, $2.5M-$5M=3, $5M-$10M=4, >=$10M=5")

# ==========================================
# 4. Facility Counts
# ==========================================
print()
print("=" * 120)
print("4. FACILITY COUNTS")
print("=" * 120)

cur.execute(f"SELECT COUNT(*) FROM bd.market_intel_facilities WHERE {HH}")
total_all = cur.fetchone()[0]

cur.execute(f"SELECT COUNT(*) FROM bd.market_intel_facilities WHERE {HH} AND {FP}")
total_fp_count = cur.fetchone()[0]

cur.execute(f"SELECT COUNT(*) FROM bd.market_intel_facilities WHERE {HH} AND do_we_serve = TRUE")
served_all = cur.fetchone()[0]

cur.execute(f"SELECT COUNT(*) FROM bd.market_intel_facilities WHERE {HH} AND {FP} AND do_we_serve = TRUE")
served_fp = cur.fetchone()[0]

cur.execute(f"SELECT COUNT(*) FROM bd.market_intel_facilities WHERE {HH} AND geographic_tier = 'A_Metro'")
metro_all = cur.fetchone()[0]

cur.execute(f"SELECT COUNT(*) FROM bd.market_intel_facilities WHERE {HH} AND {FP} AND geographic_tier = 'A_Metro'")
metro_fp = cur.fetchone()[0]

cur.execute(f"""
    SELECT source_type, COUNT(*), SUM(total_beds), SUM(census)
    FROM bd.market_intel_facilities
    WHERE {HH} AND {FP}
    GROUP BY source_type
    ORDER BY source_type
""")
type_rows = cur.fetchall()

cur.execute(f"""
    SELECT geographic_tier, COUNT(*)
    FROM bd.market_intel_facilities
    WHERE {HH} AND {FP}
    GROUP BY geographic_tier
    ORDER BY geographic_tier
""")
geo_rows = cur.fetchall()

print(f"  Total facilities (all states): {total_all}")
print(f"  Footprint facilities (SOM): {total_fp_count}")
print(f"  We Serve (all): {served_all}")
print(f"  We Serve (footprint): {served_fp}")
print(f"  Metro A_Metro (all): {metro_all}")
print(f"  Metro A_Metro (footprint): {metro_fp}")
print()
print(f"  By Type (footprint):")
for tr in type_rows:
    print(f"    {tr[0]}: {tr[1]} facilities, {tr[2]} beds, {tr[3]} census")
print()
print(f"  By Geographic Tier (footprint):")
for gr in geo_rows:
    print(f"    {gr[0]}: {gr[1]}")

# ==========================================
# 5. Revenue Breakdown
# ==========================================
print()
print("=" * 120)
print("5. REVENUE BREAKDOWN")
print("=" * 120)
print(f"  Integration $ (upsell served):     ${s2_integration:>12,.0f}/mo  (${s2_integration*12:>12,.0f}/yr)")
print(f"  New Business $ (unserved, no bar):  ${s2_new_biz:>12,.0f}/mo  (${s2_new_biz*12:>12,.0f}/yr)")
print(f"  Total Opportunity $:                ${s2_total_pot:>12,.0f}/mo  (${s2_total_pot*12:>12,.0f}/yr)")
print(f"  Current Revenue $ (served/active):  ${s2_current:>12,.0f}/mo  (${s2_current*12:>12,.0f}/yr)")

# ==========================================
# 6. Qualitative Dimensions (SI, RS, AI)
# ==========================================
print()
print("=" * 120)
print("6. QUALITATIVE DIMENSIONS (SI, RS, AI)")
print("=" * 120)

cur.execute(f"""
    SELECT facility_name, city, do_we_serve, integrated_flag, pcp_flag, mh_flag
    FROM bd.market_intel_facilities
    WHERE {HH} AND do_we_serve = TRUE
    ORDER BY city
""")
served_detail = cur.fetchall()
print(f"  SERVED FACILITIES ({len(served_detail)}):")
for sd in served_detail:
    print(f"    {str(sd[0] or ''):<35} {str(sd[1] or ''):<18} Int={sd[3]} PCP={sd[4]} MH={sd[5]}")

si_suggested = 2
print(f"\n  SI (Strategic Influence) -- SUGGESTED: {si_suggested}")
print(f"    Rationale: 16-campus SNF chain, rural/exurban VA only.")
print(f"    No REIT, ISNP, or ACO affiliations known.")
print(f"    Regional presence but limited strategic leverage outside VA.")
print(f"    Score 2 = regional operator with moderate influence.")

# RS - based on served/campus ratio
rs_served_ratio = served_fp / campus_count if campus_count > 0 else 0
if rs_served_ratio >= 0.8:
    rs = 5
elif rs_served_ratio >= 0.5:
    rs = 4
elif rs_served_ratio >= 0.25:
    rs = 3
elif served_fp > 0:
    rs = 2
else:
    rs = 1

print(f"\n  RS (Relationship Strength)")
print(f"    Served: {served_fp}/{campus_count} campuses = {rs_served_ratio:.0%}")
print(f"    RS Score = {rs}")
print(f"    Brackets: >=80%=5, 50-79%=4, 25-49%=3, >0=2, 0=1")

ai = 0
print(f"\n  AI (AI/Tech Adoption) = {ai} (no V20 Brooke scores, default)")

# ==========================================
# 7. FINAL V23 COMPOSITE SCORE
# ==========================================
print()
print("=" * 120)
print("7. FINAL V23 COMPOSITE SCORE")
print("=" * 120)

total_score = (er * 4) + (ir * 3) + (si_suggested * 3) + (rp * 4) + (rs * 3) + (ai * 3)
if total_score >= 55:
    tier = "T1"
elif total_score >= 35:
    tier = "T2"
else:
    tier = "T3"

print(f"  ER (Enterprise Reach)       = {er}  x4 = {er*4}")
print(f"  IR (Integration Readiness)  = {ir}  x3 = {ir*3}")
print(f"  SI (Strategic Influence)    = {si_suggested}  x3 = {si_suggested*3}")
print(f"  RP (Revenue Potential)      = {rp}  x4 = {rp*4}")
print(f"  RS (Relationship Strength)  = {rs}  x3 = {rs*3}")
print(f"  AI (AI/Tech Adoption)       = {ai}  x3 = {ai*3}")
print(f"  ---")
print(f"  TOTAL = ({er}x4) + ({ir}x3) + ({si_suggested}x3) + ({rp}x4) + ({rs}x3) + ({ai}x3)")
print(f"        = {er*4} + {ir*3} + {si_suggested*3} + {rp*4} + {rs*3} + {ai*3}")
print(f"        = {total_score}")
print(f"  TIER  = {tier}")
print(f"  Tier brackets: T1>=55, T2=35-54, T3<35")

print()
print("=" * 120)
print("MONDAY.COM BOARD UPDATE VALUES")
print("=" * 120)
print(f"  Entity: Heritage Hall (consolidated)")
print(f"  Entity IDs: 37, 1219, 1220")
print(f"  ER: {er}")
print(f"  IR: {ir}")
print(f"  SI: {si_suggested} (suggested)")
print(f"  RP: {rp}")
print(f"  RS: {rs}")
print(f"  AI: {ai}")
print(f"  Total Score: {total_score}")
print(f"  Tier: {tier}")
print(f"  Campuses (footprint): {campus_count}")
print(f"  Facilities (footprint): {total_fp_count}")
print(f"  Served: {served_fp}")
print(f"  S2 Total Opportunity: ${s2_total_pot:,.0f}/mo (${s2_total_pot*12:,.0f}/yr)")
print(f"  S2 Integration Rev: ${s2_integration:,.0f}/mo")
print(f"  S2 New Biz Rev: ${s2_new_biz:,.0f}/mo")
print(f"  S2 Current Rev: ${s2_current:,.0f}/mo")

cur.close()
conn.close()
print()
print("DONE -- READ-ONLY, no data modified.")
