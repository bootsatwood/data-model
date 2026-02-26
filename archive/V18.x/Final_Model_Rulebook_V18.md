# Final Model Rulebook V18.0
## Healthcare Facility Database Revenue Model - Authoritative Reference

**Version**: 18.0  
**Date**: November 2025  
**Status**: PRODUCTION READY

---

## Executive Summary

This rulebook defines the authoritative fee structures, calculation methodologies, and governance controls for the Eventus Healthcare Economic Model. All revenue calculations must conform to the specifications in this document.

**V18.0 NOTE**: This version implements V17.1 database (21,023 facilities: 15,234 SNF + 5,789 ALF, +20.6% from V15), updated fee structure per market analysis, ownership reclassification using consistent Four-Rule hierarchy (12,053 Corporate facilities in 1,026 chains, 8,970 Independent), and adds database column documentation to Section 2.

**V17.1 Database Foundation:**
- 8-state Eventus WholeHealth integration (+3,589 facilities from V15's 17,434)
- Consistent count-based ownership classification applied to all facilities
- 2,327 facilities reclassified (11.1%): single-facility LLCs corrected to Independent
- GPS-based deduplication and corporate name harmonization
- 1,743 facilities currently served

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

- Minor fixes: V18.0 → V18.1 → V18.2
- Major changes: V18.x → V19.0
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
2. **Baseline Comparison** - Verify against V18 established baselines
3. **Barrier Validation** - Total barriers verification
4. **Financial Reconciliation** - Total facilities = 21,023

### 1.6 Production Package Requirements

**The Economic Model operates as an integrated document compendium. All files must travel together as a complete package.**

#### Standard Package Contents (10 files minimum):

| File Type | File Name Pattern | Purpose |
|-----------|------------------|---------|
| **Core Data** | Combined_Database_FINAL_Vxx.xlsx | Source of truth for all facility data |
| **Scenarios** | Economic_Model_Scenario_1_Combined_Vxx.xlsx | Conservative growth calculations |
| | Economic_Model_Scenario_2_Combined_Vxx.xlsx | Market expansion calculations (+10%) |
| | Economic_Model_Scenario_3_Combined_Vxx.xlsx | Premium services calculations (+20%) |
| **Reports** | Comprehensive_Report_Workbook_Vxx.xlsx | All 25 analytical tables |
| | QC_Validation_Workbook_Vxx.xlsx | Validation checks and baselines |
| **Reference** | Fee_Schedule_Reference_Vxx.xlsx | Authoritative fee lookup |
| **Documentation** | Final_Model_Rulebook_Vxx.md | Complete technical specification |
| | START_HERE_Vxx.md | Engagement workflow and quick reference |
| | Vxx_to_Vyy_Comparison_Report.md | Change documentation |

#### Compendium Integrity Rules:

1. **Version Consistency**: All files in package must share same major version number
2. **Complete Set**: Never deliver partial packages - all 10 files required
3. **Documentation Chain**: Comparison report must trace from previous version
4. **Cross-Reference**: Files reference each other; incomplete sets break workflows

#### Delivery Checklist:

- [ ] All 10 files present
- [ ] Version numbers consistent (e.g., all V18.0)
- [ ] Comparison report included
- [ ] QC validation passed
- [ ] START_HERE updated

---

## 2. Combined Database

### 2.1 Database Architecture Flow

```
Source Files
    ↓
Combined Database (Single Source of Truth)
    ↓
Fee Schedule → Economic Model Scenarios (S1, S2, S3)
    ↓
Reports & Validation
```

**Critical Principle:** All data flows from Combined Database. Never edit downstream files to modify source data.

### 2.2 Source File Evolution

This table documents the major sources that built the Combined Database across versions:

| Version | Date | Source Description | SNF Added | ALF Added | Total Facilities | Key Changes |
|---------|------|-------------------|-----------|-----------|------------------|-------------|
| V8.0 Base | Nov 2025 | SNF Stream V2.5 + ALF Combined V9.0 merger | 14,750 | 2,684 | 17,434 | Initial unified database |
| V11.0 | Nov 2025 | Book1.xlsx Barrier Integration | - | - | 17,434 | Propagated 111 barriers to 786 facilities across 32 parent companies |
| V15.0 | Nov 2025 | Ownership consistency corrections | - | - | 17,434 | TAM/SAM/SOM methodology refined |
| V17.1 | Nov 2025 | Eventus WholeHealth 8-state integration | +484 | +3,105 | 21,023 | GPS deduplication, corporate name harmonization, Four-Rule reclassification |

**V17.1 Composition:**
- SNF: 15,234 facilities (72.5%)
- ALF: 5,789 facilities (27.5%)
- Corporate: 12,053 facilities in 1,026 chains (57.3%)
- Independent: 8,970 facilities (42.7%)

**Historical Context:**
- ALF sources consolidated in V9.0 included: ALF We Serve V2.2 (1,185), ALF In States V1.5 (1,563)
- SNF Stream V2.5 consolidated 14,750 facilities from state-specific tabs
- Book1.xlsx provided operational pull-through tracking (622 facilities, 111 with barriers)

### 2.3 Ownership Classification

**Column to Use:** `Ownership_Type`

**Classification Method:** Four-Rule Count-Based Hierarchy (applied to all 21,023 facilities in V17.1)

#### Rule 1: Blank Corporate Name → Independent

```
IF Corporate_Name IS NULL OR Corporate_Name = ''
  THEN Ownership_Type = "Independent"
```

**V18 Count:** 4,685 facilities

#### Rule 2: "INDEPENDENT" Placeholder → Independent

```
IF UPPER(Corporate_Name) = "INDEPENDENT"
  THEN Ownership_Type = "Independent"
```

**V18 Count:** 780 facilities  
**Purpose:** Prevents misclassification of standardization placeholder

#### Rule 3: Multi-Facility Chains → Corporate

```
IF COUNT(Corporate_Name) > 1 across entire database
  THEN Ownership_Type = "Corporate"
```

**V18 Count:** 1,026 chains, 12,053 facilities  
**Definition:** True multi-facility corporate operators

#### Rule 4: Single-Facility Operators → Independent

```
IF COUNT(Corporate_Name) = 1 across entire database
  THEN Ownership_Type = "Independent"
```

**V18 Count:** 3,505 facilities  
**Definition:** Facilities operating only one location (regardless of LLC/Inc legal structure)

#### Critical Distinction

| Ownership Type | Definition | Example |
|---------------|------------|---------|
| Corporate | Operates 2+ facilities | TRILOGY HEALTH SERVICES (186 facilities) |
| Independent | Operates 1 facility only | HERITAGE MANOR, LLC (1 facility) |

**CRITICAL**: Do NOT use `Corporate_Name` column presence to determine ownership. The `Corporate_Name` field may be populated for Independent facilities (particularly single-facility LLCs) and does not indicate ownership type. Always use `Ownership_Type` column.

**Business Impact:**
- **Legal structure ≠ Operational scale** - An LLC operating 1 facility is Independent
- **Corporate** = Portfolio relationships, multi-facility contracts
- **Independent** = Individual facility relationships, location-specific decisions

### 2.4 Facility Type Classification

**Column to Use:** `Source_Type`

| Value | Definition | V18 Count |
|-------|------------|-----------|
| SNF | Skilled Nursing Facility | 15,234 |
| ALF | Assisted Living Facility | 5,789 |

### 2.5 Service Status

**Column to Use:** `Do_We_Serve`

| Value | Definition |
|-------|------------|
| Yes | Currently served facility |
| No | Not currently served |

**V18 Count:** 1,743 served facilities

### 2.6 Service Flags

| Column | Values | Definition |
|--------|--------|------------|
| `Integrated_Flag` | Yes/No | Facility receives both PCP and MH services |
| `PCP_Flag` | Yes/No | Facility receives PCP services only |
| `MH_Flag` | Yes/No | Facility receives MH services only |

**Service Configuration Rules:**
- Integrated_Flag = Yes → PCP_Flag = Yes AND MH_Flag = Yes
- PCP_Flag = Yes, MH_Flag = No → PCP-only facility
- MH_Flag = Yes, PCP_Flag = No → MH-only facility
- All flags = No → Not served

---

## 3. Fee Structure - AUTHORITATIVE VALUES

### 3.1 Base Service Fees

| Service | SNF | ALF |
|---------|-----|-----|
| PCP | $3,078.00 | $2,084.00 |
| MH | $1,211.00 | $1,431.00 |
| CCM | $360.00 | $360.00 |
| SS | $4,800.00 | $4,800.00 |

### 3.2 Permanent Adjusters

| Service | Adjuster | Calculation |
|---------|----------|-------------|
| PCP | 1.00 | No adjustment |
| MH | 0.50 | Base × 0.50 |
| CCM | 0.30 | Base × 0.30 |
| SS | 0.165 | Base × 0.50 × 0.33 |

### 3.3 Adjusted Service Fees

| Service | SNF Calculation | SNF Result | ALF Calculation | ALF Result |
|---------|-----------------|------------|-----------------|------------|
| PCP | $3,078.00 × 1.00 | $3,078.00 | $2,084.00 × 1.00 | $2,084.00 |
| MH | $1,211.00 × 0.50 | $605.50 | $1,431.00 × 0.50 | $715.50 |
| CCM | $360.00 × 0.30 | $108.00 | $360.00 × 0.30 | $108.00 |
| SS | $4,800.00 × 0.165 | $792.00 | $4,800.00 × 0.165 | $792.00 |
| **TOTAL** | | **$4,583.50** | | **$3,699.50** |

---

## 4. Revenue Calculations

### 4.1 Governing Principles

**No Double Counting:** Each service component (PCP, MH, CCM, SS) can only be counted once per facility. If a service is included in Current Revenue, it cannot also appear in Integration Revenue.

**Adjusted Values:** Throughout this section, (adj) indicates the service fee with permanent adjusters applied (see Section 3.2).

**TOTAL:** The sum of all adjusted service fees: PCP + MH(adj) + CCM(adj) + SS(adj)

**Current Revenue:** Revenue from facilities we currently serve. NEVER affected by barriers.

**Integration Revenue:** Remaining services that could be added to current customers.

**New Business Revenue:** Potential revenue from facilities we do not currently serve.

### 4.2 Service Package Definitions by Scenario

| Service Type | Scenario 1 (Baseline) | Scenario 2 (PCP Enhanced) | Scenario 3 (Comprehensive) |
|--------------|----------------------|---------------------------|----------------------------|
| PCP Only | PCP | PCP + CCM(adj) + SS(adj) | PCP + CCM(adj) + SS(adj) |
| MH Only | MH(adj) | MH(adj) | MH(adj) + CCM(adj) |
| Integrated | PCP + MH(adj) + CCM(adj) + SS(adj) | PCP + MH(adj) + CCM(adj) + SS(adj) | PCP + MH(adj) + CCM(adj) + SS(adj) |

### 4.3 Current Revenue Formulas

| Service Type | Scenario 1 | Scenario 2 | Scenario 3 |
|--------------|------------|------------|------------|
| PCP Only | Census × PCP | Census × (PCP + CCM(adj) + SS(adj)) | Census × (PCP + CCM(adj) + SS(adj)) |
| MH Only | Census × MH(adj) | Census × MH(adj) | Census × (MH(adj) + CCM(adj)) |
| Integrated | Census × TOTAL | Census × TOTAL | Census × TOTAL |

### 4.4 Integration Revenue Formulas

| Service Type | Scenario 1 | Scenario 2 | Scenario 3 |
|--------------|------------|------------|------------|
| PCP Only | Census × (MH(adj) + CCM(adj) + SS(adj)) | Census × MH(adj) | Census × MH(adj) |
| MH Only | Census × (PCP + CCM(adj) + SS(adj)) | Census × (PCP + CCM(adj) + SS(adj)) | Census × (PCP + SS(adj)) |
| Integrated | $0 | $0 | $0 |
| With Barrier | $0 | $0 | $0 |

### 4.5 New Business Revenue

New Business Revenue represents potential revenue from facilities we do not currently serve. New customers always receive the full integrated package.

**Formula (All Scenarios):** Census × TOTAL

| Condition | Result |
|-----------|--------|
| Not Served, No Barrier | Census × TOTAL |
| Not Served, Has Barrier | $0 |
| Served | $0 |

### 4.6 Total Potential Revenue

**Formula:** Integration Revenue + New Business Revenue

**Note:** Does NOT include Current Revenue.

### 4.7 Scenario Behavior Patterns

| Behavior | S1 → S2 → S3 |
|----------|--------------|
| Current Revenue | Increases |
| Integration Revenue | Decreases |
| New Business Revenue | Unchanged |
| Total Potential | Integration Revenue + New Business Revenue |

**Key Insight:** As service packages are enhanced (S1→S3), current customer value increases but integration opportunity decreases proportionally.

### 4.8 V18.0 Key Metrics

**Database:** V17.1 (21,023 facilities: 15,234 SNF + 5,789 ALF)

| Metric | Status |
|--------|--------|
| Current Revenue | TBD - Calculate from V17.1 with V18 fees |
| Integration Revenue | TBD - Calculate from V17.1 with V18 fees |
| New Business Revenue | TBD - Calculate from V17.1 with V18 fees |
| **Total Potential** | **TBD - Estimated $6.0B-$6.6B** |

**Baseline Comparison:**
- V15: 17,434 facilities, $5.24B Total Potential
- V18: 21,023 facilities (+20.6%), expected $6.0B-$6.6B

---

## 5. Reporting Layer

This section defines the filters and constructs used in the Comprehensive Report Workbook.

### 5.1 Market Definitions

| Market | States |
|--------|--------|
| Existing | IN, KY, NC, OH, SC, VA |
| Priority Expansion | IA, MN, IL, MI, PA, WI, MT |
| Emerging | FL, GA |
| Exiting | WV |
| National | All other states |

### 5.2 Ownership Classification

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

### 5.3 Barrier Application

Barriers indicate facilities where potential revenue cannot be realized. All barriers result in:
- Current Revenue: **Unchanged**
- Integration Potential Revenue: **$0**
- New Business Potential Revenue: **$0**
- Total Potential Revenue: **$0**

#### Barrier Types

| Type | Facilities (V15) |
|------|------------------|
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

**Note:** V18 barrier counts to be verified in V17.1 database.

**Propagation Rule:** If one facility under a corporate entity has a barrier, all facilities under that entity should have the same barrier.

### 5.4 TAM/SAM/SOM Construct

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

## 6. Comprehensive Report Outputs

This section describes the structure and methodology for generating the Comprehensive_Report_Workbook.xlsx.

### 6.1 General Methodology

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

### 6.2 Sheet: TAM SAM SOM Facilities

**Tables 1-3: Facility Counts**

| Table | Source Type Filter | Output Format |
|-------|-------------------|---------------|
| Table 1 | SNF only | Facility counts |
| Table 2 | ALF only | Facility counts |
| Table 3 | All (SNF + ALF) | Facility counts |

**Methodology:**
1. Filter by Source_Type (SNF/ALF/All)
2. Group by TAM/SAM/SOM segment (apply filters from Section 5.4 - **Facility Count Tables**)
3. Cross-tabulate by Ownership_Type (Corporate / Independent / Total)
4. Display as "Total / Our Share" format (e.g., "10,065 / 462")
   - Total = count of facilities
   - Our Share = count where Do_We_Serve = "Yes"

**V15 Note:** SAM and SOM rows include BOTH Corporate AND Independent facilities that meet the geographic and barrier criteria.

### 6.3 Sheet: TAM SAM SOM Revenue

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
2. Group by TAM/SAM/SOM segment (apply filters from Section 5.4 - **Revenue Tables**)
3. Sum revenue columns: Current, Integration, New Biz, Total Potential
4. For range tables, calculate min (S1) and max (S3) for display

**Columns:**
- Current Revenue
- Potential Integration
- Potential New Biz
- Total Potential

### 6.4 Sheet: Fee Structure SOM

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

### 6.5 Sheet: Top Corporate Rankings

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

### 6.6 Sheet: State Analysis

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

## 7. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| **V18.0** | Nov 2025 | V17.1 database (21,023 facilities), updated fee structure, Section 2 Combined Database documentation |
| V15.0 | Nov 2025 | Tables 1-3 include Independent in SAM/SOM; Tables 16-18 exclude INDEPENDENT |
| V14.0 | Nov 2025 | Updated fee structure with walked-out math, corrected scenario definitions |
| V13.0 | Nov 2025 | Consolidated barrier columns, restructured rulebook with System Overview |
| V12.0 | Nov 2025 | Correct file formats, Integrated Barrier calculations |
| V11.0 | Nov 2025 | Integrated Barrier propagation (formatting errors) |
| V10.0 | Nov 2025 | ALF fees corrected, QC validation added |

---

**END OF RULEBOOK**

*This document is the authoritative reference. Deviations require written authorization.*
