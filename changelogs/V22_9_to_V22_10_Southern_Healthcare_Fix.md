# V22.9 -> V22.10: Southern Healthcare Management Consolidation

**Date:** 2026-03-06
**Script:** `scripts/v22_10_southern_fix.py`
**Input:** `1_Combined_Database_FINAL_V22_9.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_10.xlsx`

---

## Summary

Resolves DCR #1 (Southern rename) and DCR #2 (missing facilities) simultaneously. The 43 "missing" Southern Healthcare Management facilities were in the database all along — attributed to "SOVEREIGN HEALTHCARE HOLDINGS" (the CMS chain/holding company name).

## Background

The original DCR identified that:
- CMS ownership records show 43 facilities under Southern Healthcare Management, LLC (FL 31, NC 10, GA 2)
- The database appeared to have only 33 facilities (later corrected to 3 after V22.1 Brookdale dedup)
- The "33" were actually Southern Assisted Living, Inc. (SALI) facilities — a different, defunct company acquired by Brookdale in 2006. Those were correctly renamed to BROOKDALE SENIOR LIVING in V22.1.

## Discovery

Cross-referencing the DCR's CMS facility list against the V22.9 database revealed:
- **SOVEREIGN HEALTHCARE HOLDINGS**: 43 rows, FL(31) + GA(2) + NC(10) — exact match to the DCR list
- NC facilities share addresses with GLR-confirmed Southern Healthcare Management facilities (co-located ALF+SNF campuses)
- "Sovereign Healthcare Holdings" is the holding/chain company; "Southern Healthcare Management, LLC" is the operating company

## Changes

| Old Name | New Name | Rows | Source |
|---|---|---|---|
| SOVEREIGN HEALTHCARE HOLDINGS | SOUTHERN HEALTHCARE MANAGEMENT, LLC | 43 | CMS chain name -> GLR operating company |
| SOUTHERN HEALTHCARE | SOUTHERN HEALTHCARE MANAGEMENT, LLC | 1 | LEGACY variant normalization |

## Post-Consolidation

| Metric | Value |
|---|---|
| SOUTHERN HEALTHCARE MANAGEMENT, LLC total rows | 46 |
| Served | 8 |
| States | FL(31), GA(2), NC(13) |
| Source breakdown | CMS(43), GLR(2), LEGACY(1) |

The 46 rows = 43 CMS facilities + 3 GLR ALF co-locations at NC addresses (Monroe, Raleigh, Sunnybrook).

## Change Counts

| Metric | Count |
|---|---|
| Total renames | 44 |
| Ownership reclassifications | 1 (Ind -> Corp) |
| Rows deleted | 0 |
| Net row delta | 0 |

## Row Counts

| Metric | V22.9 | V22.10 | Delta |
|---|---|---|---|
| Total | 26,179 | 26,179 | 0 |
| Served | 1,657 | 1,657 | 0 |

## DCR Impact

- **DCR #1 (Southern rename):** CLOSED. All facilities now under correct name.
- **DCR #2 (Missing facilities):** CLOSED. All 43 CMS facilities accounted for. No facilities are actually missing — they were present under the holding company name "SOVEREIGN HEALTHCARE HOLDINGS."
