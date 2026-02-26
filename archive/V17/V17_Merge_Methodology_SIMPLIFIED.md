# V17 Merge Methodology - SIMPLIFIED (No New Columns)
## Eventus Healthcare Economic Model V17

**Date**: November 20, 2025  
**Critical Change**: NO NEW COLUMNS - V17 maintains exact V16 structure

---

## EXECUTIVE SUMMARY

✅ **V17 = V16 structure (23 columns) + NEW facilities only**  
✅ **NO new columns from Eventus**  
✅ **Simple additive merge: 17,434 + ~2,709 = ~20,143 facilities**

---

## 1. REVISED MERGE METHODOLOGY

### Core Principle: Same Columns, More Facilities

```
V16: 17,434 facilities × 23 columns
       ↓
     (unchanged)
       ↓
Eventus: 23,142 facilities
       ↓
  GPS Match → Identify ~2,709 NEW facilities
       ↓
  Extract only the ~2,709 NEW
       ↓
  Map to V16's 23 columns
       ↓
V17: ~20,143 facilities × 23 columns (SAME AS V16)
```

---

## 2. V17 COLUMN STRUCTURE (23 Columns - UNCHANGED)

| # | Column Name | Source | Notes |
|---|-------------|--------|-------|
| 1 | Source_Type | V16 / Calculated | SNF or ALF |
| 2 | Facility_Name | V16 / Eventus | Facility name |
| 3 | Corporate_Name | V16 / NULL | NULL for new facilities |
| 4 | Address | V16 / Eventus | Street address |
| 5 | City | V16 / Eventus | City name |
| 6 | State | V16 / Eventus | State abbreviation |
| 7 | ZIP | V16 / Eventus | Zip code |
| 8 | County | V16 / Eventus | County name |
| 9 | Ownership_Type | V16 / Calculated | Corporate or Independent |
| 10 | Total_Beds | V16 / Eventus | From "Total Units" |
| 11 | Census | V16 / Calculated | Total_Beds × 0.80 for new |
| 12 | Do_We_Serve | V16 / "No" | "No" for all new facilities |
| 13 | Integrated_Flag | V16 / NULL | NULL for new facilities |
| 14 | PCP_Flag | V16 / NULL | NULL for new facilities |
| 15 | MH_Flag | V16 / NULL | NULL for new facilities |
| 16 | Barrier | V16 / NULL | NULL for new facilities |
| 17 | Latitude | V16 / Eventus | GPS latitude |
| 18 | Longitude | V16 / Eventus | GPS longitude |
| 19 | Data_Quality_Flag | V16 / Calculated | Check for issues |
| 20 | Contract_Status | V16 / "GREEN" | "GREEN" for new prospects |
| 21 | Geographic_Tier | V16 / Calculated | Calculate for all |
| 22 | Integration_Eligible | V16 / Calculated | Recalculate for all |
| 23 | New_Business_Eligible | V16 / Calculated | Recalculate for all |

**NO COLUMN 24+** - V17 stops at column 23, just like V16

---

## 3. EVENTUS TO V16 COLUMN MAPPING

### For the ~2,709 NEW Facilities Only

| V16 Column # | V16 Column Name | Eventus Source Column | Transformation |
|--------------|-----------------|----------------------|----------------|
| 1 | Source_Type | NC/AL/MC/IL Open Units | **Calculate**: NC ≥ 50% = SNF; else ALF |
| 2 | Facility_Name | Building Name | Direct copy |
| 3 | Corporate_Name | *(none)* | **NULL** |
| 4 | Address | Address | Direct copy |
| 5 | City | City | Direct copy |
| 6 | State | State | Direct copy |
| 7 | ZIP | Zip | Convert to text |
| 8 | County | County/Equiv | Direct copy |
| 9 | Ownership_Type | Owner Name | **Calculate** from pattern |
| 10 | Total_Beds | Total Units | Direct copy |
| 11 | Census | *(calculated)* | **Total_Beds × 0.80** |
| 12 | Do_We_Serve | *(none)* | **"No"** |
| 13 | Integrated_Flag | *(none)* | **NULL** |
| 14 | PCP_Flag | *(none)* | **NULL** |
| 15 | MH_Flag | *(none)* | **NULL** |
| 16 | Barrier | *(none)* | **NULL** |
| 17 | Latitude | Latitude | Direct copy |
| 18 | Longitude | Longitude | Direct copy |
| 19 | Data_Quality_Flag | *(calculated)* | Flag if issues detected |
| 20 | Contract_Status | *(none)* | **"GREEN"** (default) |
| 21 | Geographic_Tier | *(calculated)* | Distance to metro centers |
| 22 | Integration_Eligible | *(calculated)* | Apply eligibility rules |
| 23 | New_Business_Eligible | *(calculated)* | Apply eligibility rules |

---

## 4. CALCULATION RULES FOR NEW FACILITIES

### Rule 1: Source_Type Classification

```python
NC_units = Eventus["NC Open Units"]
Total_units = Eventus["Total Units"]

IF NC_units / Total_units >= 0.50:
    Source_Type = "SNF"
ELSE:
    Source_Type = "ALF"
```

### Rule 2: Census Estimation

```python
Census = Total_Beds × 0.80
```

### Rule 3: Ownership_Type Classification

```python
Owner_Name = Eventus["Owner Name"]

IF Owner_Name contains "LLC" OR "Inc" OR "Corp" OR "LP" OR "LLP":
    Ownership_Type = "Corporate"
ELSE:
    Ownership_Type = "Independent"
```

### Rule 4: Geographic_Tier

```python
# Same logic as V16
Distance_to_nearest_metro = CALCULATE_MIN_DISTANCE(Latitude, Longitude, METRO_CENTERS)

IF Distance_to_nearest_metro <= 15 miles:
    Geographic_Tier = "A_Metro"
ELIF Distance_to_nearest_metro <= 50 miles:
    Geographic_Tier = "B_Highway"
ELSE:
    Geographic_Tier = "C_Rural"
```

### Rule 5: Eligibility Flags

```python
# Same logic as V16
Integration_Eligible = FALSE  # Not served, so no integration opportunity
New_Business_Eligible = TRUE  # New facilities are all new business opportunities
```

---

## 5. SIMPLIFIED MERGE ALGORITHM

```
STEP 1: Load Databases
  V16 = 17,434 facilities × 23 columns
  Eventus = 23,142 facilities × 42 columns

STEP 2: GPS Matching (≤50m radius)
  Identify ~20,433 overlaps
  Identify ~2,709 Eventus-only (NEW)

STEP 3: Keep All V16 Records
  Copy 17,434 V16 records with all 23 columns UNCHANGED

STEP 4: Process NEW Eventus Facilities
  FOR EACH of the ~2,709 NEW facilities:
    - Map Eventus columns to V16 columns
    - Calculate Source_Type
    - Calculate Census
    - Calculate Ownership_Type
    - Set Do_We_Serve = "No"
    - Set Contract_Status = "GREEN"
    - Calculate Geographic_Tier
    - Calculate eligibility flags
    - Leave service flags NULL
    - Leave Barrier NULL
    - Leave Corporate_Name NULL

STEP 5: Combine
  V17 = V16 records (17,434) + NEW Eventus records (2,709)
  Total = 20,143 facilities × 23 columns

STEP 6: Quality Control
  - Verify row count = 20,143
  - Verify column count = 23 (same as V16)
  - Verify no duplicates
  - Verify GPS coverage = 100%
  - Verify all calculations correct

STEP 7: Deliver
  Combined_Database_FINAL_V17.xlsx
  V16_to_V17_Comparison_Report.md
  V17_Match_Log.xlsx
  QC_Validation_Workbook_V17.xlsx
```

---

## 6. WHAT WE'RE NOT DOING

❌ **NOT adding any new columns**  
❌ **NOT adding Eventus Building ID**  
❌ **NOT adding MSA**  
❌ **NOT adding facility phone**  
❌ **NOT adding administrator contact info**  
❌ **NOT adding owner information**  
❌ **NOT adding CCN**  
❌ **NOT adding Year Built**  
❌ **NOT adding Profit Status**  
❌ **NOT adding Operator Name**  

**All Eventus data beyond the basic 23 V16 columns is discarded.**

---

## 7. V17 COMPOSITION

| Component | Facilities | Columns | Source |
|-----------|------------|---------|--------|
| V16 facilities (unchanged) | 17,434 | 23 | V16 database |
| NEW from Eventus | ~2,709 | 23 | Eventus (mapped to V16 structure) |
| **V17 TOTAL** | **~20,143** | **23** | **Combined** |

---

## 8. BENEFITS OF THIS APPROACH

✅ **Simple**: No new column definitions or documentation  
✅ **Compatible**: All existing tools/reports work with V17  
✅ **Clean**: No NULL columns for V16 records  
✅ **Fast**: Fewer transformations = faster processing  
✅ **Maintainable**: Same structure = easier to understand  

---

## 9. DATA WE'RE LEAVING BEHIND

From Eventus, we're **not capturing**:
- Administrator contact information (4 fields)
- Owner details (5 fields)
- Operator name
- MSA designation
- CCN (Medicare certification)
- Year Built
- Facility phone
- Profit status
- Building UUID

**Trade-off**: Simpler structure vs. enhanced contact/intelligence data

---

## 10. NEXT STEPS

1. ✅ **Confirm** this simplified approach
2. **Proceed** with merge using 23-column structure
3. **Generate** V17 database
4. **Run QC** validation
5. **Deliver** complete package

---

**Document Status**: READY FOR APPROVAL  
**Key Change**: NO NEW COLUMNS - V17 = V16 structure + more facilities  
**Date**: November 20, 2025

---

## QUICK REFERENCE

### V17 At-a-Glance (Simplified)

```
V17 = EXACT SAME 23 COLUMNS AS V16
    + ~2,709 NEW facility rows
    = ~20,143 total facilities
```

**NO new columns. NO new fields. Just more facilities.**

---

**END OF SIMPLIFIED METHODOLOGY**
