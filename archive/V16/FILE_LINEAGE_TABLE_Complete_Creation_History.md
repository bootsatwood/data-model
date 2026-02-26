# File Lineage Table - Complete Creation History
## All Files Created in This Conversation with Dependencies and Connections
### Chronological Order with Discussion Context

---

## FILE CREATION LINEAGE

| Order | File Created | Triggered By | Input Dependencies | Purpose/Connection | Key Output |
|-------|-------------|--------------|-------------------|-------------------|------------|
| **1** | Combined_Database_FINAL_V16.xlsx | Need to match $29.3M email target | • Combined_Database_FINAL_V15.xlsx<br>• Book1.xlsx (Contract Status) | Enhanced database with Contract_Status and Geographic_Tier columns to enable filtering | 17,434 facilities with new strategic flags |
| **2** | Integration_L0_All_Served.csv (+ 7 more) | Need to show layer progression | Combined_Database_FINAL_V16.xlsx | Show how 1,743 served facilities filter down to 117 Tier A facilities | Integration layer files (not separated) |
| **3** | NewBusiness_L1_Not_Served.csv (+ 5 more) | Complete two-story approach | Combined_Database_FINAL_V16.xlsx | Show new business opportunity filtering from 3,539 to 259 facilities | New Business layer files (not separated) |
| **4** | Integration_Funnel_Compendium_V16.md | Document exact path to $29.3M | Layer analysis from #2 | Comprehensive table showing each filter's impact on revenue | L0: $187.7M → L6: $23.6M breakdown |
| **5** | Geographic_Layer_Strategy_V16_Executive_Summary.md | Need executive overview | Analysis from #2-4 | High-level two-story summary with conservative approach | Integration + New Business strategy |
| **6** | SNF_Integration_L0_All_Served.csv (+ 27 more) | "Need different pins for SNF/ALF" | Original layer files #2-3 | Separated files by facility type for Google Maps visualization | 28 files: 16 Integration + 12 New Business |
| **7** | New_Business_First_Strategy_V16.md | "Don't count on M&A" pivot | Revenue analysis | Reframe strategy with New Business as primary (not M&A dependent) | 84% from New Biz, 12% Integration, 4% Retention |
| **8** | High_Level_Revenue_Math_20_Percent_Growth.md | "Show math for 20% growth minus 9% erosion" | Strategy from #7 | Calculate $51.5M gap and how three strategies fill it | $177.7M → $213.2M path |
| **9** | Revenue_Math_Range_Analysis_177M_to_194M.md | "What if revenue is $177M-194M range?" | Math from #8 | Scenario analysis showing strategy works across range | Gap ranges from $51.3M to $56.3M |
| **10** | Geographic_Sales_Tier_Alignment_Strategy.md | "Connect to sales tiers (Infill/Edge/Whale)" | Geographic analysis + Sales goals | Show how geographic findings support 14,500 bed target | OH+NC = 15,492 beds for 5,000 target |
| **11** | Strategic_Tables_Revenue_Enhanced_V16.md | "Add revenue to all tables" | Previous strategic tables | Enhanced tables with complete revenue calculations | Tables 1-6 with revenue impact |
| **12** | Complete_19_Metro_Focus_Allocation_Table.md | "Show all 19 metros individually" | Metro analysis | Detailed breakdown of all 19 metros (not collapsed) | Indianapolis #1 at $26.1M |
| **13** | Metro_Centers_19_GPS_Coordinates.csv | "Need GPS for 19 metro centers" | Geographic definitions | CSV with lat/long for Google Maps metro circles | 19 rows with coordinates |
| **14** | Metro_Region_Layer_Progression_Focus_Table.md | "Show layer math by metro" | Database V16 + Layer logic | How each metro filters through L1→L6 progression | Cleveland 20% conversion, Indy 11% |
| **15** | KPI_by_Metro_Detailed_Win_Rates_Revenue_All_19.md | "Need win rates by metro for all strategies" | Metro analysis + Revenue targets | Detailed KPIs showing required win rates and dollar amounts | Integration 37%, New Biz 28%, Retention 73% |
| **16** | Simple_Metro_51M_Target_Breakdown.md | "Simple table to show $51M breakdown" | All previous analysis | Clean summary showing how metros ladder to target | $56.9M available vs $51.5M needed |
| **17** | CONVERSATION_SUMMARY_AND_FILE_INDEX.md | "Create summary for next conversation" | Entire conversation | Complete handoff document with file index | Full conversation summary with file versions |

---

## FILE DEPENDENCY TREE

```
Combined_Database_FINAL_V15.xlsx (incoming)
    ↓
    + Book1.xlsx (Contract Status)
    ↓
Combined_Database_FINAL_V16.xlsx ← [ENHANCEMENT POINT]
    ↓
    ├── Layer CSV Files (Original - 14 files)
    │   ├── Integration_L0-L7 (8 files)
    │   └── NewBusiness_L1-L6 (6 files)
    │       ↓
    │       └── Separated SNF/ALF Files (28 files)
    │
    ├── Strategic Documents
    │   ├── Integration_Funnel_Compendium_V16.md
    │   ├── New_Business_First_Strategy_V16.md
    │   └── Geographic_Layer_Strategy_V16.md
    │
    ├── Revenue Analysis
    │   ├── High_Level_Revenue_Math_20_Percent_Growth.md
    │   └── Revenue_Math_Range_Analysis_177M_to_194M.md
    │
    └── Metro Analysis
        ├── Complete_19_Metro_Focus_Allocation_Table.md
        ├── Metro_Region_Layer_Progression_Focus_Table.md
        ├── KPI_by_Metro_Detailed_Win_Rates_Revenue_All_19.md
        ├── Simple_Metro_51M_Target_Breakdown.md
        └── Metro_Centers_19_GPS_Coordinates.csv
```

---

## DISCUSSION FLOW → FILE CREATION

### Phase 1: Problem Definition & Database Enhancement
**Discussion**: "How do we match the email's $29.3M?"
- Created: Enhanced Database V16
- Added: Contract Status and Geographic Tiers

### Phase 2: Geographic Filtering & Visualization
**Discussion**: "Show the layer progression"
- Created: 14 initial layer files
- Created: Integration Funnel Compendium
- Later: Separated into 28 SNF/ALF files

### Phase 3: Strategic Pivot
**Discussion**: "Don't count on M&A, make New Business primary"
- Created: New Business First Strategy
- Created: Revenue Math documents

### Phase 4: Sales Alignment
**Discussion**: "Connect to sales tiers (Infill/Edge/Whale)"
- Created: Geographic Sales Tier Alignment
- Created: Strategic Tables with Revenue

### Phase 5: Metro Deep Dive
**Discussion**: "Show all 19 metros with details"
- Created: Complete 19-Metro Table
- Created: Metro GPS Coordinates
- Created: Layer Progression by Metro
- Created: KPIs by Metro

### Phase 6: Simplification
**Discussion**: "Just show simple path to $51M"
- Created: Simple Metro Breakdown
- Created: Conversation Summary

---

## KEY FILE RELATIONSHIPS

### Core Transformation
`V15 Database + Book1 → V16 Database` (Added 4 critical columns)

### Layer Story Files
`V16 Database → 14 Layer CSVs → 28 Separated CSVs` (For mapping)

### Strategic Evolution
`Integration Focus → New Business First → Three-Pronged Strategy`

### Metro Analysis Suite
`19 Metros → Focus Allocation → Layer Math → KPIs → Simple Summary`

---

## VERSION CONTROL NOTES

### Superseded Files
- Combined_Database_FINAL_V15.xlsx → Replaced by V16

### Current/Active Files
- All 17 created documents (listed above)
- All 28 separated CSV files
- Combined_Database_FINAL_V16.xlsx

### External Dependencies (Referenced but not modified)
- Final_Model_Rulebook_V12.md (fee structures)
- START_HERE_V12.md (project guide)
- Book1.xlsx (source for Contract Status)

---

## CRITICAL INSIGHTS FROM LINEAGE

1. **The V16 database is the foundation** - Everything flows from this enhancement
2. **Layer files evolved twice** - First combined (14), then separated by type (28)
3. **Strategy pivoted mid-conversation** - From Integration-first to New Business-first
4. **Metro analysis deepened progressively** - From summary to detailed KPIs
5. **Simplification came last** - Complex analysis preceded simple summary

---

**Total Files Created**: 46
- 1 Enhanced Database
- 17 Strategic Documents
- 28 CSV Layer Files

**Most Important File**: Combined_Database_FINAL_V16.xlsx (everything depends on it)
**Best Summary File**: Simple_Metro_51M_Target_Breakdown.md (bottom line)
**Best Handoff File**: CONVERSATION_SUMMARY_AND_FILE_INDEX.md (complete context)

---

END OF FILE LINEAGE TABLE
