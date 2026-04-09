# scripts/archive

One-off analysis and audit scripts. Each was written to answer a specific
question or apply a specific fix at a point in time. They are retained as
audit trail — not deleted — but are not part of active tooling.

Scripts that import `utils.py` have a `sys.path` line added so they can still
find the parent directory's `utils.py` if re-run.

Moved here 2026-04-09 as part of scripts reorganization.
