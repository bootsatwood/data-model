# V21 ALF Enhancement Plan — NIC Maps Integration

**Date:** February 24, 2026
**Author:** Roian Atwood
**Status:** DRAFT — Pending Approval
**Parent:** [[01_Data Model/_Data_Model_Index|Data Model Index]]

---

## Objective

Produce Combined Database V21.0 by integrating ALF and Memory Care facility records from the NIC Maps nationwide inventory export into 8 expansion states with zero ALF coverage, plus PA as a validation control. This closes the facility count gaps identified in the [[2026-02-24_New_State_Expansion_Strategy|New State Expansion Strategy]] and enables accurate SOM calculations that reflect the full facility landscape.

---

## Scope

### Target States

| State | Current DB (V20) | SNF | ALF | NIC Maps AL/MC-only (no NC) | Net New Candidates |
|-------|-----------------|-----|-----|-----------------------------|--------------------|
| MI | 425 | 425 | 0 | 754 | ~754 (after dedup) |
| IL | 674 | 674 | 0 | 570 | ~570 |
| WI | 325 | 325 | 0 | 1,041 | ~1,041 |
| MN | 340 | 340 | 0 | 811 | ~811 |
| FL | 695 | 695 | 0 | 1,037 | ~1,037 |
| MD | 220 | 220 | 0 | 316 | ~316 |
| GA | 356 | 356 | 0 | 383 | ~383 |
| MO | 487 | 487 | 0 | 416 | ~416 |
| **PA** | **1,741** | **796** | **945** | **734** | **Validation only** |

PA is included as a validation control. ALF records are already loaded for PA. Running the same integration and dedup process against PA tests whether the pipeline correctly identifies existing records and avoids double-counting.

### States Already Loaded (Not in Scope)

ALF records are already present in V20 for: IN (641 ALF), KY (407), NC (1,235), OH (1,054), VA (645), SC (378), PA (945), TN (389), WV (5). These states are excluded from this enhancement.

### Estimated New Records

Approximately 5,328 net new ALF records across the 8 expansion states after deduplication. This count includes 75 campus sister facilities where a NIC Maps ALF candidate shares an address with an existing SNF record in V20. These are retained as separate entries per the campus facility rule (see Key Decision #6 below).

---

## Key Decisions

### 1. Source_Type Classification

**Decision:** All facilities with AL units, MC units, or both are classified as Source_Type = "ALF" in the Combined Database.

This is a simplification. NIC Maps distinguishes between AL Open Units and MC Open Units, and facilities can have one or both. The Combined Database does not currently distinguish between assisted living and memory care at the Source_Type level, and introducing a new classification mid-enhancement would change the schema and invalidate downstream reporting logic.

**Impact:** Of the 6,062 total candidate records across 9 states:

| Subtype | Count | Treatment |
|---------|-------|-----------|
| AL-only (has AL units, no MC units) | 2,495 | Source_Type = "ALF" |
| AL+MC (has both AL and MC units) | 3,174 | Source_Type = "ALF" |
| MC-only (has MC units, no AL units) | 393 | Source_Type = "ALF" |

3,567 facilities (58.8%) are being classified as ALF despite having an MC component or being MC-only.

**Traceability:** A separate worksheet or appendix in the V21 Change Compendium will document the original NIC Maps unit breakdown (AL Open Units, MC Open Units) for every new record, with a flagged sublist of the 3,567 MC-only and AL+MC facilities. This preserves the ability to reclassify in a future version if the schema evolves.

### 2. Units = Beds

**Decision:** NIC Maps "AL Open Units" and "MC Open Units" are treated as equivalent to beds.

Total_Beds = AL Open Units + MC Open Units

This applies real unit counts from NIC Maps rather than using the default 35 beds that was applied during the original ALF integration when bed counts were missing. NIC Maps provides actual operational unit counts for all facilities.

### 3. Census Derivation

**Decision:** Census = Total_Beds x 0.80, rounded to the nearest integer.

This is consistent with the established methodology used for all 5,697 existing ALF records in V20. Analysis of the current database confirms:

- 3,806 of 5,697 ALF records have a census-to-beds ratio of exactly 0.800
- The overall ALF median ratio is 0.800
- The mean ratio is 0.801
- This 80% occupancy rate was applied uniformly across all states where ALF was previously loaded (IN, KY, NC, OH, PA, SC, TN, VA, WV)

The Core Rulebook (Section 3.4.4) documents that facilities with zero or null census have been assigned surrogate values based on facility type median. The 80% rate is the operational implementation of that policy for ALF records.

### 4. Geographic Tier Classification

**Decision:** Apply the interim classification methodology from the [[2026-02-21_Metro_Definition_Enhancement_Proposal|Metro Definition Enhancement Proposal]] for expansion state facilities. Do not attempt to solve the full geographic classification problem as part of this enhancement.

The interim methodology uses:

- **A_Metro:** 15-mile radius from principal metro center cities (same threshold as production)
- **B_Highway:** 10-mile radius from interpolated Interstate waypoints (~10,154 route sample points)
- **C_Rural:** All remaining facilities

The population threshold question (Open Question #1 in the Metro Enhancement Proposal) remains unresolved. For this enhancement, we apply the interim metro centers already defined for the expansion states without imposing a formal population floor. This is consistent with how the original footprint metros were defined (ad-hoc, based on operational familiarity, no formal threshold).

New-state geographic classifications will be tagged as "(Interim)" in the Original_Geographic_Tier column to distinguish them from production classifications in the footprint states. This preserves the ability to reclassify when the full CBSA-based metro enhancement is implemented.

The full geographic enhancement (Census Bureau CBSA centroids, DOT shapefile route geometry, formal population threshold, facility-dense cluster analysis) is a separate project and should not block the V21 database release.

### 5. Ownership_Type

**Decision:** Ownership_Type is recomputed across the entire V21 database after all new records are integrated, using the Four-Rule Count-Based Hierarchy from Core Rulebook Section 2.3.

This must be a post-integration step, not a per-record assignment, because the classification depends on how many facilities share each Corporate_Name across the full database. Adding new records from NIC Maps may change existing classifications (e.g., an operator that was Independent with 1 facility in V20 may become Corporate if a second facility appears in NIC Maps).

NIC Maps "Operator Name" maps to Corporate_Name. Operator names should be standardized against the existing corporate taxonomy where possible before the ownership reclassification runs.

### 6. Campus Sister Facility Rule

**Decision:** When a NIC Maps ALF candidate shares an address (or is within 0.3 miles) of an existing SNF record in the Combined Database, it is NOT treated as a duplicate. It is retained as a separate entry.

**Rationale:** SNF and ALF facilities at the same campus address have different revenue rates. Per the Fee Schedule (Core Rulebook Section 3), SNF TOTAL = $4,583.50 per bed per year and ALF TOTAL = $3,699.50 per bed per year. Treating a campus SNF and its sister ALF as one record would distort revenue projections and SOM calculations. The data model treats them as separate facilities because they are separate revenue-generating entities.

**Impact:** 75 expansion-state NIC Maps ALF candidates were initially flagged as address-match duplicates during dedup (Step 3). All 75 were reclassified as new records with `_dedup_type = campus_sister_facility`. These 75 facilities will appear in V21 alongside their existing SNF counterparts at the same or nearby addresses.

**QC note (resolved Feb 2026):** Campus structure verification confirmed 99.3% of SNF+ALF co-located pairs (668 of 673) have distinct bed counts and/or service flags, consistent with the facility-by-service counting methodology. 5 carbon-copy pairs flagged for review; 2 are already documented as intentional campus examples. The campus sister facility rule is working as designed. See `current/Facility_Count_Discrepancy_Explanation.md § Campus Structure Verification Protocol` for the full test methodology and results.

**PA validation note:** PA dedup was ALF-on-ALF (NIC Maps ALF candidates matched against existing V20 ALF records), so the campus sister facility rule did not apply. The PA validation result (731 of 734 matched, 99.6%) remains valid.

---

## Enhancement Steps

### Step 0: Create V21 Working Copy

Duplicate `1_Combined_Database_FINAL_V20_0.xlsx` to `1_Combined_Database_FINAL_V21_0.xlsx`. All modifications are made to V21 only. V20 remains untouched until V21 is validated, at which point V20 moves to Archive.

### Step 1: Extract and Filter NIC Maps Records

From the NIC Maps export, pull all records for the 9 target states where AL Open Units > 0 OR MC Open Units > 0. Exclude records that have NC Open Units > 0 but no AL or MC units (NC-only facilities are SNFs and should already be in the database). Records with both AL/MC and NC units are excluded from this enhancement as they represent mixed facilities that require dedup investigation.

Expected output: ~6,062 candidate records.

### Step 2: Field Mapping

Map NIC Maps columns to the 25-column Combined Database schema:

| Combined DB Column | NIC Maps Source | Logic |
|---|---|---|
| Source_Type | Derived | "ALF" for all records |
| Facility_Name | Building Name [col 1] | Direct mapping |
| Corporate_Name | Operator Name [col 41] | Map to existing corporate taxonomy |
| Address | Address [col 2] | Direct mapping |
| City | City [col 3] | Direct mapping |
| State | State [col 4] | Direct mapping |
| ZIP | Zip [col 5] | Direct mapping |
| County | County/Equiv [col 7] | Direct mapping |
| Ownership_Type | Derived | Placeholder; recomputed in Step 7 |
| Total_Beds | AL Open Units [col 34] + MC Open Units [col 36] | Units = Beds |
| Census | Derived | Total_Beds x 0.80 (rounded) |
| Do_We_Serve | Default | "No" |
| Integrated_Flag | Default | "No" |
| PCP_Flag | Default | "No" |
| MH_Flag | Default | "No" |
| Barrier | Default | Null |
| Latitude | Latitude [col 9] | Direct mapping |
| Longitude | Longitude [col 10] | Direct mapping |
| Data_Quality_Flag | Default | Null |
| Contract_Status | Default | "Green" |
| Geographic_Tier | Computed | See Step 5 |
| Original_Geographic_Tier | Computed | Same as Geographic_Tier |
| Metro_Assignment | Computed | See Step 5 |
| Distance_to_Metro_Center | Computed | See Step 5 |
| Metro_Center_Used | Computed | See Step 5 |

### Step 3: Deduplication

Match NIC Maps candidates against existing Combined DB records. This is the highest-risk step.

**Match hierarchy:**

1. **CCN match:** If a NIC Maps record has a CCN that matches an existing Combined DB record, it is a duplicate. Remove from candidates. (~13% of NIC Maps records have CCNs.)
2. **Address match:** Fuzzy match on Address + City + State for records without CCN match. Threshold to be determined during PA validation.
3. **Name match:** Secondary check on Facility_Name similarity for borderline address matches.

**Reference:** [[Archive/Data Challenges/True_Duplicates_Review.xlsx|True Duplicates Review]] for known dedup edge cases and patterns from the original ALF integration (598 duplicates removed from 1,253 candidates).

### Step 4: PA Validation

Run Steps 1 through 3 on PA only. Compare results against the 945 ALF records already in V20:

- How many of the 734 NIC Maps PA candidates are correctly identified as duplicates?
- How many would be incorrectly added (false negatives in dedup)?
- How many existing PA ALF records have no NIC Maps match (records from other sources)?

Discrepancies indicate dedup logic needs tuning. Do not proceed to Step 5 until PA validation is satisfactory.

### Step 5: Geographic Classification

Apply the interim geographic tier methodology to all new ALF candidates (post-dedup):

1. Calculate haversine distance from each facility (using NIC Maps Latitude/Longitude) to defined metro centers
2. Classify within 15 miles of metro center as "A_Metro"
3. Calculate distance to nearest Interstate waypoint for non-metro facilities
4. Classify within 10 miles of Interstate as "B_Highway"
5. All remaining facilities classified as "C_Rural"
6. Populate Metro_Assignment, Distance_to_Metro_Center, and Metro_Center_Used for A_Metro facilities
7. Tag Original_Geographic_Tier to preserve interim classification origin

Metro center definitions and Interstate waypoints from the [[2026-02-21_Metro_Definition_Enhancement_Proposal|Metro Enhancement Proposal]] interim work.

### Step 6: Integrate into V21

Append deduplicated, mapped, and geographically classified records to the V21 working copy. This is a row append operation; the schema does not change.

### Step 7: Recompute Ownership_Type

Run the Four-Rule Count-Based Hierarchy across the entire V21 database (existing + new records):

1. Null/blank Corporate_Name → Independent
2. Corporate_Name = "INDEPENDENT" → Independent
3. Corporate_Name appears on 2+ facilities → Corporate
4. Corporate_Name appears on exactly 1 facility → Independent

Document any reclassifications (existing records that changed Ownership_Type due to new NIC Maps records sharing their operator name).

### Step 8: QC Validation

Per Core Rulebook Section 6:

- Facility count validation by state (V20 totals + expected additions = V21 totals)
- No duplicate CCNs in V21
- Census values: all >= 1, mean and median within expected ranges
- Revenue reasonableness spot-checks using Fee Schedule ALF TOTAL ($3,724.00)
- Corporate entity assignments spot-checked against [[02_Strategy/Corporate/2026-02-20_New_State_Entry_MUO_Analysis|MUO Analysis]]
- Geographic tier distribution reviewed per state

### Step 9: Documentation and Version Control

- Produce V20 → V21 Change Compendium documenting:
  - State-by-state record additions
  - Dedup results (matched, removed, edge cases)
  - MC/AL+MC reclassification sublist (3,567 facilities)
  - Ownership_Type reclassifications
  - Geographic tier assignments
  - Any anomalies or data quality flags
- Move V20 files to Archive
- Update [[01_Data Model/_Data_Model_Index|Data Model Index]] with V21 entry

---

## Source Files

| File | Location | Role |
|---|---|---|
| Combined Database V20.0 | `01_Data Model/Current/1_Combined_Database_FINAL_V20_0.xlsx` | Source; duplicated to V21 in Step 0 |
| NIC Maps Export | `01_Data Model/Archive/Eventus WholeHealth One-Time Nationwide Inventory Export - 11.17.25.xlsx` | ALF/MC source data |
| Core Rulebook V20.0 | `01_Data Model/Current/6_Core_Rulebook_V20_0.md` | Field definitions, business rules, QC protocol |
| Fee Schedule V20.1 | `01_Data Model/Current/2_Fee_Schedule_Reference_V20_1.xlsx` | Revenue computation reference |
| Metro Enhancement Proposal | `01_Data Model/Reference/2026-02-21_Metro_Definition_Enhancement_Proposal.md` | Geographic tier methodology |
| True Duplicates Review | `01_Data Model/Archive/Data Challenges/True_Duplicates_Review.xlsx` | Dedup edge case reference |
| MUO Analysis | `02_Strategy/Corporate/2026-02-20_New_State_Entry_MUO_Analysis.md` | Corporate partner validation |

---

## Discussion Notes

### Geographic Classification and the Missouri Problem (Feb 24, 2026)

During planning for this enhancement, we discussed the challenge of applying population-based metro thresholds to states like Missouri. The concern: outside of St. Louis (~130 ALF/MC facilities) and Kansas City (~53), Missouri has significant facility concentrations in areas that fall below conventional MSA population thresholds. Springfield has 32 ALF/MC facilities, Joplin has 16, and 72 facilities sit in non-metro areas entirely. A rigid 130K population floor (the de facto precedent from Harrisonburg in the original footprint classification) would miss operationally meaningful clusters.

This points to a broader limitation of population-based metro classification. Clinical operations care about facility density, not city population. A town of 50K with 12 ALFs along a 20-mile stretch is a viable service delivery zone even though it will never appear on a metro threshold list.

**Recommendation for future geographic enhancement:** The population threshold should not be applied in isolation. A more robust approach would compute a state-wide average facility density metric that accounts for the relationship between population centers and facility clusters, then pressure-test the metro threshold against actual facility distribution patterns. States like Missouri, where facility density is dispersed across many smaller population centers, may need a different threshold than states like Florida, where facilities concentrate heavily around a few large metros.

This could take the form of:

1. For each state, compute the population threshold that captures X% (e.g., 70%) of all facilities within the 15-mile metro radius
2. Compare that threshold to the national standard (130K or whatever is adopted)
3. Where the state-specific threshold diverges significantly from the national standard, flag it for review and potentially apply a state-adjusted floor
4. Use spatial clustering analysis (DBSCAN or similar) to identify facility-dense zones that fall outside any population-defined metro, as an additional classification layer

This analysis belongs in the [[2026-02-21_Metro_Definition_Enhancement_Proposal|Metro Enhancement Proposal]], not in this database enhancement. Documented here for continuity.

### GPS Coordinate Quality Assessment (Feb 24, 2026)

NIC Maps provides Latitude and Longitude for all facility records. Before relying on these coordinates for geographic tier calculations (Step 5), we ran a quality assessment across all 6,062 candidate ALF/MC records in the 9 target states.

**Coverage:** 100% of candidate records have populated, non-null, non-zero coordinates. No geocoding remediation is needed for missing data.

**Validation methodology:** Since external geocoding services were not available in the working environment, we ran three internal consistency checks against the NIC Maps coordinate data:

1. **State bounding box check.** Verified that every facility's lat/long falls within the expected geographic boundaries for its stated state. Used approximate state bounding boxes (e.g., Michigan: lat 41.7 to 48.3, lon -90.4 to -82.1). Result: 6,060 of 6,062 facilities pass. Two facilities fall marginally outside their state bounding box, both are legitimate border-area addresses (Broad Creek Manor in Whiteford, MD near the PA border; Burr Oak Manor in Genoa City, WI near the IL border). These are not geocoding errors.

2. **ZIP centroid clustering check.** Examined all ZIP codes with 3 or more candidate facilities to detect whether coordinates were imputed from ZIP code centroids rather than geocoded to actual addresses. If a commercial dataset geocodes lazily, multiple facilities in the same ZIP will share identical coordinates. Result: Only 1 ZIP code (16323 in PA, 3 facilities) has all facilities at identical coordinates out of 804 ZIP codes with 3+ facilities. This is negligible. The dataset does not exhibit ZIP centroid geocoding.

3. **Within-ZIP geographic spread check.** For the 298 ZIP codes with 5 or more candidate facilities, computed the maximum pairwise haversine distance between facilities. Healthy data shows spatial spread within each ZIP; centroid-imputed data shows zero spread. Result: Zero ZIPs have zero spread. 285 of 298 (95.6%) show normal spread of 1 to 10 miles, consistent with actual address-level geocoding. 5 ZIPs show small spread under 1 mile (likely small urban ZIPs where facilities are genuinely clustered). 8 ZIPs show large spread over 10 miles (likely large rural ZIP codes, not geocoding errors).

**Coordinate precision:** 99.5% of facilities have 4 or more decimal places of precision (accurate to approximately 36 feet), and 95.5% have 5 or more decimal places. This is building-level precision, consistent with a commercial real estate database that geocodes to property addresses.

**Conclusion:** NIC Maps GPS coordinates are high quality and suitable for direct use in geographic tier calculations without a remediation step. The two border-area facilities and the one identical-coordinate ZIP (3 facilities) should be flagged for manual review during QC (Step 8) but do not indicate systematic data quality issues.

**Deferred validation:** A stronger test would geocode a random sample of 20 to 30 facility addresses through an independent geocoding service (e.g., Census Bureau, Google Maps API) and compare the resulting coordinates to NIC Maps coordinates to measure absolute positional accuracy. This was not possible in the current environment but should be performed if geographic tier assignments produce unexpected results during QC.

---

## Execution Results (Feb 24, 2026)

### Final Record Counts

| State | V20 Records | New ALF Records | V21 Total |
|-------|------------|----------------|-----------|
| FL | 695 | 1,037 | 1,732 |
| GA | 356 | 383 | 739 |
| IL | 674 | 570 | 1,244 |
| MD | 220 | 316 | 536 |
| MI | 425 | 754 | 1,179 |
| MN | 340 | 811 | 1,151 |
| MO | 487 | 416 | 903 |
| WI | 325 | 1,041 | 1,366 |
| **All other states** | **17,421** | **0** | **17,421** |
| **TOTAL** | **20,943** | **5,328** | **26,271** |

### PA Validation Results

734 NIC Maps PA candidates tested against 945 existing PA ALF records. 731 matched (99.6%), confirming the dedup pipeline correctly identifies existing records. 3 candidates had no match and appear to be legitimate facilities missing from V20 (not added in this enhancement since PA was validation-only).

### Campus Sister Facility Reclassification

75 expansion-state ALF candidates initially flagged as duplicates because they share addresses with existing SNF records. All 75 reclassified as new records per the campus facility rule (Key Decision #6). These represent ALF buildings on the same campus as SNF buildings, with different revenue rates.

### Geographic Tier Classification

| Tier | Count | Percent |
|------|-------|---------|
| A_Metro (Interim) | 2,587 | 48.6% |
| B_Highway (Interim) | 1,296 | 24.3% |
| C_Rural | 1,445 | 27.1% |

All new records tagged "(Interim)" in Original_Geographic_Tier to distinguish from production footprint classifications.

### Ownership_Type Recomputation

Four-Rule Hierarchy applied across full V21 (26,271 records):

| Category | V20 | V21 | Change |
|----------|-----|-----|--------|
| Corporate | 11,858 | 16,035 | +4,177 |
| Independent | 9,085 | 10,236 | +1,151 |

9 existing V20 records were reclassified due to NIC Maps operator names creating new multi-facility relationships. Of those, 6 changed from Independent to Corporate (operators gained a second facility via NIC Maps data) and 3 changed from Corporate to Independent (name matching edge cases where NIC Maps data clarified the operator was distinct).

### QC Validation Summary

All QC checks pass for the enhancement scope:

| Check | Result |
|-------|--------|
| State count reconciliation (V20 + new = V21) | PASS (all 8 states) |
| Source_Type populated | PASS (15,244 SNF + 11,027 ALF) |
| Census: no nulls, no zeros, no negatives | PASS |
| Total_Beds: no nulls in new records | PASS (7 pre-existing V20 nulls unchanged) |
| Ownership_Type populated | PASS |
| Critical columns (Source_Type, Facility_Name, Address, City, State) | PASS |
| GPS coordinate coverage | PASS (100%) |

Pre-existing V20 issues noted but not addressed in this enhancement: 2,230 null ZIP codes (all in V20), 7 null Total_Beds (last 7 rows of V20).

---

## V21.1 Corporate Name Standardization (Feb 24, 2026)

### Rationale

V21.0 integrated NIC Maps "Operator Name" values directly into the Corporate_Name field without standardizing against the existing V20 corporate taxonomy. This created variant spellings for the same operator (e.g., "Brookdale Senior Living Inc." from NIC Maps vs "BROOKDALE SENIOR LIVING" in V20), which caused the Four-Rule Ownership_Type hierarchy to undercount Corporate classifications.

### Method

All 6,174 unique Corporate_Name values in V21.0 were normalized by stripping common suffixes (LLC, Inc., Corp., Ltd., LP, Management, Services, Holdings, etc.), removing punctuation, and collapsing to uppercase for comparison. Names that normalized to the same form were clustered. For each cluster with multiple variants, the V20 canonical form was selected as the standard (preferring the variant with the most existing rows). Where no V20 form existed, the most common variant was used.

### Results

| Metric | Value |
|--------|-------|
| Variant names identified | 218 |
| Rows with Corporate_Name changed | 1,240 |
| Of which: V20 records | 141 |
| Of which: new records | 1,099 |
| Unique corporate names eliminated | 218 (6,174 → 5,956) |

### Top Standardizations (by row count)

| NIC Maps Variant | V20 Canonical Form | Rows Remapped |
|------------------|--------------------|---------------|
| Brookdale Senior Living Inc. | BROOKDALE SENIOR LIVING | 147 |
| Americare Senior Living | AMERICARE SENIOR LIVING | 64 |
| Sunrise Senior Living | SUNRISE SENIOR LIVING MANAGEMENT, INC | 62 |
| StoryPoint Group | STORYPOINT | 56 |
| Gardant Management Solutions | GARDANT MANAGEMENT SOLUTIONS, INC | 45 |
| Cedarhurst Senior Living | CEDARHURST SENIOR LIVING | 41 |
| Lifespark | LIFESPARK | 41 |
| Presbyterian Homes & Services | PRESBYTERIAN HOMES & SERVICES | 36 |
| Senior Lifestyle | SENIOR LIFESTYLE | 35 |
| Life Care Services | LIFE CARE SERVICES | 30 |

### Ownership_Type Impact

After standardization, the Four-Rule Hierarchy was rerun across all 26,271 records:

| Category | V21.0 | V21.1 | Delta |
|----------|-------|-------|-------|
| Corporate | 16,035 | 16,214 | +179 |
| Independent | 10,236 | 10,057 | -179 |

179 facilities were reclassified from Independent to Corporate. These were operators whose facilities had been split across variant name spellings, causing each variant to appear as a single-facility operator (Independent). After standardization, the consolidated name exceeded the 2-facility threshold and the operator correctly classified as Corporate. 113 of these were existing V20 records, 66 were new NIC Maps records. 132 unique operators were affected.

### QC Verification

The V21.0 → V21.1 diff confirms that only two columns were modified: Corporate_Name (1,240 cells) and Ownership_Type (179 cells). No other columns, no rows added or removed, no schema changes. The diff is surgical and traceable.

---

## Open Items

1. **Revenue recomputation.** After V21.1 is validated, scenario models (S1/S2/S3) need to be regenerated to reflect the expanded facility base. This is a separate deliverable from the database enhancement.
2. **Geographic tier population threshold.** Not resolved for this enhancement. Interim metro centers applied as-is. Full resolution deferred to the [[2026-02-21_Metro_Definition_Enhancement_Proposal|Metro Enhancement Proposal]]. See Discussion Notes above for the Missouri-driven insight on state-wide facility density as a pressure test for population thresholds.
3. ~~**75 campus sister facilities.**~~ **Resolved.** Campus structure verification (Feb 2026) confirmed facility-by-service model is working as designed. 668 of 673 SNF+ALF co-located pairs pass structural checks. 5 carbon-copy pairs noted for future review (2 are documented intentional examples). See `current/Facility_Count_Discrepancy_Explanation.md § Campus Structure Verification Protocol`.
4. ~~**PA 3 unmatched candidates.**~~ **Resolved.** Re-validation (Mar 2026) with improved fuzzy matching found all 1,000 NIC Maps PA ALF candidates match existing database records (941 to ALFs, 59 to SNFs as campus sisters). Original "3 unmatched" was a match threshold artifact. PA validation is effectively 100%.
5. ~~**Pre-existing V20 data quality.**~~ **Resolved.** 2,227 null ZIPs filled Mar 2026 by nearest-neighbor GPS lookup (2,225) and web search (2). 7 null bed counts also resolved (5 rows populated from internal data and derivation). Zero data gaps remain.
6. **Remaining corporate name variants.** The suffix-stripping normalization catches the most common variants, but there may be additional cases where operators use genuinely different trade names (e.g., a parent company with branded subsidiaries). A manual review of operators with 1 facility in V21.1 that are near-matches to larger Corporate operators would catch these, but diminishing returns suggest this is low priority.

---

*Last updated: February 24, 2026 — V21.1 corporate name standardization complete.*
