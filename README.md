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
| 6.4_Corporate_Tiering_Methodology_Ops_View_V21_2.md | V21.2 | Operations tiering methodology |
| Facility_Count_Discrepancy_Explanation.md | — | Why Database (1,658) != CRM (~1,200) |

## Scripts

| File | Purpose |
|------|---------|
| scripts/qc_validator.py | QC tool — snapshot, compare, validate modes |
| scripts/qc_config.json | File paths + expected values (update per version) |

Run from repo root: `python scripts/qc_validator.py [snapshot|compare|validate]`

See `current/QC_Framework.md` for full documentation.

## Related

- **Vault** (OneDrive): Excel databases, economic models, report workbooks
- **reports repo** (GitHub): Budget analysis, Python scripts, HTML reports
