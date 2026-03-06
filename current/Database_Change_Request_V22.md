# Database Change Request — V22
## Issues Identified During MUO Profile Standardization (Mar 2026)

**Date:** March 2, 2026 | **Updated:** March 3, 2026
**Requested By:** Roian (GTM Strategy)
**Status:** IN PROGRESS — Wave 0 (Audit) + Wave 1 (Phantom Fix) complete. V22.0 produced.
**Source:** MUO Profile enrichment process — cross-referencing scoring workbook, economic model, CMS ownership data, and public research against 20 corporate profiles.

---

## Summary

| # | Change | Type | Entity | Priority | Status |
|---|--------|------|--------|----------|--------|
| 1 | Rename "Southern Assisted Living, LLC" → "Southern Healthcare Management, LLC" | Corporate name correction | Southern Healthcare | **HIGH** | Wave 2 |
| 2 | Reconcile Southern Healthcare facility count (33 DB vs. 43 CMS) | Missing facilities | Southern Healthcare | **HIGH** | Wave 4 |
| 3 | Atrium Centers: add to scoring workbook, verify St Mary of the Woods, deduplicate Crittenden County | Scoring + data quality | Atrium Centers | **LOW** | Wave 4/5 |
| 4 | Verify BHP/Encore entity identity | Entity clarification | BHP/Encore | **MEDIUM** | Parked |
| 5 | Correct Lutheran Services Carolinas scoring anomaly (IR weighted=0) | Scoring workbook fix (not DB) | Lutheran Services Carolinas | **LOW** | Wave 5 |
| 6 | Add T4/T5 tier classifications to scoring framework | Tier expansion | All entities | **LOW** | Wave 5 |
| 7 | Liberty Senior Living: SNF-SNF duplicates (3 facilities with PROPCO corporate names) | Duplicate rows | Liberty Senior Living | **HIGH** | Wave 2 |
| 8 | Liberty Village (IL) — separate company miscategorized under "Liberty" | Entity misattribution | Liberty Village / Liberty Senior Living | **MEDIUM** | Wave 2 |
| 9a | Phantom ALF duplicates (DB-wide) | Row removal | All entities | **HIGH** | **DONE (V22.0)** — 33 removed, 10 reclassified |
| 9b | PROPCO/OPCO reattribution (Liberty + DB-wide) | Corporate fix | All entities | **HIGH** | Wave 2 |
| 9c | Rename short-name corporate entries | Corporate fix | Liberty + others | **HIGH** | Wave 2 |
| 9d | Flag IL/55+ as non-serviceable | Data quality flag | All entities | **HIGH** | Partial (7 ILF created) — Wave 3 |
| 9e | Database-wide audit | Audit infrastructure | All entities | **HIGH** | **DONE (Wave 0)** — 6 audit scripts, NIC enrichment |

---

## Change 1: Southern Healthcare — Corporate Name Correction (HIGH)

### Problem

The scoring workbook (`2025-12-19_Scoring_Tiering_Working.xlsx`) lists **"Southern Assisted Living, LLC"** as the corporate entity (T2, score 32, 33 facilities, $7.8M opportunity).

Southern Assisted Living, Inc. (SALI) was a **different, now-defunct company:**

| | Southern Assisted Living, Inc. (SALI) | Southern Healthcare Management, LLC |
|---|---|---|
| **HQ** | Chapel Hill, NC | Casselberry, FL |
| **Type** | Assisted Living | SNF / Rehabilitation |
| **Facilities** | 41 AL communities | 43 SNF/rehab centers |
| **States** | NC, SC, VA | FL, GA, NC |
| **Status** | Acquired by Brookdale, Q1 2006 ($82.9M) | Active, current operator |
| **REIT** | Health Care REIT (now Welltower) | None |

**Source:** SEC filing; BioSpace press release (Dec 2005); CMS ownership records (Mar 2026).

### Root Cause

Both entities share "Southern" in the name and operate in North Carolina. Likely a data entry error during initial database build.

### Requested Change

Rename corporate entity from `Southern Assisted Living, LLC` to `Southern Healthcare Management, LLC` across all associated facilities in the database.

### Validation

```sql
-- Verify no facilities remain under old name
SELECT COUNT(*) FROM database WHERE Corporate_Name = 'Southern Assisted Living, LLC'
-- Expected: 0

-- Verify new name has correct count
SELECT COUNT(*) FROM database WHERE Corporate_Name = 'Southern Healthcare Management, LLC'
-- Expected: 33 (or 43 after Change 2)
```

---

## Change 2: Southern Healthcare — Missing Facilities (HIGH)

### Problem

CMS ownership records (via nursinghomereport.org, accessed Mar 2, 2026) show **43 facilities** under Southern Healthcare Management, LLC. The database contains only **33**.

### Facility Count by State

| State | CMS Count | DB Count (est.) | Gap |
|-------|-----------|-----------------|-----|
| Florida | 31 | TBD | TBD |
| North Carolina | 10 | TBD | TBD |
| Georgia | 2 | TBD | TBD |
| **Total** | **43** | **33** | **~10** |

### CMS-Verified Facility List (43 Total)

**Florida (31):**
River Valley Rehab (Blountstown), Bonifay Nursing & Rehab, Boulevard Rehab (Boynton Beach), Boynton Beach Rehab, Braden River Rehab (Bradenton), Crestview Rehab, Orange City Nursing & Rehab (DeBary), Fort Walton Rehab, Arbor Trail Rehab (Inverness), Lanier Rehab (Jacksonville), Jacksonville Nursing & Rehab, Medicana Nursing & Rehab (Lake Worth), Lake Worth Rehab, Macclenny Nursing & Rehab, Marianna Health & Rehab, Atlantic Shores Nursing & Rehab (Melbourne), Ocala Oaks Rehab, Metro West Nursing & Rehab (Orlando), Hunters Creek Nursing & Rehab (Orlando), Palm City Nursing & Rehab, Riviera Palms Rehab (Palmetto), Port Orange Nursing & Rehab, Tiffany Hall Nursing & Rehab (Port St. Lucie), Moultrie Creek Nursing & Rehab (St. Augustine), Pinellas Point Nursing & Rehab (St. Petersburg), Sarasota Point Rehab, Bayshore Pointe Nursing & Rehab (Tampa), Northdale Rehab (Tampa), Royal Oaks Nursing & Rehab (Titusville), Parkview Rehab at Winter Park, Tuskawilla Nursing & Rehab (Winter Springs)

**North Carolina (10):**
Pettigrew Rehab (Durham), Treyburn Rehab (Durham), Lincolnton Rehab, Monroe Rehab, Raleigh Rehab, Sunnybrook Rehab (Raleigh), Rocky Mount Rehab, Cypress Pointe Rehab (Wilmington), Silas Creek Rehab (Winston-Salem), Zebulon Rehab

**Georgia (2):**
Abercorn Rehab (Savannah), Warner Robins Rehab

### Requested Change

Reconcile DB facilities against the CMS list above. Add any missing facilities with proper corporate parent linkage to Southern Healthcare Management, LLC.

### Validation

```sql
SELECT COUNT(*) FROM database WHERE Corporate_Name = 'Southern Healthcare Management, LLC'
-- Expected: 43
```

---

## Change 3: Atrium Centers — DB/Scoring Reconciliation (MEDIUM → LOW)

### Problem

Atrium Centers Inc. does not appear in the **scoring workbook** but **IS in the V21.1 Combined Database** with 27 facilities correctly tagged under "ATRIUM CENTERS." Two KY facilities are currently served. Three sub-issues identified:

### Entity Details

| Metric | Value |
|--------|-------|
| Corporate Name | Atrium Centers Inc. |
| HQ | 2550 Corporate Exchange Dr, Suite 200, Columbus, OH 43231 |
| CEO | Jason Reese |
| Ownership | 100% ESOP (via OwnersEdge) |

### CMS-Verified Facility List (26 Facilities)

CMS ownership records show two legal entities: "Atrium Centers, Inc." and "Atrium Centers Management LLC" — both map to the same operator.

**Michigan (16)**

| Facility | City |
|----------|------|
| Allendale Nursing and Rehabilitation Community | Allendale |
| Fairview Nursing and Rehabilitation Community | Centreville |
| The Timbers of Cass County | Dowagiac |
| Gladwin Nursing and Rehabilitation Community | Gladwin |
| Riverside Nursing Centre | Grand Haven |
| Grayling Nursing & Rehabilitation Community | Grayling |
| King Nursing & Rehabilitation Community | Houghton Lake |
| Westgate Nursing & Rehabilitation Community | Ironwood |
| Freeman Nursing & Rehabilitation Community | Kingsford |
| Lincoln Haven Nursing & Rehabilitation Community | Lincoln |
| Marshall Nursing and Rehabilitation Community | Marshall |
| Roosevelt Park Nursing and Rehabilitation Community | Muskegon |
| Hillcrest Nursing and Rehabilitation Community | North Muskegon |
| Plainwell Pines Nursing and Rehabilitation Community | Plainwell |
| South Haven Nursing and Rehabilitation Community | South Haven |
| Heritage Nursing and Rehabilitation Community | Zeeland |

**Ohio (4)**

| Facility | City |
|----------|------|
| Austinburg Nursing and Rehab Center | Austinburg |
| Blossom Nursing and Rehab Center | Salem |
| Lexington Court Care Center | Lexington |
| Woodside Village Care Center | Mount Gilead |

**Wisconsin (4)**

| Facility | City |
|----------|------|
| Frederic Nursing and Rehab Community | Frederic |
| Mulder Health Care Facility | West Salem |
| Prescott Nursing and Rehab Community | Prescott |
| Tomah Nursing and Rehab | Tomah |

**Kentucky (2)**

| Facility | City |
|----------|------|
| Crittenden County Health & Rehabilitation Center | Marion |
| Salem Springlake Health & Rehabilitation Center | Salem |

**Sources:** atriumlivingcenters.com/centers/ (26 facilities); nursinghomereport.org CMS ownership data for "Atrium Centers, Inc." (24) and "Atrium Centers Management LLC" (25). Counts vary slightly due to CMS entity splitting.

### Historical Note

CommuniCare Health Services took over management of **13 Ohio facilities** from Atrium in March 2018 (Crain's Cleveland Business). The previous "41 facilities" estimate from web research was outdated and included divested properties.

> [!warning] **Entity Confusion Risk:** "Atrium Health & Senior Living" (KBWB Operations LLC, Kevin Breslin) is a **completely different company** — sentenced for healthcare fraud ($146M restitution). Not related to Atrium Centers Inc. (Jason Reese, ESOP).

### V21.1 DB Verification (Mar 3, 2026)

All 26 CMS-verified facilities are present in V21.1 under "ATRIUM CENTERS" plus 1 additional:

| State | DB Count | CMS Count | Served | Notes |
|-------|----------|-----------|--------|-------|
| Michigan | 16 | 16 | 0 | Match |
| Ohio | 5 | 4 | 0 | +1: St Mary of the Woods (Avon) — not on CMS list |
| Wisconsin | 4 | 4 | 0 | Match |
| Kentucky | 2 | 2 | 2 | Match; both served |
| **Total** | **27** | **26** | **2** | |

### Requested Changes

**3a. Add to Scoring Workbook (LOW)**
Add Atrium Centers to the scoring workbook. Entity meets 7-facility in-footprint threshold (5 OH + 2 KY). All facilities C_Rural except Avon (B_Highway). Likely T3 given limited footprint, rural geography, and 2 served facilities.

**3b. Verify St Mary of the Woods (LOW)**
St Mary of the Woods (Avon, OH, 50 beds, B_Highway) is tagged "ATRIUM CENTERS" in V21.1 but does NOT appear in CMS ownership records for "Atrium Centers, Inc." or "Atrium Centers Management LLC." Verify if this is a legitimate Atrium facility or a corporate parent linkage error.

**3c. Deduplicate Crittenden County (LOW)**
Crittenden County Health & Rehab Center (Marion, KY) appears under both "ATRIUM CENTERS" and "SIGNATURE HEALTH" in V21.1. One is incorrect — deduplicate.

### Impact

Primary overlap with Eventus footprint: 5 Ohio facilities and 2 Kentucky facilities (7 in-footprint). Michigan (16) and Wisconsin (4) are outside current Eventus operational footprint. Per the operational footprint scoring rule, Enterprise Reach and Revenue Potential should be scored on the 7 in-footprint facilities only.

---

## Change 4: BHP/Encore — Entity Clarification (MEDIUM)

### Problem

The scoring workbook contains a row for "Encore/Bluegrass" under T4 with no data — listed as "Alliances" with "None" for all opportunity fields. Web research identified two candidates but could not confirm which entity this refers to:

| Candidate | HQ | Facilities | States |
|-----------|-----|-----------|--------|
| BHI Senior Living, Inc. | Indianapolis, IN | 12 communities | IN, MI, OH |
| Encore Senior Living LLC | Chicago, IL | 39–43 communities | IL, WI, MN, OH, MI |

### Requested Action

Internal clarification required:
1. Which entity does "Encore/Bluegrass" refer to?
2. Is this a formal corporate relationship or an alliance/referral arrangement?
3. Should this entity be scored or remain as T4 (Alliances)?

---

## Change 5: Lutheran Services Carolinas — Scoring Anomaly (LOW)

> [!note] **This is a scoring workbook fix, not a database change.** Included here for tracking since it was identified during the same review.

### Problem

The scoring workbook (`2025-12-19_Scoring_Tiering_Working.xlsx`) shows Integration Readiness raw score = 5 but weighted score = 0 for Lutheran Services Carolinas. This appears to be a formula or data entry error in the workbook, not in the facility database.

| Dimension | Raw | Expected Weighted (×3) | Actual Weighted |
|-----------|-----|----------------------|-----------------|
| Integration Readiness | 5 | 15 | **0** |

### Impact

If corrected: total score moves from 35 to 50, which would shift Lutheran from **T2 to T1**.

### Requested Change

Verify and correct the weighted score formula for Lutheran Services Carolinas Integration Readiness in the scoring workbook. No database change required.

---

## Change 6: Tier Framework Expansion — T4/T5 (LOW)

### Background

The V20 scoring methodology has been updated to define 5 tiers (documented in `6.3_Corporate_Scoring_Methodology_V20.md`):

| Tier | Name | Score Range | Facility Points |
|------|------|-------------|-----------------|
| T1 | Strategic Enterprise | 50–100 | 7 |
| T2 | Growth & Expansion | 25–49 | 5 |
| T3 | Retention / Watch | <25 | 4 |
| T4 | Independents | Not scored | 2 |
| T5 | Barriers | Not scored | 1 |

### Requested Change

When the scoring workbook is next refreshed:
1. Add T4 designation for entities below MUO threshold (non-scored independents)
2. Add T5 designation for entities with structural barriers (own provider group, exclusive alliances, CON restrictions)
3. Facility Points column should be added to enable the corporate tier → facility A/B/C scoring linkage

### Candidates for T5 (Barriers)

- Simcha Hyman & Naftali Zanziper (Portopiccolo Group) — 115 DB facilities, 100% barriered, own provider group

---

## Change 7: Liberty Senior Living — SNF-SNF Duplicates (HIGH)

### Problem

Three Liberty facilities appear twice in V21.1 under different corporate names — once under "LIBERTY SENIOR LIVING" (the operating company) and once under a property-holding LLC name ("LIBERTY HEALTHCARE PROPERTIES OF..."). Both rows are Source_Type=SNF. These are true duplicates, not the SNF-as-ALF phantom duplicates documented in `Risk_ALF_Corporate_Attribution_and_Data_Quality.md`.

### Affected Facilities

| City | Row 1 (Operating Co) | Row 2 (PROPCO) | Beds Differ? | Serve Conflict? |
|------|----------------------|----------------|-------------|-----------------|
| Fayetteville, NC | WOODLANDS NURSING & REHABILITATION CENTER — Corp: LIBERTY SENIOR LIVING (80 beds, **Serve=Yes**) | WOODLANDS NURSING & REHABILITATION CENTER — Corp: LIBERTY HEALTHCARE PROPERTIES OF WOODLANDS LLC (90 beds, **Serve=No**) | Yes (80 vs 90) | **Yes** |
| Blowing Rock, NC | THE FOLEY CENTER AT CHESTNUT RIDGE — Corp: LIBERTY SENIOR LIVING (92 beds, Serve=No) | THE FOLEY CENTER AT CHESTNUT RIDGE — Corp: LIBERTY HEALTHCARE PROPERTIES OF (112 beds, Serve=No) | Yes (92 vs 112) | No |
| Benson, NC | LIBERTY COMMONS NSG & REHAB CTR OF JOHNSTON CTY — Corp: LIBERTY SENIOR LIVING (100 beds, Serve=No) | LIBERTY COMMONS NURSING & REHABILITATION CENTER OF JOHNSTON COUNTY — Corp: LIBERTY HEALTHCARE PROPERTIES OF JOHNSTON COUNTY LLC (120 beds, Serve=No) | Yes (100 vs 120) | No |

### Root Cause

The CMS data and NIC Maps data both include SNF records. Where the operating company and property-holding company are different legal entities (which is common in SNF ownership structures), both sources may create separate rows for the same physical building. The V21 build did not deduplicate these.

> [!warning] **Serve Status Conflict:** Woodlands (Fayetteville) shows Serve=Yes under the LIBERTY SENIOR LIVING row but Serve=No under the PROPCO row. This means the same facility has contradictory service status in the database.

### Relationship to Existing Risk Document

These SNF-SNF duplicates are **distinct from** the 7 SNF-as-ALF phantom duplicates documented in `Risk_ALF_Corporate_Attribution_and_Data_Quality.md`. That risk document covers NIC Maps ALF rows duplicating CMS SNF rows. This change covers CMS SNF rows duplicating each other due to OPCO/PROPCO naming.

### Requested Change

1. Remove the PROPCO duplicate rows (retain the "LIBERTY SENIOR LIVING" rows)
2. Verify bed counts against CMS source data
3. Audit for similar PROPCO-pattern SNF duplicates across the full database

---

## Change 8: Liberty Village (IL) — Separate Company Misattributed (MEDIUM)

### Problem

7 Illinois ALF facilities are in V21.1 under "Liberty Village of [city]" corporate names. **Liberty Village is a separate Illinois-based senior living company**, not affiliated with Liberty Senior Living (Wilmington, NC). These facilities should not be attributed to or confused with the Liberty Senior Living MUO.

### Affected Facilities

| Facility | Corporate Name (V21.1) | City | State | Source | Beds |
|----------|----------------------|------|-------|--------|------|
| Green Oaks Supportive Living Of River Oaks | Liberty Village of Freeport | Calumet City | IL | ALF | 109 |
| Liberty Village Of Geneseo | Liberty Village of Geneseo | Geneseo | IL | ALF | 70 |
| Hawthorne Inn Of Jerseyville | Liberty Village of Jerseyville | Jerseyville | IL | ALF | 40 |
| Hawthorne Inn Of Peoria | Liberty Village of Peoria | Peoria | IL | ALF | 52 |
| Hawthorne Inn Of Peru | Liberty Village of Peru | Peru | IL | ALF | 52 |
| Hawthorne Inn Of Rochelle | Liberty Village of Rochelle | Rochelle | IL | ALF | 46 |
| Liberty Village Of Streator | Liberty Village of Streator | Streator | IL | ALF | 30 |

### Why This Matters

1. **Illinois is outside Eventus operational footprint** — these facilities should not appear in any footprint-based analysis
2. **Entity confusion** — any search for "Liberty" in the database returns these alongside the NC-based operator
3. **NIC Maps data provenance** — these came from the NIC Maps ALF import; NIC Maps uses per-facility corporate names that fragment the entity into 7 separate "Liberty Village of [city]" entries rather than one parent
4. **The user's original concern about "IL facilities that were not previously in DB"** — these appear to have been added during the V21.0 NIC Maps expansion (+5,328 ALF from 8 expansion states)

### Requested Change

1. Confirm Liberty Village is a separate company (not affiliated with Liberty Senior Living)
2. If confirmed, ensure these 7 facilities are NOT counted in any Liberty Senior Living corporate analysis
3. Consider whether IL facilities belong in the database at all given footprint rules

---

## Change 9: Liberty ALF Data Quality Cure — Consolidated (HIGH)

### Problem

A proof-of-concept investigation of Liberty Senior Living (documented in `data-model/reference/Risk_ALF_Corporate_Attribution_and_Data_Quality.md`, Mar 1, 2026) exposed three systemic ALF data quality risks. This change consolidates the Risk doc findings into actionable database changes for Liberty specifically, plus flags the database-wide audit needed.

### 9a. Remove 7 Phantom ALF Duplicates

NIC Maps created ALF rows that duplicate existing CMS SNF records at 7 Liberty addresses. Liberty's website confirms these locations are **SNF-only operations** (Liberty Health & Rehab division) — no ALF community exists.

| City | SNF Row (CMS, correct) | Phantom ALF Row (NIC Maps, remove) |
|------|------------------------|-------------------------------------|
| Burlington, NC | LIBERTY COMMONS NURSING & REHAB ALAMANCE (122 beds) | LIBERTY COMMONS NURSING AND REHAB OF ALAMANCE (123 beds) |
| Louisburg, NC | LOUISBURG HEALTHCARE & REHABILITATION CENTER (92 beds) | LOUISBURG HEALTHCARE & REHABILITATION CENTER (89 beds) |
| Roxboro, NC | ROXBORO HEALTHCARE & REHAB CENTER (140 beds) | ROXBORO HEALTHCARE AND REHABILITATION CENTER (97 beds) |
| Sanford, NC | LIBERTY COMMONS NSG AND REHAB CTR OF LEE COUNTY (80 beds) | LIBERTY COMMONS NSG AND REHAB OF LEE COUNTY (54 beds) |
| Warrenton, NC | WARREN HILLS NURSING CENTER (140 beds) | WARREN HILLS NURSING CENTER ALF + SNF (2 ALF rows: 72 + 92 beds) |
| Yadkinville, NC | YADKIN NURSING CARE CENTER (147 beds) | YADKIN NURSING CENTER (54 beds) |
| Canton, NC | *(no SNF row)* | SILVER BLUFF VILLAGE-SNF (86 beds, Source_Type=ALF — name literally says "SNF") |

**Action:** Remove 8 phantom ALF rows (7 addresses, Warrenton has 2). Retain the CMS SNF rows. Canton is a special case — Silver Bluff Village-SNF is confirmed as an SNF in the Eventus Facility Database (MH only, Census 15).

**Revenue impact:** All 7 addresses are served. Phantom rows create double-counted revenue opportunities.

### 9b. Reattribute 11 PROPCO/OPCO ALFs to Liberty Senior Living

NIC Maps uses property-holding company names (LLCs, PROPCOs, OPCOs) instead of operating company names. 11 confirmed Liberty ALFs are classified as Independent under various LLC names.

| Facility | Current Corporate_Name (incorrect) | Correct Attribution |
|----------|-----------------------------------|---------------------|
| THE TERRACE AT BRIGHTMORE OF SOUTH CHARLOTTE | 10225 OLD ARDREY KELL OPCO, LLC | LIBERTY SENIOR LIVING |
| BRIGHTMORE OF WILMINGTON (2 rows) | blank / BRIGHTMORE PROPERTIES INCI LLC | LIBERTY SENIOR LIVING |
| CAROLINA BAY AT AUTUMN HALL | 630 CAROLINA BAY NC PROPCO LLC | LIBERTY SENIOR LIVING |
| HAYES BARTON PLACE | BUDLEIGH EAST MULTIFAMILY LLC | LIBERTY SENIOR LIVING |
| KEMPTON OF CHARLESTON | NOT AVAIL FROM COUNTY | LIBERTY SENIOR LIVING |
| THE KEMPTON OF HERMITAGE | STAR GROUP OF HERMITAGE LLC | LIBERTY SENIOR LIVING |
| KEMPTON OF ROCK HILL | 1611 CONSTITUTION BLVD PROPCO | LIBERTY SENIOR LIVING |
| OAKLEAF VILLAGE AT LEXINGTON | 800 N LAKE PROPCO LLC | LIBERTY SENIOR LIVING |
| SOUTH BAY AT MOUNT PLEASANT (2 rows) | MT PLEASANT SENIOR HOUSING I PROPCO | LIBERTY SENIOR LIVING |
| THE BARCLAY AT SOUTHPARK | SOUTHPARK TOWERS PROPCO LLC | LIBERTY SENIOR LIVING |

**Action:** Rename Corporate_Name to "LIBERTY SENIOR LIVING" for all 11 facilities. Rerun Four-Rule hierarchy to reclassify from Independent to Corporate.

### 9c. Rename 14 "LIBERTY" Short-Name ALFs

14 ALF rows use the truncated corporate name "LIBERTY" instead of the full "LIBERTY SENIOR LIVING." These are correctly attributed to Liberty but use an inconsistent name that fragments the entity in queries and scoring.

**Action:** Rename "LIBERTY" → "LIBERTY SENIOR LIVING" for all 14 rows.

### 9d. Flag IL/55+ Communities as Non-Serviceable

Several Liberty communities identified as ALFs are actually **Independent Living / 55+ Active Adult communities** — outside Eventus's serviceable market. Specifically, the "Inspire" branded communities (e.g., Inspire Brunswick Forest in Leland, NC) are marketed as 55+ Active Adult, not licensed ALF.

**Action:**
1. Cross-reference Liberty ALFs against NC/SC/TN state licensing records to confirm which are licensed ALFs vs. IL/Active Adult
2. Add a data quality flag (e.g., `IL_Not_ALF`) to any communities confirmed as Independent Living
3. Exclude flagged facilities from TAM/SAM calculations

### 9e. Database-Wide Audit (Future)

The Liberty investigation is a proof-of-concept. The same three risks (phantoms, hidden ownership, IL contamination) are **structural** — they arise from how NIC Maps records data. Database-wide indicators:

| Risk | Liberty Count | Estimated DB-Wide Scale |
|------|-------------|------------------------|
| Phantom ALF duplicates | 7 addresses | Unknown — requires systematic address-match audit |
| PROPCO/OPCO hidden ownership | 11 facilities | ~180+ PROPCO + ~50+ OPCO naming patterns in DB |
| IL/55+ contamination | TBD | Unknown — NIC Maps may not distinguish ALF from IL |

**Action (Phase 3):** After Liberty cure is validated, design and execute systematic database-wide audit for all three risks.

### Source Document

Full investigation details, affected addresses, naming pattern analysis, and recommended cures are in:
`data-model/reference/Risk_ALF_Corporate_Attribution_and_Data_Quality.md`

---

## Implementation Priority

### Phase 1: Execute Now (HIGH — can be done with current data)
1. **Change 1** — Rename Southern Assisted Living → Southern Healthcare Management (name fix only)
2. **Change 7** — Remove 3 Liberty PROPCO SNF duplicate rows (Fayetteville, Blowing Rock, Benson)
3. **Change 9a** — Remove 8 Liberty phantom ALF rows (7 addresses where NIC Maps duplicated SNFs as ALFs)
4. **Change 9b** — Reattribute 11 Liberty PROPCO/OPCO ALFs to "LIBERTY SENIOR LIVING"
5. **Change 9c** — Rename 14 "LIBERTY" short-name ALFs to "LIBERTY SENIOR LIVING"
6. **Change 5** — Verify/correct Lutheran IR weighted score (scoring workbook, not DB)

### Phase 2: Next Data Refresh (MEDIUM — requires additional research or internal input)
7. **Change 2** — Reconcile Southern Healthcare facility count (33 → 43)
8. **Change 8** — Verify Liberty Village (IL) is a separate company; prevent entity confusion
9. **Change 9d** — Flag Liberty IL/55+ communities as non-serviceable (requires state licensing check)
10. **Change 3a** — Add Atrium Centers to scoring workbook
11. **Change 3b** — Verify St Mary of the Woods (Avon, OH) corporate parent
12. **Change 3c** — Deduplicate Crittenden County (Marion, KY) — ATRIUM CENTERS vs SIGNATURE HEALTH
13. **Change 4** — Resolve BHP/Encore entity identity (requires internal input)

### Phase 3: Scoring Framework + Systematic Audit (LOW — broader scope)
14. **Change 6** — Add T4/T5 tiers and facility points to scoring workbook
15. **Change 9e** — Database-wide audit for phantom ALFs, PROPCO/OPCO hidden ownership, IL/55+ contamination

---

## Related Documentation

> [!note] **Why this section exists:** Data quality issues in this database tend to cascade — you pull one thread and three more appear. This index ensures nothing gets lost across the data-model repo, Vault, and MUO profiles.

### Data Quality & Risk Documents

| Document | Repo Location | What It Covers |
|----------|---------------|----------------|
| **ALF Corporate Attribution Risk** | `data-model/reference/Risk_ALF_Corporate_Attribution_and_Data_Quality.md` | **The Liberty proof-of-concept.** Three systemic risks: phantom ALF duplicates (7 addresses), hidden PROPCO/OPCO ownership (11 facilities, ~230+ DB-wide), IL/55+ contamination. Full facility tables, naming pattern analysis, revenue impact. Source for Changes 7, 8, 9. |
| **CMS Cross-Reference Results** | `data-model/reference/Proposal_CMS_Source_Data_Cross_Reference.md` | Post-V21 CMS validation. 15,192 SNFs matched = 99.65% coverage. 5 served facility name mismatches resolved. 287 unserved mismatches (mostly ALF-as-SNF or closed). 1 corporate ownership conflict (River Oaks, KY). |
| **CMS Chain ID Enhancement** | `data-model/changelogs/V21_1_to_V21_2_CMS_Chain_Enhancement.md` | V21.1→V21.2 corporate reclassification using CMS Chain ID. 320 facilities reclassified Independent → Corporate. 13 served facilities impacted. Key finding: our Four-Rule hierarchy undercounts corporate chains because per-facility LLCs get classified as Independent. |
| **Facility Count Discrepancy** | `data-model/current/Facility_Count_Discrepancy_Explanation.md` | Why DB (26,268) differs from CRM (~1,200). Campus co-location methodology. 673 co-located addresses tested post-NIC Maps, 99.3% pass rate. 1 Marquette duplicate removed. |

### NIC Maps Integration & Data Lineage

| Document | Repo Location | What It Covers |
|----------|---------------|----------------|
| **V21 ALF Enhancement Plan** | `data-model/reference/2026-02-24_V21_ALF_Enhancement_Plan.md` | **Master implementation doc for NIC Maps infusion.** +5,328 ALF from 8 expansion states (MI, IL, WI, MN, FL, MD, GA, MO). Three-tier dedup pipeline. PA validation (734 candidates, 99.6% match). Campus sister facility rule (75 retained). Geographic tier classification. V20 20,943 → V21 26,271. |
| **Source Data Lineage** | `data-model/reference/Source_Data_Lineage.md` | Upstream data provenance. CMS → Brooke → SNF Database → Combined DB. State licensing → 655 ALF. NIC Maps → 5,328 ALF. Confirmed by Brooke Ritchie Feb 27, 2026. |
| **V20→V21 Changelog** | `data-model/changelogs/V20_to_V21_ALF_Enhancement.md` | Version transition details for the NIC Maps expansion. |

### Scoring & Methodology

| Document | Repo Location | What It Covers |
|----------|---------------|----------------|
| **Corporate Scoring Methodology** | `data-model/current/6.3_Corporate_Scoring_Methodology_V20.md` | 6-dimension scoring rubric, tier definitions (T1–T5), facility points, operational footprint constraint, open questions on IR rubric. Source for Changes 5, 6. |
| **Corporate Scoring Reference Slide** | `Vault/03_Corporate_Accounts/MUO_Profiles/Reference/Corporate_Scoring_Reference_Slide.md` | MD reconstruction of GTM deck slide 46. Scoring matrix, tier definitions, discrepancies between slide and V20 methodology. |
| **Scoring Workbook** | `Vault/03_Corporate_Accounts/Tiering/2025-12-19_Scoring_Tiering_Working.xlsx` | Source of truth for raw scores and tier assignments. Contains the Lutheran IR anomaly (Change 5) and the Southern name error (Change 1). |

### MUO Profiles (entities affected by this DCR)

| Profile | Vault Location | DCR Changes |
|---------|---------------|-------------|
| **Southern Healthcare Management** | `Vault/03_Corporate_Accounts/MUO_Profiles/Southern_Healthcare_Management_MUO_Profile.md` | Changes 1, 2 |
| **Atrium Centers** | `Vault/03_Corporate_Accounts/MUO_Profiles/Atrium_Centers_MUO_Profile.md` | Change 3 |
| **BHP / Encore** | `Vault/03_Corporate_Accounts/MUO_Profiles/BHP_Encore_MUO_Profile.md` | Change 4 |
| **Lutheran Services Carolinas** | `Vault/03_Corporate_Accounts/MUO_Profiles/Lutheran_Services_Carolinas_MUO_Profile.md` | Change 5 |
| **Liberty Senior Living** | `Vault/03_Corporate_Accounts/MUO_Profiles/Liberty_Senior_Living_MUO_Profile.md` | Changes 7, 8, 9 |
| **MUO Profiles Index** | `Vault/03_Corporate_Accounts/MUO_Profiles/_MUO_Profiles_Index.md` | Links back to this DCR |

### Deferred Proposals (not in this DCR but related)

| Proposal | Repo Location | Relevance |
|----------|---------------|-----------|
| **Metro Definition Enhancement** | `data-model/reference/Proposal_Metro_Definition_Enhancement.md` | Full CBSA-based metro classification for expansion states. Affects geographic tier assignments for new NIC Maps facilities. |
| **Multi-Service Facility Classification** | `data-model/reference/Proposal_Multi_Service_Facility_Classification.md` | QC review of AL/MC, AL/SNF, CCRC classification. Related to the phantom duplicate and campus co-location issues. |
| **Facility Profile Cross-Reference** | `data-model/reference/Proposal_Facility_Profile_Cross_Reference.md` | Two-source validation (Eventus Facility Profile + CMS Provider API). Would help catch corporate ownership conflicts like River Oaks and Crittenden County. |

### Database Files

| File | Location | Notes |
|------|----------|-------|
| **Combined Database V21.1** | `Vault/02_Data_Model/Archive/1_Combined_Database_FINAL_V21_1.xlsx` | Current production DB. 26,268 rows (15,243 SNF + 11,024 ALF). All changes in this DCR reference V21.1 data. |
| **SNF Source (CMS)** | `Vault/02_Data_Model/Reference/Source_SNF_Database_with_Revenue_Q4_2025.xlsx` | Brooke's curated CMS extract. 14,752 SNFs, 105 columns, 51 state tabs. |
| **ALF Source (NIC Maps)** | `Vault/02_Data_Model/Reference/Source_NIC_Maps_Nationwide_Inventory_Export_11.17.25.xlsx` | Raw NIC Maps export. 23,142 buildings. Source of the ALF expansion and the root cause of Changes 7–9. |

---

## Wave 0+1 Completion Log (2026-03-03)

### Wave 0: Audit Infrastructure (COMPLETE)
- Built `utils.py` (shared utilities), 5 audit scripts, `nic_enrichment.py`
- Key discovery: NIC Maps source has Operator Name, CCN, and unit-type columns dropped during DB build
- NIC enrichment reclassified 841 address-match suspects: 50 confirmed phantoms, 588 co-located campuses, 508 pure IL
- 2,959 ALF rows where Corporate_Name = NIC Owner (PROPCO), not Operator
- All reports in `data-model/scripts/audit_reports/`

### Wave 1: Phantom Fix → V22.0 (COMPLETE)
- Script: `phantom_fix.py` (preview/apply mode)
- Output: `1_Combined_Database_FINAL_V22_0.xlsx`
- 12 served phantoms triaged against Eventus internal Facility Database
- 4 shared-address patterns documented (see `audit_reports/phantom_triage_served.md`)

| Action | Count | Detail |
|--------|-------|--------|
| Rows removed | 33 | 5 served phantoms + 27 non-served (SNF exists) + 1 duplicate |
| ALF reclassified to SNF | 3 | CMS CCN confirmed nursing facilities |
| ALF reclassified to ILF | 7 | New Source_Type for NC+IL campuses without CMS certification |
| SNF rows updated | 4 | Service flags migrated from removed ALF rows |

| Metric | V21.1 | V22.0 | Delta |
|--------|-------|-------|-------|
| Total rows | 26,267 | 26,234 | -33 |
| SNF | 15,243 | 15,246 | +3 |
| ALF | 11,024 | 10,981 | -43 |
| ILF | 0 | 7 | +7 |
| Served | 1,659 | 1,658 | -1 |

### New Findings Not in Original DCR
- **ILF Source_Type:** Created to classify facilities with nursing + independent living units but no CMS certification. Non-serviceable.
- **Facility DB naming convention:** Internal Facility DB uses `Name - Type - State` format (e.g., "Four Seasons Retirement Center - SNF - IN"). Combined DB should align for consent-authority matching.
- **Census vs Consents:** Facility DB "census" = consents (signed patients). Combined DB "census" = CMS avg daily residents. Different numbers.
- **Facility DB review items:** Westminster Village (Terre Haute IN) and Timbercrest (North Manchester IN) have discrepancies between Facility DB structure and Combined DB rows. Flagged for Facility DB owner.
- **7 Liberty-specific phantoms from DCR 9a:** Need verification against Wave 1 removal list — may require separate pass.

---

## Sign-Off

| Role | Name | Date | Approval |
|------|------|------|----------|
| Requested By | Roian | Mar 2, 2026 | ☐ |
| Data Owner | | | ☐ |
| Validated By | | | ☐ |

---

**END OF CHANGE REQUEST**
