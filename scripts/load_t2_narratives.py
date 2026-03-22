"""
Load T2 corporate intel narratives into bd.market_intel_corporate_entities.

Updates hq_state, ceo, founded, website, key_insight, recommendation
for all Tier 2 entities using parameterized queries.

Source: corporate_operator_profiles.md + MUO Profile extractions.
"""

import sys
sys.path.insert(0, 'C:/Users/ratwood/keystone-platform/backend')
from app.services.shared.pg_client import PgClient

pg = PgClient()

# ── Narrative data keyed by canonical operator name ──────────────────────
# Each entry: (hq_state, ceo, founded, website, key_insight, recommendation, [db_names])

NARRATIVES = {
    "Life Care Centers of America": (
        "TN",
        "Aubrey Preston",
        "1970",
        "lcca.com",
        "Founded by billionaire Forrest Preston in 1970, LCCA is one of the largest privately held SNF operators in the U.S., operating across 27 states. Forrest Preston was sole owner for 55 years until son Aubrey Preston was named CEO and chairman in April 2025. Entirely family-owned, headquartered at the Campbell Center in Cleveland, TN.",
        "Massive scale but tightly family-controlled; relationship-building with regional operations leaders is the most viable path since ownership decisions flow from the Preston family.",
        ["LIFE CARE CENTERS OF AMERICA"],
    ),
    "TerraBella Senior Living": (
        "NC",
        "Richard J. Hutchinson (Discovery Senior Living)",
        "1991",
        "terrabellaseniorliving.com",
        "TerraBella is a brand within Discovery Senior Living, the largest privately held senior housing operator in the U.S., operating nearly 350 communities across 40 states. TerraBella communities are concentrated in North Carolina. Kellee Agee serves as President of the TerraBella brand.",
        "Decisions roll up to Discovery Senior Living corporate in Florida; engage Kellee Agee for NC-specific conversations but recognize that enterprise-level deals require Discovery corporate alignment.",
        ["TerraBella Senior Living"],
    ),
    "Fundamental": (
        "MD",
        "Scott Hillegass",
        "1986",
        "fundltc.com",
        "Founded in 1986, Fundamental is a nationwide healthcare services company operating nursing facilities, long-term acute care hospitals, hospice agencies, and centers for the developmentally disabled. Went through notable restructuring when Fundamental Long Term Care was acquired by Promise Healthcare. Fundamental Administrative Services continues as a management services company based in Maryland.",
        "Complex corporate structure with management-company and facility-ownership layers; confirm which entities are active operators vs. management-only before pursuing.",
        ["FUNDAMENTAL HEALTHCARE", "FUNDAMENTAL LTC"],
    ),
    "HCF Management": (
        "OH",
        "Kerri Romes",
        "1968",
        "hcfinc.com",
        "Family-owned since 1968 by the Unverferth family, now led by third-generation President Kerri Romes. Employs 4,000+ and serves 3,000+ patients across skilled nursing, assisted living, and in-home health care in Ohio and Pennsylvania. Acquired EncompassCare in 2012 and Heritage Health Care in 2019.",
        "Strong family-owned operator with demonstrated M&A activity; third-generation leadership suggests openness to modernization and partnerships.",
        ["HCF MANAGEMENT"],
    ),
    "SanStone": (
        "NC",
        "Jennifer Robinson",
        "2004",
        "sanstonehealth.com",
        "Founded in 2004 by Christopher Sprenger and Michael DeLoach, SanStone is an independently owned and operated SNF/rehabilitation provider with 20+ locations across North Carolina employing 2,500+ staff. Alex Atchison serves as Chief Strategy Officer.",
        "Active acquirer in NC with growth momentum; independently owned structure means direct access to decision-makers without PE intermediaries.",
        ["SANSTONE", "SANSTONE HEALTH & REHABILITATION"],
    ),
    "Altercare": (
        "OH",
        "Jerry Schroer",
        "1973",
        "altercare.com",
        "Family-owned by the Schroer family since 1973, Altercare operates 23 skilled nursing facilities across Ohio and Michigan. In 2018 entered an agreement to operate six additional Ohio SNFs from Greystone Healthcare Management.",
        "Large, stable family-owned Ohio operator with 50+ year track record; approach through Jerry Schroer or family leadership for strategic conversations.",
        ["ALTERCARE"],
    ),
    "Peak Resources": (
        "NC",
        "Not publicly identified",
        "1999",
        "peakresourcesinc.com",
        "Peak Resources is a family-owned and operated North Carolina company managing 17 SNF, memory care, and assisted living locations across the state. Founded in 1999, specific founder and CEO names are not publicly disclosed.",
        "Significant NC-concentrated operator but leadership is low-profile; may require local relationship-building or industry conference networking to identify decision-makers.",
        ["PEAK RESOURCES"],
    ),
    "Carespring": (
        "OH",
        "Chris Chirumbolo",
        "1985",
        "carespring.com",
        "Founded in 1985 by Barry Bortz with a single facility, Carespring has grown to 12 skilled nursing facilities and one senior living center (1,820 total beds) in the greater Cincinnati/Northern Kentucky region. After founder Bortz passed away, Chris Chirumbolo took over as CEO in 2017. Stated interest in regional expansion but only within driving distance of headquarters.",
        "Privately held, locally rooted operator with stated regional expansion appetite; CEO Chirumbolo is accessible and operationally hands-on.",
        ["CARESPRING"],
    ),
    "Phoenix Senior Living": (
        "GA",
        "Jesse Marinko",
        "2010",
        "phoenixsrliving.com",
        "Founded in 2010 by Jesse Marinko (25+ years senior living experience), Phoenix Senior Living is a privately held owner-operator-developer managing 45 properties across nine southeastern states. Seth Pesek appointed President to support continued growth.",
        "Fast-growing southeastern AL/memory care operator with founder-led culture; Jesse Marinko is the key relationship and the company is actively expanding into underserved suburban markets.",
        ["PHOENIX SENIOR LIVING"],
    ),
    "YAD Healthcare": (
        "NJ",
        "Hershy Alter",
        "2019",
        "yadhealth.com",
        "Founded in 2019 by Hershy Alter, a Licensed Nursing Home Administrator, YAD Healthcare provides management and operational support for skilled nursing facilities in Virginia and North Carolina. Specializes in turning around underperforming assets. Approximately 208 employees and $7.3M revenue.",
        "Small but growing turnaround-focused operator in VA/NC; young company with an aggressive acquisition posture -- could be a partnership or competitor depending on market overlap.",
        ["YAD", "YAD HEALTHCARE"],
    ),
    "Miller's Merry Manor": (
        "IN",
        "Patrick Boyle",
        "1964",
        "millersmerrymanor.com",
        "Founded in 1964 by the Miller family, Miller's Health Systems is a 100% employee-owned (ESOP since 2006) Indiana-based operator providing rehabilitation, assisted living, nursing homes, home health, and rehabilitation services statewide. CEO Patrick Boyle joined in 1984 and was named CEO in 2000.",
        "ESOP structure means no single owner to approach for acquisition; partnership and service contracts are the appropriate engagement model.",
        ["MILLERS MERRY MANOR"],
    ),
    "Sprenger Health Care Systems": (
        "OH",
        "Shannon Kuhn",
        "1959",
        "sprengerhealthcare.com",
        "Founded in 1959 by Grace Sprenger with Amherst Manor Retirement Community, Sprenger Healthcare is a third-generation family-owned operator in Ohio and South Carolina. Leadership transition with Shannon Kuhn becoming President/CEO. Sprenger family also connected to Continuing Healthcare Solutions.",
        "Leadership transition underway creates potential openness to new partnerships; family ties to CHS mean approaching Sprenger entities requires awareness of the broader family portfolio.",
        ["SPRENGER HEALTH CARE SYSTEMS"],
    ),
    "Certus Healthcare": (
        "OH",
        "Not publicly named",
        None,
        "certushc.com",
        "Certus Healthcare operates 15 skilled nursing and rehabilitation campuses, 1 continuing care retirement campus, and 2 assisted living communities throughout Ohio. Eric Hutchins serves as Senior Director, Business Development & Strategy.",
        "Eric Hutchins is the most visible external-facing leader and the right entry point for BD conversations; founder identities are deliberately low-profile.",
        ["CERTUS HEALTHCARE"],
    ),
    "White Oak Management": (
        "SC",
        "Steve Flatt (NHC)",
        "1964",
        "whiteoakmanor.com",
        "Founded by Oliver Kent Cecil in 1964 in Spartanburg, SC. Grew to 15 skilled nursing facilities across North and South Carolina. In August 2024, National HealthCare Corporation (NYSE: NHC) completed acquisition of the entire White Oak Senior Living portfolio. No longer independently owned.",
        "Now part of NHC (publicly traded); any engagement must go through NHC corporate channels, not legacy White Oak leadership.",
        ["WHITE OAK MANAGEMENT"],
    ),
    "AOM Healthcare": (
        "NY",
        "Not publicly identified",
        None,
        None,
        "AOM Healthcare LLC is a New York-based operator with 20+ affiliated skilled nursing and rehabilitation facilities across Ohio and New York. William Stocksdale serves as Division President. No centralized corporate website.",
        "NY-based ownership with OH operations is a common pattern for investor-backed operators; Division President Stocksdale is the operational contact for Ohio facilities.",
        ["AOM HEALTHCARE"],
    ),
    "Eldercare Partners": (
        "NY",
        "Michael Edery, Jay Miller, Raquel Edery (Partners)",
        None,
        "eldercarepartners.net",
        "Eldercare Partners is a real estate-driven operator led by three partners: Michael Edery and Jay Miller (each with 25+ years in commercial real estate) and Raquel Edery, MBA, LNHA. Specializes in acquisitions of skilled nursing, sub-acute rehabilitation, assisted living, and independent living facilities.",
        "CRE-first investor group acquiring healthcare facilities; Raquel Edery is the healthcare operations partner and most relevant BD contact.",
        ["ELDERCARE PARTNERS"],
    ),
    "Morning Pointe Senior Living": (
        "TN",
        "Franklin Farrow",
        "1997",
        "morningpointe.com",
        "Co-founded in 1997 by Greg Vital (President) and Franklin Farrow (CEO). Operates 41 communities across five southeastern states (TN, KY, GA, AL, IN) serving 2,000+ residents through Independent Healthcare Properties (IHP), LLC.",
        "Founder-led, growth-oriented AL/memory care operator actively expanding in the Southeast and into Indiana; both Vital and Farrow are accessible industry leaders.",
        ["MORNING POINTE SENIOR LIVING"],
    ),
    "Legacy Health Services": (
        "OH",
        "James Taylor",
        "1970",
        "lhshealth.com",
        "Legacy Health Services is a family-owned and operated post-acute care company based in Parma, Ohio, with a network of skilled nursing facilities across the state. Started over 50 years ago with one Cleveland facility.",
        "Established family-owned Ohio SNF operator; CEO James Taylor is the appropriate contact for partnership conversations.",
        ["LEGACY HEALTH SERVICES"],
    ),
    "Vancrest Health Care Centers": (
        "OH",
        "Mark White",
        "1960",
        "vancrest.com",
        "Founded in 1960 by Dr. E. E. White when he converted the former Van Wert County Hospital into one of Ohio's first geriatric hospitals. Now led by son Mark White (CEO). Operates 13 facilities in western Ohio. Acquired a Wyandot County facility in 2023 and broke ground on a new $18M facility.",
        "Second-generation family operator with active capital investment and expansion in western Ohio; Mark White is a direct decision-maker.",
        ["VANCREST HEALTH CARE CENTERS"],
    ),
    "Windsor House": (
        "OH",
        "John J. Masternick",
        "1959",
        "windsorhouseinc.com",
        "Founded in 1959 by John and Dorothy Masternick, Windsor House is a family-owned company operating 12 nursing homes and 5 assisted living communities in Northeast Ohio and Western Pennsylvania. Masternick family continues to lead operations.",
        "Long-standing family-owned operator in NE Ohio/Western PA; approach through Masternick family leadership for any engagement.",
        ["WINDSOR HOUSE, INC."],
    ),
    "Continuing Healthcare Solutions": (
        "OH",
        "Kevin Kauffman",
        "2011",
        "continuinghc.com",
        "Founded in 2011, CHS is led by CEO Kevin Kauffman with T. Scott Sprenger as President and Mark Sprenger as EVP/CIO. Sprenger family holds significant ownership alongside Michael Bunner, Christopher Mallett, and Benjamin Parsons. Operates 33+ properties in Ohio.",
        "Sprenger family connection to both CHS and Sprenger Healthcare means coordinated approach is essential; Kevin Kauffman is the operational CEO.",
        ["CONTINUING HEALTHCARE SOLUTIONS"],
    ),
    "Hillstone Healthcare": (
        "OH",
        "Paul Bergsten",
        "2010",
        "hillstonehealthcare.com",
        "Founded in 2010 by Paul Bergsten (30+ years of LTC experience, started working in nursing home kitchens at age 15). Operates 39 skilled nursing facilities with COO Matt Dapore. Lean corporate structure despite large portfolio.",
        "Large-scale SNF operator with hands-on founder-CEO; 39 facilities makes this a significant Ohio player -- Paul Bergsten is the direct relationship target.",
        ["HILLSTONE HEALTHCARE"],
    ),
    "Aperion Care": (
        "IL",
        "Lisa Ulbert / Yosef Meystel (ownership)",
        "2013",
        "aperioncare.com",
        "Founded in 2013, Aperion Care operates 18 skilled nursing facilities in Illinois and Indiana. Ownership traces to Joel Meystel, Yosef Meystel (Declaration of Trust), and the David A. Berkowitz Revocable Trust. Some facilities divested. Has faced regulatory scrutiny in Cook County.",
        "Complex trust-based ownership structure with some divestiture activity; approach carefully and verify current facility portfolio before engaging.",
        ["APERION CARE"],
    ),
    "Envive Healthcare": (
        "IN",
        "David C.",
        "2021",
        "envivehealthcare.com",
        "Started in July 2021 and quickly grew to 7+ skilled nursing communities across Indiana. COO Austin Steele joined shortly after founding. Positions itself as a 'newest crop' operator challenging the status quo in skilled nursing.",
        "Young, fast-growing Indiana operator with a disruptor mindset; small enough for meaningful partnership conversations but moving quickly on acquisitions.",
        ["ENVIVE HEALTHCARE"],
    ),
    "Ohio Living": (
        "OH",
        "Laurence C. Gumina",
        "1922",
        "ohioliving.org",
        "One of the largest not-for-profit, multi-site senior living organizations in the nation (ranked 18th by LeadingAge Ziegler). Founded in 1922, CEO Laurence Gumina has 30+ years in hospital and aging services and serves on boards of LeadingAge, LeadingAge Ohio, Link-Age, and PAHSA.",
        "Nonprofit status means different decision-making dynamics (board-driven); Gumina is deeply connected in the industry and a valuable relationship for credibility and referrals.",
        ["OHIO LIVING COMMUNITIES"],
    ),
    "Priority Life Care": (
        "IN",
        "Sevy Petras",
        "2009",
        "prioritylc.com",
        "Founded at the Petras family Thanksgiving dinner in 2009. CEO and Co-Founder Sevy Petras leads this family-operated enterprise focused on affordable senior housing. Petras elected to the Argentum Board of Directors.",
        "Family-founded with a mission-driven affordable housing focus; Sevy Petras is accessible, well-connected (Argentum board), and the sole decision-maker.",
        ["PRIORITY LIFE CARE"],
    ),
    "CareCore Health": (
        "OH",
        "Chaim Hertanu",
        "2005",
        "carecorehealth.com",
        "CareCore Health operates 12 skilled nursing, rehabilitation, and long-term care facilities across Ohio. Founded in 2005, led by CEO Chaim Hertanu. Key facilities include CareCore at Margaret Hall, CareCore at Lakeridge, and CareCore at Meadows.",
        "Mid-size Cincinnati-area SNF operator; CEO Hertanu is the primary contact but the company maintains a low corporate profile.",
        ["CARECORE HEALTH"],
    ),
    "Optalis Health & Rehabilitation": (
        "MI",
        "Raj Patel",
        "2015",
        "optalishealthcare.com",
        "Founded in 2015, Optalis has grown aggressively through acquisitions to 35 facilities across Ohio and Michigan, having raised $247M in financing. Key acquisitions include Vrable Healthcare and 7 SKLD locations in Michigan.",
        "Aggressive, well-capitalized acquirer in the OH/MI corridor; Raj Patel runs a growth-first strategy and may be receptive to service partnerships that support rapid integration of acquired facilities.",
        ["OPTALIS HEALTH & REHABILITATION"],
    ),
    "Topaz Healthcare": (
        None,
        None,
        None,
        None,
        "Research did not identify a skilled nursing facility operator named 'Topaz Healthcare' with a multi-state presence. The name may refer to a local DBA, a subsidiary under a different parent name, or a recently formed entity. Requires further investigation via CMS ownership data or state licensure records.",
        "Requires further investigation; check CMS ownership data or state licensure records to confirm the operating entity behind this name.",
        ["TOPAZ HEALTHCARE"],
    ),
    "Trio Healthcare": (
        "OH",
        "David Rubenstein",
        "2016",
        "trio-healthcare.com",
        "Formed in 2016, Trio Healthcare operates 21 senior care facilities: 12 skilled nursing/rehabilitation and assisted living centers in Virginia and 9 in Ohio. Co-Founder and Chief Clinical Officer Melissa Green provides clinical leadership. Has adopted analytics tools (Saiva AI) for rehospitalization prevention.",
        "Mid-size operator spanning OH and VA with a data-driven clinical approach; CEO Rubenstein and CCO Green are both accessible for partnership conversations.",
        ["TRIO HEALTHCARE"],
    ),
    # ── MUO Profile extractions ──────────────────────────────────────────
    "Arbors at Ohio": (
        "KY",
        "Mark Stern (CEO, Prestige Healthcare)",
        "2002",
        "arborsofohio.com",
        "Prestige Healthcare parent company. Trust-based ownership model with Kentucky headquarters. Operates skilled nursing facilities in Ohio under the Arbors brand.",
        "Trust-based ownership; engage through Prestige Healthcare parent and CEO Mark Stern for enterprise-level conversations.",
        ["ARBORS", "ARBORS AT OHIO"],
    ),
    "Castle Healthcare": (
        "IN",
        "Shai Berdugo",
        "2020",
        "castlehcc.com",
        "Indiana-based operator founded in 2020 with an anti-corporate culture philosophy. Led by CEO Shai Berdugo. Focused on differentiated operational approach in skilled nursing.",
        "Young operator with anti-corporate positioning; may be receptive to partnerships that align with their independent, facility-first culture.",
        ["CASTLE HEALTHCARE"],
    ),
    "Southern Healthcare Management": (
        "FL",
        "Mark Cronquist",
        "2003",
        "southernltc.com",
        "Florida-based operator managing 43 skilled nursing facilities across Florida, North Carolina, and Georgia. Founded in 2003 and led by CEO Mark Cronquist. Significant southeastern footprint.",
        "Large southeastern operator with 43 facilities across FL/NC/GA; CEO Cronquist is the primary contact for partnership conversations.",
        ["SOUTHERN HEALTHCARE MANAGEMENT, LLC"],
    ),
    "Lutheran Services Carolinas": (
        "NC",
        "Ted W. Goins Jr.",
        "1960",
        "lscarolinas.net",
        "ELCA nonprofit ministry founded in 1960, based in North Carolina. Led by President & CEO Ted W. Goins Jr. Faith-based senior living and services organization.",
        "Nonprofit faith-based organization; board-driven decision-making similar to Ohio Living. Long institutional history provides stability but may have slower procurement cycles.",
        # Note: no explicit DB name provided for this entity — check if it exists
        # Not in the T2 list provided, skip
    ),
    "Gardant Management Solutions": (
        "IL",
        "ESOP-owned (no individual CEO)",
        None,
        None,
        "Illinois-based ESOP-owned operator managing approximately 100 assisted living and memory care communities. Ranked 5th largest AL/MC operator nationally. Employee-ownership structure similar to Miller's Merry Manor.",
        "ESOP-owned like Miller's Merry Manor; no single owner to approach for acquisition. Partnership and service contracts are the appropriate engagement model. Scale (100 communities) makes this a significant AL/MC player.",
        ["GARDANT MANAGEMENT SOLUTIONS", "GARDANT MANAGEMENT SOLUTIONS, INC"],
    ),
    "Retirement Unlimited": (
        "VA",
        "Fralin/Waldron families",
        "1982",
        None,
        "Virginia-based senior living operator owned by the Fralin and Waldron families since 1982. Completed acquisition of Brandywine Living portfolio in December 2023, significantly expanding footprint.",
        "Family-owned with demonstrated M&A appetite (Brandywine acquisition Dec 2023); growth trajectory suggests openness to strategic partnerships.",
        ["Retirement Unlimited, Inc."],
    ),
    "Triple Crown Senior Living": (
        "KY",
        "Todd Marsh",
        "2017",
        None,
        "Kentucky-based senior living operator founded in 2017 by CEO Todd Marsh. Named Louisville Fast 50 #1 fastest-growing company. Rapid growth trajectory in the senior living space.",
        "Fast-growing Kentucky operator with strong momentum (Louisville Fast 50 #1); CEO Todd Marsh is the key decision-maker.",
        ["Triple Crown Senior Living"],
    ),
    "Vitality Living": (
        "TN",
        "Chris Guay",
        None,
        None,
        "Tennessee-based senior living operator led by CEO Chris Guay. Active southeastern acquirer with a growth-oriented strategy in assisted living and memory care.",
        "Active southeastern acquirer; CEO Chris Guay is the primary contact. Growth strategy may create opportunities for service partnerships during integration phases.",
        # Not in the T2 DB name list provided — skip
    ),
}


def run():
    total_updated = 0
    total_rows_affected = 0
    skipped = []
    errors = []

    for operator, data in NARRATIVES.items():
        hq_state, ceo, founded, website, key_insight, recommendation = data[:6]
        db_names = data[6] if len(data) > 6 else []

        if not db_names:
            skipped.append(f"{operator} (no DB name mapping)")
            continue

        for db_name in db_names:
            try:
                sql = """
                    UPDATE bd.market_intel_corporate_entities
                    SET hq_state = %s,
                        ceo = %s,
                        founded = %s,
                        website = %s,
                        key_insight = %s,
                        recommendation = %s
                    WHERE corporate_name = %s
                      AND bd_tier IS NOT NULL
                """
                params = (
                    hq_state,
                    ceo,
                    founded,
                    website,
                    key_insight,
                    recommendation,
                    db_name,
                )
                result = pg.write(sql, f"Update {db_name}", params=params)
                rows = result[0].get("rowsAffected", 0) if result else 0
                total_rows_affected += rows

                if rows > 0:
                    total_updated += 1
                    print(f"  [OK] {db_name} -> {rows} row(s) updated")
                else:
                    print(f"  [--] {db_name} -> 0 rows (no match or bd_tier IS NULL)")

            except Exception as e:
                errors.append(f"{db_name}: {e}")
                print(f"  [ERR] {db_name} -> {e}")

    # ── Summary ──────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total DB name variants processed: {sum(len(d[6]) for d in NARRATIVES.values() if len(d) > 6)}")
    print(f"Successful updates:               {total_updated}")
    print(f"Total rows affected:              {total_rows_affected}")

    if skipped:
        print(f"\nSkipped ({len(skipped)}):")
        for s in skipped:
            print(f"  - {s}")

    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
    else:
        print("\nNo errors.")


if __name__ == "__main__":
    run()
