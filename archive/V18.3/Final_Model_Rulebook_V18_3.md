# Final Model Rulebook V18.3
## Healthcare Facility Database Revenue Model - Authoritative Reference

**Version**: 18.3  
**Date**: November 22, 2025  
**Status**: PRODUCTION READY

---

## Executive Summary

This rulebook defines the authoritative fee structures, calculation methodologies, and governance controls for the Eventus Healthcare Economic Model. All revenue calculations must conform to the specifications in this document.

**V18.3 NOTE**: This version corrects Comprehensive Report Workbook issues (SAM calculations, Tables 22-24 population). No changes to fees, database, or core calculations. Database and scenarios remain at V18.1 specifications.

**V18.1 Changes from V18.0:**
- **Service Flag Cleanup**: 377 served facilities had NULL values replaced with explicit 'No' values
- **SABER Healthcare Group**: Competitor Contract barrier removed (159 facilities now addressable)
- **"unknown" Entity**: Reclassified from Corporate to Independent (121 facilities)
- **Current Revenue**: Restored to $202.4M (S2) from incorrect $162.0M in first V18.1 attempt

**V17.1 Database Foundation:**
- 8-state Eventus WholeHealth integration (+3,589 facilities from V15's 17,434)
- Consistent count-based ownership classification applied to all facilities
- 2,327 facilities reclassified (11.1%): single-facility LLCs corrected to Independent
- GPS-based deduplication and corporate name harmonization
- 1,743 facilities currently served

---

## 1. System Overview & Governance

[Content unchanged from V18.0 - See Sections 1.1-1.6]

---

## 2. Combined Database

### 2.1 Database Architecture Flow

[Content unchanged from V18.0]

### 2.2 Source File Evolution

[Content unchanged from V18.0]

### 2.3 Ownership Classification

**Column to Use:** `Ownership_Type`

**V18.1 Update:** 121 facilities reclassified from Corporate to Independent due to Corporate_Name = "unknown"

#### Four-Rule Count-Based Hierarchy

[Rules 1-4 unchanged from V18.0]

**V18.1 Counts:**
- Corporate: 11,932 facilities (-121 from V18.0)
- Independent: 9,091 facilities (+121 from V18.0)
- Corporate Chains: 1,025 (-1 "unknown" pseudo-entity)

### 2.4 Facility Type Classification

[Content unchanged from V18.0]

### 2.5 Service Status

[Content unchanged from V18.0]

### 2.6 Service Flags

**V18.1 CRITICAL UPDATE:** All NULL values in service flags have been replaced with explicit 'No' values.

| Column | Values | Definition |
|--------|--------|------------|
| `Integrated_Flag` | Yes/No | Facility receives both PCP and MH services |
| `PCP_Flag` | Yes/No | Facility receives PCP services |
| `MH_Flag` | Yes/No | Facility receives MH services |

**Service Configuration Rules:**
- Integrated_Flag = Yes → PCP_Flag = Yes AND MH_Flag = Yes
- PCP_Flag = Yes, MH_Flag = No → PCP-only facility
- MH_Flag = Yes, PCP_Flag = No → MH-only facility
- All flags = No → Not served

**V18.1 Data Quality Standard:**
- **ALL service flags MUST have explicit 'Yes' or 'No' values**
- **NULL values are NOT permitted**
- **This prevents revenue calculation errors**

**V18.1 Cleanup Impact:**
- Integrated_Flag: 19,657 NULL → 'No'
- PCP_Flag: 19,769 NULL → 'No'
- MH_Flag: 19,537 NULL → 'No'
- **Critical for 377 served facilities:** Restored ~$40M in Current Revenue calculations

---

## 3. Fee Structure - AUTHORITATIVE VALUES

[Content unchanged from V18.0 - Sections 3.1-3.3]

---

## 4. Revenue Calculations

[Content unchanged from V18.0 - Sections 4.1-4.7]

### 4.8 V18.3 Key Metrics

**Database:** V17.1 (21,023 facilities: 15,234 SNF + 5,789 ALF)

| Metric | V18.3 Value |
|--------|-------------|
| **Scenario 1 (Conservative)** | |
| Current Revenue | $173.1M |
| Integration Revenue | $146.0M |
| New Business Revenue | $6,847.6M |
| **Total Potential** | **$6,993.6M** |
| | |
| **Scenario 2 (Market +10%)** | |
| Current Revenue | $202.4M |
| Integration Revenue | $151.1M |
| New Business Revenue | $7,532.3M |
| **Total Potential** | **$7,683.4M** |
| | |
| **Scenario 3 (Premium +20%)** | |
| Current Revenue | $227.7M |
| Integration Revenue | $159.9M |
| New Business Revenue | $8,217.1M |
| **Total Potential** | **$8,377.0M** |

**SAM Segment Metrics (S2):**
- SAM Total: $1,709.2M (corrected from $1,607.9M in early V18.3 draft)
- SAM SNF: $1,308.1M 
- SAM ALF: $401.0M

**Baseline Comparison:**
- V18.0: 21,023 facilities, $7.63B Total Potential (S2)
- V18.3: 21,023 facilities, $7.68B Total Potential (S2)
- Change: +$54M (+0.7%) due to SABER barrier removal

---

## 5. Reporting Layer

[Content unchanged from V18.0 - Sections 5.1-5.4]

---

## 6. Comprehensive Report Outputs

This section describes the structure and methodology for generating the Comprehensive_Report_Workbook.xlsx.

### 6.1 General Methodology

**Data Source:** All tables pull from Economic_Model_Scenario files (S2 for single values, S1-S3 for ranges).

**V18.3 Critical Implementation Notes:**
- **ALWAYS** pull fresh data from Economic Model Scenario files
- **NEVER** copy values from previous report versions  
- **VERIFY** SAM filters are correctly applied (Corporate-only for revenue)

**Standard Columns for Revenue Tables:**
- Current Revenue
- Potential Rev. Integration
- Potential Rev. New Biz
- Total Potential Revenue

**Range Calculations:** For tables showing ranges, display format is "S1 - S3" (e.g., "$41M - $49M").

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

**CRITICAL:** SAM and SOM include BOTH Corporate AND Independent facilities for facility count tables.

### 6.3 Sheet: TAM SAM SOM Revenue  

**Tables 4-9: Revenue by Segment**

| Table | Source Type | Values |
|-------|-------------|--------|
| Table 4 | SNF | S2 point values |
| Table 5 | ALF | S2 point values |
| Table 6 | Total | S2 point values |
| Table 7 | SNF | S1-S3 ranges |
| Table 8 | ALF | S1-S3 ranges |
| Table 9 | Total | S1-S3 ranges |

**CRITICAL Filter Difference:**
- TAM: All facilities (Corporate + Independent)
- SAM: **Corporate only**, Existing + Priority states, no barriers
- SOM: **Corporate only**, Existing states only, no barriers

### 6.4-6.6 [Other sections unchanged]

**V18.1 Update:** All single-value tables now use Scenario 2 data (not Scenario 1)

**Tables Using Scenario 2:**
- Tables 1-6: Facility counts and revenue by segment
- Tables 10-12: Fee Structure SOM detail
- Tables 16-18, 25: Corporate Rankings
- Tables 19-21: State Analysis

**Tables Using S1-S3 Ranges:**
- Tables 7-9: Revenue ranges
- Tables 13-15: Fee Structure ranges
- Tables 22-24: State Analysis ranges

---

## 7. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| **V18.3** | Nov 2025 | Comprehensive Report corrections: SAM segment calculations fixed, Tables 22-24 populated with state ranges. No changes to fees, database, or calculation methodologies |
| V18.1 | Nov 2025 | Service flag cleanup (NULL → 'No'), SABER barrier removal (159 facilities), "unknown" reclassification (121 facilities), Scenario 2 as baseline for single-value tables |
| V18.0 | Nov 2025 | V17.1 database (21,023 facilities), updated fee structure, Section 2 Combined Database documentation |
| V15.0 | Nov 2025 | Tables 1-3 include Independent in SAM/SOM; Tables 16-18 exclude INDEPENDENT |
| V14.0 | Nov 2025 | Updated fee structure with walked-out math, corrected scenario definitions |
| V13.0 | Nov 2025 | Consolidated barrier columns, restructured rulebook with System Overview |
| V12.0 | Nov 2025 | Correct file formats, Integrated Barrier calculations |
| V11.0 | Nov 2025 | Integrated Barrier propagation (formatting errors) |
| V10.0 | Nov 2025 | ALF fees corrected, QC validation added |

---

## 8. V18.1 Specific Guidance

### 8.1 Service Flag Data Quality

**Problem Identified:** V18.0 contained NULL values in service flags, causing revenue calculation errors.

**Solution Applied:** All NULL values replaced with explicit 'No' values per Rulebook Section 2.6.

**Impact:**
- 377 served facilities affected
- $40M in Current Revenue restored (S2)
- Revenue calculations now match historical baselines

**Prevention:** Data ingestion processes must ensure service flags always have explicit 'Yes'/'No' values.

### 8.2 SABER Healthcare Group

**Status Change:** Barriers removed in V18.1

**Previous State (V18.0):**
- Barrier: "Competitor Contract"
- Total Potential Revenue: $0 (blocked)

**Current State (V18.1):**
- Barrier: None
- Total Potential Revenue: $54.0M (S2)
- 159 facilities (60 served, 99 addressable)
- Now appears in Top Corporate Rankings

**Authorization:** Brooke phone call, November 21, 2025

### 8.3 "unknown" Entity Reclassification

**Issue:** 121 facilities had Corporate_Name = "unknown"

**Resolution:** 
- Corporate_Name changed to "" (blank)
- Ownership_Type changed from "Corporate" to "Independent"
- Facilities now correctly classified per Rule 1 (Blank Corporate Name → Independent)

**Impact:**
- Corporate count: 12,053 → 11,932
- Independent count: 8,970 → 9,091
- "unknown" removed from Corporate Rankings
- Revenue redistributed to Independent segment

---

## 9. Common Errors and Prevention

### 9.1 Comprehensive Report Generation Errors

**Error**: SAM segment showing incorrect values  
**Cause**: Not applying Corporate-only filter for revenue tables  
**Prevention**: Use separate filter functions for revenue vs facility tables

**Error**: Tables 22-24 empty  
**Cause**: Missing state-by-state range calculation logic  
**Prevention**: Ensure all 6 table sets (19-24) have complete state iteration

**Error**: Facility counts not matching database  
**Cause**: Incorrect filter application or row shifting  
**Prevention**: Verify counts against Economic Model Scenarios before finalizing

### 9.2 Data Quality Checks

Before delivering any Comprehensive Report:
1. Sum of TAM Current Revenue must equal Economic Model Scenario total
2. SAM values must be less than TAM values  
3. SOM values must be less than or equal to SAM values
4. Tables 22-24 must have visible revenue ranges
5. No cells should display #REF!, #VALUE!, or other Excel errors

### 9.3 Version-Specific Validations

**V18.3 Specific Checks:**
- SAM Total New Business (S2): Must equal ~$1,595.6M
- Tables 22-24: Must contain state-by-state ranges
- SABER Healthcare: Must appear in corporate rankings
- Total facilities: Must equal 21,023

---

**END OF RULEBOOK**

*This document is the authoritative reference. Deviations require written authorization.*
