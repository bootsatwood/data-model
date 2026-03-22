"""
Load T3 and T5 corporate intel narratives into bd.market_intel_corporate_entities.

Updates hq_state, ceo, founded, website, key_insight, recommendation
for all Tier 3 and Tier 5 entities using parameterized queries.

Source: corporate_intel_t3_t5_profiles.md (2026-03-22)
"""

import sys
import os
from dotenv import load_dotenv

# Load backend .env so PG_PASSWORD (and other PG_* vars) are available
load_dotenv('C:/Users/ratwood/keystone-platform/backend/.env')

sys.path.insert(0, 'C:/Users/ratwood/keystone-platform/backend')
from app.services.shared.pg_client import PgClient

pg = PgClient()

# ── Narrative data keyed by canonical operator name ──────────────────────
# Each entry: (hq_state, ceo, founded, website, key_insight, recommendation, [db_names])

NARRATIVES = {
    # ═══════════════════════════════════════════════════════════════════════
    # TIER 3 ENTITIES
    # ═══════════════════════════════════════════════════════════════════════
    "Progressive Quality Care": (
        "OH",
        "Eitan Flank",
        "~1960s",
        "progressivequalitycare.com",
        "Family-owned SNF operator in the Cleveland/Akron corridor of Ohio with roots dating to the 1960s. Operates ~16 facilities branded under the 'Avenue' name across OH and MI, offering skilled nursing, short-term rehab, and long-term care. Mid-size regional operator with 500-1,000 employees.",
        "Regional Ohio operator with moderate footprint; worth relationship-building as a mid-tier target given geographic density in northeast OH.",
        ["PROGRESSIVE QUALITY CARE"],
    ),
    "SEKY Holding Co.": (
        "KY",
        "Terry Forcht (parent company founder/chairman)",
        "1972",
        "forchtgroup.com",
        "Nursing home management arm of the Forcht Group of Kentucky, a diversified conglomerate spanning banking (Forcht Bank, 26 locations, $1.2B+ assets), broadcasting, insurance, and healthcare. Operates 9 facilities in southeast KY. Has faced staffing-related lawsuits.",
        "Nursing homes are a small piece of a diversified KY conglomerate; decision-making likely centralized with Forcht Group leadership. Low strategic priority unless pursuing southeast KY market specifically.",
        ["SEKY HOLDING CO."],
    ),
    "Crown Healthcare Group": (
        "OH",
        "Kevin Daubenmire",
        "~2017",
        "chcgrp.com",
        "Relatively young, family-owned SNF operator founded ~2017-2018 that has grown quickly through acquisitions. Operates nine SNFs in Ohio with presence across five states. Great Place to Work certified with a 'hometown care' model.",
        "Young, acquisition-minded operator expanding in OH; the growth trajectory and deal-making posture make them a potentially receptive BD target. Worth engaging Kevin Daubenmire directly.",
        ["CROWN HEALTHCARE GROUP"],
    ),
    "JAG Healthcare": (
        "OH",
        "James Griffiths (founder)",
        "2005",
        "jaghealthcare.com",
        "Ohio-based SNF operator founded in 2005, specializing in smaller-community facilities with fewer than 200 beds. Known for hands-on management and turnaround capability. Secured $14.5M in Oxford Finance financing to acquire six SNFs in Ohio. ~1,000 employees.",
        "Small but acquisitive Ohio operator focused on turnaround plays in rural/small-community SNFs; worth cultivating as they scale up and need more clinical services.",
        ["JAG HEALTHCARE"],
    ),
    "Vitality Living": (
        "TN",
        "Chris Guay (Founder, CEO)",
        "2016",
        "vitalityseniorliving.com",
        "Founded in 2016 by Chris Guay, former senior executive at Brookdale and Emeritus. Focuses on mid-to-high-end AL and memory care, grown to 35+ communities across TN, GA, FL, KY, AL, LA, TX, and VA. Merged with Traditions Senior Living in 2024.",
        "Confirmed existing intel. Fast-growing, well-led AL/MC operator in our geographic footprint; high priority given southeastern focus and experienced leadership team.",
        ["VITALITY LIVING"],
    ),
    "Health Care Management Group": (
        "OH",
        "Steve Boymel (transitioned to Lionstone Health Care)",
        "1984",
        "hcmg.com",
        "Locally owned operator of seven nursing care and rehab facilities in Greater Cincinnati/Northern KY, founded in 1984. Reports 94% patient satisfaction. After 31 years, ownership transitioned to Lionstone Health Care, changing the decision-making landscape.",
        "Small, quality-focused Cincinnati/NKY operator recently acquired by Lionstone Health Care. The ownership transition is a potential opening; identify the new Lionstone decision-makers and re-engage.",
        ["HEALTH CARE MANAGEMENT GROUP"],
    ),
    "Divine Healthcare Management": (
        "OH",
        "Not confirmed (multi-stakeholder: Markovits, Richland, Arem, Moskowitz, Herskowitz)",
        None,
        "divinesylvania.com",
        "Operates nine SNFs across OH and WI, headquartered in Sylvania, OH (Toledo suburb). Ownership split among five private stakeholders. Limited public presence; small, privately held operator with a low profile.",
        "Small, fragmented-ownership operator in OH/WI with limited public presence. Low priority unless targeting the Toledo/northwest OH corridor specifically.",
        ["DIVINE HEALTHCARE MANAGEMENT"],
    ),

    # ═══════════════════════════════════════════════════════════════════════
    # TIER 5 ENTITIES
    # ═══════════════════════════════════════════════════════════════════════
    "Aventura Health Group": (
        "PA",
        "Mark Kaszirer (COO)",
        None,
        "aventurahg.com",
        "PA-based operator of SNFs across multiple states including OH and PA. Faced significant regulatory challenges: CMS terminated the Medicare/Medicaid provider agreement for Aventura at Terrace View in 2025, forcing relocation of 111 residents. Low CMS chain rating. Barrier: Recent LOB.",
        "Avoid. Regulatory risk and recent Medicare termination signal operational instability. Not a reliable long-term partner.",
        ["AVENTURA"],
    ),
    "Bluegrass / Encore": (
        "KY",
        None,
        None,
        None,
        "Combined relationship between Bluegrass Health KY (15 facilities) and Encore Health Partners (12 facilities), sharing ownership/management ties across ~27 KY nursing homes. Encore acquired Evergreen (Louisville-based rehab/therapy provider), giving it in-house therapy capability. Barrier: Alliance (Evergreen therapy acquisition).",
        "Large KY footprint but locked into existing therapy alliance through Encore's Evergreen acquisition. Displacing the incumbent would require compelling clinical differentiation. Monitor for contract renewal windows.",
        ["BLUEGRASS/ENCORE", "Encore Senior Living"],
    ),
    "CarDon & Associates": (
        "IN",
        "Moore family (Carroll & Donna Moore, founders)",
        "1977",
        "cardon.us",
        "Family-owned Indiana senior living operator founded in 1977 with 45+ years of experience. Operates 20 communities across 11 IN counties. Newsweek's 2026 America's Best Nursing Homes. 91% own-provider-group barrier means nearly all clinical services are in-house.",
        "Extremely difficult to penetrate. Family-owned with 91% in-house clinical staffing and nearly 50 years of operational self-sufficiency. Only viable angle would be a niche specialty service they do not currently offer in-house.",
        ["CARDON & ASSOCIATES"],
    ),
    "ClearView Healthcare Management": (
        "KY",
        "Mick Vujanovic",
        None,
        "clearviewhcmgmt.com",
        "Louisville-based operator of SNFs across KY and TN, ~88 employees, $8.4M annual revenue. Locally operated, hands-on approach. Dual barrier: 38% in-house clinical staffing plus existing alliance with a competing provider.",
        "Mixed barrier. The 38% own-provider figure means 62% of facilities could theoretically be open to a new clinical partner. Worth exploring the alliance contract terms and whether there is dissatisfaction with the current provider. Louisville HQ is accessible geography.",
        ["CLEARVIEW"],
    ),
    "CommuniCare Health Services": (
        "OH",
        "Stephen L. Rosedale (Founder)",
        "1984",
        "communicarehealth.com",
        "One of the nation's largest family-owned post-acute care providers, founded in 1984 by Vietnam War veteran Stephen Rosedale. Grown to 150+ locations across seven states. Also owns CommuniCare Advantage health plan, making it a fully integrated operator-payer-provider system.",
        "Fortress account. Fully vertically integrated with their own health plan, clinical staff, and 150+ facilities. Not a realistic target for external clinical services. Track for market intelligence only.",
        ["COMMUNICARE"],
    ),
    "Eastern Healthcare Group": (
        "NJ",
        "Not confirmed (Ydi Irrevocable Trust, 90%+ stake)",
        None,
        "ehg.care",
        "NJ-based operator managing 17 SNFs exclusively in VA, acquired from Portopiccolo Group in 2023. Among the lowest CMS chain ratings nationally (1.4/5 stars, bottom ~3%). After Twin Lakes sale, 911 calls spiked 70% and staffing dropped. Barrier: Termination Risk (100%).",
        "Avoid entirely. Severe quality and regulatory problems across the full portfolio. Any partnership would carry reputational and compliance risk. These facilities may change hands again.",
        ["EASTERN HEALTHCARE GROUP"],
    ),
    "Exceptional Living Centers": (
        "KY",
        "Tom Watts",
        "~2000",
        "exceptionallivingcenters.com",
        "Lexington, KY-based operator (Medical Rehabilitation Centers LLC) with 25 years of experience across seven states. Led by CEO Tom Watts (former Fifth Third Bank wealth management exec). ~$438M annual revenue. In-house clinical staffing model.",
        "Large, established multi-state operator with significant revenue. The in-house clinical model is entrenched, but scale means even a small service gap could represent meaningful volume. Worth a targeted approach on specialty services not covered internally.",
        ["EXCEPTIONAL LIVING CENTERS"],
    ),
    "Hill Valley Healthcare": (
        "NY",
        "Shimmy Idels & Steven Schwartz (Co-CEOs)",
        "2018",
        "hillvalleyhc.com",
        "NY-based SNF operator founded 2018 by Shimmy Idels and Steven Schwartz, positioning as a 'boutique' skilled nursing company. Grown rapidly to 39 facilities across six states through aggressive acquisitions including a $35.25M Ziegler-financed deal. Barrier: Own provider group.",
        "Fast-growing, acquisition-heavy operator. Rapid expansion may outpace internal staffing ability, creating openings. Focus on newly acquired facilities that may not yet have established in-house teams. Virginia footprint is notable.",
        ["Hill Valley"],
    ),
    "MFA / Medical Facilities of America": (
        "VA",
        "William Fralin",
        "1972",
        "mfa.net",
        "Dominant regional SNF operator in VA and NC, founded 1972, headquartered in Roanoke. Operates 39 centers with 5,000-10,000 employees, largest nursing home operator in Virginia. MFA Maryville RE LLC is a real estate holding entity within the MFA family. Barrier: Alliance (VA).",
        "Dominant Virginia operator with 50+ year history. Alliance barrier means incumbent clinical provider exists, but scale means even winning a portion would be significant. Requires high-level relationship approach to Fralin's leadership team.",
        ["MFA", "MFA MARYVILLE RE LLC"],
    ),
    "Pavilion Healthcare / Northwood": (
        "NY",
        "Eli Leshkowitz (managerial control)",
        None,
        "pavilionhealthcare.com",
        "Operates under Northwood Healthcare Group umbrella with facilities in OH, PA, and KY (The Pavilion at Kenton). Ownership involves multiple trusts/LLCs controlled by Eli Leshkowitz and associates. Dual barrier: 29% in-house clinical staffing plus existing alliance.",
        "The 29% own-provider figure means 71% of facilities use an external partner. Most penetrable of the dual-barrier T5 entities. Identify current alliance partner and assess competitive proposal viability. KY presence at Kenton is a geographic fit.",
        ["PAVILION HEALTHCARE"],
    ),
    "Signature HealthCARE": (
        "KY",
        "E. Joseph Steier III (Co-Founder)",
        "2007",
        "ltcrevolution.com",
        "One of the largest family-owned LTC operators nationally, founded 2007 by Joe Steier. 125 locations across 11 states, 18,000 employees. McKnight's 2024 Pinnacle Thought Leader honoree, KY Entrepreneur Hall of Fame. Partners with KY Association of Health Care Facilities. Barrier: Own provider group.",
        "Major KY-based national operator with strong internal clinical infrastructure. Not a realistic target for full-service displacement, but scale and Steier's thought-leader positioning make them valuable for market intelligence and potential co-marketing or referral partnerships.",
        ["SIGNATURE HEALTH"],
    ),
    "Singh / Waltonwood Senior Living": (
        "MI",
        "Gurmale S. Grewal",
        "1973/1987",
        "singhweb.com",
        "Third-generation, family-owned MI real estate conglomerate operating the Waltonwood Senior Living brand (upscale IL/AL/MC). Founded 1973 with senior living since 1987. Also owns Oakland Home Care and Oakland Helping Hands home health agencies. Barrier: Own provider group + home health agencies.",
        "Vertically integrated with own home health agencies and premium AL/MC positioning. Own-provider barrier reinforced by home health ownership. Low probability target. Only worth exploring if they expand into markets lacking internal clinical infrastructure.",
        ["SINGH"],
    ),
    "Venza Care Management": (
        "NJ",
        "Susan Strauss (founder), Yisroel Herzka (90%+ owner)",
        "2021",
        "venzacare.com",
        "Young (2021), NJ-based nursing home operator that rapidly assembled a 20-facility portfolio across seven southeastern states (AL, DE, LA, MD, NC, SC, TN). CIBC Bank closed $70M in refinancing for two facilities. Barrier: Alliance.",
        "Young, capital-backed operator with southeastern footprint overlapping EWH markets (TN, NC, SC, AL). Alliance barrier exists but company is only 5 years old and may not have deeply entrenched relationships. Worth probing current alliance results. Strategically relevant geography.",
        ["VENZA CARE MANAGEMENT"],
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
