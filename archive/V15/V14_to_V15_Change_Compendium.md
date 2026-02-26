# V14 → V15 Change Compendium
## Eventus Healthcare Economic Model

**Date**: November 2025  
**Previous Version**: V14.0  
**Current Version**: V15.0  
**Author**: Claude (AI Assistant)

---

## Executive Summary

Version 15.0 corrects two methodological issues in the Comprehensive Report Workbook:

1. **Tables 1-3 (Facility Counts):** SAM and SOM segments now correctly include both Corporate and Independent facilities
2. **Tables 16-18, 25 (Corporate Rankings):** INDEPENDENT is now excluded as it is not a corporate entity

These changes affect report outputs only. The underlying database, scenario calculations, and fee structures remain unchanged.

---

## Part 1: Change Details

### Change 1: Tables 1-3 Facility Count Filters

**Issue Identified:**
Tables 1-3 display facility counts broken down by Corporate/Independent ownership. Under V14 rules, SAM and SOM rows showed "0" for Independent facilities because the filter required "Corporate only" ownership.

This was misleading because:
- The tables are designed to show counts BY ownership type
- Showing "0" for Independent implied no Independent facilities exist in those markets
- The geographic and barrier filters should apply, but ownership filter should not

**V14 Rule (Incorrect):**

| Segment | Markets | Ownership | Barriers |
|---------|---------|-----------|----------|
| SAM | Existing + Priority | Corporate only | Minus barriers |
| SOM | Existing only | Corporate only | Minus barriers |

**V15 Rule (Corrected):**

| Segment | Markets | Ownership | Barriers |
|---------|---------|-----------|----------|
| SAM | Existing + Priority | Corporate + Independent | Minus barriers |
| SOM | Existing only | Corporate + Independent | Minus barriers |

**Impact on Values:**

| Table | Segment | V14 Independent | V15 Independent |
|-------|---------|-----------------|-----------------|
| Table 3 | SAM | 0 / 0 | Shows actual counts |
| Table 3 | SOM | 0 / 0 | 2,051 / 391 |

**Rationale:**
Tables 1-3 answer the question "How many facilities exist by ownership type within this market segment?" The ownership breakdown is the OUTPUT, not a filter. Geographic boundaries and barrier status are the appropriate filters for these tables.

**Note:** Revenue tables (4-9, 10-15) continue to use "Corporate only" filter for SAM/SOM as documented in V14 Rulebook Section 4.4.

---

### Change 2: Tables 16-18, 25 Corporate Rankings

**Issue Identified:**
Tables 16-18 and 25 rank corporate entities by revenue opportunity. Under V14, all Independent facilities were grouped together as a single entity called "INDEPENDENT" which then appeared in the rankings.

This was misleading because:
- INDEPENDENT is not a corporate entity or chain
- It represents unrelated individual facilities
- Ranking it alongside chains like "TRILOGY HEALTH SERVICES" implies comparable strategic value
- The total for INDEPENDENT was artificially high due to aggregating many unrelated facilities

**V14 Output (Incorrect):**

| Rank | Corporate Name | Total Opportunity |
|------|---------------|-------------------|
| 1 | INDEPENDENT | $159,396,843 |
| 2 | TRILOGY HEALTH SERVICES | $33,176,493 |
| 3 | AMERICAN SENIOR COMMUNITIES | $30,088,639 |

**V15 Output (Corrected):**

| Rank | Corporate Name | Total Opportunity |
|------|---------------|-------------------|
| 1 | TRILOGY HEALTH SERVICES | $33,176,493 |
| 2 | AMERICAN SENIOR COMMUNITIES | $30,088,639 |
| 3 | FOUNDATIONS HEALTH SOLUTIONS | $22,177,376 |

**Rationale:**
These tables are designed to identify and rank corporate chains for strategic targeting. Independent facilities represent individual outreach opportunities, not chain-level relationships. They should be analyzed separately through other lenses (geographic, facility size, etc.) rather than artificially grouped as a pseudo-entity.

**Implementation:**
The filter now includes `Ownership_Type == 'Corporate'` in addition to the existing SOM filters (Existing markets, minus barriers).

---

## Part 2: Files Affected

### Modified Files

| File | Changes |
|------|---------|
| Comprehensive_Report_Workbook_V15.xlsx | Tables 1-3 and 16-18 recalculated |
| Final_Model_Rulebook_V15.md | Section 4.4 split into Facility vs Revenue rules; Section 5.5 updated with exclusion rule |
| START_HERE_V15.md | Added V15 Key Changes section |
| QC_Validation_Workbook_V15.xlsx | Updated protocol with V15-specific checks |

### Unchanged Files

| File | Reason |
|------|--------|
| Combined_Database_FINAL_V15.xlsx | No data changes |
| Economic_Model_Scenario_1/2/3_Combined_V15.xlsx | No calculation changes |
| Fee_Schedule_Reference_V15.xlsx | No fee changes |

---

## Part 3: Validation

### Pre-Change Values (V14)

**Table 3 (Total Facilities) - SOM Row:**
- Corporate: 2,331 / 908
- Independent: 0 / 0
- Total: 2,331 / 908

**Table 16 (Top Corporate - Total Opportunity) - #1:**
- INDEPENDENT: $159,396,843

### Post-Change Values (V15)

**Table 3 (Total Facilities) - SOM Row:**
- Corporate: 2,331 / 908
- Independent: 2,051 / 391
- Total: 4,382 / 1,299

**Table 16 (Top Corporate - Total Opportunity) - #1:**
- TRILOGY HEALTH SERVICES: $33,176,493

### Key Metrics (Unchanged)

| Metric | Value |
|--------|-------|
| Total Facilities | 17,434 |
| Facilities We Serve | 1,743 |
| Total Barriers | 1,383 |
| SNF Current Revenue | $93,607,105 |
| ALF Current Revenue | $83,991,652 |
| Total Current Revenue | $177,598,757 |
| Total Integration Revenue | $127,760,637 |
| Total New Business Revenue | $5,115,910,599 |
| Total Potential Revenue | $5,243,671,236 |

---

## Part 4: Rulebook Updates

### Section 4.4 Changes

**Added:** Distinction between Revenue Tables and Facility Count Tables with separate filter definitions.

**Key Addition:**
> "**IMPORTANT:** Different tables use different filter rules. See table-specific rules below."

### Section 5.2 Changes

**Added:** V15 Note clarifying the methodology for Tables 1-3:
> "V15 Note: SAM and SOM rows include BOTH Corporate AND Independent facilities that meet the geographic and barrier criteria."

### Section 5.5 Changes

**Added:** Critical rule for corporate rankings:
> "**CRITICAL RULE:** These tables rank corporate entities (chains) only. **Independent facilities are EXCLUDED from rankings.** Independent is not a corporate entity and cannot be meaningfully compared to corporate chains."

---

## Part 5: QC Protocol Updates

The QC Validation Workbook now includes V15-specific checks:

1. Verify Tables 1-3 SAM/SOM rows show non-zero Independent counts
2. Verify Tables 16-18 top-ranked entity is NOT "INDEPENDENT"
3. Confirm total facility counts in SOM include both ownership types

---

## Part 6: Authorization

**Change Requested:** November 2025  
**Requestor:** Roian (Project Owner)  
**Authorization Type:** Verbal direction in conversation  

**Specific Authorizations:**
1. Modify TAM/SAM/SOM filters for Tables 1-3 to include Independent
2. Exclude INDEPENDENT from corporate ranking tables
3. Document changes in Rulebook Section 4.4 and 5.5
4. Generate complete V15 package

---

## Part 7: V15 Package Contents

| File | Description |
|------|-------------|
| Combined_Database_FINAL_V15.xlsx | Source database (17,434 facilities) |
| Economic_Model_Scenario_1_Combined_V15.xlsx | Conservative growth calculations |
| Economic_Model_Scenario_2_Combined_V15.xlsx | Market expansion calculations |
| Economic_Model_Scenario_3_Combined_V15.xlsx | Premium services calculations |
| Comprehensive_Report_Workbook_V15.xlsx | Updated report with V15 rules |
| Final_Model_Rulebook_V15.md | Authoritative reference with updated rules |
| START_HERE_V15.md | Engagement workflow |
| Fee_Schedule_Reference_V15.xlsx | Fee lookup table |
| QC_Validation_Workbook_V15.xlsx | Validation checks |
| V14_to_V15_Change_Compendium.md | This document |

---

**END OF COMPENDIUM**

*This document serves as the authoritative record of all V14 → V15 changes.*
