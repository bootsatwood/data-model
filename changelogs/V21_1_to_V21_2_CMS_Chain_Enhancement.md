# V21.1 -> V21.2: CMS Chain ID Corporate Name Enhancement

**Date:** 2026-03-01
**Script:** `scripts/chain_update_v21_2.py`
**Input:** `1_Combined_Database_FINAL_V21_1.xlsx`
**Output:** `1_Combined_Database_FINAL_V21_2.xlsx`

---

## Summary

The Four-Rule ownership hierarchy classifies facilities by counting exact `Corporate_Name` strings. Many chain operators use per-facility LLCs (e.g., "OHI ASSET IN BEECH GROVE LLC"), so each LLC appears once and is classified Independent. CMS groups these under parent chains via Chain ID.

Cross-referencing our 6,314 matched footprint SNFs against the CMS NH Provider Info dataset (Feb 2026) found **320 facilities** we classified as Independent that CMS assigns to a chain. Updating their Corporate_Name and rerunning the Four-Rule hierarchy corrects the classification.

## Method

1. **Match** SNFs in 14 footprint states to CMS data by normalized address key (address + city + state)
2. **Filter** to facilities where our Ownership_Type = Independent and CMS has a non-blank Chain Name
3. **Classify** each match:
   - **Section A:** CMS chain name (normalized) matches an existing Corporate_Name in our database -> use our canonical spelling
   - **Section B:** CMS chain name is new to our taxonomy -> use CMS chain name directly
4. **Write** Corporate_Name changes to new V21.2 file
5. **Rerun** Four-Rule hierarchy across all 26,267 rows to recompute Ownership_Type

## Change Counts

| Metric | Count |
|--------|-------|
| **Corporate_Name changes** | **320** |
| Section A (existing name match) | 235 |
| Section B (new chain name) | 85 |
| Served facilities in scope | 15 |
| **Ownership_Type reclassifications** | **312** |
| Independent -> Corporate | 312 |
| Corporate -> Independent | 0 |
| Served reclassifications | 13 |

Note: 320 Corporate_Name changes produced 312 reclassifications (not 320) because 8 facilities had their Corporate_Name set to a chain with only 1 facility in our database at that point, keeping them Independent under Rule 4. As more facilities within those chains are updated, the count crosses the threshold.

## Database Totals (V21.2)

| Metric | V21.1 | V21.2 | Delta |
|--------|-------|-------|-------|
| Total Facilities | 26,267 | 26,267 | 0 |
| SNF | 15,243 | 15,243 | 0 |
| ALF | 11,024 | 11,024 | 0 |
| **Corporate** | **16,213** | **16,525** | **+312** |
| **Independent** | **10,054** | **9,742** | **-312** |
| Served | 1,659 | 1,659 | 0 |
| Barriers | 882 | 882 | 0 |

## Served Facility Reclassifications

These 13 served facilities were reclassified from Independent to Corporate. Revenue impact should be reviewed:

| Facility | State | New Corporate_Name | CMS Chain (ID) | Corp Count |
|----------|-------|--------------------|----------------|------------|
| ADVANCED HEALTHCARE CENTER | OH | HEALTH CARE FACILITY MANAGEMENT, LLC | (814) | 4 |
| GOLDEN YEARS HOMESTEAD | IN | GREENCROFT COMMUNITIES | (835) | 6 |
| GOOD SHEPHERD HEALTH AND REHABILITATION | KY | PLAINVIEW HEALTHCARE PARTNERS | (657) | 12 |
| GREENCROFT HEALTHCARE | IN | GREENCROFT COMMUNITIES | (835) | 6 |
| GREENFIELD SKILLED NURSING AND REHABILITATION | OH | MICHAEL SLYK | (812) | 7 |
| HAMILTON GROVE | IN | GREENCROFT COMMUNITIES | (835) | 6 |
| LIBERTY COMMONS NURSING & REHAB ALAMANCE | NC | LIBERTY SENIOR LIVING | (310) | 41 |
| OTTERBEIN MIDDLETOWN | OH | OTTERBEIN SENIORLIFE | (389) | 19 |
| PICKAWAY MANOR CARE CENTER | OH | OPTALIS HEALTH & REHABILITATION | (601) | 35 |
| PIKEVILLE NURSING AND REHAB CENTER | KY | EMERALD HEALTHCARE | (630) | 15 |
| SHELBY SKILLED NURSING AND REHABILITATION | OH | MICHAEL SLYK | (812) | 7 |
| THE PAVILION AT STOW FOR NURSING AND REHABILITATIO | OH | THE PAVILION GROUP | (514) | 6 |
| WESTCHESTER MANOR AT PROVIDENCE PLACE | NC | EVERYAGE SENIOR LIVING | (675) | 4 |

Note: 15 served facilities had Corporate_Name changes, but only 13 were reclassified. The remaining 2 stayed Independent because their chain has only 1 facility in our database (Rule 4).

## Top Chains by Facility Count (Independent -> Corporate)

| Chain | Facilities | Corp Count | States |
|-------|-----------|------------|--------|
| AMERICAN SENIOR COMMUNITIES | 16 | 156 | IN |
| TRILOGY HEALTH SERVICES | 14 | 237 | IN, MI, OH |
| SUMMIT HEALTHCARE CONSULTING | 9 | 9 | IL |
| SHAFIQ MALIK | 8 | 8 | MO |
| FOUNDATIONS HEALTH SOLUTIONS | 8 | 67 | OH |
| LIBERTY SENIOR LIVING | 7 | 41 | NC |
| MICHAEL SLYK | 7 | 7 | OH |
| DAVID OBERLANDER | 7 | 7 | OH |
| EVERCARE SKILLED NURSING | 6 | 6 | IL |
| GREENCROFT COMMUNITIES | 6 | 6 | IN |
| AVON HEALTHCARE | 6 | 6 | MI |
| Ebenezer Senior Living | 6 | 15 | MN |
| OPTALIS HEALTH & REHABILITATION | 6 | 35 | OH |
| SABER HEALTHCARE GROUP | 6 | 163 | NC, OH |

## Deferred: Both Corporate, Names Differ

~300 facilities are classified Corporate by both us and CMS, but with different chain names. These were not changed in this version. They likely represent:
- Subsidiary/parent name differences
- Recent acquisitions not yet reflected in one data source
- Regional vs national branding

These should be reviewed in a future version.

## QC Validation

- Snapshot baseline: 2026-03-01 16:17:24 (V21.1)
- Compare: 320 row changes detected (Corporate_Name only), no summary total changes
- Four-Rule: 312 Independent -> Corporate reclassifications, 0 reverse
- Validate: 0 FAIL, 1 WARN (stale scenario files), 21 PASS

## Data Source

- **CMS:** `Source_CMS_NH_ProviderInfo_Feb2026.csv` (CMS Provider Data Nursing Facility, dataset 4pq5-n9py, downloaded Feb 2026)
- **Matching:** Normalized address key (street abbreviation normalization + alphanumeric-only comparison)
- **Footprint states:** IN, KY, NC, OH, SC, VA, MI, IL, WI, MN, FL, MD, GA, MO

---

*Generated by `chain_update_v21_2.py` on 2026-03-01.*
