# Metro Definition Enhancement Proposal

**Date:** February 21, 2026
**Author:** Roian Atwood
**Status:** DRAFT
**Parent:** [[01_Data Model/_Data_Model_Index|Data Model Index]]

---

## Problem Statement

The Geographic Tier classification (A_Metro, B_Highway, C_Rural) in the Combined Database was built exclusively for the existing six-state operational footprint (IN, KY, NC, OH, SC, VA). Facilities in all other states default to C_Rural regardless of their actual proximity to metropolitan areas. As Eventus evaluates expansion into new states, this gap produces misleading classifications and limits the utility of geographic analysis outside the current footprint.

---

## Current State

### How the Original Metros Were Defined

The original 19 metro definitions were created ad-hoc. Clinical operations provided a list of cities where they operate, lat/long coordinates were looked up via Google, and a 15-mile radius was applied. There was no formal population threshold, no standardized data source, and no documented selection criteria beyond clinical team familiarity.

Of the 19 original metros, 12 were designated as named priority metro markets and received Metro_Assignment values in the database. The remaining 7 (Greensboro-High Point, Raleigh, Wilmington, Columbia, Charleston SC, Dayton, Roanoke) are classified A_Metro in Geographic_Tier but do not have Metro_Assignment populated.

### Population Range of Original Metros

| Metro | State | Approx. MSA Population |
|---|---|---|
| Harrisonburg-Charlottesville | VA | ~139,000 |
| Evansville | IN | ~272,000 |
| Wilmington | NC | ~310,000 |
| Roanoke | VA | ~315,000 |
| Lexington | KY | ~533,000 |
| Toledo | OH | ~601,000 |
| Greensboro-High Point | NC | ~780,000 |
| Dayton | OH | ~814,000 |
| Charleston SC | SC | ~850,000 |
| Columbia | SC | ~870,000 |
| Richmond | VA | ~1,330,000 |
| Louisville | KY | ~1,380,000 |
| Raleigh | NC | ~1,500,000 |
| Cleveland-Akron | OH | ~2,050,000 |
| Indianapolis | IN | ~2,150,000 |
| Columbus | OH | ~2,180,000 |
| Cincinnati | OH | ~2,270,000 |
| Charlotte | NC | ~2,760,000 |

Northwest Indiana (Gary) is a special case: it is a metro division of the Chicago MSA, not a standalone MSA. City population is ~67,000.

The smallest standalone MSA in the original set is **Harrisonburg at ~139,000**, which establishes a de facto population floor of approximately 130,000 to 140,000.

### Recent Metro Market Reports

The five most recent metro market reports (as of February 2026) cover:

1. Greater Richmond, VA
2. NW Lakeshore / Calumet / Valparaiso / Michigan City (IN/IL border)
3. Greater Cleveland-Akron-Canton, OH
4. Indianapolis / Anderson / Muncie / Columbus, IN
5. Shenandoah Valley / I-64 Corridor, VA

The Shenandoah Valley report covers the Harrisonburg-Charlottesville region, which is the smallest MSA to receive a dedicated analysis.

---

## Interim Classification (Applied February 21, 2026)

An interim three-tier classification (A_Metro, B_Highway, C_Rural) was applied to facilities in the [[2026-02-20_New_State_Entry_MUO_Analysis.xlsx|New State Entry workbook]] to address the immediate analytical gap. This is a working classification for that deliverable only. It has **not** been applied to the Combined Database.

### Interim A_Metro Rules

1. **Radius:** 15 miles from city center (same as production methodology)
2. **Metro centers:** Principal cities of well-known MSAs in each state, using approximate city-center lat/long coordinates looked up manually. This replicates the original ad-hoc approach used for the existing footprint.
3. **Distance calculation:** Haversine formula using existing facility Latitude/Longitude columns
4. **Classification:** Facilities within 15 miles of any defined metro center are labeled `A_Metro (Interim)`.
5. **No population threshold was applied.** Major cities were selected based on general knowledge of each state's principal metros, not a formal population cutoff. This is a known limitation.

### Interim B_Highway Rules

1. **Radius:** 10 miles from nearest Interstate route point (same threshold as production methodology)
2. **Route definition:** Major Interstate corridors were identified for each of the 39 outside-footprint states. Routes were defined using manually selected waypoint coordinates (latitude/longitude) at key junctions and endpoints, then interpolated at approximately 2-mile intervals along each corridor to produce a continuous sample of route points. This yielded approximately 10,154 route sample points across all states.
3. **Distance calculation:** Haversine formula from each facility to the nearest interpolated route point on the nearest Interstate.
4. **Classification priority:** A_Metro takes precedence over B_Highway. A facility within 15 miles of a metro center is classified A_Metro regardless of its distance to an Interstate. Only facilities that do not qualify as A_Metro are evaluated for B_Highway. Facilities within 10 miles of an Interstate route point that are not already A_Metro are labeled `B_Highway (Interim)`. All remaining facilities are `C_Rural`.
5. **Interstates included:** The major Interstates serving each state were selected based on the principal corridors connecting population centers. For example, Illinois included I-55, I-57, I-70, I-72, I-74, I-80, I-88, and I-90/94. The full set of routes per state is embedded in the analysis code.
6. **This is an approximation.** Waypoint interpolation along straight-line segments between reference points does not perfectly trace the actual road geometry. The production methodology uses DOT shapefile polylines which capture every curve and interchange. The interim approach is sufficient for a working classification but will produce minor inaccuracies, particularly on routes with significant curvature between waypoints.

### Interim Results

| Classification | Facilities |
|---|---|
| A_Metro (Interim) | 432 |
| B_Highway (Interim) | 301 |
| C_Rural | 413 |
| **Total** | **1,146** |

Approximately 38% of outside-footprint facilities are within 15 miles of a defined metro center, 26% are within 10 miles of a major Interstate corridor (but not near a metro), and the remaining 36% are classified rural under the interim rules.

### Metro Centers Used (39 States)

Metro centers were defined for every state where barrier-free corporate partners operate outside the existing footprint. The full list of cities is embedded in the analysis code and includes principal cities such as Chicago (IL), Detroit (MI), Pittsburgh and Philadelphia (PA), Atlanta (GA), Nashville and Memphis (TN), Miami, Tampa, Orlando, and Jacksonville (FL), among others. A complete reference table should be formalized as part of the full enhancement.

### What This Interim Classification Does NOT Do

1. **No DOT shapefile route geometry.** The B_Highway classification uses waypoint interpolation along straight-line segments rather than actual DOT National Highway System shapefiles. This is a reasonable approximation but will produce minor distance inaccuracies on routes with significant curvature between waypoints. The full enhancement should use official DOT polyline data for precise distance-to-corridor calculations.
2. **No population threshold.** Metro centers were selected by judgment, not by a formal MSA population cutoff. Some included cities may be smaller than the de facto ~130K floor established by Harrisonburg in the original classification.
3. **No facility-dense cluster identification.** Non-metro areas with high facility density (operationally attractive for clinical teams regardless of population) have not been identified. This would require spatial clustering analysis (e.g., DBSCAN) and is a separate analytical layer.
4. **No database modification.** The Combined Database V20.0 has not been changed. The interim classification exists only in the New State Entry workbook. Production Geographic_Tier values remain as-is.
5. **No formal CBSA centroid source.** City centers were approximated, not sourced from Census Bureau CBSA centroid coordinates. The full enhancement should use the federal standard.
6. **No strategic Interstate selection.** The interim classification includes all major Interstates in each state. The production B_Highway classification in the existing footprint is limited to five strategically selected corridors (I-65, I-71, I-75, I-77, I-85). For expansion states, a deliberate decision about which corridors matter operationally has not been made. The interim approach casts a wide net; the full enhancement should narrow to strategically relevant corridors per state.

---

## Proposed Full Enhancement

### Data Source

Switch from ad-hoc city lookups to **Census Bureau CBSA (Core Based Statistical Area) definitions** for metro center coordinates. This is the federal standard, publicly available, and defensible.

Source: Census Bureau CBSA definitions (publicly available at census.gov).

### Population Threshold

To be determined. Based on the original 19 metros, a floor of approximately **130,000 to 140,000 MSA population** would be consistent with existing practice. However, this threshold should be a deliberate decision rather than an inherited artifact.

Considerations for setting the threshold:

- A lower threshold (e.g., 100,000) casts a wider net and captures more mid-size cities, but may include markets that lack the facility density to justify clinical team deployment.
- A higher threshold (e.g., 250,000) focuses on operationally meaningful markets but may exclude metros where Eventus already has meaningful presence (Harrisonburg would not qualify).
- The threshold should be informed by clinical operations: what is the minimum market size where a dedicated clinical team can maintain an efficient service route?

### Scope

This enhancement should apply to all states in the database, not just the existing or priority expansion states. The database is national (20,943 facilities across 50 states), and the Geographic Tier classification should reflect that.

### Methodology

For each state:

1. Identify all Census Bureau-defined MSAs meeting the population threshold
2. Use CBSA centroid coordinates as metro center points
3. Calculate haversine distance from every facility (using existing Latitude/Longitude columns) to the nearest qualifying MSA centroid
4. Classify facilities within 15 miles as A_Metro (consistent with existing methodology)
5. Populate Metro_Assignment, Distance_to_Metro_Center, and Metro_Center_Used columns

### Beyond Metro: Facility-Dense Clusters

Metro classification captures population density, but clinical operations care about facility density. A corridor with 15 SNFs along a 30-mile stretch is operationally attractive even if no Census MSA boundary encompasses it. Future iterations of this work should consider identifying facility-dense clusters that fall outside metro areas but represent efficient service delivery zones. This is a separate analytical layer from metro classification and would require spatial clustering analysis (e.g., DBSCAN or similar) rather than simple radius calculations.

### B_Highway Tier

The B_Highway classification in production (within 10 miles of major Interstate exits on I-65, I-71, I-75, I-77, I-85) uses a curated set of five strategically selected corridors. The interim classification applied to the New State Entry workbook uses a broader approach with all major Interstates per state and waypoint-interpolated route geometry. Moving to a production-quality classification for expansion states requires:

1. Identifying which Interstate corridors matter in each expansion state (strategic decision, not just geographic coverage)
2. Obtaining DOT National Highway System shapefiles for those routes (precise polyline geometry)
3. Calculating perpendicular distance from each facility to the nearest point on the route polyline

The interim waypoint approach provides a useful working classification, but the full enhancement should use official DOT data for precision and limit the corridor set to operationally relevant routes rather than all Interstates in a state.

---

## Relationship to Other Work

This document is a **data model enhancement proposal**. It is separate from the new state entry strategy documented in [[2026-02-20_New_State_Entry_MUO_Analysis]]. The new state entry analysis identified the gap (all outside-footprint facilities showing C_Rural) but the resolution belongs in the data model, not in the strategy deliverable.

See also:

- [[6_Core_Rulebook_V20_0|Core Rulebook V20.0]] Section 2.8 for current Geographic Tier definitions
- [[Database_Change_Request_V19_2]] (archived) for the original proposal to overhaul geographic infrastructure
- [[6.2_Metro_Market_Analysis_Compendium_V19_2|Metro Market Analysis Compendium]] for how geographic tiers are used in reporting

---

## Open Questions

1. What population threshold should we use? (~130K floor based on precedent, or a deliberate new standard?)
2. Should the threshold be the same for all states, or should expansion states use a different threshold than existing states?
3. Who needs to approve this change before it is implemented? (Per Core Rulebook Section 1.3, geographic tier recalculation requires authorization.)
4. Should this be a V20.x increment or wait for V21?
5. How do we handle the Gary/NW Indiana special case going forward? (Metro division of Chicago, not a standalone MSA.)

---

*This is a living document. It will be updated as decisions are made and the enhancement is implemented.*
