"""Load remaining T1 corporate intel narratives into PostgreSQL."""
import sys
sys.path.insert(0, 'C:/Users/ratwood/keystone-platform/backend')
from app.services.shared.pg_client import PgClient

pg = PgClient()

updates = [
    # --- From existing MUO Profiles ---
    {
        'name': 'LIBERTY',
        'hq_state': 'NC',
        'ceo': 'Will Purvis (President)',
        'founded': '1990',
        'website': 'liberty-healthcare.com',
        'key_insight': (
            "Founded by the McNeill family, whose roots trace to an 1875 Whiteville, NC pharmacy. "
            "Sandy & Ronnie McNeill (4th generation) purchased their first nursing home in 1990 and "
            "named it 'Liberty' after their father's WWII Naval service. Private, family-owned with "
            "no PE or REIT involvement. Vertically integrated across SNF, AL, IL, home care, hospice, "
            "pharmacy, medical equipment, and a proprietary Medicare Advantage I-SNP/C-SNP plan "
            "(Liberty Advantage). Aggressive M&A since mid-2025: acquired The Carlisle Palm Beach (FL), "
            "took ownership of Preserve at Fairfield Glade (TN), and broke ground on Peninsula of "
            "Charleston (SC CCRC) under new 'Inspire by Liberty' brand. Created COO and CIO roles in 2025."
        ),
        'recommendation': (
            "Pursue 11 MH-only facilities for PCP integration cross-sell ($2.3M) and prioritize "
            "46 unserved facilities ($18.3M) in Charlotte, Wilmington, and Winston-Salem metro clusters. "
            "Engage President Will Purvis and new COO Bob Goyette; the Liberty Advantage I-SNP alignment "
            "with Eventus clinical model is the strongest corporate hook."
        ),
    },
    {
        'name': 'BROOKDALE SENIOR LIVING',
        'hq_state': 'TN',
        'ceo': 'Nick Stengle (CEO, appointed Oct 2025)',
        'founded': '1978',
        'website': 'brookdale.com',
        'key_insight': (
            "Largest senior living operator in the United States. Publicly traded (NYSE: BKD), "
            "~$3.2B annual revenue, 584 communities across 41 states. Full leadership overhaul in 2025: "
            "Nick Stengle appointed CEO (Oct 2025, ex-Gentiva President, ex-Sunrise EVP/COO) and "
            "Mary Sue Patchett named first COO in a decade (Dec 2025) with a new 6-region operating "
            "structure. Actively shrinking portfolio from 645 to ~550 communities by mid-2026 while "
            "shifting to 70%+ owned. Closed $300M Welltower JV (Dec 2024). HealthPlus preventive care "
            "program shows 78% fewer urgent care visits, 36% fewer hospitalizations."
        ),
        'recommendation': (
            "Retention and integration play, not growth -- 84% penetration with only $2.0M total "
            "opportunity. Monitor which communities are divested in the portfolio optimization. "
            "Engage new CEO Stengle and COO Patchett; the 6-region restructuring will change contacts."
        ),
    },
    {
        'name': 'SABER HEALTHCARE GROUP',
        'hq_state': 'OH',
        'ceo': 'William A. Weisberg (Founder, Chairman & CEO)',
        'founded': '2001',
        'website': 'saberhealth.com',
        'key_insight': (
            "Founded in 2001 by William A. Weisberg with two SNFs in Cleveland. Remains family-controlled "
            "-- Michael A. Weisberg (President/COO) and Nancy G. Weisberg (EVP). Now ~143 facilities "
            "(130 SNF, 13 ALF) across OH, PA, VA, NC, IN, DE with 15,000+ employees. Institutional "
            "capital arrived late 2025: Omega Healthcare Investors (NYSE: OHI) invested ~$315M total -- "
            "$222M JV for 49% equity in 64 facilities (Oct 2025), plus $93M for 9.9% equity in Saber "
            "Holdings (Jan 2026). Acquired 4 PA SNFs (645 beds, Dec 2025). Strategic partnership with "
            "Medrina, nation's largest physiatry group (Jan 2025). Regulatory risk: $16M+ cumulative "
            "fines, $10M False Claims Act settlement, active Corporate Integrity Agreement with HHS-OIG."
        ),
        'recommendation': (
            "Highest-value opportunity at $30.8M total potential (48% penetration). Prioritize unserved "
            "OH, PA, NC facilities ($22.9M) and integration cross-sell at 58 served ($7.8M). "
            "Target Weisberg family directly; Medrina partnership and Omega REIT alignment are natural "
            "conversation starters for clinical value positioning."
        ),
    },
    {
        'name': 'SABER HEALTHCARE',
        'hq_state': 'OH',
        'ceo': 'William A. Weisberg (Founder, Chairman & CEO)',
        'founded': '2001',
        'website': 'saberhealth.com',
        'key_insight': 'Founded 2001 by Weisberg family in Cleveland. ~143 facilities across 6 states. Omega Healthcare (OHI) invested $315M in 2025-2026. Active Corporate Integrity Agreement.',
        'recommendation': '$30.8M total potential. Target unserved OH/PA/NC facilities.',
    },
    {
        'name': 'PRUITT HEALTH',
        'hq_state': 'GA',
        'ceo': 'Neil L. Pruitt, Jr. (Chairman & CEO)',
        'founded': '1969',
        'website': 'pruitthealth.com',
        'key_insight': (
            "Founded in 1969 by Neil Pruitt, Sr. Second-generation Neil L. Pruitt, Jr. (Chairman & CEO "
            "since 2002) won the 2024 AHCA Mary K. Ousley Champion of Quality award -- the industry's "
            "top individual honor. Private, family-owned, no PE. ~$1.9B revenue, 180+ locations across "
            "GA, NC, SC, FL, TN, MD. Rebranded from UHS-Pruitt to PruittHealth (2023). Vertically "
            "integrated: SNF, home health, hospice, pharmacy (Advantage Rx), home infusion, medical "
            "supply, AL (PruittPlace). Aggressive Southeast M&A: $385M Raleigh project, $117M+ "
            "construction pipeline across TN/NC/SC/GA. Technology-forward with custom Accenture/Microsoft "
            "platform for integrated post-acute care."
        ),
        'recommendation': (
            "Deepen integration at 12 served facilities ($4.0M) and pursue 15 unserved ($6.2M), "
            "particularly NC where PruittHealth is investing heavily ($385M Raleigh). CEO Pruitt's "
            "quality-first orientation and vertical integration make him a natural Eventus partner."
        ),
    },
    {
        'name': 'PRUITTHEALTH',
        'hq_state': 'GA',
        'ceo': 'Neil L. Pruitt, Jr. (Chairman & CEO)',
        'founded': '1969',
        'website': 'pruitthealth.com',
        'key_insight': 'Founded 1969, second-generation family leadership. 2024 AHCA Champion of Quality. $1.9B revenue, 180+ locations. $385M Raleigh project. Vertically integrated (pharmacy, home health, hospice).',
        'recommendation': 'Quality-first CEO, natural Eventus partner. Target NC expansion corridor.',
    },
    {
        'name': 'LIONSTONE CARE',
        'hq_state': 'OH',
        'ceo': 'Adam Cusner, PhD, LNHA (CEO)',
        'founded': '2017',
        'website': 'lionstonecare.com',
        'key_insight': (
            "Founded circa 2017 by Aari Kazarnovsky (Managing Partner). Private, owner-operated Ohio "
            "SNF platform. Tripled scale via $230M acquisition in July 2025 (with Complete Care Amegreen, "
            "financed by Dwight Mortgage Trust), absorbing a 19-property Ohio SNF/AL portfolio. Expanding "
            "into NJ with $31.1M AL/MC facility (110 units). COO Jeffrey Degyansky brings deep Ohio SNF "
            "experience (ex-CommuniCare, Embassy, Saber). CEO Cusner is an IO psychologist by training. "
            "Developing in-house IV therapy program."
        ),
        'recommendation': (
            "Target 16 unserved facilities ($3.9M) -- many are newly acquired properties needing clinical "
            "partners. IV therapy program is a specific clinical hook. Engage COO Degyansky (knows the "
            "Eventus model from Saber/CommuniCare)."
        ),
    },
    # --- From web research ---
    {
        'name': 'INFINITY HEALTHCARE CONSULTING',
        'hq_state': 'IL',
        'ceo': 'Michael Blisko (CEO)',
        'founded': '2003',
        'website': 'infinityhealthcare.com',
        'key_insight': (
            "Founded in 2003 by Michael Blisko in Illinois. Operates 42 owned facilities plus consulting "
            "for 80+ additional across 6 states (IL, IN, OH, KY, WI, MI). I-SNP joint venture with "
            "Longevity Health signals value-based care orientation. Private, no PE."
        ),
        'recommendation': 'Explore I-SNP alignment angle similar to ASC/Liberty. Target IN/OH owned facilities.',
    },
    {
        'name': 'PACS GROUP',
        'hq_state': 'UT',
        'ceo': 'Jason Murray (CEO)',
        'founded': '2013',
        'website': 'pacsgroup.com',
        'key_insight': (
            "Founded 2013, IPO'd April 2024 (NYSE: PACS). 323 facilities in 17 states, one of the "
            "largest US post-acute platforms. Rapid growth through acquisitions. Hindenburg Research "
            "published a short report in late 2024 alleging billing irregularities -- a material risk "
            "flag. Utah-based with West Coast concentration expanding eastward."
        ),
        'recommendation': 'Large whitespace but monitor Hindenburg/regulatory risk before major BD investment.',
    },
    {
        'name': 'NATIONAL HEALTHCARE CORPORATION',
        'hq_state': 'TN',
        'ceo': 'Dr. Stephen F. Flatt (CEO)',
        'founded': '1971',
        'website': 'nhccare.com',
        'key_insight': (
            "Founded in 1971 by Dr. Carl Adams in Murfreesboro, TN. Publicly traded (NYSE American: NHC). "
            "$1.7-2.5B market cap. Operates 75 SNFs + 25 ALs + homecare and hospice across southeastern US. "
            "Acquired White Oak Management portfolio in 2024. Conservative, quality-focused operator with "
            "over 50 years of continuous family-influenced leadership."
        ),
        'recommendation': 'Established multi-state SNF operator. Target unserved KY/SC/VA facilities for expansion.',
    },
    {
        'name': 'BRICKYARD HEALTHCARE',
        'hq_state': 'IN',
        'ceo': 'Wesley Rogers (CEO)',
        'founded': '1963',
        'website': 'brickyardhealthcare.com',
        'key_insight': (
            "Heritage traces to Golden Living (1963). Rebranded to Brickyard Healthcare in 2022 under "
            "PE backing (Fillmore Capital Partners / Pearl Senior Care). 23 SNFs, all Indiana. Building "
            "a major I-SNP program. CEO Wesley Rogers leads the turnaround-to-growth transformation."
        ),
        'recommendation': 'Indiana-only, PE-backed. I-SNP development creates clinical alignment opportunity.',
    },
    {
        'name': 'OTTERBEIN SENIOR LIFE',
        'hq_state': 'OH',
        'ceo': 'Jill Wilson (CEO)',
        'founded': '1912',
        'website': 'otterbein.org',
        'key_insight': (
            "Nonprofit senior living community founded in 1912 with United Methodist roots. Full "
            "continuum (IL, AL, MC, SNF, home health) across Ohio and Indiana. Vista Grande affiliation "
            "pending. CEO Jill Wilson leads with mission-driven, quality-first orientation. Over 110 "
            "years of continuous operation."
        ),
        'recommendation': 'Mission-aligned nonprofit. Engage on quality and outcomes positioning.',
    },
    {
        'name': 'CIENA HEALTHCARE/LAUREL HEALTH CARE',
        'hq_state': 'MI',
        'ceo': 'David Parker (CEO, appointed Dec 2024)',
        'founded': '2007',
        'website': 'cienahealthcare.com',
        'key_insight': (
            "Founded by Mohammad Qazi. 84 facilities across 5 states (MI, OH, PA, IN, WI). Laurel "
            "Health Care acquisition doubled the footprint. New CEO David Parker appointed December 2024. "
            "Michigan-heavy portfolio with Ohio expansion. Private, founder-owned."
        ),
        'recommendation': 'New CEO creates engagement window. Target OH facilities in footprint.',
    },
    {
        'name': 'CCH HEALTHCARE',
        'hq_state': 'NJ',
        'ceo': 'Jacob Stern (CEO)',
        'founded': None,
        'website': None,
        'key_insight': (
            "Lakewood, NJ-based operator with 38 facilities in OH, NC, and TN. Low public profile with "
            "undisclosed ownership structure. CEO Jacob Stern. Focused on SNF operations in the Southeast "
            "and Midwest."
        ),
        'recommendation': 'Limited public intel. Facility-level engagement may be more productive than corporate.',
    },
    {
        'name': 'TLC MANAGEMENT',
        'hq_state': 'IN',
        'ceo': 'Gary Kolbeck (CEO)',
        'founded': '1987',
        'website': 'tlcmgmt.com',
        'key_insight': (
            "Family-owned management company since 1987, based in Marion, IN. Pure management model -- "
            "does not own facilities. Primarily Indiana SNFs. CEO Gary Kolbeck. Conservative, "
            "relationship-driven operator."
        ),
        'recommendation': 'Management company model means facility owners hold decision authority. Engage at facility level.',
    },
    {
        'name': 'PRINCIPLE',
        'hq_state': 'NC',
        'ceo': 'Lynn Hood (CEO)',
        'founded': '1980',
        'website': 'principleltc.com',
        'key_insight': (
            "Founded 1980 in Snow Hill, NC. CEO Lynn Hood won McKnight's Lifetime Achievement Award "
            "(2024). 45 facilities across NC, KY, VA. Sold a 7-facility portfolio in October 2025, "
            "signaling possible strategic contraction. Private, long-tenured leadership."
        ),
        'recommendation': 'Monitor portfolio moves -- the Oct 2025 divestiture may signal more. Hood is highly respected in the industry.',
    },
    {
        'name': 'PRINCIPLE LONG TERM CARE',
        'hq_state': 'NC',
        'ceo': 'Lynn Hood (CEO)',
        'founded': '1980',
        'website': 'principleltc.com',
        'key_insight': 'Founded 1980 in Snow Hill, NC. CEO Lynn Hood (McKnight Lifetime Achievement 2024). 45 facilities in NC/KY/VA. Sold 7-facility portfolio Oct 2025.',
        'recommendation': 'Monitor portfolio moves. Hood is highly respected in industry.',
    },
    {
        'name': 'AVARDIS',
        'hq_state': 'GA',
        'ceo': 'Tiffany Hoback (CEO)',
        'founded': '2025',
        'website': 'avardishealth.com',
        'key_insight': (
            "Emerged from LaVie Care Centers/Consulate Health Care bankruptcy in June 2025. ~43 "
            "facilities across 5 states. Carries significant reputational and regulatory baggage from "
            "Consulate's $258M DOJ False Claims Act settlement (2018) -- the largest nursing home fraud "
            "case in US history at the time. CEO Tiffany Hoback leads the post-bankruptcy rebuild. "
            "Previously operated as Independence Living Centers, Nspire Healthcare, and Raydiant Health Care."
        ),
        'recommendation': 'Post-bankruptcy operator with regulatory history. Approach cautiously. Monitor for stability before major BD investment.',
    },
    {
        'name': 'SUNRISE',
        'hq_state': 'VA',
        'ceo': 'Jack Callison (CEO)',
        'founded': '1981',
        'website': 'sunriseseniorliving.com',
        'key_insight': (
            "Founded in 1981 by Paul Klaassen in Fairfax, VA. One of the largest AL/MC operators "
            "globally with 270+ communities across US, Canada, and UK. Owned by Revera Inc., which is "
            "backed by the Public Sector Pension Investment Board (PSP, Canadian pension fund). In active "
            "growth mode with new community openings. Premium positioning in the AL/MC market."
        ),
        'recommendation': 'Major national AL operator. No SNFs -- limited clinical integration opportunity but significant AL footprint in our markets.',
    },
    {
        'name': 'Sunrise Senior Living',
        'hq_state': 'VA',
        'ceo': 'Jack Callison (CEO)',
        'founded': '1981',
        'website': 'sunriseseniorliving.com',
        'key_insight': 'Founded 1981 by Paul Klaassen. 270+ communities. Owned by Revera/Canadian PSP pension fund. Premium AL/MC positioning.',
        'recommendation': 'No SNFs. AL footprint in our markets but limited clinical integration opportunity.',
    },
]

count = 0
for u in updates:
    r = pg.write(
        sql="""UPDATE bd.market_intel_corporate_entities SET
            hq_state=%s, ceo=%s, founded=%s, website=%s, key_insight=%s, recommendation=%s
            WHERE corporate_name=%s AND bd_tier IS NOT NULL""",
        title=f"narrative {u['name']}",
        params=(u['hq_state'], u['ceo'], u['founded'], u['website'],
                u['key_insight'], u['recommendation'], u['name']),
    )
    affected = r[0].get('rowsAffected', 0) if r else 0
    status = 'OK' if affected > 0 else 'MISS'
    print(f"  {status} | {u['name']}")
    count += affected

# Also handle the Consulate/Nspire variant
for variant in ['CONSULATE HEALTH CARE/INDEPENDENCE LIVING CENTERS/NSPIRE HEALTHCARE/RAYDIANT HEALTH CARE']:
    r = pg.write(
        sql="""UPDATE bd.market_intel_corporate_entities SET
            hq_state=%s, ceo=%s, founded=%s, website=%s, key_insight=%s, recommendation=%s
            WHERE corporate_name=%s AND bd_tier IS NOT NULL""",
        title=f"narrative {variant}",
        params=('GA', 'Tiffany Hoback (CEO)', '2025', 'avardishealth.com',
                'Rebranded as Avardis Health (June 2025) after LaVie/Consulate bankruptcy. $258M DOJ settlement history.',
                'Post-bankruptcy. Monitor for stability.',
                variant),
    )
    affected = r[0].get('rowsAffected', 0) if r else 0
    print(f"  {'OK' if affected else 'MISS'} | {variant}")
    count += affected

print(f"\n{count} rows updated")
