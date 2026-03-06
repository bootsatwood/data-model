# V22.5 -> V22.6: Corporate Name Deduplication — Wave 3

**Date:** 2026-03-05
**Script:** `scripts/corporate_dedup_fix.py` (updated for Wave 3)
**Input:** `1_Combined_Database_FINAL_V22_5.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_6.xlsx`

---

## Summary

Third wave of corporate name consolidations. Single consolidation plus removal of 3 duplicate/phantom rows.

## Corporate Name Consolidations

| Old Name | Canonical Name | Rows | Served | Evidence |
|---|---|---|---|---|
| GREENCROFT COMMUNITIES / Greencroft Communities | GREENCROFT | 5 | 1 | CMS/NIC uses "Greencroft Communities", GLR/served uses "Greencroft". Same facilities at overlapping addresses in Goshen IN, Demotte IN, Fort Wayne IN. |

## Change Counts

| Metric | Count |
|---|---|
| Corporate Name renames | 5 |
| Ownership reclassifications | 1 (Independent -> Corporate) |
| Rows removed (duplicates/phantoms) | 3 |
| Total rows modified | 5 |
| Net row delta | -3 |

## Rows Removed — Duplicates/Phantoms

Identified during Greencroft research, validated against Facility DB, removed.

| Row | Facility | Address | Type | Served | Reason |
|---|---|---|---|---|---|
| 4794 | Greencroft Goshen | 1225 Greencroft Dr, Goshen, IN | ALF | Yes | **Phantom** — no ALF in Facility DB. Only 1 SNF (150 consents) at this address. SNF row 4767 retained. |
| 19306 | Oak Grove Christian Retirement Village | 221 W Division St, Demotte, IN | SNF | No | **Duplicate** of row 5022 — same facility, same source (CMS), same address |
| 20674 | Walnut Hills Retirement Home | 4770 Olde Pump St, Walnut Creek, OH | ALF | No | **Duplicate** of row 13013 (Walnut Hills Retirement Center) — same address, both ALF, both GLR. Row 13013 is served, 20674 is not. |

**Script:** `scripts/remove_greencroft_dupes.py`
