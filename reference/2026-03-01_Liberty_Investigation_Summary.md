# Liberty Senior Living Investigation — Summary

**Date:** 2026-03-01
**Scope:** Proof-of-concept corporate attribution audit
**Operator:** Liberty Senior Living (NC-based, 64 facilities per website)

---

## Background

After completing the V21.2 CMS Chain ID enhancement (320 Corporate_Name corrections, 312 Independent-to-Corporate reclassifications), we selected Liberty Senior Living as a proof-of-concept to test ALF corporate attribution quality. Liberty was chosen because it operates both SNFs (Liberty Health & Rehab, 41 sites) and ALFs (Liberty Senior Living, 23 communities) with a clear public website listing all locations by division.

## What We Found

The database contains **58 rows** attributable to Liberty across **46 unique addresses**, but scattered across **15 different Corporate_Name strings**. Only 41 rows use the correct name (`LIBERTY SENIOR LIVING`).

### The Three Risks

**1. Phantom ALF Records (7 addresses, all served)**

At 7 addresses, NIC Maps created an ALF row that duplicates an existing CMS SNF record — same building, nearly identical name, different bed counts. Liberty's website confirms these cities have SNFs only, no ALF operations.

| City | SNF Name (CMS) | ALF Name (NIC Maps) |
|------|----------------|---------------------|
| Burlington | LIBERTY COMMONS NURSING & REHAB ALAMANCE | LIBERTY COMMONS NURSING AND REHAB OF ALAMANCE |
| Louisburg | LOUISBURG HEALTHCARE & REHABILITATION CENTER | LOUISBURG HEALTHCARE & REHABILITATION CENTER |
| Roxboro | ROXBORO HEALTHCARE & REHAB CENTER | ROXBORO HEALTHCARE AND REHABILITATION CENTER |
| Sanford | LIBERTY COMMONS NSG AND REHAB CTR OF LEE COUNTY | LIBERTY COMMONS NSG AND REHAB OF LEE COUNTY |
| Warrenton | WARREN HILLS NURSING CENTER | WARREN HILLS NURSING CENTER ALF / SNF |
| Yadkinville | YADKIN NURSING CARE CENTER | YADKIN NURSING CENTER |
| Canton | (no SNF row) | SILVER BLUFF VILLAGE-SNF (classified ALF despite name) |

Canton's Silver Bluff Village-SNF is confirmed as an SNF in the Eventus Facility Database (MH only, Census 15). NIC Maps classified it as ALF even though the facility name contains "SNF."

All 7 addresses are served. The phantom ALF rows create double-counted revenue opportunities.

**2. Hidden Corporate Ownership (11 facilities under LLC/PROPCO names)**

NIC Maps uses property-holding company names instead of operating company names for ALF records. Under the Four-Rule hierarchy, these unique LLCs count as 1 and classify as Independent.

| Facility | NIC Maps Corporate_Name | Ownership |
|----------|------------------------|-----------|
| THE TERRACE AT BRIGHTMORE OF SOUTH CHARLOTTE | 10225 OLD ARDREY KELL OPCO, LLC | Independent |
| BRIGHTMORE OF WILMINGTON (2 rows) | blank / BRIGHTMORE PROPERTIES INCI LLC | Independent |
| CAROLINA BAY AT AUTUMN HALL | 630 CAROLINA BAY NC PROPCO LLC | Corporate* |
| HAYES BARTON PLACE | BUDLEIGH EAST MULTIFAMILY LLC | Independent |
| KEMPTON OF CHARLESTON | blank / NOT AVAIL FROM COUNTY | Independent |
| THE KEMPTON OF HERMITAGE | STAR GROUP OF HERMITAGE LLC | Independent |
| KEMPTON OF JACKSONVILLE | LIBERTY COMMONS ASSISTED LIVING OF ONSLOW COUNTY, LLC | Independent |
| KEMPTON OF ROCK HILL | 1611 CONSTITUTION BLVD PROPCO | Independent |
| OAKLEAF VILLAGE AT LEXINGTON | 800 N LAKE PROPCO LLC | Independent |
| PISGAH VALLEY RETIREMENT CENTER | PISGAH VALLEY RETIREMENT CENTER PROPERTIES LLC | Corporate* |
| SOUTH BAY AT MOUNT PLEASANT | MT PLEASANT SENIOR HOUSING I PROPCO | Corporate* |
| THE BARCLAY AT SOUTHPARK | SOUTHPARK TOWERS PROPCO LLC | Independent |

*Corporate because multiple facilities share the LLC name, but still not attributed to Liberty.

**3. Missing Facilities and IL/Active Adult Contamination (5-7 communities)**

5-7 Liberty ALF communities from their website are not in the database at all. Several — particularly the "Inspire" brand (Briar Chapel, Brunswick Forest, Royal Park, Sandhill) — are marketed as **55+ Active Adult / Independent Living** communities, not licensed ALFs.

Inspire Brunswick Forest (6146 Liberty Hall Dr, Leland NC) was confirmed as a 55+ senior apartment community. These residents are healthy, independent adults — not the population Eventus serves with PCP and MH clinical services. If NIC Maps includes IL communities in its ALF data, our TAM/SAM is inflated with zero-opportunity facilities.

## Method

1. Extracted all database rows with Liberty-linked Corporate_Names
2. Grouped by normalized address to identify multi-row sites (12 found)
3. Cross-referenced against Liberty's two website divisions:
   - Liberty Health & Rehab (SNFs): 41 sites listed by city
   - Liberty Senior Living (ALFs): 23 communities listed by name
4. Classified multi-row addresses: city on both website lists = campus, city on one list only = likely duplicate
5. Matched the 23 website ALF communities to database by name, address, and city
6. Searched nearby cities and keyword variants for the unmatched communities
7. Looked up actual addresses for unmatched facilities to confirm gaps

## Key Insight

The user's cross-reference of Liberty's two website divisions was the breakthrough. If a location were a true campus (SNF + separate ALF at the same address), it would appear on **both** website lists. Cities appearing on only the SNF list cannot have a real ALF — any ALF row at those addresses is a phantom duplicate.

## Scale of Risk

These three risks are structural — they arise from how NIC Maps records data, not from anything specific to Liberty. A preliminary scan shows 180+ distinct PROPCO-pattern and 50+ OPCO-pattern Corporate_Names in the database, suggesting the hidden ownership problem alone could affect hundreds of ALF records.

## Recommended Next Steps

| Priority | Action | Approach |
|----------|--------|----------|
| 1 | **Duplicate audit** | Address-match all 15,243 SNFs against all 11,024 ALFs. Same address + same city = flag for review. Scriptable. |
| 2 | **PROPCO/OPCO inventory** | Pull all LLC-pattern Corporate_Names, research parent operators for largest clusters first. |
| 3 | **IL/ALF distinction** | Check state licensing databases to confirm which NIC Maps records hold actual ALF licenses vs IL designations. |
| 4 | **Cure Liberty** | Rename confirmed ALFs to `LIBERTY SENIOR LIVING`, remove phantom duplicates, rerun Four-Rule. |

## Files Created

| File | Purpose |
|------|---------|
| `reference/Risk_ALF_Corporate_Attribution_and_Data_Quality.md` | Full risk documentation with name variation inventory and cure plan |
| `reference/2026-03-01_Liberty_Investigation_Summary.md` | This summary |

## Related

- `changelogs/V21_1_to_V21_2_CMS_Chain_Enhancement.md` — V21.2 CMS Chain ID work that preceded this investigation
- `reference/Source_Data_Lineage.md` — upstream data sources including NIC Maps
- Liberty Senior Living website: two divisions (Liberty Health & Rehab for SNFs, Liberty Senior Living for ALFs)

---

*Investigation conducted 2026-03-01. Cure pending.*
