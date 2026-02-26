# Final Model Rulebook V18.1
## Healthcare Facility Database Revenue Model - Authoritative Reference

**Version**: 18.1  
**Date**: November 22, 2025  
**Status**: PRODUCTION READY

---

## Executive Summary

This rulebook defines the authoritative fee structures, calculation methodologies, and governance controls for the Eventus Healthcare Economic Model. All revenue calculations must conform to the specifications in this document.

**V18.1 NOTE**: This version implements database cleanup (NULL service flags → 'No'), SABER barrier removal (159 facilities), and "unknown" entity reclassification (121 facilities to Independent). All files use V17.1 database foundation (21,023 facilities).

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

### 4.8 V18.1 Key Metrics

**Database:** V17.1 (21,023 facilities: 15,234 SNF + 5,789 ALF)

| Metric | V18.1 Value |
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
| **Total Potential** | **$8,292.4M** |

**Baseline Comparison:**
- V18.0: 21,023 facilities, $7.63B Total Potential (S2)
- V18.1: 21,023 facilities, $7.68B Total Potential (S2)
- Change: +$54M (+0.7%) due to SABER barrier removal

---

## 5. Reporting Layer

[Content unchanged from V18.0 - Sections 5.1-5.4]

---

## 6. Comprehensive Report Outputs

[Content unchanged from V18.0 - Sections 6.1-6.6]

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
| **V18.1** | Nov 2025 | Service flag cleanup (NULL → 'No'), SABER barrier removal (159 facilities), "unknown" reclassification (121 facilities), Scenario 2 as baseline for single-value tables |
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

**END OF RULEBOOK**

*This document is the authoritative reference. Deviations require written authorization.*
