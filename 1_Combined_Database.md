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
| `Integrated_Flag` | Yes/No — receives both PCP and MH (mutually exclusive with PCP/MH flags) |
| `PCP_Flag` / `MH_Flag` | Individual service flags (mutually exclusive — a facility is PCP, MH, or Integrated, never two) |
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
| **V21.1** | Feb 2026 | **26,271** | Corporate name standardization, 179 ownership reclassifications. Cleared 9 stale DUPLICATE-DEACTIVATED barriers. Corrected 11 service flag violations (mutual exclusivity). |
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

## Foundational Methodology (Nov 2025)

This database replaced a legacy financial workbook (referred to internally as "NCA") that tracked realized revenue in a single stream with manual per-facility entries. The NCA model was descriptive — it captured what Eventus earned — but had no concept of potential revenue, market opportunity, or TAM/SAM/SOM segmentation. It was retained as a static validation baseline only. Everything below describes the model that replaced it.

### Why This Model Exists

The Eventus Economic Model was built as a **predictive opportunity model** with four computed revenue streams (Current, Integration, New Business, Total) instead of the NCA's single realized-revenue ledger. Key architectural differences:

- **Explicit, tunable rate tables** with separate CCM and Shared Savings parameters (vs embedded static rates)
- **Programmatic service flag logic** — `Do_We_Serve`, `PCP_Flag`, `MH_Flag` are computational triggers, not manual entries
- **Barrier-sensitive TAM/SAM/SOM funnel** — barrier fields directly influence which market tier a facility falls into
- **Five schema layers:** corporate, service, barrier, geography, financial computation

### How the Database Was Originally Built

**SNF stream (Phase 1, Nov 2025):**
Raw source was `SNF Database with Revenue Q4 2025_V2.xlsx` (shared by Brooke Ritchie, Oct 31, 2025) with 6 state tabs (IN, KY, NC, OH, SC, VA). The upstream data originates from the **CMS Provider Data Nursing Facility database** ([dataset 4pq5-n9py](https://data.cms.gov/provider-data/dataset/4pq5-n9py)), which Brooke's team curated with Eventus-specific revenue overlays. The cleanse process removed non-operational columns, added `Macro Type` (now `Source_Type`) as Column A, harmonized service flags using a broadened detection rule ("any column with 'serve'" triggers `Do_We_Serve`), and mapped barrier fields per state (SC/VA/KY/OH: Column AA; IN: Column U; NC: Column AA). PCP, MH, and Integrated flags were restored and validated from the original state tabs.

**ALF stream (Phase 2, Nov 2025):**
ALF files from NC, KY, OH, IN were standardized to a unified naming convention: `DBA Name` → `Provider Name`, `Name of Licensee` → `Legal Business Name`, corporate groupings → `Chain Name`. Deduplication reduced 1,253 raw ALF records to 655 valid rows after removing 598 duplicates (exact + fuzzy match against the SNF file, followed by manual review). Default bed count of 35 was applied where bed counts were missing.

**Unification (Phase 3):**
SNF and ALF streams merged into a single database. The `Chain Name blank = Independent Entity` rule was established as a deliberate simplification. Revenue computation branches on `Source_Type`: SNF uses dynamic visit-based rates, ALF uses static fixed rates. Three-branch revenue classification: Integrated (PCP+MH → gets CCM+SS), Partial (one service → FFS only), Potential (not served → proxy calculation).

> Source documents preserved in vault: `new_02_Data_Model/Archive/Data_Challenges/`
> - `SNF Cleanse.docx` — step-by-step cleansing methodology and file lineage
> - `Eventus_Model_Comparison_TheirModel_vs_Ours.docx` — 7-dimension structural comparison vs legacy NCA
> - `Eventus_Corporate_Initiative_Technical_Brief_Nov2025.docx` — schema layers, computation pseudo-code, phase structure
>
> Full source lineage (all SNF and ALF upstream sources with URLs): `reference/Source_Data_Lineage.md`

## Pre-Release QC

Before releasing any version change, run the QC validator from the repo root:

1. `python scripts/qc_validator.py snapshot` — baseline before editing
2. Make your changes in Excel
3. `python scripts/qc_validator.py compare` — verify only intended rows changed
4. `python scripts/qc_validator.py validate` — confirm all counts and rules pass

See `current/QC_Framework.md` for full documentation. Config and expected values are in `scripts/qc_config.json`.

## Known Issues / Open Items

- **Facility count discrepancy:** Database vs CRM (~1,200) — campus co-location counting methodology, not an error. See `current/Facility_Count_Discrepancy_Explanation.md`
- **Metro Assignment gap:** Expansion state metros use interim definitions. Full resolution deferred to Metro Enhancement Proposal.
- **75 campus sister facilities:** Should be individually reviewed to confirm genuine campus relationships.
- **PA 3 unmatched candidates:** Three NIC Maps PA facilities had no V20 match. Investigate for future increment.
- **Pre-existing V20 data quality:** 2,230 null ZIPs and 7 null bed counts not addressed in V21.
- **Wytheville VA duplicate (row 16216):** `CARRINGTON WYTHEVILLE-SNF/NF` at 990 Holston Rd was not deactivated during the Dec 2025 dedup exercise but overlaps with replacement rows 20943/20944 (Holston Health and Rehab / Holston Senior Living, Hill Valley Healthcare). Source_Type says ALF but name says SNF/NF. Needs outlier review.
- **DUPLICATE-DEACTIVATED cleanup (Feb 2026):** 9 barrier markers cleared — row references were broken by V21 ALF expansion row shifts. No sibling facilities under the same corporate banners (Five Star Residences, Ayden Healthcare, Lionstone Care) had real barriers.
- **Revenue recomputation:** Scenario models (S1/S2/S3) need regeneration to reflect expanded V21 facility base.

## Related Files

- **Vault (Archive):** `new_02_Data_Model/Archive/1_Combined_Database_FINAL_V21_0.xlsx`
- **Vault (Archive):** `new_02_Data_Model/Archive/1_Combined_Database_FINAL_V20_0.xlsx`
- **This repo:** `current/6_Core_Rulebook_V20_0.md` — full methodology reference
- **This repo:** `2_Fee_Schedule_Reference.md` — fee inputs
- **This repo:** `3_Economic_Model_Compendium.md` — downstream scenario models

---

*One-to-one markdown companion for the Combined Database. Git tracks version history.*
