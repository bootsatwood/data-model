#!/usr/bin/env python3
"""
ALF Same-Address Different-Corp Deduplication — V22.13 -> V22.14

Removes duplicate ALF rows where the same facility appears 2+ times at the
same address but with different corporate names. These are predominantly
PROPCO vs OPCO patterns from NIC Maps data — one row has the operating
company name, the other has the property-holding LLC.

Patterns found:
  - INDEPENDENT vs actual corp name (11 pairs) — keep actual corp
  - Operating company vs PROPCO/LLC (15+ pairs) — keep operating company
  - Corp name vs "unknown" (4 pairs) — keep actual corp
  - Same-org variant names (5+ pairs) — keep by data quality score
  - Double-PROPCO (both LLCs) — keep by data quality score

Usage:
  python v22_14_alf_diffcorp_dedup.py preview
  python v22_14_alf_diffcorp_dedup.py apply
"""

import sys
from collections import Counter, defaultdict
from openpyxl import load_workbook
from utils import safe, norm, addr_key, load_db, VAULT

DB_SOURCE = VAULT / "Current" / "1_Combined_Database_FINAL_V22_13.xlsx"
DB_OUTPUT = VAULT / "Current" / "1_Combined_Database_FINAL_V22_14.xlsx"


# ---------------------------------------------------------------------------
# Row scoring — enhanced for PROPCO/OPCO discrimination
# ---------------------------------------------------------------------------

PROPCO_KEYWORDS = ['REAL ESTATE', 'REALTY', 'PROPCO', 'INVESTORS',
                   'PROPERTIES', 'HOLDINGS', 'PARTNERSHIP', 'PARTNERS']

def is_propco_name(corp):
    """Heuristic: does this look like a property-holding company?"""
    c = corp.upper()
    # Address-as-name (starts with digits)
    if c and c[0].isdigit():
        return True
    for kw in PROPCO_KEYWORDS:
        if kw in c:
            return True
    return False


def score_row(r):
    """Score a row by data quality. Higher = keep."""
    s = 0
    if safe(r.get('Do_We_Serve', '')) == 'Yes':
        s += 1000

    corp = safe(r.get('Corporate_Name', ''))
    if corp and corp.upper() not in ('INDEPENDENT', 'UNKNOWN', ''):
        s += 10
        if is_propco_name(corp):
            s -= 7  # PROPCO penalty
        # Penalize generic LLC names that are just the facility name + LLC
        if corp.upper().endswith(' LLC') and len(corp) < 35:
            s -= 2
    elif corp.upper() == 'INDEPENDENT':
        s += 1  # slightly better than blank
    # "unknown" treated as blank (no bonus)

    src = safe(r.get('Corp_Attribution_Source', ''))
    if src == 'GLR':
        s += 8
    elif src == 'CMS':
        s += 6
    elif src.startswith('NIC'):
        s += 4
    elif src == 'LEGACY':
        s += 2

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
        print("Usage: python v22_14_alf_diffcorp_dedup.py [preview|apply]")
        sys.exit(1)

    mode = sys.argv[1]
    print(f"ALF Different-Corp Deduplication — V22.13 -> V22.14 ({mode} mode)")
    print("=" * 65)

    print(f"\nLoading {DB_SOURCE.name}...")
    headers, rows = load_db(DB_SOURCE)
    print(f"  {len(rows):,} rows loaded.")

    # --- Find exact-name ALF groups with different corps ---
    print("\nPhase 1: Find exact-name ALF duplicates with different corps")
    print("-" * 55)

    alf_by_addr = defaultdict(list)
    for r in rows:
        ak = addr_key(safe(r.get('Address', '')),
                       safe(r.get('City', '')),
                       safe(r.get('State', '')))
        if not ak or ak == '||':
            continue
        if safe(r.get('Source_Type', '')) == 'ALF':
            alf_by_addr[ak].append(r)

    targets = []
    for ak, rlist in alf_by_addr.items():
        if len(rlist) < 2:
            continue
        names = set(norm(safe(r.get('Facility_Name', ''))) for r in rlist)
        if len(names) != 1:
            continue
        corps = [safe(r.get('Corporate_Name', '')) for r in rlist]
        corps_nonblank = set(c for c in corps if c and c.upper() != 'UNKNOWN')
        if len(corps_nonblank) > 1:
            targets.append((ak, rlist))

    print(f"  {len(targets)} addresses with different-corp exact-name ALF duplicates")

    # --- Phase 2: Keep/Remove ---
    print(f"\nPhase 2: Keep/Remove Decisions")
    print("-" * 55)

    rows_to_remove = set()
    served_removed = 0
    state_counts = Counter()

    for ak, rlist in sorted(targets):
        scored = [(score_row(r), r) for r in rlist]
        scored.sort(key=lambda x: x[0], reverse=True)

        keep = scored[0][1]
        removes = [s[1] for s in scored[1:]]

        city = safe(keep.get('City', ''))
        state = safe(keep.get('State', ''))
        fname = safe(keep.get('Facility_Name', ''))
        keep_corp = safe(keep.get('Corporate_Name', '')) or '(blank)'
        keep_src = safe(keep.get('Corp_Attribution_Source', '')) or '-'

        state_counts[state] += len(removes)

        served_flag = ''
        if safe(keep.get('Do_We_Serve', '')) == 'Yes':
            served_flag = ' SERVED(keep)'

        for rm in removes:
            if safe(rm.get('Do_We_Serve', '')) == 'Yes':
                served_removed += 1
                served_flag = ' ** SERVED(remove) **'
            rows_to_remove.add(rm['_excel_row'])

        count_label = f"({len(rlist)} rows)" if len(rlist) > 2 else ""
        print(f"  {fname[:48]:<48s}  {city}, {state}{served_flag} {count_label}")
        print(f"    KEEP   row {keep['_excel_row']:>5d}  corp={keep_corp[:40]}")
        for rm in removes:
            rm_corp = safe(rm.get('Corporate_Name', '')) or '(blank)'
            print(f"    REMOVE row {rm['_excel_row']:>5d}  corp={rm_corp[:40]}")

    if served_removed:
        print(f"\n  WARNING: {served_removed} served rows would be REMOVED!")

    # --- Summary ---
    print(f"\n{'=' * 65}")
    print("SUMMARY")
    print(f"{'=' * 65}")
    print(f"  Addresses processed:           {len(targets)}")
    print(f"  Rows to remove:                {len(rows_to_remove)}")
    print(f"  Served rows removed:           {served_removed}")
    print(f"  States: {dict(sorted(state_counts.items()))}")
    print(f"  Final row count:               {len(rows) - len(rows_to_remove):,}")

    if mode == 'preview':
        print(f"\n  ** PREVIEW ONLY -- no file written **")
        print(f"  Run with 'apply' to write {DB_OUTPUT.name}")
        return

    # --- Write V22.14 ---
    print(f"\nWriting {DB_OUTPUT.name}...")

    wb = load_workbook(DB_SOURCE)
    ws = wb.active

    for excel_row in sorted(rows_to_remove, reverse=True):
        ws.delete_rows(excel_row)

    wb.save(DB_OUTPUT)
    print(f"  {len(rows_to_remove)} rows deleted")
    print(f"  Saved: {DB_OUTPUT}")


if __name__ == '__main__':
    main()
