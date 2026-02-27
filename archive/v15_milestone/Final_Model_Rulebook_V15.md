# Final Model Rulebook V15.0
## Healthcare Facility Database Revenue Model - Authoritative Reference

**Version**: 15.0  
**Date**: November 2025  
**Status**: PRODUCTION READY

---

## Executive Summary

This rulebook defines the authoritative fee structures, calculation methodologies, and governance controls for the Eventus Healthcare Economic Model. All revenue calculations must conform to the specifications in this document.

**V15.0 NOTE**: This version corrects TAM/SAM/SOM facility counts to include Independent facilities in SAM/SOM segments, and removes INDEPENDENT from corporate rankings tables.

---

## 1. System Overview & Governance

### 1.1 Data Flow Architecture

```
Combined Database (Source of Truth)
         ↓
Fee Schedule ──→ Economic Model Scenarios (S1, S2, S3)
                              ↓
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
   Comprehensive      QC Validation     Custom Reports
   Report Workbook    Workbook          (Geography, Metro Market, etc.)
```

**Governing Principles:**

1. **Combined Database** is the single source of truth for all facility data
2. All data changes must originate at the database level
3. **Fee Schedule** is maintained independently and feeds scenario calculations
4. **Economic Model Scenarios** inherit from database and apply fee calculations
5. All reports and validation workbooks are generated FROM scenarios
6. Never edit downstream files to change source data

### 1.2 Prohibited Actions

**The following actions require explicit written authorization:**

1. Modify fee values in Fee Schedule
2. Change adjuster calculations
3. Alter revenue formulas
4. Edit scenario files directly (must update database first)
5. Skip QC validation before delivery
6. Deliver files without verification
7. Reuse or overwrite existing version numbers

**Violation Protocol:** Any unauthorized action triggers full audit and potential rollback to last verified version.

### 1.3 Version Control Requirements

- Minor fixes: V15.0 → V15.1 → V15.2
- Major changes: V15.x → V16.0
- **Never reuse version numbers**
- **Never overwrite files - always increment**
- **Always create comparison reports for version changes**

### 1.4 Fee Change Management

**MANDATORY for any fee modification:**

1. **Written Authorization** - Explicit approval from project owner required
2. **Impact Analysis** - Calculate full impact before implementation
3. **Documentation** - Update rulebook and comparison report
4. **Validation** - Run QC Validation Workbook to verify

### 1.5 QC Validation Requirements

**Run QC_Validation_Workbook after EVERY major step:**

1. **Fee Structure Validation** - All fees must show PASS status
2. **Baseline Comparison** - ALF Current = $83,991,652
3. **Barrier Validation** - Total barriers = 1,383
4. **Financial Reconciliation** - Total facilities = 17,434

---

## 2. Fee Structure - AUTHORITATIVE VALUES

### 2.1 Base Service Fees

| Service | SNF | ALF |
|---------|-----|-----|
| PCP | $2,600.00 | $1,875.00 |
| MH | $1,623.96 | $1,898.00 |
| CCM | $360.00 | $360.00 |
| SS | $4,800.00 | $4,800.00 |

### 2.2 Permanent Adjusters

| Service | Adjuster | Calculation |
|---------|----------|-------------|
| PCP | 1.00 | No adjustment |
| MH | 0.50 | Base × 0.50 |
| CCM | 0.30 | Base × 0.30 |
| SS | 0.165 | Base × 0.50 × 0.33 |

### 2.3 Adjusted Service Fees

| Service | SNF Calculation | SNF Result | ALF Calculation | ALF Result |
|---------|-----------------|------------|-----------------|------------|
| PCP | $2,600.00 × 1.00 | $2,600.00 | $1,875.00 × 1.00 | $1,875.00 |
| MH | $1,623.96 × 0.50 | $811.98 | $1,898.00 × 0.50 | $949.00 |
| CCM | $360.00 × 0.30 | $108.00 | $360.00 × 0.30 | $108.00 |
| SS | $4,800.00 × 0.165 | $792.00 | $4,800.00 × 0.165 | $792.00 |
| **TOTAL** | | **$4,311.98** | | **$3,724.00** |

---

## 3. Revenue Calculations

### 3.1 Governing Principles

**No Double Counting:** Each service component (PCP, MH, CCM, SS) can only be counted once per facility. If a service is included in Current Revenue, it cannot also appear in Integration Revenue.

**Adjusted Values:** Throughout this section, (adj) indicates the service fee with permanent adjusters applied (see Section 2.2).

**TOTAL:** The sum of all adjusted service fees: PCP + MH(adj) + CCM(adj) + SS(adj)

**Current Revenue:** Revenue from facilities we currently serve. NEVER affected by barriers.

**Integration Revenue:** Remaining services that could be added to current customers.

**New Business Revenue:** Potential revenue from facilities we do not currently serve.

### 3.2 Service Package Definitions by Scenario

| Service Type | Scenario 1 (Baseline) | Scenario 2 (PCP Enhanced) | Scenario 3 (Comprehensive) |
|--------------|----------------------|---------------------------|----------------------------|
| PCP Only | PCP | PCP + CCM(adj) + SS(adj) | PCP + CCM(adj) + SS(adj) |
| MH Only | MH(adj) | MH(adj) | MH(adj) + CCM(adj) |
| Integrated | PCP + MH(adj) + CCM(adj) + SS(adj) | PCP + MH(adj) + CCM(adj) + SS(adj) | PCP + MH(adj) + CCM(adj) + SS(adj) |

### 3.3 Current Revenue Formulas

| Service Type | Scenario 1 | Scenario 2 | Scenario 3 |
|--------------|------------|------------|------------|
| PCP Only | Census × PCP | Census × (PCP + CCM(adj) + SS(adj)) | Census × (PCP + CCM(adj) + SS(adj)) |
| MH Only | Census × MH(adj) | Census × MH(adj) | Census × (MH(adj) + CCM(adj)) |
| Integrated | Census × TOTAL | Census × TOTAL | Census × TOTAL |

### 3.4 Integration Revenue Formulas

| Service Type | Scenario 1 | Scenario 2 | Scenario 3 |
|--------------|------------|------------|------------|
| PCP Only | Census × (MH(adj) + CCM(adj) + SS(adj)) | Census × MH(adj) | Census × MH(adj) |
| MH Only | Census × (PCP + CCM(adj) + SS(adj)) | Census × (PCP + CCM(adj) + SS(adj)) | Census × (PCP + SS(adj)) |
| Integrated | $0 | $0 | $0 |
| With Barrier | $0 | $0 | $0 |

### 3.5 New Business Revenue

New Business Revenue represents potential revenue from facilities we do not currently serve. New customers always receive the full integrated package.

**Formula (All Scenarios):** Census × TOTAL

| Condition | Result |
|-----------|--------|
| Not Served, No Barrier | Census × TOTAL |
| Not Served, Has Barrier | $0 |
| Served | $0 |

### 3.6 Total Potential Revenue

**Formula:** Integration Revenue + New Business Revenue

**Note:** Does NOT include Current Revenue.

### 3.7 Scenario Behavior Patterns

| Behavior | S1 → S2 → S3 |
|----------|--------------|
| Current Revenue | Increases |
| Integration Revenue | Decreases |
| New Business Revenue | Unchanged |
| Total Potential | Integration Revenue + New Business Revenue |

**Key Insight:** As service packages are enhanced (S1→S3), current customer value increases but integration opportunity decreases proportionally.

### 3.8 V15.0 Key Metrics

| Metric | Scenario 1 | Scenario 2 | Scenario 3 |
|--------|------------|------------|------------|
| Current Revenue | $177,598,757 | $188,542,037 | $194,278,187 |
| Integration Revenue | $127,760,637 | $119,378,037 | $115,528,539 |
| New Business Revenue | $5,115,910,599 | $5,115,910,599 | $5,115,910,599 |
| **Total Potential** | **$5,243,671,236** | **$5,235,288,636** | **$5,231,439,138** |

---

## 4. Reporting Layer

This section defines the filters and constructs used in the Comprehensive Report Workbook.

### 4.1 Market Definitions

| Market | States |
|--------|--------|
| Existing | IN, KY, NC, OH, SC, VA |
| Priority Expansion | IA, MN, IL, MI, PA, WI, MT |
| Emerging | FL, GA |
| Exiting | WV |
| National | All other states |

### 4.2 Ownership Classification

**Source Column**: Corporate_Name (Column C)

**Classification Rules:**

| Condition | Ownership_Type |
|-----------|----------------|
| Corporate_Name is blank | Independent |
| Corporate_Name appears once (single facility) | Independent |
| Corporate_Name appears more than once (multiple facilities) | Corporate |

**Notes:**
- Classification is complete in the database; no further manipulation required
- Corporate_Name is the lookup key for grouping facilities by parent company
- Do NOT use Corporate_Name column to determine ownership; use Ownership_Type column

### 4.3 Barrier Application

Barriers indicate facilities where potential revenue cannot be realized. All barriers result in:
- Current Revenue: **Unchanged**
- Integration Potential Revenue: **$0**
- New Business Potential Revenue: **$0**
- Total Potential Revenue: **$0**

#### Barrier Types

| Type | Facilities |
|------|------------|
| Own Provider Group | 402 |
| Alliance | 281 |
| Competitor Contract | 182 |
| MH Only Opportunity | 145 |
| Competitor Agreement | 115 |
| Alliance, Own Provider Group | 113 |
| Reputation | 97 |
| Termination Risk | 29 |
| Alliance, MH Only Opportunity | 19 |
| **Total** | **1,383** |

**Propagation Rule:** If one facility under a corporate entity has a barrier, all facilities under that entity should have the same barrier.

### 4.4 TAM/SAM/SOM Construct

**IMPORTANT:** Different tables use different filter rules. See table-specific rules below.

#### Revenue Tables (Tables 4-9, 10-15)

| Segment | Markets | Source Type | Ownership Type | Barriers |
|---------|---------|-------------|----------------|----------|
| TAM | All Markets | ALF + SNF | Corporate + Independent | No filter |
| SAM | Existing + Priority | ALF + SNF | Corporate only | Minus barriers |
| SOM | Existing only | ALF + SNF | Corporate only | Minus barriers |

#### Facility Count Tables (Tables 1-3)

| Segment | Markets | Source Type | Ownership Type | Barriers |
|---------|---------|-------------|----------------|----------|
| TAM | All Markets | ALF + SNF | Corporate + Independent | No filter |
| SAM | Existing + Priority | ALF + SNF | **Corporate + Independent** | Minus barriers |
| SOM | Existing only | ALF + SNF | **Corporate + Independent** | Minus barriers |

**Rationale:** Tables 1-3 display facility counts by ownership type. Excluding Independent facilities from SAM/SOM would show misleading zeros in the Independent column. These tables show the addressable market by ownership within the geographic and barrier constraints.

---

## 5. Comprehensive Report Outputs

This section describes the structure and methodology for generating the Comprehensive_Report_Workbook.xlsx.

### 5.1 General Methodology

**Data Source:** All tables pull from Economic_Model_Scenario files (S1 for point values, S1-S3 for ranges).

**Standard Columns for Revenue Tables:**
- Current Revenue
- Potential Rev. Integration
- Potential Rev. New Biz
- Total Potential Revenue

**Range Calculations:** For tables showing ranges, display format is "S1 - S3" (e.g., "$41M - $49M").

**Aggregation Rules:**
- Sum Census-weighted revenue by grouping variable
- Count facilities by grouping variable
- Count served facilities where Do_We_Serve = "Yes"

### 5.2 Sheet: TAM SAM SOM Facilities

**Tables 1-3: Facility Counts**

| Table | Source Type Filter | Output Format |
|-------|-------------------|---------------|
| Table 1 | SNF only | Facility counts |
| Table 2 | ALF only | Facility counts |
| Table 3 | All (SNF + ALF) | Facility counts |

**Methodology:**
1. Filter by Source_Type (SNF/ALF/All)
2. Group by TAM/SAM/SOM segment (apply filters from Section 4.4 - **Facility Count Tables**)
3. Cross-tabulate by Ownership_Type (Corporate / Independent / Total)
4. Display as "Total / Our Share" format (e.g., "10,065 / 462")
   - Total = count of facilities
   - Our Share = count where Do_We_Serve = "Yes"

**V15 Note:** SAM and SOM rows include BOTH Corporate AND Independent facilities that meet the geographic and barrier criteria.

### 5.3 Sheet: TAM SAM SOM Revenue

**Tables 4-9: Revenue by Segment**

| Table | Source Type | Values |
|-------|-------------|--------|
| Table 4 | SNF | S1 point values |
| Table 5 | ALF | S1 point values |
| Table 6 | Total | S1 point values |
| Table 7 | SNF | S1-S3 ranges |
| Table 8 | ALF | S1-S3 ranges |
| Table 9 | Total | S1-S3 ranges |

**Methodology:**
1. Filter by Source_Type
2. Group by TAM/SAM/SOM segment (apply filters from Section 4.4 - **Revenue Tables**)
3. Sum revenue columns: Current, Integration, New Biz, Total Potential
4. For range tables, calculate min (S1) and max (S3) for display

**Columns:**
- Current Revenue
- Potential Integration
- Potential New Biz
- Total Potential

### 5.4 Sheet: Fee Structure SOM

**Tables 10-15: SOM Revenue Detail**

| Table | Source Type | Values |
|-------|-------------|--------|
| Table 10 | SNF | S1 point values |
| Table 11 | ALF | S1 point values |
| Table 12 | Total | S1 point values |
| Table 13 | SNF | S1-S3 ranges |
| Table 14 | ALF | S1-S3 ranges |
| Table 15 | Total | S1-S3 ranges |

**Methodology:**
1. Filter to SOM segment only (Existing markets, Corporate only, minus barriers)
2. Filter by Source_Type
3. Sum revenue columns
4. Same column structure as Tables 4-9

### 5.5 Sheet: Top Corporate Rankings

**Tables 16-18, 25: Corporate Entity Rankings**

| Table | Ranking Metric | Count |
|-------|----------------|-------|
| Table 16 | Total Opportunity | Top 20 |
| Table 17 | Integration Opportunity | Top 20 |
| Table 18 | New Business Opportunity | Top 20 |
| Table 25 | Total Opportunity | Top 60 |

**Filter:** SOM segment (Corporate only, Existing markets, no barriers) - Scenario 1

**CRITICAL RULE:** These tables rank corporate entities (chains) only. **Independent facilities are EXCLUDED from rankings.** Independent is not a corporate entity and cannot be meaningfully compared to corporate chains.

**Methodology:**
1. Apply SOM filters (Existing markets, Corporate only, no barriers)
2. Group by Corporate_Name
3. For each corporate entity, sum:
   - Total Facilities (count)
   - Facilities We Serve (count where Do_We_Serve = "Yes")
   - Current Revenue
   - Integration Opportunity
   - New Biz Opportunity
   - Total Opportunity
4. Rank by specified metric (descending)
5. Take top N records
6. Add TOTAL row at bottom

**Columns:**
- Rank
- Corporate Name
- Total Facilities
- Facilities We Serve
- Current Revenue
- Integration Opp
- New Biz Opp
- Total Opportunity

### 5.6 Sheet: State Analysis

**Tables 19-24: Revenue by State and Market**

| Table | Source Type | Values |
|-------|-------------|--------|
| Table 19 | SNF | S1 point values |
| Table 20 | ALF | S1 point values |
| Table 21 | Total | S1 point values |
| Table 22 | SNF | S1-S3 ranges |
| Table 23 | ALF | S1-S3 ranges |
| Table 24 | Total | S1-S3 ranges |

**Methodology:**
1. Filter by Source_Type
2. Group by Market → State
3. For each state, calculate:
   - Total Facilities
   - Facilities Served
   - Current Revenue
   - Potential Rev. Integration
   - Potential Rev. New Biz
   - Total Potential Revenue
4. Order by Market hierarchy (Existing first, then Priority, Emerging, Exiting, National)
5. Within Existing market, list each state separately
6. For other markets, combine states in single row

**Columns:**
- Market
- State(s)
- Total Facilities
- Facilities Served
- Current Revenue
- Potential Rev. Integration
- Potential Rev. New Biz
- Total Potential Revenue

---

## 6. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| **V15.0** | Nov 2025 | Tables 1-3 include Independent in SAM/SOM; Tables 16-18 exclude INDEPENDENT |
| V14.0 | Nov 2025 | Updated fee structure with walked-out math, corrected scenario definitions |
| V13.0 | Nov 2025 | Consolidated barrier columns, restructured rulebook with System Overview |
| V12.0 | Nov 2025 | Correct file formats, Integrated Barrier calculations |
| V11.0 | Nov 2025 | Integrated Barrier propagation (formatting errors) |
| V10.0 | Nov 2025 | ALF fees corrected, QC validation added |

---

**END OF RULEBOOK**

*This document is the authoritative reference. Deviations require written authorization.*
