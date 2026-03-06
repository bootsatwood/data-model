#!/usr/bin/env python3
"""
SNF Same-Address Deduplication — V22.11 -> V22.12

Removes duplicate SNF rows where the same facility appears twice at the same
address with the same CMS Certification Number (CCN). These duplicates arose
from multiple data sources (CMS SNF, CMS Provider Info, GLR) creating separate
rows for the same physical facility.

Method:
  1. Find addresses with 2+ SNF rows sharing the same normalized facility name
  2. Cross-reference against CMS Provider Info to verify 1 CCN per address
  3. For confirmed duplicates (1 CCN), keep the row with better data quality
  4. Remove the lower-quality duplicate

Keep logic (in priority order):
  - If one row is served and the other isn't → keep served
  - Otherwise, score by data completeness (corporate name, attribution source,
    non-empty fields) → keep higher score
  - For corporate name conflicts: prefer operating company over PROPCO/LLC name

Usage:
  python v22_12_snf_dedup.py preview
  python v22_12_snf_dedup.py apply
"""

import sys
import csv
from collections import Counter, defaultdict
from openpyxl import load_workbook
from utils import safe, norm, addr_key, load_db, CMS_PROVIDER_FILE, VAULT

DB_SOURCE = VAULT / "Current" / "1_Combined_Database_FINAL_V22_11.xlsx"
DB_OUTPUT = VAULT / "Current" / "1_Combined_Database_FINAL_V22_12.xlsx"


# ---------------------------------------------------------------------------
# Row scoring — higher = better data quality
# ---------------------------------------------------------------------------

def score_row(r):
    """Score a row by data completeness. Higher = keep."""
    s = 0
    if safe(r.get('Do_We_Serve', '')) == 'Yes':
        s += 1000  # served rows always win
    corp = safe(r.get('Corporate_Name', ''))
    if corp:
        s += 10
        # Penalize PROPCO-style names (real estate LLCs)
        if 'LLC' in corp and ('REAL ESTATE' in corp or 'REALTY' in corp or 'PROPCO' in corp):
            s -= 5
        # Penalize address-as-corp-name
        if any(c.isdigit() for c in corp[:4]):
            s -= 5
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
        print("Usage: python v22_12_snf_dedup.py [preview|apply]")
        sys.exit(1)

    mode = sys.argv[1]
    print(f"SNF Same-Address Deduplication — V22.11 -> V22.12 ({mode} mode)")
    print("=" * 65)

    # --- Load data ---
    print(f"\nLoading {DB_SOURCE.name}...")
    headers, rows = load_db(DB_SOURCE)
    print(f"  {len(rows):,} rows loaded.")

    print(f"Loading CMS Provider Info for CCN verification...")
    cms_addr = defaultdict(set)
    with open(CMS_PROVIDER_FILE, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for cr in reader:
            ak = addr_key(cr.get('Provider Address', ''),
                          cr.get('City/Town', ''),
                          cr.get('State', ''))
            ccn = cr.get('CMS Certification Number (CCN)', '')
            if ccn:
                cms_addr[ak].add(ccn)
    print(f"  {len(cms_addr):,} CMS addresses loaded.")

    # --- Find exact-name SNF duplicate addresses ---
    print("\nPhase 1: Find exact-name SNF duplicates")
    print("-" * 50)

    snf_by_addr = defaultdict(list)
    for r in rows:
        ak = addr_key(safe(r.get('Address', '')),
                       safe(r.get('City', '')),
                       safe(r.get('State', '')))
        if not ak or ak == '||':
            continue
        if safe(r.get('Source_Type', '')) == 'SNF':
            snf_by_addr[ak].append(r)

    exact_dupes = {}
    for ak, rlist in snf_by_addr.items():
        if len(rlist) < 2:
            continue
        names = set(norm(safe(r.get('Facility_Name', ''))) for r in rlist)
        if len(names) == 1:
            exact_dupes[ak] = rlist

    print(f"  {len(exact_dupes)} addresses with exact-name SNF duplicates")

    # --- Phase 2: CCN verification ---
    print("\nPhase 2: CCN cross-reference")
    print("-" * 50)

    confirmed = []  # (addr_key, keep_row, remove_row, ccn)
    multi_ccn = []
    no_cms = []

    for ak, rlist in sorted(exact_dupes.items()):
        ccns = cms_addr.get(ak, set())

        if not ccns:
            no_cms.append((ak, rlist))
            continue

        if len(ccns) > 1:
            multi_ccn.append((ak, rlist, ccns))
            continue

        # 1 CCN — confirmed duplicate. Decide which to keep.
        ccn = list(ccns)[0]
        scored = [(score_row(r), r) for r in rlist]
        scored.sort(key=lambda x: x[0], reverse=True)
        keep = scored[0][1]
        remove = scored[1][1]
        confirmed.append((ak, keep, remove, ccn))

    print(f"  1 CCN (confirmed duplicates):  {len(confirmed)}")
    print(f"  Multiple CCNs (skip):          {len(multi_ccn)}")
    print(f"  No CMS match (skip):           {len(no_cms)}")

    # --- Phase 3: Report ---
    print(f"\nPhase 3: Removal Plan")
    print("-" * 50)

    served_removed = 0
    state_counts = Counter()

    for ak, keep, remove, ccn in confirmed:
        city = safe(keep.get('City', ''))
        state = safe(keep.get('State', ''))
        fname = safe(keep.get('Facility_Name', ''))
        state_counts[state] += 1

        keep_corp = safe(keep.get('Corporate_Name', '')) or '(blank)'
        remove_corp = safe(remove.get('Corporate_Name', '')) or '(blank)'
        keep_served = safe(keep.get('Do_We_Serve', ''))
        remove_served = safe(remove.get('Do_We_Serve', ''))

        served_flag = ''
        if keep_served == 'Yes':
            served_flag = ' SERVED(keep)'
        if remove_served == 'Yes':
            served_removed += 1
            served_flag = ' ** SERVED(remove) **'

        keep_src = safe(keep.get('Corp_Attribution_Source', '')) or '-'
        remove_src = safe(remove.get('Corp_Attribution_Source', '')) or '-'

        print(f"  {fname[:45]:<45s}  {city}, {state}  CCN={ccn}{served_flag}")
        print(f"    KEEP   row {keep['_excel_row']:>5d}  corp={keep_corp[:30]:<30s}  src={keep_src}")
        print(f"    REMOVE row {remove['_excel_row']:>5d}  corp={remove_corp[:30]:<30s}  src={remove_src}")

    if served_removed:
        print(f"\n  WARNING: {served_removed} served rows would be REMOVED!")

    # --- No CMS match details ---
    if no_cms:
        print(f"\n  No CMS match ({len(no_cms)} addresses, skipped):")
        for ak, rlist in no_cms:
            r0 = rlist[0]
            served = '*' if any(safe(r.get('Do_We_Serve', '')) == 'Yes' for r in rlist) else ' '
            print(f"  {served} {safe(r0.get('Facility_Name',''))[:45]}  {safe(r0.get('City',''))}, {safe(r0.get('State',''))}  rows={[r['_excel_row'] for r in rlist]}")

    # --- Summary ---
    print(f"\n{'=' * 65}")
    print("SUMMARY")
    print(f"{'=' * 65}")
    print(f"  Exact-name SNF duplicate addresses:  {len(exact_dupes)}")
    print(f"  CCN-confirmed duplicates:            {len(confirmed)}")
    print(f"  Rows to remove:                      {len(confirmed)}")
    print(f"  Served rows removed:                 {served_removed}")
    print(f"  States: {dict(sorted(state_counts.items()))}")
    print(f"  Final row count:                     {len(rows) - len(confirmed):,}")

    if mode == 'preview':
        print(f"\n  ** PREVIEW ONLY -- no file written **")
        print(f"  Run with 'apply' to write {DB_OUTPUT.name}")
        return

    # --- Write V22.12 ---
    print(f"\nWriting {DB_OUTPUT.name}...")

    remove_rows = set(r['_excel_row'] for _, _, r, _ in confirmed)

    wb = load_workbook(DB_SOURCE)
    ws = wb.active

    # Delete rows from bottom to top to preserve row numbers
    rows_to_delete = sorted(remove_rows, reverse=True)
    for excel_row in rows_to_delete:
        ws.delete_rows(excel_row)

    wb.save(DB_OUTPUT)
    print(f"  {len(rows_to_delete)} rows deleted")
    print(f"  Saved: {DB_OUTPUT}")


if __name__ == '__main__':
    main()
