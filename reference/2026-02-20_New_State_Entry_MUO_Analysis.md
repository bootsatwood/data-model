# New State Entry Seeded by Existing MUO Relationships

**Date:** February 20, 2026
**Author:** Roian Atwood
**Source:** Combined Database V20.0 (20,943 facilities)
**Companion File:** [[2026-02-20_New_State_Entry_MUO_Analysis.xlsx]]

---

## Purpose

This analysis identifies which corporate owners (MUOs) Eventus currently serves in its existing six-state footprint who also operate facilities in states outside that footprint. The strategic premise is straightforward: entering a new state is easier when a corporate relationship already exists. If Eventus serves 10 buildings for a chain in Ohio and that chain has 30 buildings in Illinois, the Illinois entry conversation starts from a position of trust and demonstrated value rather than a cold pitch.

---

## Methodology

The analysis began with every corporate owner in the Combined Database where at least one facility is actively served (Do_We_Serve = Yes) and barrier-free. This yielded **189 corporate partners**. From there, the full national footprint of each partner was mapped across all states in the database to identify where these relationships extend beyond Eventus's current operating territory.

The existing operational footprint covers six states: IN, KY, NC, OH, SC, and VA. Everything else is considered "outside existing footprint" for purposes of this analysis.

---

## Key Findings

### The Reach Is Much Broader Than the Priority List Suggests

Of the 189 barrier-free corporate partners, **48 operate facilities outside the existing six-state footprint**, collectively reaching **39 states** and **1,146 facilities**. The current priority expansion list (IA, IL, MI, MN, MT, PA, WI) captures seven of these states, but the partner network reaches far beyond them.

### All Seven Priority Expansion States Have Partner Presence

Every state on the priority expansion list has at least one existing MUO relationship that could seed entry:

| Priority State | MUOs with Presence | Partner Facilities | S2 Total Potential Revenue |
|---|---|---|---|
| IL | 10 | 116 | $69,297,020 |
| MI | 8 | 86 | $33,303,711 |
| PA | 10 | 63 | $33,592,166 |
| WI | 4 | 12 | $2,569,510 |
| IA | 1 | 28 | $6,589,698 |
| MN | 1 | 1 | $194,340 |
| MT | 1 | 1 | $219,550 |

Illinois, Michigan, and Pennsylvania stand out with the densest partner presence and the largest S2 revenue opportunity. Iowa is interesting: a single partner (Legacy Healthcare) accounts for all 28 facilities there, which means the entry strategy hinges entirely on one relationship. Minnesota and Montana each have only one partner with one facility, making them thin from a relationship-seeding standpoint.

### Metro Density in the Top Three Priority States

Looking at where partner facilities cluster within IL, MI, and PA provides a clearer picture of where clinical teams would actually operate. The companion workbook includes a Priority Metro Density tab with the full breakdown, but the key patterns are worth noting here.

In Illinois, Chicago is the center of gravity with 50 of the state's 116 facilities and $34.3M in S2 revenue. Beyond Chicago, Peoria and Rockford each have 3 facilities, and 41 facilities fall along Interstate corridors outside metro areas. Illinois has the strongest metro concentration of the three states, with nearly half its facilities in a single metro.

Michigan is more distributed. Detroit leads with 11 facilities ($7.2M), followed by Flint (6), Grand Rapids (5), Lansing (4), Ann Arbor (3), and Kalamazoo (3). No single metro dominates, which means a Michigan entry strategy requires multi-metro clinical team deployment from the start. Thirty of Michigan's 86 facilities are classified rural under the interim rules, suggesting meaningful presence outside the major metros.

Pennsylvania shows a dual-anchor pattern. Pittsburgh (9 facilities, $4.8M) and Philadelphia (7 facilities, $4.2M) anchor opposite ends of the state, with Scranton (6 facilities) forming a third cluster in the northeast. Twenty-two of 69 facilities are rural, and 23 sit along Interstate corridors between the metros. A Pennsylvania entry likely starts in one anchor and expands from there rather than trying to cover the full state at once.

### States Worth a Second Look

Several states outside the current priority and emerging lists show substantial partner density that may warrant strategic consideration:

| State | MUOs | Facilities | Note |
|---|---|---|---|
| TN | 10 | 94 | Borders KY and VA; 10 different MUO relationships |
| CA | 4 | 152 | High facility count but geographically distant |
| TX | 7 | 65 | Multiple partners, large market |
| AL | 4 | 34 | Borders existing territory (GA emerging) |
| CO | 5 | 45 | Five partners, meaningful density |
| MO | 4 | 28 | Four partners, central geography |
| MS | 2 | 23 | Adjacent to AL, near existing |
| MD | 6 | 16 | Six partners, dense mid-Atlantic corridor |

Tennessee and Alabama deserve particular attention. Tennessee borders two existing states (KY, VA), has 10 different MUO relationships seeding it, and 94 partner-owned facilities. Alabama borders the emerging market of Georgia and has 34 partner facilities across 4 MUOs.

### Top MUOs by Reach Outside Existing Footprint

The five corporate partners with the largest out-of-footprint presence are:

| Corporate Name | Facilities Outside | States Outside | Served Facilities | Outside Footprint States |
|---|---|---|---|---|
| PACS GROUP | 172 | 11 | 3 | AK, AZ, CA, CO, MO, NV, OR, PA, TN, TX, WA |
| LIFE CARE CENTERS OF AMERICA | 167 | 21 | 39 | AZ, CO, FL, GA, HI, ID, KS, MA, MI, MO, NE, NM, NV, OR, PA, RI, TN, TX, UT, WA, WY |
| LEGACY HEALTHCARE | 84 | 3 | 44 | IA, IL, SD |
| PRUITTHEALTH | 65 | 2 | 73 | FL, GA |
| NATIONAL HEALTHCARE CORPORATION | 49 | 4 | 19 | AL, GA, MO, TN |

Life Care Centers of America is the most geographically dispersed, operating across 21 states outside the existing footprint. PruittHealth's presence is concentrated in FL and GA (both emerging markets) with a strong existing relationship (73 served facilities). Legacy Healthcare's 84 facilities are concentrated in IA, IL, and SD, making them the primary relationship for an upper-Midwest entry strategy.

---

## Observations for Strategy Discussion

The partner network reaches 39 of 50 states. This does not mean Eventus should enter all of them, but it does mean the question of "where do we have warm relationships?" has a much broader answer than the current seven-state priority list. The states where multiple independent MUO relationships converge, particularly adjacent to existing territory, represent the strongest candidates for relationship-seeded entry. Tennessee, in particular, appears underweighted given its adjacency, MUO density, and facility count.

The analysis also reveals concentration risk in certain expansion states. Iowa, Minnesota, and Montana each depend on a single corporate relationship. If that relationship stalls or the partner has a barrier applied, the state entry thesis weakens considerably.

### A Note on Geographic Tier and Operational Clustering

The Facility Detail tab in the companion workbook shows nearly all outside-footprint facilities classified as C_Rural. This is not because these facilities are all in rural areas. The Geographic Tier classification (A_Metro, B_Highway, C_Rural) was only ever built for the existing six-state footprint, so every facility in every other state defaults to C_Rural simply because no metro centers or highway corridors were defined there. This is a data model gap, not a market reality. A separate effort to extend metro definitions to expansion states is documented in [[2026-02-21_Metro_Definition_Enhancement_Proposal]].

Beyond that gap, the intent of this analysis is ultimately to support clinical teams in delivering services effectively, and that means thinking about transportation logistics and service density, not just population. Metro markets matter, but so do non-metro clusters where facilities are geographically concentrated even if the surrounding population is not large. A corridor with 15 SNFs within a 30-mile stretch is operationally attractive regardless of whether a Census Bureau MSA boundary encompasses it. As this work progresses, we should look for facility-dense clusters outside of metro areas that could represent efficient service delivery zones for clinical teams.

---

## Excel Workbook Tabs

| Tab | Contents |
|---|---|
| Executive Summary | Key metrics at a glance, including S2 revenue and priority state highlights |
| State Summary | Every state outside existing footprint with MUO count, facility count, interim geographic tier breakdown, and S2 Total Potential Revenue |
| MUO Summary | All 48 corporate partners with outside-footprint presence, including S2 revenue by partner (outside footprint and total served) |
| Facility Detail | All 1,146 individual facilities with interim geographic tier, nearest metro/Interstate, distances, and S2 Total Potential Revenue per facility |
| Priority Metro Density | Facility density by metro center for IL, MI, and PA with revenue, average census, and tier breakdown |

---

## Related Documents

- [[6_Core_Rulebook_V20_0|Core Rulebook V20.0]] for database methodology and definitions
- [[6.1_Comprehensive_Report_Compendium_V20_1|Report Compendium V20.1]] for market classification definitions
- [[MUO_Profiles_Index|MUO Profiles]] for deep-dive profiles on priority corporate accounts

---

*Analysis generated from Combined Database V20.0. All facility counts and classifications reflect the production database as of December 2025.*
