# Eventus WholeHealth — Data Model Methodology

Version-controlled methodology documents for the Eventus WholeHealth provider market intelligence platform.

## Structure

```
current/         Active methodology (V20-V21)
reference/       Supporting analysis and enhancement plans
archive/         Full version history (V02-V19.1) + foundation docs
```

## Current Methodology (V20.x)

| File | Version | Description |
|------|---------|-------------|
| 6_Core_Rulebook_V20_0.md | V20.0 | Master governance — fee structure, revenue formulas, reporting filters |
| 6.1_Comprehensive_Report_Compendium_V20_1.md | V20.1 | Tables 1-25 methodology |
| 6.2_Metro_Market_Analysis_Compendium_V19_2.md | V19.2 | Metro analysis methodology (version lag) |
| 6.3_Corporate_Scoring_Methodology_V20.md | V20.0 | Corporate scoring rules |
| Database_Change_Request_V22.md | V22 | **PENDING** — 8 DB/scoring issues from MUO profile work |
| 6.4_Corporate_Tiering_Methodology_Ops_View_V21_2.md | V21.2 | Operations tiering methodology |
| Facility_Count_Discrepancy_Explanation.md | — | Why Database (1,658) != CRM (~1,200) |

## Scripts

| File | Purpose |
|------|---------|
| scripts/chain_update_v21_2.py | CMS Chain ID enhancement — preview, apply, four-rule modes |
| scripts/chain_crossref.py | Chain classification cross-reference analysis (read-only) |
| scripts/chain_crossref_independent.py | Independent facilities with CMS chain analysis (read-only) |
| scripts/corporate_fix.py | Wave 2c corporate attribution (GLR/CMS/NIC three-tier) — V22.2 -> V22.3 |
| scripts/corporate_name_dedup.py | Corporate name dedup analysis — fuzzy matching + review workbook (read-only) |
| scripts/corporate_dedup_fix.py | Corporate name consolidation — V22.3 -> V22.4 (preview/apply) |
| scripts/remove_greencroft_dupes.py | Remove 3 duplicate/phantom Greencroft rows from V22.6 (preview/apply) |
| scripts/v22_7_fix.py | Combined V22.6->V22.7: Liberty QC + Singh/Cedarhurst/Spring Arbor dedup (preview/apply) |
| scripts/v22_8_norm_clusters.py | Exact norm cluster consolidation — V22.7 -> V22.8 (19 clusters + 4 typo fixes, 199 renames) |
| scripts/v22_9_fuzzy_dedup.py | High-confidence fuzzy match consolidation — V22.8 -> V22.9 (14 pairs, 507 renames) |
| scripts/v22_10_southern_fix.py | Southern Healthcare Management consolidation — V22.9 -> V22.10 (Sovereign→Southern, 44 renames) |
| scripts/v22_11_il_reclassify.py | IL/55+ Source_Type reclassification — V22.10 -> V22.11 (53 ALF→ILF) |
| scripts/v22_12_snf_dedup.py | SNF same-address dedup via CCN verification — V22.11 -> V22.12 (255 rows removed) |
| scripts/v22_13_alf_dedup.py | ALF same-address dedup — V22.12 -> V22.13 (215 rows removed) |
| scripts/qc_validator.py | QC tool — snapshot, compare, validate modes |
| scripts/qc_config.json | File paths + expected values (update per version) |

Run from repo root: `python scripts/qc_validator.py [snapshot|compare|validate]`

See `current/QC_Framework.md` for full documentation.

## Reference Documents

| File | Purpose |
|------|---------|
| reference/Source_Data_Lineage.md | Upstream data sources (CMS, NIC Maps, state licensing) with URLs |
| reference/Facility_Acquisitions_Log.md | Lineage for deleted facilities (acquisitions, rebrands) |
| reference/Proposal_Metro_Definition_Enhancement.md | Deferred CBSA-based metro classification |
| reference/Proposal_CMS_Source_Data_Cross_Reference.md | Deferred CMS cross-reference proposal |
| reference/Proposal_Multi_Service_Facility_Classification.md | Deferred multi-service classification review |
| reference/Risk_ALF_Corporate_Attribution_and_Data_Quality.md | ALF data quality risks: phantom duplicates, hidden ownership, IL contamination |

## Archive

Full version history from V02 through V19.1, plus foundation build docs, geographic mapping, and QC methodology.

```
archive/
├── V02/ – V19.1/     Version-by-version markdown (rulebooks, changelogs, QC summaries)
├── foundation/        Original database build methodology (21 md)
├── geographic_mapping/ KML guides, metro analysis handoffs (V9–V19)
├── qc_methodology/    QC testing handoff notes
├── v15_milestone/     V15 Rulebook, START_HERE, V14→V15 changelog
├── v16_sales_planning/ $51M target breakdown, metro allocation, revenue strategy
└── abandoned/         Proposals that were never implemented
```

> **Vault ↔ Git connection:** Each version folder here has a matching `Archive/V*/` subfolder in the Vault (`02_Data_Model/Archive/`) holding the binary counterparts — xlsx database snapshots, economic models, QC workbooks, KML files. Markdown lives in Git (diff-tracked). Binaries live in the Vault (OneDrive-synced). See the Vault `_Index.md` for the full cross-reference table.

## Related

- **Vault** (OneDrive `02_Data_Model/`): Excel databases, economic models, report workbooks, binary archive
- **reports repo** (GitHub): Budget analysis, Python scripts, HTML reports
