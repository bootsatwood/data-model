# V19 Metro Priority Targets Analysis - Continuation Handoff
## Session Summary for Next Conversation

**Date**: November 24, 2025  
**Project**: Eventus Healthcare Economic Model - Metro Market Analysis  
**Version**: V19.3

---

## Quick Start for Next Session

**Say this to continue:**
> "I'm continuing the V19 Metro Priority Targets analysis. Please read the handoff document at V19_Metro_Analysis_Handoff.md to get up to speed on where we left off."

---

## Project Context

This analysis is part of the Eventus Healthcare Economic Model, focusing on **12 metropolitan markets** within the 6-state operational footprint (IN, KY, NC, OH, SC, VA). The goal is to identify priority corporate targets for business development.

### Key Project Files (in Project Knowledge)

| File | Purpose |
|------|---------|
| Final_Model_Rulebook_V19_1.md | Authoritative reference for calculations and filters |
| Combined_Database_FINAL_V19_1.xlsx | Source database (20,943 facilities) |
| Economic_Model_Scenario_2_Combined_V19_1.xlsx | Revenue calculations (S2 = Market +10%) |

---

## What Was Accomplished This Session

### 1. Database Enhancement (V19.1 → V19.1 Enhanced)

Applied **15-mile radius methodology** from city centers to correctly classify facilities into 12 metros. This corrected Geographic_Tier misclassifications where facilities in metro areas (especially Northwest Indiana, Evansville, Toledo, Harrisonburg-Charlottesville) were incorrectly marked as C_Rural.

**Output**: `Combined_Database_FINAL_V19_1_Enhanced.xlsx`

New columns added:
- `Metro_Assignment` — Which of the 12 metros (or null)
- `Distance_to_Metro_Center` — Miles from city center
- `Metro_Center_Used` — Which city center was used
- `Original_Geographic_Tier` — Preserved original classification

**12 Metros with facility counts:**
- Cleveland-Akron: 350
- Cincinnati: 205
- Indianapolis: 202
- Columbus: 193
- Louisville: 150
- Charlotte: 133
- Richmond: 114
- Toledo: 83
- Lexington: 63
- Northwest Indiana: 61
- Evansville: 60
- Harrisonburg-Charlottesville: 53

### 2. TAM/SAM/SOM/Metro Framework

Created custom report structure (separate from standard Comprehensive Report):

| Level | Filter | Facilities |
|-------|--------|------------|
| TAM | Corporate only, all states | 11,973 |
| SAM | Corporate, Existing + Priority states, no barriers | 5,031 |
| SOM | Corporate, Existing states only, no barriers | 3,102 |
| Metro Markets | Corporate, 12 metros, no barriers, Green contract status | 685 |

**Output**: `V19_Metro_TAM_SAM_SOM_Summary.xlsx`

### 3. Priority Corporate Targets Analysis

Created two views for business development prioritization:

**View 1: Top 4 Metros - Top 3 Corporates Each**
- 12 corporate entities across 4 priority metros
- 120 facilities (28 currently served)
- $44.6M total opportunity

Top 4 Metros (by opportunity):
1. Cleveland-Akron: $35.6M
2. Indianapolis: $29.9M
3. Columbus: $25.3M
4. Cincinnati: $23.8M

**View 2: Top 75 Corporate Entities**
- 75 corporate entities across all 12 metros
- 454 facilities (86 currently served)
- $168.2M total opportunity
- At 15% conversion = $25.2M (meets target)

**Output**: `V19_Metro_Priority_Targets_Final_v2.xlsx` (with abbreviated currency: $12.2M, $950K)

---

## Key Decisions Made

### Barriers Applied

| Corporate | Status | Notes |
|-----------|--------|-------|
| **Cardon & Associates** | BARRIER ADDED | Excluded from all opportunity calculations |
| **Communicare Health** | ALREADY BLOCKED | "Own Provider Group" barrier on all 134 facilities |

### Entities Specifically Requested to Include

| Corporate | Status | In Analysis |
|-----------|--------|-------------|
| Majestic Care | No barrier, 12 metro facilities | ✓ Included |
| Saber Healthcare Group | No barrier, 21 metro facilities | ✓ Included |
| Prestige | No barrier, only 1 metro facility | Limited presence |

### Filter Rules for Metro Markets

- **Ownership**: Corporate only (Independent excluded at all levels)
- **Barriers**: Excluded
- **Contract Status**: Green only (Yellow and Red excluded)
- **Geography**: Metro_Assignment not null (within 15mi of city center)

---

## Output Files Created

All files in `/mnt/user-data/outputs/`:

| File | Description |
|------|-------------|
| `Combined_Database_FINAL_V19_1_Enhanced.xlsx` | Enhanced database with Metro_Assignment |
| `V19_Database_Enhancement_Geographic_Tier.md` | Documentation of enhancement methodology |
| `V19_Metro_TAM_SAM_SOM_Summary.xlsx` | TAM/SAM/SOM/Metro summary table |
| `V19_Metro_TAM_SAM_SOM_Methodology.md` | Documentation of filter structure |
| `V19_Metro_Corporate_Opportunities.xlsx` | All corporates by metro (13 sheets) |
| `V19_Metro_Priority_Targets_Final_v2.xlsx` | **FINAL: Top 4 Metros + Top 75 Entities** |

---

## Conversion Scenarios

### Top 4 Metros ($44.6M pool)

| Rate | Projected Revenue |
|------|-------------------|
| 10% | $4.5M |
| 15% | $6.7M |
| 20% | $8.9M |

### Top 75 Entities ($168.2M pool)

| Rate | Projected Revenue | vs $25M Target |
|------|-------------------|----------------|
| 10% | $16.8M | -$8.2M |
| **15%** | **$25.2M** | **+$0.2M ✓** |
| 20% | $33.6M | +$8.6M |

---

## Top 10 Corporate Targets (Quick Reference)

| Rank | Corporate Entity | Facilities | We Serve | Opportunity |
|------|------------------|------------|----------|-------------|
| 1 | American Senior Communities | 57 | 30 | $15.2M |
| 2 | Trilogy Health Services | 48 | 0 | $9.8M |
| 3 | Foundations Health Solutions | 19 | 0 | $7.5M |
| 4 | Legacy Health Services | 13 | 0 | $7.1M |
| 5 | Saber Healthcare Group | 21 | 9 | $6.1M |
| 6 | Ciena Healthcare | 11 | 0 | $5.9M |
| 7 | Majestic Care | 12 | 5 | $4.2M |
| 8 | Gardant Management | 10 | 0 | $4.2M |
| 9 | PACS Group | 7 | 1 | $3.8M |
| 10 | Brickyard Healthcare | 8 | 1 | $3.5M |

---

## Potential Next Steps

1. **Individual Metro Deep Dives** — Detailed analysis of specific metros
2. **Corporate Entity Profiles** — Deep dive on top targets (facilities, locations, service gaps)
3. **Integration vs New Business Split** — Separate strategies for existing customers vs new
4. **Geographic Heat Maps** — Visual representation of opportunity concentration
5. **Conversion Scenario Modeling** — More detailed assumptions by corporate/metro
6. **Slide Deck Creation** — PowerPoint with key findings
7. **Version Control** — Formalize V19.3 package with all deliverables

---

## Technical Notes

### Revenue Source
All revenue uses **Scenario 2 (Market +10%)** from Economic_Model_Scenario_2_Combined_V19_1.xlsx

### Key Columns Used
- `Ownership_Type` — Corporate vs Independent
- `Barrier` — Null = no barrier
- `Contract_Status` — Green/Yellow/Red
- `Metro_Assignment` — Added via enhancement (join on Facility_Name + Address)
- `Current_Revenue`, `Integration_Revenue`, `New_Business_Revenue` — From S2

### Excluded from Analysis
- Independent facilities (all levels)
- Facilities with barriers (SAM, SOM, Metro)
- Yellow/Red contract status (Metro only)
- Cardon & Associates (barrier added this session)

---

## Session Statistics

- Database: 20,943 total facilities → 685 Corporate Metro (filtered)
- Corporate entities in metros: 196 total → 75 prioritized
- Files created: 8
- Key deliverable: V19_Metro_Priority_Targets_Final_v2.xlsx

---

**End of Handoff Document**

*Created: November 24, 2025*
