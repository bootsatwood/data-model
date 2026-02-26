# Comprehensive Report Compendium V19.1
## Tables 1-25 Methodology & Validation

**Version**: 19.1  
**Date**: November 2025  
**Status**: PRODUCTION READY  
**Prerequisite**: Core Rulebook V19.1 QC Protocol must pass before using this compendium

---

## Document Purpose

This compendium documents the Comprehensive Report Workbook (Tables 1-25), which provides TAM/SAM/SOM analysis, corporate rankings, and state-level revenue breakdowns.

**Source Data:** Economic Model Scenarios (S1, S2, S3)  
**Primary Output:** Comprehensive_Report_Workbook_Vxx.xlsx

---

## 1. Report Overview

### 1.1 Report Structure

| Sheet | Tables | Content |
|-------|--------|---------|
| TAM SAM SOM Facilities | 1-3 | Facility counts by segment |
| TAM SAM SOM Revenue | 4-9 | Revenue by segment (point values + ranges) |
| Fee Structure SOM | 10-15 | SOM revenue by service component |
| Top Corporate Rankings | 16-18, 25 | Corporate chain rankings |
| State Analysis | 19-24 | Revenue by state and market |

### 1.2 Scenario Selection for Point Values

**CRITICAL:** Point value tables use **Scenario 2** (market baseline), NOT Scenario 1.

| Table Type | Scenario Used |
|------------|---------------|
| Tables 4-6 (TAM/SAM/SOM Revenue) | **S2** |
| Tables 10-12 (Fee Structure SOM) | **S2** |
| Tables 16-18, 25 (Corporate Rankings) | **S2** |
| Tables 19-21 (State Analysis) | **S2** |
| Range Tables (7-9, 13-15, 22-24) | S1-S3 range |

**Rationale:** S2 represents the most realistic middle-ground projection for business planning.

---

## 2. Market Definitions

### 2.1 Market Classification

| Market | States | Purpose |
|--------|--------|---------|
| Existing | IN, KY, NC, OH, SC, VA | Current operational footprint |
| Priority Expansion | IA, MN, IL, MI, PA, WI, MT | Near-term growth targets |
| Emerging | FL, GA | Future opportunity markets |
| Exiting | WV | Discontinued market |
| National | All other states | Background/context |

### 2.2 TAM/SAM/SOM Construct

**IMPORTANT:** Different tables use different filter rules.

#### Revenue Tables (Tables 4-9, 10-15, 16-18, 19-24, 25)

| Segment | Markets | Source Type | Ownership Type | Barriers |
|---------|---------|-------------|----------------|----------|
| TAM | All Markets | ALF + SNF | Corporate + Independent | No filter |
| SAM | Existing + Priority | ALF + SNF | **Corporate only** | Minus barriers |
| SOM | Existing only | ALF + SNF | **Corporate only** | Minus barriers |

#### Facility Count Tables (Tables 1-3)

| Segment | Markets | Source Type | Ownership Type | Barriers |
|---------|---------|-------------|----------------|----------|
| TAM | All Markets | ALF + SNF | Corporate + Independent | No filter |
| SAM | Existing + Priority | ALF + SNF | **Corporate + Independent** | Minus barriers |
| SOM | Existing only | ALF + SNF | **Corporate + Independent** | Minus barriers |

**Rationale:** Tables 1-3 display facility counts by ownership type. Excluding Independent facilities from SAM/SOM would show misleading zeros in the Independent column.

---

## 3. Tables 1-3: Facility Counts

### 3.1 Purpose
Display facility counts by TAM/SAM/SOM segment, cross-tabulated by ownership type.

### 3.2 Table Definitions

| Table | Source Type Filter |
|-------|-------------------|
| Table 1 | SNF only |
| Table 2 | ALF only |
| Table 3 | All (SNF + ALF) |

### 3.3 Output Format

Display as "Total / Our Share" format:
- **Total** = count of facilities meeting segment criteria
- **Our Share** = count where Do_We_Serve = "Yes"

Example: "10,065 / 462" means 10,065 total facilities, 462 served

### 3.4 Column Structure

| Column | Content |
|--------|---------|
| Segment | TAM / SAM / SOM |
| Corporate | Count / Served |
| Independent | Count / Served |
| Total | Count / Served |

### 3.5 Methodology

1. Filter by Source_Type (SNF/ALF/All)
2. Group by TAM/SAM/SOM segment (apply Facility Count Table filters from Section 2.2)
3. Cross-tabulate by Ownership_Type
4. Count total facilities and served facilities per cell

---

## 4. Tables 4-9: TAM/SAM/SOM Revenue

### 4.1 Purpose
Display revenue by TAM/SAM/SOM segment for each facility type.

### 4.2 Table Definitions

| Table | Source Type | Values |
|-------|-------------|--------|
| Table 4 | SNF | **S2 point values** |
| Table 5 | ALF | **S2 point values** |
| Table 6 | Total | **S2 point values** |
| Table 7 | SNF | S1-S3 ranges |
| Table 8 | ALF | S1-S3 ranges |
| Table 9 | Total | S1-S3 ranges |

### 4.3 Column Structure

| Column | Content |
|--------|---------|
| Segment | TAM / SAM / SOM |
| Current Revenue | Revenue from served facilities |
| Potential Integration | Integration opportunity |
| Potential New Biz | New business opportunity |
| Total Potential | Integration + New Biz |

### 4.4 Range Display Format

For Tables 7-9, display as "S1 - S3" format:
- Example: "$41M - $49M"

### 4.5 Methodology

1. Filter by Source_Type
2. Group by TAM/SAM/SOM segment (apply Revenue Table filters from Section 2.2)
3. Sum revenue columns
4. For range tables, calculate min (S1) and max (S3)

---

## 5. Tables 10-15: Fee Structure SOM (Service Breakdown)

### 5.1 Purpose
Show SOM revenue broken down by **service component** (PCP, MH, CCM, SS).

**CRITICAL:** This is a SERVICE BREAKDOWN, NOT a state or geographic breakdown.

### 5.2 Table Definitions

| Table | Source Type | Values |
|-------|-------------|--------|
| Table 10 | SNF | **S2 point values** |
| Table 11 | ALF | **S2 point values** |
| Table 12 | Total | **S2 point values** |
| Table 13 | SNF | S1-S3 ranges |
| Table 14 | ALF | S1-S3 ranges |
| Table 15 | Total | S1-S3 ranges |

### 5.3 Column Structure

| Column | Content |
|--------|---------|
| Revenue Type | Current / Integration / New Biz / Total Potential |
| PCP ($) | PCP revenue component |
| PCP (%) | PCP percentage of row total |
| MH ($) | MH revenue component |
| MH (%) | MH percentage of row total |
| CCM ($) | CCM revenue component |
| CCM (%) | CCM percentage of row total |
| SS ($) | Shared Savings revenue component |

### 5.4 Row Structure

| Row | Definition |
|-----|------------|
| Current Revenue | Revenue from currently served facilities |
| Integration Revenue | Cross-sell opportunity at served facilities |
| New Business Revenue | Revenue from unserved facilities |
| Total Potential | Integration + New Business |

### 5.5 Example Layout

```
Table 10: SNF SOM Service Breakdown (S2)
                  PCP           MH          CCM         SS
                  $      %      $     %     $     %     $
Current       $50MM  60.3%  $20MM 24.1% $3MM  3.6%  $10MM
Integration   $45MM  60.3%  $18MM 24.1% $3MM  3.6%  $9MM
New Biz       $300MM 60.3% $120MM 24.1% $15MM 3.6%  $60MM
Total Pot.    $345MM 60.3% $138MM 24.1% $18MM 3.6%  $69MM
```

### 5.6 Methodology

1. Filter to SOM segment (Existing markets, Corporate only, minus barriers)
2. Filter by Source_Type
3. Analyze service mix across facilities (PCP Only, MH Only, Integrated)
4. Allocate revenue to PCP, MH, CCM, SS components based on service configuration
5. Calculate percentage distribution per row
6. Present as Current/Integration/New Biz/Total Potential rows

---

## 6. Tables 16-18, 25: Corporate Rankings

### 6.1 Purpose
Rank corporate entities (chains) by revenue opportunity within SOM segment.

### 6.2 Table Definitions

| Table | Ranking Metric | Count |
|-------|----------------|-------|
| Table 16 | Total Opportunity | Top 20 |
| Table 17 | Integration Opportunity | Top 20 |
| Table 18 | New Business Opportunity | Top 20 |
| Table 25 | Total Opportunity | Top 60 |

### 6.3 Filter Criteria

**Segment:** SOM (Existing markets, Corporate only, no barriers)  
**Scenario:** S2 (market baseline)

**CRITICAL:** Independent facilities are EXCLUDED from rankings. "Independent" is not a corporate entity and cannot be meaningfully compared to corporate chains.

### 6.4 Column Structure

| Column | Content |
|--------|---------|
| Rank | 1, 2, 3... |
| Corporate Name | Parent company name |
| Total Facilities | Count of facilities in chain |
| Facilities We Serve | Count where Do_We_Serve = "Yes" |
| Current Revenue | S2 Current Revenue |
| Integration Opp | S2 Integration Revenue |
| New Biz Opp | S2 New Business Revenue |
| Total Opportunity | Integration + New Biz |

### 6.5 Methodology

1. Apply SOM filters (Existing markets, Corporate only, no barriers)
2. Group by Corporate_Name
3. For each corporate entity, aggregate:
   - Facility counts (total and served)
   - Revenue columns from S2
4. Rank by specified metric (descending)
5. Take top N records
6. Add TOTAL row at bottom

---

## 7. Tables 19-24: State Analysis

### 7.1 Purpose
Display revenue by state within market classification hierarchy.

### 7.2 Table Definitions

| Table | Source Type | Values |
|-------|-------------|--------|
| Table 19 | SNF | **S2 point values** |
| Table 20 | ALF | **S2 point values** |
| Table 21 | Total | **S2 point values** |
| Table 22 | SNF | S1-S3 ranges |
| Table 23 | ALF | S1-S3 ranges |
| Table 24 | Total | S1-S3 ranges |

### 7.3 Column Structure

| Column | Content |
|--------|---------|
| Market | Existing / Priority / Emerging / Exiting / National |
| State(s) | State abbreviation(s) |
| Total Facilities | Count of facilities |
| Facilities Served | Count where Do_We_Serve = "Yes" |
| Current Revenue | S2 Current Revenue |
| Potential Rev. Integration | S2 Integration Revenue |
| Potential Rev. New Biz | S2 New Business Revenue |
| Total Potential Revenue | Integration + New Biz |

### 7.4 Row Organization

| Market Type | Row Treatment |
|-------------|---------------|
| Existing | One row per state (IN, KY, NC, OH, SC, VA separately) |
| Priority | Combined or individual rows |
| Emerging | Combined row (FL, GA) |
| Exiting | Single row (WV) |
| National | Combined row (all other states) |

### 7.5 Methodology

1. Filter by Source_Type
2. Group by Market → State
3. For each state/market, aggregate:
   - Facility counts
   - Revenue columns from S2
4. Order by Market hierarchy (Existing first, then Priority, Emerging, Exiting, National)
5. Within Existing market, list each state separately

---

## 8. Report QC Validation Protocol

**PREREQUISITE:** Core Rulebook V19.1 QC Protocol must pass before running this protocol.

### 8.1 Pre-Validation Checklist

| Check | Criteria | Status |
|-------|----------|--------|
| Core QC Passed | Core Rulebook Section 6 sign-off complete | ☐ |
| Scenario files available | All 3 scenario files accessible | ☐ |
| Report file generated | Comprehensive_Report_Workbook_Vxx.xlsx exists | ☐ |

### 8.2 Facility Count Validation (Tables 1-3)

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| Table 3 TAM Total = Database Total | 20,943 | _____ | ☐ |
| Table 1 TAM + Table 2 TAM = Table 3 TAM | True | _____ | ☐ |
| Corporate + Independent = Total (each row) | True | _____ | ☐ |
| Served counts ≤ Total counts | True | _____ | ☐ |

### 8.3 Revenue Reconciliation (Tables 4-9)

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| Table 6 TAM Current = S2 Total Current | ~$182.4M | _____ | ☐ |
| Table 6 TAM Total Potential = S2 Total Potential | ~$7,060.6M | _____ | ☐ |
| Table 4 + Table 5 = Table 6 (each cell) | True | _____ | ☐ |
| SAM Current ≤ TAM Current | True | _____ | ☐ |
| SOM Current ≤ SAM Current | True | _____ | ☐ |

### 8.4 Fee Structure SOM Validation (Tables 10-15)

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| PCP% + MH% + CCM% + SS% ≈ 100% per row | True | _____ | ☐ |
| Row totals match Tables 4-6 SOM values | True | _____ | ☐ |
| Service breakdown uses S2 for point values | True | _____ | ☐ |

### 8.5 Corporate Rankings Validation (Tables 16-18, 25)

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| No "INDEPENDENT" in rankings | True | _____ | ☐ |
| Ranking order matches metric (descending) | True | _____ | ☐ |
| TOTAL row = sum of ranked entities | True | _____ | ☐ |
| Table 16 top entity appears in Table 25 | True | _____ | ☐ |

### 8.6 State Analysis Validation (Tables 19-24)

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| All 6 Existing states present | IN, KY, NC, OH, SC, VA | _____ | ☐ |
| State totals sum to report totals | True | _____ | ☐ |
| No duplicate states across markets | True | _____ | ☐ |

### 8.7 Cross-Table Consistency

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| Table 3 SOM served = Sum of Table 16-18 served | True | _____ | ☐ |
| Table 6 SOM revenue = Table 12 Total Potential row | True | _____ | ☐ |
| State analysis totals reconcile to segment totals | True | _____ | ☐ |

### 8.8 Sign-Off Criteria

**All checks must pass before report delivery.**

| Gate | Requirement | Status |
|------|-------------|--------|
| Facility Count Gate | All Section 8.2 checks pass | ☐ |
| Revenue Gate | All Section 8.3 checks pass | ☐ |
| Service Breakdown Gate | All Section 8.4 checks pass | ☐ |
| Rankings Gate | All Section 8.5 checks pass | ☐ |
| State Analysis Gate | All Section 8.6 checks pass | ☐ |
| Consistency Gate | All Section 8.7 checks pass | ☐ |

**Sign-Off:**

- Validated By: _________________
- Date: _________________
- Version: V19.1
- Report Ready for Delivery: ☐ Yes ☐ No

---

## 9. Known Limitations & Notes

### 9.1 Filter Differences

Tables 1-3 (facility counts) use different ownership filters than revenue tables. This is intentional - see Section 2.2 for rationale.

### 9.2 Scenario Selection

Point value tables use S2, not S1. This differs from some earlier documentation versions. S2 represents the market baseline and is preferred for business planning.

### 9.3 Fee Structure SOM Naming

Despite the name "Fee Structure SOM," Tables 10-15 show SERVICE BREAKDOWN, not fee structure details. The name is historical.

### 9.4 Independent Exclusion in Rankings

Independent facilities are excluded from Tables 16-18 and 25. To analyze Independent facility opportunity, use Tables 1-3 facility counts or create a custom analysis.

---

## 10. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| **V19.1** | Nov 2025 | Initial Report Compendium; extracted from monolithic rulebook; added embedded QC protocol; documented S2 usage for point values; clarified Fee Structure SOM as service breakdown |

---

**END OF COMPREHENSIVE REPORT COMPENDIUM**

*This compendium documents the Comprehensive Report Workbook (Tables 1-25). For database, fee structure, and scenario methodology, see Core Rulebook V19.1.*

*Deviations require written authorization.*
