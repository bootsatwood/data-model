# Risk: ALF Corporate Attribution and Data Quality

**Date identified:** 2026-03-01
**Identified via:** Liberty Senior Living proof-of-concept investigation
**Affects:** Combined Database V21.2 (11,024 ALF records)
**Status:** Documented. Cure in progress (Liberty first, then systematic).

---

## Executive Summary

A detailed investigation of a single corporate entity — Liberty Senior Living (41 SNFs + 23 ALF communities) — exposed three systemic data quality risks in the ALF portion of the Combined Database. These risks likely affect hundreds of ALF records beyond Liberty alone.

| Risk | Description | Liberty Impact | Estimated Database-Wide Scale |
|------|-------------|----------------|-------------------------------|
| **Phantom ALFs** | NIC Maps duplicating SNF records as ALF rows | 7 addresses with SNF-as-ALF duplicates | Unknown — requires systematic audit |
| **Hidden Ownership** | Real ALFs under LLC/PROPCO names, classified Independent | 11 facilities misattributed | Potentially hundreds — PROPCO/OPCO naming is pervasive in NIC Maps data |
| **Missing Facilities** | Real ALFs not in the database at all | 5-7 communities absent | Unknown |

Additionally, some facilities listed as ALFs on corporate websites are actually **Independent Living / Active Adult (55+) communities** — a facility type outside Eventus's serviceable market that should not appear in the database as ALFs.

---

## Risk 1: Phantom ALF Records (NIC Maps Duplicating SNFs)

### What We Found

At 7 Liberty addresses, the database contains both:
- An **SNF row** from CMS data (Corporate_Name = `LIBERTY SENIOR LIVING`)
- An **ALF row** from NIC Maps (Corporate_Name = `LIBERTY`, slightly different facility name)

Liberty's own website confirms these cities have **only SNF operations** (Liberty Health & Rehab division) — no ALF community exists at these locations.

### Affected Liberty Addresses

| City | SNF Row (CMS) | ALF Row (NIC Maps) | Both Served? |
|------|---------------|---------------------|-------------|
| Burlington, NC | LIBERTY COMMONS NURSING & REHAB ALAMANCE (122 beds) | LIBERTY COMMONS NURSING AND REHAB OF ALAMANCE (123 beds) | Yes |
| Louisburg, NC | LOUISBURG HEALTHCARE & REHABILITATION CENTER (92 beds) | LOUISBURG HEALTHCARE & REHABILITATION CENTER (89 beds) | Yes |
| Roxboro, NC | ROXBORO HEALTHCARE & REHAB CENTER (140 beds) | ROXBORO HEALTHCARE AND REHABILITATION CENTER (97 beds) | Yes |
| Sanford, NC | LIBERTY COMMONS NSG AND REHAB CTR OF LEE COUNTY (80 beds) | LIBERTY COMMONS NSG AND REHAB OF LEE COUNTY (54 beds) | Yes |
| Warrenton, NC | WARREN HILLS NURSING CENTER (140 beds) | WARREN HILLS NURSING CENTER ALF + SNF (2 ALF rows) | Yes |
| Yadkinville, NC | YADKIN NURSING CARE CENTER (147 beds) | YADKIN NURSING CENTER (54 beds) | Yes |
| Canton, NC | (no SNF row) | SILVER BLUFF VILLAGE-SNF (86 beds, Source_Type=ALF) | Yes |

**Canton detail:** Silver Bluff Village-SNF is confirmed as an SNF in the Eventus Facility Database (MH only, Census 15). NIC Maps classified it as ALF despite the name literally containing "SNF."

### Pattern

The duplicate pattern is consistent: nearly identical facility name, same address, different bed/census counts, different data source. NIC Maps appears to be ingesting SNF records and classifying them as ALFs. The bed count differences suggest NIC Maps pulls from a different data vintage or counting methodology.

### Revenue Impact

All 7 addresses are served facilities. The phantom ALF rows create **double-counted revenue opportunities** — the same building appears as both an SNF opportunity and an ALF opportunity. This inflates TAM/SAM calculations for any market containing these facilities.

### Recommended Cure

Systematic address-match comparison between CMS SNF records and NIC Maps ALF records across the full database. Where the same facility appears in both sources at the same address, the ALF row should be flagged for review and likely removed.

---

## Risk 2: Hidden Corporate Ownership (LLC/PROPCO Names)

### What We Found

NIC Maps uses **property-holding company names** (LLCs, PROPCOs, OPCOs) as the Corporate_Name for ALF records, rather than the operating company name. Under the Four-Rule hierarchy, these unique LLC names produce a count of 1 and classify as Independent.

### Liberty ALFs Under LLC/PROPCO Names

| Facility | NIC Maps Corporate_Name | True Owner | Ownership_Type |
|----------|------------------------|------------|----------------|
| THE TERRACE AT BRIGHTMORE OF SOUTH CHARLOTTE | 10225 OLD ARDREY KELL OPCO, LLC | Liberty Senior Living | Independent |
| BRIGHTMORE OF WILMINGTON (2 rows) | blank / BRIGHTMORE PROPERTIES INCI LLC | Liberty Senior Living | Independent |
| CAROLINA BAY AT AUTUMN HALL | 630 CAROLINA BAY NC PROPCO LLC | Liberty Senior Living | Corporate* |
| HAYES BARTON PLACE | BUDLEIGH EAST MULTIFAMILY LLC | Liberty Senior Living | Independent |
| KEMPTON OF CHARLESTON | blank / NOT AVAIL FROM COUNTY | Liberty Senior Living | Independent |
| THE KEMPTON OF HERMITAGE | STAR GROUP OF HERMITAGE LLC | Liberty Senior Living | Independent |
| KEMPTON OF JACKSONVILLE | LIBERTY COMMONS ASSISTED LIVING OF ONSLOW COUNTY, LLC | Liberty Senior Living | Independent |
| KEMPTON OF ROCK HILL | 1611 CONSTITUTION BLVD PROPCO | Liberty Senior Living | Independent |
| OAKLEAF VILLAGE AT LEXINGTON | 800 N LAKE PROPCO LLC | Liberty Senior Living | Independent |
| PISGAH VALLEY RETIREMENT CENTER | PISGAH VALLEY RETIREMENT CENTER PROPERTIES LLC | Liberty Senior Living | Corporate* |
| SOUTH BAY AT MOUNT PLEASANT | MT PLEASANT SENIOR HOUSING I PROPCO | Liberty Senior Living | Corporate* |
| THE BARCLAY AT SOUTHPARK | SOUTHPARK TOWERS PROPCO LLC | Liberty Senior Living | Independent |

*Corporate because other facilities share the same LLC name — but still not attributed to Liberty.

### Naming Patterns Observed

| Pattern | Example | Count in Liberty |
|---------|---------|-----------------|
| `[ADDRESS] PROPCO LLC` | 630 CAROLINA BAY NC PROPCO LLC | 4 |
| `[ADDRESS] OPCO, LLC` | 10225 OLD ARDREY KELL OPCO, LLC | 1 |
| `[PROPERTY NAME] LLC` | STAR GROUP OF HERMITAGE LLC | 3 |
| `[CITY] SENIOR HOUSING PROPCO` | MT PLEASANT SENIOR HOUSING I PROPCO | 1 |
| Blank / NOT AVAIL | — | 2 |

These patterns are **not unique to Liberty**. A scan of the full database shows PROPCO and OPCO names throughout the ALF records. If one 64-site operator has 11 facilities hidden under LLCs, the database-wide impact could be hundreds of misattributed ALF records.

### Revenue Impact

Facilities classified as Independent when they are actually part of a large corporate chain affect:
- **Corporate Scoring** — these facilities are excluded from their parent chain's score
- **Sales Strategy** — approached as independents rather than through corporate relationship
- **Market Sizing** — Corporate vs Independent market split is distorted

### Recommended Cure

1. **Short-term:** Cure Liberty as proof of concept (rename all 12 facilities to `LIBERTY SENIOR LIVING`, rerun Four-Rule)
2. **Medium-term:** Build a cross-reference of known PROPCO/OPCO/LLC names to operating companies using corporate websites and state licensing records
3. **Long-term:** Evaluate whether NIC Maps provides a parent-company field that could be used programmatically

---

## Risk 3: Missing ALF Facilities

### What We Found

Liberty's website lists 23 ALF communities. After matching by name, address, city, and nearby cities, 5-7 communities are **not in our database at all** under any name:

| Community | City | Notes |
|-----------|------|-------|
| Inspire Briar Chapel | Chapel Hill, NC | No match in Chapel Hill or nearby Pittsboro |
| Inspire Brunswick Forest | Leland, NC | Address is 6146 Liberty Hall Dr — no match in Leland |
| Inspire Royal Park | Matthews, NC | SNF exists (Royal Park Rehab), no ALF row |
| Inspire Sandhill | Southern Pines, NC | No match in Southern Pines/Pinehurst/Aberdeen |
| The Peninsula of Charleston | Charleston, SC | No match in Charleston area |
| The Preserve at Fairfield Glade | Crossville, TN | No match in Crossville |
| The Templeton of Cary | Cary, NC | Possible match (SWIFT CREEK HEALTH CENTER under CARY SENIOR HOUSING I PROPCO LLC) but unconfirmed |

### Important Distinction: ALF vs Independent Living

Several of these missing communities — particularly the "Inspire" brand — are marketed as **55+ Active Adult** or **Independent Living** communities, not licensed Assisted Living Facilities. For example, Inspire Brunswick Forest (6146 Liberty Hall Dr, Leland NC) advertises independent senior apartments for active adults age 55+.

**This matters because Independent Living / Active Adult communities are outside Eventus's serviceable market.** Eventus provides PCP (Primary Care Physician) and MH (Mental Health) clinical services to residents who need ongoing medical care — the population in SNFs and licensed ALFs. Residents of 55+ Active Adult communities are generally healthy, independent adults who do not require these services.

If NIC Maps includes Independent Living communities in its ALF data, some of our 11,024 ALF records may represent facilities where Eventus has no realistic service opportunity. This would inflate TAM/SAM calculations.

### Recommended Cure

1. Determine whether the missing Liberty communities are licensed ALFs or IL/Active Adult (state licensing records would confirm)
2. Audit NIC Maps data for markers that distinguish licensed ALF from Independent Living
3. If NIC Maps does not distinguish, add a data quality flag for facilities that may be IL rather than ALF

---

## Scope of Risk

### Why Liberty Is Representative

Liberty Senior Living was chosen as a proof of concept because:
- It operates across both SNF and ALF facility types
- It has a clear public website listing all facilities by division
- It operates in our core footprint state (NC) with expansion into SC, TN, FL

The three risks identified are **structural** — they arise from how NIC Maps records data, not from anything specific to Liberty. Any corporate operator with:
- SNFs in CMS data AND ALFs in NIC Maps data is vulnerable to **phantom duplicates**
- ALFs held through property-holding LLCs is vulnerable to **hidden ownership**
- Independent Living communities alongside ALFs is vulnerable to **IL-as-ALF contamination**

### Known Scope Indicators

| Indicator | Count | Source |
|-----------|-------|--------|
| Distinct PROPCO-pattern Corporate_Names in database | ~180+ | Database scan (Corporate_Name contains "PROPCO") |
| Distinct OPCO-pattern Corporate_Names in database | ~50+ | Database scan (Corporate_Name contains "OPCO") |
| ALF records with blank Corporate_Name | Unknown | Requires count |
| ALF records classified Independent | ~4,500+ of 11,024 | Estimated from overall 37% Independent rate |

---

## Liberty Senior Living — Full Name Variation Inventory

For reference, here are all Corporate_Name strings in the database that belong to Liberty Senior Living:

| Corporate_Name in Database | Facility Count | Ownership_Type | Correct Attribution |
|---------------------------|---------------|----------------|---------------------|
| LIBERTY SENIOR LIVING | 41 | Corporate | Correct |
| LIBERTY | 14 | Corporate | Should be LIBERTY SENIOR LIVING |
| 630 CAROLINA BAY NC PROPCO LLC | 2 | Corporate | Should be LIBERTY SENIOR LIVING |
| SOUTHPARK TOWERS PROPCO LLC | 1 | Independent | Should be LIBERTY SENIOR LIVING |
| BRIGHTMORE PROPERTIES INCI LLC | 1 | Independent | Should be LIBERTY SENIOR LIVING |
| 10225 OLD ARDREY KELL OPCO, LLC | 1 | Independent | Should be LIBERTY SENIOR LIVING |
| BUDLEIGH EAST MULTIFAMILY LLC | 1 | Independent | Should be LIBERTY SENIOR LIVING |
| STAR GROUP OF HERMITAGE LLC | 1 | Independent | Should be LIBERTY SENIOR LIVING |
| LIBERTY COMMONS ASSISTED LIVING OF ONSLOW COUNTY, LLC | 1 | Independent | Should be LIBERTY SENIOR LIVING |
| 1611 CONSTITUTION BLVD PROPCO | 1 | Independent | Should be LIBERTY SENIOR LIVING |
| 800 N LAKE PROPCO LLC | 1 | Independent | Should be LIBERTY SENIOR LIVING |
| PISGAH VALLEY RETIREMENT CENTER PROPERTIES LLC | 1 | Corporate | Should be LIBERTY SENIOR LIVING |
| MT PLEASANT SENIOR HOUSING I PROPCO | 1 | Corporate | Should be LIBERTY SENIOR LIVING |
| NOT AVAIL FROM COUNTY | 1 | Corporate | Should be LIBERTY SENIOR LIVING |
| (blank) | 2 | Independent | Should be LIBERTY SENIOR LIVING |

**Total: 71 rows across 15 Corporate_Name variants** (including phantom duplicates that should be removed, not renamed).

---

## Next Steps

1. **Cure Liberty** — Rename confirmed ALFs to `LIBERTY SENIOR LIVING`, flag/remove phantom duplicates, rerun Four-Rule hierarchy
2. **Systematic duplicate audit** — Address-match CMS SNFs against NIC Maps ALFs database-wide
3. **PROPCO/OPCO inventory** — Catalog all LLC-pattern Corporate_Names and research parent operators
4. **IL/Active Adult flag** — Determine whether NIC Maps data contains markers to distinguish licensed ALFs from Independent Living communities
5. **Update Source_Data_Lineage.md** — Document NIC Maps data quality limitations

---

*Identified during Liberty Senior Living proof-of-concept investigation, 2026-03-01.*
