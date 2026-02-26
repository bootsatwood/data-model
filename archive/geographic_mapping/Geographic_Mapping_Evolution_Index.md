# Geographic Mapping Evolution - Complete Reference

This archive documents the evolution of geographic visualization approaches used to map Eventus healthcare facility opportunities. The approach changed rapidly as methodology was refined and stakeholder needs evolved.

---

## Summary: What Changed Between Versions

| Version | Date | Database | Format | Facilities in Final Layer | Opportunity | Key Innovation |
|---------|------|----------|--------|---------------------------|-------------|----------------|
| **V9 KML** | Nov 18 | V9 | KML | 5,277 | $476.4M | 8-layer strategic framework |
| **V15 CSV** | Nov 19 | V15 | CSV | 1,360 | $528.5M | Progressive layer filtering with GPS |
| **V16 CSV** | Nov 20-21 | V16 | CSV | 376 | $116.2M | Contract status + Tier filtering |
| **V18.1 CSV** | Nov 22 | V18.1 | CSV | 746 | ~$150M | Simplified two-map approach |
| **V19 CSV** | Nov 24 | V19 | CSV | ~1,900 | ~$200M | Detailed breakdowns (Map1/Map2 split) |
| **V19 Excel** | Nov 24-Dec 26 | V18/V19 | Excel | 685 metro | $168.2M | Corporate prioritization for sales |

---

## Detailed Version Analysis

### V9 KML (_Mapping folder) - Nov 18, 2025

**Data Source:** Combined_Database_FINAL_V9.xlsx

**Approach:** 8-layer strategic framework organizing ALL facilities by:
- Geographic: Metro vs Rural
- Ownership: Corporate vs Independent
- Strategy: New Business vs Integration

**Structure:** 16 KML files (8 layers × SNF/ALF split)

**Statistics:**
| Layer | Description | Facilities | Revenue |
|-------|-------------|------------|---------|
| 1 | Metro Corporate New Business | 792 | $178.5M |
| 2 | Metro Independent New Business | 729 | $0 |
| 3 | Metro Corporate Integration | 496 | $26.5M |
| 4 | Metro Independent Integration | 137 | $4.5M |
| 5 | Rural Corporate Integration | 849 | $45.3M |
| 6 | Rural Corporate New Business | 1,086 | $209.5M |
| 7 | Rural Independent Integration | 256 | $12.1M |
| 8 | Rural Independent New Business | 932 | $0 |
| **Total** | | **5,277** | **$476.4M** |

**Key Insight:** Shows ENTIRE market universe organized by strategic priority. Blue pins (Layer 1) = primary targets.

**Location:** [[08_Archive/By Topic/Data Model V9/KML_Mapping/KML_Mapping_Index|KML Mapping Index]]

**KNOWN GAP:** Never regenerated for V15-V20 data. See [[08_Archive/By Topic/Data Model V9/KML_Mapping/KML_Mapping_Index|KML Mapping Index]].

---

### V15 CSV (files (15)) - Nov 19, 2025

**Data Source:** Combined_Database_FINAL_V15.xlsx

**Approach:** Progressive layer filtering showing funnel from universe to actionable targets.

**Structure:** 36 CSV files (6 layers × 2 stories × SNF/ALF split)

**Layer Progression:**

| Layer | Integration | New Business | Description |
|-------|-------------|--------------|-------------|
| L1 | 1,743 | 3,539 | Starting universe |
| L2 | 497 | 1,516 | Metro Focus (19 regions) |
| L3 | 438+59 | 922+594 | Corporate vs Independent split |
| L4 | 366 | 1,295 | Size threshold (30+/40+ beds) |
| L5 | 261 | 1,099 | No barriers |
| **L6** | **261** | **1,099** | **Metro-adjacent final** |

**Final Opportunity:**
- Integration: 261 facilities, $41.2M
- New Business: 1,099 facilities, $487.3M
- **Total: 1,360 facilities, $528.5M**

**Key Innovation:**
- GPS coordinates for Google My Maps import
- Presentation narrative built into methodology guide
- Visual specification (colors, shapes, sizes)

**Key Files:**
- `GOOGLE_MAPS_QUICK_GUIDE.md` - Import instructions
- `LAYER_GENERATION_SUMMARY.md` - Statistics and structure
- 36 CSV files with lat/lon coordinates

**Location:** Downloads/files (15)/

---

### V16 CSV (files (17)) - Nov 20-21, 2025

**Data Source:** Combined_Database_FINAL_V16.xlsx (enhanced with contract status)

**Approach:** More conservative filtering to match Brooke's $29.3M email target.

**Structure:** 14 CSV files (L0-L7 layers, combined SNF+ALF)

**Key Changes from V15:**
1. **Added L0 baseline** (all served)
2. **Added L7 Highway expansion** option
3. **Contract Status filtering** (GREEN/YELLOW/RED)
4. **Geographic Tier system** (A=15mi, B=15-30mi, C=>30mi)
5. **Different size thresholds** (MH:20+, PCP:30+, NB:40+)
6. **Combined SNF+ALF** into single Integration/NewBusiness stories

**Layer Progression (Integration):**

| Layer | Facilities | Revenue | Filter |
|-------|------------|---------|--------|
| L0 | 1,743 | $187.7M | Baseline - all served |
| L1 | 492 | $60.3M | Metro focus |
| L2 | 283 | $58.1M | Size threshold |
| L3 | 204 | $39.8M | No barriers |
| L4 | 203 | $39.6M | Remove RED status |
| L5 | 201 | $39.2M | Remove YELLOW status |
| **L6** | **117** | **$23.6M** | **Tier A only (15-mile)** |
| L7 | +84 | +$15.6M | Highway corridor option |

**Final Opportunity:**
- Integration Tier A: 117 facilities, $23.6M
- New Business Tier A: 259 facilities, $92.6M
- **Total: 376 facilities, $116.2M**

**Key Insight:** The $5.7M gap from Brooke's $29.3M target was attributed to:
- Tighter metro radius (15 vs possibly 20 miles)
- More aggressive barrier exclusions
- Contract status filtering (unique to this version)

**Key Files:**
- `Geographic_Layer_Strategy_V16_Executive_Summary.md`
- `Integration_Funnel_Compendium_V16.md` - Complete filter documentation
- `HANDOFF_V15_to_V16_Gap_Analysis.md` - **The investigation that led to V16** (explains $38.6M → $29.3M gap)
- `Combined_Database_FINAL_V16.xlsx` - Enhanced database

**Location:** Downloads/files (17)/ (now deleted, docs archived here)

---

### V18.1 Map CSVs - Nov 22, 2025

**Data Source:** Combined_Database_FINAL_V18.xlsx

**Approach:** Simplified to two master map files instead of 36 layer files.

**Structure:**
- `Map1_Current_Metro_Footprint_V18.1.csv` - 287 facilities (what we serve in metros)
- `Map2_Realistic_Growth_Opportunity_V18.1.csv` - 458 facilities (growth targets)

**New Features:**
- Visualization columns built-in (Color, Shape, Display_Label)
- Ready for direct Google Maps import without styling
- Includes Revenue_Opportunity and Opportunity_Type

**Map1 Breakdown (Current Customers):**
- Integrated facilities (both PCP+MH)
- Single Service facilities (PCP or MH only)
- Split by SNF/ALF with appropriate shapes

**Map2 Breakdown (Growth Opportunities):**
- Integration opportunities (expand services to existing customers)
- New Business opportunities (acquire new customers)
- Color-coded by opportunity type

**Location:** Downloads root (Map1_*.csv, Map2_*.csv files)

---

### V19 CSV (files (10) 3) - Nov 24, 2025

**Data Source:** Combined_Database_FINAL_V19.xlsx

**Approach:** Detailed breakdowns within Map1/Map2 structure.

**Structure:**
| File | Facilities | Description |
|------|------------|-------------|
| Map1_1_Integrated_ALF | 56 | Integrated ALF we serve |
| Map1_2_Integrated_SNF | 19 | Integrated SNF we serve |
| Map1_3_Single_Service_ALF | 122 | Single-service ALF we serve |
| Map1_4_Single_Service_SNF | 72 | Single-service SNF we serve |
| Map2_5_Integration_ALF | 109 | ALF integration opportunities |
| Map2_6_Integration_SNF | 60 | SNF integration opportunities |
| Map2_7_New_Business_ALF | 952 | ALF new business targets |
| Map2_8_New_Business_SNF | 462 | SNF new business targets |
| Map2_9_Excluded_Barriers | 102 | Facilities excluded due to barriers |
| Map2_10_Excluded_YellowRed | 5 | Facilities excluded due to contract status |

**Location:** Downloads/files (10) 3/

---

### V19 Excel (Final) - Nov 24 - Dec 26, 2025

**Data Source:** Combined_Database_FINAL_V18/V19.xlsx + Metro Enhancement

**Approach:** Corporate prioritization for sales actionability.

**Key Innovation:**
1. **12 Metro Markets** defined with 15-mile radius
2. **Metro_Assignment column** added to database
3. **TAM/SAM/SOM/Metro hierarchy** for market sizing
4. **Top 75 Corporate Entities** ranked by opportunity
5. **Chain-level barrier propagation** (if ANY facility has barrier, exclude entire company)

**Final Structure (V19_Metro_Priority_Targets_Final_v4.xlsx):**
- Sheet 1: Top 4 Metros (Top 3 corporates each)
- Sheet 2: Top 75 Metro (all 12 markets)
- Sheet 3: Top 75 SOM (6-state footprint)
- Sheet 4: Top 75 SAM (13-state expansion)

**Metro Markets (12 total):**
Cleveland-Akron (350), Cincinnati (205), Indianapolis (202), Columbus (193), Louisville (150), Charlotte (133), Richmond (114), Toledo (83), Lexington (63), Northwest Indiana (61), Evansville (60), Harrisonburg-Charlottesville (53)

**Opportunity:**
- Top 75 Metro: 454 facilities, $168.2M
- At 15% conversion = $25.2M (meets annual target)

**Key Files:**
- V19_Metro_Priority_Targets_Final_V19_2 (3)_with screenshots.xlsx - CURRENT
- V19_Metro_Analysis_Handoff.md - Session 1 documentation
- V19_Metro_Priority_Targets_Handoff_Session2.md - Session 2 documentation

**Location:** Downloads root

---

## Why Each Version Exists

| Version | Purpose | Audience |
|---------|---------|----------|
| V9 KML | "Big picture" - entire market organized by strategy | Executive overview |
| V15 CSV | "Funnel story" - show progressive filtering for presentation | Board/investor presentations |
| V16 CSV | "Reality check" - reconcile with Brooke's targets, add contract status | Internal validation |
| V18.1 CSV | "Simple viz" - two files that show everything needed | Quick mapping |
| V19 CSV | "Detailed breakdown" - granular view of Map1/Map2 components | Analysis |
| V19 Excel | "Sales actionable" - corporate targets ranked by opportunity | Business development |

---

## What To Keep vs. Archive

**CURRENT (keep accessible):**
- V19_Metro_Priority_Targets_Final_V19_2 (3)_with screenshots.xlsx
- V19 handoff documents (methodology reference)

**ARCHIVE (preserve for reference):**
- V9 KML files - original visualization concept
- V15 CSV files + guides - progressive filtering methodology
- V16 CSV files + guides - contract status methodology
- V18.1/V19 Map CSVs - simplified approach

**SUPERSEDED (can delete from Downloads):**
- Duplicate copies of same files
- Earlier V19 Excel versions (v2, v3, v4 without screenshots)

---

## Regeneration Notes

To regenerate any version with current V20 data:

1. **KML files:** Export from V20 database, apply 8-layer logic, convert to KML format
2. **V15 CSVs:** Apply progressive L1-L6 filtering with GPS coordinates
3. **V16 CSVs:** Add contract status and geographic tier filtering
4. **V19 Excel:** Run metro assignment, corporate aggregation, barrier propagation

The V19 handoff documents contain Python code patterns for regeneration.

---

## Cross-References

- [[00_Index/Project History#Geographic Visualization Evolution|Project History - Geographic Visualization Evolution]] - Timeline narrative
- [[00_Index/Document Lineage#Geographic Visualization Files|Document Lineage - Geographic Visualization Files]] - File inventory
- [[08_Archive/By Topic/Data Model V9/KML_Mapping/KML_Mapping_Index|KML Mapping Index]] - Original KML files documentation
- [[08_Archive/By Topic/Data Model V15/|Data Model V15]] - V15 related files
- [[08_Archive/By Topic/Data Model V16/|Data Model V16]] - V16 related files
- [[00_Index/_00_Index|Master Index]] - Main navigation

---

*Documented: January 11, 2026*
*This archive consolidates understanding of all mapping approaches used in the Eventus project.*
