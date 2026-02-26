# Integration Momentum Slide - V19 Methodology Notes

**Date**: November 24, 2025  
**Source Data**: Economic_Model_Scenario_2_Combined_V19_1.xlsx (20,943 facilities)  
**Output**: Integration_Momentum_Slide1_V19.xlsx

---

## Purpose

This document describes how the V19 data refresh differs from the original slide and explains the methodology used to match facilities and calculate revenue.

---

## Original Slide vs V19 Refresh

### What the Original Slide Showed

The original "Integration Momentum" slide displayed 25 handpicked facilities representing the active integration pipeline - facilities being converted from single-service (PCP-only or MH-only) to fully integrated (both PCP and MH services).

**Original columns:**
- Facility Name
- MUO (Multi-Unit Operator / Corporate Entity)
- State
- SNF or ALF

### What the V19 Refresh Adds

**New column:**
- **Current Revenue** - Annual revenue from Scenario 2 calculations

---

## Methodology

### Data Source

Revenue data pulled from `Economic_Model_Scenario_2_Combined_V19_1.xlsx`, which contains:
- All 20,943 facilities in the database
- Scenario 2 (Market Expansion +10%) fee calculations
- Current_Revenue, Integration_Revenue, New_Business_Revenue columns

### Facility Matching Process

Each of the 25 slide facilities was matched to the V19 database using:
1. **Exact name match** with state filter
2. **Partial name match** (first word) with state and facility type filter
3. **Corporate name search** when direct matching failed
4. **Manual verification** for ambiguous matches

### Revenue Calculation

**For most facilities:**
- Current Revenue = `Current_Revenue` column from Scenario 2

**For two facilities still showing as single-service in database:**
- Good Shepherd H/R Center
- Matthews H/R

These facilities were calculated at **fully integrated revenue** by summing:
- Current_Revenue + Integration_Revenue

This assumes they have now completed integration, consistent with their inclusion in the "Integration Momentum" pipeline.

---

## Data Corrections

### State Corrections

Two facilities had incorrect states in the original slide. These were corrected based on V19 database matching:

| Facility | Original State | Corrected State | Notes |
|----------|----------------|-----------------|-------|
| Carmel Manor | OH | **KY** | Matched to CARMEL MANOR in Fort Thomas, KY |
| Dominion Sr Living of Florence | SC | **KY** | Matched to DOMINION SENIOR LIVING OF FLORENCE in KY |

**These cells are highlighted in yellow in the Excel output.**

### MUO Standardization

Facilities marked as "N" (indicating no corporate parent) in the original slide were changed to **"Independent"** for clarity.

---

## Facilities Not Found or Zero Revenue

During initial matching, some facilities showed $0 revenue due to:
1. **Duplicate facility names** across states (e.g., Lakeside H/R exists in both IL and NC)
2. **Name variations** (e.g., "McMormick" vs "McCormick's Creek")
3. **State mismatches** requiring correction

All 25 facilities were successfully matched after corrections.

---

## Integration Revenue Discussion

### Why Integration Revenue Column Was Removed

The original analysis included an "Integration Revenue" column to show potential revenue from completing integration. However:

**Issue discovered:** Many facilities on the pipeline list are already marked as `Integrated_Flag = Yes` in the V19 database, meaning:
- They have already completed integration
- Their Integration_Revenue = $0 (nothing left to add)
- This is a **timing issue** - the database reflects current state, not historical pipeline status

**Resolution:** The Integration Revenue column was removed since:
- We cannot determine pre-integration state from current data
- Showing $0 for completed integrations would be misleading
- Current Revenue at fully integrated level tells the success story

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Table 1 Facilities | 14 |
| Table 1 Subtotal | $4,886,224 |
| Table 2 Facilities | 11 |
| Table 2 Subtotal | $2,084,536 |
| **Grand Total (25 facilities)** | **$6,970,760** |

---

## Files Delivered

1. **Integration_Momentum_Slide1_V19.xlsx** - Excel workbook with formatted tables
2. **Integration_Momentum_Methodology_V19.md** - This methodology document

---

## Recommendations for Future Updates

1. **Add timestamp flags** to database indicating when facilities completed integration
2. **Capture pre/post revenue** at time of integration conversion
3. **Maintain pipeline list** separate from integration status flags
4. **Verify state data** in source systems when onboarding new facilities

---

**Document Version**: 1.0  
**Generated**: November 24, 2025
