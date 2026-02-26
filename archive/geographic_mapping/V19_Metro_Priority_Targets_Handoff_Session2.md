# V19 Metro Priority Targets Analysis - Session 2 Handoff
## Comprehensive Session Summary

**Date**: November 25, 2025  
**Session Focus**: Report consolidation, barrier propagation, and state expansion analysis  
**Version**: V19 (based on V18.0 database/scenario files)

---

## Executive Summary

This session focused on refining the V19 Metro Priority Targets analysis with three main workstreams:

1. **Report Consolidation**: Transformed 4 separate metro tables into a single consolidated view for slide presentation
2. **SOM/SAM Expansion**: Created Top 75 corporate entity reports at SOM (6 states) and SAM (13 states) levels
3. **Barrier Propagation**: Applied chain-level barrier exclusion logic (if ANY facility has a barrier, exclude entire corporate entity)
4. **State Expansion Analysis**: Enhanced new state opportunities table with facility counts and revenue potential

---

## Files Created This Session

### Primary Deliverables

| File | Description | Location |
|------|-------------|----------|
| **V19_Metro_Priority_Targets_Final_v4.xlsx** | 4-sheet comprehensive report with barrier propagation | /mnt/user-data/outputs/ |
| **V19_New_State_Opportunities_Enhanced.xlsx** | State expansion analysis with revenue potential | /mnt/user-data/outputs/ |
| **V19_Metro_Priority_Targets_Handoff_Session2.md** | This handoff document | /mnt/user-data/outputs/ |

### Intermediate Versions (Archive)
- V19_Metro_Priority_Targets_Final_v2.xlsx (uploaded by user, original format)
- V19_Metro_Priority_Targets_Final_v3.xlsx (consolidated format, pre-barrier propagation)

---

## File Structure & Contents

### V19_Metro_Priority_Targets_Final_v4.xlsx

**Sheet 1: Top 4 Metros**
- **Scope**: Cleveland-Akron, Indianapolis, Columbus, Cincinnati
- **Format**: Top 3 corporate entities per metro (12 total)
- **Filter**: 15-mile radius from city centers, Green contract status, Corporate only, Cardon barrier exclusion
- **Facilities**: 120 (28 served)
- **Total Opportunity**: $44.6M
- **Key Feature**: Single consolidated table (no subtotals between metros)

**Sheet 2: Top 75 Metro**
- **Scope**: All 12 metropolitan markets
- **Filter**: Same as Sheet 1
- **Facilities**: 454 (86 served)
- **Total Opportunity**: $168.2M
- **Key Feature**: "Metros" column shows COUNT of metros (not list)

**Sheet 3: Top 75 SOM**
- **Scope**: IN, KY, NC, OH, SC, VA (6 states)
- **Filter**: Corporate only, Chain-level barrier exclusion, "unknown" excluded
- **Facilities**: 1,378 (315 served)
- **Total Opportunity**: $502.6M
- **Key Change**: Applied barrier propagation (CCH Healthcare removed)

**Sheet 4: Top 75 SAM**
- **Scope**: SOM + IA, MN, IL, MI, PA, WI, MD (13 states total)
- **Filter**: Same as SOM
- **Facilities**: 2,033 (273 served)
- **Total Opportunity**: $858.0M
- **Key Change**: Applied barrier propagation (CCH Healthcare removed)

**Note**: Maryland (MD) substituted for Montana (MT) per user request for this analysis only

---

## Data Flow Architecture

```
SOURCE DATA (Project Files)
├── Combined_Database_FINAL_V18.xlsx (21,023 facilities)
│   └── Columns: Source_Type, Corporate_Name, Ownership_Type, Do_We_Serve, 
│                 Barrier, State, Census, Contract_Status, Geographic_Tier
│
└── Economic_Model_Scenario_2_Combined_V18.xlsx (21,023 facilities)
    └── Revenue Columns: Current_Revenue, Integration_Revenue, 
                         New_Business_Revenue, Total_Potential_Revenue

          ↓

FILTER APPLICATIONS
├── Metro Level (Sheets 1-2)
│   ├── Geographic: 15-mile radius from 12 city centers
│   ├── Ownership: Corporate only
│   ├── Contract: Green status only
│   ├── Barriers: Cardon excluded specifically
│   └── Source: Combined_Database_FINAL_V19_1_Enhanced.xlsx (created in Session 1)
│
└── SOM/SAM Level (Sheets 3-4)
    ├── Geographic: State lists (SOM: 6, SAM: 13)
    ├── Ownership: Corporate only
    ├── Barriers: Chain-level propagation (44 entities excluded)
    ├── Exclusions: "unknown" corporate names
    └── Source: Economic_Model_Scenario_2_Combined_V18.xlsx

          ↓

AGGREGATION
└── Group by Corporate_Name
    ├── Sum: Facilities, We_Serve, Integration, New_Biz, Total_Opportunity
    └── Sort: Descending by Total_Opportunity

          ↓

REPORT GENERATION
└── Top 75 entities (or Top 3 per metro for Sheet 1)
    ├── Format: Title case on corporate names and metros
    ├── Currency: Abbreviated ($12.2M, $950K style)
    └── Conversion scenarios: 10%, 15%, 20%
```

---

## Key Decisions & Logic

### 1. Barrier Propagation (Major Change)

**Previous Approach**: Exclude only facilities WITH barriers  
**New Approach**: Exclude ENTIRE corporate entity if ANY facility has a barrier

**Implementation**:
```python
# Identify all corporate entities with any barrier anywhere in database
has_barrier = s2['Barrier'].notna() & (s2['Barrier'] != '')
corps_with_barriers = set(barrier_facilities['Corporate_Name'].unique())

# Filter excludes entire chain
mask = ~df['Corporate_Name'].isin(corps_with_barriers)
```

**Impact**:
- 44 corporate entities with barriers identified
- CCH Healthcare was primary removal (20 "clean" facilities now excluded)
- SOM: -10 facilities, -$5.0M opportunity
- SAM: -3 facilities, -$2.3M opportunity

**Rationale**: If a corporate entity has barriers at some facilities, likely indicates chain-level relationship challenges

### 2. Metro Consolidation

**User Request**: Combine 4 separate metro tables into single consolidated view for slide deck

**Changes Made**:
- Removed metro subtotal rows
- Removed spacing between metros
- Created single continuous 12-row table
- Added Grand Total row
- Kept conversion scenarios at bottom

**Format Note**: Metro names in title case (Cleveland-Akron, not CLEVELAND-AKRON)

### 3. Metros Column Change (Sheet 2)

**Previous**: Listed all metros (e.g., "Cincinnati, Columbus, Evansville, Indianapolis...")  
**Current**: Show COUNT of metros (e.g., "7")

**Rationale**: Space savings for slide presentation

### 4. State Definitions

**SOM (Serviceable Obtainable Market)**:
- States: IN, KY, NC, OH, SC, VA
- Definition: Current 6-state operational footprint

**SAM (Serviceable Available Market)**:
- States: IN, KY, NC, OH, SC, VA + IA, MN, IL, MI, PA, WI, MD
- Definition: Existing + Priority expansion states
- **Note**: MD substituted for MT for this analysis only (not standard)

### 5. Entity Verification Findings

**User Question**: Why do Trilogy, Ciena, and Lionstone show "0 We Serve" in metro reports?

**Answer**: We DO serve these entities, but in RURAL markets only:
- **Trilogy**: 24 served (Bloomington IN, Greensburg IN, Lawrenceburg IN, Bedford IN, etc.) - all outside metro radius
- **Ciena**: 1 served (Hendersonville NC) - not in Charlotte metro
- **Lionstone**: 9 served (Jackson OH, Portsmouth OH, Mansfield OH, etc.) - all rural Ohio

**Implication**: These are expansion opportunities - existing relationships that could extend into metro footprints

---

## Technical Specifications

### Filter Chain Details

**SOM Filter Pipeline**:
1. All facilities: 21,023
2. State filter (IN, KY, NC, OH, SC, VA): 7,377
3. Corporate only: 3,585
4. Exclude corps with ANY barrier: 2,606
5. Exclude "unknown": 2,606
6. Aggregate to corporate entities: 432
7. Take top 75: 1,378 facilities, $502.6M opportunity

**SAM Filter Pipeline**:
1. All facilities: 21,023
2. State filter (13 states): 11,498
3. Corporate only: 5,768
4. Exclude corps with ANY barrier: 4,585
5. Exclude "unknown": 4,585
6. Aggregate to corporate entities: 662
7. Take top 75: 2,033 facilities, $858.0M opportunity

### Revenue Calculation

**Source**: Economic_Model_Scenario_2_Combined_V18.xlsx  
**Fee Structure**: Market +10% (S2)
- SNF Integrated: $5,041.85 per census
- ALF Integrated: $4,069.45 per census

**Revenue Types Used**:
- **Metro/SOM/SAM**: Total_Potential_Revenue (Integration + New Business)
- **State Expansion**: New_Business_Revenue only (all facilities are "not served")

**Formula**:
```
Total_Potential_Revenue = Integration_Revenue + New_Business_Revenue
```

### Corporate Entities with Barriers (44 total)

Key exclusions affecting SOM/SAM:
- Genesis Healthcare (215 facilities) - Own Provider Group
- Infinity Healthcare Consulting (107 facilities) - Alliance
- Communicare Health (122 facilities) - Own Provider Group
- ALG (65 facilities) - Competitor Agreement
- Embassy Healthcare (41 facilities) - Reputation
- Hill Valley Healthcare (40 facilities) - MH Only Opportunity
- Cardon & Associates (34 facilities) - Own Provider Group
- CCH Healthcare (40 facilities, 20 with barriers) - Reputation ← Primary SOM/SAM impact
- ... and 36 more

### Title Case Conversion

Applied to corporate names and metro names for professional presentation:
- TRILOGY HEALTH SERVICES → Trilogy Health Services
- CLEVELAND-AKRON → Cleveland-Akron
- CIENA HEALTHCARE/LAUREL HEALTH CARE → Ciena Healthcare/Laurel Health Care

**Exceptions**: Preserved acronyms (PACS, BHI, LLC, HCF, NHC)

### Currency Formatting

**Abbreviated Style**:
- $1,000,000+ → $1.0M
- $1,000+ → $1K
- Under $1,000 → $0

---

## State Expansion Analysis

### New State Opportunities Enhanced Table

**States Analyzed**: MI, PA, IA, IL, WI, MN, MD, SC, FL, GA

**New Columns Added**:
1. **Total Facilities** - All facilities (Corporate + Independent)
2. **Corporate Facilities** - Addressable market
3. **Potential Revenue** - New Business opportunity (Corporate, No Barriers, S2)

**Top 5 States by Revenue**:

| Rank | State | Corp Facilities | Potential Revenue |
|------|-------|----------------|-------------------|
| 1 | Pennsylvania | 670 | $305.4M |
| 2 | Florida | 547 | $288.8M |
| 3 | Illinois | 476 | $225.7M |
| 4 | Michigan | 300 | $130.8M |
| 5 | Georgia | 253 | $111.8M |

**Calculation**: 
- Filter: State, Corporate, No Barriers
- Sum: Total_Potential_Revenue from Scenario 2
- Since these are new states, all revenue is New Business (no current/integration)

---

## QC Validation Performed

### Validation Checkpoints

1. **Source File Integrity**:
   - Database: 21,023 facilities ✓
   - Scenario 2: 21,023 facilities ✓
   - Row counts match ✓

2. **Ownership Reconciliation**:
   - Corporate: 12,053
   - Independent: 8,970
   - Total: 21,023 ✓

3. **Revenue Formula Verification**:
   - Total Potential = Integration + New Business ✓
   - Calculations match at facility and aggregation level ✓

4. **Filter Chain Audit**:
   - Step-by-step counts documented ✓
   - SOM/SAM differences explained ✓

5. **Entity Spot-Check**:
   - Trilogy Health Services: 172 facilities, $37.8M (SOM) ✓
   - American Senior Communities: 150 facilities, $32.8M ✓
   - Foundations Health Solutions: 59 facilities, $25.9M ✓

6. **Barrier Propagation Impact**:
   - 44 entities with barriers identified ✓
   - CCH Healthcare removal verified ✓
   - Net impact: -$5.0M (SOM), -$2.3M (SAM) ✓

---

## Key Insights & Business Context

### Market Saturation Understanding

**Current Market Share** (from memory):
- Metro markets: Approaching realistic saturation (32% at ceiling of 35-45% for SNF, 20-30% for ALF)
- Rural markets: Significant runway remaining

**Strategic Implications**:
- Metro analysis focuses on priority targets where expansion is still viable
- SOM/SAM reports show broader opportunity across existing/priority states
- State expansion represents greenfield opportunities

### Corporate Strategy vs Field Operations

Two distinct growth channels:
1. **Corporate Strategy** (Sheets 1-4 focus): Contract negotiations at chain headquarters
2. **Field Operations**: Individual facility pursuit within assigned geographies (60-70% of growth)

These reports serve corporate strategy channel - identifying parent companies for relationship development.

### Existing Relationships as Expansion Levers

Key finding: Trilogy, Ciena, Lionstone serve as "bridge" opportunities:
- Current relationships in rural markets
- Metro presence exists but not yet served
- Could leverage existing corporate relationships for metro expansion

### Priority Market Focus

**12 Metro Markets**:
- Cleveland-Akron (350 facilities)
- Cincinnati (205)
- Indianapolis (202)
- Columbus (193)
- Louisville (150)
- Charlotte (133)
- Richmond (114)
- Toledo (83)
- Lexington (63)
- Northwest Indiana (61)
- Evansville (60)
- Harrisonburg-Charlottesville (53)

**Top 4 Priority Metros** (from Sheet 1):
1. Cleveland-Akron: $10.9M opportunity (26 facilities in top 3 corporates)
2. Indianapolis: $17.3M opportunity (59 facilities)
3. Columbus: $8.5M opportunity (19 facilities)
4. Cincinnati: $7.9M opportunity (16 facilities)

---

## Formatting Standards

### Excel Workbook Structure

**All sheets follow consistent formatting**:
- Title row: 14pt bold
- Subtitle row: 10pt italic
- Header row: 11pt bold white text on blue background (#4472C4)
- Data: 11pt regular
- Borders: Thin on all cells
- Grand Total: Light blue shading (#D9E2F3), bold
- Conversion scenarios: Below grand total with 2-row spacing

**Column Widths**:
- Rank: 6
- Corporate Entity: 35-38
- Metros count: 8
- Facilities/We Serve: 10
- Revenue columns: 12-18

**Alignments**:
- Text: Left (except metro names: center)
- Numbers: Center (counts) or Right (currency)
- Headers: Center

### Report Subtitles

- Sheet 1: "Top 3 Corporate Entities per Metro | Cardon Excluded (Barrier)"
- Sheet 2: "Ranked by Total Opportunity | All 12 Metros | Cardon Excluded (Barrier)"
- Sheet 3: "States: IN, KY, NC, OH, SC, VA | Corporate Only | Chain-Level Barrier Exclusion"
- Sheet 4: "States: IN, KY, NC, OH, SC, VA + IA, MN, IL, MI, PA, WI, MD | Corporate Only | Chain-Level Barrier Exclusion"

---

## Code Patterns for Continuation

### Loading Data
```python
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill

# Load source files
db = pd.read_excel('/mnt/project/Combined_Database_FINAL_V18.xlsx')
s2 = pd.read_excel('/mnt/project/Economic_Model_Scenario_2_Combined_V18.xlsx')
```

### Barrier Propagation Filter
```python
# Get all corporate entities with any barrier
has_barrier = s2['Barrier'].notna() & (s2['Barrier'] != '')
barrier_facilities = s2[has_barrier]
corps_with_barriers = set(barrier_facilities[
    (barrier_facilities['Corporate_Name'].notna()) & 
    (barrier_facilities['Corporate_Name'].str.lower() != 'unknown')
]['Corporate_Name'].unique())

# Apply filter
filtered = s2[
    (s2['State'].isin(STATE_LIST)) &
    (s2['Ownership_Type'] == 'Corporate') &
    (~s2['Corporate_Name'].isin(corps_with_barriers)) &
    (s2['Corporate_Name'].str.lower() != 'unknown') &
    (s2['Corporate_Name'].notna())
]
```

### Aggregation
```python
def aggregate_corporates(df):
    agg = df.groupby('Corporate_Name').agg({
        'Facility_Name': 'count',
        'Do_We_Serve': lambda x: (x == 'Yes').sum(),
        'Integration_Revenue': 'sum',
        'New_Business_Revenue': 'sum',
        'Total_Potential_Revenue': 'sum'
    }).rename(columns={
        'Facility_Name': 'Facilities',
        'Do_We_Serve': 'We_Serve',
        'Integration_Revenue': 'Integration',
        'New_Business_Revenue': 'New_Biz',
        'Total_Potential_Revenue': 'Total_Opportunity'
    })
    return agg.sort_values('Total_Opportunity', ascending=False).reset_index()
```

### Title Case Conversion
```python
def to_title_case(text):
    if pd.isna(text):
        return text
    text = str(text)
    result = text.title()
    # Preserve acronyms
    result = result.replace("'S", "'s")
    result = result.replace("Llc", "LLC")
    result = result.replace("Bhi", "BHI")
    result = result.replace("Hcf", "HCF")
    result = result.replace("Nhc", "NHC")
    result = result.replace("Pacs", "PACS")
    return result
```

### Currency Abbreviation
```python
def format_currency_abbreviated(value):
    if pd.isna(value) or value == 0:
        return "$0"
    if value >= 1_000_000:
        return f"${value/1_000_000:.1f}M"
    elif value >= 1_000:
        return f"${value/1_000:.0f}K"
    else:
        return f"${value:.0f}"
```

---

## Potential Next Steps

### Immediate Opportunities

1. **Individual Metro Deep Dives**
   - Detailed analysis of specific metros (e.g., Cleveland-Akron breakdown)
   - Facility-level listings with addresses for field operations
   - Geographic heat maps

2. **Corporate Entity Profiles**
   - Deep dive on top 10-20 targets
   - Facility locations and service gaps
   - Barrier analysis and mitigation strategies

3. **Integration vs New Business Split**
   - Separate targeting strategies for existing customers vs new logos
   - Cross-sell opportunity analysis

4. **State Expansion Prioritization**
   - Decision matrix using table factors
   - Phased market entry recommendations
   - Resource allocation modeling

### Advanced Analytics

5. **Conversion Scenario Modeling**
   - More sophisticated assumptions by corporate entity/metro
   - Historical conversion rate analysis
   - Risk-adjusted opportunity sizing

6. **Competitive Intelligence**
   - Overlay competitor presence data
   - Market share calculations by metro/state
   - Competitive positioning analysis

7. **Field Operations Integration**
   - Reconcile corporate strategy targets with field territory assignments
   - Avoid double-counting between channels
   - Unified pipeline management

8. **Version Control & Documentation**
   - Formalize V19 package with all deliverables
   - Update master rulebook with barrier propagation logic
   - Create executive presentation deck

---

## Important Context from Previous Work

### Session 1 Accomplishments (Reference: V19_Metro_Analysis_Handoff.md)

1. **Database Enhancement**
   - Applied 15-mile radius methodology from city centers
   - Created Metro_Assignment column
   - Generated Combined_Database_FINAL_V19_1_Enhanced.xlsx

2. **TAM/SAM/SOM/Metro Framework**
   - Established 4-level market segmentation
   - Metro level added as fourth tier below SOM

3. **Metro Analysis Outputs**
   - V19_Metro_TAM_SAM_SOM_Summary.xlsx
   - V19_Metro_Corporate_Opportunities.xlsx (13 sheets)
   - Original V19_Metro_Priority_Targets_Final_v2.xlsx

### V18 Foundation (Reference: V18_Phase_2_Complete.md)

**Database**: V17.1 with 21,023 facilities
- SNF: 15,234 (72.5%)
- ALF: 5,789 (27.5%)
- Corporate: 12,053 (57.3%)
- Independent: 8,970 (42.7%)

**Scenario 2 Revenue**: $7.63B Total Potential (all facilities)
- Current: $202.7M
- Integration: $142.2M
- New Business: $7.49B

**Fee Structure (S2 - Market +10%)**:
- SNF: $5,041.85 (PCP $3,385.80 + MH $666.05 + CCM $118.80 + SS $871.20)
- ALF: $4,069.45 (PCP $2,292.40 + MH $787.05 + CCM $118.80 + SS $871.20)

---

## Known Issues & Caveats

### Data Quality Notes

1. **"Unknown" Corporate Names**: 66 facilities in SOM states, 111 in SAM states with "unknown" as Corporate_Name - excluded from analysis

2. **Barrier Granularity**: Some entities have barriers on subset of facilities (like CCH Healthcare: 20/40), but barrier propagation logic excludes all facilities

3. **Geographic Tier**: Original Geographic_Tier column in V18 database was not metro-accurate; Session 1 corrected this with Metro_Assignment logic

4. **Maryland Substitution**: MD included in SAM for this analysis only; standard SAM includes MT per rulebook

5. **Contract Status**: Only applied to Metro analysis (Green only); SOM/SAM do not filter by contract status

### Technical Limitations

1. **Memory Constraint**: Current conversation at ~90% capacity; recommend fresh session for major new work

2. **Enhanced Database**: Combined_Database_FINAL_V19_1_Enhanced.xlsx created in Session 1 is NOT in project files; only used for Metro analysis (Sheets 1-2)

3. **Barrier List Currency**: 44 corporate entities with barriers current as of V18; may change as relationships evolve

4. **Census Data Age**: Census values in V18 database may be several months old; affects revenue calculations

### Analytical Boundaries

1. **Double-Counting Risk**: Corporate strategy targets (these reports) vs field operations targets should not be combined without reconciliation

2. **Conversion Rates**: 10%/15%/20% scenarios are illustrative; actual conversion rates vary by entity, market, service line

3. **Barrier Immutability**: Assumption that barriers are chain-level may be too conservative; some entities may have facility-specific barriers that could be mitigated

4. **Market Definitions**: SOM/SAM/Metro filters create nested but not hierarchical markets (facilities can be in SOM but not Metro due to different filters)

---

## File Dependencies

### Required Project Files
- Combined_Database_FINAL_V18.xlsx (21,023 facilities)
- Economic_Model_Scenario_2_Combined_V18.xlsx (21,023 facilities with revenue)
- Final_Model_Rulebook_V18.md (methodology reference)

### Optional Reference Files
- Economic_Model_Scenario_1_Combined_V18.xlsx (Conservative baseline)
- Economic_Model_Scenario_3_Combined_V18.xlsx (Premium +20%)
- Comprehensive_Report_Workbook_V18.xlsx (Standard 25-table report)
- QC_Validation_Workbook_V18.xlsx (Validation checks)

### Session 1 Artifacts (Not in Project)
- Combined_Database_FINAL_V19_1_Enhanced.xlsx (Metro_Assignment column)
- V19_Metro_TAM_SAM_SOM_Summary.xlsx
- V19_Metro_Corporate_Opportunities.xlsx

**Note**: Session 1 files may be needed to regenerate Sheets 1-2 with updated data

---

## User Preferences & Communication Style

### Established Patterns

1. **Lead Follow**: User prefers to lead conversation; Claude follows direction
2. **No Shortcuts**: User requests full analysis, not simplifications
3. **External References**: User wants notification when Claude introduces outside sources
4. **Precision**: Emphasis on accurate calculations and data integrity
5. **Documentation**: User values comprehensive handoff documents for continuity

### Project Terminology

- "Metro markets" = 12 specific metropolitan areas with 15-mile radius
- "SOM" = 6-state operational footprint
- "SAM" = 13-state serviceable market
- "Barrier propagation" = Chain-level exclusion logic
- "Integration opportunity" = Cross-sell to existing customers
- "New business" = Revenue from unserved facilities

---

## Quick Reference Commands

### To Continue This Analysis

**Load this handoff document**:
```
"I'm continuing the V19 Metro Priority Targets analysis. Please read the handoff document at V19_Metro_Priority_Targets_Handoff_Session2.md to get up to speed."
```

**Regenerate report with updated data**:
```python
# Load Session 2 final file as template
template = pd.ExcelFile('/mnt/user-data/outputs/V19_Metro_Priority_Targets_Final_v4.xlsx')

# Pull fresh data from project files
s2 = pd.read_excel('/mnt/project/Economic_Model_Scenario_2_Combined_V18.xlsx')

# Apply filters per documentation above
# Rebuild sheets 3-4 with current logic
```

**Add new state to SAM analysis**:
```python
# Update state list
SAM_STATES = ['IN', 'KY', 'NC', 'OH', 'SC', 'VA', 'IA', 'MN', 'IL', 'MI', 'PA', 'WI', 'MD', 'NEW_STATE']

# Re-run aggregation
# Update Sheet 4
```

---

## Contact Points for Clarification

### Questions to Ask User

1. **Barrier Approach**: Confirm chain-level propagation is desired vs facility-level exclusion
2. **State Definitions**: Confirm MD vs MT in standard SAM definition going forward
3. **Metro Updates**: If additional metros should be added to the 12 currently analyzed
4. **Version Control**: Whether V19 should be formalized as new major version or remain sub-version of V18
5. **Report Distribution**: Whether to create PowerPoint deck from Excel reports

### Data Validation Needs

1. **Brooke Contact**: Internal stakeholder for data quality validation (mentioned in memory)
2. **CRM Reconciliation**: Verify facility counts against operational systems
3. **Barrier Status**: Confirm current barrier entities list is accurate
4. **Census Updates**: Determine if census data needs refresh

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| V19_Metro_Priority_Targets_Final_v2.xlsx | Nov 24, 2025 | Original 4-table metro format (uploaded by user) |
| V19_Metro_Priority_Targets_Final_v3.xlsx | Nov 25, 2025 | Consolidated table, SOM/SAM added, facility-level barriers |
| **V19_Metro_Priority_Targets_Final_v4.xlsx** | **Nov 25, 2025** | **Chain-level barrier propagation applied** |
| V19_New_State_Opportunities_Enhanced.xlsx | Nov 25, 2025 | State expansion analysis |

---

## Success Metrics for This Analysis

**Metrics Tracking**:
- Total addressable opportunity quantified: **$1.5B+** (across all reports)
- Corporate targets prioritized: **75-200** entities depending on report level
- Geographic markets analyzed: **12 metros + 13 SAM states + 10 expansion states**
- Conversion scenarios modeled: **10%, 15%, 20%** for all reports

**Decision Support Enabled**:
- Board presentation ready (consolidated format)
- Business development prioritization (Top 75 lists)
- Resource allocation guidance (state expansion revenue)
- Risk assessment (barrier propagation impact)

---

**END OF HANDOFF DOCUMENT**

*Session 2 completed November 25, 2025*  
*Next session should reference this document for full context*  
*All deliverables in /mnt/user-data/outputs/*
