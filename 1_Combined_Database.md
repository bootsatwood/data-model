# 1 — Combined Database

**Vault companion:** `new_02_Data_Model/Current/1_Combined_Database_FINAL_V21_1.xlsx`
**Current version:** V21.1
**Last updated:** 2026-02-26

---

## Purpose

The Combined Database is the master facility-level dataset for Eventus WholeHealth. It merges SNF (Skilled Nursing Facility) and ALF (Assisted Living Facility) records into a single unified view with standardized fields, geographic mapping, corporate ownership, and economic model inputs. It is the **single source of truth** for all facility data — all downstream files (scenarios, reports, scoring) inherit from it.

## Database Foundation (V21.1 Current)

| Metric | Count | % |
|--------|-------|---|
| **Total Facilities** | 26,271 | 100% |
| SNF Facilities | 15,244 | 58.0% |
| ALF Facilities | 11,027 | 42.0% |
| Corporate Facilities | 16,214 | 61.7% |
| Independent Facilities | 10,057 | 38.3% |
| Facilities We Serve | 1,663 | 6.3% |
| Facilities with Barriers | 882 | 3.4% |

**V21 change:** +5,328 ALF records integrated from NIC Maps across 8 expansion states (MI, IL, WI, MN, FL, MD, GA, MO). Corporate name standardization resolved 218 variant spellings, reclassifying 179 facilities from Independent to Corporate. See `changelogs/V20_to_V21_ALF_Enhancement.md` for full methodology.

## Key Columns

| Column | Purpose |
|--------|---------|
| `Ownership_Type` | Corporate vs Independent (Four-Rule Count-Based Hierarchy) |
| `Source_Type` | SNF or ALF (all AL, MC, and AL+MC facilities classified as ALF) |
| `Do_We_Serve` | Yes/No — currently served facility |
| `Integrated_Flag` | Yes/No — receives both PCP and MH |
| `PCP_Flag` / `MH_Flag` | Individual service flags |
| `Barrier` | Operational barriers blocking revenue |
| `Geographic_Tier` | A_Metro / B_Highway / C_Rural |
| `Original_Geographic_Tier` | Preserves interim classification for expansion states (tagged "(Interim)") |
| `Metro_Assignment` | Named metro market (12 production markets + interim expansion state metros) |
| `Distance_to_Metro_Center` | Miles from facility to assigned metro center |
| `Contract_Status` | Green / Yellow / Red |
| `Census` | Average daily occupied beds (basis for all revenue calculations) |
| `Total_Beds` | AL Open Units + MC Open Units (from NIC Maps for V21 records) |

## Ownership Classification Rules

1. **Blank Corporate Name** → Independent
2. **"INDEPENDENT" placeholder** → Independent
3. **Multi-facility chains** (count > 1) → Corporate
4. **Single-facility operators** (count = 1) → Independent

**Critical:** Always use `Ownership_Type` column, never infer from `Corporate_Name` presence.

## Version History

| Version | Date | Total | Key Changes |
|---------|------|-------|-------------|
| **V21.1** | Feb 2026 | **26,271** | Corporate name standardization: 218 variants resolved, 179 ownership reclassifications |
| V21.0 | Feb 2026 | 26,271 | +5,328 ALF from NIC Maps (8 expansion states), campus sister facility rule, interim geo tiers |
| V20.0 | Dec 2025 | 20,943 | Cardon barriers + corporate standardization |
| V19.2 | Dec 2025 | 20,943 | Duplicate resolution + data quality fixes |
| V19.1 Enhanced | Dec 2025 | 20,943 | Metro_Assignment, Distance_to_Metro_Center added |
| V18.7 | Nov 2025 | 20,943 | PowerBI reconciliation, -80 facilities, -535 barriers |
| V17.1 | Nov 2025 | 21,023 | Eventus 8-state integration, GPS dedup, Four-Rule reclassification |
| V15.0 | Nov 2025 | 17,434 | TAM/SAM/SOM methodology refined |
| V11.0 | Nov 2025 | 17,434 | Barrier integration (111 barriers → 786 facilities) |
| V8.0 | Nov 2025 | 17,434 | Initial unified SNF + ALF database |

> Full documentation for V2–V19.1 preserved in `archive/` folders. Git tracks all changes.
> V20→V21 changelog: `changelogs/V20_to_V21_ALF_Enhancement.md`

## Key Rules (V21)

- **Source_Type classification:** All facilities with AL units, MC units, or both → "ALF". NIC Maps AL/MC subtypes preserved in changelog for future reclassification if schema evolves.
- **Units = Beds:** NIC Maps "AL Open Units" + "MC Open Units" treated as Total_Beds.
- **Census derivation:** Census = Total_Beds x 0.80, rounded. Consistent with all existing ALF records.
- **Campus sister facility rule:** ALF and SNF at the same address are separate records (different revenue rates). 75 campus pairs exist in V21.
- **Ownership recomputation:** Four-Rule Hierarchy runs across the entire database after any record integration. Adding records can reclassify existing facilities.
- **Geographic tier (expansion states):** Interim classification tagged "(Interim)" in Original_Geographic_Tier. Full CBSA-based enhancement deferred.

## Known Issues / Open Items

- **Facility count discrepancy:** Database vs CRM (~1,200) — campus co-location counting methodology, not an error. See `current/Facility_Count_Discrepancy_Explanation.md`
- **Metro Assignment gap:** Expansion state metros use interim definitions. Full resolution deferred to Metro Enhancement Proposal.
- **75 campus sister facilities:** Should be individually reviewed to confirm genuine campus relationships.
- **PA 3 unmatched candidates:** Three NIC Maps PA facilities had no V20 match. Investigate for future increment.
- **Pre-existing V20 data quality:** 2,230 null ZIPs and 7 null bed counts not addressed in V21.
- **Revenue recomputation:** Scenario models (S1/S2/S3) need regeneration to reflect expanded V21 facility base.

## Related Files

- **Vault (Archive):** `new_02_Data_Model/Archive/1_Combined_Database_FINAL_V21_0.xlsx`
- **Vault (Archive):** `new_02_Data_Model/Archive/1_Combined_Database_FINAL_V20_0.xlsx`
- **This repo:** `current/6_Core_Rulebook_V20_0.md` — full methodology reference
- **This repo:** `2_Fee_Schedule_Reference.md` — fee inputs
- **This repo:** `3_Economic_Model_Compendium.md` — downstream scenario models

---

*One-to-one markdown companion for the Combined Database. Git tracks version history.*
