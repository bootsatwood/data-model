# data-model/scripts

Python tooling for the Eventus facility database. All scripts operate on the
Combined Database Excel file in `Vault/02_Data_Model/Current/`.

## Layout

| Pattern | Count | Purpose |
|---------|-------|---------|
| `v2*_*.py` | 22 | **Version migrations** — produce the next Excel version from the current one. These are the audit trail. |
| `load_*.py` | 7 | **PG loaders** — push Excel data into PostgreSQL (`bd` schema) for Keystone. |
| `build_*.py` | 18 | **Report builders** — generate workbooks, HTML reports, and scoring outputs. |
| `utils.py` | 1 | Shared utilities (normalizers, DB loader, paths). Imported by many scripts. |
| `qc_validator.py` | 1 | QC snapshot/compare/validate tool. |
| `archive/` | 69+ | One-off analysis scripts that ran once and are kept for audit trail. |
| `audit_reports/` | 38 | Output artifacts (CSV, Excel, markdown) from analysis runs. |

## Shared dependency

`utils.py` is imported by many scripts via `from utils import ...`. It must
stay at the `scripts/` root. Archived scripts that depend on it have a
`sys.path` fix so they still work if re-run from `archive/`.

## Running scripts

Most scripts expect to be run from the `scripts/` directory:

```bash
cd ~/data-model/scripts
python v26_0_migration.py --preview
python load_v25_to_pg.py
```

PG loaders read credentials from `~/data-model/.env` or have them configured
inline. See each script's header for details.
