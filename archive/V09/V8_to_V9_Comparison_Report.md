# V8.0 → V9.0 Comparison Report
## Eventus Healthcare Economic Model

**Date:** November 18, 2025  
**Previous Version:** V8.0 (November 17, 2025)  
**Current Version:** V9.0

---

## Executive Summary

Version 9.0 represents a **major revision** with three significant changes:
1. **Entity-Level Barrier Logic** - Barriers now apply to ALL facilities under a corporate entity
2. **New Barrier Entity** - Added Simcha Hyman & Naftali Zanziper (Alliance)
3. **Fee Schedule Update** - SNF PCP fee increased from $1,698.96 to $2,600.00

These changes result in a **20.9% increase** in Total Potential Revenue and a **1,420% increase** in facilities with barriers.

---

## Key Metric Changes

| Metric | V8.0 | V9.0 | Change | % Change |
|--------|------|------|--------|----------|
| Total Facilities | 17,434 | 17,434 | 0 | 0.0% |
| Facilities with Barriers | 68 | 1,034 | +966 | +1,420.6% |
| Current Revenue | $160,426,737 | $178,194,023 | +$17,767,286 | +11.1% |
| Integration Revenue | $164,643,771 | $189,669,230 | +$25,025,459 | +15.2% |
| New Business Revenue | $4,416,210,353 | $5,170,445,101 | +$754,234,748 | +17.1% |
| **Total Potential Revenue** | **$4,580,854,124** | **$5,538,308,355** | **+$957,454,231** | **+20.9%** |

---

## Change #1: Entity-Level Barrier Logic

### Previous Behavior (V8.0)
- Only individual facilities with barriers were excluded from New Business Revenue
- 68 facilities had barriers applied
- Large corporate entities appeared in Top 20 reports even with some barrier facilities

### New Behavior (V9.0)
- If ANY facility in a corporate entity has a barrier, ALL facilities under that entity are marked with barriers
- 1,034 facilities now have barriers (966 additional)
- 811 barrier facilities we don't serve have $0 revenue (excluded from market)
- 223 barrier facilities we do serve retain Current/Integration revenue

### Impact
- **Revenue excluded from market:** ~$397 million
- **Entities fully excluded from Top Corporate reports:** 21 (up from partial exclusions)

### Entity-Level Barrier Summary

| Corporate Entity | Barrier Type | Facilities | Census | Revenue Impact |
|-----------------|--------------|------------|--------|----------------|
| GENESIS HEALTHCARE | Own Provider Group | 215 | 17,847 | Excluded |
| SABER HEALTHCARE GROUP | Competitor Contract | 159 | 4,086 | Excluded |
| COMMUNICARE HEALTH | Own Provider Group | 122 | 10,260 | Excluded |
| SIMCHA HYMAN & NAFTALI ZANZIPER | Alliance | 115 | 1,489 | Excluded |
| INFINITY HEALTHCARE CONSULTING | Alliance | 107 | 2,219 | Excluded |
| SIGNATURE HEALTHCARE | Own Provider Group | 72 | 4,020 | Excluded |
| HILL VALLEY HEALTHCARE | Alliance | 40 | 2,558 | Excluded |
| CARDON & ASSOCIATES | Own Provider Group | 34 | 2,817 | Excluded |
| BRICKYARD HEALTHCARE | Competitor Contract | 23 | 636 | Excluded |
| VENZA CARE MANAGEMENT | Alliance | 18 | 1,298 | Excluded |
| JOURNEY HEALTHCARE | Alliance | 17 | 1,130 | Excluded |
| BLUEGRASS HEALTH KY | Alliance | 15 | 1,299 | Excluded |
| BHI SENIOR LIVING | Refuses Service | 14 | 804 | Excluded |
| COMMONWEALTH CARE OF ROANOKE | Competitor Contract | 13 | 799 | Excluded |
| EXCEPTIONAL LIVING CENTERS | Alliance | 13 | 936 | Excluded |
| AVENTURA HEALTH GROUP | Alliance | 12 | 322 | Excluded |
| ATRIUM HEALTH | Own Provider Group | 12 | 1,026 | Excluded |
| ENCORE HEALTH PARTNERS | Alliance | 12 | 606 | Excluded |
| CHOICE HEALTH MANAGEMENT | Alliance | 9 | 530 | Excluded |
| ALLIANCE HEALTH GROUP | Alliance | 6 | 437 | Excluded |
| MAJOR HOSPITAL | Own Provider Group | 6 | 336 | Excluded |
| **TOTAL** | | **1,034** | **55,455** | |

---

## Change #2: New Barrier Entity

### Added Entity
- **Corporate Name:** SIMCHA HYMAN & NAFTALI ZANZIPER
- **Barrier Type:** Alliance
- **Facilities Affected:** 115
- **Census:** 1,489
- **Geographic Distribution:** Multiple states

### Rationale
Entity identified as having an existing Alliance relationship that precludes Eventus services.

---

## Change #3: Fee Schedule Update

### SNF PCP Fee Change
| | V8.0 | V9.0 | Change |
|---|------|------|--------|
| SNF PCP Monthly Fee | $1,698.96 | $2,600.00 | +$901.04 (+53.0%) |

### Revenue Per Patient Impact

| Facility Type | V8.0 | V9.0 | Change |
|---------------|------|------|--------|
| SNF | $3,410.94 | $4,311.98 | +$901.04 (+26.4%) |
| ALF | $3,781.32 | $3,781.32 | $0 (unchanged) |

### Scenario Fee Structures

**Scenario 1 (Conservative Growth):**
- SNF: PCP $2,600 | MH $1,623.96 | CCM $360 | SS $4,800
- ALF: PCP $1,951.32 | MH $1,860 | CCM $360 | SS $4,800

**Scenario 2 (Market Expansion - 10% increase):**
- SNF: PCP $2,860 | MH $1,786.36 | CCM $396 | SS $5,280
- ALF: PCP $2,146.45 | MH $2,046 | CCM $396 | SS $5,280

**Scenario 3 (Premium Services - 20% increase):**
- SNF: PCP $3,120 | MH $1,948.75 | CCM $432 | SS $5,760
- ALF: PCP $2,341.58 | MH $2,232 | CCM $432 | SS $5,760

---

## TAM/SAM/SOM Impact

### TAM (Total Addressable Market)
| Metric | V8.0 | V9.0 | Change |
|--------|------|------|--------|
| Facilities | 17,434 | 17,434 | 0 |
| Total Potential | $4,580,854,124 | $5,538,308,355 | +20.9% |

### SAM (Serviceable Available Market - Existing States)
| Metric | V8.0 | V9.0 | Change |
|--------|------|------|--------|
| Facilities | 5,277 | 5,277 | 0 |
| Total Potential | (calculated) | (calculated) | Fee impact |

### SOM (Serviceable Obtainable Market - Existing States, No Barriers)
| Metric | V8.0 | V9.0 | Change |
|--------|------|------|--------|
| Facilities | ~5,200 | 4,701 | -~500 |
| Corporate Entities | ~950 | 939 | -11 |

The SOM reduction reflects entity-level barrier exclusions removing 576 additional facilities from the obtainable market in existing states.

---

## Validation Results

### Revenue Validation Check
- **Status:** PASSED
- **Facilities with $0 in all revenue columns:** 811
- **Explanation:** All 811 are barrier facilities we don't serve (expected behavior)
- **Non-barrier facilities with issues:** 0

### Data Integrity
- All facilities have at least one non-zero revenue value (or are expected $0 due to barriers)
- Census values validated
- State distributions verified

---

## Files Updated

### Source Database
- Combined_Database_FINAL_V9.xlsx (barrier column propagated to all entity facilities)

### Scenario Files
- Economic_Model_Scenario_1_Combined_V9.xlsx
- Economic_Model_Scenario_2_Combined_V9.xlsx
- Economic_Model_Scenario_3_Combined_V9.xlsx

### Reference Documents
- Fee_Schedule_Reference_V9.xlsx
- Comprehensive_Report_Workbook_V9.xlsx
- State_Summary_QC_Workbook_V9.xlsx
- Final_Model_Rulebook_V9.md

---

## Business Implications

### Positive Impacts
1. **Revenue increase** - 20.9% increase in Total Potential Revenue due to fee adjustment
2. **More accurate barrier handling** - Entity-level exclusions reflect real-world business relationships
3. **Cleaner Top Corporate reports** - No partial inclusions of barrier entities

### Considerations
1. **Reduced SOM** - 576 fewer facilities in obtainable market due to entity-level barriers
2. **811 facilities with $0 revenue** - These are permanently excluded from market opportunity
3. **Top Corporate rankings changed** - New leaders due to barrier entity removal

---

## Recommendations for Next Steps

1. **Review Top 20/60 Corporate Reports** - Verify new leaders are accurate targets
2. **Validate barrier entity list** - Confirm all 21 entities should be fully excluded
3. **Consider barrier removal process** - Some entities may become available if relationships change
4. **Monitor fee schedule impact** - Track actual vs. projected revenue at new rates

---

**Report Generated:** November 18, 2025  
**Author:** Claude (AI Assistant)  
**Version:** V9.0
