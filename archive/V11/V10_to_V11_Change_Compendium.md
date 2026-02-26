# V10 → V11 Change Compendium
## Eventus Healthcare Economic Model - Integrated Barrier Propagation

**Date**: November 18, 2025  
**Previous Version**: V10.0  
**Current Version**: V11.0  
**Author**: Claude (AI Assistant)

---

## Executive Summary

Version 11.0 implements a comprehensive Integrated Barrier system that extends facility-level operational barriers to the corporate level. This represents a significant enhancement to the revenue model's accuracy by accounting for systemic barriers that affect entire corporate entities.

### Key Changes

1. **Corporate Barrier Propagation**: Extended 110 facility-specific barriers to all 786 facilities under 32 parent companies
2. **CCH Healthcare Exception**: Ohio-only barrier rule (20 facilities) while NC facilities (20) remain unaffected
3. **Calculation Rule Implementation**: Integrated Barriers block all potential revenue while preserving current revenue

### Impact Summary

| Metric | V10 | V11 | Change |
|--------|-----|-----|--------|
| Facilities with Integrated Barriers | 110 | 786 | +676 |
| Served Census Affected | 5,542 | 17,093 | +11,551 |
| Not Served Census Affected | 122 | 45,264 | +45,142 |

---

## Part 1: Source Data Origin

### Book1.xlsx - Pull-Through Barrier Data

The Integrated Barrier data originated from operational pull-through tracking sheets:

| Sheet | Total Facilities | With Barriers |
|-------|------------------|---------------|
| ALF MH PullThru | 91 | 2 |
| ALF PCP PullThru | 127 | 14 |
| SNF PCP PullThru | 314 | 87 |
| SNF MH PullThru | 90 | 8 |
| **Total** | **622** | **111** |

Note: 111 source entries resulted in 110 database entries (1 duplicate skipped).

---

## Part 2: Barrier Category Definitions

### Six Standardized Categories

| Category | Definition | Business Impact |
|----------|------------|-----------------|
| **Alliance** | Existing alliance or partnership relationships that limit service opportunities | Cannot pursue additional services due to exclusivity arrangements |
| **MH Only Opportunity** | Facilities where only Mental Health services can be pursued | PCP expansion permanently blocked; already have MH services |
| **Competitor Agreement** | Specific contractual relationships with competing service providers | Bound by contracts with Bowen, Curana, Venza, T4, etc. |
| **Own Provider Group** | Facility has or is developing internal provider capabilities | Moving services in-house; displacement risk |
| **Reputation** | Past service issues or reputation concerns affecting the relationship | Must rebuild trust before expansion possible |
| **Termination Risk** | Recent termination or elevated risk of service termination | Relationship at risk; expansion inappropriate |

### Combined Categories

When a parent company has facilities with multiple barrier types, categories are combined:

- **Alliance, Own Provider Group** (113 facilities)
- **Alliance, MH Only Opportunity** (19 facilities)

---

## Part 3: Propagation Methodology

### Core Rule

**All facilities under a parent company with ANY barrier-flagged facility receive the barrier designation.**

Rationale: Operational barriers identified at specific facilities typically reflect corporate-level constraints (contracts, ownership decisions, reputation) that apply to all facilities under that entity.

### Propagation Logic

```
FOR each Parent Company with barrier facilities:
    GET all unique barrier categories for that parent
    COMBINE categories into single text field
    APPLY combined category to ALL facilities under parent
    SET detail to "Propagated from: [original details]"
```

### Exception: CCH HEALTHCARE

**Special Rule**: State-specific barrier application

| State | Facilities | Barrier Applied | Reason |
|-------|------------|-----------------|--------|
| Ohio | 20 | Reputation | Original barrier note "reputation in Oh?" indicates state-specific issue |
| North Carolina | 20 | None | No reputation concerns in NC market |

This exception was explicitly authorized due to the state-specific nature of the reputation issue.

---

## Part 4: Calculation Rules

### Revenue Impact by Facility Status

#### Served Facilities (Do_We_Serve = Yes)

| Revenue Type | Without Barrier | With Integrated Barrier |
|--------------|-----------------|-------------------------|
| Current Revenue | Census × Fee | Census × Fee (UNCHANGED) |
| Integration Revenue | Census × (Missing Services) | **$0** |
| New Business Revenue | $0 | $0 |
| Total Potential | Integration Revenue | **$0** |

#### Not Served Facilities (Do_We_Serve = No)

| Revenue Type | Without Barrier | With Integrated Barrier |
|--------------|-----------------|-------------------------|
| Current Revenue | $0 | $0 |
| Integration Revenue | $0 | $0 |
| New Business Revenue | Census × TOTAL | **$0** |
| Total Potential | New Business Revenue | **$0** |

### Key Principle

**Integrated Barriers block POTENTIAL revenue only.**

- Current Revenue: Represents actual existing business - NEVER blocked
- Integration Revenue: Opportunity to expand services - BLOCKED by barrier
- New Business Revenue: Opportunity for new facilities - BLOCKED by barrier
- Total Potential: Sum of opportunities - BLOCKED by barrier

### MH Only Opportunity - Special Note

Despite the name suggesting partial opportunity, this category functions identically to all other barriers:

- These facilities already have MH services (reflected in Current Revenue)
- PCP expansion is permanently blocked
- CCM and SS require PCP, so they are also blocked
- Result: Integration Revenue = $0 (same as other barriers)

---

## Part 5: Complete Propagation Log

### Summary by Parent Company

| Parent Company | Original | Added | Final | Combined Categories |
|----------------|----------|-------|-------|---------------------|
| COMMUNICARE HEALTH | 1 | 121 | 122 | Own Provider Group |
| SIMCHA HYMAN & NAFTALI ZANZIPER | 2 | 113 | 115 | Alliance, Own Provider Group |
| SIGNATURE HEALTHCARE | 1 | 71 | 72 | MH Only Opportunity |
| ALG | 8 | 57 | 65 | Competitor Agreement |
| LIFEWORKS REHAB | 5 | 46 | 51 | Alliance |
| EMBASSY HEALTHCARE | 1 | 40 | 41 | Reputation |
| HILL VALLEY HEALTHCARE | 1 | 39 | 40 | MH Only Opportunity |
| CARDON & ASSOCIATES | 4 | 30 | 34 | Own Provider Group |
| EASTERN HEALTHCARE GROUP | 3 | 20 | 23 | Termination Risk |
| CCH HEALTHCARE | 1 | 19 | 20 | Reputation (Ohio only) |
| BLUEGRASS HEALTH KY | 2 | 13 | 15 | Alliance, MH Only Opportunity |
| COMMONWEALTH CARE OF ROANOKE | 2 | 11 | 13 | Competitor Agreement |
| PRINCIPLE | 3 | 10 | 13 | Competitor Agreement |
| DAVID MARX | 1 | 9 | 10 | Competitor Agreement |
| ATRIUM HEALTH | 3 | 9 | 12 | Own Provider Group |
| MFA | 3 | 9 | 12 | Alliance |
| SUNRISE SENIOR LIVING | 2 | 9 | 11 | Competitor Agreement |
| BHI SENIOR LIVING | 6 | 8 | 14 | Reputation |
| JAG HEALTHCARE | 1 | 8 | 9 | Reputation |
| BLUEGRASS/ENCORE | 22 | 6 | 28 | Alliance, MH Only Opportunity |
| COMMUNICARE | 7 | 5 | 12 | Own Provider Group |
| AVENTURA | 1 | 5 | 6 | Termination Risk |
| SIGNATURE HEALTH | 10 | 4 | 14 | MH Only Opportunity |
| NURSING CARE MANAGEMENT OF AMERICA | 1 | 4 | 5 | Reputation |
| HILL VALLEY | 2 | 4 | 6 | MH Only Opportunity |
| CLEARVIEW | 3 | 3 | 6 | Alliance |
| YAD | 4 | 1 | 5 | Reputation |
| JAG | 2 | 1 | 3 | Reputation |
| COMMONWEALTH SENIOR LIVING | 1 | 1 | 2 | Competitor Agreement |
| BRIGHTON | 5 | 0 | 5 | MH Only Opportunity |
| NEWPORT AL HOLDINGS, LLC | 1 | 0 | 1 | Competitor Agreement |
| IVY MANAGEMENT GROUP | 1 | 0 | 1 | MH Only Opportunity |

**Total**: 110 original + 676 propagated = **786 facilities**

---

## Part 6: Category Distribution After Propagation

| Category | Facilities | Census | % of Barrier Census |
|----------|------------|--------|---------------------|
| Own Provider Group | 181 | 16,209 | 26.0% |
| MH Only Opportunity | 145 | 12,487 | 20.0% |
| Competitor Agreement | 115 | 5,903 | 9.5% |
| Alliance, Own Provider Group | 113 | 9,906 | 15.9% |
| Reputation | 97 | 5,734 | 9.2% |
| Alliance | 87 | 8,297 | 13.3% |
| Termination Risk | 29 | 2,423 | 3.9% |
| Alliance, MH Only Opportunity | 19 | 1,399 | 2.2% |
| **TOTAL** | **786** | **62,358** | **100%** |

---

## Part 7: Revenue Impact Analysis

### By Source Type

| Source Type | Facilities | Census | 
|-------------|------------|--------|
| SNF | 562 | 51,898 |
| ALF | 224 | 10,460 |

### By Service Status

| Status | Facilities | Census | Revenue Blocked |
|--------|------------|--------|-----------------|
| Served (Yes) | 306 | 17,093 | Integration Revenue |
| Not Served (No) | 480 | 45,264 | New Business Revenue |

### Percentage of Total Market

| Metric | Barrier Census | Total Census | Percentage |
|--------|----------------|--------------|------------|
| Served Market | 17,093 | 91,034 | **18.8%** |
| Unserved Market | 45,264 | 1,286,744 | **3.5%** |

---

## Part 8: Two Barrier Systems - Important Distinction

The model now contains TWO complementary barrier systems:

### Corporate Barrier (Column 16)

- **Scope**: Entire corporate entities
- **Source**: Strategic exclusions list
- **Entities**: 21 corporate groups
- **Facilities**: 1,034
- **Effect**: Blocks New Business Revenue for Not Served facilities

### Integrated Barrier (Columns 20-21)

- **Scope**: Originally facility-level, now propagated to corporate
- **Source**: Pull-through operational tracking
- **Entities**: 32 parent companies
- **Facilities**: 786
- **Effect**: Blocks ALL potential revenue (Integration + New Business)

### Overlap Analysis

Some facilities may have BOTH barriers. The Integrated Barrier is more restrictive (blocks Integration Revenue for Served facilities), so it takes precedence in calculations.

---

## Part 9: Files Generated

### Database
- **Combined_Database_FINAL_V11.xlsx** - Updated with propagated barriers

### Logs & Documentation
- **V11_Propagation_Changes_Log.xlsx** - Detailed log of all 676 propagated barriers
- **V10_to_V11_Change_Compendium.md** - This document

### To Be Generated
- Economic_Model_Scenario_1_Combined_V11.xlsx
- Economic_Model_Scenario_2_Combined_V11.xlsx
- Economic_Model_Scenario_3_Combined_V11.xlsx
- Final_Model_Rulebook_V11.md
- QC_Validation_Workbook_V11.xlsx
- Comprehensive_Report_Workbook_V11.xlsx
- Fee_Schedule_Reference_V11.xlsx
- START_HERE_V11.md

---

## Part 10: Governance & Audit Trail

### Authorization Record

- **Change Requested**: November 18, 2025
- **Requestor**: User (project owner)
- **Authorization Type**: Verbal/written in conversation
- **Key Decisions Authorized**:
  1. Corporate propagation of all integrated barriers
  2. CCH Healthcare Ohio-only exception
  3. Combined text for multiple categories
  4. Calculation rules (block potential, preserve current)

### Version Control

- V10 files preserved (never overwritten)
- V11 files created fresh with full documentation
- Change logs generated for complete audit trail

### QC Requirements

Before delivery, verify:
- [ ] All barrier categories propagated correctly
- [ ] CCH Ohio = 20 barriers, CCH NC = 0 barriers
- [ ] Revenue calculations reflect barrier rules
- [ ] Documentation complete and accurate

---

## Part 11: Future Considerations

### Periodic Refresh

Integrated Barrier data reflects conditions at time of Book1.xlsx export. Consider:
- Quarterly refresh of pull-through barrier data
- Re-evaluation of propagation rules
- Update of CCH or other exception rules

### Additional Exceptions

The CCH Healthcare Ohio-only rule establishes a precedent for state-specific or regional barrier applications. Future exceptions should be:
- Explicitly authorized
- Documented in this compendium
- Implemented with clear audit trail

### Category Evolution

As business conditions change, barrier categories may need:
- New categories added
- Existing categories redefined
- Different calculation impacts (if partial opportunities emerge)

---

**END OF COMPENDIUM**

*This document serves as the authoritative record of all V10 → V11 changes related to Integrated Barrier propagation.*
