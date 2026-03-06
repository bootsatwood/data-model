# V22.3 -> V22.4: Corporate Name Deduplication

**Date:** 2026-03-05
**Script:** `scripts/corporate_dedup_fix.py`
**Input:** `1_Combined_Database_FINAL_V22_3.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_4.xlsx`
**Analysis:** `scripts/corporate_name_dedup.py` + manual RA coding

---

## Summary

The Corporate Name Dedup analysis (4-pass fuzzy matching) found 743 potential duplicate pairs across 4,166 distinct Corporate_Names. Priority filtering (top 70 corporates + served facilities) reduced this to 157 pairs for manual review. RA coded all 157 with web research to validate matches.

This version applies confirmed consolidations only. Unresolved pairs remain as-is for future research.

## Method

1. **Automated detection** via `corporate_name_dedup.py` (4 passes: norm_corp exact, containment, token overlap, edit distance)
2. **Priority filtering** to top-70 + served facilities (743 -> 157 pairs)
3. **Manual RA coding** with web research validation (website cross-referencing, facility address matching, GLR verification)
4. **Script application** via `corporate_dedup_fix.py` — renames + facility reattributions + Four-Rule rerun

## Corporate Name Consolidations

### Lutheran Cluster (10 renames)

| Old Name | Canonical Name | Evidence |
|---|---|---|
| Luther Care Services | LUTHERCARE | Same Lititz PA campus |
| CONCORDIA LUTHERAN MINISTRIES OF PITTSBURGH | CONCORDIA LUTHERAN MINISTRIES | Same facility — Villa St. Joseph, Baden PA |
| LUTHERAN RETIREMENT MINISTRIES OF ALAMANCE COUNTY, NORTH CAROLINA | LUTHERAN RETIREMENT MINISTRIES | Same campus — Twin Lakes, Burlington NC (439 ft apart) |
| ST LUKE LUTHERAN COMMUNITY PORTAGE LAKES | St. Luke Lutheran Community | Same org per stllc.org legacy website |
| Lutheran Services in America, Inc. | SPIRITRUST LUTHERAN | Luther Ridge is a SpiriTrust facility per website |
| ALLEGHENY LUTHERAN HOME | Allegheny Lutheran Social Ministries | Affiliated per website; The Oaks at Pleasant Gap |
| LUTHERAN HOME | LUTHERAN SERVICES CAROLINAS | GlenFlora + Trinity Grove/Place are LSC facilities per website |
| LUTHERAN SERVICES CAROLINA | LUTHERAN SERVICES CAROLINAS | Typo — missing "s" |
| VIRGINIA SYNOD LUTHERAN HOME | VIRGINIA LUTHERAN HOMES | Legacy name — same Brandon Oaks, Roanoke VA |
| LUTHERAN NATIONAL COMMUNITIES AND SERVICES | NATIONAL LUTHERAN COMMUNITIES & SERVICES | Word-order flip — same org |

### Liberty Cluster (2 renames)

| Old Name | Canonical Name | Evidence |
|---|---|---|
| SEACOAST AT LIBERTY RIDGE | SeaCoast Health Systems | Website confirms; same address 701 Liberty Ridge Ln, Lexington KY |
| LIBERTY RIDGE SENIOR LIVING INC | SeaCoast Health Systems | Same facility as above |

### Bluegrass/Encore Cluster (2 renames)

| Old Name | Canonical Name | Evidence |
|---|---|---|
| ENCORE HEALTH PARTNERS | BLUEGRASS/ENCORE | Same KY SNF facilities |
| BLUEGRASS HEALTH KY | BLUEGRASS/ENCORE | Same Berea facility |

### Signature Cluster (2 renames)

| Old Name | Canonical Name | Evidence |
|---|---|---|
| SIGNATURE HEALTHCARE | SIGNATURE HEALTH | Facility DB confirms served facilities are Signature Health |
| Signature | SIGNATURE HEALTH | Truncated name — Signature Healthcare of Terre Haute |

### Facility-Level Reattributions

| Facility | Old Corp | New Corp | Reason |
|---|---|---|---|
| Trinity Glen, Winston-Salem, NC (SNF + ALF) | LUTHERAN LIFE VILLAGES | LUTHERAN SERVICES CAROLINAS | Not on LLV website (6 NE Indiana campuses only); fits LSC Trinity branding |

## Confirmed NOT THE SAME (Fuzzy Match Rejections)

These pairs were flagged by the fuzzy matcher but confirmed as separate entities:

| Name A | Name B | Why Different |
|---|---|---|
| LIBERTY | LIBERTY VILLAGE | NC/SC vs IL/WI — different states, different facilities |
| LIBERTY | Liberty Lutheran | NC/SC vs PA — completely different orgs |
| LUTHERAN LIFE VILLAGES | Lutheran Life Communities | NE Indiana (Fort Wayne) vs NW Indiana (Crown Point) |
| LUTHERAN HOME | Bethany Lutheran Homes, Inc. | NC vs WI |
| LUTHERAN HOME | LUTHERAN HOMES OF SOUTH CAROLINA INC | NC vs SC — separate orgs confirmed via websites |
| LUTHERAN HOME | VIRGINIA LUTHERAN HOMES | NC vs VA — both in GLR as separate entities |
| Senior Services | LUTHERAN SENIOR SERVICES | Generic name collision |
| LUTHERAN HOME | LUTHERAN HOME AT KANE PA | NC vs PA |
| LUTHERAN HOME | Woodside Lutheran Home | NC vs WI |
| LUTHERAN HOME | ALLEGHENY LUTHERAN HOME | NC vs PA |
| LUTHERAN HOME | VIRGINIA SYNOD LUTHERAN HOME | NC vs VA |
| LUTHERAN HOME | The Lutheran Home Association | NC vs WI |
| LUTHERAN HOME | Lutheran Home for Aged Development Corp | NC vs IL |
| LUTHERAN HOMES OF SOUTH CAROLINA INC | LUTHERAN SERVICES CAROLINA | SC vs NC — separate orgs (5 SC facilities vs NC Trinity facilities) |
| CROWN SENIOR LIVING | TRIPLE CROWN SENIOR LIVING | OH vs KY — Crown Senior Living not on Triple Crown website |
| Encore Senior Living | BLUEGRASS/ENCORE | Separate company — Midwest ALF/memory care chain (WI/OH/MI/IL/MN) vs KY SNF chain |

## Observations and Data Quality Notes

### Adams County Memorial Hospital — CMS Legal Entity Artifact
CMS lists "Adams County Memorial Hospital" (Decatur, IN) as the legal business name for **50+ Indiana SNFs** across many unrelated operators (Lutheran Life Villages, Majestic Care, Envive, Heritage Pointe, etc.). This is a legal filing structure, NOT an actual corporate parent. Do not use CMS Legal Business Name for corporate attribution.

### GLR Data Quality Issues Found
- **LUTHERAN HOME** in GLR should be **LUTHERAN SERVICES CAROLINAS** (4 NC facilities: GlenFlora, Trinity Grove, Trinity Place)
- **Trinity Glen, Winston-Salem** in GLR attributed to Lutheran Life Villages, should be Lutheran Services Carolinas
- **LUTHERAN SERVICES CAROLINA** (no "s") in GLR is a typo for LUTHERAN SERVICES CAROLINAS
- **CEDARHURST SENOR LIVING** in GLR is a typo for CEDARHURST SENIOR LIVING
- **HARMONY SENOR SERVICES** in GLR is a typo for HARMONY SENIOR SERVICES

### Coverage Gaps Identified
- **Triple Crown Senior Living:** 14 open communities across KY, IN, TN, OH, TX — we only have 3 (all KY)
- **SpiriTrust Lutheran:** Missing Village at Shrewsbury (800 Bollinger Drive, Shrewsbury, PA 17361)
- **Lutheran Life Villages:** 6 confirmed NE Indiana campuses — website does not list South Anthony (6723 S Anthony Blvd, Fort Wayne) though it is in our GLR and we serve it

### Deferred / Needs Further Research
- **BHP/Encore** (Belmont Terrace, 7300 Woodspoint Dr, Florence, KY) — probably NOT affiliated with BLUEGRASS/ENCORE but unconfirmed
- **MFA vs MFA MARYVILLE RE LLC** — MFA is a major served account (17 rows, NC/VA); MFA Maryville RE LLC (2 rows, TN) affiliation unclear
- **United Methodist cluster** — 12 fuzzy match rows, multiple separate regional Methodist retirement orgs colliding on shared words. Not yet researched.
- **Remaining fuzzy match clusters** — Magnolia (4), Providence (4), Priority (4), MorningStar (3), Traditions (3), Promedica (3), and others from the original 157 priority pairs

### Pattern: "Lutheran Home" as False-Match Magnet
"LUTHERAN HOME" is a specific NC operator (now consolidated to LUTHERAN SERVICES CAROLINAS), but the generic name matched 7 unrelated orgs in different states. Similar pattern with "Senior Services", "DOMINION", "FRIENDSHIP", and other short generic names. Future dedup passes should weight state/geography more heavily for short corporate names.
