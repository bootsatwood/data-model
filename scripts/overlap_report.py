#!/usr/bin/env python3
"""
ALF-SNF Overlap Report — Wave 0

Cross-references the entire ALF set in the Combined Database against the
CMS SNF source using composite address key (norm_addr + city + state).

Produces a full overlap matrix showing:
  - ALF rows that match a CMS SNF record (potential phantoms or co-located)
  - ALF rows with no CMS SNF match (genuinely ALF-only addresses)
  - CMS SNF records in footprint not in our database (coverage gaps)

Usage:
  python overlap_report.py              # Full report
  python overlap_report.py --csv        # Write CSV reports
  python overlap_report.py --state NC   # Filter to one state
"""

import argparse
import csv
from collections import defaultdict

from utils import (
    load_db, load_cms_snf, addr_key, norm, safe,
    ensure_report_dir, FOOTPRINT,
)


def build_db_indexes(db_rows):
    """Build address key indexes for SNF and ALF rows separately."""
    snf_index = {}
    alf_index = defaultdict(list)

    for row in db_rows:
        source = safe(row.get('Source_Type'))
        key = addr_key(
            safe(row.get('Address')),
            safe(row.get('City')),
            safe(row.get('State')),
        )
        if not key or key == '||':
            continue

        if source == 'SNF':
            snf_index[key] = row
        elif source == 'ALF':
            alf_index[key].append(row)

    return snf_index, alf_index


def build_cms_index(cms_rows, state_filter=None):
    """Build address key index for CMS SNF records."""
    index = {}
    for row in cms_rows:
        state = safe(row.get('State'))
        if state_filter and state != state_filter:
            continue
        key = addr_key(
            safe(row.get('Provider Address')),
            safe(row.get('City/Town')),
            safe(row.get('State')),
        )
        if key and key != '||':
            index[key] = row
    return index


def analyze_overlap(db_rows, cms_rows, state_filter=None):
    """Compute the full overlap matrix."""
    # Filter DB rows by state if requested
    if state_filter:
        db_rows = [r for r in db_rows if safe(r.get('State')) == state_filter]

    snf_index, alf_index = build_db_indexes(db_rows)
    cms_index = build_cms_index(cms_rows, state_filter)

    all_alf_keys = set(alf_index.keys())
    all_snf_keys = set(snf_index.keys())
    all_cms_keys = set(cms_index.keys())

    # Overlap categories for ALF rows
    alf_matches_snf = all_alf_keys & all_snf_keys          # ALF at same address as our SNF
    alf_matches_cms = all_alf_keys & all_cms_keys           # ALF at same address as CMS SNF
    alf_matches_both = alf_matches_snf & alf_matches_cms    # ALF matches both
    alf_matches_snf_only = alf_matches_snf - all_cms_keys   # ALF matches our SNF but not CMS
    alf_matches_cms_only = alf_matches_cms - all_snf_keys   # ALF matches CMS but not our SNF
    alf_no_match = all_alf_keys - all_snf_keys - all_cms_keys  # ALF-only addresses

    # Coverage gaps: CMS SNFs not in our database at all
    # (footprint states only)
    cms_footprint = {k for k in all_cms_keys
                     if safe(cms_index[k].get('State')) in FOOTPRINT}
    cms_not_in_db = cms_footprint - all_snf_keys

    # Build detailed records for matched ALFs
    matched_alfs = []
    for key in sorted(alf_matches_snf | alf_matches_cms):
        alf_rows = alf_index.get(key, [])
        snf_row = snf_index.get(key)
        cms_row = cms_index.get(key)

        match_type = []
        if key in alf_matches_both:
            match_type.append('BOTH')
        elif key in alf_matches_snf_only:
            match_type.append('DB_SNF_ONLY')
        elif key in alf_matches_cms_only:
            match_type.append('CMS_ONLY')

        for alf in alf_rows:
            record = {
                'alf_excel_row': alf['_excel_row'],
                'alf_facility': safe(alf.get('Facility_Name')),
                'alf_corporate': safe(alf.get('Corporate_Name')),
                'alf_address': safe(alf.get('Address')),
                'alf_city': safe(alf.get('City')),
                'alf_state': safe(alf.get('State')),
                'alf_beds': safe(alf.get('Total_Beds')),
                'alf_census': safe(alf.get('Census')),
                'alf_ownership': safe(alf.get('Ownership_Type')),
                'alf_served': safe(alf.get('Do_We_Serve')),
                'match_type': ', '.join(match_type),
            }

            if snf_row:
                record['snf_excel_row'] = snf_row['_excel_row']
                record['snf_facility'] = safe(snf_row.get('Facility_Name'))
                record['snf_corporate'] = safe(snf_row.get('Corporate_Name'))
                record['snf_beds'] = safe(snf_row.get('Total_Beds'))
            else:
                record['snf_excel_row'] = ''
                record['snf_facility'] = ''
                record['snf_corporate'] = ''
                record['snf_beds'] = ''

            if cms_row:
                record['cms_provider'] = safe(cms_row.get('Provider Name'))
                record['cms_beds'] = safe(cms_row.get('Number of Certified Beds'))
                record['cms_chain'] = safe(cms_row.get('Chain Name'))
            else:
                record['cms_provider'] = ''
                record['cms_beds'] = ''
                record['cms_chain'] = ''

            matched_alfs.append(record)

    # Build gap records
    gap_records = []
    for key in sorted(cms_not_in_db):
        cms_row = cms_index[key]
        gap_records.append({
            'cms_provider': safe(cms_row.get('Provider Name')),
            'cms_address': safe(cms_row.get('Provider Address')),
            'cms_city': safe(cms_row.get('City/Town')),
            'cms_state': safe(cms_row.get('State')),
            'cms_beds': safe(cms_row.get('Number of Certified Beds')),
            'cms_chain': safe(cms_row.get('Chain Name')),
            'cms_chain_id': safe(cms_row.get('Chain ID')),
        })

    return {
        'total_alf_keys': len(all_alf_keys),
        'total_snf_keys': len(all_snf_keys),
        'total_cms_keys': len(all_cms_keys),
        'alf_matches_both': len(alf_matches_both),
        'alf_matches_snf_only': len(alf_matches_snf_only),
        'alf_matches_cms_only': len(alf_matches_cms_only),
        'alf_no_match': len(alf_no_match),
        'cms_footprint_total': len(cms_footprint),
        'cms_not_in_db': len(cms_not_in_db),
        'matched_alfs': matched_alfs,
        'gap_records': gap_records,
    }


def write_csvs(results, report_dir, suffix=''):
    """Write overlap and gap CSVs."""
    if results['matched_alfs']:
        path = report_dir / f"overlap_alf_snf_matches{suffix}.csv"
        fieldnames = list(results['matched_alfs'][0].keys())
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results['matched_alfs'])
        print(f"  Overlap CSV: {path} ({len(results['matched_alfs'])} rows)")

    if results['gap_records']:
        path = report_dir / f"overlap_cms_gaps{suffix}.csv"
        fieldnames = list(results['gap_records'][0].keys())
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results['gap_records'])
        print(f"  Gap CSV: {path} ({len(results['gap_records'])} rows)")


def print_summary(results):
    print()
    print("=" * 70)
    print("ALF-SNF OVERLAP REPORT")
    print("=" * 70)
    print()
    print("Address key universe:")
    print(f"  ALF address keys:  {results['total_alf_keys']:,}")
    print(f"  SNF address keys:  {results['total_snf_keys']:,}")
    print(f"  CMS address keys:  {results['total_cms_keys']:,}")

    print()
    print("ALF overlap categories:")
    total_matched = (results['alf_matches_both']
                     + results['alf_matches_snf_only']
                     + results['alf_matches_cms_only'])
    print(f"  Matches BOTH DB-SNF + CMS:  {results['alf_matches_both']:,}")
    print(f"  Matches DB-SNF only:        {results['alf_matches_snf_only']:,}")
    print(f"  Matches CMS only:           {results['alf_matches_cms_only']:,}")
    print(f"  ---")
    print(f"  Total ALF-SNF overlaps:     {total_matched:,}")
    print(f"  ALF-only (no SNF match):    {results['alf_no_match']:,}")

    if results['total_alf_keys'] > 0:
        overlap_pct = total_matched / results['total_alf_keys'] * 100
        print(f"  Overlap rate:               {overlap_pct:.1f}%")

    print()
    print("CMS coverage gaps (footprint states):")
    print(f"  CMS SNFs in footprint:      {results['cms_footprint_total']:,}")
    print(f"  Not in our DB:              {results['cms_not_in_db']:,}")

    # Show detail on matched ALFs
    served_matches = [r for r in results['matched_alfs'] if r['alf_served'] == 'Yes']
    if served_matches:
        print(f"\n  *** {len(served_matches)} SERVED ALF rows overlap with SNF addresses ***")

    # By state
    by_state = defaultdict(int)
    for r in results['matched_alfs']:
        by_state[r['alf_state']] += 1
    if by_state:
        print()
        print("ALF-SNF overlaps by state (top 10):")
        for state, count in sorted(by_state.items(), key=lambda x: -x[1])[:10]:
            fp_tag = " *" if state in FOOTPRINT else ""
            print(f"  {state}: {count}{fp_tag}")

    # Match type breakdown
    by_type = defaultdict(int)
    for r in results['matched_alfs']:
        by_type[r['match_type']] += 1
    if by_type:
        print()
        print("Match type breakdown:")
        for mtype, count in sorted(by_type.items(), key=lambda x: -x[1]):
            print(f"  {mtype}: {count}")


def main():
    parser = argparse.ArgumentParser(description="ALF-SNF Overlap Report")
    parser.add_argument('--state', help="Filter to a single state")
    parser.add_argument('--csv', action='store_true', help="Write CSV reports")
    args = parser.parse_args()

    print("ALF-SNF Overlap Report — Wave 0")
    print()

    print("Loading Combined Database...")
    _, db_rows = load_db()
    print(f"  {len(db_rows):,} rows loaded.")

    print("Loading CMS SNF source...")
    _, cms_rows = load_cms_snf()
    print(f"  {len(cms_rows):,} CMS SNF records loaded.")

    print("Computing overlap matrix...")
    results = analyze_overlap(db_rows, cms_rows, state_filter=args.state)

    print_summary(results)

    if args.csv:
        report_dir = ensure_report_dir()
        suffix = f"_{args.state}" if args.state else ""
        write_csvs(results, report_dir, suffix)


if __name__ == '__main__':
    main()
