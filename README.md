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

See `scripts/README.md` for full layout. Summary:

```
scripts/
├── v2*_*.py       22 version migration scripts (V22.7 → V26.0) — the audit trail
├── load_*.py       7 PG loaders — push Excel into PostgreSQL for Keystone
├── build_*.py     18 report/workbook builders
├── utils.py        Shared utilities (normalizers, DB loader, paths)
├── qc_validator.py QC snapshot/compare/validate tool
├── qc_config.json  File paths + expected values (update per version)
├── audit_reports/  Output artifacts from analysis runs (CSV, Excel, markdown)
└── archive/       69 one-off analysis scripts — retained for audit trail, not active
```

Run from `scripts/` directory:
```bash
cd scripts
python v26_0_migration.py --preview
python load_v25_to_pg.py
python qc_validator.py snapshot
```

See `current/QC_Framework.md` for QC documentation.

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
