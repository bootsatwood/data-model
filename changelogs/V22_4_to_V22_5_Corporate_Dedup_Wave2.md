# V22.4 -> V22.5: Corporate Name Deduplication — Wave 2

**Date:** 2026-03-05
**Script:** `scripts/corporate_dedup_fix.py` (updated for Wave 2)
**Input:** `1_Combined_Database_FINAL_V22_4.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_5.xlsx`
**Analysis:** Continued manual RA research from V22.4 dedup session

---

## Summary

Second wave of corporate name consolidations from the ongoing dedup review. Three consolidations where CMS and GLR use different spellings for the same operator.

## Corporate Name Consolidations

| Old Name | Canonical Name | Rows | Served | Evidence |
|---|---|---|---|---|
| COMMUNICARE HEALTH | COMMUNICARE | 119 | 1 | CMS uses "CommuniCare Health", GLR/served account uses "CommuniCare". Same facilities at same addresses (IN, OH, MD, VA, WV, PA). |
| AVARDIS HEALTH | AVARDIS | 4 | 4 | GLR suffix variant. All VA facilities, all served. Same operator. |
| HILL VALLEY HEALTHCARE | Hill Valley | 41 | 2 | CMS uses "Hill Valley Healthcare", GLR uses "Hill Valley". Zero address overlap confirmed — all 41 CMS rows are distinct facilities from the 9 GLR rows. Same company per ProPublica (39 affiliated SNFs). VA, WV, KY, MD, WA, NV, TN, IL. |

## Change Counts

| Metric | Count |
|---|---|
| Corporate Name renames | 164 |
| Facility reattributions | 0 |
| Ownership reclassifications | 0 |
| Total rows modified | 164 |

## Research Notes from This Session

### Clusters Researched — No Action Needed
- **Eldercare Partners / Community Eldercare Services / Guardian Elder Care** — three separate companies (KY vs MS/TN vs PA/WV)
- **American Healthcare LLC / American Health Foundation / American Health Communities / American Health Management Group** — four separate companies (VA vs OH/PA vs TN vs SC)
- **Sunnyside Communities** — single corp name, clean (9 rows, all VA, all served)
- **Runk & Pratt** — single corp name, clean (8 rows, all VA, 7 served)

### Deferred Items
- **MFA vs MFA MARYVILLE RE LLC** — MFA (17 rows, 16 served, NC/VA) vs MFA Maryville RE LLC (2 rows, 0 served, TN). Affiliation unclear, deferred.
- **BHP/Encore** (from V22.4 session) — still unresolved

### CMS vs GLR Naming Pattern
Recurring pattern: CMS appends "Health", "Healthcare", or "Health Services" to operator names that GLR stores as shorter canonical names. This wave resolved three instances; more likely exist in the unreviewed fuzzy match pairs.
