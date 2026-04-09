#!/usr/bin/env python3
"""
Phantom Duplicate Audit — Wave 0

Detects ALF rows in the Combined Database that duplicate existing SNF rows
at the same normalized address+city+state. These "phantom" ALFs inflate
facility counts and revenue estimates.

Uses the CMS SNF source as ground truth: if an ALF row's address matches
a CMS SNF record, and a corresponding SNF row already exists in our DB,
that ALF is a phantom duplicate.

Usage:
  python phantom_audit.py                  # Full audit
  python phantom_audit.py --state NC       # Filter to one state
  python phantom_audit.py --csv            # Write CSV report
"""

import argparse
import csv
import sys
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # archive: find utils.py
from collections import defaultdict
from pathlib import Path

from utils import (
    load_db, load_cms_snf, addr_key, norm, norm_addr, safe,
    ensure_report_dir, FOOTPRINT,
)


def build_snf_index(rows):
    """Index SNF rows by composite address key."""
    index = {}
    for row in rows:
        if safe(row.get('Source_Type')) != 'SNF':
            continue
        key = addr_key(
            safe(row.get('Address')),
            safe(row.get('City')),
            safe(row.get('State')),
        )
        if key and key != '||':
            index[key] = row
    return index


def build_cms_index(cms_rows):
    """Index CMS SNF records by composite address key."""
    index = {}
    for row in cms_rows:
        key = addr_key(
            safe(row.get('Provider Address')),
            safe(row.get('City/Town')),
            safe(row.get('State')),
        )
        if key and key != '||':
            index[key] = row
    return index


def find_phantoms(db_rows, snf_index, cms_index, state_filter=None):
    """Find ALF rows that match an SNF at the same address.

    Returns a list of dicts describing each phantom pair.
    """
    phantoms = []

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
        if not key or key == '||':
            continue

        # Check: does this ALF address match an SNF in our DB?
        snf_match = snf_index.get(key)
        # Check: does this ALF address match a CMS SNF record?
        cms_match = cms_index.get(key)

        if snf_match or cms_match:
            confidence = 'HIGH' if (snf_match and cms_match) else 'MEDIUM'

            alf_name = safe(row.get('Facility_Name'))
            alf_corp = safe(row.get('Corporate_Name'))

            # Name similarity check — boost confidence if names are very similar
            if snf_match:
                snf_name = safe(snf_match.get('Facility_Name'))
                if norm(alf_name) == norm(snf_name):
                    confidence = 'HIGH'

            record = {
                'alf_excel_row': row['_excel_row'],
                'alf_facility': alf_name,
                'alf_corporate': alf_corp,
                'alf_address': safe(row.get('Address')),
                'alf_city': safe(row.get('City')),
                'alf_state': state,
                'alf_beds': safe(row.get('Total_Beds')),
                'alf_census': safe(row.get('Census')),
                'alf_ownership': safe(row.get('Ownership_Type')),
                'alf_served': safe(row.get('Do_We_Serve')),
                'confidence': confidence,
            }

            if snf_match:
                record['snf_excel_row'] = snf_match['_excel_row']
                record['snf_facility'] = safe(snf_match.get('Facility_Name'))
                record['snf_corporate'] = safe(snf_match.get('Corporate_Name'))
                record['snf_beds'] = safe(snf_match.get('Total_Beds'))
                record['snf_census'] = safe(snf_match.get('Census'))
            else:
                record['snf_excel_row'] = ''
                record['snf_facility'] = ''
                record['snf_corporate'] = ''
                record['snf_beds'] = ''
                record['snf_census'] = ''

            if cms_match:
                record['cms_provider'] = safe(cms_match.get('Provider Name'))
                record['cms_beds'] = safe(cms_match.get('Number of Certified Beds'))
                record['cms_chain'] = safe(cms_match.get('Chain Name'))
                record['cms_chain_id'] = safe(cms_match.get('Chain ID'))
            else:
                record['cms_provider'] = ''
                record['cms_beds'] = ''
                record['cms_chain'] = ''
                record['cms_chain_id'] = ''

            phantoms.append(record)

    return phantoms


def write_csv(phantoms, outpath):
    """Write phantom audit results to CSV."""
    if not phantoms:
        print("  No phantoms found — CSV not written.")
        return

    fieldnames = list(phantoms[0].keys())
    with open(outpath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(phantoms)
    print(f"  CSV written: {outpath} ({len(phantoms)} rows)")


def print_summary(phantoms):
    """Print a console summary of phantom audit results."""
    print()
    print("=" * 70)
    print("PHANTOM DUPLICATE AUDIT")
    print("=" * 70)
    print()
    print(f"Total suspect ALF-SNF address matches: {len(phantoms)}")

    high = [p for p in phantoms if p['confidence'] == 'HIGH']
    medium = [p for p in phantoms if p['confidence'] == 'MEDIUM']
    print(f"  HIGH confidence (DB SNF + CMS match): {len(high)}")
    print(f"  MEDIUM confidence (one source match):  {len(medium)}")

    served = [p for p in phantoms if p['alf_served'] == 'Yes']
    if served:
        print(f"  *** {len(served)} SERVED ALF rows are phantom suspects ***")

    # Group by state
    by_state = defaultdict(list)
    for p in phantoms:
        by_state[p['alf_state']].append(p)

    print()
    print("By state:")
    for state in sorted(by_state):
        count = len(by_state[state])
        fp_tag = " (FOOTPRINT)" if state in FOOTPRINT else ""
        print(f"  {state}: {count}{fp_tag}")

    # Show detail for HIGH confidence
    if high:
        print()
        print("-" * 70)
        print(f"HIGH-CONFIDENCE PHANTOMS ({len(high)})")
        print("-" * 70)
        for p in sorted(high, key=lambda x: (x['alf_state'], x['alf_city'])):
            print(f"\n  ALF row {p['alf_excel_row']}: {p['alf_facility']}")
            print(f"    {p['alf_address']}, {p['alf_city']} {p['alf_state']}")
            print(f"    Corp: {p['alf_corporate'] or '(blank)'}  |  Beds: {p['alf_beds']}  |  Census: {p['alf_census']}")
            if p['snf_facility']:
                print(f"  SNF row {p['snf_excel_row']}: {p['snf_facility']}")
                print(f"    Corp: {p['snf_corporate'] or '(blank)'}  |  Beds: {p['snf_beds']}  |  Census: {p['snf_census']}")
            if p['cms_provider']:
                print(f"  CMS: {p['cms_provider']}  |  Beds: {p['cms_beds']}  |  Chain: {p['cms_chain']}")
            if p['alf_served'] == 'Yes':
                print(f"    *** SERVED ***")

    # Show detail for MEDIUM confidence (first 20)
    if medium:
        print()
        print("-" * 70)
        show = medium[:20]
        print(f"MEDIUM-CONFIDENCE PHANTOMS (showing {len(show)} of {len(medium)})")
        print("-" * 70)
        for p in sorted(show, key=lambda x: (x['alf_state'], x['alf_city'])):
            match_type = "DB-SNF" if p['snf_facility'] else "CMS-only"
            print(f"  [{match_type}] row {p['alf_excel_row']}: {p['alf_facility']}, "
                  f"{p['alf_city']} {p['alf_state']}  |  Corp: {p['alf_corporate'] or '(blank)'}")


def main():
    parser = argparse.ArgumentParser(description="Phantom Duplicate Audit")
    parser.add_argument('--state', help="Filter to a single state (e.g. NC)")
    parser.add_argument('--csv', action='store_true', help="Write CSV report")
    args = parser.parse_args()

    print("Phantom Duplicate Audit — Wave 0")
    print()

    print("Loading Combined Database...")
    headers, db_rows = load_db()
    print(f"  {len(db_rows):,} rows loaded.")

    print("Loading CMS SNF source...")
    _, cms_rows = load_cms_snf()
    print(f"  {len(cms_rows):,} CMS SNF records loaded.")

    print("Building indexes...")
    snf_index = build_snf_index(db_rows)
    cms_index = build_cms_index(cms_rows)
    print(f"  {len(snf_index):,} DB SNF keys  |  {len(cms_index):,} CMS SNF keys")

    print("Scanning for phantom ALF duplicates...")
    phantoms = find_phantoms(db_rows, snf_index, cms_index, state_filter=args.state)

    print_summary(phantoms)

    if args.csv:
        report_dir = ensure_report_dir()
        suffix = f"_{args.state}" if args.state else ""
        write_csv(phantoms, report_dir / f"phantom_audit{suffix}.csv")


if __name__ == '__main__':
    main()
