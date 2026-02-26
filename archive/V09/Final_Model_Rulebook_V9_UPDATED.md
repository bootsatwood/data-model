# Final Model Rulebook V9.0
## Eventus Economic Model - Three Scenario Specification
### Complete Formula Documentation | Census-Based Calculations | Entity-Level Barriers

**Document Purpose:** This rulebook provides the complete technical specification for the Eventus Economic Model V9.0 with entity-level barrier logic and updated fee structure.

**Model Version:** 9.0 - Entity-Level Barriers + Fee Update  
**Rulebook Version:** V9.0 (Updated)  
**Date:** November 18, 2025  
**Status:** PRODUCTION READY  
**Architecture:** Three-File System (Source + Model + Reports)

---

## V9.0 CRITICAL UPDATES

### Update #1: Entity-Level Barrier Logic

**Previous Behavior (V8.0 - Facility-Level):**
- Only individual facilities with barriers were excluded
- Large entities still appeared in Top 20 with most facilities included

**Current Behavior (V9.0 - Entity-Level):**
- If ANY facility in a corporate entity has a barrier, ALL facilities under that entity are marked with barriers
- Entire corporate entities excluded from market opportunity

**Impact:**
- Facilities with barriers: 68 → 1,034 (+1,420%)
- Barrier entities: 20 → 21 (added Simcha Hyman & Naftali Zanziper)
- Revenue excluded from market: ~$397 million
- SOM facilities reduced by 576 in existing market

### Update #2: SNF PCP Fee Increase

| Fee | V8.0 | V9.0 | Change |
|-----|------|------|--------|
| SNF PCP | $1,698.96 | $2,600.00 | +53.0% |

**Revenue Per Patient Impact:**
- SNF: $3,410.94 → $4,311.98 (+26.4%)
- ALF: $3,781.32 → $3,781.32 (unchanged)

### Update #3: New Barrier Entity

Added **SIMCHA HYMAN & NAFTALI ZANZIPER** with barrier type "Alliance" (115 facilities)

---

## TABLE OF CONTENTS

**PART 0: COMPREHENSIVE REPORT WORKBOOK STRUCTURE**
**PART 1: EXECUTIVE SUMMARY**
**PART 2: FEE STRUCTURE & ADJUSTERS**
**PART 3: BARRIER MANAGEMENT**
**PART 4: REVENUE CALCULATIONS**
**PART 5: MARKET SEGMENTATION**
**PART 6: SCENARIO SPECIFICATIONS**
**APPENDICES**

---

# PART 0: COMPREHENSIVE REPORT WORKBOOK STRUCTURE

## 0.1 Sheet and Table Inventory

The Comprehensive Report Workbook contains 5 sheets with 25 tables:

| Sheet | Sheet Name | Tables | Data Source |
|-------|------------|--------|-------------|
| 1 | TAM SAM SOM Facilities | 1-3 | Scenario 1 (facility counts don't vary) |
| 2 | TAM SAM SOM Revenue | 4-9 | Tables 4-6: S1 exact; Tables 7-9: S1-S3 ranges |
| 3 | Fee Structure SOM | 10-15 | Tables 10-12: S1 exact; Tables 13-15: S1-S3 ranges |
| 4 | Top Corporate Rankings | 16-18, 25 | Scenario 1 |
| 5 | State Analysis | 19-24 | Tables 19-21: S1 exact; Tables 22-24: S1-S3 ranges |

## 0.2 Complete Table Reference

| Table | Name | Sheet | Content |
|-------|------|-------|---------|
| 1 | SNF Facilities | 1 | TAM/SAM/SOM facility counts by ownership |
| 2 | ALF Facilities | 1 | TAM/SAM/SOM facility counts by ownership |
| 3 | Total Facilities | 1 | TAM/SAM/SOM facility counts by ownership |
| 4 | SNF Revenue | 2 | TAM/SAM/SOM revenue (exact values) |
| 5 | ALF Revenue | 2 | TAM/SAM/SOM revenue (exact values) |
| 6 | Total Revenue | 2 | TAM/SAM/SOM revenue (exact values) |
| 7 | SNF Revenue (Ranges) | 2 | TAM/SAM/SOM revenue (S1-S3 ranges) |
| 8 | ALF Revenue (Ranges) | 2 | TAM/SAM/SOM revenue (S1-S3 ranges) |
| 9 | Total Revenue (Ranges) | 2 | TAM/SAM/SOM revenue (S1-S3 ranges) |
| 10 | SNF | 3 | Fee structure SOM (exact values) |
| 11 | ALF | 3 | Fee structure SOM (exact values) |
| 12 | Total | 3 | Fee structure SOM (exact values) |
| 13 | SNF (Ranges) | 3 | Fee structure SOM (S1-S3 ranges) |
| 14 | ALF (Ranges) | 3 | Fee structure SOM (S1-S3 ranges) |
| 15 | Total (Ranges) | 3 | Fee structure SOM (S1-S3 ranges) |
| 16 | Top 20 Corporate - Total | 4 | Ranked by Total Opportunity |
| 17 | Top 20 Corporate - Integration | 4 | Ranked by Integration Opportunity |
| 18 | Top 20 Corporate - New Biz | 4 | Ranked by New Business Opportunity |
| 19 | SNF | 5 | State analysis (exact values) |
| 20 | ALF | 5 | State analysis (exact values) |
| 21 | Total | 5 | State analysis (exact values) |
| 22 | SNF (Ranges) | 5 | State analysis (S1-S3 ranges) |
| 23 | ALF (Ranges) | 5 | State analysis (S1-S3 ranges) |
| 24 | Total (Ranges) | 5 | State analysis (S1-S3 ranges) |
| 25 | Top 60 Corporate - Total | 4 | Extended ranking by Total Opportunity |

## 0.3 Format Specifications by Sheet

### Sheet 1: TAM SAM SOM Facilities (Tables 1-3)

**Structure:**
- Three tables: SNF, ALF, Total
- 4 columns each

**Columns:**
- Column A: Market tier (TAM/SAM/SOM)
- Column B: Corporate (Total / Our Share)
- Column C: Independent (Total / Our Share)
- Column D: Total (Total / Our Share)

**Format:** "10,065 / 462" (total facilities / facilities we serve)

### Sheet 2: TAM SAM SOM Revenue (Tables 4-9)

**Structure:**
- Six tables: 3 exact (SNF, ALF, Total) + 3 ranges (SNF, ALF, Total)
- 5 columns each

**Columns:**
- Column A: Market tier (TAM/SAM/SOM)
- Column B: Current Revenue
- Column C: Integration Revenue
- Column D: New Biz Revenue
- Column E: Total Potential Revenue

**Format:**
- Tables 4-6: Exact values (e.g., "$76,435,085")
- Tables 7-9: Ranges in millions (e.g., "$76M - $84M")

### Sheet 3: Fee Structure SOM (Tables 10-15)

**Structure:**
- Six tables: 3 exact (SNF, ALF, Total) + 3 ranges (SNF, ALF, Total)
- 11 columns each
- Scope: SOM Corporate only (excludes Independent)

**Columns:**
- Column A: Revenue type (Current/Integration/New Biz/Total Potential)
- Columns B-C: PCP ($ and %)
- Columns D-E: MH ($ and %)
- Columns F-G: CCM ($ and %)
- Columns H-I: Shared Savings ($ and %)
- Columns J-K: Total ($ and %)

**Format:**
- Tables 10-12: Exact values
- Tables 13-15: Ranges in millions

### Sheet 4: Top Corporate Rankings (Tables 16-18, 25)

**Columns (8 total):**
- Rank
- Corporate Name
- Total Facilities
- Facilities We Serve
- Current Revenue
- Integration Opp
- New Biz Opp
- Total Opportunity

**Filter (SOM Layer):**
- Existing states only (IN, KY, NC, OH, SC, VA)
- No barriers (entity-level exclusion)
- Corporate ownership only (excludes Independent)

**Sorting:**
- Table 16: By Total Opportunity (Top 20)
- Table 17: By Integration Opportunity (Top 20)
- Table 18: By New Business Opportunity (Top 20)
- Table 25: By Total Opportunity (Top 60)

**Required:** TOTAL row at bottom summing all displayed entities

### Sheet 5: State Analysis (Tables 19-24)

**Columns (8 total):**
- Market
- State(s)
- Total Facilities
- Facilities Served
- Current Revenue
- Potential Rev. Integration
- Potential Rev. New Biz
- Total Potential Revenue

**Rows for SNF and ALF tables (19-20, 22-23):**
- Existing: OH, IN, NC, VA, KY, SC (each state on its own row)

**Rows for Total tables (21, 24):**
- Existing: OH, IN, NC, VA, KY, SC (each state on its own row)
- Priority Expansion: IA, MN, IL, MI, PA, WI, MT
- Emerging: FL, GA
- Exiting: WV
- National: All other states

**Format:**
- Tables 19-21: Exact values
- Tables 22-24: Ranges in millions

## 0.4 Range Calculation Rule

For tables showing ranges (7-9, 13-15, 22-24):

1. Calculate the metric using Scenario 1, Scenario 2, and Scenario 3 data
2. Display as: "$[S1 value]M - $[S3 value]M"
3. S1 = Conservative (lowest), S3 = Premium (highest)
4. Always show in millions (M)

**Example:** If S1 = $160,426,737 and S3 = $177,469,011, display as "$160M - $177M"

## 0.5 Market Geography Definitions

**Existing Market (6 states):** IN, KY, NC, OH, SC, VA

**Priority Expansion (7 states):** IA, MN, IL, MI, PA, WI, MT

**Emerging (2 states):** FL, GA

**Exiting (1 state):** WV

**National:** All other states not listed above

---

# PART 1: EXECUTIVE SUMMARY

## 1.1 What This Model Does

The Eventus Economic Model calculates revenue opportunities across healthcare facilities (SNFs and ALFs) using **Census-based calculations** with **permanent adjusters** applied to specific fees.

**Key Formula Structure:**
```
Revenue = Census × [Base Fees with Adjusters Applied]
```

**Four Revenue Metrics:**
1. **Current Revenue** - Revenue from facilities we currently serve (REALIZED)
2. **Integration Revenue** - Additional revenue from expanding services at existing customers (POTENTIAL)
3. **New Business Revenue** - Revenue from acquiring new corporate facilities (POTENTIAL)
4. **Total Potential Revenue** - Combined opportunity (Integration + New Business)

## 1.2 Market Overview (V9.0)

| Segment | Facilities | Total Potential |
|---------|------------|-----------------|
| TAM (Total Addressable Market) | 17,434 | $5,538,308,355 |
| SAM (Existing Market States) | 5,277 | (calculated) |
| SOM (Existing + No Barriers) | 4,701 | (calculated) |

**Existing Market States:** IN, KY, NC, OH, SC, VA

---

# PART 2: FEE STRUCTURE & ADJUSTERS

## 2.1 Base Fees (Annual per Patient)

### Scenario 1: Conservative Growth

| Fee Type | SNF | ALF |
|----------|-----|-----|
| PCP | $2,600.00 | $1,951.32 |
| MH | $1,623.96 | $1,860.00 |
| CCM | $360.00 | $360.00 |
| Shared Savings | $4,800.00 | $4,800.00 |

### Scenario 2: Market Expansion (+10%)

| Fee Type | SNF | ALF |
|----------|-----|-----|
| PCP | $2,860.00 | $2,146.45 |
| MH | $1,786.36 | $2,046.00 |
| CCM | $396.00 | $396.00 |
| Shared Savings | $5,280.00 | $5,280.00 |

### Scenario 3: Premium Services (+20%)

| Fee Type | SNF | ALF |
|----------|-----|-----|
| PCP | $3,120.00 | $2,341.58 |
| MH | $1,948.75 | $2,232.00 |
| CCM | $432.00 | $432.00 |
| Shared Savings | $5,760.00 | $5,760.00 |

## 2.2 Permanent Adjusters

These adjusters are ALWAYS applied regardless of scenario:

| Fee Type | Adjuster | Rationale |
|----------|----------|-----------|
| MH | × 0.50 | Not all patients need mental health services |
| CCM | × 0.30 | Chronic care management subset |
| Shared Savings | × 0.50 × 0.33 | Half patients eligible, third achieve savings |

## 2.3 Revenue Per Patient Calculation

**SNF (Scenario 1):**
```
Total = PCP + (MH × 0.50) + (CCM × 0.30) + (SS × 0.50 × 0.33)
Total = $2,600.00 + $811.98 + $108.00 + $792.00 = $4,311.98
```

**ALF (Scenario 1):**
```
Total = PCP + (MH × 0.50) + (CCM × 0.30) + (SS × 0.50 × 0.33)
Total = $1,951.32 + $930.00 + $108.00 + $792.00 = $3,781.32
```

---

# PART 3: BARRIER MANAGEMENT

## 3.1 Barrier Types

| Barrier Type | Description | Revenue Impact |
|--------------|-------------|----------------|
| Own Provider Group | Entity has internal medical staff | Excluded from New Biz |
| Competitor Contract | Exclusive contract with competitor | Excluded from New Biz |
| Alliance | Strategic partnership precludes Eventus | Excluded from New Biz |
| Refuses Service | Entity has declined Eventus services | Excluded from New Biz |

## 3.2 Entity-Level Barrier Logic (V9.0)

**Implementation:**
```python
# Step 1: Identify barrier entities
entities_with_barriers = df[df['Barrier'].notna()]['Corporate_Name'].unique()

# Step 2: Get barrier type for each entity
entity_barrier_map = df[df['Barrier'].notna()].groupby('Corporate_Name')['Barrier'].first()

# Step 3: Apply to all facilities
for entity in entities_with_barriers:
    barrier_type = entity_barrier_map[entity]
    df.loc[df['Corporate_Name'] == entity, 'Barrier'] = barrier_type
```

**Rationale:**
- Corporate relationships are typically entity-wide
- Partial exclusions misrepresent available market
- Top Corporate reports should exclude entire barrier entities

## 3.3 Complete Barrier Entity List (21 Entities)

| # | Corporate Entity | Barrier Type | Facilities | Census |
|---|-----------------|--------------|------------|--------|
| 1 | GENESIS HEALTHCARE | Own Provider Group | 215 | 17,847 |
| 2 | SABER HEALTHCARE GROUP | Competitor Contract | 159 | 4,086 |
| 3 | COMMUNICARE HEALTH | Own Provider Group | 122 | 10,260 |
| 4 | SIMCHA HYMAN & NAFTALI ZANZIPER | Alliance | 115 | 1,489 |
| 5 | INFINITY HEALTHCARE CONSULTING | Alliance | 107 | 2,219 |
| 6 | SIGNATURE HEALTHCARE | Own Provider Group | 72 | 4,020 |
| 7 | HILL VALLEY HEALTHCARE | Alliance | 40 | 2,558 |
| 8 | CARDON & ASSOCIATES | Own Provider Group | 34 | 2,817 |
| 9 | BRICKYARD HEALTHCARE | Competitor Contract | 23 | 636 |
| 10 | VENZA CARE MANAGEMENT | Alliance | 18 | 1,298 |
| 11 | JOURNEY HEALTHCARE | Alliance | 17 | 1,130 |
| 12 | BLUEGRASS HEALTH KY | Alliance | 15 | 1,299 |
| 13 | BHI SENIOR LIVING | Refuses Service | 14 | 804 |
| 14 | COMMONWEALTH CARE OF ROANOKE | Competitor Contract | 13 | 799 |
| 15 | EXCEPTIONAL LIVING CENTERS | Alliance | 13 | 936 |
| 16 | AVENTURA HEALTH GROUP | Alliance | 12 | 322 |
| 17 | ATRIUM HEALTH | Own Provider Group | 12 | 1,026 |
| 18 | ENCORE HEALTH PARTNERS | Alliance | 12 | 606 |
| 19 | CHOICE HEALTH MANAGEMENT | Alliance | 9 | 530 |
| 20 | ALLIANCE HEALTH GROUP | Alliance | 6 | 437 |
| 21 | MAJOR HOSPITAL | Own Provider Group | 6 | 336 |
| | **TOTAL** | | **1,034** | **55,455** |

---

# PART 4: REVENUE CALCULATIONS

## 4.1 Revenue Logic by Service Status

### Integrated Facilities (Do_We_Serve = "Yes", Integrated_Flag = "Yes")
```python
Current_Revenue = Census × Total_Per_Patient
Integration_Revenue = 0
New_Biz_Revenue = 0
Total_Potential_Revenue = 0
```

### Served with MH (Do_We_Serve = "Yes", MH_Flag = "Yes")
```python
Current_Revenue = Census × MH_Adjusted_Fee
Integration_Revenue = Census × (PCP + CCM_Adjusted + SS_Adjusted)
New_Biz_Revenue = 0
Total_Potential_Revenue = Integration_Revenue
```

### Served with PCP Only (Do_We_Serve = "Yes", PCP_Flag = "Yes")
```python
Current_Revenue = Census × PCP_Fee
Integration_Revenue = Census × (MH_Adjusted + CCM_Adjusted + SS_Adjusted)
New_Biz_Revenue = 0
Total_Potential_Revenue = Integration_Revenue
```

### Not Served, No Barrier (Do_We_Serve = "No", Barrier = NULL)
```python
Current_Revenue = 0
Integration_Revenue = 0
New_Biz_Revenue = Census × Total_Per_Patient
Total_Potential_Revenue = New_Biz_Revenue
```

### Not Served, Has Barrier (Do_We_Serve = "No", Barrier ≠ NULL)
```python
Current_Revenue = 0
Integration_Revenue = 0
New_Biz_Revenue = 0
Total_Potential_Revenue = 0
```

## 4.2 Total Potential Revenue Definition

**Formula:**
```
Total_Potential_Revenue = Integration_Revenue + New_Biz_Revenue
```

**NOT:**
```
Total_Potential_Revenue ≠ Current_Revenue + Integration_Revenue + New_Biz_Revenue
```

**Rationale:** Total Potential represents FUTURE opportunity, not current realized revenue.

---

# PART 5: MARKET SEGMENTATION

## 5.1 TAM (Total Addressable Market)

**Definition:** ALL facilities regardless of ownership type or barriers
**Facilities:** 17,434
**Geographic Scope:** National (all 51 states)
**Purpose:** Shows total market size

## 5.2 SAM (Serviceable Available Market)

**Definition:** Facilities in existing market states
**Facilities:** 5,277
**Geographic Scope:** IN, KY, NC, OH, SC, VA
**Purpose:** Shows realistic near-term market

## 5.3 SOM (Serviceable Obtainable Market)

**Definition:** Facilities in existing states with no barriers
**Facilities:** 4,701
**Geographic Scope:** IN, KY, NC, OH, SC, VA
**Exclusions:** 576 facilities from barrier entities
**Purpose:** Shows immediately actionable targets

## 5.4 SOM Layer for Top Corporate Reports

Tables 16-18 and 25 use the SOM layer with three filters:
1. **Existing market states only** (IN, KY, NC, OH, SC, VA)
2. **Entity-level barrier exclusion** (21 entities fully removed)
3. **Corporate ownership only** (excludes Independent facilities)

**Independent Exclusion Rule:**
- Facilities with `Ownership_Type = "Independent"` are excluded from Top Corporate rankings
- This prevents 6,090 unrelated Independent facilities from aggregating as a single entity
- Independent facilities remain in TAM/SAM/SOM totals but not in corporate rankings
- Results in 315 corporate entities (2,648 facilities) available for targeting

---

# PART 6: SCENARIO SPECIFICATIONS

## 6.1 Scenario 1: Conservative Growth

**Description:** Current market rates with V9.0 SNF PCP adjustment
**Use Case:** Baseline projections and conservative planning

| Metric | Value |
|--------|-------|
| SNF Rev/Patient | $4,311.98 |
| ALF Rev/Patient | $3,781.32 |
| Total Potential | $5,538,308,355 |

## 6.2 Scenario 2: Market Expansion

**Description:** 10% fee increase across all services
**Use Case:** Growth planning with moderate price increases

| Metric | Value |
|--------|-------|
| SNF Rev/Patient | $4,743.18 |
| ALF Rev/Patient | $4,159.45 |
| Total Potential | $6,092,141,262 |

## 6.3 Scenario 3: Premium Services

**Description:** 20% fee increase across all services
**Use Case:** Premium market positioning

| Metric | Value |
|--------|-------|
| SNF Rev/Patient | $5,174.38 |
| ALF Rev/Patient | $4,537.58 |
| Total Potential | $6,645,968,328 |

---

# APPENDICES

## Appendix A: File Architecture

### Source File
- **Combined_Database_FINAL_V9.xlsx**
- Contains: 17,434 facilities with barriers propagated

### Scenario Files
- Economic_Model_Scenario_1_Combined_V9.xlsx
- Economic_Model_Scenario_2_Combined_V9.xlsx
- Economic_Model_Scenario_3_Combined_V9.xlsx

### Report Files
- Comprehensive_Report_Workbook_V9.xlsx (5 sheets, 25 tables)
- State_Summary_QC_Workbook_V9.xlsx
- Fee_Schedule_Reference_V9.xlsx

## Appendix B: Column Specifications

| Column | Type | Description |
|--------|------|-------------|
| Source_Type | String | "SNF" or "ALF" |
| Facility_Name | String | Facility name |
| Corporate_Name | String | Parent company |
| Address | String | Street address |
| City | String | City |
| State | String | 2-letter state code |
| ZIP | String | ZIP code |
| County | String | County name |
| Ownership_Type | String | "Corporate" or "Independent" |
| Census | Float | Patient count |
| Do_We_Serve | String | "Yes" or "No" |
| Integrated_Flag | String | "Yes" or "No" |
| PCP_Flag | String | "Yes" or "No" |
| MH_Flag | String | "Yes" or "No" |
| Barrier | String | Barrier type or NULL |
| Current_Revenue | Float | Current revenue |
| Integration_Revenue | Float | Integration opportunity |
| New_Biz_Revenue | Float | New business opportunity |
| Total_Potential_Revenue | Float | Total potential |

## Appendix C: Version History

| Version | Date | Changes |
|---------|------|---------|
| V9.0 | 2025-11-18 | Entity-level barriers, SNF PCP $2,600, new entity, 5-sheet workbook structure |
| V8.0 | 2025-11-17 | Report workbook restructuring |
| V6.0 | 2025-11-16 | TAM calculation fix for Independent facilities |
| V5.0 | 2025-11-15 | Total Potential Revenue definition corrected |

## Appendix D: Validation Checks

### Revenue Validation
- All non-barrier facilities with census must have revenue > 0
- Barrier facilities we don't serve expected to have $0

### Data Quality
- No NULL census for active facilities
- State codes must be valid 2-letter codes
- ZIP codes standardized

---

**Document End**

**Version:** V9.0 (Updated)  
**Author:** Eventus Analytics Team  
**Last Updated:** November 18, 2025
