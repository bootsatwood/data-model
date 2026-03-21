# Heritage Reconciliation Report

> **DO NOT EXECUTE -- REVIEW ONLY**

| Field | Value |
|---|---|
| Date | 2026-03-20 |
| Purpose | Correct Heritage-related corporate attribution and data gaps in `bd.market_intel_facilities` |
| Methodology | CMS Provider Info cross-reference, NIC MAP chain validation, state registry verification, operator website confirmation |
| Database | PostgreSQL `bd.market_intel_facilities` (production) |
| Author | Roian Atwood |

---

## Part A: Heritage Hall Reattribution (American Healthcare LLC --> Heritage Hall)

### Problem

11 facility rows are attributed to **AMERICAN HEALTHCARE, LLC** (entity 1219) but are operationally part of the **Heritage Hall** chain (entity 37). American Healthcare is the legal holding company; Heritage Hall is the operator brand. Per data authority hierarchy, operator-level attribution takes precedence.

### Current Values

| id | facility_name | corporate_name_raw | entity_id | address | city | state | county | beds | census | source | do_we_serve | contract | integrated | pcp | mh | barrier | dq_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 15886 | 814 HERITAGE HALL GRUNDY | AMERICAN HEALTHCARE, LLC | 1219 | 2966 Slate Creek Rd | Grundy | VA | Buchanan | 121 | 97.0 | ALF | True | Green | False | False | True | | Surrogate_Census |
| 15887 | 818 HERITAGE HALL LEXINGTON | AMERICAN HEALTHCARE, LLC | 1219 | 205 Houston St | Lexington | VA | Rockbridge | 55 | 44.0 | ALF | True | Green | False | False | True | | Surrogate_Census |
| 15888 | 819 HERITAGE HALL LAUREL MEADOWS | AMERICAN HEALTHCARE, LLC | 1219 | 16600 Danville Pike | Laurel Fork | VA | Carroll | 59 | 47.0 | ALF | True | Green | False | True | False | | Surrogate_Census |
| 15890 | 931 HERITAGE HALL BLACKSBURG | AMERICAN HEALTHCARE, LLC | 1219 | 3610 S Main St | Blacksburg | VA | Montgomery | 133 | 106.0 | ALF | True | Green | False | False | True | | Surrogate_Census |
| 15891 | 933 HERITAGE HALL TAZEWELL | AMERICAN HEALTHCARE, LLC | 1219 | 282 Ben Bolt Ave | Tazewell | VA | Tazewell | 110 | 88.0 | ALF | True | Green | False | False | True | | Surrogate_Census |
| 16108 | HERITAGE HALL - BIG STONE GAP | AMERICAN HEALTHCARE, LLC | 1219 | 2045 Valley View Dr | Big Stone Gap | VA | Wise | 182 | 146.0 | ALF | True | Green | False | False | True | | Surrogate_Census |
| 16086 | HERITAGE HALL BIG STONE GAP | AMERICAN HEALTHCARE, LLC | 1219 | 2045 VALLEY VIEW DRIVE | BIG STONE GAP | VA | Wise | 180 | 165.3 | SNF | True | Green | True | False | False | | In Database, NOT in PowerBI - needs verification |
| 16087 | HERITAGE HALL BLACKSBURG | AMERICAN HEALTHCARE, LLC | 1219 | 3610 SOUTH MAIN STREET | BLACKSBURG | VA | Montgomery | 179 | 126.6 | SNF | True | Green | False | False | True | | In Database, NOT in PowerBI - needs verification |
| 16091 | HERITAGE HALL GRUNDY | AMERICAN HEALTHCARE, LLC | 1219 | 2966 SLATE CREEK ROAD | GRUNDY | VA | Buchanan | 120 | 113.8 | SNF | True | Green | True | False | False | | In Database, NOT in PowerBI - needs verification |
| 16085 | HERITAGE HALL - LAUREL MEADOWS | AMERICAN HEALTHCARE, LLC | 1219 | 16600 DANVILLE PIKE | LAUREL FORK | VA | Carroll | 60 | 58.7 | SNF | True | Green | False | True | False | | In Database, NOT in PowerBI - needs verification |
| 16094 | HERITAGE HALL TAZEWELL | AMERICAN HEALTHCARE, LLC | 1219 | 282 BEN BOLT AVENUE | TAZEWELL | VA | Tazewell | 180 | 158.4 | SNF | True | Green | False | False | True | | In Database, NOT in PowerBI - needs verification |

### Proposed Changes

For all 11 rows above:

| Field | Current Value | Proposed Value |
|---|---|---|
| corporate_name_raw | AMERICAN HEALTHCARE, LLC | HERITAGE HALL |
| corporate_entity_id | 1219 | 37 |

### Evidence

- CMS Provider Info lists these facilities under "AMERICAN HEALTHCARE INC" as the legal business name, but the operating/doing-business-as name is "Heritage Hall" for each location.
- Heritage Hall's own website (heritagehall.org) lists all 5 campus locations (Big Stone Gap, Blacksburg, Grundy, Laurel Meadows, Tazewell).
- Entity 37 ("HERITAGE HALL") already exists in the DB with 10 other Heritage Hall facilities correctly attributed.
- NIC MAP chain assignment confirms Heritage Hall as the operating brand, not the LLC holding company.
- Per established feedback rule: LLC corp names are NIC MAP artifacts, not real operators -- prefer management company names.

---

## Part B: South Roanoke Facility -- Reattribution (Not INSERT)

### Problem

The user initially requested this facility be ADDED. However, query results show **South Roanoke already exists** in the database as 2 rows under "AHC" (entity 1220):

| id | facility_name | corporate_name_raw | entity_id | address | city | state | county | beds | census | source | do_we_serve | contract | integrated | pcp | mh | barrier | dq_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 15889 | 822 SOUTH ROANOKE NURSING HOME | AHC | 1220 | 3823 Franklin Rd SW | Roanoke | VA | Roanoke | 89 | 71.0 | ALF | True | Green | False | False | True | | Surrogate_Census |
| 16246 | SOUTH ROANOKE NURSING AND REHABILITATION | AHC | 1220 | 3823 FRANKLIN RD, SW | ROANOKE | VA | Roanoke City | 98 | 85.6 | SNF | False | Green | False | False | False | | |

### Analysis

- Both rows share address 3823 Franklin Rd SW, Roanoke, VA -- this is the same physical location.
- "AHC" (entity 1220) is likely another abbreviation for American Healthcare -- the same holding company as entity 1219 ("AMERICAN HEALTHCARE, LLC"). This facility should be attributed to Heritage Hall.
- CMS CCN 495002 confirms: Legal Business Name = "South Roanoke Life Care LLC", Chain = Heritage Hall (Chain ID 265).
- The SNF row (id 16246) has CMS-sourced beds (98) and census (85.6). The ALF row (id 15889) has NIC MAP-sourced data with surrogate census.
- County discrepancy: row 15889 says "Roanoke", row 16246 says "Roanoke City". CMS Provider Info says "Roanoke City" (independent city in VA).
- **RESOLVED:** Both rows are valid -- ALF+SNF dual-row pattern confirmed standard for Heritage Hall locations.

### Proposed Changes

**Row 15889** (ALF -- confirmed valid, not a duplicate):

| Field | Current Value | Proposed Value |
|---|---|---|
| corporate_name_raw | AHC | HERITAGE HALL |
| corporate_entity_id | 1220 | 37 |
| county | Roanoke | Roanoke City |

**Row 16246** (SNF, CMS-sourced -- authoritative row):

| Field | Current Value | Proposed Value |
|---|---|---|
| corporate_name_raw | AHC | HERITAGE HALL |
| corporate_entity_id | 1220 | 37 |

**RESOLVED 2026-03-21:** Row 15889 is NOT a duplicate. The ALF+SNF dual-row pattern is standard for Heritage Hall locations (confirmed by Laurel Meadows precedent: rows 15888 ALF + 16085 SNF at same address). Both rows (15889 ALF + 16246 SNF) reattribute from AHC (entity 1220) to Heritage Hall (entity 37).

**Data quality flag:** `do_we_serve` and `mh_flag` disagree between ALF and SNF rows -- needs reconciliation:
- Row 15889 (ALF): do_we_serve=True, mh_flag=True
- Row 16246 (SNF): do_we_serve=False, mh_flag=False

### Evidence

- CMS Provider Info (CCN 495002): Legal Business Name = "South Roanoke Life Care LLC", Chain = Heritage Hall (Chain ID 265)
- Same address as existing DB rows confirms identity match
- AHC = American Healthcare abbreviation, same parent entity as AMERICAN HEALTHCARE, LLC
- Laurel Meadows precedent confirms ALF+SNF dual-row pattern is standard for Heritage Hall sites

---

## Part C: Heritage Senior Living Split (25 rows --> correct operators)

### Problem

25 rows are all attributed to "HERITAGE SENIOR LIVING" (entity 1088), but this corporate name actually represents at least 4 distinct operators across different states. They need to be split by state/operator.

### Current Values

| id | facility_name | corporate_name_raw | entity_id | address | city | state | county | beds | census | source | do_we_serve | contract | integrated | pcp | mh | barrier | dq_flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11961 | HERITAGE SENIOR LIVING OF MARYSVILLE | HERITAGE SENIOR LIVING | 1088 | 1565 London Ave | Marysville | OH | Union | 76 | 61.0 | ALF | False | Green | False | False | False | | Surrogate_Census |
| 11995 | HERITAGE POINT ASSISTED LIVING | HERITAGE SENIOR LIVING | 1088 | 3304 Rhodes Ave | New Boston | OH | (null) | 27 | 22.0 | ALF | True | Green | True | False | False | | Surrogate_Census, Missing_County |
| 11962 | HERITAGE SQUARE NEW BOSTON | HERITAGE SENIOR LIVING | 1088 | 3304 Rhodes Ave | New Boston | OH | Scioto | 116 | 93.0 | ALF | False | Green | False | False | False | | Surrogate_Census |
| 20056 | TRADITIONS OF HANOVER | HERITAGE SENIOR LIVING | 1088 | 5300 Northgate Dr | Bethlehem | PA | Northampton | 114 | 91.0 | ALF | False | Green | False | False | False | | |
| 18525 | KEYSTONE VILLA AT FLEETWOOD | HERITAGE SENIOR LIVING | 1088 | 501 Hoch Rd | Blandon | PA | Berks | 123 | 98.0 | ALF | False | Green | False | False | False | | |
| 17685 | CHESTNUT KNOLL PERSONAL CARE AND MEMORY CARE | HERITAGE SENIOR LIVING | 1088 | 120 W 5th St | Boyertown | PA | Berks | 86 | 69.0 | ALF | False | Green | False | False | False | | |
| 18523 | KEYSTONE VILLA AT DOUGLASSVILLE PERSONAL CARE | HERITAGE SENIOR LIVING | 1088 | 1152 Ben Franklin Hwy E | Douglassville | PA | Berks | 247 | 198.0 | ALF | False | Green | False | False | False | | |
| 19710 | THE BIRCHES OF THE LEHIGH VALLEY | HERITAGE SENIOR LIVING | 1088 | 5030 Freemansburg Ave | Easton | PA | Northampton | 92 | 74.0 | ALF | False | Green | False | False | False | | |
| 19708 | THE BIRCHES AT HARLEYSVILLE | HERITAGE SENIOR LIVING | 1088 | 691 Main St | Harleysville | PA | Montgomery | 78 | 62.0 | ALF | False | Green | False | False | False | | |
| 20058 | TRADITIONS OF LANSDALE | HERITAGE SENIOR LIVING | 1088 | 1800 Walnut St | Lansdale | PA | Montgomery | 113 | 90.0 | ALF | False | Green | False | False | False | | |
| 17360 | BELLE REVE HEALTH CARE CENTER | HERITAGE SENIOR LIVING | 1088 | 404 E Harford St | Milford | PA | Pike | 54 | 43.0 | ALF | False | Green | False | False | False | | |
| 19709 | THE BIRCHES AT NEW HOPE | HERITAGE SENIOR LIVING | 1088 | 6554 Lower York Rd | New Hope | PA | Bucks | 93 | 74.0 | ALF | False | Green | False | False | False | | |
| 17398 | BIRCHES OF NEWTOWN | HERITAGE SENIOR LIVING | 1088 | 70 Durham Rd | Newtown | PA | Bucks | 91 | 73.0 | ALF | False | Green | False | False | False | | |
| 20057 | TRADITIONS OF HERSHEY INDEPENDENT LIVING | HERITAGE SENIOR LIVING | 1088 | 100 N Larkspur Dr | Palmyra | PA | Lebanon | 131 | 105.0 | ILF | False | Green | False | False | False | | |
| 19852 | THE MANOR AT MARKET SQUARE | HERITAGE SENIOR LIVING | 1088 | 803 Penn St | Reading | PA | Berks | 89 | 71.0 | ALF | False | Green | False | False | False | | |
| 18332 | HERITAGE HILL SENIOR COMMUNITY | HERITAGE SENIOR LIVING | 1088 | 800 6th St | Weatherly | PA | Carbon | 68 | 54.0 | ALF | False | Green | False | False | False | | |
| 19404 | SENIOR COMMONS AT POWDER MILL | HERITAGE SENIOR LIVING | 1088 | 1775 Powder Mill Rd | York | PA | York | 147 | 118.0 | ALF | False | Green | False | False | False | | |
| 16017 | CHANCELLOR'S VILLAGE | HERITAGE SENIOR LIVING | 1088 | 12100 Chancellors Village Ln | Fredericksburg | VA | (null) | 72 | 58.0 | ALF | False | Green | False | False | False | | Surrogate_Beds+Surrogate_Census, Missing_County |
| 18328 | HERITAGE GREEN ASSISTED LIVING COMMUNITIES | HERITAGE SENIOR LIVING | 1088 | 201 & 202 Lillian Lane | Lynchburg | VA | Lynchburg | 124 | 99.0 | ALF | False | Green | False | False | False | | |
| 19751 | THE CROSSROADS AT BON AIR | HERITAGE SENIOR LIVING | 1088 | 9100 Bon Air Crossings Dr | Richmond | VA | Chesterfield | 186 | 149.0 | ALF | False | Green | False | False | False | | |
| 22712 | Heritage Lake Country | HERITAGE SENIOR LIVING | 1088 | 2975 Village Square Dr | Hartland | WI | Waukesha | 79 | 63.0 | ALF | False | Green | False | False | False | | |
| 22713 | Heritage Middleton | HERITAGE SENIOR LIVING | 1088 | 6234 Maywood Ave | Middleton | WI | Dane | 79 | 63.0 | ALF | False | Green | False | False | False | | |
| 22714 | Heritage Monona | HERITAGE SENIOR LIVING | 1088 | 111 Owen Rd | Monona | WI | Dane | 153 | 122.0 | ALF | False | Green | False | False | False | | |
| 22715 | Heritage Muskego | HERITAGE SENIOR LIVING | 1088 | S64 W13780 Janesville Rd | Muskego | WI | Waukesha | 72 | 58.0 | ALF | False | Green | False | False | False | | |
| 23142 | Lincoln Village | HERITAGE SENIOR LIVING | 1088 | 1330 W Lincoln Ave | Port Washington | WI | Ozaukee | 65 | 52.0 | ALF | False | Green | False | False | False | | |

### Proposed Changes by State Group

#### WI rows (5 rows) -- Keep as-is (correct WI operator)

| id | facility_name | Proposed corporate_name_raw | Notes |
|---|---|---|---|
| 22712 | Heritage Lake Country | Heritage Senior Living | Correct WI operator. 0 EWH footprint campuses. No entity_id change needed. |
| 22713 | Heritage Middleton | Heritage Senior Living | Same |
| 22714 | Heritage Monona | Heritage Senior Living | Same |
| 22715 | Heritage Muskego | Heritage Senior Living | Same |
| 23142 | Lincoln Village | Heritage Senior Living | Same |

**Action:** No changes required. These 5 rows are correctly attributed.

#### PA rows (15 rows) -- Reattribute to Heritage Senior Living LLC (Blue Bell, PA)

| id | facility_name | Proposed corporate_name_raw | Proposed entity_id | Notes |
|---|---|---|---|---|
| 20056 | TRADITIONS OF HANOVER | Heritage Senior Living LLC | 4111 | heritagesl.com, Blue Bell PA HQ |
| 18525 | KEYSTONE VILLA AT FLEETWOOD | Heritage Senior Living LLC | 4111 | Same |
| 17685 | CHESTNUT KNOLL PERSONAL CARE AND MEMORY CARE | Heritage Senior Living LLC | 4111 | Same |
| 18523 | KEYSTONE VILLA AT DOUGLASSVILLE PERSONAL CARE | Heritage Senior Living LLC | 4111 | Same |
| 19710 | THE BIRCHES OF THE LEHIGH VALLEY | Heritage Senior Living LLC | 4111 | Same |
| 19708 | THE BIRCHES AT HARLEYSVILLE | Heritage Senior Living LLC | 4111 | Same |
| 20058 | TRADITIONS OF LANSDALE | Heritage Senior Living LLC | 4111 | Same |
| 17360 | BELLE REVE HEALTH CARE CENTER | Heritage Senior Living LLC | 4111 | Same |
| 19709 | THE BIRCHES AT NEW HOPE | Heritage Senior Living LLC | 4111 | Same |
| 17398 | BIRCHES OF NEWTOWN | Heritage Senior Living LLC | 4111 | Same |
| 20057 | TRADITIONS OF HERSHEY INDEPENDENT LIVING | Heritage Senior Living LLC | 4111 | Same |
| 19852 | THE MANOR AT MARKET SQUARE | Heritage Senior Living LLC | 4111 | Same |
| 18332 | HERITAGE HILL SENIOR COMMUNITY | Heritage Senior Living LLC | 4111 | Same |
| 19404 | SENIOR COMMONS AT POWDER MILL | Heritage Senior Living LLC | 4111 | Same |

**RESOLVED 2026-03-21:** New entity **4111** assigned for Heritage Senior Living LLC (Blue Bell, PA). This is a different company from the WI Heritage Senior Living.

#### VA rows (3 rows) -- Reattribute to Heritage Senior Living LLC (same PA entity)

| id | facility_name | Proposed corporate_name_raw | Proposed entity_id | Notes |
|---|---|---|---|---|
| 16017 | CHANCELLOR'S VILLAGE | Heritage Senior Living LLC | 4111 | heritagesl.com lists VA communities |
| 18328 | HERITAGE GREEN ASSISTED LIVING COMMUNITIES | Heritage Senior Living LLC | 4111 | Same |
| 19751 | THE CROSSROADS AT BON AIR | Heritage Senior Living LLC | 4111 | Same |

#### OH Marysville (1 row) -- Reattribute to Heritage Senior Living of Marysville

| id | facility_name | Proposed corporate_name_raw | Proposed entity_id | Notes |
|---|---|---|---|---|
| 11961 | HERITAGE SENIOR LIVING OF MARYSVILLE | Heritage Senior Living of Marysville | 4113 | Independent operator, Angie Sharp. Not affiliated with WI or PA Heritage Senior Living. |

#### OH New Boston (2 rows --> 1 row) -- RESOLVED 2026-03-21

The two rows (ID 11962 "Heritage Square New Boston" 116 beds + ID 11995 "Heritage Point Assisted Living" 27 beds) at 3304 Rhodes Ave are **ONE facility**, not two. Correct operator: **Heritage Legacy Health Services, LLC** (DBA Heritage Pointe Assisted Living). Owners: Deborah Voiers-Akers and Steven Akers. Ohio DOH License #1845R.

**Action:** Merge into 1 row. Delete row 11995. Update row 11962 as follows:

| Field | Current Value (row 11962) | Proposed Value |
|---|---|---|
| corporate_name_raw | HERITAGE SENIOR LIVING | Heritage Legacy Health Services |
| corporate_entity_id | 1088 | 4112 |
| facility_name | HERITAGE SQUARE NEW BOSTON | Heritage Pointe Assisted Living |
| total_beds | 116 | 116 |
| county | Scioto | Scioto |

**Row 11995:** DELETE (duplicate portion of merged facility).

### Evidence

- **WI:** Heritage Senior Living (heritagesenior.com) is a Wisconsin-based operator with communities exclusively in WI. Not affiliated with the PA entity.
- **PA/VA:** Heritage Senior Living LLC (heritagesl.com) is headquartered in Blue Bell, PA. Operates The Birches, Keystone Villa, Traditions, and other brands across PA and VA.
- **OH Marysville:** Ohio Secretary of State filings show "Heritage Senior Living of Marysville" as an independent entity. Angie Sharp is the listed agent.
- **OH New Boston:** RESOLVED. Heritage Legacy Health Services, LLC (DBA Heritage Pointe Assisted Living). Ohio DOH License #1845R. Owners: Deborah Voiers-Akers and Steven Akers. Two DB rows at 3304 Rhodes Ave represent one facility -- merge into single row.

---

## Part D: Heritage Point Missing County

### Problem

Row 11995 (Heritage Point Assisted Living, New Boston, OH) has a null county value. The `data_quality_flag` already notes "Missing_County".

### Current Value

| id | facility_name | city | state | county | dq_flag |
|---|---|---|---|---|---|
| 11995 | HERITAGE POINT ASSISTED LIVING | New Boston | OH | (null) | Surrogate_Census, Missing_County |

### Proposed Change

| Field | Current Value | Proposed Value |
|---|---|---|
| county | (null) | Scioto |

### Evidence

- New Boston, OH is in Scioto County.
- The co-located facility Heritage Square New Boston (id 11962, same address 3304 Rhodes Ave) already has county = "Scioto".
- Ohio county lookup confirms New Boston is within Scioto County boundaries.
- Once county is populated, "Missing_County" should be removed from the data_quality_flag. Proposed dq_flag: "Surrogate_Census".

---

## Summary

> **DO NOT EXECUTE -- REVIEW ONLY**

| Part | Description | Action Type | Row Count |
|---|---|---|---|
| A | Heritage Hall reattribution (American Healthcare --> Heritage Hall) | UPDATE | 11 |
| B | South Roanoke reattribution (AHC --> Heritage Hall) | UPDATE | 2 |
| C | Heritage Senior Living split by operator | UPDATE + DELETE | 19 UPDATE + 1 DELETE (5 WI rows unchanged) |
| D | Heritage Point missing county fix | UPDATE | 1 (subsumed by Part C New Boston merge) |
| **Total** | | | **33 rows updated, 1 row deleted** |

### Breakdown

| Metric | Count |
|---|---|
| Total rows queried | 38 |
| Rows requiring UPDATE | 33 |
| Rows requiring INSERT | 0 |
| Rows requiring DELETE | 1 (row 11995, merged into 11962) |
| Rows unchanged (WI Heritage Senior Living) | 5 |
| New entity IDs assigned | 3 |

### Entity ID Assignments (RESOLVED 2026-03-21)

| Entity ID | Corporate Name | State(s) | Row Count |
|---|---|---|---|
| 1088 (retained) | Heritage Senior Living | WI | 5 |
| 4111 (new) | Heritage Senior Living LLC | PA, VA | 18 (15 PA + 3 VA) |
| 4112 (new) | Heritage Legacy Health Services | OH | 1 (merged New Boston) |
| 4113 (new) | Heritage Senior Living of Marysville | OH | 1 |

### Remaining Open Items

1. ~~Entity ID assignment for Heritage Senior Living LLC (PA/VA)~~ -- RESOLVED: entity 4111
2. ~~Entity ID assignment for Heritage Senior Living of Marysville (OH)~~ -- RESOLVED: entity 4113
3. ~~New Boston OH operator confirmation~~ -- RESOLVED: Heritage Legacy Health Services, LLC (DBA Heritage Pointe Assisted Living), entity 4112. Rows merged.
4. ~~South Roanoke ALF/SNF dedup review~~ -- RESOLVED: NOT a duplicate. ALF+SNF dual-row pattern is standard (Laurel Meadows precedent). Data quality flag: do_we_serve and mh_flag disagree between rows -- needs reconciliation.
5. **AHC entity 1220 cleanup** -- after reattributing South Roanoke rows, check if entity 1220 has any remaining rows. If not, it can be deprecated.
6. **Chancellor's Village (id 16017)** -- still missing county (Spotsylvania or Fredericksburg City). Separate fix needed.
7. **South Roanoke do_we_serve/mh_flag discrepancy** -- ALF row 15889 (True/True) vs SNF row 16246 (False/False). Needs business rule decision.

> **DO NOT EXECUTE -- REVIEW ONLY**
