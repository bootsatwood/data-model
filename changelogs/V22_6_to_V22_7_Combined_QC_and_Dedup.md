# V22.6 -> V22.7: Liberty QC + Corporate Dedup Wave 4

**Date:** 2026-03-05
**Script:** `scripts/v22_7_fix.py`
**Input:** `1_Combined_Database_FINAL_V22_6.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_7.xlsx`

---

## Summary

Combined update: Liberty website crosswalk QC corrections + corporate name deduplication for Singh/Waltonwood, Cedarhurst, and Spring Arbor.

## Part A: Liberty QC Corrections

See `V22_6_to_V22_7_Liberty_QC_Corrections.md` for full details including CCN verification, revenue impact, and 10 website locations not in DB.

### Deletions (9 rows)

| Group | Facility | Address | City, NC | Reason |
|---|---|---|---|---|
| CMS SNF dupe | Swift Creek Health Center | 221 Brightmore Dr | Cary | Same CCN as retained row |
| CMS SNF dupe | Liberty HC Svcs of Golden Years | 7348 North West St | Falcon | Same CCN as retained row |
| CMS SNF dupe | Woodlands N&R Center | 400 Pelt Dr | Fayetteville | Same CCN as retained row |
| CMS SNF dupe | Woodhaven Nursing Center | 1150 Pine Run Dr | Lumberton | Same CCN as retained row |
| CMS SNF dupe | The Foley Center at Chestnut Ridge | 621 Chestnut Ridge Pkwy | Blowing Rock | Same CCN as retained row |
| CMS SNF dupe | Bradley Creek Health Center | 740 Diamond Shoals Rd | Wilmington | Same CCN as retained row |
| CMS SNF dupe | Pisgah Manor | 104 Holcombe Cove Rd | Candler | Same CCN, keep lower bed count (118) |
| ALF phantom | Liberty Commons Alamance | 791 Boone Station Dr | Burlington | No ALF exists, SNF row retained |
| ALF phantom | Silver Bluff Village-SNF | 100 Silver Bluff Dr | Canton | Phantom ALF, SNF + real ALF retained |

### Service Flag Correction (1 row)

| Facility | City | Old | New | Reason |
|---|---|---|---|---|
| Woodlands N&R Center | Fayetteville, NC | Served=Yes, MH=Yes | Served=No, MH=No | Eventus does not serve this facility |

## Part B: Corporate Name Consolidations

### Singh/Waltonwood (30 rows -> 19 rows)

All Waltonwood facilities are operated by Singh Management Group.

| Old Name | Rows Renamed |
|---|---|
| Singh Developments (Waltonwood) | 9 |
| Waltonwood | 9 |
| Waltonwood Senior Living | 2 |
| WALTONWOOD AT CARY, LLC | 1 |

Canonical: **SINGH** (GLR authority)

11 duplicate rows removed (all unserved). Duplicates from NIC Maps + state licensing data at same addresses. Website confirms 7 MI + 5 NC + 1 VA = 13 active locations.

### Cedarhurst (57 rows -> 54 rows)

| Old Name | Rows | Fix |
|---|---|---|
| CEDARHURST SENOR LIVING | 9 | Typo: "SENOR" -> "SENIOR" |

Canonical: **CEDARHURST SENIOR LIVING**

3 duplicate rows removed (all unserved, confirmed against Facility DB):
- Cedar Creek Of Bloomington (dupe of Cedar Creek Assisted Living, 2770 S Adams Rd, Bloomington IN)
- Cedar Creek Of Marion (dupe of Cedar Hurst Living Of Marion, 725 W 50th St, Marion IN)
- Cedarhurst Of Beaumont (exact dupe, 1165 Monarch St, Lexington KY)

### Spring Arbor (21 rows -> 16 rows)

| Old Name | Rows Renamed |
|---|---|
| Spring Arbor Senior Living | 9 |
| SPRING ARBOR KILL DEVIL HILLS NC TENANT, LLC | 1 |
| SPRING ARBOR COTTAGE OF FREDERICKSB | 1 |

Canonical: **SPRING ARBOR MANAGEMENT** (GLR authority)

5 duplicate rows removed (all unserved). Duplicates at same addresses as served GLR care-type rows (Albemarle, Apex, Cary x2, Greensboro).

### Atrium — No Action

Three separate organizations confirmed via web research:
- **ATRIUM HEALTH** (13 rows, 12 served) — Major NC/KY health system, atriumhealth.org
- **ATRIUM CENTERS** (26 rows, 0 served) — Employee-owned MI/OH/WI SNF operator, atriumlivingcenters.com
- **Atrium Health & Senior Living** (1 row, 0 served) — Defunct FL operator (receivership 2018, sold to North Shore 2019)

## Change Counts

| Metric | Count |
|---|---|
| Corporate Name renames | 41 |
| Service flag corrections | 1 |
| Rows deleted | 28 |
| Ownership reclassifications | 2 (Independent -> Corporate) |
| Net row delta | -28 |

## Row Counts

| Metric | V22.6 | V22.7 | Delta |
|---|---|---|---|
| Total | 26,207 | 26,179 | -28 |
