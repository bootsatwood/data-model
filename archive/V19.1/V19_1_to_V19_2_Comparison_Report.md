# V19.1 to V19.2 Comparison Report
## Database vs Methodology Versioning

**Date**: December 2024  
**Status**: Documentation

---

## Critical Clarification

**V19.1 = Database Version**  
**V19.2 = Methodology/Reporting Version**

There is no V19.2 database. The V19.2 designation refers to updated filtering and reporting methodology applied to the V19.1 database.

---

## Version Definitions

| Version | Type | Description |
|---------|------|-------------|
| **V19.1** | Database | Combined_Database_FINAL_V19_1.xlsx (20,943 facilities) |
| **V19.1** | Scenario Files | Economic_Model_Scenario_X_Combined_V19_1.xlsx |
| **V19.2** | Methodology | Updated filtering rules applied to V19.1 data |
| **V19.2** | Reports | V19_Metro_Priority_Targets_Final_V19_2.xlsx |

---

## What Changed: Session 1 (V19.1) → V19.2

### Filter Methodology Changes

| Filter | Session 1 (V19.1) | V19.2 | Impact |
|--------|-------------------|-------|--------|
| **Barrier Exclusion** | Facility-level only | Chain-level propagation | If ANY facility has barrier, exclude entire corp |
| **Cardon** | Not excluded | Permanent barrier | -14 facilities, -$5.3M |
| **Minimum Facilities** | No filter | >7 facilities | Removes small operators from rankings |
| **Metro Count** | 19 metros | 12 metros | Different geographic scope |

### Metro Market Definitions

**Session 1 (19 Metros):**
- OH: Cleveland, Akron, Columbus, Cincinnati
- IN: Indianapolis, Gary, Fort Wayne, Evansville
- KY: Louisville, Lexington
- NC: Charlotte, Greensboro, Raleigh
- VA: Richmond, Virginia Beach
- SC: Greenville, Columbia, Charleston
- WV: Charleston

**V19.2 (12 Metros):**
- OH: Cleveland-Akron (combined), Columbus, Cincinnati, Toledo
- IN: Indianapolis, Northwest Indiana (Gary), Evansville
- KY: Louisville, Lexington
- NC: Charlotte
- VA: Richmond, Harrisonburg-Charlottesville

**Key Differences:**
- Session 1 had separate Cleveland and Akron; V19.2 combines them
- Session 1 included NC metros (Greensboro, Raleigh) not in V19.2
- Session 1 included VA Beach, not in V19.2
- Session 1 included 3 SC metros, V19.2 has none beyond Charlotte overlap
- Session 1 included Charleston WV, not in V19.2
- Session 1 included Fort Wayne IN, not in V19.2
- V19.2 added Toledo OH, not in Session 1
- V19.2 added Harrisonburg-Charlottesville VA, not in Session 1

---

## Revenue Impact Summary

### Metro Markets Comparison

| Metric | Session 1 | V19.2 | Difference |
|--------|-----------|-------|------------|
| Facilities | 685 | 604 | -81 |
| Total Potential | $215.9M | $192.5M | -$23.4M |

### Difference Attribution

| Change | Facilities | Revenue Impact |
|--------|------------|----------------|
| Cardon permanent barrier | -14 | -$5.3M |
| Metro definition change (19→12) | -67 | -$18.1M |
| Chain-level barrier propagation | 0 | $0 |
| **Total** | **-81** | **-$23.4M** |

---

## TAM/SAM/SOM Comparison

| Segment | Session 1 | V19.2 | Difference |
|---------|-----------|-------|------------|
| TAM | 11,973 | 11,845 | -128 |
| SAM | 5,031 | 4,869 | -162 |
| SOM | 3,102 | 2,942 | -160 |
| Metro | 685 | 604 | -81 |

**Note**: TAM/SAM/SOM differences are driven by chain-level barrier propagation and Cardon exclusion, not metro definitions.

---

## Files Inventory

### V19.1 Database Files (Source Data)
- `Combined_Database_FINAL_V19_1.xlsx` — 20,943 facilities
- `Economic_Model_Scenario_1_Combined_V19_1.xlsx`
- `Economic_Model_Scenario_2_Combined_V19_1.xlsx`
- `Economic_Model_Scenario_3_Combined_V19_1.xlsx`

### V19.2 Reports (Methodology Applied)
- `V19_Metro_Priority_Targets_Final_V19_2.xlsx` — 6 sheets with V19.2 filters
- `V19_New_State_Opportunities_V19_2.xlsx` — New state expansion analysis
- `Majestic_Customer_Opportunity_Analysis.md` — Customer deep-dive
- `Majestic_Facility_List_Complete.xlsx` — Customer facility detail

### Session 1 Reference Files
- `V19_Metro_TAM_SAM_SOM_Summary.xlsx` — Original Session 1 output
- `V19_Metro_TAM_SAM_SOM_Methodology.md` — Session 1 methodology
- `Metro_Centers_19_GPS_Coordinates.csv` — Session 1 metro definitions

---

## V19_Metro_Priority_Targets_Final_V19_2.xlsx Contents

| Sheet | Content | Filters Applied |
|-------|---------|-----------------|
| 1. TAM SAM SOM Metro | Market segmentation summary | V19.2 methodology |
| 2. Top 4 Metros | Top 3 corps per priority metro | 12 metros, Corporate, Green, Chain barriers, Cardon |
| 3. Top 75 Metro | Top corps across all metros | 12 metros, Corporate, Green, Chain barriers, Cardon, >7 fac |
| 4. Top 75 SOM | Top corps in 6 SOM states | Corporate, Chain barriers, Cardon, >7 fac |
| 5. Top 75 SAM | Top corps in 13 SAM states | Corporate, Chain barriers, Cardon, >7 fac |
| 6. Barriers & Contract Issues | All barrier + Yellow/Red facilities | Corporate + Independent |

---

## Filter Parameter Reference

| Filter | Session 1 Metro | TAM SAM SOM Metro (V19.2) | Sheet 1: Top 4 Metros | Sheet 2: Top 75 Metro | Sheet 3: Top 75 SOM | Sheet 4: Top 75 SAM | Sheet 5: Barriers |
|--------|-----------------|---------------------------|----------------------|----------------------|---------------------|---------------------|-------------------|
| **Geographic** | 19 metros | 12 metros | 4 metros | 12 metros | 6 states | 13 states | All states |
| **Ownership** | Corporate | Corporate | Corporate | Corporate | Corporate | Corporate | Corp + Ind |
| **Contract Status** | Green | Green | Green | Green | No filter | No filter | Yellow + Red |
| **Barriers** | Facility-level | Chain-level | Chain-level | Chain-level | Chain-level | Chain-level | Barrier = Yes |
| **Cardon** | Not excluded | Permanent | Permanent | Permanent | Permanent | Permanent | N/A |
| **Min Facilities** | No filter | No filter | No filter | >7 | >7 | >7 | No filter |
| **Facilities** | 685 | 604 | 103 | 230 | 1,782 | 2,361 | 894 |
| **Total Potential** | $215.9M | $192.5M | $41.3M | $69.6M | $489.9M | $843.9M | N/A |

---

## Barrier Corps List (V19.2)

Chain-level barrier propagation excludes all facilities from these 23 corporate entities:

| Corporate Entity | Facilities | Barrier Source |
|------------------|------------|----------------|
| ATRIUM HEALTH | 12 | Database barrier flag |
| AVENTURA | 6 | Database barrier flag |
| BLUEGRASS HEALTH KY | 15 | Database barrier flag |
| BLUEGRASS/ENCORE | 26 | Database barrier flag |
| BRIGHTON | 5 | Database barrier flag |
| CARDON & ASSOCIATES | 34 | **Permanent barrier (manual)** |
| COMMONWEALTH CARE OF ROANOKE | 13 | Database barrier flag |
| COMMUNICARE | 12 | Database barrier flag |
| COMMUNICARE HEALTH | 122 | Database barrier flag |
| DAVID MARX | 10 | Database barrier flag |
| EASTERN HEALTHCARE GROUP | 20 | Database barrier flag |
| EMBASSY HEALTHCARE | 40 | Database barrier flag |
| ENCORE HEALTH PARTNERS | 12 | Database barrier flag |
| EXCEPTIONAL LIVING CENTERS | 13 | Database barrier flag |
| GENESIS HEALTHCARE | 215 | Database barrier flag |
| HILL VALLEY HEALTHCARE | 47 | Database barrier flag |
| JOURNEY HEALTHCARE | 17 | Database barrier flag |
| LIFEWORKS REHAB | 51 | Database barrier flag |
| MAJOR HOSPITAL | 6 | Database barrier flag |
| MFA | 8 | Database barrier flag |
| SIGNATURE HEALTH | 13 | Database barrier flag |
| SIGNATURE HEALTHCARE | 72 | Database barrier flag |
| SIMCHA HYMAN & NAFTALI ZANZIPER | 115 | Database barrier flag |

**Note**: Cardon is the only "permanent barrier" — manually added regardless of database flag status.

---

## When to Use Which Version

| Use Case | Version | Files |
|----------|---------|-------|
| Raw facility data | V19.1 | Combined_Database_FINAL_V19_1.xlsx |
| Revenue calculations | V19.1 | Economic_Model_Scenario_X_Combined_V19_1.xlsx |
| Metro market analysis | V19.2 | V19_Metro_Priority_Targets_Final_V19_2.xlsx |
| Corporate rankings | V19.2 | V19_Metro_Priority_Targets_Final_V19_2.xlsx |
| Historical comparison | Session 1 | V19_Metro_TAM_SAM_SOM_Summary.xlsx |

---

## Recommendations

1. **Use V19.2 methodology** for all forward-looking analysis — it reflects current business decisions (Cardon exclusion, chain-level barriers)

2. **Reference V19.1 database** for facility-level data and revenue calculations

3. **Document any deviations** if reverting to Session 1 methodology for specific analyses

4. **Do not create a V19.2 database** — the methodology changes are filter-level, not data-level

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| V19.1 | Nov 2024 | Database created (20,943 facilities) |
| Session 1 | Nov 2024 | Initial metro analysis (19 metros, 685 facilities, $215.9M) |
| V19.2 | Dec 2024 | Methodology update: Chain barriers, Cardon permanent, 12 metros, >7 filter |

---

**Document Created**: December 2024  
**Purpose**: Clarify database vs methodology versioning  
**Status**: Reference Documentation
