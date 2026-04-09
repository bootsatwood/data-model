import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # archive: find utils.py
#!/usr/bin/env python3
"""
NIC Maps Enrichment Audit — Wave 0 (Enhanced)

Joins NIC Maps source fields back to Combined Database ALF rows to resolve
ambiguity in the original audits. The NIC source contains three critical
columns that were dropped during database construction:

  1. Operator Name  — the actual facility operator (vs Owner Name used as Corporate_Name)
  2. CCN            — CMS Certification Number (if present, it's a nursing facility)
  3. Unit-type cols — AL/MC/NC/IL/AA open unit counts (what's actually in the building)

This script produces a single enriched CSV that classifies every ALF row into:
  - PHANTOM:      NC-only building (no AL/MC units) or has CCN matching CMS SNF
  - CO_LOCATED:   Has both NC and AL/MC units (campus with SNF wing + ALF wing)
  - PROPCO_SPLIT: Owner Name != Operator Name (Corporate_Name is the landlord)
  - IL_CONFIRMED: Has IL or AA units > 0 (independent living contamination)
  - CLEAN:        None of the above — appears to be a genuine ALF

Usage:
  python nic_enrichment.py              # Full report
  python nic_enrichment.py --csv        # Write enriched CSV
  python nic_enrichment.py --state NC   # Filter to one state
"""

import argparse
import csv
from collections import defaultdict

from utils import (
    load_db, load_cms_snf, load_nic_alf, addr_key, norm, safe,
    ensure_report_dir, FOOTPRINT,
)


# ---------------------------------------------------------------------------
# NIC index builder
# ---------------------------------------------------------------------------

def build_nic_index(nic_rows):
    """Index NIC buildings by address key.

    For duplicate addresses, keep the row with the most total units
    (largest building at that address is most likely the primary record).
    """
    index = {}
    for row in nic_rows:
        key = addr_key(
            safe(row.get('Address')),
            safe(row.get('City')),
            safe(row.get('State')),
        )
        if not key or key == '||':
            continue

        total = _int(row.get('Total Units'))
        if key in index:
            existing_total = _int(index[key].get('Total Units'))
            if total <= existing_total:
                continue
        index[key] = row

    return index


def build_cms_ccn_index(cms_rows):
    """Index CMS SNF records by CCN for cross-reference."""
    index = {}
    for row in cms_rows:
        ccn = safe(row.get('CMS Certification Number (CCN)'))
        if ccn:
            index[ccn] = row
    return index


def _int(val):
    """Safe int conversion for unit counts."""
    try:
        return int(val or 0)
    except (ValueError, TypeError):
        return 0


def _float(val):
    """Safe float conversion."""
    try:
        return float(val or 0)
    except (ValueError, TypeError):
        return 0


# ---------------------------------------------------------------------------
# Classification logic
# ---------------------------------------------------------------------------

def classify_alf_row(db_row, nic_row, cms_ccn_index, snf_index):
    """Classify a single ALF row using NIC enrichment data.

    Returns a dict with all enrichment fields and classification tags.
    """
    tags = []
    detail = []

    # --- Extract NIC fields ---
    nic_operator = safe(nic_row.get('Operator Name')) if nic_row else ''
    nic_owner = safe(nic_row.get('Owner Name')) if nic_row else ''
    nic_ccn = safe(nic_row.get('CCN')) if nic_row else ''
    nic_profit = safe(nic_row.get('Profit Status')) if nic_row else ''

    nc_units = _int(nic_row.get('NC Open Units')) if nic_row else 0
    al_units = _int(nic_row.get('AL Open Units')) if nic_row else 0
    mc_units = _int(nic_row.get('MC Open Units')) if nic_row else 0
    il_units = _int(nic_row.get('IL Open Units')) if nic_row else 0
    aa_units = _int(nic_row.get('AA Open Units')) if nic_row else 0
    total_units = _int(nic_row.get('Total Units')) if nic_row else 0

    db_corp = safe(db_row.get('Corporate_Name'))
    db_addr = safe(db_row.get('Address'))
    db_city = safe(db_row.get('City'))
    db_state = safe(db_row.get('State'))

    # --- Check 1: Phantom (NC-only, no AL/MC) ---
    if nc_units > 0 and al_units == 0 and mc_units == 0:
        tags.append('PHANTOM_NC_ONLY')
        detail.append(f'NC={nc_units}, AL=0, MC=0 — nursing-only building')

    # --- Check 2: Phantom (has CCN matching CMS) ---
    if nic_ccn and nic_ccn in cms_ccn_index:
        tags.append('PHANTOM_CCN_MATCH')
        cms_rec = cms_ccn_index[nic_ccn]
        cms_name = safe(cms_rec.get('Provider Name'))
        detail.append(f'CCN {nic_ccn} matches CMS SNF: {cms_name}')

    # --- Check 3: Co-located (has NC + AL or MC) ---
    if nc_units > 0 and (al_units > 0 or mc_units > 0):
        tags.append('CO_LOCATED')
        detail.append(f'NC={nc_units} + AL={al_units} + MC={mc_units} — campus/CCRC')

    # --- Check 4: Address matches our DB SNF ---
    key = addr_key(db_addr, db_city, db_state)
    if key in snf_index:
        tags.append('ADDR_MATCHES_DB_SNF')
        snf_name = safe(snf_index[key].get('Facility_Name'))
        detail.append(f'Same address as SNF: {snf_name}')

    # --- Check 5: PROPCO/OPCO split (Operator != Owner) ---
    if nic_operator and nic_owner:
        if norm(nic_operator) != norm(nic_owner):
            # Check if DB Corporate_Name matches Owner (PROPCO) or Operator
            if db_corp and norm(db_corp) == norm(nic_owner):
                tags.append('PROPCO_AS_CORPORATE')
                detail.append(f'Corp=Owner({nic_owner}), real operator={nic_operator}')
            elif db_corp and norm(db_corp) != norm(nic_operator):
                tags.append('PROPCO_SPLIT')
                detail.append(f'Operator={nic_operator}, Owner={nic_owner}')

    # --- Check 6: IL/AA contamination ---
    if il_units > 0:
        pct = il_units / total_units * 100 if total_units > 0 else 0
        if al_units == 0 and mc_units == 0 and nc_units == 0:
            tags.append('IL_ONLY')
            detail.append(f'IL={il_units} ({pct:.0f}% of total) — pure IL facility')
        else:
            tags.append('IL_MIXED')
            detail.append(f'IL={il_units} ({pct:.0f}% of total) with other unit types')

    if aa_units > 0:
        tags.append('AA_UNITS')
        detail.append(f'AA={aa_units} — Active Adult / 55+')

    # --- Final classification ---
    if not nic_row:
        classification = 'NO_NIC_MATCH'
    elif 'PHANTOM_NC_ONLY' in tags or ('PHANTOM_CCN_MATCH' in tags and 'CO_LOCATED' not in tags):
        classification = 'PHANTOM'
    elif 'CO_LOCATED' in tags:
        classification = 'CO_LOCATED'
    elif 'IL_ONLY' in tags:
        classification = 'IL_ONLY'
    elif tags:
        classification = 'FLAGGED'
    else:
        classification = 'CLEAN'

    return {
        'excel_row': db_row['_excel_row'],
        'facility': safe(db_row.get('Facility_Name')),
        'corporate_name': db_corp,
        'address': db_addr,
        'city': db_city,
        'state': db_state,
        'ownership_type': safe(db_row.get('Ownership_Type')),
        'do_we_serve': safe(db_row.get('Do_We_Serve')),
        'db_beds': safe(db_row.get('Total_Beds')),
        'db_census': safe(db_row.get('Census')),
        'nic_operator': nic_operator,
        'nic_owner': nic_owner,
        'nic_ccn': nic_ccn,
        'nic_profit_status': nic_profit,
        'nc_units': nc_units,
        'al_units': al_units,
        'mc_units': mc_units,
        'il_units': il_units,
        'aa_units': aa_units,
        'total_units': total_units,
        'classification': classification,
        'tags': ', '.join(tags),
        'detail': ' | '.join(detail),
    }


# ---------------------------------------------------------------------------
# Main audit
# ---------------------------------------------------------------------------

def run_enrichment(db_rows, nic_index, cms_ccn_index, snf_index, state_filter=None):
    """Classify all ALF rows using NIC enrichment."""
    results = []

    for row in db_rows:
        if safe(row.get('Source_Type')) != 'ALF':
            continue
        state = safe(row.get('State'))
        if state_filter and state != state_filter:
            continue

        key = addr_key(
            safe(row.get('Address')),
            safe(row.get('City')),
            safe(row.get('State')),
        )
        nic_row = nic_index.get(key)

        record = classify_alf_row(row, nic_row, cms_ccn_index, snf_index)
        results.append(record)

    return results


def write_csv(results, outpath):
    if not results:
        print("  No results — CSV not written.")
        return
    fieldnames = list(results[0].keys())
    with open(outpath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"  CSV written: {outpath} ({len(results)} rows)")


def print_summary(results):
    print()
    print("=" * 70)
    print("NIC ENRICHMENT AUDIT — ALF CLASSIFICATION")
    print("=" * 70)
    print()

    # Classification breakdown
    by_class = defaultdict(list)
    for r in results:
        by_class[r['classification']].append(r)

    print(f"Total ALF rows analyzed: {len(results):,}")
    print()
    print("Classification breakdown:")
    for cls in ['PHANTOM', 'CO_LOCATED', 'IL_ONLY', 'FLAGGED', 'CLEAN', 'NO_NIC_MATCH']:
        rows = by_class.get(cls, [])
        served = sum(1 for r in rows if r['do_we_serve'] == 'Yes')
        served_tag = f"  ({served} served)" if served else ""
        print(f"  {cls:<15} {len(rows):>6,}{served_tag}")

    # --- PHANTOM detail ---
    phantoms = by_class.get('PHANTOM', [])
    if phantoms:
        print()
        print("-" * 70)
        print(f"CONFIRMED PHANTOMS ({len(phantoms)}) — NC-only or CCN-matched, no AL/MC")
        print("-" * 70)

        # By state
        ph_by_state = defaultdict(int)
        for r in phantoms:
            ph_by_state[r['state']] += 1
        print()
        print("  By state:")
        for state, count in sorted(ph_by_state.items(), key=lambda x: -x[1]):
            fp = " *" if state in FOOTPRINT else ""
            print(f"    {state}: {count}{fp}")

        served_ph = [r for r in phantoms if r['do_we_serve'] == 'Yes']
        if served_ph:
            print(f"\n  *** {len(served_ph)} SERVED confirmed phantoms ***")
            for r in sorted(served_ph, key=lambda x: (x['state'], x['facility']))[:20]:
                print(f"    row {r['excel_row']}: {r['facility']}, {r['city']} {r['state']}")
                print(f"      NC={r['nc_units']} AL={r['al_units']} MC={r['mc_units']}  |  CCN: {r['nic_ccn'] or '(none)'}")
                print(f"      {r['detail']}")

    # --- CO_LOCATED detail ---
    colocated = by_class.get('CO_LOCATED', [])
    if colocated:
        print()
        print("-" * 70)
        print(f"CO-LOCATED CAMPUSES ({len(colocated)}) — Have both NC + AL/MC units")
        print("-" * 70)
        served_co = sum(1 for r in colocated if r['do_we_serve'] == 'Yes')
        print(f"  {served_co} served  |  These are real ALFs on shared campuses — keep them")

    # --- IL_ONLY detail ---
    il_only = by_class.get('IL_ONLY', [])
    if il_only:
        print()
        print("-" * 70)
        print(f"PURE IL FACILITIES ({len(il_only)}) — IL units only, no AL/MC/NC")
        print("-" * 70)
        served_il = sum(1 for r in il_only if r['do_we_serve'] == 'Yes')
        print(f"  {served_il} served  |  These should be flagged non-serviceable")

        il_by_state = defaultdict(int)
        for r in il_only:
            il_by_state[r['state']] += 1
        print("  By state:")
        for state, count in sorted(il_by_state.items(), key=lambda x: -x[1])[:10]:
            fp = " *" if state in FOOTPRINT else ""
            print(f"    {state}: {count}{fp}")

    # --- PROPCO resolution ---
    propco_resolved = [r for r in results if 'PROPCO_AS_CORPORATE' in r['tags']]
    propco_split = [r for r in results if 'PROPCO_SPLIT' in r['tags']]
    if propco_resolved or propco_split:
        print()
        print("-" * 70)
        print(f"PROPCO/OPCO RESOLUTION")
        print("-" * 70)
        print(f"  Corporate_Name = Owner (PROPCO confirmed): {len(propco_resolved):,}")
        print(f"  Operator != Owner (split visible):         {len(propco_split):,}")

        if propco_resolved:
            # Show top operators that should replace PROPCO names
            operator_counts = defaultdict(int)
            for r in propco_resolved:
                operator_counts[r['nic_operator']] += 1
            print()
            print(f"  Top operators hidden behind PROPCO names:")
            for op, count in sorted(operator_counts.items(), key=lambda x: -x[1])[:20]:
                print(f"    {count:4d}x  {op}")

    # --- Tag frequency ---
    tag_counts = defaultdict(int)
    for r in results:
        for tag in r['tags'].split(', '):
            if tag:
                tag_counts[tag] += 1
    print()
    print("-" * 70)
    print("ALL TAG FREQUENCY")
    print("-" * 70)
    for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
        print(f"  {tag:<25} {count:>6,}")


def main():
    parser = argparse.ArgumentParser(description="NIC Maps Enrichment Audit")
    parser.add_argument('--state', help="Filter to a single state")
    parser.add_argument('--csv', action='store_true', help="Write enriched CSV")
    args = parser.parse_args()

    print("NIC Maps Enrichment Audit — Wave 0 (Enhanced)")
    print()

    print("Loading Combined Database...")
    _, db_rows = load_db()
    print(f"  {len(db_rows):,} rows loaded.")

    print("Loading NIC Maps source...")
    _, nic_rows = load_nic_alf()
    print(f"  {len(nic_rows):,} NIC buildings loaded.")

    print("Loading CMS SNF source (for CCN cross-ref)...")
    _, cms_rows = load_cms_snf()
    print(f"  {len(cms_rows):,} CMS records loaded.")

    print("Building indexes...")
    nic_index = build_nic_index(nic_rows)
    print(f"  {len(nic_index):,} NIC address keys")

    cms_ccn_index = build_cms_ccn_index(cms_rows)
    print(f"  {len(cms_ccn_index):,} CMS CCN keys")

    # SNF index from our DB for co-location check
    snf_index = {}
    for row in db_rows:
        if safe(row.get('Source_Type')) == 'SNF':
            key = addr_key(
                safe(row.get('Address')),
                safe(row.get('City')),
                safe(row.get('State')),
            )
            if key and key != '||':
                snf_index[key] = row
    print(f"  {len(snf_index):,} DB SNF address keys")

    print()
    print("Classifying ALF rows with NIC enrichment...")
    results = run_enrichment(db_rows, nic_index, cms_ccn_index, snf_index,
                             state_filter=args.state)

    print_summary(results)

    if args.csv:
        report_dir = ensure_report_dir()
        suffix = f"_{args.state}" if args.state else ""
        write_csv(results, report_dir / f"nic_enrichment{suffix}.csv")


if __name__ == '__main__':
    main()
