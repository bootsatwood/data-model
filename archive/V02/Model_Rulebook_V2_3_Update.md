# Final Model Rulebook V2.3 - Update Document
## Eventus Economic Model - Fee Structure Finalized

**Document Purpose:** This update document defines the actual fee structure for Scenario 1 and supersedes the placeholder values in V2.2.

**Model Version:** 3.0 - Modular Architecture  
**Rulebook Version:** V2.3 UPDATE  
**Date:** November 15, 2025  
**Status:** PRODUCTION READY - Fee Structure Finalized  
**Architecture:** Three-File System (Source + Model + Reports)

---

## WHAT CHANGED FROM V2.2 TO V2.3

**V2.3 Updates:**
1. ✅ **Added Actual Fee Structure** - Real rates for SNF and ALF facilities
2. ✅ **Renamed "Social Services" to "Shared Savings"** - Corrected terminology
3. ✅ **Documented Rate Matrix** - Different rates for SNF vs ALF
4. ✅ **Removed "Annual Rate" terminology** - Simplified to static fee values
5. ✅ **Test Implementation Complete** - Working model with 14,750 SNF facilities

**V2.2 Retained:**
- All architectural principles remain unchanged
- Four revenue streams (Current, Integration, New Biz, Total)
- Three-file modular system
- Market segmentation (TAM/SAM/SOM)
- Reporting layer structure

---

## SCENARIO 1 FEE STRUCTURE (ACTUAL RATES)

### **Fee Structure Matrix**

| Service Type | SNF Rate | ALF Rate | Notes |
|--------------|----------|----------|-------|
| **PCP Fee** | $1,698.96 | $1,875.00 | Primary Care Provider services |
| **MH Fee** | $1,623.96 | $1,898.00 | Mental Health / Behavioral Health services |
| **CCM Fee** | $360.00 | $360.00 | Chronic Care Management (same for both) |
| **Shared Savings** | $4,800.00 | $4,800.00 | Shared Savings (same for both) |

### **Integrated Services Package**

**SNF Integrated Package:**
- PCP: $1,698.96
- MH: $1,623.96
- CCM: $360.00
- Shared Savings: $4,800.00
- **Total: $8,482.92**

**ALF Integrated Package:**
- PCP: $1,875.00
- MH: $1,898.00
- CCM: $360.00
- Shared Savings: $4,800.00
- **Total: $8,933.00**

---

## REVENUE CALCULATION FORMULAS (UPDATED)

### **Current Revenue**

For facilities where `Do_We_Serve = "yes"`:

**If Integrated_Flag = "yes":**
```
Current_Revenue = PCP_Fee + MH_Fee + CCM_Fee + Shared_Savings
SNF: $1,698.96 + $1,623.96 + $360 + $4,800 = $8,482.92
ALF: $1,875.00 + $1,898.00 + $360 + $4,800 = $8,933.00
```

**If PCP_Flag = "yes" (PCP Only):**
```
Current_Revenue = PCP_Fee + CCM_Fee + Shared_Savings
SNF: $1,698.96 + $360 + $4,800 = $6,858.96
ALF: $1,875.00 + $360 + $4,800 = $7,035.00
```

**If MH_Flag = "yes" (MH Only):**
```
Current_Revenue = MH_Fee + CCM_Fee + Shared_Savings
SNF: $1,623.96 + $360 + $4,800 = $6,783.96
ALF: $1,898.00 + $360 + $4,800 = $7,058.00
```

**If no service flags:**
```
Current_Revenue = $0 (data quality issue)
```

### **Integration Revenue**

For facilities where `Do_We_Serve = "yes"` and not already Integrated:

**If PCP_Only (can add MH):**
```
Integration_Revenue = MH_Fee
SNF: $1,623.96
ALF: $1,898.00
```

**If MH_Only (can add PCP):**
```
Integration_Revenue = PCP_Fee
SNF: $1,698.96
ALF: $1,875.00
```

**If Integrated (already has both):**
```
Integration_Revenue = $0
```

### **New Business Revenue**

For unserved facilities where `Ownership_Type = "Corporate"` and `Barrier = null`:

```
New_Biz_Revenue = Integrated_Package
SNF: $8,482.92
ALF: $8,933.00
```

### **Total Revenue**

```
Total_Revenue = Current_Revenue + Integration_Revenue + New_Biz_Revenue
```

---

## TEST IMPLEMENTATION RESULTS

### **Test Scope**
- **Data Source:** SNF_Database_Final_v2_4_2025-11-14.xlsx
- **Facility Count:** 14,750 SNF facilities
- **Rates Used:** SNF fee structure
- **Date:** November 15, 2025

### **Test Results - TAM (Total Addressable Market)**

**Facilities:**
- Total SNF Facilities: 14,750
- Currently Served: 563 (3.8%)
- Corporate: 10,065 (68.2%)
- Independent: 4,685 (31.8%)

**Revenue:**
- Current Revenue: **$3,919,967.64**
- Integration Opportunity: **$601,428.72**
- New Business Opportunity: **$81,215,476.08**
- **Total TAM Revenue: $85,736,872.44**

### **Test Results - SOM (Serviceable Obtainable Market)**

**Facilities:**
- SOM Facilities: 9,997
- Currently Served: 354 (3.5%)
- Barriers: 68 facilities excluded

**Revenue:**
- Current Revenue: **$2,971,205.28**
- Integration Opportunity: **$438,928.56**
- New Business Opportunity: **$81,215,476.08**
- **Total SOM Revenue: $84,625,609.92**

### **Service Breakdown (Current Revenue - SOM)**

| Service Component | Revenue | % of Total |
|-------------------|---------|------------|
| PCP (Primary Care) | $1,182,926.88 | 39.8% |
| MH (Mental Health) | $469,825.44 | 15.8% |
| CCM | $127,440.00 | 4.3% |
| Shared Savings | $1,191,013.44 | 40.1% |
| **TOTAL** | **$2,971,205.28** | **100.0%** |

### **Top 5 Corporate Entities (by Total Opportunity)**

1. **THE ENSIGN GROUP** - 303 facilities, $2,570,324.76 opportunity
2. **PACS GROUP** - 212 facilities, $1,798,379.04 opportunity
3. **GENESIS HEALTHCARE** - 215 facilities, $1,782,267.12 opportunity
4. **LIFE CARE CENTERS OF AMERICA** - 195 facilities, $1,654,169.40 opportunity
5. **CREATIVE SOLUTIONS IN HEALTHCARE** - 145 facilities, $1,230,023.40 opportunity

---

## DATA QUALITY ISSUES IDENTIFIED

### **Issue #1: Service Flags Without Do_We_Serve**
**Count:** 4 facilities  
**Description:** Facilities have service flags (Integrated/PCP/MH) but are NOT marked as Do_We_Serve = "yes"

**Facilities:**
1. Waters of Castleton Skilled Nursing Facility (IN) - Integrated_Flag=yes
2. Autumn Care of Cornelius (NC) - PCP_Flag=yes
3. Gardens of North Olmsted (OH) - PCP_Flag=yes
4. Harvard Gardens Rehabilitation & Care Center (OH) - MH_Flag=yes

**Recommendation:** Verify if these should be marked as served or if flags should be removed.

### **Issue #2: Do_We_Serve Without Service Flags**
**Count:** 30 facilities  
**Description:** Facilities marked as Do_We_Serve = "yes" but have NO service flags set

**States Affected:**
- North Carolina: 9 facilities
- Indiana: 8 facilities
- Ohio: 7 facilities
- Kentucky: 6 facilities

**Recommendation:** Populate missing service flags based on actual services provided.

**Impact:** These 30 facilities contribute $0 to Current_Revenue due to missing service flags.

---

## FILE STRUCTURE (UNCHANGED FROM V2.2)

### **Three-File Architecture**

```
FILE 1: Source_Data_Master.xlsx (User Provided)
└── SNF_Database_Final_v2_4_2025-11-14.xlsx

FILE 2: Economic_Model_Scenario_1.xlsx (Generated)
├── Sheet 1: Fee_Structure (SNF/ALF rates)
├── Sheet 2: Calculations (Revenue formulas)
├── Sheet 3: Segmentation (TAM/SAM/SOM)
└── Sheet 4: Results (Aggregations)

FILE 3: Reports_Scenario_1.xlsx (Generated)
├── Report 1: Facilities_Count
├── Report 2: Revenue_Summary
├── Report 3: SOM_Fee_Breakdown
└── Report 4: Top_20_Corporate_Entities
```

---

## IMPLEMENTATION VALIDATION

### **Model Validation Checklist**

✅ **Fee Structure**
- SNF rates correctly implemented
- ALF rates documented (ready for future use)
- Integrated package calculated correctly

✅ **Revenue Calculations**
- Current Revenue: $3,919,967.64 (563 served facilities)
- Integration Revenue: $601,428.72 (357 opportunities)
- New Biz Revenue: $81,215,476.08 (9,574 unserved corporate facilities)

✅ **Market Segmentation**
- TAM: 14,750 facilities
- SAM: 10,065 facilities (corporate only)
- SOM: 9,997 facilities (corporate, no barriers)

✅ **Reports Generated**
- All 4 reports successfully created
- Formatting applied
- Data integrity verified

✅ **Data Quality**
- 34 facilities flagged for review (4 + 30)
- Issues documented for QA follow-up
- Model functional with current data

---

## NEXT STEPS

### **Immediate Actions**

1. **Review Generated Files:**
   - Economic_Model_Scenario_1.xlsx
   - Reports_Scenario_1.xlsx

2. **QA Data Quality Issues:**
   - Resolve 4 facilities with flags but not marked as served
   - Populate missing service flags for 30 facilities

3. **Validate Business Logic:**
   - Confirm revenue calculations match expectations
   - Review top corporate entities list
   - Verify segmentation logic

### **Future Enhancements**

1. **Add ALF Data:**
   - Load ALF facilities from source
   - Apply ALF fee structure
   - Generate combined SNF+ALF reports

2. **Create Scenario 2:**
   - Modify Fee_Structure sheet
   - Test alternative rate structures
   - Compare to Scenario 1 baseline

3. **Geographic Analysis (Report 5):**
   - Define requirements for state-level analysis
   - Build geographic revenue breakdown
   - Add visualization recommendations

---

## DOCUMENT CONTROL

### **Version Information**

**Rulebook Version:** V2.3 UPDATE  
**Date:** November 15, 2025  
**Status:** PRODUCTION READY - Fee Structure Finalized  
**Model Version:** 3.0 (Modular Architecture)

### **Change Summary**

**From V2.2 to V2.3:**
- Added actual fee structure (SNF and ALF rates)
- Renamed "Social Services" to "Shared Savings"
- Removed "annual rate" terminology
- Completed test implementation with real data
- Documented data quality issues
- Generated working model and reports

**Files Generated:**
1. Economic_Model_Scenario_1.xlsx (4.5 MB)
2. Reports_Scenario_1.xlsx (11 KB)
3. Model_Rulebook_V2_3_Update.md (this document)

### **Approval Status**

**Test Status:** ✅ SUCCESSFUL  
**Ready for:** Production use with SNF data  
**Pending:** ALF data integration, data quality cleanup

---

## END OF V2.3 UPDATE DOCUMENT

**This document supplements the V2.2 rulebook with actual fee structure and test results.**

**Use V2.2 for:** Architecture, formulas, and implementation procedures  
**Use V2.3 for:** Actual rates, test results, and data quality issues

**Last Updated:** November 15, 2025  
**Next Review:** After data quality issues resolved or ALF integration complete
