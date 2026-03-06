# V22.10 -> V22.11: IL/55+ Source_Type Reclassification

**Date:** 2026-03-06
**Script:** `scripts/v22_11_il_reclassify.py`
**Input:** `1_Combined_Database_FINAL_V22_10.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_11.xlsx`

---

## Summary

Reclassifies 53 HIGH-confidence non-ALF facilities from Source_Type ALF to ILF. These are Independent Living communities, senior apartments, 55+ communities, and active adult communities that were imported from NIC Maps as ALFs but are not licensed Assisted Living Facilities.

## Background

The Wave 0 IL contamination audit (`il_contamination_audit.csv`) identified 413 candidate rows across three confidence levels:
- HIGH: 62 rows (13 served)
- MEDIUM: 303 rows (5 served)
- LOW: 48 rows (0 served)

This version addresses the HIGH confidence tier. Of 62 candidates, 53 are clear reclassifications, 8 are deferred (ambiguous), and 1 was not found in the current DB.

## Changes by Category

### IL_ABBREVIATION (9 rows, 8 served)

Campus IL components with "-IL" or "(IL)" suffix — these are the Independent Living wing of a multi-building campus.

| Row | Facility | State | Served | Co-located With |
|---|---|---|---|---|
| 4798 | GREENWOOD VILLAGE SOUTH IL | IN | Yes | SNF + 3 ALFs |
| 4995 | MARQUETTE MANOR IL | IN | Yes | SNF + ALF |
| 16115 | BENTLEY COMMONS-IL | VA | Yes | 2 ALFs |
| 16257 | HARMONY ROANOKE - IL | VA | Yes | ALF |
| 16303 | KENDAL IL | VA | Yes | — |
| 16405 | RUNK & PRATT LIBERTY RIDGE-IL | VA | Yes | ALF |
| 16482 | THE LODGE AT OLD TRAIL-IL | VA | Yes | ALF |
| 16488 | THE SUMMIT-IL | VA | Yes | — |
| 18569 | HARMONY COLLECTION AT COLUMBIA (IL) | SC | No | — |

### INDEPENDENT_LIVING (8 rows, 1 served)

Facilities with "Independent Living" in name.

| Row | Facility | State | Served | Co-located With |
|---|---|---|---|---|
| 16239 | GLEBE-INDEPENDENT LIVING | VA | Yes | ALF + SNF |
| 17888 | CHANDLER PLACE INDEPENDENT LIVING | SC | No | — |
| 19540 | PRIME INDEPENDENT LIVING GASTONIA | NC | No | — |
| 19898 | SOUTHERN HERITAGE INDEPENDENT LIVING | TN | No | — |
| 20124 | THE ARBORS INDEPENDENT LIVING | VA | No | — |
| 20220 | THE HARMONY COLLECTION AT ROANOKE INDEPENDENT LIVING | VA | No | — |
| 20465 | THE WOODLANDS IL AT OTTERBEIN SUNSET HOUSE | OH | No | — |
| 20504 | TRADITIONS OF HERSHEY INDEPENDENT LIVING | PA | No | — |

### SENIOR_APARTMENTS (25 rows, 0 served)

Age-restricted apartment buildings — not licensed care facilities.

| Row | Facility | State |
|---|---|---|
| 17289 | 900 ACQUA SENIOR APARTMENTS | VA |
| 17744 | BROOKHAVEN AT COUNTY LINE SENIOR APARTMENTS | IN |
| 17835 | CAVALIER SENIOR APARTMENTS | VA |
| 17912 | CHAUNCEY POINTE SENIOR APARTMENTS | OH |
| 18122 | CROMWELL HOUSE SENIOR APARTMENTS - 55+ | VA |
| 18308 | FAIRFIELD VILLAGE SENIOR APARTMENTS | OH |
| 18329 | FIELDCHASE SENIOR APARTMENTS | OH |
| 18414 | GARDENS ON GATEWAY SENIOR APARTMENTS | IN |
| 18417 | GATEWAY POINTE SENIOR APARTMENTS 55+ | OH |
| 19022 | MANCHESTER LAKES SENIOR APARTMENT HOMES | VA |
| 19119 | MERIDIAN HILLS SENIOR APARTMENTS | KY |
| 19151 | MOFFETT MANOR SENIOR APARTMENTS | VA |
| 19260 | NORA COMMONS ON THE MONON SENIOR APARTMENTS | IN |
| 19298 | OAK HILL SENIOR APARTMENTS | PA |
| 19414 | PARK PLACE SENIOR APARTMENTS | VA |
| 19442 | PARSONS VILLAGE EAST SENIOR APARTMENTS | OH |
| 19504 | PLAZA TOWERS SENIOR APARTMENTS | TN |
| 19752 | SADDLEBROOK SENIOR APARTMENTS | TN |
| 19798 | SENIOR APARTMENTS | OH |
| 20066 | SYCAMORE CREEK SENIOR APARTMENTS | OH |
| 20125 | THE ARBORS SENIOR APARTMENTS | VA |
| 20194 | THE GABLES AT DRUID HILLS SENIOR APARTMENTS | NC |
| 20316 | THE OAKS OF WELLINGTON - 55 & OLDER SENIOR APARTMENTS | VA |
| 20534 | TUCKER STATION SENIOR APARTMENTS | KY |
| 20743 | WESTWOOD PLACE SENIOR APARTMENTS | OH |

### ACTIVE_ADULT / ADULT_COMMUNITY (7 rows, 0 served)

Active adult and 55+ lifestyle communities — not licensed care facilities.

| Row | Facility | State | Corporate |
|---|---|---|---|
| 12913 | VITALIA ACTIVE ADULT COMMUNITY AT MONTROSE | OH | Arrow Senior Living Management |
| 12914 | VITALIA ACTIVE ADULT COMMUNITY AT NORTH OLMSTED | OH | Arrow Senior Living Management |
| 12915 | VITALIA ACTIVE ADULT COMMUNITY AT ROCKSIDE | OH | INDEPENDENT |
| 12916 | VITALIA ACTIVE ADULT COMMUNITY ROCKSIDE | OH | INDEPENDENT |
| 20626 | VITALIA ACTIVE ADULT COMMUNITY AT NORTH ROYALTON | OH | Arrow Senior Living Management |
| 20627 | VITALIA ACTIVE ADULT COMMUNITY AT ROCKSIDE (SEVEN HILLS) | OH | Arrow Senior Living Management |
| 21307 | Autumn Fields Adult Community | IL | Autumn Fields Adult Community |

### AGE_55_PLUS (2 rows, 0 served)

| Row | Facility | State |
|---|---|---|
| 18444 | GLENNS CREEK MANOR SENIOR LIVING 55+ APARTMENTS | KY |
| 18722 | HORIZON HOMES (55+ COMMUNITY) APARTMENTS | IN |

### ADULT_LIVING (1 row, 0 served)

| Row | Facility | State |
|---|---|---|
| 17317 | ADULT LIVING AT ROSEBROOK | PA |

### CCRC IL Component (1 row, 1 served)

| Row | Facility | State | Co-located With |
|---|---|---|---|
| 11764 | CCRC I-DOVER APARTMENTS | OH | CCRC I-DOVER NURSING HOME + SNF |

## Deferred (8 rows)

| Facility | State | Served | Issue |
|---|---|---|---|
| WOODLAND HILLS INDEPENDENT LIVING, AL & MC | VA | Yes | Name includes AL & MC — combined facility |
| THE WILLOWS OF EASLEY & ASSISTED & INDEPENDENT LIVING | SC | No | Name includes "Assisted" — combined facility |
| HOLLY MANOR AL IL OPERATIONS LLC | VA | No | "AL IL" ambiguous — could be combined AL+IL |
| CCRC I-DOVER NURSING HOME | OH | Yes | "Nursing Home" suggests SNF, not IL — Source_Type issue |
| CENTRAL CONTINUING CARE-SNF/NF | NC | Yes | Has "SNF/NF" in name — possible Source_Type misclassification |
| TRINITY OAKS CONTINUING CARE RETIREMENT COMMUNITY | NC | No | Ambiguous CCRC campus listing (2 rows) |
| Collington Continuing Care Retirement Community | MD | No | Ambiguous CCRC campus listing |

## Not Found (1 row)

| Facility | State | Issue |
|---|---|---|
| THE HILLSMAN HOUSE INDEPENDENT LIVING | NC | Not in current DB — may have been renamed in prior version |

## Change Counts

| Metric | Count |
|---|---|
| Source_Type reclassifications | 53 (ALF -> ILF) |
| Served rows reclassified | 10 |
| Rows deleted | 0 |
| Net row delta | 0 |

## Row Counts

| Metric | V22.10 | V22.11 | Delta |
|---|---|---|---|
| Total | 26,179 | 26,179 | 0 |
| SNF | 15,239 | 15,239 | 0 |
| ALF | 10,933 | 10,880 | -53 |
| ILF | 7 | 60 | +53 |
| Served | 1,657 | 1,657 | 0 |

## Remaining IL Contamination

| Confidence | Total | Addressed | Remaining |
|---|---|---|---|
| HIGH | 62 | 53 | 9 (8 deferred + 1 not found) |
| MEDIUM | 303 | 0 | 303 |
| LOW | 48 | 0 | 48 |
