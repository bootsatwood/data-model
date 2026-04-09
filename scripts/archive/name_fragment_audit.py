import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # archive: find utils.py
#!/usr/bin/env python3
"""
Corporate Name Fragmentation Audit — Wave 0

Groups Corporate_Name variants by normalized stem to identify fragmented
names that should be consolidated. For example, "LIBERTY" appears as 15+
variants (LIBERTY SENIOR LIVING, LIBERTY, 630 CAROLINA BAY NC PROPCO LLC,
etc.) that all represent the same operator.

Approach:
  1. Normalize all Corporate_Names to a canonical stem (lowercase, alphanum)
  2. Group rows by stem
  3. Report stems with multiple distinct spellings (fragmentation)

Usage:
  python name_fragment_audit.py              # Full audit
  python name_fragment_audit.py --csv        # Write CSV report
  python name_fragment_audit.py --min 2      # Minimum variant count (default: 2)
  python name_fragment_audit.py --source ALF # Filter to ALF only
"""

import argparse
import csv
from collections import defaultdict

from utils import load_db, norm, safe, ensure_report_dir, FOOTPRINT


def build_name_clusters(db_rows, source_filter=None):
    """Group Corporate_Names by normalized stem.

    Returns dict: norm_name -> {
        'variants': {spelling: count},
        'rows': [row_summaries],
        'total_rows': int,
    }
    """
    clusters = defaultdict(lambda: {'variants': defaultdict(int), 'rows': [], 'total_rows': 0})

    for row in db_rows:
        corp = safe(row.get('Corporate_Name'))
        if not corp:
            continue
        source = safe(row.get('Source_Type'))
        if source_filter and source != source_filter:
            continue

        n = norm(corp)
        if not n:
            continue

        cluster = clusters[n]
        cluster['variants'][corp] += 1
        cluster['total_rows'] += 1
        cluster['rows'].append({
            'excel_row': row['_excel_row'],
            'facility': safe(row.get('Facility_Name')),
            'corporate_name': corp,
            'city': safe(row.get('City')),
            'state': safe(row.get('State')),
            'source_type': source,
            'ownership_type': safe(row.get('Ownership_Type')),
            'do_we_serve': safe(row.get('Do_We_Serve')),
        })

    return clusters


def find_fragmented(clusters, min_variants=2):
    """Filter to clusters with multiple distinct spellings."""
    fragmented = {}
    for stem, data in clusters.items():
        if len(data['variants']) >= min_variants:
            fragmented[stem] = data
    return fragmented


def write_csv(fragmented, outpath):
    """Write fragmentation report to CSV.

    One row per Corporate_Name variant, grouped by stem.
    """
    if not fragmented:
        print("  No fragmentation found — CSV not written.")
        return

    rows = []
    for stem in sorted(fragmented, key=lambda s: -fragmented[s]['total_rows']):
        data = fragmented[stem]
        variant_count = len(data['variants'])
        for variant, count in sorted(data['variants'].items(), key=lambda x: -x[1]):
            # Get sample states and ownership types for this variant
            variant_rows = [r for r in data['rows'] if r['corporate_name'] == variant]
            states = sorted(set(r['state'] for r in variant_rows))
            sources = sorted(set(r['source_type'] for r in variant_rows))
            own_types = sorted(set(r['ownership_type'] for r in variant_rows))
            served = sum(1 for r in variant_rows if r['do_we_serve'] == 'Yes')

            rows.append({
                'norm_stem': stem,
                'variant_count_in_cluster': variant_count,
                'total_rows_in_cluster': data['total_rows'],
                'corporate_name': variant,
                'row_count': count,
                'states': ', '.join(states),
                'source_types': ', '.join(sources),
                'ownership_types': ', '.join(own_types),
                'served_count': served,
            })

    fieldnames = list(rows[0].keys())
    with open(outpath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  CSV written: {outpath} ({len(rows)} variant rows across {len(fragmented)} clusters)")


def print_summary(fragmented, clusters):
    print()
    print("=" * 70)
    print("CORPORATE NAME FRAGMENTATION AUDIT")
    print("=" * 70)
    print()
    print(f"Total distinct Corporate_Names (normalized): {len(clusters):,}")
    print(f"Clusters with 2+ spelling variants: {len(fragmented):,}")

    total_affected = sum(d['total_rows'] for d in fragmented.values())
    print(f"Total facility rows in fragmented clusters: {total_affected:,}")

    # Show top fragmented clusters by total row count
    sorted_clusters = sorted(fragmented.items(), key=lambda x: -x[1]['total_rows'])

    print()
    print("-" * 70)
    print(f"TOP FRAGMENTED CLUSTERS (showing up to 30)")
    print("-" * 70)

    for stem, data in sorted_clusters[:30]:
        variant_count = len(data['variants'])
        total = data['total_rows']
        served = sum(1 for r in data['rows'] if r['do_we_serve'] == 'Yes')
        states = sorted(set(r['state'] for r in data['rows']))
        sources = sorted(set(r['source_type'] for r in data['rows']))

        served_tag = f"  *** {served} SERVED ***" if served else ""
        print(f"\n  [{stem}] — {variant_count} variants, {total} rows, "
              f"{', '.join(sources)}, {', '.join(states[:5])}"
              f"{'...' if len(states) > 5 else ''}{served_tag}")

        for variant, count in sorted(data['variants'].items(), key=lambda x: -x[1]):
            v_rows = [r for r in data['rows'] if r['corporate_name'] == variant]
            v_own = sorted(set(r['ownership_type'] for r in v_rows))
            print(f"    {count:4d}x  \"{variant}\"  [{', '.join(v_own)}]")

    # Summary statistics
    variant_distribution = defaultdict(int)
    for data in fragmented.values():
        variant_distribution[len(data['variants'])] += 1

    print()
    print("-" * 70)
    print("VARIANT COUNT DISTRIBUTION")
    print("-" * 70)
    for v_count in sorted(variant_distribution):
        cluster_count = variant_distribution[v_count]
        print(f"  {v_count} variants: {cluster_count} clusters")


def main():
    parser = argparse.ArgumentParser(description="Corporate Name Fragmentation Audit")
    parser.add_argument('--min', type=int, default=2, help="Minimum variant count (default: 2)")
    parser.add_argument('--source', choices=['SNF', 'ALF'], help="Filter to one source type")
    parser.add_argument('--csv', action='store_true', help="Write CSV report")
    args = parser.parse_args()

    print("Corporate Name Fragmentation Audit — Wave 0")
    print()

    print("Loading Combined Database...")
    _, db_rows = load_db()
    print(f"  {len(db_rows):,} rows loaded.")

    print("Building name clusters...")
    clusters = build_name_clusters(db_rows, source_filter=args.source)
    print(f"  {len(clusters):,} distinct normalized names.")

    print("Identifying fragmented clusters...")
    fragmented = find_fragmented(clusters, min_variants=args.min)

    print_summary(fragmented, clusters)

    if args.csv:
        report_dir = ensure_report_dir()
        suffix = f"_{args.source}" if args.source else ""
        write_csv(fragmented, report_dir / f"name_fragment_audit{suffix}.csv")


if __name__ == '__main__':
    main()
