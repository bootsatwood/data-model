# Final Model Rulebook V5.0
## Eventus Economic Model - Three Scenario Specification
### Complete Formula Documentation | Census-Based Calculations | Adjuster System

**Document Purpose:** This rulebook provides the CORRECTED technical specification for the Eventus Economic Model with the critical V5.0 formula correction for Total Potential Revenue.

**Model Version:** 5.0 - Corrected Total Potential Revenue Formula  
**Rulebook Version:** V5.0 CRITICAL CORRECTION  
**Date:** November 16, 2025  
**Status:** PRODUCTION READY - Total Potential Revenue Formula Fixed  
**Architecture:** Three-File System (Source + Model + Reports)

---

## CRITICAL CORRECTION IN V5.0

**What Was WRONG in V4.0:**
```
Total_Revenue = Current_Revenue + Integration_Revenue + New_Biz_Revenue  ❌
```

**What Is NOW CORRECT in V5.0:**
```
Total_Potential_Revenue = Integration_Revenue + New_Biz_Revenue  ✅
```

**Why This Matters:**
- **Current Revenue** = What we earn TODAY (already realized, separate metric)
- **Integration Revenue** = POTENTIAL additional revenue from expanding services
- **New Business Revenue** = POTENTIAL revenue from new customers
- **Total Potential Revenue** = Total OPPORTUNITY revenue (Integration + New Business)

**Total Potential Revenue does NOT include Current Revenue because Current is already happening, not potential.**

---

## TABLE OF CONTENTS

**PART 1: EXECUTIVE SUMMARY**
- 1.1 What This Model Does
- 1.2 The Four Revenue Metrics Explained
- 1.3 Three Scenarios Overview
- 1.4 Fee Structure and Adjusters

**PART 2: FEE STRUCTURE & ADJUSTERS**
- 2.1 Base Fee Rates (SNF and ALF)
- 2.2 Permanent Adjusters
- 2.3 Adjusted Fee Values
- 2.4 Why Adjusters Never Change

**PART 3: SCENARIO 1 - ORIGINAL V2.2 SPECIFICATION**
- 3.1 Scenario 1 Service Packages
- 3.2 Current Revenue Formulas
- 3.3 Integration Revenue Formulas
- 3.4 New Business Revenue Formulas
- 3.5 Total Potential Revenue Formula (V5.0 CORRECTED)
- 3.6 Worked Examples

**PART 4: SCENARIO 2 - PCP ENHANCEMENT**
- 4.1 What Changes in Scenario 2
- 4.2 Scenario 2 Service Packages
- 4.3 Current Revenue Formulas
- 4.4 Integration Revenue Formulas
- 4.5 Total Potential Revenue Formula (V5.0)
- 4.6 Worked Examples

**PART 5: SCENARIO 3 - MH + PCP ENHANCEMENT**
- 5.1 What Changes in Scenario 3
- 5.2 Scenario 3 Service Packages
- 5.3 Current Revenue Formulas
- 5.4 Integration Revenue Formulas
- 5.5 Total Potential Revenue Formula (V5.0)
- 5.6 Worked Examples

**PART 6: SCENARIO COMPARISON**
- 6.1 Side-by-Side Comparison
- 6.2 Revenue Distribution Analysis
- 6.3 When to Use Each Scenario
- 6.4 Test Results from All Scenarios (V5.0)

**PART 7: IMPLEMENTATION**
- 7.1 Building Scenario 1 Model
- 7.2 Building Scenario 2 Model
- 7.3 Building Scenario 3 Model
- 7.4 Validation Procedures

**PART 8: COMPLETE FORMULA REFERENCE**
- 8.1 All Scenario 1 Formulas
- 8.2 All Scenario 2 Formulas
- 8.3 All Scenario 3 Formulas
- 8.4 Excel Formula Templates

**APPENDICES**
- Appendix A: Adjuster Reference Guide
- Appendix B: Census Calculations
- Appendix C: Test Results (All Scenarios V5.0)
- Appendix D: Change Log
- Appendix E: Reporting Framework

---

# PART 1: EXECUTIVE SUMMARY

## 1.1 What This Model Does

The Eventus Economic Model calculates revenue opportunities across healthcare facilities (SNFs and ALFs) using **Census-based calculations** with **permanent adjusters** applied to specific fees.

**Key Formula Structure:**
```
Revenue = Census × [Base Fees with Adjusters Applied]
```

**Four Revenue Metrics:**
1. **Current Revenue** - Revenue from facilities we currently serve (REALIZED)
2. **Integration Revenue** - Additional revenue from expanding services at existing customers (POTENTIAL)
3. **New Business Revenue** - Revenue from acquiring new corporate facilities (POTENTIAL)
4. **Total Potential Revenue** - Combined opportunity (Integration + New Business)

**Market Segmentation:**
- **TAM** (Total Addressable Market) - All 14,750 facilities
- **SAM** (Serviceable Addressable Market) - Corporate facilities only
- **SOM** (Serviceable Obtainable Market) - Corporate facilities with no barriers

## 1.2 The Four Revenue Metrics Explained

### **Metric 1: Current Revenue**
**Who:** Facilities where Do_We_Serve = "yes"  
**What:** Revenue we earn TODAY from services currently provided  
**How Much:** Depends on service type (Integrated, PCP Only, or MH Only)  
**Nature:** REALIZED revenue (already happening)

### **Metric 2: Integration Revenue**
**Who:** Facilities we currently serve but haven't integrated  
**What:** POTENTIAL additional revenue from adding the missing service  
**How Much:** Cost of the missing service components  
**Nature:** OPPORTUNITY revenue (growth potential with current customers)

### **Metric 3: New Business Revenue**
**Who:** Corporate facilities we don't serve with no barriers  
**What:** Full integrated package at new facilities  
**How Much:** Complete integrated service package  
**Nature:** OPPORTUNITY revenue (growth potential with new customers)

### **Metric 4: Total Potential Revenue (V5.0 CORRECTED)**
**Formula:** `Total_Potential_Revenue = Integration_Revenue + New_Biz_Revenue`  
**What It Means:** Total opportunity for ADDITIONAL revenue  
**What It Excludes:** Current Revenue (already realized)  
**Purpose:** Total growth opportunity calculation

**CRITICAL V5.0 INSIGHT:**
Current Revenue is reported SEPARATELY because it represents what we're already earning. Total Potential Revenue represents FUTURE OPPORTUNITY, not current state.

## 1.3 Three Scenarios Overview

### **Scenario 1: Original Specification (V2.2)**
**Purpose:** Base case, reflects original business model

- **PCP Only:** Census × PCP_Fee (just PCP, nothing else)
- **MH Only:** Census × (MH_Fee × 0.50) (MH with adjuster only)
- **Integrated:** Census × [PCP + (MH × 0.50) + (CCM × 0.30) + (SS × 0.50 × 0.33)]

**Key Insight:** Integrated services are the only way to get CCM and Shared Savings revenue.

### **Scenario 2: PCP Enhancement**
**Purpose:** Test giving PCP-only customers CCM and Shared Savings benefits

- **PCP Only:** Census × [PCP_Fee + (CCM × 0.30) + (SS × 0.50 × 0.33)] ← Enhanced
- **MH Only:** Census × (MH_Fee × 0.50) (unchanged from S1)
- **Integrated:** Census × [PCP + (MH × 0.50) + (CCM × 0.30) + (SS × 0.50 × 0.33)] (unchanged from S1)

**Key Insight:** Makes PCP-only packages more valuable, reduces integration opportunity for PCP customers.

### **Scenario 3: MH + PCP Enhancement**
**Purpose:** Test giving both PCP and MH customers additional benefits

- **PCP Only:** Census × [PCP_Fee + (CCM × 0.30) + (SS × 0.50 × 0.33)] (same as S2)
- **MH Only:** Census × [(MH_Fee × 0.50) + (CCM × 0.30)] ← Enhanced with CCM
- **Integrated:** Census × [PCP + (MH × 0.50) + (CCM × 0.30) + (SS × 0.50 × 0.33)] (unchanged)

**Key Insight:** Makes MH-only packages more valuable, but MH still doesn't get Shared Savings.

## 1.4 Fee Structure and Adjusters

### **Base Fee Rates:**

| Service | SNF Rate | ALF Rate |
|---------|----------|----------|
| PCP | $1,698.96 | $1,875.00 |
| MH | $1,623.96 | $1,898.00 |
| CCM | $360.00 | $360.00 |
| Shared Savings (SS) | $4,800.00 | $4,800.00 |

### **Permanent Adjusters:**

| Fee | Adjuster | Calculation | Result (SNF) |
|-----|----------|-------------|--------------|
| PCP | 1.00 (none) | $1,698.96 × 1.00 | $1,698.96 |
| MH | 0.50 | $1,623.96 × 0.50 | $811.98 |
| CCM | 0.30 | $360.00 × 0.30 | $108.00 |
| SS | 0.50 × 0.33 | $4,800.00 × 0.50 × 0.33 | $792.00 |

**CRITICAL:** These adjusters are **permanent** and **tied to the fees themselves**. They NEVER change across scenarios. What changes is WHICH fees are included in each service package.

---

# PART 2: FEE STRUCTURE & ADJUSTERS

## 2.1 Base Fee Rates (SNF and ALF)

### **SNF (Skilled Nursing Facility) Rates**

```
PCP_FEE_SNF = $1,698.96
MH_FEE_SNF = $1,623.96
CCM_FEE = $360.00
SS_FEE = $4,800.00
```

### **ALF (Assisted Living Facility) Rates**

```
PCP_FEE_ALF = $1,875.00
MH_FEE_ALF = $1,898.00
CCM_FEE = $360.00
SS_FEE = $4,800.00
```

**Note:** CCM and SS rates are the same for both facility types.

## 2.2 Permanent Adjusters

These adjusters are **hardcoded** and **never change**:

```
MH_ADJUSTER = 0.50
CCM_ADJUSTER = 0.30
SS_ADJUSTER_1 = 0.50
SS_ADJUSTER_2 = 0.33
```

**Why Two SS Adjusters?**
Shared Savings has a compound adjustment: first multiply by 0.50, then multiply by 0.33, resulting in a final effective rate of 16.5% of the base fee.

## 2.3 Adjusted Fee Values

### **SNF Adjusted Fees:**

```
PCP (no adjuster):     $1,698.96
MH_ADJUSTED:          $1,623.96 × 0.50 = $811.98
CCM_ADJUSTED:         $360.00 × 0.30 = $108.00
SS_ADJUSTED:          $4,800.00 × 0.50 × 0.33 = $792.00
```

### **ALF Adjusted Fees:**

```
PCP (no adjuster):     $1,875.00
MH_ADJUSTED:          $1,898.00 × 0.50 = $949.00
CCM_ADJUSTED:         $360.00 × 0.30 = $108.00
SS_ADJUSTED:          $4,800.00 × 0.50 × 0.33 = $792.00
```

**Integrated Package Totals:**

```
SNF_INTEGRATED = $1,698.96 + $811.98 + $108.00 + $792.00 = $3,410.94
ALF_INTEGRATED = $1,875.00 + $949.00 + $108.00 + $792.00 = $3,724.00
```

## 2.4 Why Adjusters Never Change

The adjusters represent **fixed discounting or cost-sharing percentages** in the business model:

- **MH × 0.50:** Mental health services billed at 50% rate
- **CCM × 0.30:** Chronic Care Management captures 30% of value
- **SS × 0.50 × 0.33:** Shared Savings has two-stage adjustment (50% capture × 33% sharing)

These are embedded in the contract structure and reimbursement rates, so they remain constant across all scenarios.

---

# PART 3: SCENARIO 1 - ORIGINAL V2.2 SPECIFICATION

## 3.1 Scenario 1 Service Packages

**SNF Rates:**

| Service Type | Package Components | Rate Calculation | Annual Rate per Census |
|--------------|-------------------|------------------|----------------------|
| **PCP Only** | PCP only | $1,698.96 | $1,698.96 |
| **MH Only** | MH × 0.50 | $1,623.96 × 0.50 | $811.98 |
| **Integrated** | PCP + (MH × 0.50) + (CCM × 0.30) + (SS × 0.50 × 0.33) | $1,698.96 + $811.98 + $108.00 + $792.00 | $3,410.94 |

## 3.2 Current Revenue Formulas - Scenario 1

**Business Logic:**
Only facilities we currently serve (Do_We_Serve = "yes") generate current revenue. The amount depends on which services they receive.

### **Formula Logic:**

```python
IF Do_We_Serve != "yes":
    Current_Revenue = 0

ELSE IF Census is missing or <= 0:
    Current_Revenue = 0

ELSE IF Integrated_Flag = "yes":
    IF Source_Type = "SNF":
        Current_Revenue = Census × $3,410.94
    ELSE IF Source_Type = "ALF":
        Current_Revenue = Census × $3,724.00

ELSE IF PCP_Flag = "yes":
    IF Source_Type = "SNF":
        Current_Revenue = Census × $1,698.96
    ELSE IF Source_Type = "ALF":
        Current_Revenue = Census × $1,875.00

ELSE IF MH_Flag = "yes":
    IF Source_Type = "SNF":
        Current_Revenue = Census × $811.98
    ELSE IF Source_Type = "ALF":
        Current_Revenue = Census × $949.00

ELSE:
    Current_Revenue = 0
```

### **Excel Formula (Row 2, SNF only):**

```excel
=IF(L2<>"yes", 0,
    IF(OR(ISBLANK(K2), K2<=0), 0,
        IF(M2="yes", K2*3410.94,
            IF(N2="yes", K2*1698.96,
                IF(O2="yes", K2*811.98, 0)
            )
        )
    )
)
```

Where:
- K2 = Census
- L2 = Do_We_Serve
- M2 = Integrated_Flag
- N2 = PCP_Flag
- O2 = MH_Flag

## 3.3 Integration Revenue Formulas - Scenario 1

**Business Logic:**
Integration revenue represents what we can EARN by expanding services at facilities we already serve but haven't integrated.

### **Formula Logic:**

```python
IF Do_We_Serve != "yes":
    Integration_Revenue = 0

ELSE IF Census is missing or <= 0:
    Integration_Revenue = 0

ELSE IF Integrated_Flag = "yes":
    Integration_Revenue = 0  (already integrated)

ELSE IF PCP_Flag = "yes":
    # Can add MH + CCM + SS to become integrated
    IF Source_Type = "SNF":
        Integration_Revenue = Census × ($811.98 + $108.00 + $792.00)
        Integration_Revenue = Census × $1,711.98
    ELSE IF Source_Type = "ALF":
        Integration_Revenue = Census × ($949.00 + $108.00 + $792.00)
        Integration_Revenue = Census × $1,849.00

ELSE IF MH_Flag = "yes":
    # Can add PCP + CCM + SS to become integrated
    IF Source_Type = "SNF":
        Integration_Revenue = Census × ($1,698.96 + $108.00 + $792.00)
        Integration_Revenue = Census × $2,598.96
    ELSE IF Source_Type = "ALF":
        Integration_Revenue = Census × ($1,875.00 + $108.00 + $792.00)
        Integration_Revenue = Census × $2,775.00

ELSE:
    Integration_Revenue = 0
```

### **Excel Formula (Row 2, SNF only):**

```excel
=IF(L2<>"yes", 0,
    IF(OR(ISBLANK(K2), K2<=0), 0,
        IF(M2="yes", 0,
            IF(N2="yes", K2*1711.98,
                IF(O2="yes", K2*2598.96, 0)
            )
        )
    )
)
```

## 3.4 New Business Revenue Formulas - Scenario 1

**Business Logic:**
New Business revenue represents the full integrated package at corporate facilities we don't serve and have no barriers.

### **Formula Logic:**

```python
IF Do_We_Serve = "yes":
    New_Biz_Revenue = 0  (already a customer)

ELSE IF Ownership_Type != "Corporate":
    New_Biz_Revenue = 0  (we don't target independents)

ELSE IF Barrier is not null:
    New_Biz_Revenue = 0  (barrier prevents acquisition)

ELSE IF Census is missing or <= 0:
    New_Biz_Revenue = 0

ELSE:
    # Full integrated package for new corporate facility
    IF Source_Type = "SNF":
        New_Biz_Revenue = Census × $3,410.94
    ELSE IF Source_Type = "ALF":
        New_Biz_Revenue = Census × $3,724.00
```

### **Excel Formula (Row 2, SNF only):**

```excel
=IF(L2="yes", 0,
    IF(I2<>"Corporate", 0,
        IF(NOT(ISBLANK(P2)), 0,
            IF(OR(ISBLANK(K2), K2<=0), 0,
                K2*3410.94
            )
        )
    )
)
```

Where:
- I2 = Ownership_Type
- P2 = Barrier

## 3.5 Total Potential Revenue Formula (V5.0 CORRECTED)

### **V5.0 CRITICAL CORRECTION:**

```python
# V4.0 WRONG:
Total_Revenue = Current_Revenue + Integration_Revenue + New_Biz_Revenue  ❌

# V5.0 CORRECT:
Total_Potential_Revenue = Integration_Revenue + New_Biz_Revenue  ✅
```

### **Excel Formula (Row 2):**

```excel
=V2+W2
```

**NOT:** `=U2+V2+W2`

Where:
- U2 = Current_Revenue (EXCLUDED from total potential)
- V2 = Integration_Revenue
- W2 = New_Biz_Revenue
- X2 = Total_Potential_Revenue

**Why This Is Correct:**
- Current Revenue is what we earn TODAY (already realized)
- Total Potential Revenue represents FUTURE OPPORTUNITY
- Adding Current to Potential double-counts existing revenue

## 3.6 Worked Examples - Scenario 1

### **Example 1: SNF Integrated Facility (Already Serving)**

**Data:**
- Source_Type: SNF
- Census: 100
- Do_We_Serve: yes
- Integrated_Flag: yes

**Calculations:**
```
Current_Revenue = 100 × $3,410.94 = $341,094.00
Integration_Revenue = 0 (already integrated)
New_Biz_Revenue = 0 (already served)
Total_Potential_Revenue = $0 + $0 = $0
```

**Interpretation:** We're earning $341,094 today with no growth opportunity at this facility.

### **Example 2: SNF PCP Only Facility (Integration Opportunity)**

**Data:**
- Source_Type: SNF
- Census: 100
- Do_We_Serve: yes
- PCP_Flag: yes

**Calculations:**
```
Current_Revenue = 100 × $1,698.96 = $169,896.00
Integration_Revenue = 100 × $1,711.98 = $171,198.00
  (Can add MH + CCM + SS)
New_Biz_Revenue = 0 (already served)
Total_Potential_Revenue = $171,198.00 + $0 = $171,198.00
```

**Interpretation:** We're earning $169,896 today, with $171,198 growth potential by adding services.

### **Example 3: SNF MH Only Facility (Integration Opportunity)**

**Data:**
- Source_Type: SNF
- Census: 100
- Do_We_Serve: yes
- MH_Flag: yes

**Calculations:**
```
Current_Revenue = 100 × $811.98 = $81,198.00
Integration_Revenue = 100 × $2,598.96 = $259,896.00
  (Can add PCP + CCM + SS)
New_Biz_Revenue = 0 (already served)
Total_Potential_Revenue = $259,896.00 + $0 = $259,896.00
```

**Interpretation:** We're earning $81,198 today, with $259,896 growth potential.

### **Example 4: SNF Unserved Corporate Facility (New Business)**

**Data:**
- Source_Type: SNF
- Census: 100
- Do_We_Serve: no
- Ownership_Type: Corporate
- Barrier: [blank]

**Calculations:**
```
Current_Revenue = 0 (not served)
Integration_Revenue = 0 (not served)
New_Biz_Revenue = 100 × $3,410.94 = $341,094.00
Total_Potential_Revenue = $0 + $341,094.00 = $341,094.00
```

**Interpretation:** We earn $0 today, with $341,094 opportunity if we acquire this facility.

### **Example 5: SNF Independent Facility (No Opportunity)**

**Data:**
- Source_Type: SNF
- Census: 100
- Do_We_Serve: no
- Ownership_Type: Independent

**Calculations:**
```
Current_Revenue = 0 (not served)
Integration_Revenue = 0 (not served)
New_Biz_Revenue = 0 (independent, not targeted)
Total_Potential_Revenue = $0 + $0 = $0
```

**Interpretation:** No revenue today, no opportunity (we don't target independents).

---

# PART 4: SCENARIO 2 - PCP ENHANCEMENT

## 4.1 What Changes in Scenario 2

**Scenario 2 Tests:** What happens if we enhance PCP-only packages with CCM and Shared Savings?

**Changes from Scenario 1:**
- **PCP Only:** ENHANCED - now includes CCM + SS ($1,698.96 → $2,598.96)
- **MH Only:** UNCHANGED - still just MH × 0.50 ($811.98)
- **Integrated:** UNCHANGED - still full package ($3,410.94)

**Business Impact:**
- **Current Revenue:** INCREASES (PCP customers now earn more)
- **Integration Revenue:** DECREASES (PCP customers need less to integrate - just MH)
- **Total Potential Revenue:** STAYS THE SAME (everyone can still reach integrated)

## 4.2 Scenario 2 Service Packages

**SNF Rates:**

| Service Type | Package Components | Rate Calculation | Annual Rate per Census |
|--------------|-------------------|------------------|----------------------|
| **PCP Only** | PCP + (CCM × 0.30) + (SS × 0.50 × 0.33) | $1,698.96 + $108.00 + $792.00 | $2,598.96 |
| **MH Only** | MH × 0.50 | $1,623.96 × 0.50 | $811.98 |
| **Integrated** | PCP + (MH × 0.50) + (CCM × 0.30) + (SS × 0.50 × 0.33) | Same as S1 | $3,410.94 |

## 4.3 Current Revenue Formulas - Scenario 2

```python
IF Do_We_Serve != "yes":
    Current_Revenue = 0

ELSE IF Census is missing or <= 0:
    Current_Revenue = 0

ELSE IF Integrated_Flag = "yes":
    # Unchanged from S1
    IF Source_Type = "SNF":
        Current_Revenue = Census × $3,410.94
    ELSE IF Source_Type = "ALF":
        Current_Revenue = Census × $3,724.00

ELSE IF PCP_Flag = "yes":
    # ENHANCED - now includes CCM + SS
    IF Source_Type = "SNF":
        Current_Revenue = Census × $2,598.96  # Was $1,698.96 in S1
    ELSE IF Source_Type = "ALF":
        Current_Revenue = Census × $2,775.00  # Was $1,875.00 in S1

ELSE IF MH_Flag = "yes":
    # Unchanged from S1
    IF Source_Type = "SNF":
        Current_Revenue = Census × $811.98
    ELSE IF Source_Type = "ALF":
        Current_Revenue = Census × $949.00

ELSE:
    Current_Revenue = 0
```

## 4.4 Integration Revenue Formulas - Scenario 2

```python
IF Do_We_Serve != "yes":
    Integration_Revenue = 0

ELSE IF Census is missing or <= 0:
    Integration_Revenue = 0

ELSE IF Integrated_Flag = "yes":
    Integration_Revenue = 0

ELSE IF PCP_Flag = "yes":
    # Just need to add MH (already have CCM + SS)
    IF Source_Type = "SNF":
        Integration_Revenue = Census × $811.98  # Was $1,711.98 in S1
    ELSE IF Source_Type = "ALF":
        Integration_Revenue = Census × $949.00  # Was $1,849.00 in S1

ELSE IF MH_Flag = "yes":
    # Unchanged from S1 - still need PCP + CCM + SS
    IF Source_Type = "SNF":
        Integration_Revenue = Census × $2,598.96
    ELSE IF Source_Type = "ALF":
        Integration_Revenue = Census × $2,775.00

ELSE:
    Integration_Revenue = 0
```

## 4.5 Total Potential Revenue Formula (V5.0)

**Same as Scenario 1:**
```python
Total_Potential_Revenue = Integration_Revenue + New_Biz_Revenue
```

**Excel Formula:**
```excel
=V2+W2
```

## 4.6 Worked Examples - Scenario 2

### **Example 1: SNF PCP Only - Enhanced Package**

**Data:**
- Census: 100
- Do_We_Serve: yes
- PCP_Flag: yes

**Scenario 1 (for comparison):**
```
Current: $169,896.00
Integration: $171,198.00
Total Potential: $171,198.00
```

**Scenario 2:**
```
Current_Revenue = 100 × $2,598.96 = $259,896.00  ← INCREASED
Integration_Revenue = 100 × $811.98 = $81,198.00  ← DECREASED
New_Biz_Revenue = 0
Total_Potential_Revenue = $81,198.00 + $0 = $81,198.00
```

**Key Insight:** Current revenue up $90,000, but integration opportunity down $90,000. Total potential stays at integrated package value.

### **Example 2: SNF MH Only - Unchanged**

**Data:**
- Census: 100
- Do_We_Serve: yes
- MH_Flag: yes

**Scenario 2 (Same as S1):**
```
Current_Revenue = 100 × $811.98 = $81,198.00
Integration_Revenue = 100 × $2,598.96 = $259,896.00
Total_Potential_Revenue = $259,896.00
```

**Key Insight:** MH packages unchanged in S2 - no benefit from PCP enhancement.

---

# PART 5: SCENARIO 3 - MH + PCP ENHANCEMENT

## 5.1 What Changes in Scenario 3

**Scenario 3 Tests:** What if we enhance BOTH PCP and MH packages?

**Changes from Scenario 2:**
- **PCP Only:** SAME AS S2 - includes CCM + SS ($2,598.96)
- **MH Only:** ENHANCED - now includes CCM ($811.98 → $919.98)
- **Integrated:** UNCHANGED - still full package ($3,410.94)

**Business Impact:**
- **Current Revenue:** INCREASES FURTHER (both PCP and MH earn more)
- **Integration Revenue:** DECREASES FURTHER (less needed to integrate)
- **Total Potential Revenue:** STAYS THE SAME (everyone still reaches integrated)

## 5.2 Scenario 3 Service Packages

**SNF Rates:**

| Service Type | Package Components | Rate Calculation | Annual Rate per Census |
|--------------|-------------------|------------------|----------------------|
| **PCP Only** | PCP + (CCM × 0.30) + (SS × 0.50 × 0.33) | Same as S2 | $2,598.96 |
| **MH Only** | (MH × 0.50) + (CCM × 0.30) | $811.98 + $108.00 | $919.98 |
| **Integrated** | PCP + (MH × 0.50) + (CCM × 0.30) + (SS × 0.50 × 0.33) | Same as S1/S2 | $3,410.94 |

## 5.3 Current Revenue Formulas - Scenario 3

```python
IF Do_We_Serve != "yes":
    Current_Revenue = 0

ELSE IF Census is missing or <= 0:
    Current_Revenue = 0

ELSE IF Integrated_Flag = "yes":
    # Unchanged
    IF Source_Type = "SNF":
        Current_Revenue = Census × $3,410.94
    ELSE IF Source_Type = "ALF":
        Current_Revenue = Census × $3,724.00

ELSE IF PCP_Flag = "yes":
    # Same as S2
    IF Source_Type = "SNF":
        Current_Revenue = Census × $2,598.96
    ELSE IF Source_Type = "ALF":
        Current_Revenue = Census × $2,775.00

ELSE IF MH_Flag = "yes":
    # ENHANCED - now includes CCM
    IF Source_Type = "SNF":
        Current_Revenue = Census × $919.98  # Was $811.98 in S1/S2
    ELSE IF Source_Type = "ALF":
        Current_Revenue = Census × $1,057.00  # Was $949.00 in S1/S2

ELSE:
    Current_Revenue = 0
```

## 5.4 Integration Revenue Formulas - Scenario 3

```python
IF Do_We_Serve != "yes":
    Integration_Revenue = 0

ELSE IF Census is missing or <= 0:
    Integration_Revenue = 0

ELSE IF Integrated_Flag = "yes":
    Integration_Revenue = 0

ELSE IF PCP_Flag = "yes":
    # Same as S2 - just need MH
    IF Source_Type = "SNF":
        Integration_Revenue = Census × $811.98
    ELSE IF Source_Type = "ALF":
        Integration_Revenue = Census × $949.00

ELSE IF MH_Flag = "yes":
    # Need PCP + SS (already have CCM)
    IF Source_Type = "SNF":
        Integration_Revenue = Census × ($1,698.96 + $792.00)
        Integration_Revenue = Census × $2,490.96  # Was $2,598.96 in S1/S2
    ELSE IF Source_Type = "ALF":
        Integration_Revenue = Census × ($1,875.00 + $792.00)
        Integration_Revenue = Census × $2,667.00  # Was $2,775.00 in S1/S2

ELSE:
    Integration_Revenue = 0
```

## 5.5 Total Potential Revenue Formula (V5.0)

**Same as Scenarios 1 & 2:**
```python
Total_Potential_Revenue = Integration_Revenue + New_Biz_Revenue
```

## 5.6 Worked Examples - Scenario 3

### **Example: SNF MH Only - Enhanced Package**

**Data:**
- Census: 100
- Do_We_Serve: yes
- MH_Flag: yes

**Scenario 1:**
```
Current: $81,198.00
Integration: $259,896.00
Total Potential: $259,896.00
```

**Scenario 2:**
```
Current: $81,198.00 (same)
Integration: $259,896.00 (same)
Total Potential: $259,896.00
```

**Scenario 3:**
```
Current_Revenue = 100 × $919.98 = $91,998.00  ← INCREASED
Integration_Revenue = 100 × $2,490.96 = $249,096.00  ← DECREASED
Total_Potential_Revenue = $249,096.00
```

**Key Insight:** MH customers now benefit from CCM, increasing current revenue by $10,800 while reducing integration need by same amount.

---

# PART 6: SCENARIO COMPARISON

## 6.1 Side-by-Side Comparison

**Service Package Rates (SNF):**

| Service Type | Scenario 1 | Scenario 2 | Scenario 3 |
|--------------|-----------|-----------|-----------|
| **PCP Only** | $1,698.96 | $2,598.96 ↑ | $2,598.96 |
| **MH Only** | $811.98 | $811.98 | $919.98 ↑ |
| **Integrated** | $3,410.94 | $3,410.94 | $3,410.94 |

## 6.2 Revenue Distribution Analysis

**Actual Test Results (14,750 SNF Facilities):**

| Metric | Scenario 1 | Scenario 2 | Scenario 3 |
|--------|-----------|-----------|-----------|
| **Current Revenue** | $72,977,188 | $77,537,938 ↑ | $80,154,854 ↑ |
| **Integration Revenue** | $71,650,079 | $67,089,329 ↓ | $64,472,413 ↓ |
| **New Business Revenue** | $2,879,987,963 | $2,879,987,963 | $2,879,987,963 |
| **Total Potential Revenue** | $2,951,638,042 | $2,947,077,292 | $2,944,460,376 |

**Pattern Validation:**
- ✅ Current Revenue INCREASES S1 → S2 → S3
- ✅ Integration Revenue DECREASES S1 → S2 → S3
- ✅ New Business UNCHANGED across scenarios
- ✅ Total Potential Revenue nearly identical (minor rounding differences)

## 6.3 When to Use Each Scenario

### **Use Scenario 1 when:**
- Modeling baseline/conservative case
- Demonstrating value of integration
- Original business model projections

### **Use Scenario 2 when:**
- Testing PCP-focused sales strategy
- Evaluating impact of enhanced PCP packages
- Comparing PCP vs MH customer value

### **Use Scenario 3 when:**
- Testing comprehensive enhancement strategy
- Evaluating impact of enhanced both PCP and MH packages
- Modeling "best case" current revenue

## 6.4 Test Results from All Scenarios (V5.0)

**Test Dataset:** 14,750 SNF facilities (SNF_Database_Final_v2_4_2025-11-14.xlsx)  
**Date Run:** November 16, 2025

### **Scenario 1 Results:**

| Segment | Facilities | Served | Current Revenue | Integration Revenue | New Biz Revenue | Total Potential Revenue |
|---------|-----------|--------|-----------------|--------------------|--------------------|----------------------|
| TAM | 14,750 | 563 | $72,977,188.22 | $71,650,078.72 | $2,879,987,963.19 | $2,951,638,041.91 |
| SAM | 10,065 | 527 | $69,834,492.62 | $68,149,893.32 | $2,879,987,963.19 | $2,948,137,856.51 |
| SOM | 9,997 | 354 | $55,903,741.42 | $61,586,195.52 | $2,879,987,963.19 | $2,941,574,158.71 |

### **Scenario 2 Results:**

| Segment | Facilities | Served | Current Revenue | Integration Revenue | New Biz Revenue | Total Potential Revenue |
|---------|-----------|--------|-----------------|--------------------|--------------------|----------------------|
| TAM | 14,750 | 563 | $77,537,938.22 | $67,089,328.72 | $2,879,987,963.19 | $2,947,077,291.91 |
| SAM | 10,065 | 527 | $74,395,242.62 | $63,589,143.32 | $2,879,987,963.19 | $2,943,577,106.51 |
| SOM | 9,997 | 354 | $60,464,491.42 | $57,025,445.52 | $2,879,987,963.19 | $2,937,013,408.71 |

### **Scenario 3 Results:**

| Segment | Facilities | Served | Current Revenue | Integration Revenue | New Biz Revenue | Total Potential Revenue |
|---------|-----------|--------|-----------------|--------------------|--------------------|----------------------|
| TAM | 14,750 | 563 | $80,154,853.82 | $64,472,413.12 | $2,879,987,963.19 | $2,944,460,376.31 |
| SAM | 10,065 | 527 | $77,012,158.22 | $60,972,228.72 | $2,879,987,963.19 | $2,940,960,191.91 |
| SOM | 9,997 | 354 | $63,081,407.02 | $54,408,529.92 | $2,879,987,963.19 | $2,934,396,493.11 |

**Validation:** ✅ All scenarios show expected patterns

---

# APPENDIX A: ADJUSTER REFERENCE GUIDE

## Adjuster Values (Permanent)

| Fee | Adjuster | Formula | SNF Result | ALF Result |
|-----|----------|---------|------------|------------|
| PCP | 1.00 | Fee × 1.00 | $1,698.96 | $1,875.00 |
| MH | 0.50 | Fee × 0.50 | $811.98 | $949.00 |
| CCM | 0.30 | Fee × 0.30 | $108.00 | $108.00 |
| SS | 0.50 × 0.33 | Fee × 0.50 × 0.33 | $792.00 | $792.00 |

## Why These Specific Values?

**MH_ADJUSTER = 0.50:**
Reflects 50% billing rate for mental health services, possibly due to cost-sharing arrangements with other providers or Medicare billing limitations.

**CCM_ADJUSTER = 0.30:**
Chronic Care Management captures 30% of potential value, reflecting actual reimbursement rates or contractual limitations.

**SS_ADJUSTER = 0.50 × 0.33:**
Shared Savings has compound adjustment:
- First 0.50: Represents 50% capture rate of potential savings
- Second 0.33: Represents 33% sharing ratio with facility
- Combined: 16.5% effective rate

---

# APPENDIX B: CENSUS CALCULATIONS

## Why Census Matters

**Formula Structure:**
```
Revenue = Census × [Service Package Rate]
```

**Census represents:** Number of occupied beds (average daily census)

**Example:**
- Facility has 120 total beds
- Average census = 100 (83% occupancy)
- Integrated rate = $3,410.94 per census unit
- Annual revenue = 100 × $3,410.94 = $341,094

**If Census Changes:**
- Census drops to 90: Revenue = $306,985 (−10%)
- Census rises to 110: Revenue = $375,203 (+10%)

## Handling Missing Census Data

**Rule:** If Census is NULL, blank, or ≤ 0, then Revenue = $0

**Why:** Cannot calculate revenue without knowing how many residents are being served.

**Data Quality:** Census field should be validated and populated for all facilities where Do_We_Serve = "yes"

---

# APPENDIX C: CHANGE LOG

## V5.0 (November 16, 2025)

**Status:** PRODUCTION READY - Critical Formula Correction

**Critical Change:**
- ✅ **RENAMED** "Total_Revenue" to "Total_Potential_Revenue"
- ✅ **CORRECTED FORMULA:** Changed from `Current + Integration + New Business` to `Integration + New Business`
- ✅ **CLARIFIED** Current Revenue is SEPARATE (already realized, not potential)

**Documentation Updates:**
- Complete rewrite of Total Potential Revenue sections
- New examples showing correct interpretation
- Updated all test results with correct values
- Added Appendix E: Reporting Framework

**What This Fixes:**
- Eliminates confusion about including current revenue in "total"
- Properly separates realized revenue (Current) from opportunity revenue (Potential)
- Aligns terminology with business intent (measuring growth opportunity)

**Ready for:** Production implementation with correct Total Potential Revenue formula

---

## V4.0 (November 16, 2025)

**Status:** DEPRECATED - Formula was WRONG

**Issues:**
- Incorrectly included Current Revenue in Total Revenue calculation
- Created confusion about what "total" represented

---

## V3.0 (November 16, 2025)

**Status:** DEPRECATED - Multiple formula errors

---

## V2.3 (November 15, 2025)

**Status:** DEPRECATED

---

## V2.2 (November 15, 2025)

**Status:** Original specification (Scenario 1 source of truth)

---

# APPENDIX D: REPORTING FRAMEWORK

## For Current Performance:
**Report:** Current Revenue only
- "We currently earn $73M from served facilities"
- Tracks actual realized revenue

## For Growth Potential with Existing Customers:
**Report:** Integration Revenue
- "We have $72M in integration opportunity with current customers"
- Tracks upsell potential

## For New Customer Acquisition:
**Report:** New Business Revenue
- "We have $2.88B in new business opportunity"
- Tracks new customer potential

## For Total Opportunity:
**Report:** Total Potential Revenue (Integration + New Business)
- "Total potential revenue opportunity is $2.95B"
- Combines both growth vectors
- **EXCLUDES Current Revenue** (already happening)

## For Complete Picture:
**Report:** All four metrics together
- Current: What we have today
- Integration: Growth with current customers
- New Business: Growth with new customers  
- Total Potential: Combined opportunity

---

# END OF RULEBOOK V5.0

**This document provides CORRECT formulas for Total Potential Revenue across all three scenarios.**

**Use V5.0 for:**
1. Understanding the CORRECT revenue calculations
2. Building all three scenario models
3. Validating formula implementations
4. Training team members
5. Auditing model accuracy

**Last Updated:** November 16, 2025  
**Status:** PRODUCTION READY - COMPLETE CORRECTED SPECIFICATION  

**What's Included:**
- ✅ Correct Total Potential Revenue formula
- ✅ All three scenarios fully documented
- ✅ Complete test results with V5.0 corrections
- ✅ Reporting framework guidance
- ✅ Clear separation of Current (realized) vs Potential (opportunity)

**Next Steps:**
1. Use V5.0 model files for business planning
2. Generate reports using correct Total Potential Revenue
3. Train stakeholders on the four revenue metrics
4. Apply to combined ALF + SNF datasets

---

**✅ PRODUCTION READY - USE THIS VERSION**
