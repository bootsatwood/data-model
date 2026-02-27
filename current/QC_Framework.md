# QC Validation Framework

**Version:** V21.1
**Last updated:** 2026-02-27

## Purpose

The QC Validator prevents data drift during edit sessions and validates database integrity before delivery. It replaces the original V16.0 QC tool (Nov 2025) which only checked surface-level totals.

## Three Modes

| Mode | Command | When to use |
|---|---|---|
| **Snapshot** | `python scripts/qc_validator.py snapshot` | Before starting an edit session |
| **Compare** | `python scripts/qc_validator.py compare` | After each edit session |
| **Validate** | `python scripts/qc_validator.py validate` | Before delivering a new version |

### Snapshot

Captures a full baseline of every countable dimension in the database:
- Total counts (facilities, SNF/ALF, corporate/independent, served, barriers)
- Per-state breakdowns of all the above
- Service flag counts (Integrated, PCP-only, MH-only) total and per-state
- Barrier counts by type and by state
- Geographic tier distribution
- Metro assignment counts
- Contract status distribution
- Row-level fingerprints (hash of key fields for change detection)

Saves to `scripts/.snapshots/` as timestamped JSON + `latest.json`.

### Compare

Reads the current database, computes the same dimensions, and diffs against the last snapshot:
- **Summary deltas** — any total that changed
- **Per-state deltas** — only states where something shifted
- **Row-level changes** — which specific rows changed (by fingerprint comparison)
- **New/removed rows** — rows that appeared or disappeared

This is the critical mode for outlier review safety — it tells you exactly what changed and whether anything changed that you didn't intend.

### Validate

Checks the database against known-good expected values from `qc_config.json`:
- **Structure** — all 25 columns present and in order
- **Counts** — totals match expected for every dimension
- **Rules** — business logic consistency:
  - `INDEPENDENT` corporate name → `Ownership_Type` must be `Independent`
  - `Do_We_Serve=Yes` → at least one of `PCP_Flag` or `MH_Flag` must be `Yes`
  - `Integrated_Flag=Yes` ↔ both `PCP_Flag=Yes` AND `MH_Flag=Yes`
  - No `DUPLICATE-DEACTIVATED` barrier markers (flagged as WARN)
- **Cross-file** — database row count vs scenario row count

Reports PASS / FAIL / WARN per check.

## Typical Workflow

```
1. python scripts/qc_validator.py snapshot     # baseline before editing
2. ... make your edits in Excel ...
3. python scripts/qc_validator.py compare      # what changed?
4. ... review the diff, confirm expected ...
5. python scripts/qc_validator.py snapshot     # new baseline for next session
6. ... repeat for each edit batch ...
7. python scripts/qc_validator.py validate     # final check before delivery
```

## Configuration

All file paths, column definitions, and expected values live in `scripts/qc_config.json`. When a version bump happens (e.g., V21.1 → V21.2):

1. Update `"version"` field
2. Update `"files"` with new filenames
3. Update `"expected"` with new baseline counts
4. Take a fresh snapshot

The script itself should not need changes between versions.

## Files

| File | Purpose |
|---|---|
| `scripts/qc_validator.py` | The QC tool (Python, openpyxl-only) |
| `scripts/qc_config.json` | File paths + expected values (edit per version) |
| `scripts/.snapshots/` | Local snapshot/diff JSON files (gitignored) |

## Known Limitations

- **82 duplicate composite keys** exist in V21.1 (same Source_Type + Facility_Name + Address + City + State + ZIP). These are campus sister facilities. The fingerprinting collapses them — changes to one of a pair may not be individually tracked. A future enhancement could add row number or a unique ID to the key.
- **Snapshot doesn't store raw field values** — compare mode shows which rows changed but can't display old → new values. You see the change detection; the details are in your Excel save history.
- **Scenario/report deep validation deferred** — scenarios are V20.0 and will be rebuilt after the outlier review.

---

*This framework lives in the data-model repo alongside the methodology docs it validates.*
