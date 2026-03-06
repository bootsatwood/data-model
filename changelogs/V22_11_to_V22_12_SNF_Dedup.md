# V22.11 -> V22.12: SNF Same-Address Deduplication

**Date:** 2026-03-06
**Script:** `scripts/v22_12_snf_dedup.py`
**Input:** `1_Combined_Database_FINAL_V22_11.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_12.xlsx`

---

## Summary

Removes 255 duplicate SNF rows where the same facility appeared twice at the same address. Each pair was verified by cross-referencing against CMS Provider Info to confirm a single CCN (CMS Certification Number) at the address. CCNs persist through ownership changes, so 1 CCN = 1 facility = duplicate row.

## Method

1. Find addresses with 2+ SNF rows sharing the same normalized facility name (260 found)
2. Cross-reference each address against `Source_CMS_NH_ProviderInfo_Feb2026.csv` for CCN count
3. 1 CCN = confirmed duplicate (255); Multiple CCNs = legitimate separate facilities (0); No CMS match = skip (5)
4. For each confirmed pair, keep the row with better data quality (served status > corporate name > attribution source > field completeness)

## Results

| CCN Result | Addresses | Served |
|---|---|---|
| 1 CCN (confirmed duplicate) | 255 | 23 |
| Multiple CCNs (legitimate) | 0 | 0 |
| No CMS match (skipped) | 5 | 1 |

### Key Observations

- **100% confirmation rate** — every CMS-matched pair had exactly 1 CCN. Zero false positives.
- **0 served rows lost** — in all 23 served pairs, the served row was kept and the unserved duplicate removed.
- **Typical pattern:** One row from CMS SNF source (often blank corporate name from pre-V22.3), one from CMS Provider Info or other import with corporate attribution. The row with corporate name/attribution source was kept.
- **4 corporate name conflicts** (both rows had different corp names, both LEGACY): kept operating company name over PROPCO/real estate LLC name.

### Corporate Name Conflicts (4 pairs)

| Facility | City, State | Kept Corp | Removed Corp | Reason |
|---|---|---|---|---|
| LECOM AT SNYDER MEMORIAL | Marienville, PA | WINDSOR HOUSE, INC. | SNYDER MEMORIAL REAL ESTATE LLC | PROPCO |
| UNIVERSAL HEALTH CARE LILLINGTON | Lillington, NC | CHOICE HEALTH MANAGEMENT | 1995 E CORNELIUS HARNETT BLVD LLC | PROPCO |
| SAPPHIRE CARE AND REHAB CENTER | East Stroudsburg, PA | PRIORITY HEALTHCARE GROUP | GPH EAST STROUDSBURG | PROPCO variant |
| NORTHERN LAKES NURSING AND REHAB | Angola, IN | PULASKI MEMORIAL HOSPITAL | WILLIAMS STREET NURSING LLC | PROPCO |

### No CMS Match (5 pairs, skipped)

| Facility | City, State | Served |
|---|---|---|
| CHERRY POINT BAY NURSING AND REHAB | Havelock, NC | Yes |
| MOUNTAIN VIEW CARE AND REHAB | Scranton, PA | No |
| OAK GLEN HEALTHCARE AND REHAB | Lewisburg, PA | No |
| PENDER MEMORIAL HOSP SNF | Burgaw, NC | No |
| RICHMOND PINES HEALTHCARE AND REHAB | Hamlet, NC | No |

## Change Counts

| Metric | Count |
|---|---|
| Rows removed | 255 |
| Served rows removed | 0 |
| Corporate name changes | 0 |
| Ownership reclassifications | 0 |

## Row Counts

| Metric | V22.11 | V22.12 | Delta |
|---|---|---|---|
| Total | 26,179 | 25,924 | -255 |
| SNF | 15,239 | 14,984 | -255 |
| ALF | 10,880 | 10,880 | 0 |
| ILF | 60 | 60 | 0 |
| Served | 1,657 | 1,657 | 0 |

## State Distribution of Removed Rows

| State | Removed |
|---|---|
| OH | 71 |
| PA | 66 |
| NC | 54 |
| IN | 39 |
| VA | 11 |
| TN | 6 |
| KY | 5 |
| SC | 3 |

## Remaining Same-Address Duplicates

After V22.12, the following same-type same-address categories remain:
- **SNF different-name pairs:** 156 addresses (need individual review — different names may be legitimate or may be rename/CHOW pairs)
- **ALF exact-name pairs:** 246 addresses (no CCN available for ALFs — need NIC or state license cross-reference)
- **ALF different-name pairs:** 316 addresses
- **5 SNF no-CMS-match pairs:** Skipped, need manual verification
