# Final Model Rulebook V11.0
## Healthcare Facility Database Revenue Model - Authoritative Reference

**Version**: 11.0  
**Date**: November 18, 2025  
**Status**: PRODUCTION READY

---

## Executive Summary

This rulebook defines the authoritative fee structures, calculation methodologies, barrier systems, and governance controls for the Eventus Healthcare Economic Model. All revenue calculations must conform to the specifications in this document.

**V11.0 ENHANCEMENT**: This version implements corporate-level Integrated Barrier propagation. Facility-specific operational barriers from pull-through tracking have been extended to all facilities under each affected parent company. This significantly impacts potential revenue calculations by blocking Integration and New Business Revenue for 786 facilities.

---

## 1. Fee Structure - AUTHORITATIVE VALUES

### 1.1 SNF (Skilled Nursing Facility) Fees

| Scenario | PCP | MH (adj) | CCM (adj) | SS (adj) | TOTAL |
|----------|-----|----------|-----------|----------|-------|
| S1 Conservative | $2,600.00 | $811.98 | $108.00 | $792.00 | **$4,311.98** |
| S2 Market (+10%) | $2,860.00 | $893.18 | $118.80 | $871.20 | **$4,743.18** |
| S3 Premium (+20%) | $3,120.00 | $974.38 | $129.60 | $950.40 | **$5,174.38** |

### 1.2 ALF (Assisted Living Facility) Fees

| Scenario | PCP | MH (adj) | CCM (adj) | SS (adj) | TOTAL |
|----------|-----|----------|-----------|----------|-------|
| S1 Conservative | $1,875.00 | $949.00 | $108.00 | $792.00 | **$3,724.00** |
| S2 Market (+10%) | $2,062.50 | $1,043.90 | $118.80 | $871.20 | **$4,096.40** |
| S3 Premium (+20%) | $2,250.00 | $1,138.80 | $129.60 | $950.40 | **$4,468.80** |

### 1.3 Permanent Adjusters

| Service | Adjuster | Formula |
|---------|----------|---------|
| MH | 0.50 | Base MH × 0.50 |
| CCM | 0.30 | Base CCM × 0.30 |
| Shared Savings | 0.165 | Base SS × 0.50 × 0.33 |

---

## 2. Revenue Calculations

### 2.1 Current Revenue

**Definition**: Revenue from existing services at facilities we currently serve.

| Service Configuration | Formula |
|----------------------|---------|
| Integrated | Census × TOTAL |
| MH Only | Census × MH (adjusted) |
| PCP Only | Census × PCP |

**Note**: Current Revenue is NEVER affected by barriers.

### 2.2 Integration Revenue

**Definition**: Revenue opportunity from adding missing services to existing facilities.

| Service Configuration | Formula | With Integrated Barrier |
|----------------------|---------|------------------------|
| MH Only | Census × (PCP + CCM + SS) | **$0** |
| PCP Only | Census × (MH + CCM + SS) | **$0** |
| Integrated | $0 | $0 |

### 2.3 New Business Revenue

**Definition**: Revenue opportunity from facilities we don't currently serve.

| Condition | Formula |
|-----------|---------|
| Not Served, No Corporate Barrier, No Integrated Barrier | Census × TOTAL |
| Not Served, Has Corporate Barrier | **$0** |
| Not Served, Has Integrated Barrier | **$0** |
| Served | $0 |

### 2.4 Total Potential Revenue

**Formula**: Integration Revenue + New Business Revenue

**Note**: Does NOT include Current Revenue. Represents incremental opportunity only.

---

## 3. Barrier Systems

### 3.1 Two Complementary Barrier Systems

The model employs TWO distinct barrier systems that work together:

| System | Column | Level | Facilities | Primary Effect |
|--------|--------|-------|------------|----------------|
| Corporate Barrier | 16 (Barrier) | Corporate Entity | 1,034 | Blocks New Business |
| Integrated Barrier | 20-21 | Facility/Corporate | 786 | Blocks ALL Potential |

### 3.2 Corporate Barrier (Original System)

**Purpose**: Strategic exclusions of entire corporate entities from New Business pursuit.

**Effect**: Blocks New Business Revenue only (Not Served facilities = $0)

**Entities**: 21 corporate groups (see Section 6)

### 3.3 Integrated Barrier System (V11 Enhancement)

**Purpose**: Operational barriers identified through pull-through tracking, propagated to corporate level.

**Effect**: Blocks ALL potential revenue:
- Integration Revenue = $0
- New Business Revenue = $0
- Total Potential Revenue = $0
- Current Revenue = UNCHANGED

#### 3.3.1 Barrier Categories

| Category | Facilities | Definition |
|----------|------------|------------|
| Own Provider Group | 181 | Facility developing internal provider capabilities |
| MH Only Opportunity | 145 | Only Mental Health can be pursued; PCP blocked |
| Competitor Agreement | 115 | Contractual relationship with competitor |
| Alliance, Own Provider Group | 113 | Combined barriers from parent company |
| Reputation | 97 | Past service issues affecting relationship |
| Alliance | 87 | Partnership limiting service opportunities |
| Termination Risk | 29 | Recent or pending termination |
| Alliance, MH Only Opportunity | 19 | Combined barriers from parent company |

#### 3.3.2 Propagation Rules

**Core Rule**: All facilities under a parent company with ANY barrier-flagged facility receive the barrier designation.

**Rationale**: Operational barriers typically reflect corporate-level constraints that apply to all facilities under that entity.

**Combined Categories**: When a parent has multiple barrier types, they are combined into single text (e.g., "Alliance, MH Only Opportunity").

#### 3.3.3 CCH HEALTHCARE Exception

**Special Rule**: State-specific barrier application

| State | Facilities | Barrier | Reason |
|-------|------------|---------|--------|
| Ohio | 20 | Reputation | State-specific reputation issue |
| North Carolina | 20 | None | No concerns in NC market |

This exception was explicitly authorized due to the localized nature of the reputation issue.

#### 3.3.4 Integrated Barrier Calculation Impact

**For Served Facilities (Do_We_Serve = Yes):**

| Revenue Type | Without Barrier | With Integrated Barrier |
|--------------|-----------------|-------------------------|
| Current Revenue | Calculated normally | Calculated normally |
| Integration Revenue | Calculated normally | **$0** |

**For Not Served Facilities (Do_We_Serve = No):**

| Revenue Type | Without Barrier | With Integrated Barrier |
|--------------|-----------------|-------------------------|
| New Business Revenue | Census × TOTAL | **$0** |

### 3.4 Barrier Overlap Handling

When a facility has BOTH Corporate Barrier AND Integrated Barrier:
- The Integrated Barrier takes precedence (more restrictive)
- For Served facilities: Integration Revenue = $0
- For Not Served facilities: Both systems already block New Business

---

## 4. V11.0 Key Metrics

| Metric | Scenario 1 | Scenario 2 | Scenario 3 |
|--------|------------|------------|------------|
| Current Revenue | $177,684,185 | $195,452,682 | $213,221,179 |
| Integration Revenue | $147,384,026 | $162,122,438 | $176,860,849 |
| New Business Revenue | $5,115,910,599 | $5,627,503,884 | $6,139,097,168 |
| **Total Potential** | **$5,263,294,625** | **$5,789,626,321** | **$6,315,958,018** |

### Integrated Barrier Impact

| Revenue Type | V10 (S1) | V11 (S1) | Blocked | % Blocked |
|--------------|----------|----------|---------|-----------|
| Integration | $187,688,338 | $147,384,026 | $40,304,312 | 21.5% |
| New Business | $5,165,524,753 | $5,115,910,599 | $49,614,154 | 1.0% |
| **Total Potential** | **$5,353,213,091** | **$5,263,294,625** | **$89,918,466** | **1.7%** |

*Note: Current Revenue slightly higher than V10 due to source data update (1 SNF facility with both PCP+MH flags).*

### V11 Validation Points

| Check | Expected Value |
|-------|----------------|
| Total Facilities | 17,434 |
| Corporate Barrier Facilities | 1,034 |
| Integrated Barrier Facilities | 786 |
| Served with Integrated Barrier | 306 |
| Not Served with Integrated Barrier | 480 |

### Baseline Comparison

| Metric | V10 | V11 | Change |
|--------|-----|-----|--------|
| ALF Current Revenue | $83,991,652 | $83,991,652 | None (unaffected) |
| SNF Current Revenue | $93,517,883 | $93,517,883 | None (unaffected) |
| Integrated Barrier Facilities | 110 | 786 | +676 (propagation) |

---

## 5. Market Definitions

### Geographic Markets

| Market | States |
|--------|--------|
| Existing | IN, KY, NC, OH, SC, VA |
| Priority Expansion | IA, MN, IL, MI, PA, WI, MT |
| Emerging | FL, GA |
| Exiting | WV |
| National | All others |

### Market Segments

| Segment | Definition | Facilities |
|---------|------------|------------|
| TAM | All facilities | 17,434 |
| SAM | Existing states | 5,277 |
| SOM | Existing states, no barriers | Reduced by Integrated Barriers |

---

## 6. Corporate Barrier Entities (21 Total)

Corporate entities fully excluded from New Business:

1. GENESIS HEALTHCARE (215)
2. SABER HEALTHCARE GROUP (159)
3. COMMUNICARE HEALTH (122)
4. SIMCHA HYMAN & NAFTALI ZANZIPER (115)
5. INFINITY HEALTHCARE CONSULTING (107)
6. SIGNATURE HEALTHCARE (72)
7. HILL VALLEY HEALTHCARE (40)
8. CARDON & ASSOCIATES (34)
9. BRICKYARD HEALTHCARE (23)
10. VENZA CARE MANAGEMENT (18)
11. JOURNEY HEALTHCARE (17)
12. BLUEGRASS HEALTH KY (15)
13. BHI SENIOR LIVING (14)
14. COMMONWEALTH CARE OF ROANOKE (13)
15. EXCEPTIONAL LIVING CENTERS (13)
16. AVENTURA HEALTH GROUP (12)
17. ATRIUM HEALTH (12)
18. ENCORE HEALTH PARTNERS (12)
19. CHOICE HEALTH MANAGEMENT (9)
20. ALLIANCE HEALTH GROUP (6)
21. MAJOR HOSPITAL (6)

**Total**: 1,034 facilities with Corporate Barriers

---

## 7. Integrated Barrier Entities (32 Total)

Parent companies with propagated Integrated Barriers:

| # | Parent Company | Facilities | Categories |
|---|----------------|------------|------------|
| 1 | COMMUNICARE HEALTH | 122 | Own Provider Group |
| 2 | SIMCHA HYMAN & NAFTALI ZANZIPER | 115 | Alliance, Own Provider Group |
| 3 | SIGNATURE HEALTHCARE | 72 | MH Only Opportunity |
| 4 | ALG | 65 | Competitor Agreement |
| 5 | LIFEWORKS REHAB | 51 | Alliance |
| 6 | EMBASSY HEALTHCARE | 41 | Reputation |
| 7 | HILL VALLEY HEALTHCARE | 40 | MH Only Opportunity |
| 8 | CARDON & ASSOCIATES | 34 | Own Provider Group |
| 9 | BLUEGRASS/ENCORE | 28 | Alliance, MH Only Opportunity |
| 10 | EASTERN HEALTHCARE GROUP | 23 | Termination Risk |
| 11 | CCH HEALTHCARE | 20 | Reputation (Ohio only) |
| 12 | BLUEGRASS HEALTH KY | 15 | Alliance, MH Only Opportunity |
| 13 | BHI SENIOR LIVING | 14 | Reputation |
| 14 | SIGNATURE HEALTH | 14 | MH Only Opportunity |
| 15 | COMMONWEALTH CARE OF ROANOKE | 13 | Competitor Agreement |
| 16 | PRINCIPLE | 13 | Competitor Agreement |
| 17 | ATRIUM HEALTH | 12 | Own Provider Group |
| 18 | COMMUNICARE | 12 | Own Provider Group |
| 19 | MFA | 12 | Alliance |
| 20 | SUNRISE SENIOR LIVING | 11 | Competitor Agreement |
| 21 | DAVID MARX | 10 | Competitor Agreement |
| 22 | JAG HEALTHCARE | 9 | Reputation |
| 23 | AVENTURA | 6 | Termination Risk |
| 24 | CLEARVIEW | 6 | Alliance |
| 25 | HILL VALLEY | 6 | MH Only Opportunity |
| 26 | BRIGHTON | 5 | MH Only Opportunity |
| 27 | NURSING CARE MANAGEMENT OF AMERICA | 5 | Reputation |
| 28 | YAD | 5 | Reputation |
| 29 | JAG | 3 | Reputation |
| 30 | COMMONWEALTH SENIOR LIVING | 2 | Competitor Agreement |
| 31 | IVY MANAGEMENT GROUP | 1 | MH Only Opportunity |
| 32 | NEWPORT AL HOLDINGS, LLC | 1 | Competitor Agreement |

**Total**: 786 facilities with Integrated Barriers

---

## 8. Governance Controls

### 8.1 Fee Change Management

**MANDATORY for any fee modification:**

1. **Written Authorization** - Explicit approval from project owner required
2. **Impact Analysis** - Calculate full impact before implementation
3. **Documentation** - Update rulebook and comparison report
4. **Validation** - Run QC Validation Workbook to verify

### 8.2 Barrier Change Management

**MANDATORY for barrier modifications:**

1. **Written Authorization** - Required for adding/removing barriers
2. **Propagation Review** - Consider corporate-level impact
3. **Exception Documentation** - Document any state/regional exceptions
4. **Audit Trail** - Log all changes in compendium

### 8.3 Version Control Protocol

**Numbering Rules:**
- Minor fixes: V11.0 → V11.1 → V11.2
- Major changes: V11.x → V12.0
- **Never reuse version numbers**
- **Never overwrite files - always increment**

**File Naming:**
```
Economic_Model_Scenario_1_Combined_V11.xlsx
QC_Validation_Workbook_V11.xlsx
Final_Model_Rulebook_V11.md
```

### 8.4 QC Validation Requirements

**Run QC_Validation_Workbook after EVERY major step:**

1. **Fee Structure Validation**
   - All fees must show PASS status
   - Revenue per patient matches expected

2. **Baseline Comparison**
   - ALF Current = $83,991,652
   - SNF Current = $93,517,883
   - No unexpected variations >1%

3. **Barrier Validation**
   - Corporate Barrier facilities = 1,034
   - Integrated Barrier facilities = 786
   - CCH Ohio = 20, CCH NC = 0

4. **Financial Reconciliation**
   - Total facilities = 17,434
   - All totals match expected

### 8.5 Capacity Monitoring

**For long conversations:**
- Check remaining capacity every 3-4 tool calls
- Report capacity status periodically
- Plan work to complete within available space
- Save critical outputs before capacity runs low

---

## 9. File Dependencies

### Source
- Combined_Database_FINAL_V11.xlsx

### Outputs
- Economic_Model_Scenario_[1-3]_Combined_V11.xlsx
- QC_Validation_Workbook_V11.xlsx
- Comprehensive_Report_Workbook_V11.xlsx
- Fee_Schedule_Reference_V11.xlsx

### Documentation
- Final_Model_Rulebook_V11.md
- START_HERE_V11.md
- V10_to_V11_Change_Compendium.md

---

## 10. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| **V11.0** | Nov 18, 2025 | Integrated Barrier propagation (786 facilities), CCH Ohio exception |
| V10.0 | Nov 2025 | ALF fees corrected, QC validation added |
| V9.0 | Nov 2025 | Entity barriers, SNF PCP $2,600 (ALF fees incorrect) |
| V8.0 | Nov 2025 | Baseline version |

---

## 11. Prohibited Actions

**NEVER do without explicit authorization:**

- Modify fee values
- Change adjusters
- Alter formulas
- Add or remove barrier entities
- Modify propagation rules
- Create barrier exceptions
- Skip QC validation
- Deliver without verification
- Reuse version numbers

---

**END OF RULEBOOK**

*This document is the authoritative reference for the Eventus Healthcare Economic Model. All deviations require explicit written authorization and must be documented in the change compendium.*
