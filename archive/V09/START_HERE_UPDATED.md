# START_HERE.md
## Eventus Healthcare Economic Model - Project Reference

**Version:** 9.0  
**Last Updated:** November 18, 2025  
**Status:** PRODUCTION READY

---

## PROJECT OVERVIEW

The Eventus Economic Model calculates revenue opportunities across 17,434 healthcare facilities (SNFs and ALFs) using census-based calculations with three pricing scenarios. The model supports strategic planning for market expansion, customer integration, and new business development.

### Key Metrics (V9.0)

| Metric | Value |
|--------|-------|
| Total Facilities | 17,434 |
| Facilities with Barriers | 1,034 (21 entities) |
| Current Revenue | $178,194,023 |
| Total Potential Revenue | $5,538,308,355 |

---

## FILE INVENTORY

### Core Files

| File | Purpose |
|------|---------|
| **Combined_Database_FINAL_V9.xlsx** | Source database with all 17,434 facilities |
| **Economic_Model_Scenario_1_Combined_V9.xlsx** | Conservative growth scenario |
| **Economic_Model_Scenario_2_Combined_V9.xlsx** | Market expansion scenario (+10%) |
| **Economic_Model_Scenario_3_Combined_V9.xlsx** | Premium services scenario (+20%) |

### Report Files

| File | Purpose |
|------|---------|
| **Comprehensive_Report_Workbook_V9_STYLED.xlsx** | Main report with 5 sheets, 25 tables |
| **State_Summary_QC_Workbook_V9.xlsx** | State-level QC validation |
| **Fee_Schedule_Reference_V9.xlsx** | Fee structure reference |

### Documentation

| File | Purpose |
|------|---------|
| **Final_Model_Rulebook_V9_UPDATED.md** | Complete technical specification |
| **V8_to_V9_Comparison_Report.md** | Change documentation from V8 to V9 |
| **START_HERE.md** | This file - project reference |

---

## COMPREHENSIVE REPORT WORKBOOK STRUCTURE

The main reporting workbook contains 5 sheets with 25 tables:

### Sheet 1: TAM SAM SOM Facilities
**Tables 1-3** | 4 columns | Facility counts by ownership type

- Table 1: SNF Facilities
- Table 2: ALF Facilities
- Table 3: Total Facilities

Format: "Total / Our Share" (e.g., "10,065 / 462")

### Sheet 2: TAM SAM SOM Revenue
**Tables 4-9** | 5 columns | Revenue metrics

- Tables 4-6: Exact values (Scenario 1)
- Tables 7-9: Ranges (Scenario 1 to Scenario 3)

### Sheet 3: Fee Structure SOM
**Tables 10-15** | 11 columns | Fee breakdown by service type

- Tables 10-12: Exact values (Scenario 1)
- Tables 13-15: Ranges (Scenario 1 to Scenario 3)

Scope: SOM Corporate only (excludes Independent)

### Sheet 4: Top Corporate Rankings
**Tables 16-18, 25** | 8 columns | Corporate entity rankings

- Table 16: Top 20 by Total Opportunity
- Table 17: Top 20 by Integration Opportunity
- Table 18: Top 20 by New Business Opportunity
- Table 25: Top 60 by Total Opportunity

Filter: Existing states, no barriers, corporate only

### Sheet 5: State Analysis
**Tables 19-24** | 8 columns | Geographic breakdown

- Tables 19-21: Exact values (Scenario 1)
- Tables 22-24: Ranges (Scenario 1 to Scenario 3)

Markets: Existing (6 states), Priority Expansion, Emerging, Exiting, National

---

## V9.0 KEY CHANGES

### 1. Entity-Level Barrier Logic
Barriers now propagate to ALL facilities under a corporate entity:
- Previous: 68 facilities with barriers
- Current: 1,034 facilities with barriers (21 entities)

### 2. SNF PCP Fee Increase
- Previous: $1,698.96
- Current: $2,600.00 (+53.0%)

### 3. New Barrier Entity
Added SIMCHA HYMAN & NAFTALI ZANZIPER (Alliance, 115 facilities)

### 4. Workbook Restructure
- Previous: 10 sheets with mixed organization
- Current: 5 sheets with logical groupings by column width

---

## MARKET DEFINITIONS

### Geographic Markets

| Market | States | Purpose |
|--------|--------|---------|
| Existing | IN, KY, NC, OH, SC, VA | Current operations |
| Priority Expansion | IA, MN, IL, MI, PA, WI, MT | Near-term expansion |
| Emerging | FL, GA | Growth opportunities |
| Exiting | WV | Wind-down market |
| National | All others | Long-term potential |

### Market Segments

| Segment | Definition | Facilities |
|---------|------------|------------|
| TAM | All facilities | 17,434 |
| SAM | Existing states only | 5,277 |
| SOM | Existing states, no barriers | 4,701 |

---

## REVENUE DEFINITIONS

| Metric | Definition |
|--------|------------|
| **Current Revenue** | Revenue from facilities we currently serve (REALIZED) |
| **Integration Revenue** | Additional revenue from expanding services at existing customers (POTENTIAL) |
| **New Business Revenue** | Revenue from acquiring new facilities (POTENTIAL) |
| **Total Potential Revenue** | Integration + New Business (FUTURE OPPORTUNITY) |

**Important:** Total Potential Revenue does NOT include Current Revenue.

---

## FEE STRUCTURE (SCENARIO 1)

### Base Fees (Annual per Patient)

| Fee Type | SNF | ALF |
|----------|-----|-----|
| PCP | $2,600.00 | $1,951.32 |
| MH | $1,623.96 | $1,860.00 |
| CCM | $360.00 | $360.00 |
| Shared Savings | $4,800.00 | $4,800.00 |

### Permanent Adjusters

| Fee Type | Adjuster |
|----------|----------|
| MH | × 0.50 |
| CCM | × 0.30 |
| Shared Savings | × 0.50 × 0.33 |

### Revenue Per Patient

- SNF: $4,311.98
- ALF: $3,781.32

---

## BARRIER ENTITIES (21 TOTAL)

The following corporate entities are fully excluded from New Business Revenue and Top Corporate reports:

1. GENESIS HEALTHCARE (215 facilities)
2. SABER HEALTHCARE GROUP (159 facilities)
3. COMMUNICARE HEALTH (122 facilities)
4. SIMCHA HYMAN & NAFTALI ZANZIPER (115 facilities)
5. INFINITY HEALTHCARE CONSULTING (107 facilities)
6. SIGNATURE HEALTHCARE (72 facilities)
7. HILL VALLEY HEALTHCARE (40 facilities)
8. CARDON & ASSOCIATES (34 facilities)
9. BRICKYARD HEALTHCARE (23 facilities)
10. VENZA CARE MANAGEMENT (18 facilities)
11. JOURNEY HEALTHCARE (17 facilities)
12. BLUEGRASS HEALTH KY (15 facilities)
13. BHI SENIOR LIVING (14 facilities)
14. COMMONWEALTH CARE OF ROANOKE (13 facilities)
15. EXCEPTIONAL LIVING CENTERS (13 facilities)
16. AVENTURA HEALTH GROUP (12 facilities)
17. ATRIUM HEALTH (12 facilities)
18. ENCORE HEALTH PARTNERS (12 facilities)
19. CHOICE HEALTH MANAGEMENT (9 facilities)
20. ALLIANCE HEALTH GROUP (6 facilities)
21. MAJOR HOSPITAL (6 facilities)

---

## SCENARIO COMPARISON

| Metric | S1 (Conservative) | S2 (+10%) | S3 (+20%) |
|--------|-------------------|-----------|-----------|
| SNF Rev/Patient | $4,311.98 | $4,743.18 | $5,174.38 |
| ALF Rev/Patient | $3,781.32 | $4,159.45 | $4,537.58 |
| Total Potential | $5.54B | $6.09B | $6.65B |

---

## VALIDATION CHECKLIST

When working with this model, verify:

- [ ] Total facilities = 17,434
- [ ] Barrier facilities = 1,034
- [ ] Barrier entities = 21
- [ ] TAM Total Potential (S1) = $5,538,308,355
- [ ] Top corporate entity = TRILOGY HEALTH SERVICES
- [ ] All barrier entities excluded from Top Corporate tables

---

## COMMON TASKS

### Regenerating Report Workbook

If scenario files change, regenerate the Comprehensive Report Workbook using:
1. Load all three scenario files
2. Calculate TAM/SAM/SOM metrics
3. Calculate fee breakdowns for SOM Corporate
4. Generate Top Corporate rankings (SOM layer)
5. Calculate state-level metrics
6. Format with table numbering 1-25

### Adding a New Barrier Entity

1. Update source database with barrier type for one facility
2. Run entity-level barrier propagation script
3. Regenerate all three scenario files
4. Regenerate report workbook

### Updating Fee Schedule

1. Update Fee_Schedule_Reference_V9.xlsx
2. Recalculate all scenario files with new fees
3. Regenerate report workbook
4. Update Final_Model_Rulebook with new fees

---

## VERSION HISTORY

| Version | Date | Key Changes |
|---------|------|-------------|
| V9.0 | 2025-11-18 | Entity-level barriers, SNF PCP $2,600, 5-sheet workbook |
| V8.0 | 2025-11-17 | Report workbook restructuring |
| V6.0 | 2025-11-16 | TAM calculation fix |
| V5.0 | 2025-11-15 | Total Potential Revenue definition |

---

## CONTACT

For questions about this model, refer to the Final_Model_Rulebook_V9_UPDATED.md for complete technical specifications.

---

**Document End**
