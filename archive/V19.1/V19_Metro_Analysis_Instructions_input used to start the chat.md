# V19 Metro Market Analysis - Instructions for Next Chat

**Date Created**: November 23, 2025  
**Purpose**: Complete metro market analysis on V19 database using Scenario 2  
**Expected Outputs**: 3 markdown reports + 12+ CSV files for Google Maps

---

## Files Provided

You have been given these files to work with:

1. **Combined_Database_FINAL_V19_1.xlsx** (or Combined_Database_FINAL_V19_1__1_.xlsx) - Source database (20,943 facilities)
2. **Economic_Model_Scenario_2_Combined_V19_1.xlsx** - Revenue calculations (use this, not Scenario 1)
3. **Fee_Schedule_Reference_V19_1.xlsx** - Fee structure
4. **Final_Model_Rulebook_V19_1.md** - Calculation methodology and rules

---

## Database Overview (V19)

- **Total Facilities**: 20,943
- **Metro Facilities (A_Metro in 6-state footprint)**: 1,756
- **Currently Served**: 1,663
- **Geographic Tiers**: A_Metro (1,766), B_Highway (1,289), C_Rural (17,875)

**Key Columns:**
- Source_Type (SNF/ALF)
- Ownership_Type (Corporate/Independent)
- Geographic_Tier (A_Metro/B_Highway/C_Rural)
- Do_We_Serve (Yes/No)
- Service Flags: Integrated_Flag, PCP_Flag, MH_Flag
- Barrier (blocks potential revenue)
- State, Corporate_Name, Census

---

## Three Required Analyses

### Analysis 1: 12 Metro Markets (Detailed + Rollup)

**Metros to Analyze** (same as V18):

**Ohio (4 metros):**
1. Cleveland-Akron
2. Cincinnati
3. Columbus
4. Toledo

**Indiana (3 metros):**
5. Indianapolis
6. Northwest Indiana (Gary-Hammond)
7. Evansville

**Kentucky (2 metros):**
8. Louisville
9. Lexington

**North Carolina (1 metro):**
10. Charlotte

**Virginia (2 metros):**
11. Richmond
12. Harrisonburg-Charlottesville

---

#### Metro Analysis Structure (Per Metro)

For EACH of the 12 metros, create a detailed analysis with:

**Section 1: Market Overview**
- Total facilities (SNF/ALF breakdown)
- Corporate vs Independent breakdown
- Currently served facilities
- Available facilities (no barriers, not served)
- Excluded facilities (barriers)

**Section 2: Market Segmentation Table**
```
| Market Segment | Facilities | % of Portfolio | Revenue | Status |
|----------------|------------|----------------|---------|--------|
| Current Customers | X | XX% | $X.XM | ✓ Already serving |
| Growth Opportunity | X | XX% | $X.XM | ► Available to pursue |
| Excluded (Barriers) | X | XX% | $X.XM | ✗ Permanently blocked |
| Total Metro | X | 100% | $X.XM | - |
```

**Section 3: Conversion Scenarios Table**
```
| Scenario | Conversion Rate | Facilities Won | Total Facilities | Market Share | Revenue Opportunity |
|----------|----------------|----------------|------------------|--------------|---------------------|
| Low | 15% | X | XXX | XX% | $X.XM |
| Medium | 20% | X | XXX | XX% | $X.XM |
| High | 25% | X | XXX | XX% | $X.XM |
| Industry Maximum | 35-40% | X-X | XXX-XXX | XX-XX% | $X.X-X.XM |
```

**Section 4: Top Corporate Opportunities**
- Top 10 corporate entities by Total Opportunity
- Include: Rank, Corporate Name, Total Facilities, Facilities We Serve, Current Revenue, Integration Opp, New Biz Opp, Total Opportunity

**Section 5: Saturation Analysis**
- Current penetration calculation
- Path to 35% saturation target
- Facilities needed to reach target

---

#### Rollup Summary Document

Create one combined summary showing all 12 metros:

**Table: All 12 Metros Combined**
```
| Metro | Current Customers | Growth Opportunity | Excluded (Barriers) | Total | Revenue Opportunity (Medium) |
|-------|-------------------|-------------------|---------------------|-------|------------------------------|
| Cleveland-Akron | X | X | X | X | $X.XM |
| Cincinnati | X | X | X | X | $X.XM |
[...all 12 metros...]
| TOTAL ALL METROS | XXX | XXX | XXX | XXX | $XX.XM |
```

**Conversion Scenarios for All Metros:**
```
| Scenario | Conversion Rate | Facilities Won | Total Facilities | Market Share | Revenue Opportunity |
|----------|----------------|----------------|------------------|--------------|---------------------|
| Low | 15% | +XX | XXX | XX% | $XX.XM |
| Medium | 20% | +XX | XXX | XX% | $XX.XM |
| High | 25% | +XX | XXX | XX% | $XX.XM |
```

---

### Analysis 2: Field Operations Metro Opportunity

**Target**: Integration cross-sell and independent facilities within the 12 metros

**Structure:**

**Executive Summary**
- Total addressable market (integration + independent)
- 3-year conversion scenarios (Conservative/Realistic/Optimistic)

**Channel 1: Integration Cross-Sell**

Market Segmentation Table:
```
| Customer Segment | Facilities | % of Served | Revenue Potential | Status |
|-----------------|------------|-------------|-------------------|--------|
| Integrated (Already Complete) | X | XX% | $0 | ✓ Already integrated |
| Integration Opportunity | X | XX% | $X.XM | ► Available to cross-sell |
| - MH-only → add PCP | X | XX% | $X.XM | Primary opportunity |
| - PCP-only → add MH | X | XX% | $X.XM | Secondary opportunity |
| Total Served Facilities | X | 100% | $X.XM | - |
```

Conversion Scenarios Table:
```
| Scenario | Conversion Rate | Facilities Won | Total Facilities Served | Market Share | Revenue Opportunity |
|----------|----------------|----------------|------------------------|--------------|---------------------|
| Conservative | 20% | XX | XXX | XX% | $X.XM |
| Realistic | 25% | XX | XXX | XX% | $X.XM |
| Optimistic | 30% | XX | XXX | XX% | $X.XM |
| Industry Maximum | 40-45% | XX-XX | XXX-XXX | XX-XX% | $X.X-X.XM |
```

**Channel 2: Independent Facilities (≥50 beds, metro markets)**

Market Segmentation Table:
```
| Market Segment | Facilities | % of Portfolio | Revenue Opportunity | Status |
|----------------|------------|----------------|---------------------|--------|
| Currently Served Independent | X | X% | $0 | ✓ Already serving |
| Growth Opportunity | X | XX% | $X.XM | ► Available to pursue |
| - SNF (≥50 beds) | X | XX% | $X.XM | $XXK avg/facility |
| - ALF (≥50 beds) | X | XX% | $X.XM | $XXK avg/facility |
| Total Large Independent Metro | X | 100% | $X.XM | - |
```

Conversion Scenarios Table:
```
| Scenario | Conversion Rate | Facilities Won | Total Facilities Served | Market Share | Revenue Opportunity |
|----------|----------------|----------------|------------------------|--------------|---------------------|
| Conservative | 10% | XX | XXX | XX% | $XX.XM |
| Realistic | 12.5% | XX | XXX | XX% | $XX.XM |
| Optimistic | 15% | XX | XXX | XX% | $XX.XM |
| Industry Maximum | 20-25% | XXX-XXX | XXX-XXX | XX-XX% | $XX.X-XX.XM |
```

**Combined Field Operations Summary Table:**
```
| Scenario | Integration Wins | Independent Wins | Total Facilities | Revenue Opportunity | Channel Breakdown |
|----------|------------------|------------------|------------------|---------------------|-------------------|
| Conservative | XX | XX | XXX | $XX.XM | Integration $X.XM + Independent $XX.XM |
| Realistic | XX | XX | XXX | $XX.XM | Integration $X.XM + Independent $XX.XM |
| Optimistic | XX | XX | XXX | $XX.XM | Integration $X.XM + Independent $XX.XM |
```

---

### Analysis 3: Tier B Off-Highway Geography

**Target**: Facilities along major transportation corridors (B_Highway geographic tier) within 6-state footprint

**Structure:**

**Market Overview**
- Total Tier B Highway facilities in footprint states (IN, KY, NC, OH, SC, VA)
- Currently served vs not served
- Available (no barriers)

**Market Segmentation Table:**
```
| Market Segment | Facilities | % of Tier B | Revenue Opportunity | Status |
|----------------|------------|-------------|---------------------|--------|
| Currently Served | X | XX% | $X.XM | ✓ Already serving |
| Growth Opportunity | X | XX% | $X.XM | ► Available to pursue |
| Excluded (Barriers) | X | XX% | $X.XM | ✗ Blocked |
| Total Tier B Highway | X | 100% | $X.XM | - |
```

**Geographic Distribution (by state):**
```
| State | Tier B Facilities | Addressable | Revenue Opportunity @ 10% | Notes |
|-------|------------------|-------------|--------------------------|-------|
| OH | XXX | XXX | $X.XM | Largest existing presence |
| NC | XXX | XXX | $X.XM | Strong metro presence |
[...all 6 states...]
```

**Conversion Scenarios (Tier B Only):**
```
| Scenario | Penetration Rate | Facilities Won | Total Served | Revenue Opportunity | Notes |
|----------|------------------|----------------|--------------|---------------------|-------|
| Conservative Pilot | 5% | XX | XXX | $X.XM | 2-3 facility clusters |
| Realistic | 10% | XXX | XXX | $XX.XM | 6-8 facility clusters |
| Optimistic | 15% | XXX | XXX | $XX.XM | Full Tier B activation |
```

**Rationale for Filters:**
- 5-15% penetration (vs 35-45% in metros) due to operational challenges
- Clustering requirement: 8-10 facilities within 60-min radius
- Telehealth-enabled hub model required

---

## Revenue Calculation Instructions

### Use Scenario 2 Data (IMPORTANT)

**DO NOT use Scenario 1 - use Economic_Model_Scenario_2_Combined_V19_1.xlsx**

**Revenue Components to Extract:**

1. **Current Revenue**: 
   - From Scenario 2 file: Sum revenue for facilities where Do_We_Serve = "Yes"
   - By service type (Integrated, PCP-only, MH-only)

2. **Integration Revenue**:
   - PCP-only facilities: Calculate potential MH add-on (Census × MH adjusted fee)
   - MH-only facilities: Calculate potential PCP add-on (Census × PCP fee)
   - Formula in Rulebook Section 4.4

3. **New Business Revenue**:
   - Not served, no barriers: Census × TOTAL fee (full integrated package)
   - Formula in Rulebook Section 4.5

**Refer to Final_Model_Rulebook_V19_1.md Section 4 for exact formulas**

---

## Google Maps CSV Files (CRITICAL OUTPUT)

Generate CSV files for each metro market to create Google Maps visualization layers.

### CSV Files Needed (12 metros × 4 layers = 48 files minimum)

**For EACH metro, create 4 CSV files:**

1. **{Metro}_Current_Customers.csv**
2. **{Metro}_Growth_Opportunity.csv**
3. **{Metro}_Excluded_Barriers.csv**
4. **{Metro}_Top_Corporate_Targets.csv**

### CSV Column Structure

**For Current Customers, Growth Opportunity, Excluded:**
```csv
Name,Latitude,Longitude,Address,City,State,ZIP,Ownership_Type,Source_Type,Census,Corporate_Name,Revenue,Service_Type
```

**For Top Corporate Targets:**
```csv
Corporate_Name,Facilities,Facilities_We_Serve,Total_Opportunity,Integration_Opp,New_Business_Opp,Primary_Metro,Facility_List
```

### Example CSV Structure

**Cleveland_Current_Customers.csv:**
```csv
Name,Latitude,Longitude,Address,City,State,ZIP,Ownership_Type,Source_Type,Census,Corporate_Name,Revenue,Service_Type
"Trilogy Care Center",41.4993,-81.6944,"123 Main St","Cleveland","OH",44101,"Corporate","SNF",95,"TRILOGY HEALTH SERVICES",$435000,"Integrated"
"Independent Manor",41.5234,-81.6789,"456 Oak Ave","Akron","OH",44301,"Independent","ALF",78,"",$145000,"PCP Only"
```

**Cleveland_Growth_Opportunity.csv:**
```csv
Name,Latitude,Longitude,Address,City,State,ZIP,Ownership_Type,Source_Type,Census,Corporate_Name,Potential_Revenue,Opportunity_Type
"Ciena Healthcare",41.4856,-81.7123,"789 Elm St","Cleveland","OH",44102,"Corporate","SNF",102,"CIENA HEALTHCARE",$467000,"New Business"
```

**Cleveland_Top_Corporate_Targets.csv:**
```csv
Corporate_Name,Facilities,Facilities_We_Serve,Total_Opportunity,Integration_Opp,New_Business_Opp,Primary_Metro,Facility_List
"CIENA HEALTHCARE",11,2,$5200000,$300000,$4900000,"Cleveland","Facility A; Facility B; Facility C..."
"TRILOGY HEALTH SERVICES",8,3,$3800000,$800000,$3000000,"Cleveland","Facility D; Facility E..."
```

### Layer-Specific Filtering Rules

**Layer 1: Current Customers**
- Filter: Do_We_Serve = "Yes"
- Color in Google Maps: Green
- Include: All served facilities regardless of service type

**Layer 2: Growth Opportunity**
- Filter: Do_We_Serve = "No" AND Barrier is NULL/empty
- Color in Google Maps: Blue
- Include: All addressable facilities

**Layer 3: Excluded (Barriers)**
- Filter: Barrier is NOT NULL
- Color in Google Maps: Red
- Include: All facilities with any barrier

**Layer 4: Top Corporate Targets**
- Filter: Top 10 corporate entities by Total Opportunity in this metro
- Color in Google Maps: Yellow
- Include: Corporate-level summary (not individual facilities)

### Additional CSV Files

**Tier_B_Highway_All_States.csv** (for Tier B analysis):
```csv
Name,Latitude,Longitude,Address,City,State,ZIP,County,Census,Corporate_Name,Source_Type,Ownership_Type,Potential_Revenue
```
- Filter: Geographic_Tier = "B_Highway" AND State IN ['IN','KY','NC','OH','SC','VA']

---

## Output File Naming Convention

**Markdown Reports:**
1. `V19_Metro_Analysis_Detailed_{Metro_Name}.md` (12 files)
2. `V19_Metro_Analysis_Rollup_Summary.md` (1 file)
3. `V19_Field_Operations_Metro_Opportunity.md` (1 file)
4. `V19_Tier_B_Off_Highway_Analysis.md` (1 file)

**CSV Files for Maps:**
1. `{Metro}_Current_Customers.csv` (12 files)
2. `{Metro}_Growth_Opportunity.csv` (12 files)
3. `{Metro}_Excluded_Barriers.csv` (12 files)
4. `{Metro}_Top_Corporate_Targets.csv` (12 files)
5. `Tier_B_Highway_All_States.csv` (1 file)

**Total Expected Files: 4 MD + 49 CSV = 53 files**

---

## Conversion Rate Assumptions

Use these standard conversion rates across all analyses:

**Metro Markets:**
- Low: 15%
- Medium: 20%
- High: 25%
- Industry Maximum: 35-40%

**Field Operations - Integration:**
- Conservative: 20%
- Realistic: 25%
- Optimistic: 30%
- Industry Maximum: 40-45%

**Field Operations - Independent:**
- Conservative: 10%
- Realistic: 12.5%
- Optimistic: 15%
- Industry Maximum: 20-25%

**Tier B Off-Highway:**
- Conservative Pilot: 5%
- Realistic: 10%
- Optimistic: 15%

---

## Reference Materials from V18

The user has completed this exact analysis on V18 data. Key reference documents in the project:

1. **Metro Analysis Example**: Look at previous metro analysis structure for Cleveland, Cincinnati, etc.
2. **Field Operations Structure**: See Field_Operations_Metro_Opportunity_V18.md for format
3. **Table Formats**: Use the two-table approach:
   - Table 1: Market Segmentation (universe breakdown)
   - Table 2: Conversion Scenarios (Low/Medium/High/Max with revenue calculations)

---

## Key Metrics to Track

**Across all analyses, ensure you calculate and report:**

1. **Total Facilities** (universe size)
2. **Currently Served** (existing customers)
3. **Growth Opportunity** (addressable, no barriers)
4. **Excluded** (barriers block revenue)
5. **Current Revenue** (from Scenario 2)
6. **Integration Revenue Opportunity** (cross-sell potential)
7. **New Business Revenue Opportunity** (new customer potential)
8. **Total Potential Revenue** (Integration + New Business)
9. **Market Share** (% penetration at each scenario)
10. **Facilities Won** (incremental count at each scenario)

---

## Critical Quality Checks

Before delivering outputs:

1. **Facility Count Reconciliation**: 
   - Sum of all metros should not exceed 1,756 total metro facilities
   - Current + Growth + Excluded should equal Total for each metro

2. **Revenue Validation**:
   - Current Revenue should come from Scenario 2 file
   - Integration + New Business should match Scenario 2 calculations
   - No negative revenue values

3. **Geographic Accuracy**:
   - All CSV files must have valid Latitude/Longitude
   - State abbreviations must be consistent (2-letter)

4. **CSV Format**:
   - Use UTF-8 encoding
   - Properly escape commas in facility names
   - Include headers in first row

5. **Conversion Math**:
   - Facilities Won should equal Growth Opportunity × Conversion Rate
   - Market Share should equal (Current + Facilities Won) / Total

---

## Analysis Workflow

**Step 1**: Load all four files (database, scenario 2, fee schedule, rulebook)

**Step 2**: For each of 12 metros:
- Filter database for metro facilities
- Extract current revenue from Scenario 2
- Calculate integration opportunity
- Calculate new business opportunity
- Generate conversion scenarios
- Create 4 CSV files
- Generate detailed markdown report

**Step 3**: Create rollup summary combining all 12 metros

**Step 4**: Analyze Field Operations opportunity across all metros:
- Integration cross-sell (served facilities)
- Independent facilities ≥50 beds

**Step 5**: Analyze Tier B Highway opportunity:
- Filter Geographic_Tier = "B_Highway"
- States: IN, KY, NC, OH, SC, VA
- Generate CSV for mapping

**Step 6**: Quality check all outputs

**Step 7**: Deliver 53 files to /mnt/user-data/outputs/

---

## Notes and Warnings

1. **Use Scenario 2, not Scenario 1** - This is critical for revenue accuracy
2. **Barrier logic**: Any facility with Barrier populated (not NULL) should be excluded from Growth Opportunity
3. **Corporate Name handling**: Empty or "INDEPENDENT" in Corporate_Name = Independent ownership
4. **Census weighting**: All revenue calculations must use Census field, not Total_Beds
5. **Geographic filtering**: Use Geographic_Tier = "A_Metro" for metro analysis, not city names
6. **Independent facilities**: For Field Ops Channel 2, filter Census ≥ 50 beds

---

## Expected Timeline

This is a substantial analysis. Expected completion:
- **12 Metro Detailed Reports**: 45-60 minutes
- **Rollup Summary**: 10 minutes
- **Field Operations**: 15 minutes
- **Tier B Analysis**: 10 minutes
- **49 CSV Files**: 30 minutes
- **Quality Checks**: 15 minutes

**Total: ~2-2.5 hours of analysis and generation**

---

## Questions to Ask User Before Starting

1. Are all 12 metros the same as V18 analysis, or any changes?
2. Should independent facilities in metros be included in Growth Opportunity or excluded?
3. What revenue year does Scenario 2 represent (for documentation)?
4. Any specific corporate entities to highlight in rankings?

---

**END OF INSTRUCTIONS**

When you complete this analysis, notify the user that all 53 files are ready in `/mnt/user-data/outputs/` and provide links to the 4 main markdown reports for review.
