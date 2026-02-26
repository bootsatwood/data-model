# Database Change Request
## Combined Database V19.1 Enhanced → V19.2 (or V20)

**Date**: December 2025  
**Requested By**: Roian  
**Status**: PENDING REVIEW  

---

## Summary of Requested Changes

### EXECUTE NOW (V19.2)
*Safe to implement — no population shifts*

| Change | Type | Facilities Affected | Impact | Priority |
|--------|------|---------------------|--------|----------|
| Cardon barrier flag | Add barrier | 34 | Barrier count 848 → 882 | **REQUIRED** |
| Corporate name standardization | Naming convention | 6 entities (~57 facilities) | Clean crosswalk to scoring | **REQUIRED** |
| Contract_Status population | Validated | 13 nulls | Minor — 99.94% populated | LOW |

### FUTURE CONSIDERATION (Post-Project)
*Requires validation — will shift population counts*

| Change | Type | Facilities Affected | Impact | Risk |
|--------|------|---------------------|--------|------|
| Metro recalculation (MSA centroids) | Repopulate 3 columns | All 20,930 | A_Metro count will change | **HIGH** |
| Interstate distance columns | Add 2 new columns | All 20,930 | New data | MEDIUM |
| Geographic_Tier recalculation | Derived | All 20,943 | A/B/C counts will change | **HIGH** |
| Reference tables in Rulebook | Documentation | N/A | Methodology formalization | LOW |

**⚠️ DO NOT EXECUTE FUTURE CONSIDERATION ITEMS UNTIL CURRENT PROJECT COMPLETE ⚠️**

---

## Change 1: Cardon Barrier Flag (REQUIRED)

### Current State
- **Entity**: CARDON & ASSOCIATES
- **Facilities**: 34
- **Database Barrier Flag**: None
- **Handling**: Manual exception rule applied at report generation ("Permanent barrier")

### Problem
This violates Core Rulebook Governing Principle #1: "Combined Database is the single source of truth for all facility data."

Cardon is currently excluded via exception logic in:
- V19_Metro_TAM_SAM_SOM_Methodology.md
- V19_1_to_V19_2_Comparison_Report
- All V19.2 report filters

### Requested Change
Add `Barrier = "Permanent - Cardon"` (or appropriate barrier category) to all 34 Cardon facilities in the database.

### Facilities to Update

```sql
UPDATE Combined_Database
SET Barrier = 'Permanent - Cardon'
WHERE Corporate_Name = 'CARDON & ASSOCIATES'
```

**Facility Count**: 34  
**States**: IN (primary)

### Impact
- Barrier count: 848 → 882
- Eliminates need for manual Cardon exception in all reports
- All downstream reports automatically exclude Cardon via standard barrier logic
- Documentation simplification: remove "Cardon permanent barrier" notes from methodology docs

### Validation After Change
```
SELECT COUNT(*) FROM Combined_Database WHERE Barrier IS NOT NULL
-- Expected: 882

SELECT COUNT(*) FROM Combined_Database WHERE Corporate_Name = 'CARDON & ASSOCIATES'
-- Expected: 34 (all should have Barrier populated)
```

---

## Change 2: Geographic_Tier Alignment

**Status:** DOCUMENTED — NO IMMEDIATE CHANGE

**Current Gap:**
- 2,039 facilities classified A_Metro
- Only 1,667 have Metro_Assignment populated
- 372 facilities are A_Metro but missing Metro_Assignment (in metros outside current 12)

**Resolution for Now:**
Document the distinction in Core Rulebook Section 2.8:
- Geographic_Tier = operational reach (19 metros)
- Metro_Assignment = strategic targeting (12 metros)

**Future Resolution:**
See "Future Consideration" section at end of document for comprehensive geographic recalculation proposal.

---

## Change 3: Contract_Status Validation (VALIDATED - MINOR ISSUE)

### Validation Results

| Value | Count | Percentage |
|-------|-------|------------|
| Green | 20,879 | 99.7% |
| Yellow | 38 | 0.2% |
| Red | 13 | 0.1% |
| NULL | 13 | 0.06% |

**Population Rate:** 99.94% (20,930 of 20,943)

### NULL Analysis
- 13 facilities have NULL Contract_Status
- 12 of 13 are facilities we currently serve (Do_We_Serve = Yes)
- 1 is a facility we don't serve

### Recommendation
**Low priority** — only 13 facilities affected. Options:
1. Manually review and populate the 13 nulls
2. Treat NULL as "Unknown" in report filters (exclude from Green-only filters)
3. Default NULL to Green for served facilities (assumption: if we serve them, relationship is active)

### Action
Flag for manual review during next data refresh. No blocking issue for V19.2.

---

## Change 4: Corporate Name Standardization (REQUIRED)

### Current State
When crosswalking between Book1_Scoring.xlsx (V20 Corporate Scoring) and Combined_Database_FINAL_V19_1_Enhanced.xlsx, 6 entities failed to match due to naming convention differences.

### Name Mapping Table

| Workbook Name | Database Name(s) | Facilities | Issue |
|---------------|------------------|------------|-------|
| Topaz | TOPAZ HEALTHCARE | 11 | Missing "HEALTHCARE" suffix |
| Kissito | KISSITO HEALTHCARE | 13 | Missing "HEALTHCARE" suffix |
| Terra Bella | TERRABELLA SENIOR LIVING | 11 | Spacing + suffix difference |
| Sunrise | SUNRISE SENIOR LIVING | 11+ | Missing "SENIOR LIVING" suffix |
| Carrolton | CARROLTON FACILTY MANAGEMENT + CARROLTON NURSING HOMES | 4 + 6 = 10 | **Split across 2 corporate entities** |
| Momentous Health | MOMENTUS HEALTH | 1 | **Spelling difference + only 1 facility** |

### Requested Changes

**4A. Standardize Corporate_Name column to match scoring workbook conventions:**

| Current Database Value | Proposed Standard Value |
|------------------------|------------------------|
| TOPAZ HEALTHCARE | TOPAZ |
| KISSITO HEALTHCARE | KISSITO |
| TERRABELLA SENIOR LIVING | TERRA BELLA |
| SUNRISE SENIOR LIVING | SUNRISE |

**4B. Consolidate Carrolton entities:**

Merge the following into single corporate entity "CARROLTON":
- CARROLTON FACILTY MANAGEMENT (4 facilities)
- CARROLTON NURSING HOMES (6 facilities)

This will result in 10 facilities under "CARROLTON".

**4C. Resolve Momentous Health:**

Options:
1. Correct spelling: MOMENTUS HEALTH → MOMENTOUS HEALTH
2. Flag for review: Only 1 facility in database — does not meet MUO criteria (7+ facilities)
3. Determine if additional facilities should be associated with this corporate entity

### Impact
- Enables clean crosswalk between scoring workbook and database
- Eliminates manual name mapping during report generation
- Ensures facility counts match between systems

### Validation After Change
```python
# All 70 scoring entities should match exactly
scoring_names = [list of 70 corporate names from Book1]
db_corps = db['Corporate_Name'].unique()

for name in scoring_names:
    assert name.upper() in [c.upper() for c in db_corps], f"Missing: {name}"
```

---

## Implementation Plan

### Phase 1: Execute Now (V19.2 — Safe Changes)
1. ☐ Add Cardon barrier flags (34 facilities)
2. ☐ Standardize corporate names (6 entities, ~57 facilities)
3. ☐ Consolidate Carrolton entities (merge 2 → 1)
4. ☐ Update barrier count in all documentation (848 → 882)
5. ✅ Validate Contract_Status population — **DONE: 99.94% populated, 13 nulls flagged for review**

### Phase 2: Documentation Updates (V19.2)
1. Remove "Cardon permanent barrier (manual)" from:
   - V19_Metro_TAM_SAM_SOM_Methodology.md
   - V19_1_to_V19_2_Comparison_Report
   - Any other methodology docs
2. Add Geographic_Tier clarification note to Core Rulebook Section 2.8.1
3. Update Core Rulebook Section 5.1 barrier count (848 → 882)
4. Document corporate name standardization rules in Core Rulebook

### Phase 3: Report Regeneration (V19.2)
1. Regenerate V19.2 reports with updated database
2. Verify Cardon exclusion works via standard barrier logic
3. Verify all 70 scoring entities crosswalk cleanly to database
4. Update facility counts in all summary tables

### Phase 4: Future (Post-Project — Geographic Overhaul)
**⚠️ DO NOT EXECUTE UNTIL CURRENT PROJECT COMPLETE ⚠️**
1. ☐ Conduct sensitivity analysis — Metro (MSA centroid method vs current)
2. ☐ Conduct sensitivity analysis — Highway (corridor method vs current exit-based)
3. ☐ Add Metro_Reference_Table to Core Rulebook
4. ☐ Add Interstate_Reference_Table to Core Rulebook
5. ☐ Add Named View definitions (Metro_12, Metro_19, Highway_5) to Core Rulebook
6. ☐ Repopulate Metro_Assignment, Distance_to_Metro_Center, Metro_Center_Used for all facilities
7. ☐ Add Nearest_Interstate, Distance_to_Interstate columns
8. ☐ Recalculate Geographic_Tier from new distance data
9. ☐ Validate all report outputs against new data

---

## Sign-Off

| Role | Name | Date | Approval |
|------|------|------|----------|
| Requested By | Roian | Dec 2025 | ☐ |
| Data Owner | | | ☐ |
| Validated By | | | ☐ |

---

## Appendix: Cardon Facility List (34 Facilities)

**All facilities in Indiana | 20 SNF, 14 ALF | Current Barrier: None**

| Facility Name | City | Type |
|---------------|------|------|
| ALTENHEIM HEALTH & LIVING COMMUNITY | Indianapolis | SNF, ALF |
| ARBOR TRACE HEALTH & LIVING COMMUNITY | Richmond | SNF, ALF |
| ASPEN TRACE HEALTH & LIVING COMMUNITY | Greenwood | SNF, ALF |
| BELL TRACE HEALTH AND LIVING CENTER | Bloomington | SNF |
| BROOKSIDE VILLAGE INC | Jasper | SNF, ALF |
| BROWN COUNTY HEALTH AND LIVING COMMUNITY | Nashville | SNF |
| CARMEL HEALTH & LIVING COMMUNITY | Carmel | SNF |
| COPPER TRACE HEALTH & LIVING COMMUNITY | Westfield | SNF, ALF |
| COUNTRYSIDE MANOR HEALTH & LIVING COMMUNITY | Anderson | SNF |
| CUMBERLAND TRACE HEALTH & LIVING COMMUNITY | Plainfield | SNF, ALF |
| GREENWOOD HEALTH AND LIVING COMMUNITY | Greenwood | SNF |
| HAMILTON TRACE OF FISHERS | Fishers | SNF, ALF |
| HARBOUR MANOR HEALTH & LIVING COMMUNITY | Noblesville | SNF, ALF |
| HOOSIER HEALTH & LIVING COMMUNITY | Brownstown | SNF |
| LINCOLN HILLS OF NEW ALBANY | New Albany | SNF, ALF |
| MORRISTOWN MANOR | Morristown | SNF |
| PAOLI HEALTH AND LIVING COMMUNITY | Paoli | SNF, ALF |
| RAWLINS HOUSE HEALTH & LIVING COMMUNITY | Pendleton | SNF, ALF |
| TERRACE AT SOLARBRON | Evansville | SNF, ALF |
| UNIVERSITY HEIGHTS HEALTH AND LIVING COMMUNITY | Indianapolis | SNF |

**Note:** Some locations have both SNF and ALF facilities listed separately in the database.

---

## FUTURE CONSIDERATION: Geographic Infrastructure Overhaul

**⚠️ DO NOT EXECUTE UNTIL CURRENT PROJECT COMPLETE — WILL SHIFT POPULATION COUNTS ⚠️**

### Background

Current geographic classification was built ad-hoc:
- Clinical ops provided city list
- Google lookup for lat/long of city centers
- Distance calculated from facilities to those points

This creates gaps when new metros are requested and lacks defensibility.

### Proposed Architecture

**Database contains facility-level data only:**

| Column | Description |
|--------|-------------|
| Latitude | Facility coordinate (existing — 99.9% populated) |
| Longitude | Facility coordinate (existing — 99.9% populated) |
| Nearest_MSA | Calculated — which MSA centroid is closest |
| Distance_to_MSA | Calculated — miles to nearest MSA centroid |
| Nearest_Interstate | **NEW** — which Interstate is closest |
| Distance_to_Interstate | **NEW** — miles to nearest Interstate |
| Geographic_Tier | Derived: A (≤15mi MSA), B (≤10mi Interstate, not A), C (all other) |

**Core Rulebook contains methodology:**

| Table | Contents |
|-------|----------|
| Metro_Reference_Table | All MSAs in 13-state footprint with Census centroid coordinates |
| Interstate_Reference_Table | All Interstates in 13-state footprint with DOT shapefile reference |
| Named Views | Metro_12, Metro_19, Highway_5 (filter definitions for reports) |

**Reports filter on named views defined in Rulebook.**

### Data Sources

| Data | Source | Notes |
|------|--------|-------|
| MSA centroids | Census Bureau CBSA definitions | Publicly available, federal standard |
| Interstate routes | DOT National Highway System | Shapefile/polyline data |

### Proposed Database Changes

**Repopulate existing columns (all 20,930 facilities with coordinates):**
- Metro_Assignment → Nearest_MSA (or keep name, expand population)
- Distance_to_Metro_Center → recalculate using MSA centroids
- Metro_Center_Used → recalculate

**Add new columns:**
- Nearest_Interstate
- Distance_to_Interstate

**Recalculate derived column:**
- Geographic_Tier (A/B/C based on distance thresholds)

### Required Before Execution

**Sensitivity Analysis — Metro:**
Compare current 2,039 A_Metro count to what MSA centroid method would produce.

**Sensitivity Analysis — Highway:**
Compare current 1,250 B_Highway (exit-based) to proposed corridor-based method:
- How many current B_Highway would still qualify?
- How many new facilities would qualify?
- How many would lose classification?

If deltas are >10%, requires business decision before proceeding.

### Rulebook Additions Required

**Section 2.8.2 — Metro Reference Table:**
All MSAs in 13-state footprint (estimated 50-80 metros) with:
- MSA_Name
- Center_City
- Center_Latitude
- Center_Longitude
- State

**Section 2.8.X — Interstate Reference Table:**
All Interstates in 13-state footprint with shapefile reference.

**Section 2.8.X — Named Reporting Views:**

| View Name | Definition | Use |
|-----------|------------|-----|
| Metro_12 | Cleveland-Akron, Columbus, Cincinnati, Toledo, Indianapolis, Northwest Indiana, Evansville, Louisville, Lexington, Charlotte, Richmond, Harrisonburg-Charlottesville | Current priority |
| Metro_19 | Metro_12 + Greensboro-High Point, Raleigh, Wilmington, Columbia, Charleston SC, Dayton, Roanoke, Charleston WV | Original operational |
| Highway_5 | I-65, I-71, I-75, I-77, I-85 | Current priority corridors |

### Rationale

- **Comprehensive:** Every metro/interstate in footprint covered, not just ones someone thought to ask about
- **Repeatable:** Adding a metro = updating Rulebook view definition, not database rebuild
- **Defensible:** "We use Census MSA definitions" is a real answer
- **Flexible:** Database is complete; reports filter on business need

---

**END OF CHANGE REQUEST**
