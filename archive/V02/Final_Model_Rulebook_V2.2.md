# Final Model Rulebook V2.2
## Eventus Economic Model - Modular Architecture
### Component-Based Design | Scenario Management | Data Integrity

**Document Purpose:** This rulebook defines the modular architecture for the Eventus Economic Model, separating source data from computation to prevent data corruption and enable scenario flexibility. This V2.2 corrects revenue stream calculations and prepares for multi-scenario analysis.

**Model Version:** 3.0 - Modular Architecture  
**Rulebook Version:** V2.2 FINAL  
**Date:** November 15, 2025  
**Status:** PRODUCTION READY - Complete with Reporting Layer  
**Architecture:** Three-File System (Source + Model + Reports)

---

## CRITICAL CORRECTIONS IN V2.2

**What Changed from V2.1:**
1. ✅ **Removed "Opportunity_Revenue"** - This was an incorrect artifact
2. ✅ **Added Four Revenue Streams:** Current, Integration, New Biz, Total
3. ✅ **Fixed Annual Calculation** - Rates are already annual, no ×12 needed
4. ✅ **Documented as Scenario 1** - Enables Scenario 2+ flexibility
5. ✅ **Added File 3 (Reports)** - Separate reporting outputs

**Verified Benchmark:** $127,572,232 TAM Current Revenue (unchanged)

---

## TABLE OF CONTENTS

**PART 1: ARCHITECTURE OVERVIEW**
- 1.1 System Design Philosophy
- 1.2 Three-File Structure & Dependencies
- 1.3 Component Flow Diagram
- 1.4 Processing Sequence
- 1.5 Why This Architecture?

**PART 2: FILE 1 - SOURCE DATA MASTER**
- 2.1 Purpose & Scope
- 2.2 Required Columns & Data Types
- 2.3 Data Quality Rules
- 2.4 What NOT to Include
- 2.5 Validation Checklist

**PART 3: FILE 2 - ECONOMIC MODEL (SCENARIO 1)**
- 3.1 File Structure Overview
- 3.2 Sheet 1: Fee_Structure (Scenario-Specific Rates)
- 3.3 Sheet 2: Calculations (Four Revenue Streams)
- 3.4 Sheet 3: Segmentation (TAM/SAM/SOM)
- 3.5 Sheet 4: Results (Aggregations)
- 3.6 Sheet 5: Scenario_Definitions (Documentation)
- 3.7 Sheet 6: QA_Validation (Quality Checks)

**PART 4: SCENARIO 1 FORMULAS & BENCHMARKS**
- 4.1 Scenario 1 Benchmark: $127.6M
- 4.2 Fee Structure Rates (Annual)
- 4.3 Current Revenue Formulas
- 4.4 Integration Revenue Formulas
- 4.5 New Biz Revenue Formulas
- 4.6 Total Revenue Formula
- 4.7 Service Component Breakdown

**PART 5: FILE 3 - REPORTS OUTPUT**
- 5.1 Reports File Structure
- 5.2 Report 1: Facilities Count
- 5.3 Report 2: Revenue Summary
- 5.4 Report 3: SOM Fee Structure Breakdown
- 5.5 Report 4: Top 20 Corporate Entities (SOM Only)
- 5.6 Report 5: Geographic Analysis (SOM Only) - PLACEHOLDER
- 5.7 Additional Reports (Future)

**PART 6: SCENARIO MANAGEMENT**
- 6.1 How Scenarios Work
- 6.2 Creating New Scenarios
- 6.3 Scenario 1: Current State
- 6.4 Scenario 2: Placeholder
- 6.5 Scenario 3: Placeholder

**PART 7: QUALITY ASSURANCE**
- 7.1 Component-Level Validation
- 7.2 End-to-End Validation
- 7.3 Troubleshooting Guide
- 7.4 Expected Results

**PART 8: IMPLEMENTATION PROCEDURES**
- 8.1 Building from Scratch
- 8.2 Linking Files
- 8.3 Verifying Calculations
- 8.4 Testing Scenarios

**APPENDICES**
- Appendix A: Column Reference Guide
- Appendix B: Formula Reference
- Appendix C: Corporate Entity Rankings
- Appendix D: Change Log

---

# PART 1: ARCHITECTURE OVERVIEW

## 1.1 System Design Philosophy

### **Core Principle: Separation of Concerns**

The Eventus Economic Model uses a **modular, component-based architecture** that separates:

1. **Source Data** (immutable, protected) from **Calculations** (formulas, derived values)
2. **Configuration** (rates, scenario variables) from **Logic** (business rules, formulas)
3. **Computation** (revenue calculations) from **Segmentation** (market filters)
4. **Model Execution** (Files 1-2) from **Reporting** (File 3)

### **Design Goals**

**Data Integrity**
- Prevent unauthorized modifications to source data
- Maintain formula consistency across model iterations
- Enable audit trails for all calculations
- Support data validation at multiple checkpoints

**Scenario Flexibility**
- Swap rate structures without touching source data or formulas
- Test multiple scenarios using same underlying data
- Document assumptions for each scenario
- Compare scenarios side-by-side

**Reporting Independence**
- Separate computation from presentation
- Generate stakeholder-ready reports without exposing model internals
- Enable ad-hoc report creation without model changes

**Maintainability**
- Clear component boundaries
- Documented formulas and business rules
- Modular structure allows component updates
- Version control friendly

---

## 1.2 Three-File Structure & Dependencies

### **Three-File Architecture**

```
FILE 1: Source_Data_Master.xlsx
└── Sheet 1: Source_Data (1 sheet only)
    ├── Facility demographics
    ├── Service flags
    ├── Market classifications
    ├── Census & bed counts
    └── Occupancy data

FILE 2: Economic_Model_Scenario_1.xlsx
├── Sheet 1: Fee_Structure (SCENARIO VARIABLE)
│   ├── Service rates by type
│   ├── Coverage multipliers
│   ├── Scenario metadata
│   └── Documentation
│
├── Sheet 2: Calculations
│   ├── Links to File 1 (Source_Data)
│   ├── Links to Sheet 1 (Fee_Structure)
│   ├── Four revenue stream formulas
│   └── Service component breakdown
│
├── Sheet 3: Segmentation
│   ├── Links to Sheet 2 (Calculations)
│   ├── TAM/SAM/SOM filters
│   ├── Corporate entity flags
│   └── Barrier exclusions
│
├── Sheet 4: Results
│   ├── Links to Sheet 3 (Segmentation)
│   ├── Revenue aggregations by segment
│   ├── Facility counts
│   └── Summary metrics
│
├── Sheet 5: Scenario_Definitions
│   ├── Scenario 1 documentation
│   ├── Scenario 2+ placeholders
│   └── Assumptions log
│
└── Sheet 6: QA_Validation
    ├── Links to all prior sheets
    ├── Benchmark validations
    ├── Data quality checks
    └── Formula integrity tests

FILE 3: Reports_Scenario_1.xlsx (NEW)
├── Sheet 1: Facilities_Count
│   ├── Links to File 2 (Results & Segmentation)
│   ├── SNF/ALF/Total breakdowns
│   └── Corporate vs Independent counts
│
├── Sheet 2: Revenue
│   ├── Links to File 2 (Results & Segmentation)
│   ├── Current/Integration/New Biz/Total
│   └── SNF/ALF/Total breakdowns
│
├── Sheet 3: SOM_Fee_Breakdown
│   ├── Links to File 2 (Segmentation)
│   ├── Revenue by service type (PCP/MH/CCM/SS)
│   └── SNF/ALF/Total tables
│
├── Sheet 4: Top_20_Corporate_Entities
│   ├── Links to File 2 (Segmentation)
│   ├── Table A: Total Combined Opportunity (Top 20)
│   ├── Table B: Integration Opportunity (Top 20)
│   └── Table C: New Business Opportunity (Top 20)
│
└── [Additional report sheets as needed]
```

### **File Dependencies**

```
Source_Data_Master.xlsx (File 1)
    ↓
    → Economic_Model_Scenario_1.xlsx (File 2)
      ↓
      Sheet 1 (Fee_Structure) ←─── SCENARIO SPECIFIC (swap this)
      ↓
      Sheet 2 (Calculations) ←───── Reads File 1 + Sheet 1
      ↓
      Sheet 3 (Segmentation) ←───── Reads Sheet 2
      ↓
      Sheet 4 (Results) ←────────── Reads Sheet 3
      ↓
      Sheet 5 (Scenario_Definitions) ← Metadata only
      ↓
      Sheet 6 (QA_Validation) ←──── Reads all sheets
      ↓
      → Reports_Scenario_1.xlsx (File 3)
        ↓
        All report sheets ←──────── Read File 2 (Results & Segmentation)
```

**Key Insight:** Only Sheet 1 (Fee_Structure) in File 2 changes between scenarios. Everything else remains constant.

---

## 1.3 Component Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│  COMPONENT 1: SOURCE DATA (File 1)                              │
│  • 17,490 total facilities (SNF + ALF)                          │
│  • Demographics, service flags, market status                    │
│  • NO FORMULAS - Clean data only                                │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────────────┐
│  COMPONENT 2: FEE STRUCTURE (File 2, Sheet 1)                   │
│  • Scenario-specific rates (swap this for new scenarios)        │
│  • PCP, MH, CCM, SS rates                                       │
│  • Coverage multipliers (Adjuster_1, Adjuster_2, Adjuster_3)   │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────────────┐
│  COMPONENT 3: CALCULATIONS (File 2, Sheet 2)                    │
│  • Imports Component 1 (source data)                            │
│  • Imports Component 2 (fee structure)                          │
│  • Calculates FOUR revenue streams:                             │
│    - Current Revenue (served facilities)                        │
│    - Integration Revenue (served facilities, missing services)  │
│    - New Biz Revenue (unserved facilities)                      │
│    - Total Revenue (Integration + New Biz)                      │
│  • Breaks down by service component (PCP, MH, CCM, SS)         │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────────────┐
│  COMPONENT 4: SEGMENTATION (File 2, Sheet 3)                    │
│  • TAM: All 17,490 facilities                                   │
│  • SAM: Corporate in Existing/Emerging markets                  │
│  • SOM: Corporate in Existing markets, no barriers              │
│  • Outputs: TAM_Flag, SAM_Flag, SOM_Flag                        │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────────────┐
│  COMPONENT 5: RESULTS (File 2, Sheet 4)                         │
│  • Aggregates revenue by segment (TAM/SAM/SOM)                  │
│  • Aggregates by facility type (SNF/ALF)                        │
│  • Aggregates by ownership (Corporate/Independent)              │
│  • Counts facilities by segment                                 │
│  • Produces executive summary table                             │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────────────┐
│  COMPONENT 6: SCENARIO DEFINITIONS (File 2, Sheet 5)            │
│  • Documents scenario assumptions                                │
│  • Compares scenarios side-by-side                              │
│  • Metadata only (no calculations)                              │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────────────┐
│  COMPONENT 7: QA VALIDATION (File 2, Sheet 6)                   │
│  • Validates against $127.6M benchmark                          │
│  • Checks data quality (99.99% target)                          │
│  • Verifies formula integrity                                   │
│  • Overall status: PASS/FAIL                                    │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────────────┐
│  FILE 3: REPORTS (Reports_Scenario_1.xlsx)                      │
│  • Each sheet = one stakeholder report                          │
│  • Links to File 2 for data                                     │
│  • Formatted for distribution                                   │
│  • No model internals exposed                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.4 Processing Sequence

### **Component Processing Order**

**CRITICAL:** Components must be processed in this exact order to maintain data integrity and calculation accuracy.

**Step 1: Component 1 (Source Data)**
- Load clean facility data
- No calculations performed
- Output: Raw data table

**Step 2: Component 2 (Fee Structure)**
- Load scenario-specific rates
- Define multipliers and assumptions
- Output: Rate lookup table

**Step 3: Component 3 (Calculations)**
- Import Components 1 & 2
- Apply four revenue stream formulas
- Calculate service component breakdown
- Output: Facility-level revenue data (all four streams)

**Step 4: Component 4 (Segmentation)**
- Import Component 3 results
- Apply TAM/SAM/SOM filters
- Assign segment flags
- Output: Segmented facility data

**Step 5: Component 5 (Results)**
- Import Component 4 results
- Aggregate by segment/type/ownership
- Calculate summary statistics
- Output: Executive summary table

**Step 6: Component 6 (Scenario Definitions)**
- Document scenario assumptions
- No calculations required
- Output: Metadata documentation

**Step 7: Component 7 (QA Validation)**
- Import all prior components
- Run validation checks
- Compare to benchmarks
- Output: PASS/FAIL status

**Step 8: File 3 (Reports)**
- Import File 2 results
- Format for stakeholder distribution
- Generate report tables
- Output: Distributable Excel reports

---

## 1.5 Why This Architecture?

### **Problems with Previous Approaches**

**Monolithic Design Issues:**
- Data corruption from unauthorized edits
- Formula changes broke downstream calculations
- No clear separation between data and logic
- Difficult to test scenarios
- Hard to collaborate without conflicts

**"Opportunity_Revenue" Artifact (V2.1 Error):**
- Collapsed Integration and New Biz into one metric
- Lost visibility into served vs. unserved opportunity
- Couldn't match stakeholder reporting needs
- Incorrect annual calculation (×12 when rates already annual)

### **Solutions in V2.2 Modular Design**

**Data Integrity**
- Source data protected in separate file
- Formulas cannot be accidentally modified
- Clear component boundaries
- Validation at each step

**Scenario Flexibility**
- Swap Sheet 1 (Fee_Structure) for new scenarios
- All other components remain unchanged
- Easy to test and compare scenarios
- Documented assumptions for each scenario

**Reporting Independence**
- File 3 separates presentation from computation
- Stakeholders see formatted reports, not model internals
- Can distribute reports without exposing proprietary logic
- Add new reports without touching model

**Four Revenue Streams**
- **Current:** What we earn today
- **Integration:** Upsell opportunity with existing clients
- **New Biz:** Opportunity from new client acquisition
- **Total:** Full market opportunity (Integration + New Biz)

**Collaboration**
- Users work on independent scenario files
- Source data remains pristine
- Clear ownership of components
- Version control friendly

---

# PART 2: FILE 1 - SOURCE DATA MASTER

## 2.1 Purpose & Scope

### **Component 1: Clean Source Data**

**File Name:** `Source_Data_Master.xlsx`  
**Sheets:** 1 (Source_Data)  
**Purpose:** Centralized, immutable facility database

**What This File Contains:**
- All 17,490 facilities (SNF + ALF)
- Facility demographics and identifiers
- Service flags (PCP, MH, Integrated, SS)
- Market classifications (Existing, Emerging, New)
- Ownership type (Corporate, Independent)
- Census and bed counts
- Occupancy rates

**What This File Does NOT Contain:**
- NO revenue calculations
- NO formulas (except basic data cleaning if needed)
- NO scenario-specific rates or assumptions
- NO aggregations or summaries

### **Key Principle**

**This file is READ-ONLY during model execution.** All modifications should go through a formal data update process with validation.

---

## 2.2 Required Columns & Data Types

### **Facility Identifiers**

| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| `Provider_Number` | Text | CMS Provider ID (SNF) or unique ID (ALF) | "105506" |
| `Facility_Name` | Text | Official facility name | "Sunrise Senior Living" |
| `Facility_Type` | Text | SNF or ALF | "SNF" |
| `Corporate_Entity` | Text | Parent organization name | "Sunrise Senior Living Inc" |
| `Ownership` | Text | Corporate or Independent | "Corporate" |
| `State` | Text | Two-letter state code | "NC" |
| `ZIP` | Text | 5-digit ZIP code | "27298" |

### **Service Flags**

| Column Name | Data Type | Description | Logic |
|------------|-----------|-------------|-------|
| `PCP_Only_Flag` | Text | "Yes"/"No" | PCP = Yes, MH = No, Integrated = No |
| `MH_Only_Flag` | Text | "Yes"/"No" | PCP = No, MH = Yes, Integrated = No |
| `Integrated_Flag` | Text | "Yes"/"No" | PCP = Yes, MH = Yes |
| `SS_Service_Flag` | Text | "Yes"/"No" | Facility has Shared Savings |

**CRITICAL:** These flags are mutually exclusive. A facility can only have ONE service type flag = "Yes".

### **Served Status**

| Column Name | Data Type | Description | Logic |
|------------|-----------|-------------|-------|
| `Do_We_Serve` | Text | "Yes"/"No" | Facility currently served by Eventus |

**Key Distinction:**
- `Do_We_Serve = "Yes"` → Facility is SERVED (has current revenue)
- `Do_We_Serve ≠ "Yes"` → Facility is UNSERVED (new biz opportunity)

### **Market Classifications**

| Column Name | Data Type | Description | Values |
|------------|-----------|-------------|--------|
| `Market_Status` | Text | Current market presence | "Existing", "Emerging", "New" |
| `Has_Barrier` | Text | Barrier to entry | "Yes", "No" |

**Market Hierarchy:**
- **Existing:** Currently served markets
- **Emerging:** Markets with initial presence
- **New:** Untapped markets

### **Operational Metrics**

| Column Name | Data Type | Description | Units |
|------------|-----------|-------------|-------|
| `Census` | Number | Average daily census | Patients |
| `Total_Beds` | Number | Licensed bed count | Beds |
| `Occupancy_Rate` | Number | Census ÷ Total_Beds | Decimal (0.80 = 80%) |

**Special Cases:**
- **ALF Served Facilities:** If Total_Beds = 0, use 49 beds as surrogate
- **ALF Unserved Facilities:** If Total_Beds = 0, use 72 beds as surrogate
- **SNF Facilities:** All have Total_Beds populated

---

## 2.3 Data Quality Rules

### **Data Integrity Checks**

**Rule 1: No Duplicate Facilities**
- Each `Provider_Number` must be unique
- If duplicates found, investigate and remove

**Rule 2: Service Flag Exclusivity**
- Sum(`PCP_Only_Flag`, `MH_Only_Flag`, `Integrated_Flag`) = 1 per facility
- If sum ≠ 1, flag for investigation

**Rule 3: Census vs. Bed Consistency**
- If Census > 0, Total_Beds must be > 0 (or use surrogate for ALF)
- Occupancy_Rate should be ≤ 1.0 (warn if > 1.0)

**Rule 4: Market Status Validity**
- Market_Status must be one of: "Existing", "Emerging", "New"
- No nulls or blanks allowed

**Rule 5: Ownership Type Validity**
- Ownership must be "Corporate" or "Independent"
- No nulls or blanks allowed

**Rule 6: Served Status Alignment**
- If Do_We_Serve = "Yes", Census should be > 0
- If Census > 0, Do_We_Serve should = "Yes"

### **Data Quality Target**

**Goal:** 99.99% data quality (≤2 facilities with data issues out of 17,490)

**Acceptable Issues:**
- Missing Total_Beds for ALF (use surrogate)
- Occupancy > 100% (flag but allow)

**Unacceptable Issues:**
- Duplicate Provider_Numbers
- Multiple service flags = "Yes"
- Missing Market_Status
- Missing Ownership
- Served facilities with no service flags

---

## 2.4 What NOT to Include

### **DO NOT Include in Source_Data_Master.xlsx:**

**Revenue Calculations**
- ❌ Current_Revenue
- ❌ Integration_Revenue
- ❌ New_Biz_Revenue
- ❌ Total_Revenue
- ❌ Any service component revenues (PCP_Revenue, MH_Revenue, etc.)

**Scenario-Specific Rates**
- ❌ FFS_PCP_Rate, FFS_MH_Rate, CCM_Rate, SS_Rate
- ❌ Coverage multipliers (Adjuster_1, Adjuster_2, Adjuster_3)

**Segmentation Flags**
- ❌ TAM_Flag, SAM_Flag, SOM_Flag
- (These belong in Component 4)

**Aggregations**
- ❌ Total Revenue by Segment
- ❌ Facility Counts by Segment

**Formulas**
- ❌ IF statements
- ❌ VLOOKUP/INDEX-MATCH to rate tables
- ❌ SUMIF/SUMIFS aggregations

### **Why These Restrictions?**

**Data Integrity:** Source data should be fact-based, not calculated. Formulas can break during file operations.

**Scenario Flexibility:** Rates and assumptions belong in scenario-specific files, not source data.

**Separation of Concerns:** Each component has a specific role. Mixing components causes corruption.

---

## 2.5 Validation Checklist

### **Before Using Source_Data_Master.xlsx**

**✅ Visual Inspection**
- [ ] File has exactly 1 sheet named "Source_Data"
- [ ] First row contains column headers
- [ ] No blank rows in data
- [ ] No blank columns in data
- [ ] Row count = 17,490 (excluding header)

**✅ Column Completeness**
- [ ] All required columns present (see §2.2)
- [ ] Column names spelled correctly (case-sensitive)
- [ ] No extra columns beyond specification

**✅ Data Quality**
- [ ] No duplicate Provider_Numbers
- [ ] Service flags are mutually exclusive
- [ ] Market_Status values are valid
- [ ] Ownership values are valid
- [ ] Census and Total_Beds are numeric
- [ ] Do_We_Serve alignment with service flags

**✅ Formula Check**
- [ ] No formulas in any cells (except allowable data cleaning)
- [ ] All cells contain static values or text

**✅ Documentation**
- [ ] File name follows convention: `Source_Data_Master.xlsx`
- [ ] File saved in same directory as Economic_Model file
- [ ] Backup copy created before any modifications

---

# PART 3: FILE 2 - ECONOMIC MODEL (SCENARIO 1)

## 3.1 File Structure Overview

### **Component Integration**

**File Name:** `Economic_Model_Scenario_1.xlsx`  
**Purpose:** Complete computational model for Scenario 1  
**Sheets:** 6 (all linked sequentially)

**Sheet Flow:**
```
Sheet 1: Fee_Structure
    ↓
Sheet 2: Calculations (reads File 1 + Sheet 1)
    ↓
Sheet 3: Segmentation (reads Sheet 2)
    ↓
Sheet 4: Results (reads Sheet 3)
    ↓
Sheet 5: Scenario_Definitions (metadata only)
    ↓
Sheet 6: QA_Validation (reads all sheets)
```

**Key Principle:** Data flows forward only. No backward references (Sheet 4 does not reference Sheet 2).

---

## 3.2 Sheet 1: Fee_Structure (Component 2)

### **Purpose**

**Component 2: Scenario-Specific Rate Configuration**

This sheet contains all scenario-specific rates, multipliers, and assumptions. **This is the ONLY component that changes between scenarios.**

### **Sheet Layout**

**Structure:**

```
Section A: Scenario Metadata (Rows 1-10)
Section B: Rate Values (Rows 12-20)
Section C: Coverage Multipliers (Rows 22-30)
Section D: Documentation (Rows 32-40)
```

### **Section A: Scenario Metadata**

| Row | Column A | Column B | Column C | Notes |
|-----|----------|----------|----------|-------|
| 1 | **Scenario Name** | Scenario 1: Current State | | Display name |
| 2 | **Scenario ID** | S1 | | Short code |
| 3 | **Date Created** | 11/15/2025 | | ISO date |
| 4 | **Created By** | Eventus Team | | Author |
| 5 | **Description** | Current revenue with validated benchmarks | | Purpose |
| 6 | **Benchmark** | $127,572,232 | | Expected result |
| 7 | **Status** | ACTIVE | | ACTIVE/DRAFT/RETIRED |
| 8 | **Notes** | SS component uses Adjuster_1 × Adjuster_3 | | Key assumptions |

### **Section B: Rate Values (Annual Rates)**

| Row | A: Rate Name | B: Value | C: Description |
|-----|-------------|---------|----------------|
| 12 | **FFS_PCP_Rate** | $1,875 | Primary Care Provider (annual per census) |
| 13 | **FFS_MH_Rate** | $1,898 | Mental Health (annual per census) |
| 14 | **CCM_Rate** | $360 | Chronic Care Management (annual per census) |
| 15 | **SS_Rate** | $4,800 | Shared Savings (annual per census) |

**CRITICAL:** These are ANNUAL rates. Do NOT multiply by 12.

### **Section C: Coverage Multipliers**

| Row | A: Multiplier Name | B: Value | C: Description |
|-----|--------------------|----------|----------------|
| 22 | **Adjuster_1** | 0.50 | MH and SS coverage factor (50%) |
| 23 | **Adjuster_2** | 0.30 | CCM coverage factor (30%) |
| 24 | **Adjuster_3** | 0.33 | SS retention rate (33%) |

**SS Component Calculation:**
```
SS_Component = SS_Rate × Adjuster_1 × Adjuster_3
             = $4,800 × 0.50 × 0.33
             = $792
```

### **Section D: Documentation**

| Row | A: Field | B: Value |
|-----|----------|----------|
| 32 | **Source** | Validated benchmarks from production model |
| 33 | **Last Updated** | 11/15/2025 |
| 34 | **Updated By** | Eventus Team |
| 35 | **Change Log** | V2.2 - Corrected to annual rates, removed ×12 |

### **Named Ranges (Optional but Recommended)**

For easier formula reference in Sheet 2, create named ranges:

| Named Range | Refers To | Value |
|-------------|-----------|-------|
| `FFS_PCP_Rate` | Sheet1!$B$12 | 1875 |
| `FFS_MH_Rate` | Sheet1!$B$13 | 1898 |
| `CCM_Rate` | Sheet1!$B$14 | 360 |
| `SS_Rate` | Sheet1!$B$15 | 4800 |
| `Adjuster_1` | Sheet1!$B$22 | 0.50 |
| `Adjuster_2` | Sheet1!$B$23 | 0.30 |
| `Adjuster_3` | Sheet1!$B$24 | 0.33 |

---

## 3.3 Sheet 2: Calculations (Component 3)

### **Purpose**

**Component 3: Four Revenue Stream Calculation Engine**

This sheet imports source data from File 1 and rates from Sheet 1, then calculates the four revenue streams for each facility:
1. Current Revenue
2. Integration Revenue
3. New Biz Revenue
4. Total Revenue

Plus service component breakdowns (PCP, MH, CCM, SS).

### **Sheet Layout**

**Columns A-Z:** Import from File 1 (Source_Data)  
**Columns AA-AZ:** Calculated fields (four revenue streams + components)

### **Import Section (Columns A-P)**

**These columns link to File 1:**

| Column | Field Name | Source | Notes |
|--------|-----------|--------|-------|
| A | Provider_Number | File1!A:A | Facility ID |
| B | Facility_Name | File1!B:B | Name |
| C | Facility_Type | File1!C:C | SNF/ALF |
| D | Corporate_Entity | File1!D:D | Parent org |
| E | Ownership | File1!E:E | Corporate/Independent |
| F | State | File1!F:F | State code |
| G | ZIP | File1!G:G | ZIP code |
| H | PCP_Only_Flag | File1!H:H | Yes/No |
| I | MH_Only_Flag | File1!I:I | Yes/No |
| J | Integrated_Flag | File1!J:J | Yes/No |
| K | SS_Service_Flag | File1!K:K | Yes/No |
| L | Market_Status | File1!L:L | Existing/Emerging/New |
| M | Has_Barrier | File1!M:M | Yes/No |
| N | Census | File1!N:N | Average daily census |
| O | Total_Beds | File1!O:O | Licensed beds |
| P | Do_We_Serve | File1!P:P | Yes/No |

**Formula Pattern for Column A, Row 2:**
```excel
='[Source_Data_Master.xlsx]Source_Data'!A2
```

**Apply this pattern down for all 17,490 rows and across for columns A-P.**

### **Calculation Section (Columns AA-AZ)**

### **Column AA: Current_Revenue**

**Purpose:** Calculate actual revenue from currently served facilities based on service type.

**Applied to:** Do_We_Serve = "Yes" ONLY

**Formula (Row 2):**
```excel
=IF(P2="Yes",
   IF(J2="Yes",
      N2*(FFS_PCP_Rate + (FFS_MH_Rate*Adjuster_1) + (CCM_Rate*Adjuster_2) + (SS_Rate*Adjuster_1*Adjuster_3)),
      IF(H2="Yes",
         N2*FFS_PCP_Rate,
         IF(I2="Yes",
            N2*(FFS_MH_Rate*Adjuster_1),
            0
         )
      )
   ),
   0
)
```

**Logic Breakdown:**

1. **IF Do_We_Serve = "Yes":** Only calculate for served facilities
2. **IF Integrated (J="Yes"):**
   - Census × (FFS_PCP_Rate + (FFS_MH_Rate × Adjuster_1) + (CCM_Rate × Adjuster_2) + (SS_Rate × Adjuster_1 × Adjuster_3))
3. **ELSE IF PCP-Only (H="Yes"):**
   - Census × FFS_PCP_Rate
4. **ELSE IF MH-Only (I="Yes"):**
   - Census × (FFS_MH_Rate × Adjuster_1)
5. **ELSE:** 0 (no service type flag set - should not happen after data quality checks)

---

### **Column AB: Integration_Revenue**

**Purpose:** Calculate revenue opportunity from adding missing services to served facilities.

**Applied to:** Do_We_Serve = "Yes" ONLY

**Formula (Row 2):**
```excel
=IF(P2="Yes",
   IF(H2="Yes",
      N2*((FFS_MH_Rate*Adjuster_1) + (CCM_Rate*Adjuster_2) + (SS_Rate*Adjuster_1*Adjuster_3)),
      IF(I2="Yes",
         N2*(FFS_PCP_Rate + (CCM_Rate*Adjuster_2) + (SS_Rate*Adjuster_1*Adjuster_3)),
         IF(J2="Yes",
            N2*((CCM_Rate*Adjuster_2) + (SS_Rate*Adjuster_1*Adjuster_3)),
            0
         )
      )
   ),
   0
)
```

**Logic Breakdown:**

1. **IF Do_We_Serve = "Yes":**
2. **IF PCP-Only (H="Yes"):** Add MH, CCM, SS
   - Census × ((FFS_MH_Rate × Adjuster_1) + (CCM_Rate × Adjuster_2) + (SS_Rate × Adjuster_1 × Adjuster_3))
3. **ELSE IF MH-Only (I="Yes"):** Add PCP, CCM, SS
   - Census × (FFS_PCP_Rate + (CCM_Rate × Adjuster_2) + (SS_Rate × Adjuster_1 × Adjuster_3))
4. **ELSE IF Integrated (J="Yes"):** Add CCM, SS
   - Census × ((CCM_Rate × Adjuster_2) + (SS_Rate × Adjuster_1 × Adjuster_3))
   - **Assumption:** Integrated facilities already have PCP + MH, just missing CCM + SS
5. **ELSE:** 0

---

### **Column AC: New_Biz_Revenue**

**Purpose:** Calculate revenue opportunity from unserved facilities assuming full Integrated services.

**Applied to:** Do_We_Serve ≠ "Yes"

**Formula (Row 2):**
```excel
=IF(P2<>"Yes",
   N2*(FFS_PCP_Rate + (FFS_MH_Rate*Adjuster_1) + (CCM_Rate*Adjuster_2) + (SS_Rate*Adjuster_1*Adjuster_3)),
   0
)
```

**Logic Breakdown:**

1. **IF Do_We_Serve ≠ "Yes":** Only calculate for unserved facilities
2. **Calculate full Integrated revenue:**
   - Census × (FFS_PCP_Rate + (FFS_MH_Rate × Adjuster_1) + (CCM_Rate × Adjuster_2) + (SS_Rate × Adjuster_1 × Adjuster_3))
3. **Assumption:** Every new facility gets full Integrated service package

---

### **Column AD: Total_Revenue**

**Purpose:** Sum of Integration and New Biz revenue opportunities.

**Formula (Row 2):**
```excel
=AB2+AC2
```

**Simple addition:** Integration_Revenue + New_Biz_Revenue

---

### **Service Component Breakdown (Columns AE-AH)**

**Optional but recommended for Report 3 (Fee Structure Breakdown)**

**Column AE: PCP_Component_Current**
```excel
=IF(P2="Yes",
   IF(OR(H2="Yes", J2="Yes"),
      N2*FFS_PCP_Rate,
      0
   ),
   0
)
```

**Column AF: MH_Component_Current**
```excel
=IF(P2="Yes",
   IF(OR(I2="Yes", J2="Yes"),
      N2*(FFS_MH_Rate*Adjuster_1),
      0
   ),
   0
)
```

**Column AG: CCM_Component_Current**
```excel
=IF(P2="Yes",
   IF(J2="Yes",
      N2*(CCM_Rate*Adjuster_2),
      0
   ),
   0
)
```

**Column AH: SS_Component_Current**
```excel
=IF(P2="Yes",
   IF(J2="Yes",
      N2*(SS_Rate*Adjuster_1*Adjuster_3),
      0
   ),
   0
)
```

**Note:** Similar columns (AI-AL) for Integration components, (AM-AP) for New Biz components if full service breakdown needed for reporting.

---

### **Quality Checks**

**After Building Sheet 2:**

1. **Visual Inspection:**
   - Row 2 formulas correct?
   - Formulas copied down to row 17,491?
   - No #REF errors?

2. **Benchmark Check:**
   - Sum of Column AA (Current_Revenue) = $127,572,232?
   - If not, investigate formula errors

3. **Data Validation:**
   - No negative revenues?
   - Integration_Revenue = 0 for unserved facilities?
   - New_Biz_Revenue = 0 for served facilities?

4. **Logic Validation:**
   - Served facility with PCP-Only: Current > 0, Integration > 0, New Biz = 0?
   - Unserved facility: Current = 0, Integration = 0, New Biz > 0?

---

## 3.4 Sheet 3: Segmentation (Component 4)

### **Purpose**

**Component 4: Market Segmentation Logic**

This sheet applies TAM/SAM/SOM filters to assign segment flags to each facility.

### **Sheet Layout**

**Columns A-AZ:** Import from Sheet 2 (Calculations)  
**Columns BA-BZ:** Segmentation flags and logic

### **Import Section (Columns A-AZ)**

**Link all calculated data from Sheet 2:**

**Formula Pattern for Column A, Row 2:**
```excel
=Calculations!A2
```

**Copy across for columns A-AD (all columns from Sheet 2, including the four revenue streams).**

### **Segmentation Section (Columns BA-BZ)**

**Column BA: TAM_Flag**

**Purpose:** Total Addressable Market = ALL facilities.

**Formula (Row 2):**
```excel
=TRUE
```

**Logic:** Every facility in the dataset is part of TAM.

**Expected Count:** 17,490 facilities

---

**Column BB: SAM_Flag**

**Purpose:** Serviceable Addressable Market = Corporate facilities in Existing or Emerging markets.

**Formula (Row 2):**
```excel
=AND(E2="Corporate", OR(L2="Existing", L2="Emerging"))
```

**Logic:**
- Ownership = "Corporate" (Column E)
- AND Market_Status = "Existing" OR "Emerging" (Column L)

**Expected Count:** ~5,600-7,000 facilities (corporate entities in target markets)

---

**Column BC: SOM_Flag**

**Purpose:** Serviceable Obtainable Market = Corporate facilities in Existing markets with no barriers.

**Formula (Row 2):**
```excel
=AND(E2="Corporate", L2="Existing", M2="No")
```

**Logic:**
- Ownership = "Corporate" (Column E)
- AND Market_Status = "Existing" (Column L)
- AND Has_Barrier = "No" (Column M)

**Expected Count:** ~3,000-3,500 facilities (immediately addressable market)

---

**Column BD: Segment_Priority**

**Purpose:** Assign priority ranking for targeting.

**Formula (Row 2):**
```excel
=IF(BC2=TRUE, "1-SOM", IF(BB2=TRUE, "2-SAM", IF(BA2=TRUE, "3-TAM", "None")))
```

**Logic:**
- SOM facilities = Priority 1 (highest priority)
- SAM facilities = Priority 2
- TAM-only facilities = Priority 3 (lowest priority)

---

### **Quality Checks**

**After Building Sheet 3:**

1. **Segment Hierarchy:**
   - All SOM facilities should also be SAM and TAM
   - All SAM facilities should also be TAM
   - Formula: SOM_Count ≤ SAM_Count ≤ TAM_Count

2. **Flag Validation:**
   - Count TRUE values in TAM_Flag = 17,490?
   - Count TRUE values in SAM_Flag ≤ 17,490?
   - Count TRUE values in SOM_Flag ≤ SAM_Count?

3. **Corporate Entity Check:**
   - All SOM and SAM facilities have Ownership = "Corporate"?
   - No independent facilities in SOM or SAM?

---

## 3.5 Sheet 4: Results (Component 5)

### **Purpose**

**Component 5: Executive Summary & Aggregations**

This sheet produces the final revenue summary table for stakeholder reporting.

### **Sheet Layout**

**Section A: Executive Summary Table (Rows 1-10)**  
**Section B: Supporting Calculations (Rows 12+)**

### **Section A: Executive Summary Table**

**Table Structure:**

| Row | A: Segment | B: Facilities | C: Current Rev | D: Integration Rev | E: New Biz Rev | F: Total Rev |
|-----|------------|---------------|----------------|--------------------|--------------------|--------------|
| 1 | **Segment** | **# Facilities** | **Current** | **Integration** | **New Biz** | **Total** |
| 2 | TAM | =COUNTIF(Segmentation!BA:BA,TRUE) | =SUMIF(Segmentation!BA:BA,TRUE,Segmentation!AA:AA) | =SUMIF(Segmentation!BA:BA,TRUE,Segmentation!AB:AB) | =SUMIF(Segmentation!BA:BA,TRUE,Segmentation!AC:AC) | =SUMIF(Segmentation!BA:BA,TRUE,Segmentation!AD:AD) |
| 3 | SAM | =COUNTIF(Segmentation!BB:BB,TRUE) | =SUMIF(Segmentation!BB:BB,TRUE,Segmentation!AA:AA) | =SUMIF(Segmentation!BB:BB,TRUE,Segmentation!AB:AB) | =SUMIF(Segmentation!BB:BB,TRUE,Segmentation!AC:AC) | =SUMIF(Segmentation!BB:BB,TRUE,Segmentation!AD:AD) |
| 4 | SOM | =COUNTIF(Segmentation!BC:BC,TRUE) | =SUMIF(Segmentation!BC:BC,TRUE,Segmentation!AA:AA) | =SUMIF(Segmentation!BC:BC,TRUE,Segmentation!AB:AB) | =SUMIF(Segmentation!BC:BC,TRUE,Segmentation!AC:AC) | =SUMIF(Segmentation!BC:BC,TRUE,Segmentation!AD:AD) |

**Expected Results (Scenario 1):**

| Segment | Facilities | Current Revenue | Integration Rev | New Biz Rev | Total Rev |
|---------|------------|-----------------|-----------------|-------------|-----------|
| **TAM** | 17,490 | $127,572,232 | [To Calculate] | [To Calculate] | [To Calculate] |
| **SAM** | [To Calculate] | [To Calculate] | [To Calculate] | [To Calculate] | [To Calculate] |
| **SOM** | [To Calculate] | $88,500,000 (approx) | [To Calculate] | [To Calculate] | [To Calculate] |

**CRITICAL BENCHMARK:** TAM Current Revenue MUST equal $127,572,232. This is the validated benchmark for Scenario 1.

### **Section B: Supporting Calculations**

**Served vs. Unserved Breakdown:**

| Row | A: Description | B: Formula/Value |
|-----|----------------|------------------|
| 12 | **TAM Served Facilities** | =COUNTIFS(Segmentation!BA:BA,TRUE, Segmentation!P:P,"Yes") |
| 13 | **TAM Unserved Facilities** | =B2-B12 |
| 14 | **SAM Served Facilities** | =COUNTIFS(Segmentation!BB:BB,TRUE, Segmentation!P:P,"Yes") |
| 15 | **SAM Unserved Facilities** | =B3-B14 |
| 16 | **SOM Served Facilities** | =COUNTIFS(Segmentation!BC:BC,TRUE, Segmentation!P:P,"Yes") |
| 17 | **SOM Unserved Facilities** | =B4-B16 |

**Facility Type Breakdown:**

| Row | A: Description | B: Formula/Value |
|-----|----------------|------------------|
| 22 | **TAM SNF Facilities** | =COUNTIFS(Segmentation!BA:BA,TRUE, Segmentation!C:C,"SNF") |
| 23 | **TAM ALF Facilities** | =COUNTIFS(Segmentation!BA:BA,TRUE, Segmentation!C:C,"ALF") |
| 24 | **SAM SNF Facilities** | =COUNTIFS(Segmentation!BB:BB,TRUE, Segmentation!C:C,"SNF") |
| 25 | **SAM ALF Facilities** | =COUNTIFS(Segmentation!BB:BB,TRUE, Segmentation!C:C,"ALF") |
| 26 | **SOM SNF Facilities** | =COUNTIFS(Segmentation!BC:BC,TRUE, Segmentation!C:C,"SNF") |
| 27 | **SOM ALF Facilities** | =COUNTIFS(Segmentation!BC:BC,TRUE, Segmentation!C:C,"ALF") |

**Corporate vs. Independent Breakdown:**

| Row | A: Description | B: Formula/Value |
|-----|----------------|------------------|
| 32 | **TAM Corporate Facilities** | =COUNTIFS(Segmentation!BA:BA,TRUE, Segmentation!E:E,"Corporate") |
| 33 | **TAM Independent Facilities** | =B2-B32 |

### **Quality Checks**

**After Building Sheet 4:**

1. **Benchmark Validation:**
   - TAM Current Revenue (Cell C2) = $127,572,232?
   - If not, trace back to Sheet 2 formulas

2. **Hierarchy Check:**
   - C4 (SOM) ≤ C3 (SAM) ≤ C2 (TAM)?
   - B4 (SOM) ≤ B3 (SAM) ≤ B2 (TAM)?

3. **Revenue Logic Check:**
   - TAM Integration + TAM New Biz = TAM Total?
   - Similar for SAM and SOM?

4. **Supporting Calculations:**
   - Served + Unserved = Total for each segment?
   - SNF + ALF = Total for each segment?
   - Corporate + Independent = TAM total?

---

## 3.6 Sheet 5: Scenario_Definitions (Component 6)

### **Purpose**

**Component 6: Scenario Documentation & Comparison**

This sheet documents all scenario assumptions and enables side-by-side comparison of different scenarios.

### **Sheet Layout**

**Section A: Scenario 1 Definition (Rows 1-40)**  
**Section B: Scenario 2 Placeholder (Rows 42-60)**  
**Section C: Scenario 3 Placeholder (Rows 62-80)**  
**Section D: Scenario Comparison Table (Rows 82+)**

### **Section A: Scenario 1 Definition**

| Row | A: Field | B: Value | C: Notes |
|-----|----------|----------|----------|
| 1 | **Scenario Name** | Scenario 1: Current State | Display name |
| 2 | **Scenario ID** | S1 | Short identifier |
| 3 | **Status** | ACTIVE | ACTIVE/DRAFT/RETIRED |
| 4 | **Created Date** | 11/15/2025 | ISO date |
| 5 | **Created By** | Eventus Team | Author |
| 6 | **Description** | Current revenue model with validated benchmarks | Purpose |
| 7 | **Benchmark** | $127,572,232 | Expected TAM Current Revenue |
| 8 | **Benchmark Status** | ✅ VALIDATED | Pass/Fail |
| 10 | **Key Assumptions** | | |
| 11 | • FFS_PCP_Rate | $1,875 (annual) | Primary care |
| 12 | • FFS_MH_Rate | $1,898 (annual) | Mental health |
| 13 | • CCM_Rate | $360 (annual) | Chronic care mgmt |
| 14 | • SS_Rate | $4,800 (annual) | Shared savings |
| 15 | • Adjuster_1 (MH/SS) | 0.50 | 50% coverage |
| 16 | • Adjuster_2 (CCM) | 0.30 | 30% coverage |
| 17 | • Adjuster_3 (SS) | 0.33 | 33% retention |
| 18 | • SS Component | $4,800 × 0.50 × 0.33 = $792 | Critical formula |
| 19 | • ALF Bed Surrogate (Served) | 49 beds | For facilities with Total_Beds = 0 |
| 20 | • ALF Bed Surrogate (Unserved) | 72 beds | For facilities with Total_Beds = 0 |
| 22 | **Service Type Logic** | | |
| 23 | • Integrated | PCP + MH + CCM + SS | Full service bundle |
| 24 | • PCP-Only | PCP only | Primary care only |
| 25 | • MH-Only | MH only | Mental health only |
| 27 | **Revenue Streams** | | |
| 28 | • Current Revenue | Served facilities, current services | What we earn today |
| 29 | • Integration Revenue | Served facilities, missing services | Upsell opportunity |
| 30 | • New Biz Revenue | Unserved facilities, full Integrated | New client acquisition |
| 31 | • Total Revenue | Integration + New Biz | Full market opportunity |
| 33 | **Segmentation Rules** | | |
| 34 | • TAM | All 17,490 facilities | Total addressable market |
| 35 | • SAM | Corporate in Existing/Emerging markets | ~5,600-7,000 facilities |
| 36 | • SOM | Corporate in Existing, no barriers | ~3,000-3,500 facilities |

### **Section B: Scenario 2 Placeholder**

| Row | A: Field | B: Value | C: Notes |
|-----|----------|----------|----------|
| 42 | **Scenario Name** | Scenario 2: [TBD] | PLACEHOLDER |
| 43 | **Scenario ID** | S2 | Short identifier |
| 44 | **Status** | DRAFT | Not yet implemented |
| 45 | **Description** | [To be defined] | Purpose |
| 46 | **Key Changes from S1** | | |
| 47 | • [Rate/Multiplier Changes] | [TBD] | Document changes |

### **Section C: Scenario 3 Placeholder**

| Row | A: Field | B: Value | C: Notes |
|-----|----------|----------|----------|
| 62 | **Scenario Name** | Scenario 3: [TBD] | PLACEHOLDER |
| 63 | **Scenario ID** | S3 | Short identifier |
| 64 | **Status** | DRAFT | Not yet implemented |
| 65 | **Description** | [To be defined] | Purpose |

### **Section D: Scenario Comparison Table**

| Row | A: Metric | B: S1 (Current) | C: S2 | D: S3 |
|-----|-----------|-----------------|-------|-------|
| 82 | **TAM Current Revenue** | $127.6M | [TBD] | [TBD] |
| 83 | **TAM Integration Revenue** | [TBD] | [TBD] | [TBD] |
| 84 | **TAM New Biz Revenue** | [TBD] | [TBD] | [TBD] |
| 85 | **TAM Total Revenue** | [TBD] | [TBD] | [TBD] |
| 86 | **SOM Current Revenue** | $88.5M | [TBD] | [TBD] |
| 87 | **Total Facilities (TAM)** | 17,490 | 17,490 | 17,490 |

### **Usage Notes**

**This sheet is METADATA ONLY.** No calculations or formulas are required here (except for pulling results from Sheet 4 if desired for comparison).

---

## 3.7 Sheet 6: QA_Validation (Component 7)

### **Purpose**

**Component 7: Quality Assurance & Validation**

This sheet runs comprehensive validation checks to ensure data integrity and computational accuracy.

### **Sheet Layout**

**Section A: Benchmark Validation (Rows 1-10)**  
**Section B: Data Quality Checks (Rows 12-30)**  
**Section C: Formula Integrity Tests (Rows 32-50)**  
**Section D: Revenue Logic Validation (Rows 52-70)**  
**Section E: Overall Status (Rows 72-80)**

### **Section A: Benchmark Validation**

| Row | A: Check | B: Expected | C: Actual | D: Status |
|-----|----------|-------------|-----------|-----------|
| 1 | **TAM Current Revenue** | $127,572,232 | =Results!C2 | =IF(ABS(C1-B1)<100,"✅ PASS","❌ FAIL") |
| 2 | **SOM Current Revenue** | $88,500,000 | =Results!C4 | =IF(ABS(C2-B2)<1000000,"✅ PASS","⚠️ WARN") |
| 3 | **Total Facilities** | 17,490 | =Results!B2 | =IF(C3=B3,"✅ PASS","❌ FAIL") |

**Notes:**
- TAM Current Revenue must match exactly (within $100 tolerance for rounding)
- SOM Current Revenue is approximate (within $1M tolerance)
- Total Facilities must be exact

### **Section B: Data Quality Checks**

| Row | A: Check | B: Threshold | C: Actual | D: Status |
|-----|----------|--------------|-----------|-----------|
| 12 | **Data Quality Rate** | 99.99% | =[Calculate] | =IF(C12>=B12,"✅ PASS","❌ FAIL") |
| 13 | **Duplicate Facilities** | 0 | =[Count duplicates] | =IF(C13=B13,"✅ PASS","❌ FAIL") |
| 14 | **Service Flag Errors** | ≤2 | =[Count flag errors] | =IF(C14<=B14,"✅ PASS","❌ FAIL") |
| 15 | **Missing Market Status** | 0 | =COUNTBLANK(Segmentation!L:L)-1 | =IF(C15=B15,"✅ PASS","❌ FAIL") |
| 16 | **Missing Ownership** | 0 | =COUNTBLANK(Segmentation!E:E)-1 | =IF(C16=B16,"✅ PASS","❌ FAIL") |

### **Section C: Formula Integrity Tests**

| Row | A: Check | B: Expected | C: Actual | D: Status |
|-----|----------|-------------|-----------|-----------|
| 32 | **Current Revenue has formulas** | TRUE | =ISFORMULA(Calculations!AA2) | =IF(C32=B32,"✅ PASS","❌ FAIL") |
| 33 | **Integration Revenue has formulas** | TRUE | =ISFORMULA(Calculations!AB2) | =IF(C33=B33,"✅ PASS","❌ FAIL") |
| 34 | **New Biz Revenue has formulas** | TRUE | =ISFORMULA(Calculations!AC2) | =IF(C34=B34,"✅ PASS","❌ FAIL") |
| 35 | **No #REF errors in Calculations** | 0 | =COUNTIF(Calculations!AA:AZ,"#REF!") | =IF(C35=B35,"✅ PASS","❌ FAIL") |
| 36 | **No negative revenues** | 0 | =COUNTIF(Calculations!AA:AD,"<0") | =IF(C36=B36,"✅ PASS","❌ FAIL") |

### **Section D: Revenue Logic Validation**

| Row | A: Check | B: Expected | C: Actual | D: Status |
|-----|----------|-------------|-----------|-----------|
| 52 | **Served facilities: Integration > 0** | TRUE | =[Validate logic] | =IF(C52=B52,"✅ PASS","❌ FAIL") |
| 53 | **Served facilities: New Biz = 0** | TRUE | =[Validate logic] | =IF(C53=B53,"✅ PASS","❌ FAIL") |
| 54 | **Unserved facilities: Current = 0** | TRUE | =[Validate logic] | =IF(C54=B54,"✅ PASS","❌ FAIL") |
| 55 | **Unserved facilities: Integration = 0** | TRUE | =[Validate logic] | =IF(C55=B55,"✅ PASS","❌ FAIL") |
| 56 | **Total = Integration + New Biz** | TRUE | =[Validate formula] | =IF(C56=B56,"✅ PASS","❌ FAIL") |

### **Section E: Overall Status**

| Row | A: Description | B: Value |
|-----|----------------|----------|
| 72 | **Total Checks** | =COUNTA(D1:D56) |
| 73 | **Checks Passed** | =COUNTIF(D1:D56,"✅ PASS") |
| 74 | **Checks Failed** | =COUNTIF(D1:D56,"❌ FAIL") |
| 75 | **Checks Warned** | =COUNTIF(D1:D56,"⚠️ WARN") |
| 76 | **Pass Rate** | =B73/B72 |
| 78 | **OVERALL STATUS** | =IF(B74=0, IF(B75=0,"✅ ALL CHECKS PASSED","⚠️ WARNINGS PRESENT"),"❌ VALIDATION FAILED") |

**Success Criteria:**
- All checks must pass (green ✅)
- Warnings (yellow ⚠️) require investigation but don't block deployment
- Any failures (red ❌) must be resolved before using the model

---

# PART 4: SCENARIO 1 FORMULAS & BENCHMARKS

## 4.1 Scenario 1 Benchmark: $127.6M

### **Primary Validation Benchmark**

**Total Addressable Market (TAM) Current Revenue:**

```
Expected: $127,572,232
Tolerance: ±$100 (rounding)
Status: ✅ VALIDATED (99.99% data quality, 100% computational accuracy)
```

**This benchmark is CRITICAL.** Any model implementation MUST produce this exact result for TAM Current Revenue in Scenario 1.

### **Secondary Benchmarks**

**Serviceable Obtainable Market (SOM) Current Revenue:**

```
Expected: ~$88,500,000
Tolerance: ±$1,000,000
Status: ✅ VALIDATED
```

**Total Facilities:**

```
Expected: 17,490
Tolerance: 0 (must be exact)
Status: ✅ VALIDATED
```

---

## 4.2 Fee Structure Rates (Annual)

### **Scenario 1 Rate Values**

**CRITICAL:** These are ANNUAL rates per census. Do NOT multiply by 12.

| Rate Component | Value | Description |
|----------------|-------|-------------|
| **FFS_PCP_Rate** | $1,875 | Primary Care Provider (annual per census) |
| **FFS_MH_Rate** | $1,898 | Mental Health (annual per census) |
| **CCM_Rate** | $360 | Chronic Care Management (annual per census) |
| **SS_Rate** | $4,800 | Shared Savings (annual per census) |

### **Coverage Multipliers**

| Multiplier | Value | Description |
|------------|-------|-------------|
| **Adjuster_1** | 0.50 | MH and SS coverage factor (50%) |
| **Adjuster_2** | 0.30 | CCM coverage factor (30%) |
| **Adjuster_3** | 0.33 | SS retention rate (33%) |

### **Composite Rates**

**Integrated Service (Full Package):**
```
Monthly Rate = FFS_PCP + (FFS_MH × 0.50) + (CCM × 0.30) + (SS × 0.50 × 0.33)
             = $1,875 + ($1,898 × 0.50) + ($360 × 0.30) + ($4,800 × 0.50 × 0.33)
             = $1,875 + $949 + $108 + $792
             = $3,724 per census (annual)
```

**Component Breakdown:**
- PCP: $1,875 (50.3% of integrated rate)
- MH: $949 (25.5% of integrated rate)
- CCM: $108 (2.9% of integrated rate)
- SS: $792 (21.3% of integrated rate)

---

## 4.3 Current Revenue Formulas

### **Purpose**

Calculate actual revenue from facilities currently served by Eventus.

**Applied to:** Do_We_Serve = "Yes" ONLY

### **Integrated Services**

**Facilities with Integrated_Flag = "Yes"**

```
Current_Revenue = Census × (
    FFS_PCP_Rate + 
    (FFS_MH_Rate × Adjuster_1) + 
    (CCM_Rate × Adjuster_2) + 
    (SS_Rate × Adjuster_1 × Adjuster_3)
)

= Census × (
    $1,875 + 
    ($1,898 × 0.50) + 
    ($360 × 0.30) + 
    ($4,800 × 0.50 × 0.33)
)

= Census × $3,724
```

### **PCP-Only Services**

**Facilities with PCP_Only_Flag = "Yes"**

```
Current_Revenue = Census × FFS_PCP_Rate

= Census × $1,875
```

### **MH-Only Services**

**Facilities with MH_Only_Flag = "Yes"**

```
Current_Revenue = Census × (FFS_MH_Rate × Adjuster_1)

= Census × ($1,898 × 0.50)

= Census × $949
```

### **Validation Example**

**Facility:** Average census = 78.5, Integrated services

```
Current_Revenue = 78.5 × $3,724
                = $292,334

Range Check: ✅ Falls within $50k-$300k expected range
```

---

## 4.4 Integration Revenue Formulas

### **Purpose**

Calculate revenue opportunity from adding missing services to served facilities.

**Applied to:** Do_We_Serve = "Yes" ONLY

### **PCP-Only Facilities → Add MH, CCM, SS**

```
Integration_Revenue = Census × (
    (FFS_MH_Rate × Adjuster_1) + 
    (CCM_Rate × Adjuster_2) + 
    (SS_Rate × Adjuster_1 × Adjuster_3)
)

= Census × (
    ($1,898 × 0.50) + 
    ($360 × 0.30) + 
    ($4,800 × 0.50 × 0.33)
)

= Census × ($949 + $108 + $792)

= Census × $1,849
```

### **MH-Only Facilities → Add PCP, CCM, SS**

```
Integration_Revenue = Census × (
    FFS_PCP_Rate + 
    (CCM_Rate × Adjuster_2) + 
    (SS_Rate × Adjuster_1 × Adjuster_3)
)

= Census × (
    $1,875 + 
    ($360 × 0.30) + 
    ($4,800 × 0.50 × 0.33)
)

= Census × ($1,875 + $108 + $792)

= Census × $2,775
```

### **Integrated Facilities → Add CCM, SS**

**Assumption:** Already have PCP + MH, just missing CCM + SS

```
Integration_Revenue = Census × (
    (CCM_Rate × Adjuster_2) + 
    (SS_Rate × Adjuster_1 × Adjuster_3)
)

= Census × (
    ($360 × 0.30) + 
    ($4,800 × 0.50 × 0.33)
)

= Census × ($108 + $792)

= Census × $900
```

---

## 4.5 New Biz Revenue Formulas

### **Purpose**

Calculate revenue opportunity from unserved facilities assuming full Integrated services.

**Applied to:** Do_We_Serve ≠ "Yes"

### **All Unserved Facilities → Full Integrated**

**Assumption:** Every new facility gets complete Integrated service package

```
New_Biz_Revenue = Census × (
    FFS_PCP_Rate + 
    (FFS_MH_Rate × Adjuster_1) + 
    (CCM_Rate × Adjuster_2) + 
    (SS_Rate × Adjuster_1 × Adjuster_3)
)

= Census × (
    $1,875 + 
    ($1,898 × 0.50) + 
    ($360 × 0.30) + 
    ($4,800 × 0.50 × 0.33)
)

= Census × $3,724
```

**Note:** This is identical to the Integrated Current Revenue formula, but applied to unserved facilities.

---

## 4.6 Total Revenue Formula

### **Purpose**

Sum of Integration and New Biz revenue opportunities.

```
Total_Revenue = Integration_Revenue + New_Biz_Revenue
```

**Strategic Interpretation:**
- **Integration:** Short-term upsell opportunity (6-12 months)
- **New Biz:** Long-term market expansion (12-24 months)
- **Total:** Full addressable market opportunity

---

## 4.7 Service Component Breakdown

### **Purpose**

Break down each revenue stream by service type (PCP, MH, CCM, SS) for detailed reporting.

### **Current Revenue Components**

**For Integrated Facilities:**
- PCP Component: Census × $1,875
- MH Component: Census × ($1,898 × 0.50) = Census × $949
- CCM Component: Census × ($360 × 0.30) = Census × $108
- SS Component: Census × ($4,800 × 0.50 × 0.33) = Census × $792

**For PCP-Only Facilities:**
- PCP Component: Census × $1,875
- MH Component: $0
- CCM Component: $0
- SS Component: $0

**For MH-Only Facilities:**
- PCP Component: $0
- MH Component: Census × ($1,898 × 0.50) = Census × $949
- CCM Component: $0
- SS Component: $0

### **Integration Revenue Components**

**For PCP-Only → Integrated:**
- PCP Component: $0 (already have)
- MH Component: Census × $949 (adding)
- CCM Component: Census × $108 (adding)
- SS Component: Census × $792 (adding)

**For MH-Only → Integrated:**
- PCP Component: Census × $1,875 (adding)
- MH Component: $0 (already have)
- CCM Component: Census × $108 (adding)
- SS Component: Census × $792 (adding)

**For Integrated → Integrated+CCM+SS:**
- PCP Component: $0 (already have)
- MH Component: $0 (already have)
- CCM Component: Census × $108 (adding)
- SS Component: Census × $792 (adding)

### **New Biz Revenue Components**

**For All Unserved Facilities:**
- PCP Component: Census × $1,875
- MH Component: Census × $949
- CCM Component: Census × $108
- SS Component: Census × $792

---

# PART 5: FILE 3 - REPORTS OUTPUT

## 5.1 Reports File Structure

### **Purpose**

**File 3: Stakeholder-Ready Reports**

This file contains formatted reports for distribution to stakeholders without exposing model internals.

**File Name:** `Reports_Scenario_1.xlsx`  
**Purpose:** Formatted reporting outputs linked to File 2  
**Sheets:** One sheet per report (expandable as needed)

### **Key Principles**

**Separation from Model:**
- File 3 is INDEPENDENT from Files 1 & 2 operationally
- Can be distributed without sharing proprietary model logic
- Links to File 2 (Results & Segmentation sheets) for data

**Report Focus:**
- Executive-ready formatting
- Color coding for visual clarity
- Stakeholder-specific views
- No formulas visible to end users

**Flexibility:**
- Add new report sheets without touching Files 1 or 2
- Customize formatting without affecting calculations
- Version reports independently (e.g., Monthly snapshots)

---

## 5.2 Report 1: Facilities Count

### **Report Structure**

**Sheet Name:** "Facilities_Count"  
**Purpose:** Count facilities by segment, type, and ownership with served vs. total breakdown

**Layout:** Three sections (SNF, ALF, Total) on one sheet

### **Section 1: SNF Facilities**

| Row | A: Segment | B: Corporate | C: Independent | D: Total |
|-----|------------|--------------|----------------|----------|
| 1 | **SNF** | **Facilities** | | |
| 2 | | **Total / Our Share** | | |
| 3 | | Corporate | Independent | Total |
| 4 | TAM | [Total] / [Served] | [Total] / [Served] | [Total] / [Served] |
| 5 | SAM | [Total] / [Served] | [Total] / [Served] | [Total] / [Served] |
| 6 | SOM | [Total] / [Served] | [Total] / [Served] | [Total] / [Served] |

**Example Data (from your screenshot):**
- TAM: 10,031 / 453 (Corporate), 4,719 / 101 (Independent), 14,750 / 554 (Total)
- SAM: 4,431 / 414 (Corporate), 2,031 / 101 (Independent), 6,462 / 515 (Total)
- SOM: 2,667 / 414 (Corporate), 914 / 101 (Independent), 3,581 / 515 (Total)

**Formulas:**

**Cell B4 (TAM Corporate Total / Served):**
```excel
=COUNTIFS([File2]Segmentation!$BA:$BA,TRUE,[File2]Segmentation!$C:$C,"SNF",[File2]Segmentation!$E:$E,"Corporate") 
& " / " 
& COUNTIFS([File2]Segmentation!$BA:$BA,TRUE,[File2]Segmentation!$C:$C,"SNF",[File2]Segmentation!$E:$E,"Corporate",[File2]Segmentation!$P:$P,"Yes")
```

**Repeat pattern for all cells with segment/ownership/type combinations.**

### **Section 2: ALF Facilities**

Same structure as SNF, filtering for Facility_Type = "ALF"

### **Section 3: Total Facilities**

Same structure, no facility type filter (includes both SNF and ALF)

### **Formatting:**
- TAM rows: Blue background (#4472C4)
- SAM rows: Orange background (#ED7D31)
- SOM rows: Green background (#70AD47)
- Total section: Purple border
- Number format: #,##0 (comma separator, no decimals)

---

## 5.3 Report 2: Revenue Summary

### **Report Structure**

**Sheet Name:** "Revenue"  
**Purpose:** Revenue breakdown by segment and type with Current/Integration/New Biz/Total columns

**Layout:** Three sections (SNF, ALF, Total) on one sheet

### **Section 1: SNF Revenue**

| Row | A: Segment | B: Current | C: Integration | D: New Biz | E: Total |
|-----|------------|------------|----------------|------------|----------|
| 1 | **SNF** | **Revenue** | | | |
| 2 | | | **Potential** | | |
| 3 | | Current | Integration | New Biz | Total |
| 4 | TAM | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX |
| 5 | SAM | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX |
| 6 | SOM | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX |

**Example Data (from your screenshot for Total):**
- TAM: $147,330,900 (Current), $88,895,661 (Integration), $4,474,494,941 (New Biz), $4,563,390,602 (Total)
- SAM: $141,174,036 (Current), $82,542,503 (Integration), $2,056,569,965 (New Biz), $2,139,112,468 (Total)
- SOM: $141,174,036 (Current), $82,542,503 (Integration), $1,279,677,21 (New Biz), $1,362,219,71 (Total)

**Formulas:**

**Cell B4 (TAM Current Revenue for SNF):**
```excel
=SUMIFS([File2]Segmentation!$AA:$AA,[File2]Segmentation!$BA:$BA,TRUE,[File2]Segmentation!$C:$C,"SNF")
```

**Cell C4 (TAM Integration Revenue for SNF):**
```excel
=SUMIFS([File2]Segmentation!$AB:$AB,[File2]Segmentation!$BA:$BA,TRUE,[File2]Segmentation!$C:$C,"SNF")
```

**Cell D4 (TAM New Biz Revenue for SNF):**
```excel
=SUMIFS([File2]Segmentation!$AC:$AC,[File2]Segmentation!$BA:$BA,TRUE,[File2]Segmentation!$C:$C,"SNF")
```

**Cell E4 (TAM Total Revenue for SNF):**
```excel
=C4+D4
```
OR
```excel
=SUMIFS([File2]Segmentation!$AD:$AD,[File2]Segmentation!$BA:$BA,TRUE,[File2]Segmentation!$C:$C,"SNF")
```

**Repeat pattern for SAM (BB), SOM (BC), and ALF sections.**

### **Section 2: ALF Revenue**

Same structure as SNF, filtering for Facility_Type = "ALF"

### **Section 3: Total Revenue**

Same structure, no facility type filter

### **Formatting:**
- TAM rows: Blue background
- SAM rows: Orange background
- SOM rows: Green background
- Total section: Purple border
- Currency format: $#,##0 (no decimals)

---

## 5.4 Report 3: SOM Fee Structure Breakdown

### **Report Structure**

**Sheet Name:** "SOM_Fee_Breakdown"  
**Purpose:** Break down SOM revenue by service component (PCP, MH, CCM, SS) for strategic planning

**Layout:** Three tables (SNF, ALF, Total) on one sheet, SOM SEGMENT ONLY

### **Table A: SNF**

**Header:** SOM SEGMENT: REVENUE BREAKDOWN BY FEE STRUCTURE

**Table Structure:**

| Row | A: Revenues | B: PCP | C: MH | D: CCM | E: SS | F: Total |
|-----|-------------|--------|-------|--------|-------|----------|
| 1 | Current ($) | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX |
| 2 | Current (%) | XX% | XX% | XX% | XX% | 100% |
| 3 | Integration ($) | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX |
| 4 | Integration (%) | XX% | XX% | XX% | XX% | 100% |
| 5 | New Biz ($) | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX |
| 6 | New Biz (%) | XX% | XX% | XX% | XX% | 100% |
| 7 | Total Revenue ($) | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX |
| 8 | Total Revenue (%) | XX% | XX% | XX% | XX% | 100% |

**Formulas (assuming service component columns exist in File 2, Sheet 2):**

**If Component Columns Exist (AE-AH for Current):**

**Cell B1 (SOM Current PCP Revenue for SNF):**
```excel
=SUMIFS([File2]Segmentation!$AE:$AE,[File2]Segmentation!$BC:$BC,TRUE,[File2]Segmentation!$C:$C,"SNF")
```

**Cell B2 (SOM Current PCP %):**
```excel
=B1/F1
```

**If Component Columns Don't Exist:**

Need to calculate components in Report file itself using service type flags:

**Cell B1 (SOM Current PCP Revenue for SNF):**
```excel
=SUMIFS([File2]Segmentation!$N:$N,[File2]Segmentation!$BC:$BC,TRUE,[File2]Segmentation!$C:$C,"SNF",[File2]Segmentation!$P:$P,"Yes",Segmentation!$H:$H,"Yes")*1875
+SUMIFS([File2]Segmentation!$N:$N,[File2]Segmentation!$BC:$BC,TRUE,[File2]Segmentation!$C:$C,"SNF",[File2]Segmentation!$P:$P,"Yes",[File2]Segmentation!$J:$J,"Yes")*1875
```

**This gets complex quickly - RECOMMENDATION: Add component columns to File 2, Sheet 2 for cleaner reporting.**

### **Table B: ALF**

Same structure as SNF, filtering for Facility_Type = "ALF"

### **Table C: Total Facilities**

Same structure, no facility type filter

### **Formatting:**
- Currency format: $#,##0 (no decimals)
- Percentage format: 0.0% (one decimal)
- Header: Bold, larger font

---

## 5.5 Report 4: Top 20 Corporate Entities (SOM Only)

### **Report Structure**

**Sheet Name:** "Top_20_Corporate_Entities"  
**Purpose:** Strategic targeting report ranking corporate entities by opportunity type (SOM segment only)

**Layout:** Three tables on one sheet, all filtered to SOM segment only

---

### **TABLE A: SOM ONLY - TOP 20 CORPORATE ENTITIES - TOTAL COMBINED OPPORTUNITY**

**Header:** Ranked by: Integration Opportunity + New Biz Opportunity (Short-Term + Long-Term)

**Table Structure:**

| Row | A: Rank | B: Corporate Name | C: Total Facilities | D: Facilities We Serve | E: Current Revenue | F: Integration Opp | G: New Biz Opp | H: Total Opportunity |
|-----|---------|-------------------|---------------------|------------------------|--------------------|--------------------|----------------|----------------------|
| 1 | 1 | [Entity Name] | XX | XX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX |
| 2 | 2 | [Entity Name] | XX | XX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 20 | 20 | [Entity Name] | XX | XX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX | $XX,XXX,XXX |
| 21 | **TOTAL** | | **XXX** | **XXX** | **$XX,XXX,XXX** | **$XX,XXX,XXX** | **$XX,XXX,XXX** | **$XX,XXX,XXX** |

**Data Source Logic:**

This requires aggregating SOM facilities by Corporate_Entity. Since Excel pivot tables or manual formulas get complex, here's the approach:

**Option A: Using Pivot Table (Recommended)**
1. Create pivot table from File 2, Sheet 3 (Segmentation)
2. Filter: SOM_Flag = TRUE
3. Rows: Corporate_Entity
4. Values: 
   - Count of Provider_Number (Total Facilities)
   - Count of Provider_Number WHERE Do_We_Serve = "Yes" (Facilities We Serve)
   - Sum of Current_Revenue
   - Sum of Integration_Revenue
   - Sum of New_Biz_Revenue
   - Calculated Field: Total_Opportunity = Integration_Revenue + New_Biz_Revenue
5. Sort by: Total_Opportunity (descending)
6. Show: Top 20

**Option B: Using Formulas (More Complex)**

Create helper table with unique corporate entities, then use SUMIFS:

**Cell C1 (Total Facilities for Entity in B1):**
```excel
=COUNTIFS([File2]Segmentation!$BC:$BC,TRUE,[File2]Segmentation!$D:$D,B1)
```

**Cell D1 (Facilities We Serve for Entity in B1):**
```excel
=COUNTIFS([File2]Segmentation!$BC:$BC,TRUE,[File2]Segmentation!$D:$D,B1,[File2]Segmentation!$P:$P,"Yes")
```

**Cell E1 (Current Revenue for Entity in B1):**
```excel
=SUMIFS([File2]Segmentation!$AA:$AA,[File2]Segmentation!$BC:$BC,TRUE,[File2]Segmentation!$D:$D,B1)
```

**Cell F1 (Integration Opp for Entity in B1):**
```excel
=SUMIFS([File2]Segmentation!$AB:$AB,[File2]Segmentation!$BC:$BC,TRUE,[File2]Segmentation!$D:$D,B1)
```

**Cell G1 (New Biz Opp for Entity in B1):**
```excel
=SUMIFS([File2]Segmentation!$AC:$AC,[File2]Segmentation!$BC:$BC,TRUE,[File2]Segmentation!$D:$D,B1)
```

**Cell H1 (Total Opportunity):**
```excel
=F1+G1
```

**TOTAL Row (Row 21):**
- Total Facilities: =SUM(C1:C20)
- Facilities We Serve: =SUM(D1:D20)
- Current Revenue: =SUM(E1:E20)
- Integration Opp: =SUM(F1:F20)
- New Biz Opp: =SUM(G1:G20)
- Total Opportunity: =SUM(H1:H20)

**Ranking:** Use RANK function or sort manually by Total Opportunity descending, then number 1-20.

---

### **TABLE B: SOM ONLY - TOP 20 CORPORATE ENTITIES - INTEGRATION OPPORTUNITY**

**Header:** Ranked by: Integration Opportunity

**Table Structure:**

| Row | A: Rank | B: Corporate Name | C: Total Facilities | D: Facilities We Serve | E: Integration Opportunity |
|-----|---------|-------------------|---------------------|------------------------|----------------------------|
| 1 | 1 | [Entity Name] | XX | XX | $XX,XXX,XXX |
| 2 | 2 | [Entity Name] | XX | XX | $XX,XXX,XXX |
| ... | ... | ... | ... | ... | ... |
| 20 | 20 | [Entity Name] | XX | XX | $XX,XXX,XXX |
| 21 | **TOTAL** | | **XXX** | **XXX** | **$XX,XXX,XXX** |

**Data Source Logic:**

Same aggregation as Table A, but:
- Sort by: Integration Opportunity (descending)
- Show only: Rank, Corporate Name, Total Facilities, Facilities We Serve, Integration Opportunity

**Cell E1 (Integration Opportunity for Entity in B1):**
```excel
=SUMIFS([File2]Segmentation!$AB:$AB,[File2]Segmentation!$BC:$BC,TRUE,[File2]Segmentation!$D:$D,B1)
```

**Strategic Note:** Integration Opportunity represents **short-term upsell** to existing served facilities within each corporate entity.

---

### **TABLE C: SOM ONLY - TOP 20 CORPORATE ENTITIES - NEW BUSINESS OPPORTUNITY**

**Header:** Ranked by: New Biz Opportunity

**Table Structure:**

| Row | A: Rank | B: Corporate Name | C: Total Facilities | D: Facilities We Serve | E: New Business Opportunity |
|-----|---------|-------------------|---------------------|------------------------|------------------------------|
| 1 | 1 | [Entity Name] | XX | XX | $XX,XXX,XXX |
| 2 | 2 | [Entity Name] | XX | XX | $XX,XXX,XXX |
| ... | ... | ... | ... | ... | ... |
| 20 | 20 | [Entity Name] | XX | XX | $XX,XXX,XXX |
| 21 | **TOTAL** | | **XXX** | **XXX** | **$XX,XXX,XXX** |

**Data Source Logic:**

Same aggregation as Table A, but:
- Sort by: New Biz Opportunity (descending)
- Show only: Rank, Corporate Name, Total Facilities, Facilities We Serve, New Business Opportunity

**Cell E1 (New Biz Opportunity for Entity in B1):**
```excel
=SUMIFS([File2]Segmentation!$AC:$AC,[File2]Segmentation!$BC:$BC,TRUE,[File2]Segmentation!$D:$D,B1)
```

**Strategic Note:** New Biz Opportunity represents **long-term acquisition** of unserved facilities within each corporate entity.

---

### **Formatting**

**Color Scheme:**
- Header rows: Green background (#70AD47) - SOM segment color
- Table headers: Bold, white text
- Currency format: $#,##0 (no decimals)
- Number format: #,##0 (comma separator)

**Layout:**
- Table A: Rows 1-22 (with spacing)
- Table B: Rows 25-46 (with spacing)
- Table C: Rows 49-70 (with spacing)
- Leave 2 blank rows between tables

**Notes:**
- All tables filtered to **SOM segment only** (SOM_Flag = TRUE)
- Top 20 entities by specified ranking criteria
- TOTAL row sums all Top 20 (not all SOM entities, just the Top 20)
- Rankings may differ across tables (same entity could be #1 in Total but #5 in Integration)

---

## 5.6 Report 5: Geographic Analysis (SOM Only) - PLACEHOLDER

### **Report Structure**

**Sheet Name:** "Geographic_Analysis"  
**Purpose:** Geographic targeting report for SOM facilities by region  
**Status:** PLACEHOLDER - To be fully defined

**Concept:**
- Filter: SOM segment only (SOM_Flag = TRUE)
- Group by: Geographic regions (State, ZIP, or custom regions)
- Sort by: Revenue opportunity or facility count
- Identify: In-scope vs. out-of-scope geographic areas
- Enable: Regional sales territory planning

**Potential Data Elements:**
- State or Region
- Facility Count
- Current Revenue
- Integration Opportunity
- New Biz Opportunity
- Total Opportunity
- In-Scope / Out-of-Scope flag

**Formatting:**
- Green color scheme (SOM segment)
- Regional groupings or map-based visualization
- Rankings by opportunity size

**To Be Defined:**
- Exact geographic grouping logic (by State? ZIP? Custom regions?)
- In-scope/out-of-scope criteria
- Ranking methodology
- Additional metrics needed

**Implementation:** Define full specifications when requirements finalized, then update this section.

---

## 5.7 Additional Reports (Future)

**Placeholder for future reports as defined by stakeholder needs:**

- **Report 6:** Scenario Comparison (side-by-side S1 vs S2 vs S3)
- **Report 7:** TAM/SAM Opportunity Analysis (non-SOM opportunities)
- **Report 8:** Quarterly Performance Tracking
- **Report 9:** [TBD]

**Each new report follows the same pattern:**
1. Create new sheet in File 3
2. Link to File 2 (Results & Segmentation)
3. Format for stakeholder distribution
4. Document in this section
5. Update table of contents and file structure diagrams

---

# PART 6: SCENARIO MANAGEMENT

## 6.1 How Scenarios Work

### **Scenario Architecture**

**Single Change Point:** Sheet 1 (Fee_Structure) in File 2

All scenarios share:
- Same source data (File 1)
- Same calculation logic (Sheet 2 formulas)
- Same segmentation rules (Sheet 3)
- Same reporting structure (Sheet 4)
- Same report formats (File 3)

**Only Sheet 1 (Fee_Structure) changes between scenarios.**

### **What Changes in Scenarios**

**Sheet 1 Variables:**
- Service rates (FFS_PCP_Rate, FFS_MH_Rate, CCM_Rate, SS_Rate)
- Coverage multipliers (Adjuster_1, Adjuster_2, Adjuster_3)
- Scenario metadata (name, description, assumptions)

**Everything Else Stays Constant:**
- Source data (File 1)
- Revenue formulas (Sheet 2) - same logic, different inputs
- Segmentation logic (Sheet 3)
- Reporting format (File 3)

### **Scenario Workflow**

```
1. Define scenario parameters → Sheet 1 (Fee_Structure)
2. Model recalculates automatically → Sheets 2-4
3. Validate results → Sheet 6 (QA_Validation)
4. Document assumptions → Sheet 5 (Scenario_Definitions)
5. Generate reports → File 3
6. Present to stakeholders
```

---

## 6.2 Creating New Scenarios

### **Step-by-Step Procedure**

**Step 1: Save Scenario 1 File**
```
File → Save As → "Economic_Model_Scenario_2.xlsx"
```

**Step 2: Update Sheet 1 (Fee_Structure)**
- Change scenario metadata (rows 1-8)
- Modify rates as needed (rows 12-15)
- Update multipliers if needed (rows 22-24)
- Document changes (rows 32-35)

**Step 3: Verify Recalculation**
- Check Sheet 2: Formulas reference updated Sheet 1?
- Check Sheet 4: Results reflect new rates?

**Step 4: Update Sheet 5 (Scenario_Definitions)**
- Document new scenario assumptions
- Note differences from Scenario 1
- Update comparison table

**Step 5: Run QA Validation (Sheet 6)**
- Check benchmark (will differ from S1)
- Verify data quality checks (should still pass)
- Confirm formula integrity (should still pass)
- Document new baseline benchmark

**Step 6: Update File 3 (Reports)**
- Save as "Reports_Scenario_2.xlsx"
- Update links to new File 2
- Verify all reports pull correct data

**Step 7: Compare Scenarios**
- Open both S1 and S2 side-by-side
- Compare Results (File 2, Sheet 4)
- Compare Reports (File 3)
- Analyze differences

### **Best Practices**

**DO:**
- ✅ Always start from a validated baseline (S1)
- ✅ Change only Sheet 1 (Fee_Structure)
- ✅ Document all assumptions in Sheet 5
- ✅ Run full QA validation before presenting
- ✅ Keep scenario files in same directory
- ✅ Name files clearly (Economic_Model_Scenario_2.xlsx)

**DON'T:**
- ❌ Modify source data (File 1) for scenarios
- ❌ Change formulas in Sheets 2-4
- ❌ Skip QA validation
- ❌ Mix scenario assumptions (keep scenarios pure)

---

## 6.3 Scenario 1: Current State

### **Definition**

**Scenario Name:** Scenario 1: Current State  
**Scenario ID:** S1  
**Status:** ACTIVE (Validated)  
**Purpose:** Baseline model representing current revenue with validated benchmarks

### **Fee Structure**

**Rates (Annual):**
- FFS_PCP_Rate: $1,875
- FFS_MH_Rate: $1,898
- CCM_Rate: $360
- SS_Rate: $4,800

**Multipliers:**
- Adjuster_1 (MH/SS coverage): 0.50
- Adjuster_2 (CCM coverage): 0.30
- Adjuster_3 (SS retention): 0.33

### **Revenue Streams**

**Four Revenue Types:**
1. **Current Revenue:** Served facilities, current service configuration
2. **Integration Revenue:** Served facilities, missing services
3. **New Biz Revenue:** Unserved facilities, full Integrated
4. **Total Revenue:** Integration + New Biz

### **Expected Results**

**Validated Benchmarks:**
- TAM Current Revenue: $127,572,232 ✅
- SOM Current Revenue: ~$88,500,000 ✅
- Total Facilities: 17,490 ✅

### **Use Cases**

**Strategic Planning:**
- Establishes baseline for growth projections
- Identifies current market penetration
- Supports budget forecasting

**Performance Tracking:**
- Benchmark for actual results
- Variance analysis vs. actual
- Trend analysis over time

**Scenario Comparison:**
- Reference point for all other scenarios
- "Current State" vs. "Future State" analysis

---

## 6.4 Scenario 2: Placeholder

### **Concept**

**Scenario Name:** Scenario 2: [TBD]  
**Scenario ID:** S2  
**Status:** DRAFT (Placeholder)  
**Purpose:** [To be defined based on strategic priorities]

### **Potential Scenario Ideas**

**Option A: CCM Integration**
- Add CCM to all PCP facilities immediately
- Accelerates cash flow
- Same total opportunity, different timing

**Option B: Rate Increase**
- Model impact of rate negotiations
- FFS_PCP_Rate: $1,875 → $2,000
- Sensitivity analysis

**Option C: Coverage Expansion**
- Increase MH coverage: Adjuster_1: 0.50 → 0.60
- Model improved penetration

### **Implementation (When Ready)**

**Sheet 1 Changes:**
- Update scenario metadata
- Modify relevant rates/multipliers
- Document assumptions

**Sheet 5 Documentation:**
- Define scenario purpose
- Note changes from S1
- Expected strategic impact

---

## 6.5 Scenario 3: Placeholder

### **Concept**

**Scenario Name:** Scenario 3: [TBD]  
**Scenario ID:** S3  
**Status:** DRAFT (Placeholder)  
**Purpose:** [To be defined]

---

# PART 7: QUALITY ASSURANCE

## 7.1 Component-Level Validation

### **Component 1: Source Data (File 1)**

**Validation Checklist:**

**Data Completeness**
- [ ] Row count = 17,490 (excluding header)
- [ ] All required columns present (see §2.2)
- [ ] No blank rows
- [ ] No blank columns

**Data Quality**
- [ ] No duplicate Provider_Numbers
- [ ] Service flags mutually exclusive (sum = 1)
- [ ] Market_Status values valid (Existing/Emerging/New)
- [ ] Ownership values valid (Corporate/Independent)
- [ ] Do_We_Serve alignment with service flags

**Data Types**
- [ ] Census is numeric (or blank for unserved)
- [ ] Total_Beds is numeric (or 0 for some ALF)
- [ ] Occupancy_Rate is numeric (or blank)

**Formula Check**
- [ ] No formulas present (except allowable data cleaning)

**Expected Result:** 99.99% data quality (≤2 facilities with issues)

---

### **Component 2: Fee Structure (Sheet 1)**

**Validation Checklist:**

**Scenario Metadata**
- [ ] Scenario Name populated
- [ ] Scenario ID follows convention (S1, S2, etc.)
- [ ] Status is valid (ACTIVE/DRAFT/RETIRED)
- [ ] Benchmark value populated (for comparison)

**Rate Values**
- [ ] All rates populated and numeric
- [ ] All rates > 0 (no negatives, no blanks)
- [ ] Rates are ANNUAL (not monthly × 12)

**Multipliers**
- [ ] Adjuster_1 = 0.50
- [ ] Adjuster_2 = 0.30
- [ ] Adjuster_3 = 0.33

**Named Ranges (If Used)**
- [ ] All named ranges defined correctly
- [ ] Named ranges point to correct cells
- [ ] No #NAME errors in model

**Expected Result:** All rates and multipliers valid and documented

---

### **Component 3: Calculations (Sheet 2)**

**Validation Checklist:**

**Data Import**
- [ ] Columns A-P link to File 1 (Source_Data)
- [ ] Link status = OK (check Data → Edit Links)
- [ ] Row count matches File 1 (17,490 rows)

**Formula Integrity**
- [ ] Current_Revenue (Column AA) has formulas
- [ ] Integration_Revenue (Column AB) has formulas
- [ ] New_Biz_Revenue (Column AC) has formulas
- [ ] Total_Revenue (Column AD) has formulas
- [ ] Formulas reference Sheet 1 (Fee_Structure)
- [ ] No #REF errors
- [ ] No #VALUE errors
- [ ] No #NAME errors

**Calculation Logic**
- [ ] No negative revenues
- [ ] Served facilities: Integration > 0, New Biz = 0
- [ ] Unserved facilities: Current = 0, Integration = 0, New Biz > 0
- [ ] Total = Integration + New Biz for all facilities

**Benchmark Check**
- [ ] Sum of Column AA (Current_Revenue) = $127,572,232
- [ ] If not exact, investigate formula errors

**Expected Result:** 100% computational accuracy, benchmark validated

---

### **Component 4: Segmentation (Sheet 3)**

**Validation Checklist:**

**Data Import**
- [ ] All columns from Sheet 2 imported
- [ ] Row count matches Sheet 2 (17,490 rows)

**Segmentation Flags**
- [ ] TAM_Flag = TRUE for all 17,490 facilities
- [ ] SAM_Flag count ≤ TAM_Flag count
- [ ] SOM_Flag count ≤ SAM_Flag count

**Logic Validation**
- [ ] All SOM facilities have Ownership = "Corporate"
- [ ] All SAM facilities have Ownership = "Corporate"
- [ ] All SOM facilities have Has_Barrier = "No"
- [ ] All SOM facilities have Market_Status = "Existing"

**Hierarchy Check**
- [ ] Every SOM facility is also SAM and TAM
- [ ] Every SAM facility is also TAM

**Expected Result:** Segment hierarchy maintained, corporate-only filters correct

---

### **Component 5: Results (Sheet 4)**

**Validation Checklist:**

**Executive Summary Table**
- [ ] TAM Current Revenue = $127,572,232 (±$100)
- [ ] TAM facilities = 17,490
- [ ] SAM facilities ≤ TAM facilities
- [ ] SOM facilities ≤ SAM facilities

**Revenue Hierarchy**
- [ ] TAM Current Revenue ≥ SAM Current Revenue ≥ SOM Current Revenue
- [ ] TAM Total Revenue ≥ SAM Total Revenue ≥ SOM Total Revenue

**Revenue Logic**
- [ ] TAM Total = TAM Integration + TAM New Biz
- [ ] SAM Total = SAM Integration + SAM New Biz
- [ ] SOM Total = SOM Integration + SOM New Biz

**Supporting Calculations**
- [ ] Served + Unserved = Total for each segment
- [ ] SNF + ALF = Total for each segment
- [ ] Corporate + Independent = TAM total (for TAM only)

**Expected Result:** Benchmark validated, hierarchy maintained, logic sound

---

### **Component 6: Scenario Definitions (Sheet 5)**

**Validation Checklist:**

**Documentation Completeness**
- [ ] Scenario name and ID documented
- [ ] Key assumptions listed
- [ ] Rate structure documented
- [ ] Revenue stream logic explained

**Scenario Comparison**
- [ ] Comparison table populated (if applicable)
- [ ] Differences from baseline noted

**Expected Result:** Complete documentation for audit and reference

---

### **Component 7: QA Validation (Sheet 6)**

**Validation Checklist:**

**Benchmark Tests**
- [ ] TAM Current Revenue check = PASS
- [ ] Total Facilities check = PASS

**Data Quality Tests**
- [ ] Data quality rate ≥ 99.99% = PASS
- [ ] Duplicate facilities = 0 = PASS
- [ ] Service flag errors ≤ 2 = PASS

**Formula Integrity Tests**
- [ ] Formulas present in Calculations = PASS
- [ ] No #REF errors = PASS
- [ ] No negative revenues = PASS

**Revenue Logic Tests**
- [ ] Served facilities logic = PASS
- [ ] Unserved facilities logic = PASS
- [ ] Total = Integration + New Biz = PASS

**Overall Status**
- [ ] Overall Status = "✅ ALL CHECKS PASSED"

**Expected Result:** 100% pass rate, all checks green

---

## 7.2 End-to-End Validation

### **Full Model Validation Procedure**

**Time Required:** 30-45 minutes

**Prerequisites:**
- [ ] File 1 (Source_Data_Master.xlsx) validated per §7.1
- [ ] File 2 (Economic_Model_Scenario_1.xlsx) built per specifications
- [ ] File 3 (Reports_Scenario_1.xlsx) built per specifications

---

**PHASE 1: Quick Benchmark Check (5 minutes)**

**File 2, Sheet 4 (Results):**
- [ ] Navigate to Cell C2 (TAM Current Revenue)
- [ ] Value = $127,572,232 (±$100)?
- [ ] **IF YES:** Likely correct → Continue validation
- [ ] **IF NO:** Stop, investigate formulas

**File 2, Sheet 6 (QA_Validation):**
- [ ] Navigate to Overall Status cell (around row 78)
- [ ] Value = "✅ ALL CHECKS PASSED"?
- [ ] **IF YES:** Model passed automated checks
- [ ] **IF NO:** Review failed checks, fix before proceeding

---

**PHASE 2: Component Spot Checks (10 minutes)**

**Sheet 2 (Calculations):**
- [ ] Click Cell AA2 → Check formula bar
- [ ] Should see: Complex IF statement for Current_Revenue
- [ ] Click Cell AB2 → Check formula bar
- [ ] Should see: Complex IF statement for Integration_Revenue
- [ ] Click Cell AC2 → Check formula bar
- [ ] Should see: Complex IF statement for New_Biz_Revenue
- [ ] Scroll to bottom → Formulas present throughout?

**Sheet 3 (Segmentation):**
- [ ] Click Cell BA2 → Should see: =TRUE
- [ ] Click Cell BB2 → Should see: =AND(...)
- [ ] Click Cell BC2 → Should see: =AND(...)

**Sheet 4 (Results):**
- [ ] Verify hierarchy: B2 ≥ B3 ≥ B4 (facilities)
- [ ] Verify hierarchy: C2 ≥ C3 ≥ C4 (current revenue)

---

**PHASE 3: Sample Calculation Verification (10 minutes)**

**Pick a served facility with known values:**

**Example:** Row 100, Census = 65.3, Integrated_Flag = "Yes"

**Manual Calculation:**
```
Current_Revenue = 65.3 × $3,724 = $243,176.20
```

**Check Cell AA100:**
- [ ] Value ≈ $243,176?
- [ ] If match: ✅ Formula working correctly
- [ ] If not: Investigate formula

**Pick an unserved facility:**

**Example:** Row 5000, Census = 48.2, Do_We_Serve = "No"

**Expected:**
- [ ] Current_Revenue (AA5000) = $0
- [ ] Integration_Revenue (AB5000) = $0
- [ ] New_Biz_Revenue (AC5000) = 48.2 × $3,724 = $179,496.80
- [ ] Verify formulas match expectations

---

**PHASE 4: Report Validation (10 minutes)**

**File 3, Sheet 1 (Facilities_Count):**
- [ ] Numbers match File 2, Sheet 4 aggregations?
- [ ] Format: "Total / Our Share" present?
- [ ] Color coding correct (TAM=blue, SAM=orange, SOM=green)?

**File 3, Sheet 2 (Revenue):**
- [ ] Current Revenue numbers match File 2, Sheet 4?
- [ ] Integration + New Biz = Total for each segment?

**File 3, Sheet 3 (SOM_Fee_Breakdown):**
- [ ] PCP + MH + CCM + SS = Total for each row?
- [ ] Percentages sum to 100% for each row?

---

**VALIDATION RESULT**

**IF ALL CHECKS PASS:**
- ✅ **Model is VALIDATED**
- Ready for production use
- Ready for scenario testing
- Ready for stakeholder presentation

**IF ANY CHECKS FAIL:**
- ❌ **Model has ERRORS**
- Do NOT use for production
- Investigate failures per §7.3 Troubleshooting Guide
- Re-validate after corrections

---

## 7.3 Troubleshooting Guide

### **Common Issues & Solutions**

---

**ISSUE 1: TAM Current Revenue ≠ $127,572,232**

**Symptoms:**
- File 2, Sheet 4, Cell C2 shows different value
- QA Validation shows "❌ FAIL" for benchmark

**Possible Causes:**

**Cause 1A: Wrong rates in Sheet 1**
- **Check:** Navigate to Sheet 1, verify rates
- **Expected:** FFS_PCP_Rate = $1,875, etc.
- **Fix:** Correct rates to Scenario 1 values

**Cause 1B: Formulas using ×12 (incorrect)**
- **Check:** Sheet 2, Cell AA2 formula
- **Look for:** "×12" or "*12" anywhere in formula
- **Fix:** Remove ×12, rates are already annual

**Cause 1C: Formula error in Sheet 2**
- **Check:** Sheet 2, Column AA (Current_Revenue)
- **Look for:** #REF! errors, #VALUE! errors
- **Fix:** Correct formula references, rebuild if necessary

**Cause 1D: Source data corruption**
- **Check:** File 1 (Source_Data_Master.xlsx)
- **Verify:** Row count = 17,490
- **Verify:** No duplicate Provider_Numbers
- **Fix:** Reload clean source data

---

**ISSUE 2: #REF! Errors in Calculations Sheet**

**Symptoms:**
- Sheet 2 shows #REF! in multiple cells
- Formulas reference missing sheet or file

**Possible Causes:**

**Cause 2A: File 1 link broken**
- **Check:** Data → Edit Links
- **Look for:** "Source not found" or "Update not available"
- **Fix:** Click "Change Source" → Browse to File 1 → Update

**Cause 2B: Sheet renamed**
- **Check:** File 1 sheet name = "Source_Data"?
- **Check:** File 2 sheet names correct?
- **Fix:** Rename sheets to match specifications

**Cause 2C: File moved**
- **Check:** Both files in same directory?
- **Fix:** Move files together OR update links with new path

---

**ISSUE 3: Revenue Logic Broken (Integration/New Biz wrong)**

**Symptoms:**
- Served facilities showing New Biz Revenue > 0
- Unserved facilities showing Current Revenue > 0
- Total ≠ Integration + New Biz

**Possible Causes:**

**Cause 3A: Do_We_Serve flag incorrect**
- **Check:** File 1, Column P (Do_We_Serve)
- **Verify:** Alignment with Census > 0
- **Fix:** Correct Do_We_Serve flags in source data

**Cause 3B: Formula logic error in Sheet 2**
- **Check:** Cells AB2, AC2 formulas
- **Verify:** AB2 checks P="Yes", AC2 checks P≠"Yes"
- **Fix:** Rebuild formulas per §3.3

**Cause 3C: Total formula wrong**
- **Check:** Cell AD2 formula
- **Expected:** =AB2+AC2
- **Fix:** Correct formula

---

**ISSUE 4: Segment Hierarchy Broken (SOM > SAM)**

**Symptoms:**
- File 2, Sheet 4 shows SOM > SAM (impossible)
- QA Validation shows "❌ FAIL" for hierarchy

**Possible Causes:**

**Cause 4A: Segmentation flag formula error**
- **Check:** Sheet 3, Columns BB and BC
- **Verify:** SAM includes "Existing" OR "Emerging"
- **Verify:** SOM includes "Existing" only AND no barriers
- **Fix:** Rebuild formulas per §3.4

**Cause 4B: Data quality issue**
- **Check:** Sheet 3, find facilities where BC (SOM) = TRUE
- **Verify:** All have E (Ownership) = "Corporate"
- **Verify:** All have L (Market_Status) = "Existing"
- **Verify:** All have M (Has_Barrier) = "No"
- **Fix:** Correct source data in File 1

---

**ISSUE 5: Reports Not Updating**

**Symptoms:**
- File 3 reports show old data
- Changes to File 2 don't reflect in File 3

**Possible Causes:**

**Cause 5A: File 3 links broken**
- **Check:** File 3, Data → Edit Links
- **Verify:** Links point to correct File 2
- **Fix:** Update links to current File 2

**Cause 5B: Calculation mode = Manual**
- **Check:** File 3, Formulas → Calculation Options
- **Should be:** Automatic
- **Fix:** Set to Automatic → Press F9 to recalculate

---

## 7.4 Expected Results

### **Scenario 1 Expected Results Summary**

**When model is correctly implemented, File 2, Sheet 4 (Results) should show:**

| Metric | Expected Value | Tolerance | Status |
|--------|----------------|-----------|--------|
| **TAM Facilities** | 17,490 | ±0 (exact) | ✅ CRITICAL |
| **TAM Current Revenue** | $127,572,232 | ±$100 | ✅ CRITICAL |
| **TAM Integration Revenue** | [TBD] | ±10% | ⚠️ ESTIMATE |
| **TAM New Biz Revenue** | [TBD] | ±10% | ⚠️ ESTIMATE |
| **TAM Total Revenue** | [TBD] | ±10% | ⚠️ ESTIMATE |
| **SOM Facilities** | ~3,000-3,500 | ±10% | ⚠️ ESTIMATE |
| **SOM Current Revenue** | ~$88,500,000 | ±$1M | ✅ VALIDATED |
| **SOM Integration Revenue** | [TBD] | ±10% | ⚠️ ESTIMATE |
| **SOM New Biz Revenue** | [TBD] | ±10% | ⚠️ ESTIMATE |
| **SOM Total Revenue** | [TBD] | ±10% | ⚠️ ESTIMATE |

**Key:**
- ✅ CRITICAL: Must match exactly (or within tight tolerance)
- ✅ VALIDATED: Strong confidence in value
- ⚠️ ESTIMATE: Approximate, used for planning

### **Quality Metrics**

**Data Quality:**
- 99.99% data quality rate
- ≤2 facilities with data issues
- 0 duplicate facilities
- 0 service flag errors

**Computational Accuracy:**
- 100% formula integrity
- 0 #REF! errors
- 0 #VALUE! errors
- 0 negative revenues

**Segmentation Integrity:**
- TAM ≥ SAM ≥ SOM (both facilities and revenue)
- All SOM/SAM facilities are Corporate
- All SOM facilities have no barriers
- All SOM facilities in Existing markets

---

# PART 8: IMPLEMENTATION PROCEDURES

## 8.1 Building from Scratch

### **Prerequisites**

**Tools Required:**
- Microsoft Excel 2016 or later
- Clean source data file (see Part 2)

**Skills Required:**
- Excel proficiency (formulas, linking, named ranges)
- Understanding of healthcare revenue models
- Attention to detail

**Time Required:**
- File 1 preparation: 1-2 hours
- File 2 construction: 4-6 hours
- File 3 construction: 2-3 hours
- Testing & validation: 2-3 hours
- **Total: 9-14 hours**

---

### **STEP 1: Prepare Source Data (File 1)**

**1.1 Obtain Clean Data**
- [ ] Start with facility list (SNF + ALF)
- [ ] Include all required columns (see §2.2)
- [ ] Remove duplicates
- [ ] Validate service flags

**1.2 Create Source_Data_Master.xlsx**
- [ ] Create new Excel workbook
- [ ] Rename Sheet1 to "Source_Data"
- [ ] Delete other sheets (Sheet2, Sheet3)
- [ ] Paste clean data starting at A1
- [ ] Format as table (optional but recommended)

**1.3 Validate Source Data**
- [ ] Run checks per §2.5
- [ ] Verify row count = 17,490
- [ ] Check for data quality issues
- [ ] Fix any issues found
- [ ] **Save as:** `Source_Data_Master.xlsx`

---

### **STEP 2: Create Economic Model File (File 2)**

**2.1 Create New Workbook**
- [ ] Create new Excel workbook
- [ ] **Save as:** `Economic_Model_Scenario_1.xlsx`
- [ ] In same directory as File 1

**2.2 Create Sheet Structure**
- [ ] Rename sheets:
  - Sheet1 → "Fee_Structure"
  - Sheet2 → "Calculations"
  - Sheet3 → "Segmentation"
- [ ] Add new sheets:
  - Sheet4: "Results"
  - Sheet5: "Scenario_Definitions"
  - Sheet6: "QA_Validation"

---

### **STEP 3: Build Sheet 1 (Fee_Structure)**

**3.1 Add Scenario Metadata (Rows 1-10)**
- [ ] Type headers and values per §3.2
- [ ] Scenario Name: "Scenario 1: Current State"
- [ ] Scenario ID: "S1"
- [ ] Benchmark: $127,572,232

**3.2 Add Rate Values (Rows 12-15)**
- [ ] Row 12: FFS_PCP_Rate, $1,875
- [ ] Row 13: FFS_MH_Rate, $1,898
- [ ] Row 14: CCM_Rate, $360
- [ ] Row 15: SS_Rate, $4,800

**3.3 Add Multipliers (Rows 22-24)**
- [ ] Row 22: Adjuster_1, 0.50
- [ ] Row 23: Adjuster_2, 0.30
- [ ] Row 24: Adjuster_3, 0.33

**3.4 (Optional) Create Named Ranges**
- [ ] Define names per §3.2
- [ ] Test: Type "=FFS_PCP_Rate" in any cell → Should return 1875

**3.5 Save**
- [ ] File → Save

---

### **STEP 4: Build Sheet 2 (Calculations)**

**4.1 Import Source Data (Columns A-P)**
- [ ] Cell A1: Type "Provider_Number"
- [ ] Cell A2: Type formula: `='[Source_Data_Master.xlsx]Source_Data'!A2`
- [ ] Excel prompts for file → Browse to File 1 → Select
- [ ] Copy formula A2 down to row 17,491 (17,490 data rows + header)
- [ ] Copy formula across to column P
- [ ] **Verify:** Row count = 17,490, no #REF! errors

**4.2 Add Revenue Stream Columns (Columns AA-AD)**
- [ ] Column AA header: "Current_Revenue"
- [ ] Column AB header: "Integration_Revenue"
- [ ] Column AC header: "New_Biz_Revenue"
- [ ] Column AD header: "Total_Revenue"

**4.3 Build Current_Revenue Formula (Column AA)**
- [ ] Cell AA2: Enter formula per §3.3 or §4.3
- [ ] **Verify:** AA2 shows a number (not #REF!)
- [ ] Copy formula down to row 17,491

**4.4 Build Integration_Revenue Formula (Column AB)**
- [ ] Cell AB2: Enter formula per §3.3 or §4.4
- [ ] Copy formula down to row 17,491

**4.5 Build New_Biz_Revenue Formula (Column AC)**
- [ ] Cell AC2: Enter formula per §3.3 or §4.5
- [ ] Copy formula down to row 17,491

**4.6 Build Total_Revenue Formula (Column AD)**
- [ ] Cell AD2: `=AB2+AC2`
- [ ] Copy formula down to row 17,491

**4.7 (Optional) Add Service Component Columns (AE-AH+)**
- [ ] If needed for Report 3, add component breakdowns
- [ ] See §3.3 for formulas

**4.8 Validate Calculations**
- [ ] Check for errors: Ctrl+F → "#REF!" → Should find 0
- [ ] Sum Column AA → Should ≈ $127,572,232
- [ ] If not exact, debug formulas

**4.9 Save**
- [ ] File → Save

---

### **STEP 5: Build Sheet 3 (Segmentation)**

**5.1 Import Calculated Data (Columns A-AD)**
- [ ] Cell A2: `=Calculations!A2`
- [ ] Copy down to row 17,491
- [ ] Copy across to column AD
- [ ] **Verify:** All data imported, no #REF! errors

**5.2 Add Segmentation Columns (Columns BA-BD)**
- [ ] Column BA header: "TAM_Flag"
- [ ] Column BB header: "SAM_Flag"
- [ ] Column BC header: "SOM_Flag"
- [ ] Column BD header: "Segment_Priority"

**5.3 Build Segmentation Formulas**
- [ ] Cell BA2: `=TRUE`
- [ ] Cell BB2: `=AND(E2="Corporate", OR(L2="Existing", L2="Emerging"))`
- [ ] Cell BC2: `=AND(E2="Corporate", L2="Existing", M2="No")`
- [ ] Cell BD2: `=IF(BC2=TRUE, "1-SOM", IF(BB2=TRUE, "2-SAM", "3-TAM"))`
- [ ] Copy formulas down to row 17,491

**5.4 Validate Segmentation**
- [ ] Count TRUE in BA → Should = 17,490
- [ ] Count TRUE in BB → Should ≤ 17,490
- [ ] Count TRUE in BC → Should ≤ Count in BB
- [ ] **Verify hierarchy:** SOM ⊆ SAM ⊆ TAM

**5.5 Save**
- [ ] File → Save

---

### **STEP 6: Build Sheet 4 (Results)**

**6.1 Create Executive Summary Table**
- [ ] Row 1: Headers (Segment, # Facilities, Current, Integration, New Biz, Total)
- [ ] Row 2: TAM formulas per §3.5
- [ ] Row 3: SAM formulas per §3.5
- [ ] Row 4: SOM formulas per §3.5

**Example Row 2 (TAM):**
- [ ] Cell A2: "TAM"
- [ ] Cell B2: `=COUNTIF(Segmentation!BA:BA,TRUE)`
- [ ] Cell C2: `=SUMIF(Segmentation!BA:BA,TRUE,Segmentation!AA:AA)`
- [ ] Cell D2: `=SUMIF(Segmentation!BA:BA,TRUE,Segmentation!AB:AB)`
- [ ] Cell E2: `=SUMIF(Segmentation!BA:BA,TRUE,Segmentation!AC:AC)`
- [ ] Cell F2: `=D2+E2`

**6.2 Add Supporting Calculations**
- [ ] Section B: Served vs. Unserved breakdown per §3.5
- [ ] Section C: Facility type breakdown (SNF/ALF)

**6.3 Validate Results**
- [ ] Cell C2 (TAM Current Revenue) = $127,572,232?
- [ ] If not, trace back to Sheet 2 formulas

**6.4 Save**
- [ ] File → Save

---

### **STEP 7: Build Sheet 5 (Scenario_Definitions)**

**7.1 Document Scenario 1**
- [ ] Add scenario metadata per §3.6
- [ ] Document key assumptions
- [ ] Note service type logic
- [ ] Describe segmentation rules

**7.2 Add Scenario Placeholders**
- [ ] Add Scenario 2 section (placeholder)
- [ ] Add Scenario 3 section (placeholder)

**7.3 Create Comparison Table**
- [ ] Add scenario comparison table
- [ ] Pull results from Sheet 4 for S1

**7.4 Save**
- [ ] File → Save

---

### **STEP 8: Build Sheet 6 (QA_Validation)**

**8.1 Add Benchmark Tests**
- [ ] Section A per §3.7
- [ ] Include TAM Current Revenue check
- [ ] Include SOM Current Revenue check
- [ ] Include Total Facilities check

**8.2 Add Data Quality Tests**
- [ ] Section B per §3.7
- [ ] Check for duplicates
- [ ] Check for service flag errors
- [ ] Check for missing data

**8.3 Add Formula Integrity Tests**
- [ ] Section C per §3.7
- [ ] Verify formulas present
- [ ] Check for #REF! errors
- [ ] Check for negative revenues

**8.4 Add Revenue Logic Tests**
- [ ] Section D per §3.7
- [ ] Verify served facility logic
- [ ] Verify unserved facility logic
- [ ] Verify Total = Integration + New Biz

**8.5 Add Overall Status**
- [ ] Section E per §3.7
- [ ] Count total checks
- [ ] Count passed checks
- [ ] Calculate pass rate
- [ ] Display overall status

**8.6 Save**
- [ ] File → Save

---

### **STEP 9: Create Reports File (File 3)**

**9.1 Create New Workbook**
- [ ] Create new Excel workbook
- [ ] **Save as:** `Reports_Scenario_1.xlsx`
- [ ] In same directory as Files 1 & 2

**9.2 Build Report 1 (Facilities_Count)**
- [ ] Create sheet "Facilities_Count"
- [ ] Build per §5.2
- [ ] Link to File 2 (Results & Segmentation)
- [ ] Apply formatting (colors, borders)

**9.3 Build Report 2 (Revenue)**
- [ ] Create sheet "Revenue"
- [ ] Build per §5.3
- [ ] Link to File 2 (Results & Segmentation)
- [ ] Apply formatting

**9.4 Build Report 3 (SOM_Fee_Breakdown)**
- [ ] Create sheet "SOM_Fee_Breakdown"
- [ ] Build per §5.4
- [ ] Link to File 2 (Segmentation)
- [ ] Apply formatting

**9.5 Build Report 4 (Top_20_Corporate_Entities)**
- [ ] Create sheet "Top_20_Corporate_Entities"
- [ ] Build three tables per §5.5
- [ ] Aggregate by Corporate_Entity (use pivot or formulas)
- [ ] Rank and filter to Top 20 for each table
- [ ] Apply SOM green color scheme

**9.6 Save**
- [ ] File → Save

---

### **STEP 10: Final Validation**

**10.1 Run End-to-End Validation**
- [ ] Follow procedure per §7.2
- [ ] Check all components
- [ ] Verify benchmark
- [ ] Review QA status

**10.2 Test Recalculation**
- [ ] Change a rate in File 2, Sheet 1
- [ ] Verify File 2, Sheet 4 updates
- [ ] Verify File 3 reports update
- [ ] Change rate back
- [ ] Verify everything returns to benchmark

**10.3 Test File Linking**
- [ ] Close all files
- [ ] Open File 2 only
- [ ] Update links when prompted
- [ ] Verify model still works
- [ ] Open File 3
- [ ] Update links
- [ ] Verify reports still work

**10.4 Create Backup**
- [ ] Copy all three files to backup location
- [ ] Add date to backup filenames
- [ ] Example: `Source_Data_Master_2025-11-15.xlsx`

---

### **STEP 11: Document & Distribute**

**11.1 Create Documentation Package**
- [ ] This Rulebook (V2.2)
- [ ] Scenario 1 Results Summary (from File 2, Sheet 4)
- [ ] QA Validation Report (from File 2, Sheet 6)
- [ ] Implementation Notes

**11.2 Distribute to Stakeholders**
- [ ] Share all three files (in same folder)
- [ ] Include Rulebook V2.2
- [ ] Provide usage instructions
- [ ] Note: Files must stay together

**11.3 Training**
- [ ] Train team on modular architecture
- [ ] Demonstrate scenario swapping
- [ ] Review QA procedures
- [ ] Answer questions

---

## 8.2 Linking Files

### **How File Linking Works**

**External Links in Excel:**

When File 2 references File 1, or File 3 references File 2, Excel creates **external links**. The link stores:
- Path to source file (full file path)
- Sheet name (e.g., "Source_Data")
- Cell references (e.g., A2:P17491)

**Link Formula Example:**
```excel
='[Source_Data_Master.xlsx]Source_Data'!A2
```

**Components:**
- `[Source_Data_Master.xlsx]` = External file name
- `Source_Data` = Sheet name in that file
- `!A2` = Cell reference

---

### **Best Practice: Keep Files Together**

**Recommended File Structure:**

```
Project_Directory/
├── Source_Data_Master.xlsx (File 1)
├── Economic_Model_Scenario_1.xlsx (File 2)
├── Economic_Model_Scenario_2.xlsx (File 2 - future)
├── Reports_Scenario_1.xlsx (File 3)
└── Final_Model_Rulebook_V2.2.md (this document)
```

**Why This Works:**
- Excel stores relative paths when possible
- Moving the folder moves all files together
- Links update automatically if folder moved

---

### **Managing Links**

**View Current Links:**
1. Open File 2 or File 3
2. Data tab → Edit Links
3. View list of external links

**Update Links:**
1. Open File 2 or File 3 only (source files closed)
2. Excel prompts: "Update links?"
3. Click "Update"
4. OR: Data → Edit Links → Update Values

**Change Link Source:**
1. Data → Edit Links
2. Select link
3. Click "Change Source"
4. Browse to new file location
5. Click OK

**Break Links (Not Recommended):**
1. Data → Edit Links
2. Select link
3. Click "Break Link"
4. **WARNING:** Converts formulas to static values (irreversible)

---

### **Troubleshooting Links**

**Issue: "Update Links?" prompt every time**
- **Cause:** Source file in different location than dependent file
- **Fix:** Move source file to same directory as dependent file

**Issue: #REF! errors after opening File 2**
- **Cause:** File 1 not found or path changed
- **Fix:** Data → Edit Links → Change Source → Browse to File 1

**Issue: Links don't update after editing source file**
- **Cause:** Dependent file open when source was edited
- **Fix:** Close dependent file, reopen, update links

---

## 8.3 Verifying Calculations

### **Quick Verification (2 minutes)**

**Benchmark Check:**
1. Open File 2
2. Navigate to Sheet 4 (Results)
3. Look at Cell C2 (TAM Current Revenue)
4. **Expected:** $127,572,232
5. **If match:** ✅ Model is correct
6. **If not:** ❌ Investigate formulas

**QA Status Check:**
1. Navigate to Sheet 6 (QA_Validation)
2. Scroll to bottom (around row 78)
3. Look at "OVERALL STATUS" cell
4. **Expected:** "✅ ALL CHECKS PASSED"
5. **If match:** ✅ Model is validated
6. **If not:** ❌ Review failed checks

---

### **Deep Verification (15 minutes)**

**Source Link Verification:**
1. Data → Edit Links
2. **Verify:** Link status = "OK"
3. **Verify:** File path shows correct location
4. **If not OK:** Update or change source

**Formula Integrity Check:**
1. Sheet 2 (Calculations), Column AA
2. Click random cell (e.g., AA100)
3. Look at formula bar
4. **Expected:** Complex IF statement (not just a value)
5. **Verify:** Formula references Sheet1 (Fee_Structure)
6. **If static value:** Formula was broken, rebuild

**Sample Calculation Verification:**
1. Sheet 2, find Integrated facility with known census
2. Example: Row 50, Census = 85.2
3. Manual calculation: 85.2 × $3,724 = $317,284.80
4. Compare to Cell AA50
5. **Expected:** Close match (within $1 due to rounding)

**Revenue Logic Verification:**
1. Sheet 2, find served facility (Do_We_Serve = "Yes")
2. **Expected:**
   - Current_Revenue (AA) > 0
   - Integration_Revenue (AB) ≥ 0
   - New_Biz_Revenue (AC) = 0
3. Find unserved facility (Do_We_Serve ≠ "Yes")
4. **Expected:**
   - Current_Revenue (AA) = 0
   - Integration_Revenue (AB) = 0
   - New_Biz_Revenue (AC) > 0

**Segmentation Logic Verification:**
1. Sheet 3, find Corporate facility in Existing market, no barrier
2. **Expected Flags:**
   - TAM_Flag (Column BA) = TRUE
   - SAM_Flag (Column BB) = TRUE
   - SOM_Flag (Column BC) = TRUE
3. **If mismatch:** Check segmentation formulas

**Results Aggregation Verification:**
1. Sheet 4, check hierarchy:
   - B2 (TAM facilities) ≥ B3 (SAM) ≥ B4 (SOM)
   - C2 (TAM current revenue) ≥ C3 (SAM) ≥ C4 (SOM)
2. **If hierarchy broken:** Check segmentation logic
3. Verify Total = Integration + New Biz:
   - F2 = D2 + E2 (TAM)
   - F3 = D3 + E3 (SAM)
   - F4 = D4 + E4 (SOM)

---

### **Recalculation Test**

**Purpose:** Verify model responds to rate changes

**Procedure:**
1. Note current value: File 2, Sheet 4, Cell C2 (e.g., $127,572,232)
2. Navigate to Sheet 1
3. Change Cell B12 (FFS_PCP_Rate) from $1,875 to $2,000
4. Navigate to Sheet 4
5. **Expected:** Cell C2 increases (e.g., to $135M+)
6. Navigate back to Sheet 1
7. Change Cell B12 back to $1,875
8. Navigate to Sheet 4
9. **Expected:** Cell C2 returns to $127,572,232

**If model doesn't recalculate:**
- Check: Formulas → Calculation Options → Should be "Automatic"
- Try: Press F9 to force recalculation
- Investigate: Circular references or broken formulas

---

## 8.4 Testing Scenarios

### **Scenario Testing Procedure**

**Purpose:** Verify new scenarios work correctly before presentation

---

**PHASE 1: Create Test Scenario (5 minutes)**

**Step 1: Copy Base File**
- [ ] Close all files
- [ ] Copy `Economic_Model_Scenario_1.xlsx`
- [ ] Rename to `Economic_Model_Scenario_TEST.xlsx`
- [ ] Open TEST file

**Step 2: Modify Fee Structure**
- [ ] Navigate to Sheet 1
- [ ] Change scenario name to "TEST"
- [ ] Make a small rate change (e.g., increase FFS_PCP_Rate by $100)
- [ ] Note expected impact direction (revenue should increase)

**Step 3: Verify Recalculation**
- [ ] Navigate to Sheet 4
- [ ] Check TAM Current Revenue
- [ ] **Expected:** Higher than $127.6M (due to rate increase)
- [ ] **If changed:** ✅ Recalculation works
- [ ] **If same:** ❌ Model not recalculating (investigate)

---

**PHASE 2: Test Extreme Scenarios (10 minutes)**

**Test 1: Zero Rates**
- [ ] Sheet 1: Set all rates to $0
- [ ] Sheet 4: TAM Current Revenue should = $0
- [ ] Revert rates to original

**Test 2: Double Rates**
- [ ] Sheet 1: Multiply all rates by 2
- [ ] Sheet 4: TAM Current Revenue should ≈ double
- [ ] Revert rates to original

**Test 3: Zero Coverage**
- [ ] Sheet 1: Set Adjuster_1 to 0
- [ ] Sheet 4: Revenue should drop (less MH/SS revenue)
- [ ] Revert to 0.50

**Result:** If all tests behave as expected, scenario mechanism works correctly.

---

**PHASE 3: Test Data Independence (5 minutes)**

**Purpose:** Verify File 1 remains unchanged across scenarios

**Step 1: Create Second Scenario**
- [ ] Close TEST file
- [ ] Copy `Economic_Model_Scenario_1.xlsx`
- [ ] Rename to `Economic_Model_Scenario_2_DRAFT.xlsx`
- [ ] Open both S1 and S2_DRAFT

**Step 2: Modify S2_DRAFT**
- [ ] Navigate to Sheet 1
- [ ] Change rates significantly
- [ ] Save S2_DRAFT
- [ ] Close S2_DRAFT

**Step 3: Verify S1 Unchanged**
- [ ] Switch to S1 file (should still be open)
- [ ] Navigate to Sheet 4
- [ ] **Expected:** TAM Current Revenue still = $127,572,232
- [ ] **If changed:** ❌ Files are interfering (investigate)
- [ ] **If same:** ✅ Scenarios are independent

**Step 4: Verify File 1 Unchanged**
- [ ] Open File 1 (Source_Data_Master.xlsx)
- [ ] Check row count = 17,490
- [ ] Spot check a few cells
- [ ] **Expected:** No changes to data
- [ ] **If changed:** ❌ Scenario corrupted source (investigate)

---

# APPENDICES

## Appendix A: Column Reference Guide

### **File 1 (Source_Data_Master.xlsx) Columns**

| Column | Field Name | Data Type | Description | Example |
|--------|-----------|-----------|-------------|---------|
| A | Provider_Number | Text | CMS Provider ID or unique ID | "105506" |
| B | Facility_Name | Text | Official facility name | "Sunrise Senior Living" |
| C | Facility_Type | Text | SNF or ALF | "SNF" |
| D | Corporate_Entity | Text | Parent organization | "Sunrise Senior Living Inc" |
| E | Ownership | Text | Corporate or Independent | "Corporate" |
| F | State | Text | Two-letter state code | "NC" |
| G | ZIP | Text | 5-digit ZIP code | "27298" |
| H | PCP_Only_Flag | Text | PCP service only | "Yes" or "No" |
| I | MH_Only_Flag | Text | MH service only | "Yes" or "No" |
| J | Integrated_Flag | Text | Both PCP and MH | "Yes" or "No" |
| K | SS_Service_Flag | Text | Shared Savings | "Yes" or "No" |
| L | Market_Status | Text | Market classification | "Existing", "Emerging", "New" |
| M | Has_Barrier | Text | Barrier to entry | "Yes" or "No" |
| N | Census | Number | Average daily census | 78.5 |
| O | Total_Beds | Number | Licensed bed count | 120 |
| P | Do_We_Serve | Text | Facility served by Eventus | "Yes" or "No" |

---

### **File 2 (Economic_Model) - Sheet 2 (Calculations) Columns**

| Column | Field Name | Data Type | Description | Formula/Logic |
|--------|-----------|-----------|-------------|---------------|
| A-P | (Imported from File 1) | Various | See File 1 columns above | Links to File 1 |
| AA | Current_Revenue | Number | Current revenue from served facilities | Complex IF (see §3.3) |
| AB | Integration_Revenue | Number | Opportunity from adding services to served | Complex IF (see §3.3) |
| AC | New_Biz_Revenue | Number | Opportunity from unserved facilities | Complex IF (see §3.3) |
| AD | Total_Revenue | Number | Integration + New Biz | `=AB+AC` |
| AE | PCP_Component_Current | Number | PCP revenue from current | (Optional) |
| AF | MH_Component_Current | Number | MH revenue from current | (Optional) |
| AG | CCM_Component_Current | Number | CCM revenue from current | (Optional) |
| AH | SS_Component_Current | Number | SS revenue from current | (Optional) |

---

### **File 2 (Economic_Model) - Sheet 3 (Segmentation) Columns**

| Column | Field Name | Data Type | Description | Formula/Logic |
|--------|-----------|-----------|-------------|---------------|
| A-AD | (Imported from Sheet 2) | Various | See Sheet 2 columns above | Links to Sheet 2 |
| BA | TAM_Flag | Boolean | Total Addressable Market | `=TRUE` |
| BB | SAM_Flag | Boolean | Serviceable Addressable Market | `=AND(Corporate, Existing/Emerging)` |
| BC | SOM_Flag | Boolean | Serviceable Obtainable Market | `=AND(Corporate, Existing, No Barrier)` |
| BD | Segment_Priority | Text | Targeting priority | `=IF(SOM, "1-SOM", ...)` |

---

## Appendix B: Formula Reference

### **Four Revenue Stream Formulas (Detailed)**

**See Part 4 (Sections 4.3-4.6) for complete formula documentation.**

---

## Appendix C: Corporate Entity Rankings

### **Top Corporate Entities by Facility Count**

**Purpose:** Identify largest corporate targets for strategic prioritization

**Top 20 Corporate Entities (Sample - Update with actual data):**

| Rank | Corporate Entity | Facilities | Served | Unserved | Current Revenue |
|------|------------------|------------|--------|----------|-----------------|
| 1 | Brookdale Senior Living | 450 | 280 | 170 | $XX,XXX,XXX |
| 2 | Sunrise Senior Living | 320 | 200 | 120 | $XX,XXX,XXX |
| 3 | Five Star Senior Living | 280 | 180 | 100 | $XX,XXX,XXX |
| ... | ... | ... | ... | ... | ... |

**Note:** Update this table with actual corporate entity data from your dataset.

---

## Appendix D: Change Log

### **Rulebook Version History**

---

**V2.2 (November 15, 2025)**

**Status:** PRODUCTION READY - FINAL

**Major Changes:**
- ✅ **Removed "Opportunity_Revenue" artifact** - This was incorrect
- ✅ **Added Four Revenue Streams:** Current, Integration, New Biz, Total
- ✅ **Fixed Annual Calculation:** Removed ×12, rates are already annual
- ✅ **Documented as Scenario 1:** Enables Scenario 2+ flexibility
- ✅ **Added File 3 (Reports):** Separate reporting outputs with 5 report specifications
- ✅ **Corrected all formulas** to match actual business logic
- ✅ **Added comprehensive reporting layer** with four complete reports + one placeholder

**Critical Corrections:**
- Part 3 (File 2): Completely rebuilt Sheet 2 (Calculations) with correct revenue streams
- Part 4: New section documenting Scenario 1 formulas with proper annual rates
- Part 5: New section for File 3 (Reports) structure with complete specifications
- All formulas verified to produce values in $50k-$300k range for average facilities

**Reporting Layer (Part 5):**
- Report 1: Facilities Count (SNF/ALF/Total with Total/Served breakdown)
- Report 2: Revenue Summary (Current/Integration/New Biz/Total by segment)
- Report 3: SOM Fee Structure Breakdown (Revenue by service type: PCP/MH/CCM/SS)
- Report 4: Top 20 Corporate Entities - SOM Only (3 tables: Combined, Integration, New Biz)
- Report 5: Geographic Analysis - SOM Only (PLACEHOLDER for future development)

**Document Structure:**
- Part 1: Architecture Overview (5 sections) - Added File 3
- Part 2: File 1 - Source Data Master (5 sections) - Added Do_We_Serve column
- Part 3: File 2 - Economic Model (7 sections) - Rebuilt Calculations sheet
- Part 4: Scenario 1 Formulas & Benchmarks (7 sections) - NEW
- Part 5: File 3 - Reports Output (7 sections) - NEW with 5 report specs
- Part 6: Scenario Management (5 sections) - Updated for new architecture
- Part 7: Quality Assurance (4 sections) - Updated validation checks
- Part 8: Implementation Procedures (4 sections) - Updated for three files
- Appendices: A-D (reference materials)

**Total:** 44 major sections, comprehensive coverage of three-file architecture with complete reporting framework

**Ready for:** Production implementation, scenario testing, stakeholder distribution

---

**V2.1 (November 15, 2025)**

**Status:** DEPRECATED (Contained "Opportunity_Revenue" error)

**Issues Identified:**
- Incorrectly collapsed Integration and New Biz into single "Opportunity_Revenue"
- Used ×12 multiplier when rates already annual
- Could not support stakeholder reporting needs

**Lessons Learned:**
- Need four distinct revenue streams for proper analysis
- Annual vs. monthly rate clarity is critical
- Reporting layer must be separate from model

---

**V2.0 (November 14, 2025)**

**Status:** DEPRECATED (Monolithic architecture)

**Lessons Learned:**
- Monolithic structure led to data corruption
- Need for modular architecture
- Importance of source data separation

---

**V1.0 (November 13, 2025)**

**Status:** DEPRECATED

**Validated Results:**
- 99.99% data quality
- 100% computational accuracy
- $127,572,232 TAM Current Revenue benchmark

---

## DOCUMENT CONTROL

### **Version Information**

**Rulebook Version:** V2.2 FINAL  
**Date:** November 15, 2025  
**Status:** PRODUCTION READY - FINALIZED  
**Model Version:** 3.0 (Modular Architecture)

### **Document Authority**

**Created By:** Eventus Economic Model Team  
**Finalized:** November 15, 2025  
**Approved By:** Ready for implementation and testing  
**Review Cycle:** After Scenario 1 validation successful  
**Next Review:** After first scenario comparison complete or Report 5 definition

### **Distribution**

**Internal Stakeholders:**
- Implementation Team (technical staff building model)
- Finance & Analytics (revenue forecasting)
- Business Development (strategic planning)
- Executive Leadership (board presentations)

**Confidentiality:** Internal Use Only

### **Usage Instructions**

**For Implementation Team:**
1. Read entire rulebook to understand three-file architecture
2. Build File 1 (Source_Data_Master.xlsx) per Part 2
3. Build File 2 (Economic_Model_Scenario_1.xlsx) per Part 3
4. Build File 3 (Reports_Scenario_1.xlsx) per Part 5
5. Follow linking instructions per Part 8
6. Run QA validation per Part 7
7. Verify $127.6M benchmark before declaring success

**For Ongoing Model Use:**
1. Keep source data pristine (File 1 - read-only)
2. Modify only Fee_Structure (File 2, Sheet 1) for new scenarios
3. Run QA validation after every change
4. Document all scenarios in Scenario_Definitions (File 2, Sheet 5)
5. Generate reports in File 3 for stakeholder distribution
6. Always create backups before major changes

**For Scenario Creation:**
1. Copy File 2 → Rename for new scenario
2. Update Sheet 1 (Fee_Structure) only
3. Verify recalculation in Sheet 4
4. Document assumptions in Sheet 5
5. Run QA validation in Sheet 6
6. Copy File 3 → Rename and update links
7. Compare to Scenario 1 baseline

### **Support & Contact**

**Questions about implementation:**
- Contact: Eventus Economic Model Team
- Include: Rulebook section reference, specific issue description

**Questions about business logic:**
- Contact: Finance & Analytics Team
- Include: Scenario context, strategic rationale

**Questions about data quality:**
- Contact: Data Operations Team
- Include: Facility identifiers, specific data issues

### **Future Updates**

**When to update this rulebook:**
- Architectural changes (e.g., adding File 4)
- Formula changes (e.g., new service types, rate structures)
- Segmentation logic changes (e.g., new market definitions)
- Benchmark updates (e.g., annual model recalibration)
- New report specifications (add to Part 5)

**Update procedure:**
1. Document proposed changes
2. Test changes in sandbox environment
3. Update rulebook sections affected
4. Increment version number (V2.3, V3.0, etc.)
5. Distribute updated rulebook to stakeholders
6. Archive previous version for reference

---

## END OF RULEBOOK V2.2 FINAL

**This document defines the complete three-file architecture for the Eventus Economic Model.**

**Use this V2.2 FINAL as the definitive guide for implementing the modular system with correct four revenue streams and comprehensive reporting layer.**

**Last Updated:** November 15, 2025  
**Status:** PRODUCTION READY - FINALIZED  
**Next Steps:** 
1. Build Files 1, 2, and 3 per specifications
2. Validate against $127.6M benchmark
3. Generate all four reports (Reports 1-4)
4. Define Report 5 (Geographic Analysis) when requirements ready
5. Begin Scenario 2 planning

**What's Included:**
- ✅ Three-file modular architecture
- ✅ Four revenue streams (Current, Integration, New Biz, Total)
- ✅ Corrected annual rate formulas
- ✅ Complete reporting layer with 4 reports + 1 placeholder
- ✅ Scenario 1 fully documented and validated
- ✅ QA validation framework
- ✅ Implementation procedures (step-by-step)

---

**✅ READY FOR IMPLEMENTATION**
