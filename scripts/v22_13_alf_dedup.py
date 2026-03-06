#!/usr/bin/env python3
"""
ALF Same-Address Deduplication — V22.12 -> V22.13

Removes duplicate ALF rows where the same facility appears 2+ times at the
same address with the same (or compatible) corporate name. Unlike SNFs, ALFs
have no CCN for verification. Instead, we use exact facility name match +
corporate name agreement as the duplicate signal.

Scope (high-confidence only):
  - Exact-name + same corp (or both blank): 191 pairs
  - Exact-name + one has corp, one blank: 15 pairs
  - Exact-name + same corp triples: 8 addresses (remove 2 of 3)

Deferred:
  - Exact-name + different corps (40 addresses) — likely PROPCO/OPCO, needs review
  - Different-name pairs (316 addresses) — could be legitimate campus variants

Usage:
  python v22_13_alf_dedup.py preview
  python v22_13_alf_dedup.py apply
"""

import sys
from collections import Counter, defaultdict
from openpyxl import load_workbook
from utils import safe, norm, addr_key, load_db, VAULT

DB_SOURCE = VAULT / "Current" / "1_Combined_Database_FINAL_V22_12.xlsx"
DB_OUTPUT = VAULT / "Current" / "1_Combined_Database_FINAL_V22_13.xlsx"


# ---------------------------------------------------------------------------
# Row scoring — higher = better data quality
# ---------------------------------------------------------------------------

def score_row(r):
    """Score a row by data completeness. Higher = keep."""
    s = 0
    if safe(r.get('Do_We_Serve', '')) == 'Yes':
        s += 1000  # served rows always win
    corp = safe(r.get('Corporate_Name', ''))
    if corp and corp != 'INDEPENDENT':
        s += 10
    src = safe(r.get('Corp_Attribution_Source', ''))
    if src == 'GLR':
        s += 8
    elif src == 'CMS':
        s += 6
    elif src.startswith('NIC'):
        s += 4
    elif src == 'LEGACY':
        s += 2
    # Count non-empty fields
    for h, v in r.items():
        if h.startswith('_'):
            continue
        if safe(v):
            s += 1
    return s


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('preview', 'apply'):
        print("Usage: python v22_13_alf_dedup.py [preview|apply]")
        sys.exit(1)

    mode = sys.argv[1]
    print(f"ALF Same-Address Deduplication — V22.12 -> V22.13 ({mode} mode)")
    print("=" * 65)

    print(f"\nLoading {DB_SOURCE.name}...")
    headers, rows = load_db(DB_SOURCE)
    print(f"  {len(rows):,} rows loaded.")

    # --- Find exact-name ALF duplicates ---
    print("\nPhase 1: Find exact-name ALF duplicates")
    print("-" * 50)

    alf_by_addr = defaultdict(list)
    for r in rows:
        ak = addr_key(safe(r.get('Address', '')),
                       safe(r.get('City', '')),
                       safe(r.get('State', '')))
        if not ak or ak == '||':
            continue
        if safe(r.get('Source_Type', '')) == 'ALF':
            alf_by_addr[ak].append(r)

    # Filter to exact-name groups with compatible corps
    high_conf = []
    deferred_diff_corp = 0

    for ak, rlist in alf_by_addr.items():
        if len(rlist) < 2:
            continue
        names = set(norm(safe(r.get('Facility_Name', ''))) for r in rlist)
        if len(names) != 1:
            continue

        # Check corporate name compatibility
        corps = [safe(r.get('Corporate_Name', '')) for r in rlist]
        corps_nonblank = set(c for c in corps if c)

        if len(corps_nonblank) <= 1:
            # Same corp, both blank, or one has corp + one blank → high confidence
            high_conf.append((ak, rlist))
        else:
            deferred_diff_corp += 1

    print(f"  High-confidence exact-name duplicates: {len(high_conf)} addresses")
    print(f"  Deferred (different corps): {deferred_diff_corp} addresses")

    # --- Phase 2: Determine keep/remove ---
    print(f"\nPhase 2: Keep/Remove Decisions")
    print("-" * 50)

    rows_to_remove = set()
    served_removed = 0
    state_counts = Counter()
    pairs_processed = 0
    triples_processed = 0

    for ak, rlist in sorted(high_conf):
        # Score all rows, keep the best one
        scored = [(score_row(r), r) for r in rlist]
        scored.sort(key=lambda x: x[0], reverse=True)

        keep = scored[0][1]
        removes = [s[1] for s in scored[1:]]

        city = safe(keep.get('City', ''))
        state = safe(keep.get('State', ''))
        fname = safe(keep.get('Facility_Name', ''))
        keep_corp = safe(keep.get('Corporate_Name', '')) or '(blank)'
        keep_src = safe(keep.get('Corp_Attribution_Source', '')) or '-'
        keep_served = safe(keep.get('Do_We_Serve', ''))

        state_counts[state] += len(removes)

        if len(rlist) > 2:
            triples_processed += 1
        else:
            pairs_processed += 1

        served_flag = ''
        if keep_served == 'Yes':
            served_flag = ' SERVED(keep)'

        for rm in removes:
            rm_served = safe(rm.get('Do_We_Serve', ''))
            if rm_served == 'Yes':
                served_removed += 1
                served_flag = ' ** SERVED(remove) **'
            rows_to_remove.add(rm['_excel_row'])

        rm_rows = [r['_excel_row'] for r in removes]
        rm_corps = [safe(r.get('Corporate_Name', '')) or '(blank)' for r in removes]

        count_label = f"({len(rlist)} rows)" if len(rlist) > 2 else ""
        print(f"  {fname[:45]:<45s}  {city}, {state}{served_flag} {count_label}")
        print(f"    KEEP   row {keep['_excel_row']:>5d}  corp={keep_corp[:30]:<30s}  src={keep_src}")
        for rm, rc in zip(removes, rm_corps):
            rm_src = safe(rm.get('Corp_Attribution_Source', '')) or '-'
            print(f"    REMOVE row {rm['_excel_row']:>5d}  corp={rc[:30]:<30s}  src={rm_src}")

    if served_removed:
        print(f"\n  WARNING: {served_removed} served rows would be REMOVED!")

    # --- Summary ---
    print(f"\n{'=' * 65}")
    print("SUMMARY")
    print(f"{'=' * 65}")
    print(f"  Pairs processed:               {pairs_processed}")
    print(f"  Triples processed:             {triples_processed}")
    print(f"  Rows to remove:                {len(rows_to_remove)}")
    print(f"  Served rows removed:           {served_removed}")
    print(f"  States: {dict(sorted(state_counts.items()))}")
    print(f"  Final row count:               {len(rows) - len(rows_to_remove):,}")

    if mode == 'preview':
        print(f"\n  ** PREVIEW ONLY -- no file written **")
        print(f"  Run with 'apply' to write {DB_OUTPUT.name}")
        return

    # --- Write V22.13 ---
    print(f"\nWriting {DB_OUTPUT.name}...")

    wb = load_workbook(DB_SOURCE)
    ws = wb.active

    # Delete rows from bottom to top to preserve row numbers
    for excel_row in sorted(rows_to_remove, reverse=True):
        ws.delete_rows(excel_row)

    wb.save(DB_OUTPUT)
    print(f"  {len(rows_to_remove)} rows deleted")
    print(f"  Saved: {DB_OUTPUT}")


if __name__ == '__main__':
    main()
