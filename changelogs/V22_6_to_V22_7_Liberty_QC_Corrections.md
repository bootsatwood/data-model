# V22.6 -> V22.7: Liberty QC Corrections

**Date:** 2026-03-05
**Source:** Liberty Health website crosswalk vs Combined Database V22.6
**Input:** `1_Combined_Database_FINAL_V22_6.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_7.xlsx`
**Crosswalk scripts:** `scripts/build_liberty_crosswalk.py`, `scripts/liberty_crosswalk_match.py`
**CCN verification:** `Vault/02_Data_Model/Reference/Source_CMS_NH_ProviderInfo_Feb2026.csv`

---

## Summary

Website-to-database crosswalk identified 10 extra DB rows beyond the 66 confirmed Liberty locations (64 website + 2 GLR-only). 9 approved for deletion. 1 service flag correction.

## Master Location Count

| Source | Count |
|--------|-------|
| Liberty Health & Rehab website (SNF) | 41 |
| Liberty Senior Living website (ALF) | 23 |
| GLR Facility DB only (not on website) | 2 |
| **Total confirmed locations** | **66** |

The 2 GLR-only facilities: Pigeon Valley Rest Home (55 Lake Dr, Canton NC) and Snow Hill Assisted Living (1328 SE 2nd St, Snow Hill NC). Both served.

---

## Deletions (9 rows)

### Group 1: CMS SNF Duplicates (6 rows)

Same CCN, same address, same facility name, same SNF designation. Second row is a data import artifact. Delete the duplicate row (row B), keep row A.

| Facility | Address | City | CCN | Row A Beds | Row B Beds | Variance |
|----------|---------|------|-----|------------|------------|----------|
| Swift Creek Health Center | 221 Brightmore Dr | Cary, NC | 345577 | 28 | 38 | 26% |
| Liberty HC Svcs of Golden Years | 7348 North West St | Falcon, NC | 345367 | 58 | 77 | 25% |
| Woodlands N&R Center | 400 Pelt Dr | Fayetteville, NC | 345481 | 80 | 90 | 11% |
| Woodhaven Nursing Center | 1150 Pine Run Dr | Lumberton, NC | 345054 | 115 | 130 | 12% |
| The Foley Center at Chestnut Ridge | 621 Chestnut Ridge Pkwy | Blowing Rock, NC | 345045 | 92 | 112 | 18% |
| Bradley Creek Health Center | 740 Diamond Shoals Rd | Wilmington, NC | 345571 | 30 | 40 | 25% |

**Method:** CCN lookup in CMS NH Provider Information (Feb 2026) confirmed 1 certification number per address. Bed variance is consistent with different CMS data snapshots, not separate facilities.

### Group 2: Pisgah Manor Duplicate (1 row)

| Facility | Address | City | CCN | Keep (Beds) | Delete (Beds) | Variance |
|----------|---------|------|-----|-------------|---------------|----------|
| Pisgah Manor | 104 Holcombe Cove Rd | Candler, NC | 345393 | 118 | 188 | 37% |

Same CCN, same address, same SNF. Larger bed variance (37%) but confirmed 1 CCN. Facility is unserved so bed count cannot be verified against Facility DB. **Decision: keep the lesser bed count (118).**

### Group 3: Liberty Commons Alamance ALF (1 row)

| Facility | Address | City | Type | Beds | Census | Served |
|----------|---------|------|------|------|--------|--------|
| Liberty Commons Nursing and Rehab of Alamance | 791 Boone Station Dr | Burlington, NC | ALF | 123 | 98 | Yes (MH) |

**Delete.** User confirmed only the SNF exists at this address. There is no ALF operation at Liberty Commons Alamance. The ALF row is a phantom created by NIC Maps (same pattern as V22.0 phantom fix). The SNF row (Liberty Commons Nursing & Rehab Alamance, SNF, 122 beds, served INT) is retained.

**Service flag note:** The deleted ALF row was marked served (MH). This service is already captured on the SNF row (served, INT). No service data is lost.

### Group 4: Silver Bluff Village-SNF (1 row)

| Facility | Address | City | Type in DB | Beds | Census | Served |
|----------|---------|------|------------|------|--------|--------|
| Silver Bluff Village-SNF | 100 Silver Bluff Dr | Canton, NC | ALF | 86 | 69 | Yes (MH) |

**Delete.** This row is classified as ALF in the database but has "SNF" in the facility name. It is a duplicate of Silver Bluff Inc (SNF, 131 beds, served MH) at the same address. The Facility DB name is Silver Bluff Village-SNF.

**Retained rows at 100 Silver Bluff Dr:**
- Silver Bluff Inc (SNF, 131 beds, 117 census, served MH) — the real SNF
- Silver Bluff Village-Arrowhead Cove (ALF, 12 beds, 10 census, served MH) — the real ALF

---

## Service Flag Correction (1 row)

| Facility | Address | City | Current Flag | Corrected Flag |
|----------|---------|------|-------------|----------------|
| Woodlands N&R Center | 400 Pelt Dr | Fayetteville, NC | Do_We_Serve=Yes, MH=Yes | Do_We_Serve=No, MH=No |

**Reason:** User confirmed Eventus does not serve this facility. Their three Woodlands facilities are in OH (2) and VA (1). The Fayetteville NC facility is a Liberty Health SNF (confirmed on website) but the served/MH flag is incorrect — likely a fuzzy name match error during GLR import.

---

## Change Counts

| Metric | Count |
|--------|-------|
| Rows deleted | 9 |
| Service flag corrections | 1 |
| Net row delta | -9 |
| Resulting LIBERTY row count | 67 |
| Confirmed Liberty locations | 66 |

---

## 10 Website Locations Not in DB (No Action — Documentation Only)

These are already counted in the 66 master location count. They are gaps in the DB, not new locations.

### 4 LHR (SNF) — Real clinical opportunities, should be added when data available

| Facility | Address | City | St |
|----------|---------|------|----|
| Inn at Quail Haven Village | 155 Blake Rd | Pinehurst | NC |
| Parkview Health & Rehab | 1718 Legion Rd | Chapel Hill | NC |
| Bloomsbury at Hayes Barton Place | 2750 Oberlin Rd | Raleigh | NC |
| Preserve at Fairfield Glade | 100 Samaritan Way | Crossville | TN |

### 6 LSL (ALF) — Not clinical opportunities

| Facility | Address | City | St | Reason |
|----------|---------|------|----|--------|
| The Carrollton | 701 S Carrollton Ave | New Orleans | LA | Out of footprint |
| Inspire Briar Chapel | 152 Market Chapel Rd | Pittsboro | NC | 55+ IL, not licensed ALF |
| Inspire Brunswick Forest | 6146 Liberty Hall Dr | Leland | NC | 55+ IL, not licensed ALF |
| Inspire Royal Park | 4101 Glenloch Circle | Matthews | NC | 55+ IL, not licensed ALF |
| Inspire Sandhill | 440 Town Center Place | Columbia | SC | 55+ IL, not licensed ALF |
| The Peninsula of Charleston | 625 King St | Charleston | SC | New CCRC, under construction |

---

## Revenue Impact

| Change | Current Rev | Integration Rev | New Biz Rev |
|--------|-------------|-----------------|-------------|
| Woodlands served flag fix | -$45,836 | -$301,135 | +new biz for both rows |
| Alamance ALF deletion (served MH) | -$70,119 | -$292,432 | n/a |
| Silver Bluff Village-SNF deletion (served MH) | -$49,370 | -$205,896 | n/a |
| 6 CMS SNF dupe deletions (all unserved) | $0 | $0 | varies |
| Pisgah Manor dupe deletion (unserved) | $0 | $0 | varies |

**Note:** Alamance and Silver Bluff service is already captured on the retained rows at those addresses (SNF INT and SNF MH respectively). The revenue reduction reflects removal of phantom double-counting, not loss of actual service.
