# V22.8 -> V22.9: High-Confidence Fuzzy Match Consolidation

**Date:** 2026-03-06
**Script:** `scripts/v22_9_fuzzy_dedup.py`
**Input:** `1_Combined_Database_FINAL_V22_8.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_9.xlsx`

---

## Summary

Consolidated 14 high-confidence fuzzy match pairs (507 renames) identified in `Corporate_Name_Dedup_Review_ra_v2.xlsx`. Each pair was verified via GLR cross-reference, geographic analysis, and/or corporate research. Ambiguous pairs were deferred.

## Consolidations (14 pairs, 507 renames)

### GLR-Authoritative (10 pairs)

| Old Name | New Name (GLR Canonical) | Rows Renamed | Combined Total |
|---|---|---|---|
| GENESIS HEALTHCARE | GENESIS | 205 | 207 (4 served) |
| StoryPoint Group | STORYPOINT | 92 | 97 (5 served) |
| FOUNDATIONS HEALTH SOLUTIONS | FOUNDATIONS HEALTH | 67 | 69 (2 served) |
| PRINCIPLE LONG TERM CARE | PRINCIPLE | 37 | 63 (28 served) |
| Principle LTC | PRINCIPLE | 1 | (included above) |
| The Arbor Company | ARBOR COMPANY | 34 | 38 (2 served) |
| BICKFORD SENIOR LIVING | BICKFORD | 37 | 38 (1 served) |
| A PHOENIX SENIOR LIVING COMMUNITY | PHOENIX SENIOR LIVING | 2 | 46 (3 served) |
| TERRA BELLA | TerraBella Senior Living | 2 | 40 (11 served) |
| LIONSTONE | LIONSTONE CARE | 1 | 44 (23 served) |

### Other High-Confidence (4 pairs)

| Old Name | New Name | Rows Renamed | Basis |
|---|---|---|---|
| HCF MANAGEMENT INDIANA | HCF MANAGEMENT | 6 | CMS state-variant of GLR name |
| SRI MANAGEMENT GROUP | SRI Management | 1 | Same company, highest count |
| Evangelical Lutheran Good Samaritan Society/ Sandford | GOOD SAMARITAN SOCIETY | 21 | Full legal name -> CMS short form |
| THE EVANGELICAL LUTHERAN GOOD SAMARITAN SOCIETY | GOOD SAMARITAN SOCIETY | 1 | Same |

## Confirmed Different Entities (No Action)

| Entity A | Entity B | Reason |
|---|---|---|
| NATIONAL HEALTHCARE CORPORATION (86 rows, SE US: AL,GA,KY,MO,SC,TN,VA) | NATIONAL HEALTH CARE ASSOCIATES (42 rows, New England: CT,MA,ME,NH,NY,VT) | Completely different companies and geographies |
| LIFECARE (8 rows, IN only, GLR) | LIFE CARE CENTERS OF AMERICA (194 rows, national, CMS) | GLR identifies as separate IN-based operator |
| LIFE CARE CENTERS (2 rows, OH, GLR) | LIFE CARE CENTERS OF AMERICA (194 rows) | GLR identifies as separate entity |
| LIFE CARE SERVICES (75 rows, management co) | (all of the above) | Des Moines-based management company, separate |

## Deferred (Needs More Research)

| Pair | Rows | Issue |
|---|---|---|
| CASCADIA HEALTHCARE (44) / CASCADES HEALTHCARE (20) | 64 | Geographic overlap in ID/WA but uncertain affiliation |
| LAUREL HEALTH CARE COMPANY (2, GLR) / CIENA HEALTHCARE/LAUREL HEALTH CARE (86, CMS) | 88 | Acquisition/naming transition, GLR uses pre-acquisition name |

## Ownership Reclassifications (5 Independent -> Corporate)

| Facility | City, State | Corporate Name |
|---|---|---|
| Bickford of Greenwood | Greenwood, IN | BICKFORD |
| Gaither Suites at West Park | Paducah, KY | SRI Management |
| ALS Woodstock Inc | Woodstock, OH | LIONSTONE CARE |
| Good Samaritan Society - Northwood Retirement Community | Jasper, IN | GOOD SAMARITAN SOCIETY |
| Eden Fields Memory Care | Standish, MI | PRINCIPLE |

## Change Counts

| Metric | Count |
|---|---|
| Total renames | 507 |
| Ownership reclassifications | 5 (all Ind -> Corp) |
| Rows deleted | 0 |
| Net row delta | 0 |

## Row Counts

| Metric | V22.8 | V22.9 | Delta |
|---|---|---|---|
| Total | 26,179 | 26,179 | 0 |
| Served | 1,657 | 1,657 | 0 |

## Post-Consolidation Corporate Counts

| Corporate Name | Total Rows | Served |
|---|---|---|
| GENESIS | 207 | 4 |
| GOOD SAMARITAN SOCIETY | 112 | 0 |
| STORYPOINT | 97 | 5 |
| FOUNDATIONS HEALTH | 69 | 2 |
| PRINCIPLE | 63 | 28 |
| PHOENIX SENIOR LIVING | 46 | 3 |
| LIONSTONE CARE | 44 | 23 |
| TerraBella Senior Living | 40 | 11 |
| ARBOR COMPANY | 38 | 2 |
| BICKFORD | 38 | 1 |
| HCF MANAGEMENT | 38 | 5 |
| SRI Management | 38 | 0 |
