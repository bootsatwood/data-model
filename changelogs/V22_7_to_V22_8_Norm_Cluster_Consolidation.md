# V22.7 -> V22.8: Exact Norm Cluster Consolidation + Typo Fixes

**Date:** 2026-03-06
**Script:** `scripts/v22_8_norm_clusters.py`
**Input:** `1_Combined_Database_FINAL_V22_7.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_8.xlsx`

---

## Summary

Consolidated 20 exact norm clusters (same entity, different spelling/case/formatting) and fixed 4 obvious typos identified in fuzzy match review. No rows deleted.

## Part A: Exact Norm Cluster Consolidations (19 clusters, 189 renames)

All clusters were identified by the `corporate_name_dedup.py` analysis and listed in `Corporate_Name_Dedup_Review_ra_v2.xlsx`, Sheet "Exact Norm Clusters."

### GLR-Authoritative (9 clusters)

| Cluster | Old Name | New Name (GLR Canonical) | Rows Renamed |
|---|---|---|---|
| 1 | PRUITTHEALTH | PRUITT HEALTH | 109 |
| 2 | SUNRISE SENIOR LIVING | Sunrise Senior Living | 6 |
| 3 | OTTERBEIN SENIORLIFE | OTTERBEIN SENIOR LIFE | 29 |
| 4 | MILLER'S MERRY MANOR | MILLERS MERRY MANOR | 15 |
| 9 | KISSITO HEALTHCARE | Kissito Healthcare | 2 |
| 10 | LYON HEALTHCARE | Lyon Healthcare | 6 |
| 12 | CrownPointe Communities | CROWN POINTE COMMUNITIES | 1 |
| 14 | BLUE CENTRAL GROUP? | BLUE CENTRAL GROUP | 1 |
| 20 | MP CARE II, LLC | MPCARE II, LLC | 1 |

### Highest-Count Canonical (10 clusters)

| Cluster | Old Name | New Name | Rows Renamed |
|---|---|---|---|
| 5 | PRESBYTERIAN SENIORCARE NETWORK | Presbyterian Senior Care Network | 7 |
| 6 | BeehiveHomes | BeeHive Homes | 1 |
| 7 | JUNIPER COMMUNITIES | Juniper Communities | 3 |
| 8 | MERRILL GARDENS L.L.C | Merrill Gardens | 2 |
| 11 | Citizens Memorial Healthcare | CITIZENS MEMORIAL HEALTH CARE | 1 |
| 15 | Prelude Homes and Services | Prelude Homes & Services | 1 |
| 16 | MILL CREEK MANOR, LLC | MILLCREEK MANOR | 1 |
| 17 | Caring Place Healthcare Group | CARING PLACE HEALTHCARE GROUP | 1 |
| 18 | North Port Retirement Centers, Inc. | Northport Retirement Centers, Inc | 1 |
| 19 | Rest Haven Homes, Inc. | Resthaven Homes, Inc | 1 |

Note: Cluster 13 (Greencroft) was already consolidated in V22.6.

## Part B: Typo Fixes (4 fixes, 10 renames)

Identified in `Corporate_Name_Dedup_Review_ra_v2.xlsx`, Sheet "Fuzzy Matches" as edit-distance matches with obvious misspellings.

| Old Name | New Name | Rows | Fix Type |
|---|---|---|---|
| MAJETIC CARE | MAJESTIC CARE | 1 | Missing 'S' |
| HARMONY SENOR SERVICES | HARMONY SENIOR SERVICES | 5 | Missing 'I' (same pattern as Cedarhurst V22.7) |
| EXCEPTIONAL LIVING CENTER | EXCEPTIONAL LIVING CENTERS | 1 | Singular -> plural |
| OAKDALE SENIORS ALLIANCE | OAKDALE SENIOR ALLIANCE | 3 | SENIORS -> SENIOR (served variant = canonical) |

## Part C: Ownership Reclassifications (13 Independent -> Corporate)

Consolidation caused these names to cross the 2-facility threshold for Corporate classification:

| Facility | City, State | Corporate Name |
|---|---|---|
| Majestic Care of Deming Park | Terre Haute, IN | MAJESTIC CARE |
| Brookstone Terrace of Thomasville (x2) | Thomasville, NC | MPCARE II, LLC |
| Mill Creek Manor | Statesville, NC | MILLCREEK MANOR |
| Kirtland Woods of Journey | Kirtland, OH | EXCEPTIONAL LIVING CENTERS |
| The Lodge Retirement Community | Cincinnati, OH | CARING PLACE HEALTHCARE GROUP |
| Woods Edge Rehab & Nursing | Cincinnati, OH | BLUE CENTRAL GROUP |
| Autumn Village 2b | Jackson, GA | BeeHive Homes |
| Butterfield Residential Care Center | Bolivar, MO | CITIZENS MEMORIAL HEALTH CARE |
| CrownPointe of Spring Hill | Spring Hill, FL | CROWN POINTE COMMUNITIES |
| Harborview Acres | Port Charlotte, FL | Northport Retirement Centers, Inc |
| Prelude Homes & Services, LLC | Woodbury, MN | Prelude Homes & Services |
| Rest Haven Homes | Grand Rapids, MI | Resthaven Homes, Inc |

## Change Counts

| Metric | Count |
|---|---|
| Norm cluster renames | 189 |
| Typo fix renames | 10 |
| Total renames | 199 |
| Ownership reclassifications | 13 (all Ind -> Corp) |
| Rows deleted | 0 |
| Net row delta | 0 |

## Row Counts

| Metric | V22.7 | V22.8 | Delta |
|---|---|---|---|
| Total | 26,179 | 26,179 | 0 |
| SNF | 15,219 | 15,219 | 0 |
| ALF | 10,953 | 10,953 | 0 |
| ILF | 7 | 7 | 0 |
| Served | 1,657 | 1,657 | 0 |
| Distinct Corp Names | ~4,125 | ~4,102 | ~-23 |

## Post-Consolidation Corporate Counts

| Corporate Name | Total Rows | Served |
|---|---|---|
| PRUITT HEALTH | 126 | 31 |
| Sunrise Senior Living | 119 | 4 |
| MAJESTIC CARE | 53 | 21 |
| HARMONY SENIOR SERVICES | 50 | 5 |
| OTTERBEIN SENIOR LIFE | 36 | 14 |
| Presbyterian Senior Care Network | 19 | 0 |
| MILLERS MERRY MANOR | 19 | 3 |
| BeeHive Homes | 16 | 0 |
| EXCEPTIONAL LIVING CENTERS | 15 | 2 |
| Juniper Communities | 13 | 0 |
| Merrill Gardens | 13 | 0 |
| Kissito Healthcare | 12 | 11 |
| Lyon Healthcare | 9 | 3 |
| CITIZENS MEMORIAL HEALTH CARE | 7 | 0 |
| OAKDALE SENIOR ALLIANCE | 6 | 2 |
| CROWN POINTE COMMUNITIES | 6 | 1 |
| BLUE CENTRAL GROUP | 4 | 4 |
| Prelude Homes & Services | 4 | 0 |
| CARING PLACE HEALTHCARE GROUP | 3 | 1 |
| MILLCREEK MANOR | 3 | 0 |
| Northport Retirement Centers, Inc | 3 | 0 |
| Resthaven Homes, Inc | 3 | 0 |
| MPCARE II, LLC | 2 | 1 |
