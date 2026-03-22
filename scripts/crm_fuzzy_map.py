"""
CRM Pipeline Corporate Owner Fuzzy Mapper

Matches AE-entered corporate owner values from Monday.com CRM Pipeline
to V25 canonical names in PostgreSQL.

Produces a mapping file for review before executing updates.
"""

import psycopg2
from difflib import SequenceMatcher

# AE values from board insights query (2026-03-21)
AE_VALUES = [
    ("Priority Life Care", 7), ("REAL PROPERTY HEALTH FACILITIES", 1),
    ("American Senior Communities", 9), ("Casa Consulting", 7),
    ("American Senior Care", 4), ("Sonida Senior Living", 3), ("TLC", 4),
    ("Carecore", 2), ("National Church Residences", 1), ("Envive", 3),
    ("Arcadia", 3), ("Private", 12), ("East way", 1), ("signature", 1),
    ("PACS", 6), ("Signature", 5), ("Trilogy", 21),
    ("Clearview Healthcare", 8), ("Charter", 2), ("Topaz", 4),
    ("Clearview", 1), ("SEKY Holding Co.", 1), ("Louisville", 1),
    ("clearview", 1), ("Signature Healthcare Community", 5),
    ("Principle", 5), ("Topaz Healthcare", 5), ("Bungalows", 1),
    ("Presbyterian Homes of Kentucky", 2), ("Christian Care Center", 2),
    ("trilogy", 2), ("nazareth", 1), ("Baptist Life Communities", 1),
    ("Baptist Live Communities", 1), ("Willow Ridge Senior Living", 1),
    ("HCMG", 4), ("Celebrations", 2), ("Glenridge Healthcare", 2),
    ("Triple Crown", 9), ("Principle/Venza", 6), ("CHI", 1),
    ("Dominion Senior Living", 1), ("Hillstone HC", 2), ("Lionstone", 7),
    ("HCF Management", 4), ("JAG", 6), ("Foundations Health Solutions", 2),
    ("CCH", 5), ("Liberty Healthcare", 7),
    ("Sprenger Healthcare Systems", 2), ("Divine Healthcare Management", 3),
    ("Astoria SNF inc,", 1), ("McKinley Holdco", 1),
    ("Allegiance Healthcare", 1), ("Foundations", 8), ("Cardon", 8),
    ("Provisions", 1), ("Saber", 15), ("Prestige Healthcare", 4),
    ("Pacs Group", 2), ("Garden Healthcare Group", 1),
    ("EMBASSY HEALTHCARE", 5), ("Ciena", 7), ("Otterbein", 11),
    ("James D, Inc.", 1), ("Vancrest Health Care Centers", 9),
    ("Optalis", 3), ("Sonida Living", 2), ("Legacy", 1), ("Brookdale", 89),
    ("Majestic Care", 26), ("Altercare Integrated Health Services", 1),
    ("Aspire", 5), ("Christina Village Communities", 1), ("Liberty", 5),
    ("Our Home", 1), ("Communicare", 5), ("CHS", 1),
    ("Sunshine Retirement Living", 1), ("Traditions", 3), ("Laurels", 1),
    ("Continuing Health Solutions", 1), ("Country Club", 1), ("Arbors", 1),
    ("Altercare", 1), ("Victorian Senior", 4),
    ("Life Enrichment Communities", 1), ("SABER HEALTHCARE GROUP", 20),
    ("Principle LTC", 8), ("Independent", 6),
    ("Crown Pointe Communities", 2), ("Life Care Centers of America", 4),
    ("Infinity Healthcare Management", 2), ("OPS Living", 1),
    ("Miller's Merry Manor", 4), ("Hill Valley Healthcare", 1),
    ("Sterling Healthcare", 4), ("Waters", 8), ("Story Point", 3),
    ("ASC", 37), ("Privately Owned", 40), ("OPCO", 1), ("Gardant", 2),
    ("Bloom", 2), ("Brickyard", 8), ("Majesticare", 5),
    ("Adams county memorial Hospital", 1), ("Majestic", 5), ("waters", 1),
    ("priority", 1), ("Transcendent", 1), ("Witham Memorial Hospital", 1),
    ("Life Care", 3), ("1019 Healthcare", 4), ("Aperion", 3), ("asc", 1),
    ("Castle Health Care", 4), ("Eastern HCG", 4), ("LifeWorks", 4),
    ("Bedford County", 1), ("MFA", 8), ("Eastern Care Group", 4),
    ("Cedar", 2), ("Hill Valley", 14), ("Westminster Canterbury", 1),
    ("Deer Meadows", 1), ("NHC", 1), ("Trio Healthcare", 3),
    ("Valley Care", 3), ("Heritage Hall", 4),
    ("Sunnyside Presbyterian Home", 3), ("CCR", 1), ("Runk & Pratt", 5),
    ("Inspirit Senior Living", 1), ("Integrity", 2), ("Sanstone", 4),
    ("ALG", 8), ("Carrolton", 3), ("Spring Arbor", 5), ("TerraBella", 3),
    ("ALG Senior", 23), ("Jaybird", 1), ("Consulate", 1), ("YAD", 7),
    ("Cardinal Care", 1), ("Harborview", 1), ("Five Star", 4),
    ("Century Care Management", 3), ("Navion", 5), ("MainStay", 4),
    ("William James Group", 1), ("Sinceri Senior Living", 4),
    ("Vitality Senior Living", 1), ("Harmony", 1), ("Mainstay", 1),
    ("Majes", 1), ("Moravian Church", 1), ("Navion SL", 6),
    ("Twenty20 Management", 4), ("SHCM", 1), ("HCF", 1),
    ("Marquis Health Consulting Services", 1), ("Promedica", 1),
    ("APRIL ENTERPRISES, INC.", 1), ("Ohio Living", 2), ("AHF Ohio", 1),
    ("Pavilion Healthcare", 2), ("Exceptional Living Centers", 1),
    ("Care Managment Group", 1), ("NHC Healthcare", 2),
    ("Erikson Senior Living", 1), ("CCH Healthcare", 3),
    ("A Grace Mgmt Community", 1), ("Commonwealth", 1),
    ("Commonwealth Senior Living", 1),
    ("SANSTONE HEALTH & REHABILITATION", 4), ("Major Hospital", 3),
    ("TRILOGY HEALTH SERVICES", 35), ("LIONSTONE CARE", 7),
    ("Unafilliated", 3), ("CERTUS HEALTHCARE", 7),
    ("HEALTH CARE MANAGEMENT GROUP", 5), ("Masonic Home", 3),
    ("Prestige", 3), ("Citadel Healthcare", 1),
    ("GARDEN HEALTHCARE GROUP", 2), ("ELC", 1),
    ("BRICKYARD HEALTHCARE", 11), ("Luxor", 1),
    ("Harborview Health Systems", 1), ("Terra Bella", 6), ("ISG Inc", 1),
    ("Liberty Senior Living", 1), ("Alliance", 2), ("Avardis", 4),
    ("Peak Resources", 1), ("Southern Healthcare Management", 1),
    ("White Oak Manor", 1), ("ADAMS COUNTY MEMORIAL HOSPITAL", 2),
    ("AMERICAN SENIOR COMMUNITIES", 28),
]

# Non-corporate designations (don't map to V25)
NON_CORPORATE = {
    "Private", "Privately Owned", "Independent", "Unafilliated", "OPCO",
}

# Manual overrides for known bad fuzzy matches
MANUAL_OVERRIDES = {
    # Bad containment/fuzzy matches corrected
    "Waters": "THE WATERS",
    "waters": "THE WATERS",
    "Navion SL": "Navion Senior Solutions",
    "Miller's Merry Manor": "MILLER'S MERRY MANOR",
    "Sprenger Healthcare Systems": "SPRENGER HEALTH CARE SYSTEMS",
    "Infinity Healthcare Management": "INFINITY HEALTHCARE CONSULTING",
    "Celebrations": None,  # Unknown — leave as-is, needs manual research
    "Glenridge Healthcare": None,  # Unknown
    "American Senior Care": None,  # Distinct from American Senior Communities — needs research
    "HCMG": "HEALTH CARE MANAGEMENT GROUP",  # Abbreviation
    "Eastern HCG": "EASTERN HEALTHCARE GROUP",
    "Eastern Care Group": "EASTERN HEALTHCARE GROUP",
    "Cedar": None,  # Too generic — needs facility-level matching
    "Louisville": None,  # City name, not a corporate
    "nazareth": None,  # Too ambiguous
    "Sunnyside Presbyterian Home": "SUNNYSIDE PRESBYTERIAN HOME",
    "McKinley Holdco": None,  # Unknown
    "Provisions": None,  # Unknown
    "Christina Village Communities": None,  # Unknown
    "Life Enrichment Communities": None,  # Unknown
    "White Oak Manor": "WHITE OAK MANAGEMENT",
    "Moravian Church": None,  # Unknown — religious org
    "SHCM": "SOUTHERN HEALTHCARE MANAGEMENT, LLC",  # Abbreviation
    "Witham Memorial Hospital": "WITHAM MEMORIAL HOSPITAL",  # Leave as-is (hospital)
    "Our Home": None,  # Too generic
    "CHS": None,  # Too ambiguous (multiple possible matches)
    "ELC": "EXCEPTIONAL LIVING CENTERS",  # Abbreviation
    "East way": None,  # Unknown
    "CCR": None,  # Too ambiguous
    "Baptist Life Communities": "BAPTIST LIFE COMMUNITIES",  # Leave as-is
    "Baptist Live Communities": "BAPTIST LIFE COMMUNITIES",  # Typo fix
    "Clearview Healthcare": "CLEARVIEW HEALTHCARE",  # Don't normalize to CLEARVIEW
    "Signature": "SIGNATURE HEALTHCARE",
    "signature": "SIGNATURE HEALTHCARE",
    "Signature Healthcare Community": "SIGNATURE HEALTHCARE",
    "Prestige": "PRESTIGE HEALTHCARE",
    "Prestige Healthcare": "PRESTIGE HEALTHCARE",
    "Masonic Home": None,  # Multiple distinct Masonic Homes — needs facility match
    "Allegiance Healthcare": None,  # Unknown — needs research
    "APRIL ENTERPRISES, INC.": None,  # Unknown
    "A Grace Mgmt Community": None,  # Unknown
    "Deer Meadows": None,  # Unknown
    "Hillstone HC": "HILLSTONE HEALTHCARE",
    "Continuing Health Solutions": "CONTINUING HEALTHCARE SOLUTIONS",
    "OPS Living": "OPS SOUTH BEND LLC",
    "Arcadia": "ARCADIA CARE",  # IN/OH operator, not the MD one
    "Sonida Living": "SONIDA SENIOR LIVING",
    "Liberty Healthcare": "LIBERTY",  # Same as Liberty in DB
    "Liberty Senior Living": "LIBERTY",
    "Brookdale": "BROOKDALE SENIOR LIVING",
    "Foundations": "FOUNDATIONS HEALTH",
    "Foundations Health Solutions": "FOUNDATIONS HEALTH",
    "Cardon": "CARDON & ASSOCIATES",
    "Principle/Venza": "PRINCIPLE",
    "Story Point": "STORYPOINT",
    "Ciena": "CIENA HEALTHCARE/LAUREL HEALTH CARE",
    "Terra Bella": "TerraBella Senior Living",
    "Majesticare": "MAJESTIC CARE",
    "Majestic": "MAJESTIC CARE",
    "Majes": "MAJESTIC CARE",
    "Five Star": "FIVE STAR RESIDENCES",
    "Lionstone": "LIONSTONE CARE",
    "Saber": "SABER HEALTHCARE GROUP",
    "Otterbein": "OTTERBEIN SENIOR LIFE",
    "Triple Crown": "Triple Crown Senior Living",
    "Navion": "Navion Senior Solutions",
    "Gardant": "GARDANT MANAGEMENT SOLUTIONS",
    "NHC Healthcare": "NATIONAL HEALTHCARE CORPORATION",
    "NHC": "NATIONAL HEALTHCARE CORPORATION",
    "Victorian Senior": "VICTORIAN SENIOR CARE",
    "Principle LTC": "PRINCIPLE",
    "Bloom": "Bloom Senior Living",
    "Commonwealth": "COMMONWEALTH SENIOR LIVING",
    "Optalis": "Optalis Healthcare",
    "CHI": "CHI LIVING",
    "Castle Health Care": "CASTLE HEALTHCARE",
    "Charter": "CHARTER SENIOR LIVING",
    "Spring Arbor": "SPRING ARBOR MANAGEMENT",
    "Jaybird": "JAYBIRD SENIOR LIVING",
    "Cardinal Care": "Cardinal Care Management",
    "Harborview": "HARBORVIEW HEALTH SYSTEMS",
    "Harmony": None,  # Could be Harmony Senior Services or Harmony Care Group
    "Consulate": "Consulate Health Care",
    "MainStay": "MAINSTAY SENIOR LIVING",
    "Mainstay": "MAINSTAY SENIOR LIVING",
    "Integrity": "INTEGRITY SENIOR LIVING",
    "Vitality Senior Living": "VITALITY LIVING",
    "Life Care": "LIFE CARE SERVICES",
    "Country Club": None,  # Too generic
    "Laurels": "LAURELS",
    "Altercare": "ALTERCARE",
    "Luxor": "LUXOR HEALTHCARE GROUP",
    "Westminster Canterbury": "WESTMINSTER CANTERBURY",
    "Peak Resources": "PEAK RESOURCES",
    "Southern Healthcare Management": "SOUTHERN HEALTHCARE MANAGEMENT, LLC",
    "Erikson Senior Living": "ERICKSON SENIOR LIVING",
    "Care Managment Group": "CARE MANAGEMENT GROUP",
    "Twenty20 Management": "TWENTY/20 MANAGEMENT",
    "LifeWorks": "LIFEWORKS REHAB",
    "Presbyterian Homes of Kentucky": None,  # Distinct KY org
    "Christian Care Center": None,  # Local org
    "Hill Valley Healthcare": "Hill Valley",
    "Sterling Healthcare": "STERLING HEALTHCARE MANAGEMENT",
    "Valley Care": "VALLEY CARE MANAGEMENT",
    "Carrolton": "CARROLTON FACILTY MANAGEMENT",
}


def get_v25_names():
    conn = psycopg2.connect(
        host="keystone-platform-postgres.postgres.database.azure.com",
        port=5432, database="postgres", user="ratwood",
        password="Ch0EeU3yz7ep5bEWTKT1UoC^NMPCZXzN", sslmode="require",
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT corporate_name FROM bd.market_intel_corporate_entities ORDER BY corporate_name")
    names = [r[0] for r in cur.fetchall()]
    cur.close()
    conn.close()
    return names


def normalize(s):
    """Lowercase, strip common suffixes for matching."""
    s = s.lower().strip()
    for suffix in [" healthcare", " health care", " health", " senior living",
                   " living", " management", " group", " inc", " llc", " corp",
                   " solutions", " services", " systems", " centers",
                   " of america", " integrated health services"]:
        if s.endswith(suffix):
            s = s[:-len(suffix)].strip()
    return s


def fuzzy_match(ae_val, v25_names, v25_upper, v25_normalized):
    """Find best V25 match for an AE value."""
    ae_upper = ae_val.upper()
    ae_norm = normalize(ae_val)

    # 1. Exact case-insensitive
    if ae_upper in v25_upper:
        return v25_upper[ae_upper], "EXACT", 1.0

    # 2. Normalized match
    if ae_norm in v25_normalized:
        return v25_normalized[ae_norm], "NORMALIZED", 0.95

    # 3. Containment (AE value is substring of V25 name or vice versa)
    for name in v25_names:
        if ae_upper in name.upper() or name.upper() in ae_upper:
            return name, "CONTAINMENT", 0.85

    # 4. Normalized containment
    for name in v25_names:
        n_name = normalize(name)
        if ae_norm in n_name or n_name in ae_norm:
            return name, "NORM_CONTAINMENT", 0.80

    # 5. Sequence matcher (fuzzy)
    best_score = 0
    best_match = None
    for name in v25_names:
        score = SequenceMatcher(None, ae_norm, normalize(name)).ratio()
        if score > best_score:
            best_score = score
            best_match = name

    if best_score >= 0.70:
        return best_match, "FUZZY", best_score

    return None, "NO_MATCH", best_score


def main():
    v25_names = get_v25_names()
    v25_upper = {n.upper(): n for n in v25_names}
    v25_normalized = {normalize(n): n for n in v25_names}

    print(f"V25 canonical names: {len(v25_names)}")
    print(f"AE values to map: {len(AE_VALUES)}")
    print()

    exact_matches = []
    rewrites = []
    no_matches = []
    skipped = []

    for ae_val, count in AE_VALUES:
        if ae_val in NON_CORPORATE:
            skipped.append((ae_val, count, "NON_CORPORATE"))
            continue

        # Check manual overrides first
        if ae_val in MANUAL_OVERRIDES:
            override = MANUAL_OVERRIDES[ae_val]
            if override is None:
                no_matches.append((ae_val, count, 0.0))
                continue
            match, method, score = override, "MANUAL", 1.0
        else:
            match, method, score = fuzzy_match(ae_val, v25_names, v25_upper, v25_normalized)

        if match:
            needs_rewrite = ae_val != match
            if needs_rewrite:
                rewrites.append((ae_val, match, count, method, score))
            else:
                exact_matches.append((ae_val, match, count))
        else:
            no_matches.append((ae_val, count, score))

    # Report
    print(f"{'='*80}")
    print(f"EXACT (no rewrite needed): {len(exact_matches)} values, {sum(c for _,_,c in exact_matches)} items")
    print(f"REWRITE needed: {len(rewrites)} values, {sum(c for _,_,c,_,_ in rewrites)} items")
    print(f"NO MATCH: {len(no_matches)} values, {sum(c for _,c,_ in no_matches)} items")
    print(f"SKIPPED (non-corporate): {len(skipped)} values, {sum(c for _,c,_ in skipped)} items")
    print(f"{'='*80}")

    print(f"\n{'='*80}")
    print("REWRITES (AE value -> V25 canonical)")
    print(f"{'='*80}")
    for ae, v25, cnt, method, score in sorted(rewrites, key=lambda x: -x[2]):
        print(f"  {ae:<45} -> {v25:<45} ({cnt:>3} items) [{method} {score:.2f}]")

    print(f"\n{'='*80}")
    print("EXACT MATCHES (already correct)")
    print(f"{'='*80}")
    for ae, v25, cnt in sorted(exact_matches, key=lambda x: -x[2]):
        print(f"  {ae:<45} ({cnt:>3} items)")

    print(f"\n{'='*80}")
    print("NO MATCH (need manual review)")
    print(f"{'='*80}")
    for ae, cnt, score in sorted(no_matches, key=lambda x: -x[1]):
        print(f"  {ae:<45} ({cnt:>3} items) [best score: {score:.2f}]")

    print(f"\n{'='*80}")
    print("SKIPPED (non-corporate designations)")
    print(f"{'='*80}")
    for ae, cnt, reason in skipped:
        print(f"  {ae:<45} ({cnt:>3} items)")


if __name__ == "__main__":
    main()
