# V17 Merge - Quick Reference Summary
## Eventus Healthcare Economic Model

**Date**: November 20, 2025  
**Status**: ✅ COMPLETE - ALL QC CHECKS PASSED

---

## WHAT HAPPENED

**V17 = V16 + NEW FACILITIES FROM 8 STATES**

```
V16:  17,434 facilities (100% preserved unchanged)
NEW: + 3,589 facilities (from IN, KY, NC, OH, SC, VA, PA, TN)
     ──────────
V17:  21,023 facilities × 21 columns
```

---

## KEY RESULTS

### ✅ All QC Checks Passed

| Check | Result |
|-------|--------|
| Row count | 21,023 ✓ |
| Column count | 21 ✓ |
| Do_We_Serve (V16) | 1,743 Yes ✓ |
| Service flags preserved | All ✓ |
| Contract status preserved | All ✓ |
| Geographic tier preserved | All ✓ |
| GPS coverage | 100% ✓ |
| **NO DATA DRIFT** | **✓** |

### 📊 Major Changes

| Metric | V16 → V17 | Change |
|--------|-----------|--------|
| **Total Facilities** | 17,434 → 21,023 | +3,589 (+21%) |
| **Columns** | 23 → 21 | -2 (removed unused) |
| **ALF Facilities** | 2,684 → 5,789 | +3,105 (+116%) |
| **PA Facilities** | 661 → 1,741 | +1,080 (+163%) |
| **TN Facilities** | 304 → 713 | +409 (+135%) |

---

## WHAT CHANGED

### ✅ What Was Added

- **3,589 NEW facilities** from 8-state focus area
- Better ALF market coverage (+116%)
- PA and TN expansion (Edge Expansion Strategy)
- Enhanced geographic targeting

### ❌ What Was Removed

- Integration_Eligible column (was all FALSE, unused)
- New_Business_Eligible column (was all FALSE, unused)

### ♻️ What Stayed the Same

- **ALL 17,434 V16 facilities unchanged**
- Do_We_Serve counts (1,743 Yes / 15,691 No)
- Service flags (Integrated, PCP, MH)
- Contract status (40 Yellow, 14 Red)
- Geographic tiers
- 100% data integrity preserved

---

## FILES DELIVERED

### Core Database
📁 [Combined_Database_FINAL_V17.xlsx](computer:///mnt/user-data/outputs/Combined_Database_FINAL_V17.xlsx)
- 21,023 facilities × 21 columns
- 17.9 MB file size

### Quality Control
📁 [QC_Validation_Workbook_V17.xlsx](computer:///mnt/user-data/outputs/QC_Validation_Workbook_V17.xlsx)
- 3 sheets: QC Summary, V16 vs V17, NEW Facilities
- All checks PASS

### Documentation
📁 [V16_to_V17_Comparison_Report.md](computer:///mnt/user-data/outputs/V16_to_V17_Comparison_Report.md)
- Comprehensive 13-section analysis
- Methodology, QC results, business insights

---

## COLUMN STRUCTURE (21 columns)

1. Source_Type
2. Facility_Name
3. Corporate_Name
4. Address
5. City
6. State
7. ZIP
8. County
9. Ownership_Type
10. Total_Beds
11. Census
12. Do_We_Serve
13. Integrated_Flag
14. PCP_Flag
15. MH_Flag
16. Barrier
17. Latitude
18. Longitude
19. Data_Quality_Flag
20. Contract_Status
21. Geographic_Tier

---

## BY THE NUMBERS

### Service Status
- **Served (Yes)**: 1,743 (unchanged from V16)
- **Not Served (No)**: 19,280 (15,691 V16 + 3,589 NEW)

### Facility Type
- **SNF**: 15,234 (14,750 V16 + 484 NEW)
- **ALF**: 5,789 (2,684 V16 + 3,105 NEW)

### Geographic Tier
- **A_Metro** (≤15 mi): 1,785 (1,122 V16 + 663 NEW)
- **B_Highway** (15-50 mi): 1,300 (706 V16 + 594 NEW)
- **C_Rural** (>50 mi): 17,938 (15,606 V16 + 2,332 NEW)

### Contract Status
- **Green**: 20,969 (17,380 V16 + 3,589 NEW)
- **Yellow**: 40 (unchanged from V16)
- **Red**: 14 (unchanged from V16)

---

## NEW FACILITIES BREAKDOWN (3,589 total)

### By State

| State | NEW Added | Strategy |
|-------|-----------|----------|
| **PA** | 1,080 | ⭐ Edge Expansion (+163%) |
| **TN** | 409 | ⭐ Edge Expansion (+135%) |
| OH | 568 | Core strengthening |
| VA | 525 | Core strengthening |
| NC | 318 | Core strengthening |
| IN | 291 | Core strengthening |
| SC | 266 | Core strengthening |
| KY | 132 | Core strengthening |

### Characteristics

- **86.5% ALF** (3,105 facilities)
- **13.5% SNF** (484 facilities)
- **65% C_Rural**, 18.5% A_Metro, 16.5% B_Highway
- **100% Contract_Status = Green** (no RED/YELLOW matches)
- **100% Do_We_Serve = No** (all new prospects)

---

## MERGE METHODOLOGY

1. ✅ Filtered Eventus to 8 states (IN, KY, NC, OH, SC, VA, PA, TN)
2. ✅ GPS matched within 50m radius (1,320 matches, 3,589 NEW)
3. ✅ Preserved ALL V16 data unchanged (17,434 facilities)
4. ✅ Mapped NEW facilities to V17 structure
5. ✅ Calculated Source_Type from NC Open Units
6. ✅ Calculated Geographic_Tier from 19 metro centers
7. ✅ Corporate name matching for Contract_Status
8. ✅ Combined V16 + NEW = V17
9. ✅ QC Validation - ALL CHECKS PASSED

---

## NEXT STEPS

### Immediate
1. ✅ **V17 is ready for use** - all QC passed
2. Review NEW facilities by state
3. Consider outreach strategy for PA/TN

### Future
1. Validate Census estimates (sample check)
2. Rebuild eligibility flags when needed
3. Refine corporate matching if needed
4. Consider drive-time analysis vs. straight-line

---

## IMPORTANT NOTES

⚠️ **V16 Data Integrity**: 100% preserved, zero changes  
⚠️ **Scope**: NEW facilities ONLY from 8 states (not nationwide)  
⚠️ **Corporate Matching**: No RED/YELLOW matches found  
⚠️ **Census**: Estimated at 0.80 × Total_Beds for NEW facilities  

✅ **Production Ready**: All validation checks passed  
✅ **No Data Drift**: V16 portion exactly preserved  
✅ **Clean Merge**: No errors, warnings, or data quality issues  

---

**Generated**: November 20, 2025  
**V17 Status**: ✅ PRODUCTION READY

---

**Quick Links**:
- [V17 Database](computer:///mnt/user-data/outputs/Combined_Database_FINAL_V17.xlsx)
- [QC Workbook](computer:///mnt/user-data/outputs/QC_Validation_Workbook_V17.xlsx)
- [Full Comparison Report](computer:///mnt/user-data/outputs/V16_to_V17_Comparison_Report.md)
