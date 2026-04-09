import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # archive: find utils.py
#!/usr/bin/env python3
"""
IL/55+ Contamination Audit — Wave 0

Flags ALF rows where the facility name or corporate name contains keywords
indicating Independent Living or 55+ Active Adult communities. These
facilities are outside the Eventus serviceable market (no clinical services)
but may be present in NIC Maps ALF data.

Keyword categories:
  - Independent Living (IL, independent living, senior living independent)
  - 55+ / Active Adult (55+, active adult, senior apartments)
  - CCRC indicators (continuing care, life plan)

Usage:
  python il_contamination_audit.py              # Full audit
  python il_contamination_audit.py --csv        # Write CSV report
  python il_contamination_audit.py --state NC   # Filter to one state
"""

import argparse
import csv
import re
from collections import defaultdict

from utils import load_db, safe, ensure_report_dir, FOOTPRINT


# ---------------------------------------------------------------------------
# Keyword patterns (case-insensitive)
# ---------------------------------------------------------------------------

IL_KEYWORDS = [
    # Independent Living explicit
    (r'\bindependent\s+living\b', 'INDEPENDENT_LIVING'),
    (r'\bIL\b(?!\w)', 'IL_ABBREVIATION'),  # "IL" as standalone (not part of "ILLINOIS" etc.)
    (r'\bsenior\s+apartments?\b', 'SENIOR_APARTMENTS'),
    (r'\bsenior\s+residences?\b', 'SENIOR_RESIDENCE'),
    (r'\bretirement\s+apartments?\b', 'RETIREMENT_APARTMENTS'),
    # 55+ / Active Adult
    (r'55\s*\+', 'AGE_55_PLUS'),
    (r'\bactive\s+adult\b', 'ACTIVE_ADULT'),
    (r'\badult\s+community\b', 'ADULT_COMMUNITY'),
    (r'\badult\s+living\b', 'ADULT_LIVING'),
    # CCRC indicators
    (r'\bcontinuing\s+care\b', 'CCRC'),
    (r'\blife\s+plan\b', 'LIFE_PLAN'),
    (r'\bCCRC\b', 'CCRC'),
    # Other non-serviceable signals
    (r'\bvillas?\b', 'VILLA'),
    (r'\bcottages?\b', 'COTTAGE'),
    (r'\btownhome\b', 'TOWNHOME'),
]

# Compiled patterns
COMPILED_PATTERNS = [(re.compile(p, re.IGNORECASE), tag) for p, tag in IL_KEYWORDS]

# States where "IL" abbreviation should be suppressed (Illinois confusion)
IL_STATE_SUPPRESS = {'IL'}


def check_il_keywords(text, state=''):
    """Check text for IL/55+ keywords. Returns list of matched tags."""
    if not text:
        return []

    tags = []
    for pattern, tag in COMPILED_PATTERNS:
        # Suppress IL_ABBREVIATION in Illinois to avoid false positives
        if tag == 'IL_ABBREVIATION' and state in IL_STATE_SUPPRESS:
            continue
        if pattern.search(text):
            tags.append(tag)

    return tags


def audit(db_rows, state_filter=None):
    """Flag ALF rows with IL/55+ contamination signals."""
    results = []

    for row in db_rows:
        if safe(row.get('Source_Type')) != 'ALF':
            continue
        state = safe(row.get('State'))
        if state_filter and state != state_filter:
            continue

        facility = safe(row.get('Facility_Name'))
        corp = safe(row.get('Corporate_Name'))

        fac_tags = check_il_keywords(facility, state)
        corp_tags = check_il_keywords(corp, state)

        all_tags = list(set(fac_tags + corp_tags))
        if not all_tags:
            continue

        # Classify confidence
        # HIGH: explicit IL/55+ in facility name
        # MEDIUM: only in corporate name, or only weak signals (VILLA, COTTAGE)
        weak_tags = {'VILLA', 'COTTAGE', 'TOWNHOME', 'SENIOR_RESIDENCE'}
        strong_fac_tags = [t for t in fac_tags if t not in weak_tags]

        if strong_fac_tags:
            confidence = 'HIGH'
        elif fac_tags:
            confidence = 'MEDIUM'
        elif corp_tags:
            confidence = 'LOW'
        else:
            confidence = 'LOW'

        results.append({
            'excel_row': row['_excel_row'],
            'facility': facility,
            'corporate_name': corp,
            'address': safe(row.get('Address')),
            'city': safe(row.get('City')),
            'state': state,
            'ownership_type': safe(row.get('Ownership_Type')),
            'do_we_serve': safe(row.get('Do_We_Serve')),
            'beds': safe(row.get('Total_Beds')),
            'census': safe(row.get('Census')),
            'data_quality_flag': safe(row.get('Data_Quality_Flag')),
            'facility_tags': ', '.join(fac_tags) if fac_tags else '',
            'corporate_tags': ', '.join(corp_tags) if corp_tags else '',
            'all_tags': ', '.join(sorted(all_tags)),
            'confidence': confidence,
        })

    return results


def write_csv(results, outpath):
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
    print()
    print("=" * 70)
    print("IL/55+ CONTAMINATION AUDIT")
    print("=" * 70)
    print()
    print(f"Total ALF rows with IL/55+ signals: {len(results)}")

    high = [r for r in results if r['confidence'] == 'HIGH']
    medium = [r for r in results if r['confidence'] == 'MEDIUM']
    low = [r for r in results if r['confidence'] == 'LOW']
    print(f"  HIGH confidence:   {len(high)}")
    print(f"  MEDIUM confidence: {len(medium)}")
    print(f"  LOW confidence:    {len(low)}")

    served = [r for r in results if r['do_we_serve'] == 'Yes']
    if served:
        print(f"\n  *** {len(served)} SERVED ALF rows flagged ***")

    # Tag frequency
    tag_counts = defaultdict(int)
    for r in results:
        for tag in r['all_tags'].split(', '):
            if tag:
                tag_counts[tag] += 1
    print()
    print("Keyword frequency:")
    for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
        print(f"  {tag}: {count}")

    # By state
    by_state = defaultdict(int)
    for r in results:
        by_state[r['state']] += 1
    print()
    print("By state (top 15):")
    for state, count in sorted(by_state.items(), key=lambda x: -x[1])[:15]:
        fp_tag = " *" if state in FOOTPRINT else ""
        print(f"  {state}: {count}{fp_tag}")

    # HIGH confidence detail
    if high:
        print()
        print("-" * 70)
        print(f"HIGH-CONFIDENCE IL/55+ FLAGS ({len(high)})")
        print("-" * 70)
        for r in sorted(high, key=lambda x: (x['state'], x['city']))[:50]:
            print(f"  row {r['excel_row']}: {r['facility']}")
            print(f"    {r['city']}, {r['state']}  |  Tags: {r['all_tags']}")
            if r['corporate_name']:
                print(f"    Corp: {r['corporate_name']}")


def main():
    parser = argparse.ArgumentParser(description="IL/55+ Contamination Audit")
    parser.add_argument('--state', help="Filter to a single state")
    parser.add_argument('--csv', action='store_true', help="Write CSV report")
    args = parser.parse_args()

    print("IL/55+ Contamination Audit — Wave 0")
    print()

    print("Loading Combined Database...")
    _, db_rows = load_db()
    alf_count = sum(1 for r in db_rows if safe(r.get('Source_Type')) == 'ALF')
    print(f"  {len(db_rows):,} total rows  |  {alf_count:,} ALF rows to scan.")

    print("Scanning for IL/55+ keywords...")
    results = audit(db_rows, state_filter=args.state)

    print_summary(results)

    if args.csv:
        report_dir = ensure_report_dir()
        suffix = f"_{args.state}" if args.state else ""
        write_csv(results, report_dir / f"il_contamination_audit{suffix}.csv")


if __name__ == '__main__':
    main()
