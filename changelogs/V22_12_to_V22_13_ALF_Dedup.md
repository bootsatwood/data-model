# V22.12 -> V22.13: ALF Same-Address Deduplication

**Date:** 2026-03-06
**Script:** `scripts/v22_13_alf_dedup.py`
**Input:** `1_Combined_Database_FINAL_V22_12.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_13.xlsx`

---

## Summary

Removes 215 duplicate ALF rows where the same facility appears 2+ times at the same address with the same (or compatible) corporate name. Unlike SNFs, ALFs have no CCN for verification. Instead, exact facility name match + corporate name agreement serves as the duplicate signal.

## Method

1. Find addresses with 2+ ALF rows sharing the same normalized facility name
2. Filter to high-confidence: same corporate name, both blank, or one has corp + one blank
3. Score each row by data quality (served status > corporate name > attribution source > field completeness)
4. Keep the highest-scoring row, remove the rest

## Scope

| Category | Addresses | Rows Removed |
|---|---|---|
| Exact-name + same corp (pairs) | 188 | 188 |
| Exact-name + one blank corp (pairs) | 9 | 9 |
| Exact-name + same corp (triples) | 9 | 18 |
| **Total** | **206** | **215** |

### Deferred (not addressed)

| Category | Addresses | Reason |
|---|---|---|
| Exact-name + different corps | 40 | Likely PROPCO/OPCO — needs individual review |
| Different-name pairs | 316 | Could be legitimate campus variants (MC vs AL) |

## Key Observations

- **0 both-served conflicts** — in all served pairs, only one row was served. The served row was always kept.
- **0 served rows lost** — all 113 served addresses correctly retained the served row.
- **NC dominates** (119 of 215 removed) — NC ALF data had extensive duplication, likely from overlapping GLR + NIC imports.
- **Triples** followed same pattern: 3 identical rows (often GLR + NIC + LEGACY), keep the best-scored one.

## Change Counts

| Metric | Count |
|---|---|
| Rows removed | 215 |
| Served rows removed | 0 |
| Pairs processed | 197 |
| Triples processed | 9 |

## Row Counts

| Metric | V22.12 | V22.13 | Delta |
|---|---|---|---|
| Total | 25,924 | 25,709 | -215 |
| SNF | 14,984 | 14,984 | 0 |
| ALF | 10,880 | 10,665 | -215 |
| ILF | 60 | 60 | 0 |
| Served | 1,657 | 1,657 | 0 |

## State Distribution of Removed Rows

| State | Removed |
|---|---|
| NC | 119 |
| OH | 32 |
| KY | 21 |
| IN | 17 |
| IL | 10 |
| GA | 6 |
| VA | 4 |
| SC | 3 |
| MI | 1 |
| PA | 1 |
| TN | 1 |

## Remaining Same-Address ALF Duplicates

| Category | Addresses | Notes |
|---|---|---|
| Exact-name different corps | 40 | Mostly PROPCO vs OPCO, all LEGACY sourced |
| Different-name pairs | 316 | Includes campus variants (MC vs AL), co-located buildings |
