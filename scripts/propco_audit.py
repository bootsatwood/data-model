#!/usr/bin/env python3
"""
PROPCO/OPCO Corporate Name Audit — Wave 0

Finds rows where Corporate_Name matches property-company naming patterns
rather than operating-company names. These typically come from NIC Maps ALF
data where the ownership entity is a real-estate holding company, not the
facility operator.

Patterns detected:
  - PROPCO (property company)
  - OPCO (operating company entity, not the actual operator brand)
  - LLC / HOLDINGS / PROPERTIES / PARTNERS / TRUST / REALTY
  - Address-based names (start with a street number)
  - NOT AVAIL / UNKNOWN placeholders

Usage:
  python propco_audit.py              # Full audit
  python propco_audit.py --csv        # Write CSV report
  python propco_audit.py --state NC   # Filter to one state
"""

import argparse
import csv
import re
from collections import defaultdict

from utils import load_db, safe, ensure_report_dir, FOOTPRINT


# ---------------------------------------------------------------------------
# Pattern definitions
# ---------------------------------------------------------------------------

PROPCO_PATTERNS = [
    (r'\bPROPCO\b', 'PROPCO'),
    (r'\bOPCO\b', 'OPCO'),
    (r'\bHOLDINGS?\b', 'HOLDINGS'),
    (r'\bPROPERT(Y|IES)\b', 'PROPERTIES'),
    (r'\bPARTNERS?\b', 'PARTNERS'),
    (r'\bTRUST\b', 'TRUST'),
    (r'\bREALTY\b', 'REALTY'),
    (r'\bINVESTORS?\b', 'INVESTOR'),
]

# Address-based names: starts with digits (e.g., "630 CAROLINA BAY NC PROPCO LLC")
ADDRESS_PATTERN = re.compile(r'^\d+\s')

# Placeholder names
PLACEHOLDER_PATTERN = re.compile(r'^(NOT AVAIL|UNKNOWN|N/A|NONE)$', re.IGNORECASE)

# LLC suffix (only flagged if the name ALSO has another pattern or is address-based)
LLC_PATTERN = re.compile(r'\bLLC\b', re.IGNORECASE)


def classify_corporate_name(name):
    """Check if a Corporate_Name matches PROPCO/OPCO patterns.

    Returns a list of matched pattern tags, or empty list if clean.
    """
    if not name:
        return []

    tags = []
    upper = name.upper()

    # Check explicit patterns
    for pattern, tag in PROPCO_PATTERNS:
        if re.search(pattern, upper):
            tags.append(tag)

    # Check address-based name
    if ADDRESS_PATTERN.match(name):
        tags.append('ADDRESS_BASED')

    # Check placeholder
    if PLACEHOLDER_PATTERN.match(name.strip()):
        tags.append('PLACEHOLDER')

    # LLC alone is very common and not always a problem — only flag if
    # the name is short (likely a shell entity) or has another pattern
    if LLC_PATTERN.search(upper):
        if tags:
            tags.append('LLC')
        elif len(name.split()) <= 4:
            # Short LLC names are often shell entities
            tags.append('SHORT_LLC')

    return tags


def audit(db_rows, state_filter=None):
    """Find all rows with PROPCO/OPCO naming patterns."""
    results = []

    for row in db_rows:
        state = safe(row.get('State'))
        if state_filter and state != state_filter:
            continue

        corp = safe(row.get('Corporate_Name'))
        if not corp:
            continue

        tags = classify_corporate_name(corp)
        if not tags:
            continue

        results.append({
            'excel_row': row['_excel_row'],
            'facility': safe(row.get('Facility_Name')),
            'corporate_name': corp,
            'address': safe(row.get('Address')),
            'city': safe(row.get('City')),
            'state': state,
            'source_type': safe(row.get('Source_Type')),
            'ownership_type': safe(row.get('Ownership_Type')),
            'do_we_serve': safe(row.get('Do_We_Serve')),
            'beds': safe(row.get('Total_Beds')),
            'census': safe(row.get('Census')),
            'pattern_tags': ', '.join(tags),
        })

    return results


def write_csv(results, outpath):
    """Write audit results to CSV."""
    if not results:
        print("  No matches found — CSV not written.")
        return
    fieldnames = list(results[0].keys())
    with open(outpath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"  CSV written: {outpath} ({len(results)} rows)")


def print_summary(results):
    """Print console summary."""
    print()
    print("=" * 70)
    print("PROPCO/OPCO CORPORATE NAME AUDIT")
    print("=" * 70)
    print()
    print(f"Total rows with property-company naming patterns: {len(results)}")

    # By source type
    by_source = defaultdict(int)
    for r in results:
        by_source[r['source_type']] += 1
    print(f"  SNF: {by_source.get('SNF', 0)}  |  ALF: {by_source.get('ALF', 0)}")

    # By pattern tag
    tag_counts = defaultdict(int)
    for r in results:
        for tag in r['pattern_tags'].split(', '):
            tag_counts[tag] += 1
    print()
    print("Pattern breakdown:")
    for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
        print(f"  {tag}: {count}")

    # By ownership type
    by_own = defaultdict(int)
    for r in results:
        by_own[r['ownership_type']] += 1
    print()
    print("Ownership type:")
    for own, count in sorted(by_own.items(), key=lambda x: -x[1]):
        print(f"  {own}: {count}")

    served = [r for r in results if r['do_we_serve'] == 'Yes']
    if served:
        print(f"\n  *** {len(served)} SERVED rows have PROPCO/OPCO names ***")
        for r in served:
            print(f"    row {r['excel_row']}: {r['facility']} — {r['corporate_name']}")

    # Top corporate names by frequency
    name_counts = defaultdict(int)
    for r in results:
        name_counts[r['corporate_name']] += 1

    print()
    print(f"Top corporate names ({min(25, len(name_counts))} of {len(name_counts)} distinct):")
    for name, count in sorted(name_counts.items(), key=lambda x: -x[1])[:25]:
        tags = next(r['pattern_tags'] for r in results if r['corporate_name'] == name)
        print(f"  {count:3d}x  {name}  [{tags}]")

    # By state (footprint only)
    by_state = defaultdict(int)
    for r in results:
        by_state[r['state']] += 1
    print()
    print("By state (footprint):")
    for state in sorted(by_state):
        if state in FOOTPRINT:
            print(f"  {state}: {by_state[state]}")
    non_fp = sum(c for s, c in by_state.items() if s not in FOOTPRINT)
    if non_fp:
        print(f"  (non-footprint total: {non_fp})")


def main():
    parser = argparse.ArgumentParser(description="PROPCO/OPCO Corporate Name Audit")
    parser.add_argument('--state', help="Filter to a single state")
    parser.add_argument('--csv', action='store_true', help="Write CSV report")
    args = parser.parse_args()

    print("PROPCO/OPCO Corporate Name Audit — Wave 0")
    print()

    print("Loading Combined Database...")
    _, db_rows = load_db()
    print(f"  {len(db_rows):,} rows loaded.")

    print("Scanning for PROPCO/OPCO patterns...")
    results = audit(db_rows, state_filter=args.state)

    print_summary(results)

    if args.csv:
        report_dir = ensure_report_dir()
        suffix = f"_{args.state}" if args.state else ""
        write_csv(results, report_dir / f"propco_audit{suffix}.csv")


if __name__ == '__main__':
    main()
