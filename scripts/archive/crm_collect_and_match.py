"""
CRM Pipeline: Collect blank items from Monday.com data files and match against V25.

This script reads Monday.com items from JSON files (saved from API responses),
matches them against V25 PostgreSQL data, and outputs a write plan.

Usage:
  1. Save Monday.com API response items to scripts/monday_blanks/*.json
  2. Run: python scripts/crm_collect_and_match.py
  3. Review output
  4. Execute writes with crm_execute_writes.py
"""

import json
import os
import psycopg2
from difflib import SequenceMatcher

STATE_MAP = {
    'INDIANA':'IN','OHIO':'OH','KENTUCKY':'KY','NORTH CAROLINA':'NC',
    'SOUTH CAROLINA':'SC','VIRGINIA':'VA','WEST VIRGINIA':'WV',
    'GEORGIA':'GA','TENNESSEE':'TN','FLORIDA':'FL',
    'PENNSYLVANIA':'PA','NEW YORK':'NY','MICHIGAN':'MI',
    'ILLINOIS':'IL','MARYLAND':'MD',
}

SKIP_NAMES = {'New facility', 'new facility', 'New facility name', ''}


def norm(s):
    if not s: return ''
    s = s.upper().strip()
    # Remove (copy) suffix
    while s.endswith('(COPY)'):
        s = s[:-6].strip()
    for sfx in [' - SNF',' - ALF',' SNF',' ALF',' LLC',' INC',
                ' NURSING AND REHABILITATION',' NURSING & REHABILITATION',
                ' NURSING AND REHAB',' NURSING & REHAB',
                ' HEALTH AND REHABILITATION',' HEALTH & REHABILITATION',
                ' HEALTH AND REHAB',' HEALTH & REHAB',
                ' REHABILITATION CENTER',' REHAB CENTER',
                ' HEALTHCARE CENTER',' HEALTH CENTER',
                ' SENIOR LIVING',' ASSISTED LIVING',
                ' RETIREMENT COMMUNITY',' CARE CENTER',
                ' NURSING HOME',' AND REHABILITATION CENTER',
                ' HEALTH AND REHABILITATION CENTER',
                ' NURSING AND REHABILITATION CENTER',
                ' HEALTH & REHAB CENTER',' NURSING & REHAB CENTER']:
        if s.endswith(sfx): s = s[:-len(sfx)].strip()
    return s


def normalize_state(state):
    if not state: return ''
    s = state.upper().strip()
    if len(s) == 2: return s
    return STATE_MAP.get(s, s[:2])


def main():
    # Load V25 data
    print("Loading V25 from PostgreSQL...")
    conn = psycopg2.connect(
        host="keystone-platform-postgres.postgres.database.azure.com",
        port=5432, database="postgres", user="ratwood",
        password="Ch0EeU3yz7ep5bEWTKT1UoC^NMPCZXzN", sslmode="require",
    )
    cur = conn.cursor()

    # Build city+state index
    cur.execute("SELECT facility_name, corporate_name_raw, city, state FROM bd.market_intel_facilities")
    cs_index = {}
    all_facilities = []
    for name, corp, city, state in cur.fetchall():
        all_facilities.append((name, corp, city, state))
        if city and state:
            key = (city.upper().strip(), state.strip())
            if key not in cs_index:
                cs_index[key] = []
            cs_index[key].append((name, corp, norm(name)))

    # Corporates with 3+ facilities
    cur.execute("""SELECT corporate_name FROM bd.market_intel_corporate_entities ce
        JOIN bd.market_intel_facilities f ON f.corporate_entity_id = ce.id
        GROUP BY corporate_name HAVING COUNT(*) >= 3
        ORDER BY LENGTH(corporate_name) DESC""")
    corporates = [r[0] for r in cur.fetchall()]

    cur.close()
    conn.close()

    print(f"  {len(all_facilities)} facilities, {len(corporates)} corporates, {len(cs_index)} city+state combos")

    # Load Monday items from JSON files
    items_dir = os.path.join(os.path.dirname(__file__), 'monday_blanks')
    if not os.path.exists(items_dir):
        print(f"No items directory at {items_dir}")
        print("Please save Monday.com blank items as JSON files in scripts/monday_blanks/")
        return

    all_items = []
    for fn in sorted(os.listdir(items_dir)):
        if fn.endswith('.json'):
            with open(os.path.join(items_dir, fn), 'r') as f:
                items = json.load(f)
                all_items.extend(items)
                print(f"  Loaded {len(items)} items from {fn}")

    print(f"\nTotal items to process: {len(all_items)}")

    # Skip "New facility" placeholders
    real_items = [i for i in all_items if i['name'] not in SKIP_NAMES]
    print(f"After removing placeholders: {len(real_items)}")

    # Match each item
    matches = []
    no_matches = []

    for item in real_items:
        item_name = item['name']
        item_city = item.get('city', '') or ''
        item_state = normalize_state(item.get('state', ''))
        item_name_n = norm(item_name)
        item_city_n = item_city.upper().strip()
        item_upper = item_name.upper()

        result = None
        method = ''
        matched_name = ''

        # Tier 1: Name contains known corporate (4+ chars)
        for corp in corporates:
            corp_upper = corp.upper()
            if len(corp_upper) >= 4 and corp_upper in item_upper:
                result = corp
                method = 'CORP_IN_NAME'
                break

        # Tier 2: Exact name + city + state
        if not result and item_city_n and item_state:
            candidates = cs_index.get((item_city_n, item_state), [])
            for fn, fc, fnn in candidates:
                if fnn == item_name_n and fc:
                    result = fc
                    method = 'EXACT_CS'
                    matched_name = fn
                    break

        # Tier 3: Fuzzy name + city + state (>= 0.75)
        if not result and item_city_n and item_state:
            candidates = cs_index.get((item_city_n, item_state), [])
            best_score = 0
            for fn, fc, fnn in candidates:
                s = SequenceMatcher(None, item_name_n, fnn).ratio()
                if s > best_score and fc:
                    best_score = s
                    result = fc
                    matched_name = fn
                    method = f'FUZZY_CS_{s:.2f}'
            if best_score < 0.65:
                result = None
                method = ''
                matched_name = ''

        # Tier 4: Fuzzy name + state only (>= 0.85)
        if not result and item_state:
            best_score = 0
            for fn, fc, city, state in all_facilities:
                if state and state.strip() == item_state and fc:
                    s = SequenceMatcher(None, item_name_n, norm(fn)).ratio()
                    if s > best_score:
                        best_score = s
                        result = fc
                        matched_name = fn
                        method = f'FUZZY_S_{s:.2f}'
            if best_score < 0.85:
                result = None
                method = ''
                matched_name = ''

        if result:
            matches.append({
                'id': item['id'],
                'name': item_name,
                'city': item_city,
                'state': item.get('state', ''),
                'corporate': result,
                'method': method,
                'matched': matched_name,
            })
        else:
            no_matches.append({
                'id': item['id'],
                'name': item_name,
                'city': item_city,
                'state': item.get('state', ''),
            })

    # Output results
    print(f"\n{'='*80}")
    print(f"RESULTS: {len(matches)} matched, {len(no_matches)} unmatched")
    print(f"{'='*80}")

    # Save write plan
    write_plan_path = os.path.join(os.path.dirname(__file__), 'crm_write_plan.json')
    with open(write_plan_path, 'w') as f:
        json.dump(matches, f, indent=2)
    print(f"\nWrite plan saved to {write_plan_path}")

    # Save no-match list
    no_match_path = os.path.join(os.path.dirname(__file__), 'crm_no_matches.json')
    with open(no_match_path, 'w') as f:
        json.dump(no_matches, f, indent=2)
    print(f"No-match list saved to {no_match_path}")

    # Summary by method
    from collections import Counter
    methods = Counter(m['method'] for m in matches)
    print(f"\nMatch methods:")
    for method, count in methods.most_common():
        print(f"  {method}: {count}")

    # Summary by corporate
    corps = Counter(m['corporate'] for m in matches)
    print(f"\nTop 20 corporates matched:")
    for corp, count in corps.most_common(20):
        print(f"  {corp}: {count}")

    # Show some no-matches
    print(f"\nFirst 20 unmatched:")
    for item in no_matches[:20]:
        print(f"  {item['name']} | {item['city']} | {item['state']}")


if __name__ == '__main__':
    main()
