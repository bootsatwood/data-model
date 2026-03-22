"""Load T1 corporate intel narratives into PostgreSQL."""
import sys
sys.path.insert(0, 'C:/Users/ratwood/keystone-platform/backend')
from app.services.shared.pg_client import PgClient

pg = PgClient()

updates = [
    {
        'name': 'MAJESTIC CARE',
        'hq_state': 'IN',
        'ceo': 'Paul D. Pruitt (CEO)',
        'founded': '2018',
        'website': 'majesticcare.com',
        'key_insight': (
            'Founded in 2018 as an affiliate of Marx Development Group (NYC, David Marx founder/CEO, '
            '~$500M developed properties). MDG owns real estate while Majestic operates under an integrated '
            'owner-operator structure. Co-founder Bernie McGuinness departed May 2023 and launched rival operator '
            'Journey Healthcare (21 buildings by Nov 2024). CEO Paul Pruitt (27+ years LTC, ex-COO Mission Point) '
            'leads an aggressive acquisition spree: 6 Ohio SNFs from Certus Healthcare (Dec 2024), $60M acquisition '
            'of 4 West Virginia state-owned LTC facilities (Nov 2025), and $80M commitment to build 3 new WV facilities.'
        ),
        'recommendation': (
            'Top-scored entity (100). Prioritize PCP cross-sell at 15 MH-only served facilities for near-term '
            'integration revenue, then pursue Ohio whitespace (6 unserved, $3.2M) via corporate introduction '
            'referencing the established IN/KY relationship.'
        ),
    },
    {
        'name': 'AMERICAN SENIOR COMMUNITIES',
        'hq_state': 'IN',
        'ceo': 'Steve Van Camp (CEO)',
        'founded': '2000',
        'website': 'asccare.com',
        'key_insight': (
            "Indiana's largest senior care provider (#12 nationwide in SNF locations), founded by the Jackson "
            "family who entered the nursing home business in the 1960s. Ownership split: Jackson family and "
            "David Justice own the operating entity, while Health & Hospital Corporation of Marion County (HHC) "
            "owns significant physical facilities. In Jan 2025, ASC formed the largest provider-owned I-SNP "
            "network in the country as a JV with 5 other Indiana providers, launching in 18 counties and "
            "expanding to 43."
        ),
        'recommendation': (
            'Highest-revenue corporate relationship ($14.8M current) with $32.8M total potential. '
            'Engage CEO Van Camp and COO Andy Shane on I-SNP alignment -- value-based care models '
            'reward integrated clinical services.'
        ),
    },
    {
        'name': 'ALG',
        'hq_state': 'NC',
        'ceo': 'Charles E. Trefzger (Founder, President & CEO)',
        'founded': '1996',
        'website': 'algsenior.com',
        'key_insight': (
            'Founded in 1996 as Affinity Living Group by Charles Trefzger (Wake Forest Law, ex-Ernst & Whinney). '
            'Historically 150+ communities across 8 states, ranked 6th largest memory care and 8th largest AL by '
            'Argentum (2021), but contracted to ~63 active properties. Financial distress emerged 2024: Fannie Mae '
            'receivership after $28.3M loan default, and LTC Properties (NYSE: LTC) deferred $1.5M rent on 11 NC '
            'communities. LTC subsequently took majority ownership (53-93% stakes) of 17 ALG-operated NC/SC '
            'properties through JV conversion.'
        ),
        'recommendation': (
            'Retention-first account, not growth. We serve 100% of DB facilities ($7.36M current). '
            'Monitor LTC Properties increasing ownership control over 17 communities -- if ALG loses '
            'management contracts, service relationships could transfer to a new operator.'
        ),
    },
    {
        'name': 'ALG Senior',
        'hq_state': 'NC',
        'ceo': 'Charles E. Trefzger (Founder, President & CEO)',
        'founded': '1996',
        'website': 'algsenior.com',
        'key_insight': (
            'Founded in 1996 as Affinity Living Group by Charles Trefzger. Historically 150+ communities, '
            'now ~63. Financial distress: Fannie Mae receivership (2024), LTC Properties (NYSE: LTC) took '
            'majority ownership of 17 ALG-operated NC/SC properties through JV conversion after loan defaults.'
        ),
        'recommendation': 'Retention-first. 100% penetrated. Monitor LTC Properties ownership control.',
    },
    {
        'name': 'TRILOGY',
        'hq_state': 'KY',
        'ceo': 'Leigh Ann Barney (President & CEO)',
        'founded': '1997',
        'website': 'trilogyhs.com',
        'key_insight': (
            'Founded in 1997 by Randy Bufford (Chairman Emeritus) in Louisville, KY. Pioneered the Integrated '
            'Senior Health Campus model (IL/AL/MC/SNF on a single campus). Griffin-American Healthcare REIT III '
            'acquired ~96% for $1.125B (Sept 2015), merged into American Healthcare REIT (NYSE: AHR) at IPO '
            'Oct 2021. AHR became sole REIT owner Sept 2024 ($258M for NorthStar remaining 24%). Trilogy owns '
            'Synchrony Health Services, a vertically integrated pharmacy/rehab/lab arm processing 1.2M '
            'prescriptions/month. Acquired Kingston HealthCare (Toledo, OH) Dec 2025 adding 14 campuses.'
        ),
        'recommendation': (
            '#1 corporate opportunity in SOM market ($41.8M total potential, 4.8% penetration). '
            'Target Louisville (11 facilities, 0 served) and Indianapolis (10 facilities, 0 served) '
            'for metro market entry.'
        ),
    },
    {
        'name': 'TRILOGY HEALTH SERVICES',
        'hq_state': 'KY',
        'ceo': 'Leigh Ann Barney (President & CEO)',
        'founded': '1997',
        'website': 'trilogyhs.com',
        'key_insight': (
            'Founded in 1997 by Randy Bufford in Louisville. Owned by American Healthcare REIT (NYSE: AHR). '
            'Integrated Senior Health Campus model. Synchrony Health Services pharmacy/rehab arm processes '
            '1.2M prescriptions/month. Kingston HealthCare acquisition (Dec 2025) added 14 Ohio campuses.'
        ),
        'recommendation': '#1 SOM opportunity ($41.8M potential, 4.8% penetration). Target Louisville and Indianapolis.',
    },
    {
        'name': 'NAVION SENIOR SOLUTIONS',
        'hq_state': 'NC',
        'ceo': 'Beverly Janco Tuttle (CEO)',
        'founded': '2015',
        'website': 'navionseniorliving.com',
        'key_insight': (
            'Founded in 2015 as Ravn Senior Solutions by Stephen Morton, a serial senior living entrepreneur '
            'who previously founded SALI (41 communities NC/SC/VA, sold to Brookdale for $82.9M in 2006) and '
            'led Bell Senior Living (sold to Five Star 2012). Family-owned, no PE. Mixed model: ~19 owned, '
            'rest managed for NHI (NYSE: NHI), Blackstone/Longview, and DHC (5 former Five Star SC properties, '
            '2021). CEO Beverly Janco Tuttle appointed January 2025, Morton retains Chairman role. 51 communities '
            'across 7 states.'
        ),
        'recommendation': (
            'Jan 2025 CEO transition creates engagement inflection point. Prioritize 16 SC campuses as '
            'largest whitespace. Clarify owned vs managed status per facility -- REIT/PE owners (NHI, '
            'Blackstone) may hold decision authority at managed communities.'
        ),
    },
    {
        'name': 'Navion Senior Solutions',
        'hq_state': 'NC',
        'ceo': 'Beverly Janco Tuttle (CEO)',
        'founded': '2015',
        'website': 'navionseniorliving.com',
        'key_insight': (
            'Founded 2015 by Stephen Morton (ex-SALI/Brookdale, ex-Bell/Five Star). Family-owned, no PE. '
            '51 communities across 7 states. Mixed owned/managed model (NHI, Blackstone/Longview, DHC). '
            'New CEO Beverly Janco Tuttle appointed January 2025.'
        ),
        'recommendation': 'CEO transition creates engagement inflection. Prioritize SC whitespace (16 campuses).',
    },
    {
        'name': 'KISCO SENIOR LIVING',
        'hq_state': 'CA',
        'ceo': 'Andrew S. Kohlberg (Founder, President & CEO)',
        'founded': '1990',
        'website': 'kiscoseniorliving.com',
        'key_insight': (
            'Founded in 1990 in Carlsbad, CA by Andrew Kohlberg (also Vice Chairman/investor, Phoenix Suns). '
            '32 communities across 10 states + DC, $600M+ annual revenue, $3B+ AUM. Long-term strategic '
            'development partnership with Welltower (major healthcare REIT), co-developing premium properties '
            'like Cardinal at North Hills (Raleigh). MJ Ritschel sits on the NIC Operator Advisory Board. '
            'Affiliated with Balfour Senior Living in 2023 (~10 Colorado communities). NC is a stated growth market.'
        ),
        'recommendation': (
            'We serve 84% of DB facilities with 75% integration -- strong at facility level but lacks '
            'corporate alignment. Establish corporate relationship with Kohlberg team while Kisco actively '
            'targets NC for growth.'
        ),
    },
    {
        'name': 'HERITAGE HALL',
        'hq_state': 'VA',
        'ceo': None,
        'founded': None,
        'website': None,
        'key_insight': (
            'Virginia-based for-profit SNF chain operating 16 skilled nursing facilities across rural and '
            'exurban Virginia, from Leesburg in Northern VA to Wise and Clintwood in the SW coal country. '
            'All facilities operate under separate "[City] Life Care LLC/Corp" legal entities (CMS Chain ID 265). '
            'Three facilities are five-star rated (Front Royal, Laurel Meadows, Leesburg). One facility, '
            'South Roanoke Nursing and Rehabilitation, operates under non-Heritage branding. '
            'Ownership and leadership details are not publicly disclosed.'
        ),
        'recommendation': (
            'Deeply penetrated (94% of campuses served) but only 4 of 15 served are fully integrated. '
            'Primary opportunity: deepen integration at 11 single-service sites. '
            'Leadership identification is a gap -- no CEO or executive contacts on file.'
        ),
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
    status = 'OK' if affected > 0 else 'NOT FOUND'
    print(f"  {status} | {u['name']}")
    count += affected

print(f"\n{count} rows updated")
