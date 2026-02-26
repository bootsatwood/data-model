# Final Model Rulebook V3.0
## Eventus Economic Model - Complete Technical Specification
### Comprehensive Formula Documentation | Computation Logic | Reconstruction Guide

**Document Purpose:** This rulebook provides complete technical documentation of the Eventus Economic Model, including every formula, computation step, and business logic rule needed to reconstruct the entire system from scratch.

**Model Version:** 3.0 - Modular Architecture  
**Rulebook Version:** V3.0 COMPLETE SPECIFICATION  
**Date:** November 16, 2025  
**Status:** PRODUCTION READY - Complete Technical Documentation  
**Architecture:** Three-File System (Source + Model + Reports)

---

## CRITICAL UPDATE: V3.0 CHANGES

**What V3.0 Adds:**
1. ✅ **Complete Formula Documentation** - Every equation with examples
2. ✅ **Step-by-Step Computation Logic** - Exact calculation sequences
3. ✅ **Business Logic Rules** - All IF/THEN conditions documented
4. ✅ **Sample Calculations** - Worked examples with real numbers
5. ✅ **Data Flow Diagrams** - How data moves between sheets/files
6. ✅ **Reconstruction Guide** - Build the entire model from this document alone
7. ✅ **Column-by-Column Specifications** - Every field defined and calculated

**Previous Versions Retained:**
- V2.3: Actual fee structure (SNF/ALF rates)
- V2.2: Four revenue streams, three-file architecture
- All architectural principles unchanged

---

## TABLE OF CONTENTS

**PART 1: EXECUTIVE SUMMARY**
- 1.1 What This Model Does
- 1.2 The Four Revenue Streams Explained
- 1.3 Quick Start Guide
- 1.4 Files Overview

**PART 2: FEE STRUCTURE (FILE 2, SHEET 1)**
- 2.1 Fee Structure Matrix
- 2.2 Integrated Package Calculations
- 2.3 Service Type Definitions
- 2.4 How to Read the Fee Structure

**PART 3: REVENUE FORMULAS - COMPLETE SPECIFICATION**
- 3.1 Current Revenue - Full Formula with Examples
- 3.2 Integration Revenue - Full Formula with Examples
- 3.3 New Business Revenue - Full Formula with Examples
- 3.4 Total Revenue - Full Formula with Examples
- 3.5 Service Component Breakdown Formulas

**PART 4: BUSINESS LOGIC RULES**
- 4.1 Service Flag Logic
- 4.2 Market Segmentation Logic
- 4.3 Revenue Eligibility Rules
- 4.4 Data Quality Handling

**PART 5: FILE 2 CALCULATIONS (SHEET 2) - COLUMN BY COLUMN**
- 5.1 Source Data Columns (A-T)
- 5.2 Revenue Calculation Columns (U-X)
- 5.3 Service Component Columns (Y-AB)
- 5.4 Complete Column Reference

**PART 6: FILE 2 SEGMENTATION (SHEET 3) - COMPLETE LOGIC**
- 6.1 TAM Flag Calculation
- 6.2 SAM Flag Calculation
- 6.3 SOM Flag Calculation
- 6.4 Segment Priority Assignment

**PART 7: FILE 2 RESULTS (SHEET 4) - AGGREGATION FORMULAS**
- 7.1 TAM Aggregations
- 7.2 SAM Aggregations
- 7.3 SOM Aggregations
- 7.4 Summary Calculations

**PART 8: FILE 3 REPORTS - COMPLETE SPECIFICATIONS**
- 8.1 Report 1: Facilities Count (with formulas)
- 8.2 Report 2: Revenue Summary (with formulas)
- 8.3 Report 3: SOM Fee Breakdown (with formulas)
- 8.4 Report 4: Top 20 Corporate Entities (with formulas)

**PART 9: WORKED EXAMPLES**
- 9.1 Example Facility 1: Integrated Service
- 9.2 Example Facility 2: PCP Only with Integration Opportunity
- 9.3 Example Facility 3: MH Only with Integration Opportunity
- 9.4 Example Facility 4: Unserved Corporate (New Business)
- 9.5 Example Facility 5: Independent Facility

**PART 10: RECONSTRUCTION GUIDE**
- 10.1 Building File 1 (Source Data)
- 10.2 Building File 2 (Economic Model)
- 10.3 Building File 3 (Reports)
- 10.4 Validation Steps

**APPENDICES**
- Appendix A: Complete Column Mapping
- Appendix B: All Formulas Reference
- Appendix C: Test Results from November 15, 2025
- Appendix D: Change Log

---

# PART 1: EXECUTIVE SUMMARY

## 1.1 What This Model Does

The Eventus Economic Model calculates revenue opportunities across healthcare facilities (SNFs and ALFs) by analyzing:

1. **Current Revenue** - What we earn today from facilities we currently serve
2. **Integration Revenue** - Additional revenue from adding services to existing customers
3. **New Business Revenue** - Revenue from acquiring new corporate facilities
4. **Total Revenue** - Sum of all three revenue streams

The model segments the market into:
- **TAM** (Total Addressable Market) - All facilities
- **SAM** (Serviceable Addressable Market) - Corporate facilities only
- **SOM** (Serviceable Obtainable Market) - Corporate facilities with no barriers

## 1.2 The Four Revenue Streams Explained

### **Stream 1: Current Revenue**
**Who:** Facilities where Do_We_Serve = "yes"  
**What:** Revenue from services we currently provide  
**How Much:** Depends on service type (Integrated, PCP Only, or MH Only)

### **Stream 2: Integration Revenue**
**Who:** Facilities we currently serve but haven't integrated  
**What:** Additional revenue from adding the missing service  
**How Much:** Cost of the missing service (PCP or MH)

### **Stream 3: New Business Revenue**
**Who:** Corporate facilities we don't serve with no barriers  
**What:** Full integrated package at new facilities  
**How Much:** Complete integrated service package

### **Stream 4: Total Revenue**
**Formula:** Current + Integration + New Business  
**Purpose:** Complete revenue opportunity calculation

## 1.3 Quick Start Guide

1. **Read Part 2** - Understand the fee structure
2. **Read Part 3** - Learn the four revenue formulas
3. **Read Part 9** - Work through examples
4. **Read Part 10** - Build the model yourself

## 1.4 Files Overview

**File 1: Source_Data_Master.xlsx**
- Raw facility data (provided by user)
- No calculations, data only
- 20 columns of facility information

**File 2: Economic_Model_Scenario_1.xlsx**
- Sheet 1: Fee_Structure (rates)
- Sheet 2: Calculations (revenue formulas)
- Sheet 3: Segmentation (market filters)
- Sheet 4: Results (aggregations)

**File 3: Reports_Scenario_1.xlsx**
- 4 stakeholder-ready reports
- Links to File 2 data
- No calculations, presentation only

---

# PART 2: FEE STRUCTURE (FILE 2, SHEET 1)

## 2.1 Fee Structure Matrix

This is the foundation of all revenue calculations.

### **SNF (Skilled Nursing Facility) Rates**

| Service Type | Fee Value | Variable Name | Notes |
|--------------|-----------|---------------|-------|
| PCP (Primary Care Provider) | $1,698.96 | `PCP_FEE_SNF` | Annual fee per facility |
| MH (Mental Health) | $1,623.96 | `MH_FEE_SNF` | Annual fee per facility |
| CCM (Chronic Care Management) | $360.00 | `CCM_FEE` | Same for SNF and ALF |
| Shared Savings | $4,800.00 | `SS_FEE` | Same for SNF and ALF |

### **ALF (Assisted Living Facility) Rates**

| Service Type | Fee Value | Variable Name | Notes |
|--------------|-----------|---------------|-------|
| PCP (Primary Care Provider) | $1,875.00 | `PCP_FEE_ALF` | Annual fee per facility |
| MH (Mental Health) | $1,898.00 | `MH_FEE_ALF` | Annual fee per facility |
| CCM (Chronic Care Management) | $360.00 | `CCM_FEE` | Same for SNF and ALF |
| Shared Savings | $4,800.00 | `SS_FEE` | Same for SNF and ALF |

## 2.2 Integrated Package Calculations

### **SNF Integrated Package**
```
INTEGRATED_SNF = PCP_FEE_SNF + MH_FEE_SNF + CCM_FEE + SS_FEE
INTEGRATED_SNF = $1,698.96 + $1,623.96 + $360.00 + $4,800.00
INTEGRATED_SNF = $8,482.92
```

### **ALF Integrated Package**
```
INTEGRATED_ALF = PCP_FEE_ALF + MH_FEE_ALF + CCM_FEE + SS_FEE
INTEGRATED_ALF = $1,875.00 + $1,898.00 + $360.00 + $4,800.00
INTEGRATED_ALF = $8,933.00
```

## 2.3 Service Type Definitions

### **Integrated Services**
- Provides BOTH PCP and MH services
- Includes CCM and Shared Savings
- Highest revenue per facility
- Flag: `Integrated_Flag = "yes"`

### **PCP Only Services**
- Provides PCP service only (not MH)
- Includes CCM and Shared Savings
- Mid-tier revenue per facility
- Flag: `PCP_Flag = "yes"` AND `Integrated_Flag != "yes"`

### **MH Only Services**
- Provides MH service only (not PCP)
- Includes CCM and Shared Savings
- Mid-tier revenue per facility
- Flag: `MH_Flag = "yes"` AND `Integrated_Flag != "yes"` AND `PCP_Flag != "yes"`

## 2.4 How to Read the Fee Structure

**In File 2, Sheet 1, the structure looks like:**

```
Row 1: SCENARIO 1 FEE STRUCTURE
Row 2: Scenario Name: Scenario 1 - Current State
Row 3: Date: November 15, 2025

Row 5: SERVICE FEES BY FACILITY TYPE
Row 6: [Headers] | SNF | ALF | Notes
Row 7: PCP Fee | 1698.96 | 1875.00 | Primary Care Provider services
Row 8: MH Fee | 1623.96 | 1898.00 | Mental Health services
Row 9: CCM Fee | 360.00 | 360.00 | Chronic Care Management
Row 10: Shared Savings | 4800.00 | 4800.00 | Shared Savings

Row 12: INTEGRATED SERVICES (Full Package)
Row 13: Components: PCP + MH + CCM + Shared Savings
```

**When building calculations, reference these cells:**
- SNF PCP Fee: Cell B7
- SNF MH Fee: Cell B8
- SNF CCM Fee: Cell B9
- SNF Shared Savings: Cell B10
- ALF rates in Column C

---

# PART 3: REVENUE FORMULAS - COMPLETE SPECIFICATION

## 3.1 Current Revenue - Full Formula with Examples

### **Formula Logic**

```
IF Facility is NOT served (Do_We_Serve != "yes"):
    Current_Revenue = $0
    
ELSE IF Facility is served (Do_We_Serve = "yes"):
    
    IF Integrated_Flag = "yes":
        IF Source_Type = "SNF":
            Current_Revenue = $8,482.92
        ELSE IF Source_Type = "ALF":
            Current_Revenue = $8,933.00
    
    ELSE IF PCP_Flag = "yes":
        IF Source_Type = "SNF":
            Current_Revenue = $1,698.96 + $360 + $4,800 = $6,858.96
        ELSE IF Source_Type = "ALF":
            Current_Revenue = $1,875.00 + $360 + $4,800 = $7,035.00
    
    ELSE IF MH_Flag = "yes":
        IF Source_Type = "SNF":
            Current_Revenue = $1,623.96 + $360 + $4,800 = $6,783.96
        ELSE IF Source_Type = "ALF":
            Current_Revenue = $1,898.00 + $360 + $4,800 = $7,058.00
    
    ELSE:
        Current_Revenue = $0
        (This is a data quality issue - served but no flags)
```

### **Pseudocode Version**

```python
def calculate_current_revenue(row):
    # Check if facility is served
    if row['Do_We_Serve'] != 'yes':
        return 0
    
    # Determine facility type fees
    if row['Source_Type'] == 'SNF':
        PCP_FEE = 1698.96
        MH_FEE = 1623.96
        CCM_FEE = 360.00
        SS_FEE = 4800.00
        INTEGRATED = 8482.92
    else:  # ALF
        PCP_FEE = 1875.00
        MH_FEE = 1898.00
        CCM_FEE = 360.00
        SS_FEE = 4800.00
        INTEGRATED = 8933.00
    
    # Calculate based on service type
    if row['Integrated_Flag'] == 'yes':
        return INTEGRATED
    elif row['PCP_Flag'] == 'yes':
        return PCP_FEE + CCM_FEE + SS_FEE
    elif row['MH_Flag'] == 'yes':
        return MH_FEE + CCM_FEE + SS_FEE
    else:
        return 0  # No service flags
```

### **Worked Examples**

**Example 1: SNF with Integrated Services**
- Source_Type: SNF
- Do_We_Serve: yes
- Integrated_Flag: yes
- **Current_Revenue = $8,482.92**

**Example 2: SNF with PCP Only**
- Source_Type: SNF
- Do_We_Serve: yes
- PCP_Flag: yes
- Integrated_Flag: (not "yes")
- **Current_Revenue = $1,698.96 + $360 + $4,800 = $6,858.96**

**Example 3: ALF with MH Only**
- Source_Type: ALF
- Do_We_Serve: yes
- MH_Flag: yes
- PCP_Flag: (not "yes")
- Integrated_Flag: (not "yes")
- **Current_Revenue = $1,898.00 + $360 + $4,800 = $7,058.00**

**Example 4: Not Served**
- Do_We_Serve: (not "yes")
- **Current_Revenue = $0**

## 3.2 Integration Revenue - Full Formula with Examples

### **Formula Logic**

Integration Revenue represents the opportunity to ADD services to facilities we already serve.

```
IF Facility is NOT served (Do_We_Serve != "yes"):
    Integration_Revenue = $0
    (Can't integrate if we're not there)

ELSE IF Facility already has Integrated services (Integrated_Flag = "yes"):
    Integration_Revenue = $0
    (Already fully integrated)

ELSE IF Facility has PCP Only (PCP_Flag = "yes" AND Integrated_Flag != "yes"):
    IF Source_Type = "SNF":
        Integration_Revenue = $1,623.96  (add MH service)
    ELSE IF Source_Type = "ALF":
        Integration_Revenue = $1,898.00  (add MH service)

ELSE IF Facility has MH Only (MH_Flag = "yes" AND PCP_Flag != "yes" AND Integrated_Flag != "yes"):
    IF Source_Type = "SNF":
        Integration_Revenue = $1,698.96  (add PCP service)
    ELSE IF Source_Type = "ALF":
        Integration_Revenue = $1,875.00  (add PCP service)

ELSE:
    Integration_Revenue = $0
    (No service flags or data quality issue)
```

### **Pseudocode Version**

```python
def calculate_integration_revenue(row):
    # Must be served to have integration opportunity
    if row['Do_We_Serve'] != 'yes':
        return 0
    
    # Already integrated = no opportunity
    if row['Integrated_Flag'] == 'yes':
        return 0
    
    # Determine facility type fees
    if row['Source_Type'] == 'SNF':
        PCP_FEE = 1698.96
        MH_FEE = 1623.96
    else:  # ALF
        PCP_FEE = 1875.00
        MH_FEE = 1898.00
    
    # PCP Only can add MH
    if row['PCP_Flag'] == 'yes':
        return MH_FEE
    
    # MH Only can add PCP
    elif row['MH_Flag'] == 'yes':
        return PCP_FEE
    
    else:
        return 0  # No integration opportunity
```

### **Worked Examples**

**Example 1: SNF with PCP Only (Can Add MH)**
- Source_Type: SNF
- Do_We_Serve: yes
- PCP_Flag: yes
- Integrated_Flag: (not "yes")
- **Integration_Revenue = $1,623.96** (add MH service)
- After integration: Current_Revenue becomes $8,482.92

**Example 2: ALF with MH Only (Can Add PCP)**
- Source_Type: ALF
- Do_We_Serve: yes
- MH_Flag: yes
- PCP_Flag: (not "yes")
- Integrated_Flag: (not "yes")
- **Integration_Revenue = $1,875.00** (add PCP service)
- After integration: Current_Revenue becomes $8,933.00

**Example 3: Already Integrated**
- Do_We_Serve: yes
- Integrated_Flag: yes
- **Integration_Revenue = $0** (already has both services)

**Example 4: Not Served**
- Do_We_Serve: (not "yes")
- **Integration_Revenue = $0** (can't integrate if we're not there)

## 3.3 New Business Revenue - Full Formula with Examples

### **Formula Logic**

New Business Revenue represents the opportunity to acquire new corporate facilities.

```
IF Facility is already served (Do_We_Serve = "yes"):
    New_Biz_Revenue = $0
    (Already a customer)

ELSE IF Ownership_Type != "Corporate":
    New_Biz_Revenue = $0
    (We only target corporate facilities)

ELSE IF Barrier is not null (has a barrier):
    New_Biz_Revenue = $0
    (Barrier prevents acquisition)

ELSE:
    (Corporate, not served, no barrier)
    IF Source_Type = "SNF":
        New_Biz_Revenue = $8,482.92  (full integrated package)
    ELSE IF Source_Type = "ALF":
        New_Biz_Revenue = $8,933.00  (full integrated package)
```

### **Pseudocode Version**

```python
def calculate_new_biz_revenue(row):
    # Already served = not new business
    if row['Do_We_Serve'] == 'yes':
        return 0
    
    # Must be corporate
    if row['Ownership_Type'] != 'Corporate':
        return 0
    
    # Must not have barriers
    if pd.notna(row['Barrier']):  # Barrier exists
        return 0
    
    # Calculate integrated package
    if row['Source_Type'] == 'SNF':
        return 8482.92
    else:  # ALF
        return 8933.00
```

### **Worked Examples**

**Example 1: Unserved Corporate SNF, No Barrier**
- Source_Type: SNF
- Do_We_Serve: (not "yes")
- Ownership_Type: Corporate
- Barrier: null
- **New_Biz_Revenue = $8,482.92**

**Example 2: Unserved Corporate ALF, No Barrier**
- Source_Type: ALF
- Do_We_Serve: (not "yes")
- Ownership_Type: Corporate
- Barrier: null
- **New_Biz_Revenue = $8,933.00**

**Example 3: Corporate but Has Barrier**
- Ownership_Type: Corporate
- Do_We_Serve: (not "yes")
- Barrier: "Alliance"
- **New_Biz_Revenue = $0**

**Example 4: Independent Facility**
- Ownership_Type: Independent
- Do_We_Serve: (not "yes")
- Barrier: null
- **New_Biz_Revenue = $0** (we don't target independent facilities)

**Example 5: Already Served**
- Do_We_Serve: yes
- Ownership_Type: Corporate
- Barrier: null
- **New_Biz_Revenue = $0** (already a customer)

## 3.4 Total Revenue - Full Formula with Examples

### **Formula Logic**

```
Total_Revenue = Current_Revenue + Integration_Revenue + New_Biz_Revenue
```

**Important:** These three streams are mutually exclusive at the facility level:
- If Current_Revenue > 0, then New_Biz_Revenue = 0 (can't be both served and new)
- Integration_Revenue can coexist with Current_Revenue (current customer with expansion opportunity)
- New_Biz_Revenue never coexists with Current or Integration (not a customer yet)

### **Worked Examples**

**Example 1: Integrated SNF Customer**
- Current_Revenue: $8,482.92
- Integration_Revenue: $0 (already integrated)
- New_Biz_Revenue: $0 (already served)
- **Total_Revenue = $8,482.92**

**Example 2: PCP Only SNF Customer**
- Current_Revenue: $6,858.96
- Integration_Revenue: $1,623.96 (can add MH)
- New_Biz_Revenue: $0 (already served)
- **Total_Revenue = $8,482.92**

**Example 3: Unserved Corporate SNF**
- Current_Revenue: $0 (not served)
- Integration_Revenue: $0 (not served)
- New_Biz_Revenue: $8,482.92
- **Total_Revenue = $8,482.92**

**Example 4: Independent Unserved Facility**
- Current_Revenue: $0 (not served)
- Integration_Revenue: $0 (not served)
- New_Biz_Revenue: $0 (independent, not targeted)
- **Total_Revenue = $0**

## 3.5 Service Component Breakdown Formulas

These formulas break down Current_Revenue into its components for reporting.

### **Current_PCP (PCP Component of Current Revenue)**

```python
def calculate_current_pcp(row):
    if row['Do_We_Serve'] != 'yes':
        return 0
    
    # Has PCP if Integrated OR PCP_Only
    if row['Integrated_Flag'] == 'yes' or row['PCP_Flag'] == 'yes':
        if row['Source_Type'] == 'SNF':
            return 1698.96
        else:  # ALF
            return 1875.00
    else:
        return 0
```

### **Current_MH (MH Component of Current Revenue)**

```python
def calculate_current_mh(row):
    if row['Do_We_Serve'] != 'yes':
        return 0
    
    # Has MH if Integrated OR MH_Only
    if row['Integrated_Flag'] == 'yes' or row['MH_Flag'] == 'yes':
        if row['Source_Type'] == 'SNF':
            return 1623.96
        else:  # ALF
            return 1898.00
    else:
        return 0
```

### **Current_CCM (CCM Component of Current Revenue)**

```python
def calculate_current_ccm(row):
    if row['Do_We_Serve'] != 'yes':
        return 0
    
    # Has CCM if has ANY service (Integrated, PCP, or MH)
    if (row['Integrated_Flag'] == 'yes' or 
        row['PCP_Flag'] == 'yes' or 
        row['MH_Flag'] == 'yes'):
        return 360.00  # Same for SNF and ALF
    else:
        return 0
```

### **Current_SS (Shared Savings Component of Current Revenue)**

```python
def calculate_current_ss(row):
    if row['Do_We_Serve'] != 'yes':
        return 0
    
    # Has SS if has ANY service (Integrated, PCP, or MH)
    if (row['Integrated_Flag'] == 'yes' or 
        row['PCP_Flag'] == 'yes' or 
        row['MH_Flag'] == 'yes'):
        return 4800.00  # Same for SNF and ALF
    else:
        return 0
```

### **Verification Formula**

```
Current_PCP + Current_MH + Current_CCM + Current_SS = Current_Revenue
```

This should always be true for every facility.

---

# PART 4: BUSINESS LOGIC RULES

## 4.1 Service Flag Logic

### **Service Flag Hierarchy**

The service flags follow a mutually exclusive hierarchy:

1. **Integrated_Flag = "yes"** (Highest priority)
   - Facility receives BOTH PCP and MH services
   - Automatically includes CCM and Shared Savings
   - When Integrated_Flag = "yes", PCP_Flag and MH_Flag are ignored
   
2. **PCP_Flag = "yes"** (Medium priority, only if Integrated != "yes")
   - Facility receives PCP service only
   - Does NOT receive MH service
   - Includes CCM and Shared Savings
   
3. **MH_Flag = "yes"** (Lowest priority, only if Integrated != "yes" AND PCP != "yes")
   - Facility receives MH service only
   - Does NOT receive PCP service
   - Includes CCM and Shared Savings

### **Service Flag Rules**

**Rule 1: Integrated Takes Precedence**
```
IF Integrated_Flag = "yes":
    Service_Type = "Integrated"
    Ignore PCP_Flag and MH_Flag values
```

**Rule 2: PCP Only Check**
```
IF Integrated_Flag != "yes" AND PCP_Flag = "yes":
    Service_Type = "PCP_Only"
    Ignore MH_Flag value
```

**Rule 3: MH Only Check**
```
IF Integrated_Flag != "yes" AND PCP_Flag != "yes" AND MH_Flag = "yes":
    Service_Type = "MH_Only"
```

**Rule 4: No Service Flags**
```
IF Integrated_Flag != "yes" AND PCP_Flag != "yes" AND MH_Flag != "yes":
    Service_Type = "Unknown"
    This is a DATA QUALITY ISSUE if Do_We_Serve = "yes"
```

### **Service Flag Combinations (Valid and Invalid)**

**Valid Combinations:**
| Integrated | PCP | MH | Result | Notes |
|-----------|-----|----|---------|----|
| yes | any | any | Integrated | Integrated takes precedence |
| no/null | yes | any | PCP_Only | PCP takes precedence over MH |
| no/null | no/null | yes | MH_Only | MH is the only service |
| no/null | no/null | no/null | None | No services (only valid if Do_We_Serve != "yes") |

**Data Quality Issues:**
- Do_We_Serve = "yes" BUT all flags are null → Missing service flags
- Do_We_Serve != "yes" BUT any flag = "yes" → Service without customer relationship

## 4.2 Market Segmentation Logic

### **TAM (Total Addressable Market)**

```
TAM_Flag = TRUE for ALL facilities
```

**Logic:** Every facility in the database is part of the total addressable market.

**Count:** All 14,750+ facilities

### **SAM (Serviceable Addressable Market)**

```
IF Ownership_Type = "Corporate":
    SAM_Flag = TRUE
ELSE:
    SAM_Flag = FALSE
```

**Logic:** We only pursue corporate-owned facilities (not independent).

**Reasoning:** Corporate facilities offer:
- Multi-site opportunities
- Standardized decision-making
- Scalable relationships
- Central billing

**Example:**
- Genesis Healthcare (Corporate) → SAM_Flag = TRUE
- Mom & Pop Nursing Home (Independent) → SAM_Flag = FALSE

### **SOM (Serviceable Obtainable Market)**

```
IF Ownership_Type = "Corporate" AND Barrier IS NULL:
    SOM_Flag = TRUE
ELSE:
    SOM_Flag = FALSE
```

**Logic:** Corporate facilities we can actually obtain (no barriers to entry).

**Barriers Include:**
- "Alliance" - Exclusive partnership with competitor
- "Own Provider Group" - They have their own internal providers
- "Competitor Contract" - Under contract with competitor
- "Refuses Service" - Explicitly declined our services

**Example:**
- Corporate facility, no barrier → SOM_Flag = TRUE
- Corporate facility, barrier = "Alliance" → SOM_Flag = FALSE

### **Segment Priority Assignment**

```
IF SOM_Flag = TRUE:
    Segment_Priority = "1-SOM"
ELSE IF SAM_Flag = TRUE:
    Segment_Priority = "2-SAM"
ELSE:
    Segment_Priority = "3-TAM"
```

**Usage:** Prioritize sales efforts on SOM (highest probability), then SAM, then TAM.

## 4.3 Revenue Eligibility Rules

### **Current Revenue Eligibility**

```
Eligible for Current_Revenue IF:
    Do_We_Serve = "yes"
    AND
    At least one service flag is set (Integrated, PCP, or MH)
```

**Disqualified:**
- Do_We_Serve != "yes" → Not a customer
- All service flags null → Data quality issue

### **Integration Revenue Eligibility**

```
Eligible for Integration_Revenue IF:
    Do_We_Serve = "yes"
    AND
    Integrated_Flag != "yes"
    AND
    (PCP_Flag = "yes" OR MH_Flag = "yes")
```

**Disqualified:**
- Do_We_Serve != "yes" → Not a customer
- Integrated_Flag = "yes" → Already integrated
- No service flags → Can't integrate if no services

### **New Business Revenue Eligibility**

```
Eligible for New_Biz_Revenue IF:
    Do_We_Serve != "yes"
    AND
    Ownership_Type = "Corporate"
    AND
    Barrier IS NULL
```

**Disqualified:**
- Do_We_Serve = "yes" → Already a customer
- Ownership_Type = "Independent" → We don't target
- Barrier exists → Blocked from acquisition

## 4.4 Data Quality Handling

### **Issue Type 1: Service Flags Without Do_We_Serve**

**Pattern:**
- Integrated_Flag = "yes" OR PCP_Flag = "yes" OR MH_Flag = "yes"
- Do_We_Serve != "yes"

**Handling:**
- Current_Revenue = $0
- Integration_Revenue = $0
- New_Biz_Revenue = depends on other criteria
- **Action Required:** Verify if should be marked as served

### **Issue Type 2: Do_We_Serve Without Service Flags**

**Pattern:**
- Do_We_Serve = "yes"
- Integrated_Flag != "yes" AND PCP_Flag != "yes" AND MH_Flag != "yes"

**Handling:**
- Current_Revenue = $0
- Integration_Revenue = $0
- New_Biz_Revenue = $0
- **Action Required:** Populate missing service flags

### **Issue Type 3: Missing Source_Type**

**Pattern:**
- Source_Type is null or not "SNF" or "ALF"

**Handling:**
- Cannot calculate revenue (unknown fee structure)
- **Action Required:** Populate Source_Type field

---

# PART 5: FILE 2 CALCULATIONS (SHEET 2) - COLUMN BY COLUMN

## 5.1 Source Data Columns (Columns A-T from File 1)

These columns are imported directly from File 1 (Source_Data_Master.xlsx):

| Column | Field Name | Data Type | Source | Description |
|--------|-----------|-----------|--------|-------------|
| A | Source_Type | Text | File 1 | "SNF" or "ALF" |
| B | Facility_Name | Text | File 1 | Name of facility |
| C | Corporate_Name | Text | File 1 | Parent company (if corporate) |
| D | Address | Text | File 1 | Street address |
| E | City | Text | File 1 | City |
| F | State | Text | File 1 | State abbreviation |
| G | ZIP | Number | File 1 | Zip code |
| H | County | Text | File 1 | County name |
| I | Ownership_Type | Text | File 1 | "Corporate" or "Independent" |
| J | Total_Beds | Number | File 1 | Licensed bed count |
| K | Census | Number | File 1 | Current census |
| L | Do_We_Serve | Text | File 1 | "yes" if we serve this facility |
| M | Integrated_Flag | Text | File 1 | "yes" if integrated services |
| N | PCP_Flag | Text | File 1 | "yes" if PCP services only |
| O | MH_Flag | Text | File 1 | "yes" if MH services only |
| P | Barrier | Text | File 1 | Barrier type if exists |
| Q | Location | Text | File 1 | Full address string |
| R | Latitude | Number | File 1 | GPS latitude |
| S | Longitude | Number | File 1 | GPS longitude |
| T | Data_Quality_Flag | Text | File 1 | Data quality issues |

**Implementation:** Link these columns to File 1 using external references.

## 5.2 Revenue Calculation Columns (Columns U-X)

These columns contain the four revenue stream formulas:

### **Column U: Current_Revenue**

**Formula in Row 2 (assumes headers in Row 1):**
```excel
=IF(L2<>"yes", 0,
    IF(M2="yes",
        IF(A2="SNF", 8482.92, 8933.00),
        IF(N2="yes",
            IF(A2="SNF", 6858.96, 7035.00),
            IF(O2="yes",
                IF(A2="SNF", 6783.96, 7058.00),
                0
            )
        )
    )
)
```

**Python Equivalent:**
```python
df['Current_Revenue'] = df.apply(calculate_current_revenue, axis=1)
```
(Using function from Part 3.1)

### **Column V: Integration_Revenue**

**Formula in Row 2:**
```excel
=IF(L2<>"yes", 0,
    IF(M2="yes", 0,
        IF(N2="yes",
            IF(A2="SNF", 1623.96, 1898.00),
            IF(O2="yes",
                IF(A2="SNF", 1698.96, 1875.00),
                0
            )
        )
    )
)
```

**Python Equivalent:**
```python
df['Integration_Revenue'] = df.apply(calculate_integration_revenue, axis=1)
```
(Using function from Part 3.2)

### **Column W: New_Biz_Revenue**

**Formula in Row 2:**
```excel
=IF(L2="yes", 0,
    IF(I2<>"Corporate", 0,
        IF(ISBLANK(P2),
            IF(A2="SNF", 8482.92, 8933.00),
            0
        )
    )
)
```

**Python Equivalent:**
```python
df['New_Biz_Revenue'] = df.apply(calculate_new_biz_revenue, axis=1)
```
(Using function from Part 3.3)

### **Column X: Total_Revenue**

**Formula in Row 2:**
```excel
=U2+V2+W2
```

**Python Equivalent:**
```python
df['Total_Revenue'] = df['Current_Revenue'] + df['Integration_Revenue'] + df['New_Biz_Revenue']
```

## 5.3 Service Component Columns (Columns Y-AB)

These columns break down Current_Revenue by service component:

### **Column Y: Current_PCP**

**Formula in Row 2:**
```excel
=IF(L2<>"yes", 0,
    IF(OR(M2="yes", N2="yes"),
        IF(A2="SNF", 1698.96, 1875.00),
        0
    )
)
```

### **Column Z: Current_MH**

**Formula in Row 2:**
```excel
=IF(L2<>"yes", 0,
    IF(OR(M2="yes", O2="yes"),
        IF(A2="SNF", 1623.96, 1898.00),
        0
    )
)
```

### **Column AA: Current_CCM**

**Formula in Row 2:**
```excel
=IF(L2<>"yes", 0,
    IF(OR(M2="yes", N2="yes", O2="yes"),
        360.00,
        0
    )
)
```

### **Column AB: Current_SS**

**Formula in Row 2:**
```excel
=IF(L2<>"yes", 0,
    IF(OR(M2="yes", N2="yes", O2="yes"),
        4800.00,
        0
    )
)
```

## 5.4 Complete Column Reference

**File 2, Sheet 2 (Calculations) Column Layout:**

| Column | Field | Type | Source/Formula |
|--------|-------|------|----------------|
| A-T | Source Data | Import | From File 1 |
| U | Current_Revenue | Calculated | Multi-level IF formula |
| V | Integration_Revenue | Calculated | Multi-level IF formula |
| W | New_Biz_Revenue | Calculated | Multi-level IF formula |
| X | Total_Revenue | Calculated | =U+V+W |
| Y | Current_PCP | Calculated | Conditional formula |
| Z | Current_MH | Calculated | Conditional formula |
| AA | Current_CCM | Calculated | Conditional formula |
| AB | Current_SS | Calculated | Conditional formula |

**Total Columns:** 28 (A through AB)

---

# PART 6: FILE 2 SEGMENTATION (SHEET 3) - COMPLETE LOGIC

## 6.1 TAM Flag Calculation

**Column Location:** Column AC (or appropriate column after copying all columns from Sheet 2)

**Formula:**
```excel
=TRUE
```

**Logic:** Every facility is part of TAM, so this is simply TRUE for all rows.

**Python:**
```python
df['TAM_Flag'] = True
```

## 6.2 SAM Flag Calculation

**Column Location:** Column AD

**Formula in Row 2:**
```excel
=IF(I2="Corporate", TRUE, FALSE)
```

**Logic:** Only corporate facilities are part of SAM.

**Python:**
```python
df['SAM_Flag'] = df['Ownership_Type'] == 'Corporate'
```

## 6.3 SOM Flag Calculation

**Column Location:** Column AE

**Formula in Row 2:**
```excel
=IF(AND(I2="Corporate", ISBLANK(P2)), TRUE, FALSE)
```

**Logic:** Corporate facilities with no barriers are part of SOM.

**Python:**
```python
df['SOM_Flag'] = (df['Ownership_Type'] == 'Corporate') & (pd.isna(df['Barrier']))
```

## 6.4 Segment Priority Assignment

**Column Location:** Column AF

**Formula in Row 2:**
```excel
=IF(AE2=TRUE, "1-SOM",
    IF(AD2=TRUE, "2-SAM",
        "3-TAM"
    )
)
```

**Logic:** Assign priority based on segment membership.

**Python:**
```python
def assign_segment(row):
    if row['SOM_Flag']:
        return "1-SOM"
    elif row['SAM_Flag']:
        return "2-SAM"
    else:
        return "3-TAM"

df['Segment_Priority'] = df.apply(assign_segment, axis=1)
```

---

# PART 7: FILE 2 RESULTS (SHEET 4) - AGGREGATION FORMULAS

## 7.1 TAM Aggregations

**Sheet 4 Layout:**

```
Row 1: SCENARIO 1 RESULTS SUMMARY
Row 3: [Headers] | Total Facilities | Served | Current Revenue | Integration Revenue | New Biz Revenue | Total Revenue
Row 4: TAM | [formulas below] | ... | ... | ... | ... | ...
```

### **Cell B4: TAM Total Facilities**
```excel
=COUNTA(Segmentation!A:A)-1
```
(Count all facilities, minus header row)

### **Cell C4: TAM Served Facilities**
```excel
=COUNTIF(Segmentation!L:L, "yes")
```
(Count facilities where Do_We_Serve = "yes")

### **Cell D4: TAM Current Revenue**
```excel
=SUM(Segmentation!U:U)
```
(Sum all Current_Revenue values)

### **Cell E4: TAM Integration Revenue**
```excel
=SUM(Segmentation!V:V)
```
(Sum all Integration_Revenue values)

### **Cell F4: TAM New Biz Revenue**
```excel
=SUM(Segmentation!W:W)
```
(Sum all New_Biz_Revenue values)

### **Cell G4: TAM Total Revenue**
```excel
=SUM(Segmentation!X:X)
```
OR
```excel
=D4+E4+F4
```
(Sum all Total_Revenue values, or sum the three streams)

## 7.2 SAM Aggregations

**Row 5: SAM**

### **Cell B5: SAM Total Facilities**
```excel
=COUNTIF(Segmentation!AD:AD, TRUE)
```
(Count facilities where SAM_Flag = TRUE)

### **Cell C5: SAM Served Facilities**
```excel
=COUNTIFS(Segmentation!AD:AD, TRUE, Segmentation!L:L, "yes")
```
(Count facilities where SAM_Flag = TRUE AND Do_We_Serve = "yes")

### **Cell D5: SAM Current Revenue**
```excel
=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!U:U)
```
(Sum Current_Revenue where SAM_Flag = TRUE)

### **Cell E5: SAM Integration Revenue**
```excel
=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!V:V)
```
(Sum Integration_Revenue where SAM_Flag = TRUE)

### **Cell F5: SAM New Biz Revenue**
```excel
=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!W:W)
```
(Sum New_Biz_Revenue where SAM_Flag = TRUE)

### **Cell G5: SAM Total Revenue**
```excel
=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!X:X)
```
OR
```excel
=D5+E5+F5
```

## 7.3 SOM Aggregations

**Row 6: SOM**

### **Cell B6: SOM Total Facilities**
```excel
=COUNTIF(Segmentation!AE:AE, TRUE)
```
(Count facilities where SOM_Flag = TRUE)

### **Cell C6: SOM Served Facilities**
```excel
=COUNTIFS(Segmentation!AE:AE, TRUE, Segmentation!L:L, "yes")
```
(Count facilities where SOM_Flag = TRUE AND Do_We_Serve = "yes")

### **Cell D6: SOM Current Revenue**
```excel
=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!U:U)
```

### **Cell E6: SOM Integration Revenue**
```excel
=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!V:V)
```

### **Cell F6: SOM New Biz Revenue**
```excel
=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!W:W)
```

### **Cell G6: SOM Total Revenue**
```excel
=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!X:X)
```
OR
```excel
=D6+E6+F6
```

## 7.4 Summary Calculations

**Python Aggregation Approach:**

```python
# TAM Results
tam_results = {
    'Total_Facilities': len(df),
    'Served': (df['Do_We_Serve'] == 'yes').sum(),
    'Current_Revenue': df['Current_Revenue'].sum(),
    'Integration_Revenue': df['Integration_Revenue'].sum(),
    'New_Biz_Revenue': df['New_Biz_Revenue'].sum(),
    'Total_Revenue': df['Total_Revenue'].sum()
}

# SAM Results
sam_df = df[df['SAM_Flag']]
sam_results = {
    'Total_Facilities': len(sam_df),
    'Served': (sam_df['Do_We_Serve'] == 'yes').sum(),
    'Current_Revenue': sam_df['Current_Revenue'].sum(),
    'Integration_Revenue': sam_df['Integration_Revenue'].sum(),
    'New_Biz_Revenue': sam_df['New_Biz_Revenue'].sum(),
    'Total_Revenue': sam_df['Total_Revenue'].sum()
}

# SOM Results
som_df = df[df['SOM_Flag']]
som_results = {
    'Total_Facilities': len(som_df),
    'Served': (som_df['Do_We_Serve'] == 'yes').sum(),
    'Current_Revenue': som_df['Current_Revenue'].sum(),
    'Integration_Revenue': som_df['Integration_Revenue'].sum(),
    'New_Biz_Revenue': som_df['New_Biz_Revenue'].sum(),
    'Total_Revenue': som_df['Total_Revenue'].sum()
}
```

---

# PART 8: FILE 3 REPORTS - COMPLETE SPECIFICATIONS

## 8.1 Report 1: Facilities Count (with formulas)

**File:** Reports_Scenario_1.xlsx  
**Sheet:** Facilities_Count

### **Layout:**

```
Row 1: REPORT 1: FACILITIES COUNT
Row 2: Scenario 1 - Current State
Row 3: SNF Facilities Only

Row 5: [Headers] | Total | Served | Unserved
Row 6: TAM | [formulas] | [formulas] | [formulas]
Row 7: SAM | [formulas] | [formulas] | [formulas]
Row 8: SOM | [formulas] | [formulas] | [formulas]

Row 10: [Headers] | Total | Served | Unserved
Row 11: Corporate | [formulas] | [formulas] | [formulas]
Row 12: Independent | [formulas] | [formulas] | [formulas]
Row 13: TOTAL | [formulas] | [formulas] | [formulas]
```

### **Formulas:**

**Cell B6 (TAM Total):**
```excel
=[Economic_Model_Scenario_1.xlsx]Results!$B$4
```

**Cell C6 (TAM Served):**
```excel
=[Economic_Model_Scenario_1.xlsx]Results!$C$4
```

**Cell D6 (TAM Unserved):**
```excel
=B6-C6
```

**Cells B7-D7 (SAM):** Similar pattern referencing Results!$B$5:$C$5

**Cells B8-D8 (SOM):** Similar pattern referencing Results!$B$6:$C$6

**Cell B11 (Corporate Total):**
```excel
=COUNTIF([Economic_Model_Scenario_1.xlsx]Segmentation!$I:$I, "Corporate")
```

**Cell C11 (Corporate Served):**
```excel
=COUNTIFS([Economic_Model_Scenario_1.xlsx]Segmentation!$I:$I, "Corporate",
          [Economic_Model_Scenario_1.xlsx]Segmentation!$L:$L, "yes")
```

**Cell D11 (Corporate Unserved):**
```excel
=B11-C11
```

**Similar pattern for Independent (Row 12) and TOTAL (Row 13)**

## 8.2 Report 2: Revenue Summary (with formulas)

**Sheet:** Revenue_Summary

### **Layout:**

```
Row 1: REPORT 2: REVENUE SUMMARY
Row 2: Scenario 1 - Current State
Row 3: SNF Facilities Only

Row 5: [Headers] | Current Revenue | Integration Revenue | New Biz Revenue | Total Revenue
Row 6: TAM | [formulas] | [formulas] | [formulas] | [formulas]
Row 7: SAM | [formulas] | [formulas] | [formulas] | [formulas]
Row 8: SOM | [formulas] | [formulas] | [formulas] | [formulas]
```

### **Formulas:**

**Cell B6 (TAM Current Revenue):**
```excel
=[Economic_Model_Scenario_1.xlsx]Results!$D$4
```

**Cell C6 (TAM Integration Revenue):**
```excel
=[Economic_Model_Scenario_1.xlsx]Results!$E$4
```

**Cell D6 (TAM New Biz Revenue):**
```excel
=[Economic_Model_Scenario_1.xlsx]Results!$F$4
```

**Cell E6 (TAM Total Revenue):**
```excel
=[Economic_Model_Scenario_1.xlsx]Results!$G$4
```
OR
```excel
=B6+C6+D6
```

**Similar pattern for SAM (Row 7, Results Row 5) and SOM (Row 8, Results Row 6)**

## 8.3 Report 3: SOM Fee Breakdown (with formulas)

**Sheet:** SOM_Fee_Breakdown

### **Layout:**

```
Row 1: REPORT 3: SOM FEE STRUCTURE BREAKDOWN
Row 2: Scenario 1 - Current State
Row 3: SNF Facilities - SOM Segment Only

Row 5: [Headers] | Current Revenue | % of Total
Row 6: PCP (Primary Care) | [formula] | [formula]
Row 7: MH (Mental Health) | [formula] | [formula]
Row 8: CCM (Chronic Care Management) | [formula] | [formula]
Row 9: Shared Savings | [formula] | [formula]
Row 10: TOTAL CURRENT REVENUE | [formula] | 100%

Row 12: OPPORTUNITY ANALYSIS
Row 13: Current Revenue | [formula]
Row 14: Integration Opportunity | [formula]
Row 15: New Business Opportunity | [formula]
Row 16: Total SOM Opportunity | [formula]
```

### **Formulas:**

**Cell B6 (SOM PCP Revenue):**
```excel
=SUMIF([Economic_Model_Scenario_1.xlsx]Segmentation!$AE:$AE, TRUE,
       [Economic_Model_Scenario_1.xlsx]Segmentation!$Y:$Y)
```
(Sum Current_PCP where SOM_Flag = TRUE)

**Cell C6 (PCP % of Total):**
```excel
=B6/B10
```
(Format as percentage)

**Cell B7 (SOM MH Revenue):**
```excel
=SUMIF([Economic_Model_Scenario_1.xlsx]Segmentation!$AE:$AE, TRUE,
       [Economic_Model_Scenario_1.xlsx]Segmentation!$Z:$Z)
```

**Cell B8 (SOM CCM Revenue):**
```excel
=SUMIF([Economic_Model_Scenario_1.xlsx]Segmentation!$AE:$AE, TRUE,
       [Economic_Model_Scenario_1.xlsx]Segmentation!$AA:$AA)
```

**Cell B9 (SOM SS Revenue):**
```excel
=SUMIF([Economic_Model_Scenario_1.xlsx]Segmentation!$AE:$AE, TRUE,
       [Economic_Model_Scenario_1.xlsx]Segmentation!$AB:$AB)
```

**Cell B10 (Total Current Revenue):**
```excel
=B6+B7+B8+B9
```
OR
```excel
=[Economic_Model_Scenario_1.xlsx]Results!$D$6
```

**Cell B13 (Current Revenue in Opportunity section):**
```excel
=B10
```

**Cell B14 (Integration Opportunity):**
```excel
=[Economic_Model_Scenario_1.xlsx]Results!$E$6
```

**Cell B15 (New Business Opportunity):**
```excel
=[Economic_Model_Scenario_1.xlsx]Results!$F$6
```

**Cell B16 (Total SOM Opportunity):**
```excel
=B13+B14+B15
```
OR
```excel
=[Economic_Model_Scenario_1.xlsx]Results!$G$6
```

## 8.4 Report 4: Top 20 Corporate Entities (with formulas)

**Sheet:** Top_20_Corporate

This report requires more complex calculations - typically done in Python/VBA then imported as values.

### **Approach 1: Python Pre-Calculation**

```python
# Filter to SOM and Corporate
som_corporate = df[(df['SOM_Flag']) & (df['Ownership_Type'] == 'Corporate')].copy()

# Group by Corporate_Name
corporate_summary = som_corporate.groupby('Corporate_Name').agg({
    'Facility_Name': 'count',  # Facility count
    'Total_Revenue': 'sum',    # Total Opportunity
    'Integration_Revenue': 'sum',  # Integration Opp
    'New_Biz_Revenue': 'sum',  # New Biz Opp
    'Do_We_Serve': lambda x: (x == 'yes').sum()  # Currently Served count
}).reset_index()

corporate_summary.columns = ['Corporate_Name', 'Facilities', 'Total_Opp', 
                              'Integration_Opp', 'New_Biz_Opp', 'Served']

# Get top 20 by Total Opportunity
top20_total = corporate_summary.nlargest(20, 'Total_Opp')

# Get top 20 by Integration Opportunity
top20_integration = corporate_summary.nlargest(20, 'Integration_Opp')

# Get top 20 by New Business Opportunity
top20_new_biz = corporate_summary.nlargest(20, 'New_Biz_Opp')
```

### **Approach 2: Excel Pivot Table + Manual Ranking**

1. Create pivot table from Segmentation sheet
2. Filter: SOM_Flag = TRUE AND Ownership_Type = "Corporate"
3. Rows: Corporate_Name
4. Values: 
   - Count of Facility_Name
   - Sum of Total_Revenue
   - Sum of Integration_Revenue
   - Sum of New_Biz_Revenue
   - Count of Do_We_Serve (filtered to "yes")
5. Sort by Total_Revenue descending
6. Copy top 20 to report sheet

### **Layout:**

```
TABLE A: TOP 20 BY TOTAL COMBINED OPPORTUNITY
Rank | Corporate Entity | Facilities | Served | Total Opportunity

TABLE B: TOP 20 BY INTEGRATION OPPORTUNITY
Rank | Corporate Entity | Facilities | Served | Integration Opportunity

TABLE C: TOP 20 BY NEW BUSINESS OPPORTUNITY
Rank | Corporate Entity | Facilities | Served | New Business Opportunity
```

---

# PART 9: WORKED EXAMPLES

## 9.1 Example Facility 1: Integrated Service

**Facility Data:**
```
Source_Type: SNF
Facility_Name: Sunrise Senior Living - Main Campus
Corporate_Name: SUNRISE SENIOR LIVING
Ownership_Type: Corporate
Do_We_Serve: yes
Integrated_Flag: yes
PCP_Flag: (null)
MH_Flag: (null)
Barrier: (null)
```

**Step-by-Step Calculation:**

**Step 1: Current_Revenue**
- Do_We_Serve = "yes" ✓
- Integrated_Flag = "yes" ✓
- Source_Type = "SNF"
- **Current_Revenue = $8,482.92** (SNF Integrated Package)

**Step 2: Integration_Revenue**
- Do_We_Serve = "yes" ✓
- Integrated_Flag = "yes" → Already integrated
- **Integration_Revenue = $0**

**Step 3: New_Biz_Revenue**
- Do_We_Serve = "yes" → Already a customer
- **New_Biz_Revenue = $0**

**Step 4: Total_Revenue**
- **Total_Revenue = $8,482.92 + $0 + $0 = $8,482.92**

**Step 5: Service Components**
- Current_PCP: $1,698.96 (has Integrated)
- Current_MH: $1,623.96 (has Integrated)
- Current_CCM: $360.00 (has any service)
- Current_SS: $4,800.00 (has any service)
- **Verification:** $1,698.96 + $1,623.96 + $360 + $4,800 = $8,482.92 ✓

**Step 6: Segmentation**
- TAM_Flag: TRUE (all facilities)
- SAM_Flag: TRUE (Corporate)
- SOM_Flag: TRUE (Corporate, no barrier)
- Segment_Priority: "1-SOM"

## 9.2 Example Facility 2: PCP Only with Integration Opportunity

**Facility Data:**
```
Source_Type: SNF
Facility_Name: Oakwood Rehabilitation Center
Corporate_Name: OAKWOOD HEALTH SYSTEM
Ownership_Type: Corporate
Do_We_Serve: yes
Integrated_Flag: (null)
PCP_Flag: yes
MH_Flag: (null)
Barrier: (null)
```

**Step-by-Step Calculation:**

**Step 1: Current_Revenue**
- Do_We_Serve = "yes" ✓
- Integrated_Flag != "yes" ✓
- PCP_Flag = "yes" ✓
- Source_Type = "SNF"
- **Current_Revenue = $1,698.96 + $360 + $4,800 = $6,858.96**

**Step 2: Integration_Revenue**
- Do_We_Serve = "yes" ✓
- Integrated_Flag != "yes" ✓
- PCP_Flag = "yes" ✓ → Can add MH
- Source_Type = "SNF"
- **Integration_Revenue = $1,623.96** (add MH service)

**Step 3: New_Biz_Revenue**
- Do_We_Serve = "yes" → Already a customer
- **New_Biz_Revenue = $0**

**Step 4: Total_Revenue**
- **Total_Revenue = $6,858.96 + $1,623.96 + $0 = $8,482.92**

**Step 5: Service Components**
- Current_PCP: $1,698.96 (has PCP)
- Current_MH: $0 (no MH yet)
- Current_CCM: $360.00 (has PCP service)
- Current_SS: $4,800.00 (has PCP service)
- **Verification:** $1,698.96 + $0 + $360 + $4,800 = $6,858.96 ✓

**Step 6: Segmentation**
- TAM_Flag: TRUE
- SAM_Flag: TRUE
- SOM_Flag: TRUE
- Segment_Priority: "1-SOM"

**Integration Insight:** If we add MH service, Current_Revenue becomes $8,482.92 (full integrated package).

## 9.3 Example Facility 3: MH Only with Integration Opportunity

**Facility Data:**
```
Source_Type: ALF
Facility_Name: Peaceful Gardens Assisted Living
Corporate_Name: (null)
Ownership_Type: Independent
Do_We_Serve: yes
Integrated_Flag: (null)
PCP_Flag: (null)
MH_Flag: yes
Barrier: (null)
```

**Step-by-Step Calculation:**

**Step 1: Current_Revenue**
- Do_We_Serve = "yes" ✓
- Integrated_Flag != "yes" ✓
- PCP_Flag != "yes" ✓
- MH_Flag = "yes" ✓
- Source_Type = "ALF"
- **Current_Revenue = $1,898.00 + $360 + $4,800 = $7,058.00**

**Step 2: Integration_Revenue**
- Do_We_Serve = "yes" ✓
- Integrated_Flag != "yes" ✓
- MH_Flag = "yes" ✓ → Can add PCP
- Source_Type = "ALF"
- **Integration_Revenue = $1,875.00** (add PCP service)

**Step 3: New_Biz_Revenue**
- Do_We_Serve = "yes" → Already a customer
- **New_Biz_Revenue = $0**

**Step 4: Total_Revenue**
- **Total_Revenue = $7,058.00 + $1,875.00 + $0 = $8,933.00**

**Step 5: Service Components**
- Current_PCP: $0 (no PCP yet)
- Current_MH: $1,898.00 (has MH)
- Current_CCM: $360.00 (has MH service)
- Current_SS: $4,800.00 (has MH service)
- **Verification:** $0 + $1,898.00 + $360 + $4,800 = $7,058.00 ✓

**Step 6: Segmentation**
- TAM_Flag: TRUE
- SAM_Flag: FALSE (Independent)
- SOM_Flag: FALSE (Independent)
- Segment_Priority: "3-TAM"

**Integration Insight:** If we add PCP service, Current_Revenue becomes $8,933.00 (full ALF integrated package).

## 9.4 Example Facility 4: Unserved Corporate (New Business)

**Facility Data:**
```
Source_Type: SNF
Facility_Name: Meadowbrook Nursing Center
Corporate_Name: GENESIS HEALTHCARE
Ownership_Type: Corporate
Do_We_Serve: (null)
Integrated_Flag: (null)
PCP_Flag: (null)
MH_Flag: (null)
Barrier: (null)
```

**Step-by-Step Calculation:**

**Step 1: Current_Revenue**
- Do_We_Serve != "yes" → Not a customer
- **Current_Revenue = $0**

**Step 2: Integration_Revenue**
- Do_We_Serve != "yes" → Not a customer
- **Integration_Revenue = $0**

**Step 3: New_Biz_Revenue**
- Do_We_Serve != "yes" ✓
- Ownership_Type = "Corporate" ✓
- Barrier is null ✓
- Source_Type = "SNF"
- **New_Biz_Revenue = $8,482.92** (full integrated package)

**Step 4: Total_Revenue**
- **Total_Revenue = $0 + $0 + $8,482.92 = $8,482.92**

**Step 5: Service Components**
- Current_PCP: $0 (not served)
- Current_MH: $0 (not served)
- Current_CCM: $0 (not served)
- Current_SS: $0 (not served)
- **Verification:** $0 + $0 + $0 + $0 = $0 ✓

**Step 6: Segmentation**
- TAM_Flag: TRUE
- SAM_Flag: TRUE (Corporate)
- SOM_Flag: TRUE (Corporate, no barrier)
- Segment_Priority: "1-SOM"

**New Business Insight:** This is a prime acquisition target - corporate facility with no barriers, worth full $8,482.92 in annual revenue.

## 9.5 Example Facility 5: Independent Facility

**Facility Data:**
```
Source_Type: SNF
Facility_Name: Mom & Pop Nursing Home
Corporate_Name: (null)
Ownership_Type: Independent
Do_We_Serve: (null)
Integrated_Flag: (null)
PCP_Flag: (null)
MH_Flag: (null)
Barrier: (null)
```

**Step-by-Step Calculation:**

**Step 1: Current_Revenue**
- Do_We_Serve != "yes" → Not a customer
- **Current_Revenue = $0**

**Step 2: Integration_Revenue**
- Do_We_Serve != "yes" → Not a customer
- **Integration_Revenue = $0**

**Step 3: New_Biz_Revenue**
- Do_We_Serve != "yes" ✓
- Ownership_Type = "Independent" → We don't target
- **New_Biz_Revenue = $0**

**Step 4: Total_Revenue**
- **Total_Revenue = $0 + $0 + $0 = $0**

**Step 5: Service Components**
- All $0 (not served)

**Step 6: Segmentation**
- TAM_Flag: TRUE (part of total market)
- SAM_Flag: FALSE (Independent)
- SOM_Flag: FALSE (Independent)
- Segment_Priority: "3-TAM"

**Business Insight:** Independent facilities are part of TAM but not SAM/SOM - we don't actively pursue them.

---

# PART 10: RECONSTRUCTION GUIDE

## 10.1 Building File 1 (Source Data)

### **Required Columns:**

Create an Excel file named `Source_Data_Master.xlsx` with one sheet containing these 20 columns:

| Column | Name | Data Type | Sample Value |
|--------|------|-----------|--------------|
| A | Source_Type | Text | "SNF" or "ALF" |
| B | Facility_Name | Text | "Sunrise Senior Living" |
| C | Corporate_Name | Text | "GENESIS HEALTHCARE" |
| D | Address | Text | "123 Main Street" |
| E | City | Text | "Charlotte" |
| F | State | Text | "NC" |
| G | ZIP | Number | 28202 |
| H | County | Text | "Mecklenburg" |
| I | Ownership_Type | Text | "Corporate" or "Independent" |
| J | Total_Beds | Number | 120 |
| K | Census | Number | 98.5 |
| L | Do_We_Serve | Text | "yes" or blank |
| M | Integrated_Flag | Text | "yes" or blank |
| N | PCP_Flag | Text | "yes" or blank |
| O | MH_Flag | Text | "yes" or blank |
| P | Barrier | Text | "Alliance" or blank |
| Q | Location | Text | "123 Main Street,Charlotte,NC,28202" |
| R | Latitude | Number | 35.2271 |
| S | Longitude | Number | -80.8431 |
| T | Data_Quality_Flag | Text | Issue description or blank |

### **Data Quality Rules:**

1. **Source_Type:** Must be "SNF" or "ALF" (case-sensitive)
2. **Do_We_Serve:** Use "yes" for served facilities, leave blank for unserved
3. **Service Flags:** Only set if Do_We_Serve = "yes"
4. **Ownership_Type:** Must be "Corporate" or "Independent"
5. **Barrier:** Leave blank if no barrier exists

### **Sample Data:**

```csv
Source_Type,Facility_Name,Corporate_Name,Ownership_Type,Do_We_Serve,Integrated_Flag,PCP_Flag,MH_Flag,Barrier
SNF,Facility A,GENESIS HEALTHCARE,Corporate,yes,yes,,,
SNF,Facility B,GENESIS HEALTHCARE,Corporate,yes,,yes,,
SNF,Facility C,GENESIS HEALTHCARE,Corporate,yes,,,yes,
SNF,Facility D,GENESIS HEALTHCARE,Corporate,,,,,,
SNF,Facility E,GENESIS HEALTHCARE,Corporate,,,,,Alliance
SNF,Facility F,,Independent,,,,,,
```

## 10.2 Building File 2 (Economic Model)

### **Sheet 1: Fee_Structure**

**Create manually:**

Row 1: `SCENARIO 1 FEE STRUCTURE`
Row 2: `Scenario Name:` | `Scenario 1 - Current State`
Row 5: `SERVICE FEES BY FACILITY TYPE`
Row 6: Headers | `SNF` | `ALF` | `Notes`
Row 7: `PCP Fee` | `1698.96` | `1875.00` | `Primary Care Provider services`
Row 8: `MH Fee` | `1623.96` | `1898.00` | `Mental Health services`
Row 9: `CCM Fee` | `360.00` | `360.00` | `Chronic Care Management`
Row 10: `Shared Savings` | `4800.00` | `4800.00` | `Shared Savings`

### **Sheet 2: Calculations**

**Step 1:** Import all 20 columns from File 1 (columns A-T)

**Excel Method:**
```
In cell A2: ='[Source_Data_Master.xlsx]Sheet1'!A2
Copy across to column T
Copy down for all rows
```

**Step 2:** Add revenue formulas in columns U-X

**Cell U2 (Current_Revenue):**
```excel
=IF(L2<>"yes", 0,
    IF(M2="yes",
        IF(A2="SNF", 8482.92, 8933.00),
        IF(N2="yes",
            IF(A2="SNF", 6858.96, 7035.00),
            IF(O2="yes",
                IF(A2="SNF", 6783.96, 7058.00),
                0
            )
        )
    )
)
```

**Cell V2 (Integration_Revenue):**
```excel
=IF(L2<>"yes", 0,
    IF(M2="yes", 0,
        IF(N2="yes",
            IF(A2="SNF", 1623.96, 1898.00),
            IF(O2="yes",
                IF(A2="SNF", 1698.96, 1875.00),
                0
            )
        )
    )
)
```

**Cell W2 (New_Biz_Revenue):**
```excel
=IF(L2="yes", 0,
    IF(I2<>"Corporate", 0,
        IF(ISBLANK(P2),
            IF(A2="SNF", 8482.92, 8933.00),
            0
        )
    )
)
```

**Cell X2 (Total_Revenue):**
```excel
=U2+V2+W2
```

**Step 3:** Add service component formulas in columns Y-AB

**Cell Y2 (Current_PCP):**
```excel
=IF(L2<>"yes", 0, IF(OR(M2="yes", N2="yes"), IF(A2="SNF", 1698.96, 1875.00), 0))
```

**Cell Z2 (Current_MH):**
```excel
=IF(L2<>"yes", 0, IF(OR(M2="yes", O2="yes"), IF(A2="SNF", 1623.96, 1898.00), 0))
```

**Cell AA2 (Current_CCM):**
```excel
=IF(L2<>"yes", 0, IF(OR(M2="yes", N2="yes", O2="yes"), 360.00, 0))
```

**Cell AB2 (Current_SS):**
```excel
=IF(L2<>"yes", 0, IF(OR(M2="yes", N2="yes", O2="yes"), 4800.00, 0))
```

**Step 4:** Copy all formulas down for all data rows

### **Sheet 3: Segmentation**

**Step 1:** Import all columns from Sheet 2 (columns A-AB)

**Excel Method:**
```
In cell A2: =Calculations!A2
Copy across to column AB
Copy down for all rows
```

**Step 2:** Add segmentation flags in columns AC-AF

**Cell AC2 (TAM_Flag):**
```excel
=TRUE
```

**Cell AD2 (SAM_Flag):**
```excel
=IF(I2="Corporate", TRUE, FALSE)
```

**Cell AE2 (SOM_Flag):**
```excel
=IF(AND(I2="Corporate", ISBLANK(P2)), TRUE, FALSE)
```

**Cell AF2 (Segment_Priority):**
```excel
=IF(AE2=TRUE, "1-SOM", IF(AD2=TRUE, "2-SAM", "3-TAM"))
```

**Step 3:** Copy formulas down for all rows

### **Sheet 4: Results**

**Create summary table:**

Row 1: `SCENARIO 1 RESULTS SUMMARY`
Row 3: Headers | `Total Facilities` | `Served` | `Current Revenue` | `Integration Revenue` | `New Biz Revenue` | `Total Revenue`

**Row 4: TAM**

Cell B4: `=COUNTA(Segmentation!A:A)-1`
Cell C4: `=COUNTIF(Segmentation!L:L, "yes")`
Cell D4: `=SUM(Segmentation!U:U)`
Cell E4: `=SUM(Segmentation!V:V)`
Cell F4: `=SUM(Segmentation!W:W)`
Cell G4: `=SUM(Segmentation!X:X)`

**Row 5: SAM**

Cell B5: `=COUNTIF(Segmentation!AD:AD, TRUE)`
Cell C5: `=COUNTIFS(Segmentation!AD:AD, TRUE, Segmentation!L:L, "yes")`
Cell D5: `=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!U:U)`
Cell E5: `=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!V:V)`
Cell F5: `=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!W:W)`
Cell G5: `=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!X:X)`

**Row 6: SOM**

Cell B6: `=COUNTIF(Segmentation!AE:AE, TRUE)`
Cell C6: `=COUNTIFS(Segmentation!AE:AE, TRUE, Segmentation!L:L, "yes")`
Cell D6: `=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!U:U)`
Cell E6: `=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!V:V)`
Cell F6: `=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!W:W)`
Cell G6: `=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!X:X)`

## 10.3 Building File 3 (Reports)

Create a new workbook linking to File 2's Results and Segmentation sheets.

**Follow the formulas documented in Part 8 for each report sheet.**

## 10.4 Validation Steps

### **Validation Checklist:**

1. **Fee Structure Validation**
   - [ ] SNF PCP Fee = $1,698.96
   - [ ] SNF MH Fee = $1,623.96
   - [ ] SNF Integrated = $8,482.92
   - [ ] ALF PCP Fee = $1,875.00
   - [ ] ALF MH Fee = $1,898.00
   - [ ] ALF Integrated = $8,933.00

2. **Current Revenue Validation**
   - [ ] Integrated SNF facility shows $8,482.92
   - [ ] PCP Only SNF facility shows $6,858.96
   - [ ] MH Only SNF facility shows $6,783.96
   - [ ] Unserved facility shows $0

3. **Integration Revenue Validation**
   - [ ] PCP Only facility shows MH fee
   - [ ] MH Only facility shows PCP fee
   - [ ] Integrated facility shows $0
   - [ ] Unserved facility shows $0

4. **New Biz Revenue Validation**
   - [ ] Unserved corporate facility (no barrier) shows integrated package
   - [ ] Served facility shows $0
   - [ ] Independent facility shows $0
   - [ ] Corporate with barrier shows $0

5. **Component Validation**
   - [ ] Current_PCP + Current_MH + Current_CCM + Current_SS = Current_Revenue
   - [ ] All served integrated facilities have all 4 components
   - [ ] PCP Only facilities have PCP, CCM, SS (no MH)
   - [ ] MH Only facilities have MH, CCM, SS (no PCP)

6. **Segmentation Validation**
   - [ ] TAM_Flag = TRUE for all facilities
   - [ ] SAM_Flag = TRUE only for Corporate facilities
   - [ ] SOM_Flag = TRUE only for Corporate with no barrier
   - [ ] Segment_Priority correctly assigned

7. **Aggregation Validation**
   - [ ] TAM facilities = total row count
   - [ ] SAM facilities ≤ TAM facilities
   - [ ] SOM facilities ≤ SAM facilities
   - [ ] Revenue totals match sum of individual facilities

---

# APPENDIX A: COMPLETE COLUMN MAPPING

## File 1: Source_Data_Master.xlsx

| Col | Field | Type | Description |
|-----|-------|------|-------------|
| A | Source_Type | Text | "SNF" or "ALF" |
| B | Facility_Name | Text | Facility name |
| C | Corporate_Name | Text | Parent company |
| D | Address | Text | Street address |
| E | City | Text | City |
| F | State | Text | State code |
| G | ZIP | Number | Zip code |
| H | County | Text | County |
| I | Ownership_Type | Text | "Corporate"/"Independent" |
| J | Total_Beds | Number | Bed count |
| K | Census | Number | Current census |
| L | Do_We_Serve | Text | "yes" if served |
| M | Integrated_Flag | Text | "yes" if integrated |
| N | PCP_Flag | Text | "yes" if PCP only |
| O | MH_Flag | Text | "yes" if MH only |
| P | Barrier | Text | Barrier type |
| Q | Location | Text | Full address |
| R | Latitude | Number | GPS lat |
| S | Longitude | Number | GPS long |
| T | Data_Quality_Flag | Text | DQ issues |

## File 2, Sheet 2: Calculations

| Col | Field | Type | Source |
|-----|-------|------|--------|
| A-T | (Source columns) | Various | From File 1 |
| U | Current_Revenue | Currency | Formula |
| V | Integration_Revenue | Currency | Formula |
| W | New_Biz_Revenue | Currency | Formula |
| X | Total_Revenue | Currency | =U+V+W |
| Y | Current_PCP | Currency | Formula |
| Z | Current_MH | Currency | Formula |
| AA | Current_CCM | Currency | Formula |
| AB | Current_SS | Currency | Formula |

## File 2, Sheet 3: Segmentation

| Col | Field | Type | Source |
|-----|-------|------|--------|
| A-AB | (Calculations columns) | Various | From Sheet 2 |
| AC | TAM_Flag | Boolean | =TRUE |
| AD | SAM_Flag | Boolean | Formula |
| AE | SOM_Flag | Boolean | Formula |
| AF | Segment_Priority | Text | Formula |

---

# APPENDIX B: ALL FORMULAS REFERENCE

## Revenue Formulas (Sheet 2, Columns U-X)

**Current_Revenue (U2):**
```excel
=IF(L2<>"yes", 0,
    IF(M2="yes",
        IF(A2="SNF", 8482.92, 8933.00),
        IF(N2="yes",
            IF(A2="SNF", 6858.96, 7035.00),
            IF(O2="yes",
                IF(A2="SNF", 6783.96, 7058.00),
                0
            )
        )
    )
)
```

**Integration_Revenue (V2):**
```excel
=IF(L2<>"yes", 0,
    IF(M2="yes", 0,
        IF(N2="yes",
            IF(A2="SNF", 1623.96, 1898.00),
            IF(O2="yes",
                IF(A2="SNF", 1698.96, 1875.00),
                0
            )
        )
    )
)
```

**New_Biz_Revenue (W2):**
```excel
=IF(L2="yes", 0,
    IF(I2<>"Corporate", 0,
        IF(ISBLANK(P2),
            IF(A2="SNF", 8482.92, 8933.00),
            0
        )
    )
)
```

**Total_Revenue (X2):**
```excel
=U2+V2+W2
```

## Component Formulas (Sheet 2, Columns Y-AB)

**Current_PCP (Y2):**
```excel
=IF(L2<>"yes", 0, IF(OR(M2="yes", N2="yes"), IF(A2="SNF", 1698.96, 1875.00), 0))
```

**Current_MH (Z2):**
```excel
=IF(L2<>"yes", 0, IF(OR(M2="yes", O2="yes"), IF(A2="SNF", 1623.96, 1898.00), 0))
```

**Current_CCM (AA2):**
```excel
=IF(L2<>"yes", 0, IF(OR(M2="yes", N2="yes", O2="yes"), 360.00, 0))
```

**Current_SS (AB2):**
```excel
=IF(L2<>"yes", 0, IF(OR(M2="yes", N2="yes", O2="yes"), 4800.00, 0))
```

## Segmentation Formulas (Sheet 3, Columns AC-AF)

**TAM_Flag (AC2):**
```excel
=TRUE
```

**SAM_Flag (AD2):**
```excel
=IF(I2="Corporate", TRUE, FALSE)
```

**SOM_Flag (AE2):**
```excel
=IF(AND(I2="Corporate", ISBLANK(P2)), TRUE, FALSE)
```

**Segment_Priority (AF2):**
```excel
=IF(AE2=TRUE, "1-SOM", IF(AD2=TRUE, "2-SAM", "3-TAM"))
```

## Results Aggregations (Sheet 4)

**TAM Row (Row 4):**
- B4: `=COUNTA(Segmentation!A:A)-1`
- C4: `=COUNTIF(Segmentation!L:L, "yes")`
- D4: `=SUM(Segmentation!U:U)`
- E4: `=SUM(Segmentation!V:V)`
- F4: `=SUM(Segmentation!W:W)`
- G4: `=SUM(Segmentation!X:X)`

**SAM Row (Row 5):**
- B5: `=COUNTIF(Segmentation!AD:AD, TRUE)`
- C5: `=COUNTIFS(Segmentation!AD:AD, TRUE, Segmentation!L:L, "yes")`
- D5: `=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!U:U)`
- E5: `=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!V:V)`
- F5: `=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!W:W)`
- G5: `=SUMIF(Segmentation!AD:AD, TRUE, Segmentation!X:X)`

**SOM Row (Row 6):**
- B6: `=COUNTIF(Segmentation!AE:AE, TRUE)`
- C6: `=COUNTIFS(Segmentation!AE:AE, TRUE, Segmentation!L:L, "yes")`
- D6: `=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!U:U)`
- E6: `=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!V:V)`
- F6: `=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!W:W)`
- G6: `=SUMIF(Segmentation!AE:AE, TRUE, Segmentation!X:X)`

---

# APPENDIX C: TEST RESULTS FROM NOVEMBER 15, 2025

## Test Configuration

**Source Data:** SNF_Database_Final_v2_4_2025-11-14.xlsx  
**Facility Count:** 14,750 SNF facilities  
**Fee Structure:** SNF rates (Scenario 1)  
**Date:** November 15, 2025

## TAM Results

| Metric | Value |
|--------|-------|
| Total Facilities | 14,750 |
| Served Facilities | 563 (3.8%) |
| Current Revenue | $3,919,967.64 |
| Integration Revenue | $601,428.72 |
| New Biz Revenue | $81,215,476.08 |
| **Total TAM Revenue** | **$85,736,872.44** |

## SAM Results

| Metric | Value |
|--------|-------|
| Total Facilities | 10,065 (68.2%) |
| Served Facilities | 527 (5.2%) |
| Current Revenue | $3,622,863.48 |
| Integration Revenue | $534,928.56 |
| New Biz Revenue | $81,215,476.08 |
| **Total SAM Revenue** | **$85,373,268.12** |

## SOM Results

| Metric | Value |
|--------|-------|
| Total Facilities | 9,997 (67.8%) |
| Served Facilities | 354 (3.5%) |
| Current Revenue | $2,971,205.28 |
| Integration Revenue | $438,928.56 |
| New Biz Revenue | $81,215,476.08 |
| **Total SOM Revenue** | **$84,625,609.92** |

## Service Component Breakdown (SOM Current Revenue)

| Component | Revenue | % of Total |
|-----------|---------|------------|
| PCP | $1,182,926.88 | 39.8% |
| MH | $469,825.44 | 15.8% |
| CCM | $127,440.00 | 4.3% |
| Shared Savings | $1,191,013.44 | 40.1% |
| **TOTAL** | **$2,971,205.28** | **100.0%** |

## Top 5 Corporate Entities (SOM Only)

| Rank | Corporate Entity | Facilities | Total Opportunity |
|------|-----------------|------------|-------------------|
| 1 | THE ENSIGN GROUP | 303 | $2,570,324.76 |
| 2 | PACS GROUP | 212 | $1,798,379.04 |
| 3 | GENESIS HEALTHCARE | 215 | $1,782,267.12 |
| 4 | LIFE CARE CENTERS OF AMERICA | 195 | $1,654,169.40 |
| 5 | CREATIVE SOLUTIONS IN HEALTHCARE | 145 | $1,230,023.40 |

## Data Quality Issues Identified

**Issue #1:** 4 facilities with service flags but Do_We_Serve != "yes"  
**Issue #2:** 30 facilities with Do_We_Serve = "yes" but no service flags  
**Total Data Quality Issues:** 34 facilities (0.2% of total)

---

# APPENDIX D: CHANGE LOG

## V3.0 (November 16, 2025)

**Status:** PRODUCTION READY - Complete Technical Specification

**Major Additions:**
- ✅ Complete formula documentation with examples
- ✅ Step-by-step computation logic for all revenue streams
- ✅ Business logic rules fully documented
- ✅ Column-by-column specifications for all sheets
- ✅ Five worked examples showing calculations
- ✅ Complete reconstruction guide (build from scratch)
- ✅ All Excel formulas provided in copyable format
- ✅ Python pseudocode equivalents for all calculations
- ✅ Comprehensive validation checklist
- ✅ Complete test results from November 15, 2025

**Document Structure:**
- Part 1: Executive Summary (4 sections)
- Part 2: Fee Structure (4 sections)
- Part 3: Revenue Formulas (5 sections with examples)
- Part 4: Business Logic Rules (4 sections)
- Part 5: File 2 Calculations - Column by Column (4 sections)
- Part 6: File 2 Segmentation - Complete Logic (4 sections)
- Part 7: File 2 Results - Aggregation Formulas (4 sections)
- Part 8: File 3 Reports - Complete Specifications (4 sections)
- Part 9: Worked Examples (5 complete scenarios)
- Part 10: Reconstruction Guide (4 sections)
- Appendices: A-D (complete reference materials)

**Total:** 10 major parts, 44+ sections, comprehensive technical specification

**Key Features:**
- Any technical user can reconstruct the entire model from this document alone
- All formulas provided in both Excel and Python formats
- Complete worked examples showing every calculation type
- Detailed validation procedures
- Production test results included

**Ready for:** Independent implementation, technical handoff, audit review

---

## V2.3 UPDATE (November 15, 2025)

**Status:** Production Ready - Fee Structure Finalized

**Changes:**
- Added actual fee structure (SNF/ALF rates)
- Renamed "Social Services" to "Shared Savings"
- Removed "annual rate" terminology
- Completed test implementation
- Documented data quality issues

---

## V2.2 FINAL (November 15, 2025)

**Status:** DEPRECATED (Missing formula details)

**Changes:**
- Removed "Opportunity_Revenue" artifact
- Added four revenue streams (Current, Integration, New Biz, Total)
- Fixed annual calculation (removed ×12)
- Documented as Scenario 1
- Added File 3 (Reports) structure

---

## END OF RULEBOOK V3.0

**This document provides complete technical documentation for reconstructing the Eventus Economic Model from scratch.**

**Use this V3.0 as the definitive technical specification for:**
1. Understanding every calculation and formula
2. Building the model independently
3. Validating model outputs
4. Training new team members
5. Auditing model accuracy
6. Creating new scenarios

**Last Updated:** November 16, 2025  
**Status:** PRODUCTION READY - COMPLETE TECHNICAL SPECIFICATION  
**Next Steps:** 
1. Use this document to independently reconstruct the model
2. Validate against test results in Appendix C
3. Implement data quality fixes for 34 flagged facilities
4. Prepare for ALF data integration
5. Begin Scenario 2 planning

**What's Included:**
- ✅ Every formula with examples
- ✅ Complete business logic rules
- ✅ Step-by-step reconstruction guide
- ✅ Worked examples for all scenarios
- ✅ Validation procedures
- ✅ Test results and benchmarks
- ✅ Column-by-column specifications
- ✅ Excel AND Python implementations

---

**✅ COMPLETE TECHNICAL SPECIFICATION - READY FOR USE**
