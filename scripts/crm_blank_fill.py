"""
CRM Pipeline Blank Corporate Owner Fill

Matches Monday.com CRM Pipeline items with blank *Corporate Owner
to V25 PostgreSQL facilities by facility name + city + state.

Produces a dry-run report for review before executing updates.

Usage:
  python scripts/crm_blank_fill.py              # dry run
  python scripts/crm_blank_fill.py --execute     # live write (after review)
"""

import psycopg2
import json
import sys
import re
from difflib import SequenceMatcher

# Groups to process (excluding Established and Metro Markets)
ACTIVE_GROUPS = {
    "New Facility Targets", "New Facility Leads", "New Facility Prospects",
    "Contracting", "Consenting", "Scheduling", "Collins Opportunity",
    "REVISIT", "Unqualified",
}

# Skip items with these names
SKIP_NAMES = {"New facility", "new facility", ""}


def normalize_name(name):
    """Normalize facility name for matching."""
    if not name:
        return ""
    s = name.upper().strip()
    # Remove common suffixes/prefixes
    for remove in [" - SNF", " - ALF", " SNF", " ALF", " LLC", " INC",
                   " NURSING AND REHABILITATION", " NURSING & REHABILITATION",
                   " NURSING AND REHAB", " NURSING & REHAB",
                   " HEALTH AND REHABILITATION", " HEALTH & REHABILITATION",
                   " HEALTH AND REHAB", " HEALTH & REHAB",
                   " REHABILITATION CENTER", " REHAB CENTER",
                   " HEALTHCARE CENTER", " HEALTH CENTER",
                   " SENIOR LIVING", " ASSISTED LIVING",
                   " RETIREMENT COMMUNITY", " CARE CENTER",
                   " NURSING HOME", " CONVALESCENT CENTER"]:
        if s.endswith(remove):
            s = s[:-len(remove)].strip()
    return s


def normalize_city(city):
    """Normalize city for matching."""
    if not city:
        return ""
    return city.upper().strip()


def normalize_state(state):
    """Convert state name to 2-letter abbreviation."""
    if not state:
        return ""
    state_map = {
        "INDIANA": "IN", "OHIO": "OH", "KENTUCKY": "KY",
        "NORTH CAROLINA": "NC", "SOUTH CAROLINA": "SC",
        "VIRGINIA": "VA", "WEST VIRGINIA": "WV",
        "GEORGIA": "GA", "TENNESSEE": "TN", "FLORIDA": "FL",
        "PENNSYLVANIA": "PA", "NEW YORK": "NY", "MICHIGAN": "MI",
        "ILLINOIS": "IL", "MARYLAND": "MD", "CALIFORNIA": "CA",
        "TEXAS": "TX", "WISCONSIN": "WI", "MINNESOTA": "MN",
        "IOWA": "IA", "MISSOURI": "MO", "ALABAMA": "AL",
        "CONNECTICUT": "CT", "NEW JERSEY": "NJ", "DELAWARE": "DE",
        "MAINE": "ME", "MONTANA": "MT", "OREGON": "OR",
        "WASHINGTON": "WA", "IDAHO": "ID", "ARIZONA": "AZ",
        "COLORADO": "CO", "UTAH": "UT", "NEVADA": "NV",
        "LOUISIANA": "LA", "ARKANSAS": "AR", "MISSISSIPPI": "MS",
    }
    s = state.upper().strip()
    if len(s) == 2:
        return s
    return state_map.get(s, s)


def get_v25_facilities():
    """Load all V25 facilities from PostgreSQL."""
    conn = psycopg2.connect(
        host="keystone-platform-postgres.postgres.database.azure.com",
        port=5432, database="postgres", user="ratwood",
        password="Ch0EeU3yz7ep5bEWTKT1UoC^NMPCZXzN", sslmode="require",
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT facility_name, corporate_name_raw, city, state, address
        FROM bd.market_intel_facilities
        ORDER BY facility_name
    """)
    facilities = []
    for row in cur.fetchall():
        facilities.append({
            "name": row[0] or "",
            "corporate": row[1],
            "city": row[2] or "",
            "state": row[3] or "",
            "address": row[4] or "",
            "name_norm": normalize_name(row[0]),
            "city_norm": normalize_city(row[2]),
            "state_norm": normalize_state(row[3] or ""),
        })
    cur.close()
    conn.close()
    return facilities


def get_known_corporates():
    """Get list of known corporate names for name-contains matching."""
    conn = psycopg2.connect(
        host="keystone-platform-postgres.postgres.database.azure.com",
        port=5432, database="postgres", user="ratwood",
        password="Ch0EeU3yz7ep5bEWTKT1UoC^NMPCZXzN", sslmode="require",
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT corporate_name, COUNT(*) as cnt
        FROM bd.market_intel_corporate_entities ce
        JOIN bd.market_intel_facilities f ON f.corporate_entity_id = ce.id
        GROUP BY corporate_name
        HAVING COUNT(*) >= 3
        ORDER BY COUNT(*) DESC
    """)
    corporates = [(row[0], row[1]) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return corporates


def match_item(item_name, item_city, item_state, v25_facilities, corporates):
    """Try to match a Monday.com item to a V25 facility.

    Returns (corporate_name, method, confidence, v25_facility_name) or (None, None, 0, None)
    """
    item_name_norm = normalize_name(item_name)
    item_city_norm = normalize_city(item_city)
    item_state_norm = normalize_state(item_state)

    # Tier 1: Item name contains a known corporate name
    item_upper = item_name.upper()
    for corp_name, corp_count in corporates:
        corp_upper = corp_name.upper()
        # Only match if corporate name is 4+ chars (avoid false positives on short names)
        if len(corp_upper) >= 4 and corp_upper in item_upper:
            return corp_name, "NAME_CONTAINS_CORP", 0.95, None

    # Tier 2: Exact name + city + state match
    if item_city_norm and item_state_norm:
        for f in v25_facilities:
            if (f["name_norm"] == item_name_norm and
                f["city_norm"] == item_city_norm and
                f["state_norm"] == item_state_norm):
                if f["corporate"]:
                    return f["corporate"], "EXACT_NAME_CITY_STATE", 1.0, f["name"]

    # Tier 3: Fuzzy name + state match
    if item_state_norm:
        best_score = 0
        best_match = None
        for f in v25_facilities:
            if f["state_norm"] != item_state_norm:
                continue
            score = SequenceMatcher(None, item_name_norm, f["name_norm"]).ratio()
            if score > best_score:
                best_score = score
                best_match = f
        if best_score >= 0.80 and best_match and best_match["corporate"]:
            return best_match["corporate"], "FUZZY_NAME_STATE", best_score, best_match["name"]

    # Tier 4: Fuzzy name only (lowest confidence)
    best_score = 0
    best_match = None
    for f in v25_facilities:
        score = SequenceMatcher(None, item_name_norm, f["name_norm"]).ratio()
        if score > best_score:
            best_score = score
            best_match = f
    if best_score >= 0.85 and best_match and best_match["corporate"]:
        return best_match["corporate"], "FUZZY_NAME_ONLY", best_score, best_match["name"]

    return None, "NO_MATCH", 0, None


def main():
    dry_run = "--execute" not in sys.argv

    print("=" * 80)
    print(f"CRM Pipeline Blank Corporate Owner Fill {'(DRY RUN)' if dry_run else '(LIVE)'}")
    print("=" * 80)

    print("\nLoading V25 facilities from PostgreSQL...")
    v25_facilities = get_v25_facilities()
    print(f"  Loaded {len(v25_facilities)} facilities")

    print("Loading known corporates...")
    corporates = get_known_corporates()
    print(f"  Loaded {len(corporates)} corporates (3+ facilities)")

    # Read Monday.com items — we'll use the data already printed
    # For now, simulate with what we have
    print("\nNote: This script needs Monday.com item data passed in.")
    print("Run crm_blank_fill_with_monday.py for the full pipeline.")
    print(f"\nReady to match. V25 has {len(v25_facilities)} facilities, {len(corporates)} corporates.")

    # Quick test with some known items from the sample
    test_items = [
        ("Brickyard Healthcare - Knox Care Center", None, None),
        ("Aperion Estates Peru", None, None),
        ("Aperion Care Marion", None, None),
        ("Signature Healthcare Bremen", None, "Indiana"),
        ("Cedar Creek Assisted Living", "Bloomington", "Indiana"),
        ("Westview Nursing and Rehab", "Bedford", "Indiana"),
        ("Stonecroft Health Campus", "Bloomington", "Indiana"),
        ("Gentry Park Senior Living", "Bloomington", "Indiana"),
        ("Millers Merry Manor New Castle", None, None),
        ("Hickory Creek of New Castle", None, None),
        ("Christian Health Center Corbin", "Corbin", "Kentucky"),
        ("Williamsburg Health & Rehabilitation", "Williamsburg", "Kentucky"),
        ("Holy Cross Village", "Notre Dame", "Indiana"),
    ]

    print(f"\n{'='*80}")
    print("TEST MATCHES (from sample items)")
    print(f"{'='*80}")

    matched = 0
    unmatched = 0
    for name, city, state in test_items:
        corp, method, conf, v25_name = match_item(name, city, state, v25_facilities, corporates)
        if corp:
            matched += 1
            v25_display = f" (matched: {v25_name})" if v25_name else ""
            print(f"  MATCH  | {name:<45} -> {corp:<35} [{method} {conf:.2f}]{v25_display}")
        else:
            unmatched += 1
            print(f"  MISS   | {name:<45} -> ???")

    print(f"\nMatched: {matched}/{len(test_items)}, Unmatched: {unmatched}/{len(test_items)}")


if __name__ == "__main__":
    main()
