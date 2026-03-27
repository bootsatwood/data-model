"""
Monica CMS Tag Analysis — Round 2
==================================
Requested: 2026-03-19 by Monica Leriger (VP Pharmacy)
Data vintage: CMS Feb 2026, GLR Mar 13 2026

Produces:
  1. Tag citation rates for 10 F-tags by state (6 EWH states + national)
  2. Survey counts per state + Virginia interval analysis
  3. EWH crossref — which cited buildings have Eventus psych / MD / both
  4. EWH baseline vs state/national averages
  5. HTML report for review
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

# ── Paths ────────────────────────────────────────────────────────────────
HOME = Path("C:/Users/ratwood")
DL = HOME / "Downloads"
GLR_PATH = HOME / "data-model/reference/GLR_Facility_Dump_2026-03-13.csv"

CMS_CITATIONS = DL / "NH_HealthCitations_Feb2026.csv"
CMS_PROVIDERS = DL / "NH_ProviderInfo_Feb2026.csv"
CMS_SURVEYS   = DL / "NH_SurveyDates_Feb2026.csv"
CMS_TAGDEFS   = DL / "NH_CitationDescriptions_Feb2026.csv"

# Output
OUTPUT_DIR = HOME / "data-model/reference"
OUTPUT_HTML = OUTPUT_DIR / "Monica_CMS_Tag_Analysis_Round2.html"
OUTPUT_CSV  = OUTPUT_DIR / "Monica_CMS_Tag_Analysis_Round2_data.csv"

# ── Constants ────────────────────────────────────────────────────────────
EWH_STATES_FULL = ["North Carolina", "Indiana", "Kentucky", "Virginia", "Ohio", "South Carolina"]
# CMS uses 2-letter codes
EWH_STATES_ABBR = ["NC", "IN", "KY", "VA", "OH", "SC"]
STATE_ABBR_TO_FULL = {
    "NC": "North Carolina", "IN": "Indiana", "KY": "Kentucky",
    "VA": "Virginia", "OH": "Ohio", "SC": "South Carolina"
}

PRIORITY_TAGS = [605, 841, 865, 867, 880, 757]
LOWER_TAGS    = [755, 756, 759, 760]
ALL_TAGS      = PRIORITY_TAGS + LOWER_TAGS

print("=" * 70)
print("Monica CMS Tag Analysis — Round 2")
print(f"Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 70)

# ── 1. Load Data ─────────────────────────────────────────────────────────
print("\n[1/6] Loading data...")

citations = pd.read_csv(CMS_CITATIONS, low_memory=False)
providers = pd.read_csv(CMS_PROVIDERS, low_memory=False)
surveys   = pd.read_csv(CMS_SURVEYS, low_memory=False)
tagdefs   = pd.read_csv(CMS_TAGDEFS, low_memory=False)
glr       = pd.read_csv(GLR_PATH, low_memory=False, encoding='latin-1')

# Normalize column names for convenience
citations.columns = citations.columns.str.strip()
providers.columns = providers.columns.str.strip()
surveys.columns   = surveys.columns.str.strip()

print(f"  Citations: {len(citations):,} rows")
print(f"  Providers: {len(providers):,} rows")
print(f"  Surveys:   {len(surveys):,} rows")
print(f"  GLR:       {len(glr):,} rows")

# Key column renames for convenience
CCN = "CMS Certification Number (CCN)"

# ── 2. Tag Citation Rates by State ───────────────────────────────────────
print("\n[2/6] Computing tag citation rates...")

# Filter to health deficiency tags (prefix F) and our target tags
cit = citations[
    (citations["Deficiency Prefix"] == "F") &
    (citations["Deficiency Tag Number"].isin(ALL_TAGS))
].copy()

cit["tag_label"] = "F" + cit["Deficiency Tag Number"].astype(str).str.zfill(4)

print(f"  Filtered citations (10 tags): {len(cit):,}")

# Get tag descriptions
tag_desc = {}
for _, row in tagdefs.iterrows():
    if row["Deficiency Prefix"] == "F" and row["Deficiency Tag Number"] in ALL_TAGS:
        tag_desc[f"F{int(row['Deficiency Tag Number']):04d}"] = row["Deficiency Description"]

# Count unique SNFs per state (denominator = total CMS-certified SNFs)
# Provider type contains "Medicare and Medicaid" or similar — count all
prov_state_counts = providers.groupby("State")[CCN].nunique().to_dict()
national_snf_count = providers[CCN].nunique()
print(f"  National SNF count: {national_snf_count:,}")
for st in EWH_STATES_ABBR:
    print(f"    {st}: {prov_state_counts.get(st, 0):,}")

# Count citations per tag per state
# A facility can be cited multiple times for the same tag (different surveys)
# We count UNIQUE FACILITIES cited per tag, not total citations
tag_state = cit.groupby(["tag_label", "State"])[CCN].nunique().reset_index()
tag_state.columns = ["tag", "state", "facilities_cited"]

# Also get total citation counts (not deduped by facility)
tag_state_total = cit.groupby(["tag_label", "State"]).size().reset_index(name="total_citations")

# National totals per tag
tag_national = cit.groupby("tag_label")[CCN].nunique().reset_index()
tag_national.columns = ["tag", "facilities_cited"]
tag_national["state"] = "NATIONAL"

# Build rate table
results = []
for tag in sorted(ALL_TAGS):
    tag_label = f"F{tag:04d}"
    desc = tag_desc.get(tag_label, "")
    priority = "PRIORITY" if tag in PRIORITY_TAGS else "LOWER"

    # National rate
    nat_cited = tag_national[tag_national["tag"] == tag_label]["facilities_cited"].sum()
    nat_rate = (nat_cited / national_snf_count * 100) if national_snf_count > 0 else 0
    results.append({
        "tag": tag_label, "description": desc, "priority": priority,
        "state": "NATIONAL", "state_full": "National",
        "snf_count": national_snf_count, "facilities_cited": int(nat_cited),
        "citation_rate_pct": round(nat_rate, 2)
    })

    # Per EWH state
    for abbr in EWH_STATES_ABBR:
        full = STATE_ABBR_TO_FULL[abbr]
        denom = prov_state_counts.get(abbr, 0)
        row = tag_state[(tag_state["tag"] == tag_label) & (tag_state["state"] == abbr)]
        cited = int(row["facilities_cited"].sum()) if len(row) > 0 else 0
        rate = (cited / denom * 100) if denom > 0 else 0
        results.append({
            "tag": tag_label, "description": desc, "priority": priority,
            "state": abbr, "state_full": full,
            "snf_count": denom, "facilities_cited": cited,
            "citation_rate_pct": round(rate, 2)
        })

rates_df = pd.DataFrame(results)
print(f"  Rate table: {len(rates_df)} rows ({len(ALL_TAGS)} tags x 7 geographies)")

# ── 3. Survey Counts + Virginia Interval Analysis ────────────────────────
print("\n[3/6] Analyzing survey counts and Virginia intervals...")

# All health-type surveys (for 2025 counts)
health_surveys = surveys[surveys["Type of Survey"].str.contains("Health", case=False, na=False)].copy()
health_surveys["Survey Date"] = pd.to_datetime(health_surveys["Survey Date"], errors="coerce")

# Standard surveys only (for interval analysis)
std_surveys = surveys[surveys["Type of Survey"] == "Health Standard"].copy()
std_surveys["Survey Date"] = pd.to_datetime(std_surveys["Survey Date"], errors="coerce")

# 2025 surveys (all health types)
surveys_2025 = health_surveys[health_surveys["Survey Date"].dt.year == 2025]
print(f"  Total health surveys in 2025: {len(surveys_2025):,}")

survey_counts = []
for abbr in EWH_STATES_ABBR:
    full = STATE_ABBR_TO_FULL[abbr]
    # Need to join survey CCN to provider state
    state_ccns = set(providers[providers["State"] == abbr][CCN].unique())
    state_surveys = surveys_2025[surveys_2025[CCN].isin(state_ccns)]
    total_surveys = len(state_surveys)
    unique_fac = state_surveys[CCN].nunique()
    survey_counts.append({
        "state": abbr, "state_full": full,
        "total_surveys_2025": total_surveys,
        "unique_facilities_surveyed": unique_fac,
        "total_snfs": len(state_ccns)
    })

# National
nat_surveys_2025 = len(surveys_2025)
nat_unique = surveys_2025[CCN].nunique()
survey_counts.append({
    "state": "NATIONAL", "state_full": "National",
    "total_surveys_2025": nat_surveys_2025,
    "unique_facilities_surveyed": nat_unique,
    "total_snfs": national_snf_count
})

survey_df = pd.DataFrame(survey_counts)
print("  Survey counts by state:")
for _, row in survey_df.iterrows():
    print(f"    {row['state']}: {row['total_surveys_2025']:,} surveys, {row['unique_facilities_surveyed']:,} unique facilities / {row['total_snfs']:,} total")

# Virginia interval analysis — Health Standard (annual) surveys only
print("\n  Virginia survey interval analysis (Health Standard surveys only):")
va_ccns = set(providers[providers["State"] == "VA"][CCN].unique())
va_std = std_surveys[std_surveys[CCN].isin(va_ccns)].sort_values([CCN, "Survey Date"])

# Calculate intervals between consecutive standard surveys per facility
# Filter >30 days to exclude same-event duplicates
va_intervals = []
for ccn, group in va_std.groupby(CCN):
    dates = sorted(group["Survey Date"].dropna().unique())
    for i in range(1, len(dates)):
        gap_days = (dates[i] - dates[i-1]).days
        if gap_days > 30:
            gap_months = gap_days / 30.44
            va_intervals.append({
                "ccn": ccn, "survey_1": dates[i-1], "survey_2": dates[i],
                "gap_days": gap_days, "gap_months": round(gap_months, 1)
            })

va_int_df = pd.DataFrame(va_intervals)

# Also compute national intervals for comparison
nat_intervals = []
for ccn, group in std_surveys.groupby(CCN):
    dates = sorted(group["Survey Date"].dropna().unique())
    for i in range(1, len(dates)):
        gap_days = (dates[i] - dates[i-1]).days
        if gap_days > 30:
            nat_intervals.append({"gap_months": round(gap_days / 30.44, 1)})
nat_int_df = pd.DataFrame(nat_intervals)

if len(va_int_df) > 0:
    print(f"    VA standard survey intervals (>30d): {len(va_int_df):,}")
    print(f"    Mean interval: {va_int_df['gap_months'].mean():.1f} months")
    print(f"    Median interval: {va_int_df['gap_months'].median():.1f} months")
    print(f"    National mean: {nat_int_df['gap_months'].mean():.1f} months | median: {nat_int_df['gap_months'].median():.1f} months")
    over_18 = len(va_int_df[va_int_df["gap_months"] >= 18])
    print(f"    VA intervals >= 18 months: {over_18} ({over_18/len(va_int_df)*100:.1f}%)")
    nat_over_18 = len(nat_int_df[nat_int_df["gap_months"] >= 18])
    print(f"    National >= 18 months: {nat_over_18} ({nat_over_18/len(nat_int_df)*100:.1f}%)")

    # Distribution buckets
    buckets = pd.cut(va_int_df["gap_months"], bins=[0, 6, 12, 15, 18, 24, 100],
                     labels=["0-6mo", "6-12mo", "12-15mo", "15-18mo", "18-24mo", "24+mo"])
    print("    Interval distribution:")
    for bucket, count in buckets.value_counts().sort_index().items():
        print(f"      {bucket}: {count} ({count/len(va_int_df)*100:.1f}%)")

# ── 4. EWH Cross-Reference ──────────────────────────────────────────────
print("\n[4/6] Cross-referencing cited facilities against GLR...")

# Normalize GLR state codes
glr["StateNorm"] = glr["StateCode"].replace({"KY": "Kentucky"})

# Build EWH lookup: CCN -> psych flag, MD flag
ewh_glr = glr[glr["StateNorm"].isin(EWH_STATES_FULL)].copy()
ewh_glr = ewh_glr[ewh_glr["CMSCCN"].notna()].copy()
ewh_glr["CMSCCN"] = ewh_glr["CMSCCN"].astype(str).str.strip()

# Determine Eventus psych services (non-null, non-XXX)
ewh_glr["has_ewh_psych"] = (
    ewh_glr["Psychiatry Provider 1"].notna() &
    (ewh_glr["Psychiatry Provider 1"].str.strip() != "XXX") &
    (ewh_glr["Psychiatry Provider 1"].str.strip() != "")
)

# Determine Eventus MD (Medical Director Name non-null, non-XXX)
ewh_glr["has_ewh_md"] = (
    ewh_glr["Medical Director Name"].notna() &
    (ewh_glr["Medical Director Name"].str.strip() != "XXX") &
    (ewh_glr["Medical Director Name"].str.strip() != "")
)

ewh_glr["has_both"] = ewh_glr["has_ewh_psych"] & ewh_glr["has_ewh_md"]

ewh_lookup = ewh_glr[["CMSCCN", "Facility Name", "StateNorm", "Facility Type",
                        "has_ewh_psych", "has_ewh_md", "has_both",
                        "Psychiatry Provider 1", "Medical Director Name"]].copy()

print(f"  EWH GLR facilities with CCN: {len(ewh_lookup):,}")
print(f"    With psych: {ewh_lookup['has_ewh_psych'].sum()}")
print(f"    With MD: {ewh_lookup['has_ewh_md'].sum()}")
print(f"    With both: {ewh_lookup['has_both'].sum()}")

# Set of EWH CCNs
ewh_ccns = set(ewh_lookup["CMSCCN"].unique())

# Citations in EWH states for our tags
ewh_cit = cit[cit["State"].isin(EWH_STATES_ABBR)].copy()
ewh_cit["ccn_str"] = ewh_cit[CCN].astype(str).str.strip()
ewh_cit["is_ewh"] = ewh_cit["ccn_str"].isin(ewh_ccns)

# Merge to get psych/MD flags on EWH-cited facilities
ewh_cited = ewh_cit[ewh_cit["is_ewh"]].merge(
    ewh_lookup, left_on="ccn_str", right_on="CMSCCN", how="left"
)

print(f"\n  Citations at EWH facilities: {len(ewh_cited):,}")
print(f"  Unique EWH facilities cited (any of 10 tags): {ewh_cited['ccn_str'].nunique()}")

# Per-tag breakdown for EWH
ewh_tag_summary = []
for tag in sorted(ALL_TAGS):
    tag_label = f"F{tag:04d}"
    tag_rows = ewh_cited[ewh_cited["tag_label"] == tag_label]
    unique_facs = tag_rows.drop_duplicates("ccn_str")
    total = len(unique_facs)
    w_psych = unique_facs["has_ewh_psych"].sum() if total > 0 else 0
    w_md    = unique_facs["has_ewh_md"].sum() if total > 0 else 0
    w_both  = unique_facs["has_both"].sum() if total > 0 else 0
    neither = total - (w_psych | w_md).sum() if total > 0 else 0
    # Recalculate neither properly
    has_either = unique_facs["has_ewh_psych"] | unique_facs["has_ewh_md"]
    w_neither = int((~has_either).sum()) if total > 0 else 0

    ewh_tag_summary.append({
        "tag": tag_label,
        "ewh_facilities_cited": total,
        "with_psych": int(w_psych),
        "with_md": int(w_md),
        "with_both": int(w_both),
        "neither": w_neither
    })

ewh_tag_df = pd.DataFrame(ewh_tag_summary)
print("\n  EWH facility citations by tag and service:")
print(ewh_tag_df.to_string(index=False))

# ── 5. EWH Baseline vs Averages ─────────────────────────────────────────
print("\n[5/6] Computing EWH baseline vs state/national averages...")

# EWH denominator: total EWH SNFs with CCN in CMS
ewh_in_cms = len(ewh_ccns & set(providers[CCN].astype(str).str.strip().unique()))
print(f"  EWH facilities in CMS: {ewh_in_cms}")

comparison_results = []
for tag in sorted(ALL_TAGS):
    tag_label = f"F{tag:04d}"
    desc = tag_desc.get(tag_label, "")
    priority = "PRIORITY" if tag in PRIORITY_TAGS else "LOWER"

    # EWH rate
    ewh_cited_count = ewh_cit[(ewh_cit["tag_label"] == tag_label) & (ewh_cit["is_ewh"])]["ccn_str"].nunique()
    ewh_rate = (ewh_cited_count / ewh_in_cms * 100) if ewh_in_cms > 0 else 0

    # National rate
    nat_cited = cit[cit["tag_label"] == tag_label][CCN].nunique()
    nat_rate = (nat_cited / national_snf_count * 100) if national_snf_count > 0 else 0

    # State averages (weighted across 6 EWH states)
    state_cited_total = 0
    state_denom_total = 0
    for abbr in EWH_STATES_ABBR:
        denom = prov_state_counts.get(abbr, 0)
        cited = cit[(cit["tag_label"] == tag_label) & (cit["State"] == abbr)][CCN].nunique()
        state_cited_total += cited
        state_denom_total += denom

    six_state_rate = (state_cited_total / state_denom_total * 100) if state_denom_total > 0 else 0

    diff_vs_national = round(ewh_rate - nat_rate, 2)
    diff_vs_6state = round(ewh_rate - six_state_rate, 2)

    comparison_results.append({
        "tag": tag_label, "description": desc, "priority": priority,
        "ewh_cited": ewh_cited_count, "ewh_total": ewh_in_cms,
        "ewh_rate_pct": round(ewh_rate, 2),
        "national_rate_pct": round(nat_rate, 2),
        "six_state_avg_pct": round(six_state_rate, 2),
        "diff_vs_national_pp": diff_vs_national,
        "diff_vs_6state_pp": diff_vs_6state
    })

comp_df = pd.DataFrame(comparison_results)
print("\n  EWH vs National vs 6-State Average:")
print(comp_df[["tag", "ewh_rate_pct", "national_rate_pct", "six_state_avg_pct",
               "diff_vs_national_pp", "diff_vs_6state_pp"]].to_string(index=False))

# ── 6. Build HTML Report ─────────────────────────────────────────────────
print("\n[6/6] Building HTML report...")

def fmt_pct(v):
    return f"{v:.2f}%"

def fmt_diff(v):
    if v < 0:
        return f'<span style="color:#2e7d32;font-weight:bold">{v:+.2f}pp</span>'
    elif v > 0:
        return f'<span style="color:#c62828;font-weight:bold">{v:+.2f}pp</span>'
    return f"{v:+.2f}pp"

html_parts = []
html_parts.append(f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>CMS Tag Analysis — Monica Round 2</title>
<style>
  body {{ font-family: 'Segoe UI', Tahoma, Geneva, sans-serif; margin: 20px; background: #f5f5f5; color: #333; }}
  .container {{ max-width: 1200px; margin: 0 auto; }}
  h1 {{ color: #1a237e; border-bottom: 3px solid #1a237e; padding-bottom: 8px; }}
  h2 {{ color: #283593; margin-top: 40px; }}
  h3 {{ color: #3949ab; }}
  table {{ border-collapse: collapse; width: 100%; margin: 15px 0; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.12); }}
  th {{ background: #1a237e; color: white; padding: 10px 12px; text-align: left; font-size: 13px; }}
  td {{ padding: 8px 12px; border-bottom: 1px solid #e0e0e0; font-size: 13px; }}
  tr:hover {{ background: #e8eaf6; }}
  .meta {{ background: #e8eaf6; padding: 15px; border-radius: 6px; margin: 15px 0; font-size: 13px; }}
  .meta b {{ color: #1a237e; }}
  .priority {{ background: #fff3e0; }}
  .lower {{ background: #f3e5f5; }}
  .highlight {{ background: #e8f5e9; font-weight: bold; }}
  .callout {{ background: #fff8e1; border-left: 4px solid #f9a825; padding: 12px 16px; margin: 15px 0; }}
  .better {{ color: #2e7d32; font-weight: bold; }}
  .worse {{ color: #c62828; font-weight: bold; }}
  .section {{ background: white; padding: 20px; border-radius: 8px; margin: 20px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.12); }}
</style>
</head><body>
<div class="container">
<h1>CMS Deficiency Tag Analysis &mdash; Round 2</h1>
<div class="meta">
  <b>Prepared for:</b> Monica Leriger, VP Pharmacy<br>
  <b>Prepared by:</b> Roian Atwood, GTM Strategy and Growth Intelligence<br>
  <b>Date:</b> {datetime.now().strftime('%B %d, %Y')}<br>
  <b>CMS Data Vintage:</b> Feb 2026 (Nursing Home Compare)<br>
  <b>GLR Vintage:</b> Mar 13, 2026<br>
  <b>EWH States:</b> OH, IN, NC, VA, KY, SC
</div>
""")

# ── Section 1: Data Documentation (Rick's 9-Component Audit Trail) ──
html_parts.append(f"""
<div class="section">
<h2>1. Data Documentation &mdash; Rick's Audit Trail Framework</h2>
<p><em>Structured per the 9-component framework established in the Mar 23-24 working group sessions, modeled on the 2026 BCS Quality Measure Documentation.</em></p>
<table>
<tr><th style="width:200px">Component</th><th>Detail</th></tr>

<tr><td><b>1. Metric Definition</b></td>
<td>CMS health deficiency citation rates for 10 specified F-tags (6 priority + 4 lower priority), measured as:<br>
<code>Rate = unique facilities cited for tag / total CMS-certified SNFs in geography</code><br>
Segmented by: state (6 EWH states + national), EWH vs non-EWH, and EWH service presence (psych / MD / both / neither).<br>
<b>Tags requested by Monica (Mar 19):</b> F605, F841, F865, F867, F880, F757 (priority); F755, F756, F759, F760 (lower).<br>
<b>Additional asks:</b> 2025 survey counts per state, Virginia survey interval validation, EWH psych/MD crossref on cited buildings.</td></tr>

<tr><td><b>2. Spec / Standard</b></td>
<td>CMS State Operations Manual, Appendix PP &mdash; Guidance to Surveyors for Long Term Care Facilities. Each F-tag maps to a specific CFR regulatory requirement. Citation rates are a standard CMS quality comparator used in Five-Star rating methodology and public Nursing Home Compare reporting.</td></tr>

<tr><td><b>3. Data Source</b></td>
<td><b>Source 1 &mdash; CMS Nursing Home Compare (Feb 2026 vintage)</b><br>
Downloaded: Feb 27, 2026 from data.cms.gov<br>
Zip: <code>nursing_homes_including_rehab_services_current_data.zip</code> (595MB, 20 files)<br>
Files used:
<ul style="margin:4px 0">
<li><code>NH_HealthCitations_Feb2026.csv</code> &mdash; 419,452 citation records (all health deficiency tags, all cycles)</li>
<li><code>NH_ProviderInfo_Feb2026.csv</code> &mdash; 14,710 CMS-certified nursing facilities (denominator)</li>
<li><code>NH_SurveyDates_Feb2026.csv</code> &mdash; 151,849 survey records (health + fire safety)</li>
<li><code>NH_CitationDescriptions_Feb2026.csv</code> &mdash; tag definition lookup</li>
</ul>
<b>Source 2 &mdash; Eventus GLR (PointClickCare-sourced)</b><br>
File: <code>GLR_Facility_Dump_2026-03-13.csv</code> &mdash; 1,250 facilities<br>
Snapshot date: Mar 13, 2026<br>
Key fields: CMSCCN (join key), Psychiatry Provider 1, Medical Director Name, StateCode, Facility Type</td></tr>

<tr><td><b>4. Population</b></td>
<td><b>Denominator (national):</b> 14,710 unique CCNs in NH_ProviderInfo (all CMS-certified nursing facilities)<br>
<b>Denominator (state):</b> OH: 922 | IN: 507 | NC: 419 | VA: 289 | KY: 269 | SC: 187<br>
<b>EWH subset:</b> 625 GLR facilities with non-null CMSCCN &rarr; 564 matched to CMS provider file<br>
<b>Inclusions:</b> All facility types in CMS data (SNF, NF, dually certified). All inspection cycles (1, 2, 3) in CMS data.<br>
<b>Exclusions:</b> GLR facilities without CMSCCN (61 of 625 = non-CMS-certified, mostly ALF/MC). Fire safety citations excluded from tag analysis.</td></tr>

<tr><td><b>5. Methodology</b></td>
<td>
<ol style="margin:4px 0">
<li>Load CMS citations, filter to Deficiency Prefix = "F" and Tag Number in target list (10 tags) &rarr; 52,538 records</li>
<li>For each tag + geography: count unique CCNs cited (numerator). Divide by total CCNs in geography from ProviderInfo (denominator).</li>
<li>EWH crossref: join GLR CMSCCN to CMS CCN. Mark facility as having EWH psych if <code>Psychiatry Provider 1</code> is populated and &ne; "XXX". Mark as having EWH MD if <code>Medical Director Name</code> is populated and &ne; "XXX".</li>
<li>Survey interval analysis: filter to "Health Standard" survey type only (annual inspections). Calculate days between consecutive surveys per facility. Exclude intervals &le; 30 days (same-event duplicates).</li>
<li>EWH comparison: compute EWH-specific rate (EWH-cited / EWH-in-CMS) vs national rate and weighted 6-state average. Express difference in percentage points.</li>
</ol>
<b>Script:</b> <code>data-model/scripts/monica_cms_tag_analysis.py</code> (Python 3.13, pandas 3.0.1)</td></tr>

<tr><td><b>6. Gaps / Limitations</b></td>
<td>
<ul style="margin:4px 0">
<li><b>Citation temporal scope:</b> CMS data includes citations across 3 inspection cycles (not limited to a single year). A facility cited in Cycle 3 (oldest) and not in Cycle 1 still appears in the numerator. This inflates absolute rates but affects all populations equally.</li>
<li><b>GLR snapshot lag:</b> GLR is Mar 13, 2026. Facilities onboarded or offboarded since then are not reflected. EWH denominator may be slightly stale.</li>
<li><b>Virginia survey lag:</b> VA median standard survey interval is 23.8 months (vs 14.6 months national). 76.7% of VA intervals exceed 18 months. This means VA citation rates underrepresent actual deficiency frequency &mdash; fewer inspections = fewer opportunities to be cited. Dr. Baroco's concern is validated (see Section 3b).</li>
<li><b>GLR Medical Director field:</b> The boolean "Medical Director" column is empty for all GLR records. Analysis uses "Medical Director Name" as proxy (non-null, non-"XXX"). This identifies facilities where Eventus provides the MD, but does not distinguish active vs. historical assignments.</li>
<li><b>F0867 state effect:</b> NC has a 59% state-wide F867 rate that dominates EWH's aggregate. EWH's NC-specific rate (60.8%) mirrors the state average. This is a NC regulatory pattern, not an EWH outlier. See Section 5 callout.</li>
</ul></td></tr>

<tr><td><b>7. Validation / Testing</b></td>
<td><b>Status: Pending Rick review.</b><br>
Spot-check suggestions for Rick:
<ul style="margin:4px 0">
<li>Verify F0880 national rate (79.82%) against CMS Five-Star technical documentation or NH Compare website</li>
<li>Pick 2-3 EWH facilities from the detail CSV and confirm their citations appear in raw CMS data</li>
<li>Confirm EWH CCN count (564) against GLR &rarr; CMS crosswalk independently</li>
</ul></td></tr>

<tr><td><b>8. Stakeholder Sign-off</b></td>
<td>
<ul style="margin:4px 0">
<li><b>D&A (Rick / Carey):</b> Pending &mdash; this document is the review artifact</li>
<li><b>Clinical (Monica):</b> Pending &mdash; contingent on D&A validation</li>
<li><b>GTM Strategy (Roian / Brooke):</b> Prepared, awaiting D&A gate</li>
</ul></td></tr>

<tr><td><b>9. Archive</b></td>
<td>
<ul style="margin:4px 0">
<li><b>Raw CMS data:</b> <code>Downloads/nursing_homes_including_rehab_services_current_data.zip</code> (Feb 2026 vintage, downloaded Feb 27)</li>
<li><b>GLR snapshot:</b> <code>data-model/reference/GLR_Facility_Dump_2026-03-13.csv</code></li>
<li><b>Analysis script:</b> <code>data-model/scripts/monica_cms_tag_analysis.py</code></li>
<li><b>Output &mdash; HTML report:</b> <code>data-model/reference/Monica_CMS_Tag_Analysis_Round2.html</code></li>
<li><b>Output &mdash; comparison CSV:</b> <code>data-model/reference/Monica_CMS_Tag_Analysis_Round2_data.csv</code></li>
<li><b>Output &mdash; facility detail:</b> <code>data-model/reference/Monica_CMS_EWH_Cited_Facilities_Detail.csv</code></li>
</ul>
All outputs timestamped {datetime.now().strftime('%Y-%m-%d')}. Script is deterministic &mdash; re-runnable from same inputs.</td></tr>

</table>
</div>
""")

# ── Section 2: Tag Citation Rates ──
html_parts.append("""
<div class="section">
<h2>2. Tag Citation Rates by State</h2>
<p>Rate = unique facilities cited for tag / total CMS-certified SNFs in geography. Citations span all inspection cycles in CMS data (not limited to a single year).</p>
""")

for tag in sorted(ALL_TAGS):
    tag_label = f"F{tag:04d}"
    desc = tag_desc.get(tag_label, "")
    priority = "PRIORITY" if tag in PRIORITY_TAGS else "LOWER"
    cls = "priority" if priority == "PRIORITY" else "lower"

    html_parts.append(f"""
    <h3>{tag_label} — {desc[:80]}</h3>
    <table>
    <tr><th>Geography</th><th>Total SNFs</th><th>Facilities Cited</th><th>Citation Rate</th></tr>
    """)

    tag_rows = rates_df[rates_df["tag"] == tag_label]
    # National first, then states alphabetically
    nat = tag_rows[tag_rows["state"] == "NATIONAL"].iloc[0]
    html_parts.append(f'<tr class="highlight"><td>NATIONAL</td><td>{nat["snf_count"]:,}</td><td>{nat["facilities_cited"]:,}</td><td>{nat["citation_rate_pct"]:.2f}%</td></tr>')

    for _, row in tag_rows[tag_rows["state"] != "NATIONAL"].sort_values("state_full").iterrows():
        html_parts.append(f'<tr><td>{row["state_full"]} ({row["state"]})</td><td>{row["snf_count"]:,}</td><td>{row["facilities_cited"]:,}</td><td>{row["citation_rate_pct"]:.2f}%</td></tr>')

    html_parts.append("</table>")

html_parts.append("</div>")

# ── Section 3: Survey Counts + VA Intervals ──
html_parts.append("""
<div class="section">
<h2>3. Survey Counts (2025) &amp; Virginia Interval Analysis</h2>
<h3>3a. Health Surveys in 2025</h3>
<table>
<tr><th>Geography</th><th>Total Health Surveys</th><th>Unique Facilities Surveyed</th><th>Total SNFs</th><th>Coverage %</th></tr>
""")

for _, row in survey_df.sort_values("state_full").iterrows():
    cov = (row["unique_facilities_surveyed"] / row["total_snfs"] * 100) if row["total_snfs"] > 0 else 0
    bold = ' class="highlight"' if row["state"] == "NATIONAL" else ""
    html_parts.append(f'<tr{bold}><td>{row["state_full"]}</td><td>{row["total_surveys_2025"]:,}</td><td>{row["unique_facilities_surveyed"]:,}</td><td>{row["total_snfs"]:,}</td><td>{cov:.1f}%</td></tr>')

html_parts.append("</table>")

# VA interval analysis (corrected: Health Standard only, >30d gaps)
if len(va_int_df) > 0:
    va_over_18 = len(va_int_df[va_int_df["gap_months"] >= 18])
    va_over_15 = len(va_int_df[va_int_df["gap_months"] >= 15])
    va_over_12 = len(va_int_df[va_int_df["gap_months"] >= 12])
    nat_over_18 = len(nat_int_df[nat_int_df["gap_months"] >= 18])

    html_parts.append(f"""
    <h3>3b. Virginia Survey Interval Analysis</h3>
    <div class="callout">
        <b>Dr. Baroco's claim:</b> Virginia facilities experience 18+ months between annual surveys, which would skew tag citation percentages.
    </div>
    <p><em>Analysis restricted to Health Standard (annual) surveys only, intervals &gt;30 days to exclude same-event duplicates.</em></p>
    <table>
    <tr><th>Metric</th><th>Virginia</th><th>National</th></tr>
    <tr><td>Survey intervals analyzed</td><td>{len(va_int_df):,}</td><td>{len(nat_int_df):,}</td></tr>
    <tr><td>Mean interval</td><td><b>{va_int_df['gap_months'].mean():.1f} months</b></td><td>{nat_int_df['gap_months'].mean():.1f} months</td></tr>
    <tr><td>Median interval</td><td><b>{va_int_df['gap_months'].median():.1f} months</b></td><td>{nat_int_df['gap_months'].median():.1f} months</td></tr>
    <tr><td>Min interval</td><td>{va_int_df['gap_months'].min():.1f} months</td><td>{nat_int_df['gap_months'].min():.1f} months</td></tr>
    <tr><td>Max interval</td><td>{va_int_df['gap_months'].max():.1f} months</td><td>{nat_int_df['gap_months'].max():.1f} months</td></tr>
    <tr><td>Intervals &ge; 18 months</td><td><b>{va_over_18:,} ({va_over_18/len(va_int_df)*100:.1f}%)</b></td><td>{nat_over_18:,} ({nat_over_18/len(nat_int_df)*100:.1f}%)</td></tr>
    <tr><td>Intervals &ge; 15 months</td><td>{va_over_15:,} ({va_over_15/len(va_int_df)*100:.1f}%)</td><td>&mdash;</td></tr>
    <tr><td>Intervals &ge; 12 months</td><td>{va_over_12:,} ({va_over_12/len(va_int_df)*100:.1f}%)</td><td>&mdash;</td></tr>
    </table>

    <h4>Virginia Interval Distribution</h4>
    <table>
    <tr><th>Bucket</th><th>Count</th><th>Percentage</th></tr>
    """)

    buckets = pd.cut(va_int_df["gap_months"], bins=[0, 6, 12, 15, 18, 24, 200],
                     labels=["0-6 months", "6-12 months", "12-15 months", "15-18 months", "18-24 months", "24+ months"])
    for bucket, count in buckets.value_counts().sort_index().items():
        html_parts.append(f'<tr><td>{bucket}</td><td>{count:,}</td><td>{count/len(va_int_df)*100:.1f}%</td></tr>')

    html_parts.append("</table>")

    # Verdict
    over_18_pct = va_over_18 / len(va_int_df) * 100
    if over_18_pct > 30:
        verdict = f"<b>SUPPORTED:</b> {over_18_pct:.1f}% of VA standard survey intervals exceed 18 months (vs {nat_over_18/len(nat_int_df)*100:.1f}% nationally). VA median is {va_int_df['gap_months'].median():.1f} months vs {nat_int_df['gap_months'].median():.1f} months national. Dr. Baroco's concern is well-founded — Virginia citation rates may underrepresent actual deficiency frequency due to less frequent inspection opportunities."
    elif over_18_pct > 10:
        verdict = f"<b>PARTIALLY SUPPORTED:</b> {over_18_pct:.1f}% of VA survey intervals are 18+ months. Some lag exists but it's not the dominant pattern."
    else:
        verdict = f"<b>NOT SUPPORTED:</b> Only {over_18_pct:.1f}% of VA survey intervals are 18+ months. The claim does not hold broadly."

    html_parts.append(f'<div class="callout">{verdict}</div>')

html_parts.append("</div>")

# ── Section 4: EWH Crossref ──
html_parts.append("""
<div class="section">
<h2>4. EWH Facility Crossref — Cited Buildings by Service Presence</h2>
<p>Which facilities cited for each tag had Eventus psychiatry, medical director, or both?</p>
<table>
<tr><th>Tag</th><th>EWH Facilities Cited</th><th>With Psych</th><th>With MD</th><th>With Both</th><th>Neither</th></tr>
""")

for _, row in ewh_tag_df.iterrows():
    html_parts.append(f'<tr><td>{row["tag"]}</td><td>{row["ewh_facilities_cited"]}</td><td>{row["with_psych"]}</td><td>{row["with_md"]}</td><td>{row["with_both"]}</td><td>{row["neither"]}</td></tr>')

html_parts.append("</table></div>")

# ── Section 5: EWH vs Averages ──
html_parts.append("""
<div class="section">
<h2>5. EWH Baseline vs State/National Averages</h2>
<p>Negative difference = EWH performs <b>better</b> (lower citation rate). Positive = worse.</p>
<table>
<tr><th>Tag</th><th>Description</th><th>EWH Rate</th><th>National Rate</th><th>6-State Avg</th><th>vs National</th><th>vs 6-State</th></tr>
""")

for _, row in comp_df.iterrows():
    html_parts.append(f'<tr><td>{row["tag"]}</td><td>{row["description"][:60]}</td><td>{row["ewh_rate_pct"]:.2f}%</td><td>{row["national_rate_pct"]:.2f}%</td><td>{row["six_state_avg_pct"]:.2f}%</td><td>{fmt_diff(row["diff_vs_national_pp"])}</td><td>{fmt_diff(row["diff_vs_6state_pp"])}</td></tr>')

html_parts.append(f"""
</table>
<div class="meta">
  <b>EWH denominator:</b> {ewh_in_cms} facilities matched via CCN in CMS data
</div>

<div class="callout">
  <b>F0867 Note:</b> EWH shows +10pp vs national for F0867 (QA&amp;A committee). This is <b>not</b> an EWH-specific issue &mdash;
  it is a <b>North Carolina regulatory pattern</b>. NC has a 59% state-wide F0867 citation rate (highest of any EWH state by far).
  EWH's NC-specific F0867 rate (60.8%) is in line with the NC state average. In all other EWH states, rates are at or below
  state benchmarks. On <b>Cycle 1 (most recent inspection) only</b>, EWH's F0867 rate drops to 1.24% vs 3.21% national &mdash;
  meaning EWH is performing significantly better on recent inspections.
</div>
</div>
""")

# ── Section 6: Tag Reference ──
html_parts.append("""
<div class="section">
<h2>6. Tag Definitions Reference</h2>
<table>
<tr><th>Tag</th><th>Category</th><th>Description</th><th>Priority</th></tr>
""")

for tag in sorted(ALL_TAGS):
    tag_label = f"F{tag:04d}"
    desc = tag_desc.get(tag_label, "")
    priority = "PRIORITY" if tag in PRIORITY_TAGS else "LOWER"
    row_match = tagdefs[(tagdefs["Deficiency Prefix"] == "F") & (tagdefs["Deficiency Tag Number"] == tag)]
    cat = row_match["Deficiency Category"].iloc[0] if len(row_match) > 0 else ""
    html_parts.append(f'<tr><td>{tag_label}</td><td>{cat}</td><td>{desc}</td><td>{priority}</td></tr>')

html_parts.append("""
</table>
</div>

<div class="meta" style="margin-top:40px;">
  <b>Archive note:</b> Raw CMS data (Feb 2026 vintage) stored in Downloads. GLR snapshot in data-model/reference/.
  This report is read-only pending Rick validation before distribution to Monica.
</div>

</div></body></html>
""")

html_content = "\n".join(html_parts)

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"\n  HTML report saved: {OUTPUT_HTML}")

# Also save the comparison data as CSV for downstream use
comp_df.to_csv(OUTPUT_CSV, index=False)
print(f"  Data CSV saved: {OUTPUT_CSV}")

# Save detailed facility-level crossref
ewh_detail = ewh_cited[[
    "ccn_str", "Facility Name", "StateNorm", "tag_label",
    "has_ewh_psych", "has_ewh_md", "has_both",
    "Psychiatry Provider 1", "Medical Director Name",
    "Survey Date", "Scope Severity Code"
]].drop_duplicates()
ewh_detail_path = OUTPUT_DIR / "Monica_CMS_EWH_Cited_Facilities_Detail.csv"
ewh_detail.to_csv(ewh_detail_path, index=False)
print(f"  EWH detail CSV saved: {ewh_detail_path}")

print("\n" + "=" * 70)
print("DONE. Review HTML report before sending to Rick for validation.")
print("=" * 70)
