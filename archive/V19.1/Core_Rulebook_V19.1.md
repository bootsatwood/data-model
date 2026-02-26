# Core Rulebook V19.1
## Healthcare Facility Database & Scenario Model - Authoritative Reference

**Version**: 19.1  
**Date**: November 2025  
**Status**: PRODUCTION READY  
**Scope**: Database specification, fee structure, scenario calculations

---

## Document Architecture

This Core Rulebook is part of a modular documentation system:

```
CORE RULEBOOK (this document)
├─ Database specification
├─ Fee structure governance
├─ Scenario calculation methodology
├─ Core QC Protocol
│
REPORT COMPENDIUMS (separate documents)
├─ Comprehensive_Report_Compendium_V19.md
├─ Metro_Priority_Targets_Compendium_V19.md
├─ [Additional report-specific compendiums]
```

**Handoff Principle**: This Core Rulebook must be validated (Section 6 QC Protocol) before any Report Compendium work begins. Reports inherit from validated scenarios.

---

## 1. System Overview & Governance

### 1.1 Data Flow Architecture

```
Combined Database (Source of Truth)
         ↓
Fee Schedule ──→ Economic Model Scenarios (S1, S2, S3)
                              ↓
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
   Comprehensive      Metro Priority     Custom Reports
   Report Workbook    Targets Report     (per compendium)
```

**Governing Principles:**

1. **Combined Database** is the single source of truth for all facility data
2. All data changes must originate at the database level
3. **Fee Schedule** is maintained independently and feeds scenario calculations
4. **Economic Model Scenarios** inherit from database and apply fee calculations
5. All reports and validation workbooks are generated FROM scenarios
6. Never edit downstream files to change source data

### 1.2 Version Control Architecture

**Three Independent Version Tracks:**

| Track | Scope | Example | Triggers Version Increment |
|-------|-------|---------|---------------------------|
| **Database** | Facility data, barriers, service flags | V18.7 | Any facility add/remove, barrier change, service flag update |
| **Scenario/Fee** | Fee structure, calculation methodology | V19.1 | Fee value change, adjuster change, formula correction |
| **Reports** | Output generation, formatting | Per compendium | Filter logic change, output structure change |

**Version Notation:**
- Major.Minor format (e.g., V19.1)
- Minor fixes: V19.1 → V19.2 → V19.3
- Major changes: V19.x → V20.0
- **Never reuse version numbers**
- **Never overwrite files - always increment**

### 1.3 Prohibited Actions

**The following actions require explicit written authorization:**

1. Modify fee values in Fee Schedule
2. Change adjuster calculations
3. Alter revenue formulas
4. Edit scenario files directly (must update database first)
5. Skip QC validation before delivery
6. Deliver files without verification
7. Reuse or overwrite existing version numbers

**Violation Protocol:** Any unauthorized action triggers full audit and potential rollback to last verified version.

### 1.4 Fee Change Management

**MANDATORY for any fee modification:**

1. **Written Authorization** - Explicit approval from project owner required
2. **Impact Analysis** - Calculate full impact before implementation
3. **Documentation** - Update rulebook and comparison report
4. **Validation** - Run Core QC Protocol (Section 6) to verify

### 1.5 Production Package Requirements

**Core Package Contents:**

| File Type | File Name Pattern | Purpose |
|-----------|------------------|---------|
| **Core Data** | Combined_Database_FINAL_Vxx.xlsx | Source of truth for all facility data |
| **Scenarios** | Economic_Model_Scenario_1_Combined_Vxx.xlsx | Baseline service packages |
| | Economic_Model_Scenario_2_Combined_Vxx.xlsx | PCP Enhanced packages |
| | Economic_Model_Scenario_3_Combined_Vxx.xlsx | Comprehensive packages |
| **Reference** | Fee_Schedule_Reference_Vxx.xlsx | Authoritative fee lookup |
| **Documentation** | Core_Rulebook_Vxx.md | This document |

**Compendium Integrity Rules:**

1. **Version Consistency**: All core files must share same version number
2. **Complete Set**: Never deliver partial core packages
3. **QC Gate**: Core QC Protocol must pass before report generation
4. **Documentation Chain**: Changes require comparison documentation

---

## 2. Combined Database

### 2.1 Database Foundation

**Current Version:** V18.7 (20,943 facilities)

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Facilities** | 20,943 | 100% |
| SNF Facilities | 15,244 | 72.8% |
| ALF Facilities | 5,699 | 27.2% |
| Corporate Facilities | 12,053 | 57.5% |
| Independent Facilities | 8,890 | 42.5% |
| Corporate Chains | 1,026 | - |
| Facilities We Serve | 1,663 | 7.9% |
| Facilities with Barriers | 848 | 4.0% |

### 2.2 Source File Evolution

| Version | Date | Source Description | Total Facilities | Key Changes |
|---------|------|-------------------|------------------|-------------|
| V8.0 Base | Nov 2025 | SNF Stream V2.5 + ALF Combined V9.0 merger | 17,434 | Initial unified database |
| V11.0 | Nov 2025 | Book1.xlsx Barrier Integration | 17,434 | Propagated 111 barriers to 786 facilities |
| V15.0 | Nov 2025 | Ownership consistency corrections | 17,434 | TAM/SAM/SOM methodology refined |
| V17.1 | Nov 2025 | Eventus WholeHealth 8-state integration | 21,023 | GPS deduplication, Four-Rule reclassification |
| **V18.7** | Nov 2025 | PowerBI reconciliation + strategic barrier removals | **20,943** | -80 facilities, -535 barriers |

### 2.3 Ownership Classification

**Column to Use:** `Ownership_Type`

**Classification Method:** Four-Rule Count-Based Hierarchy

#### Rule 1: Blank Corporate Name → Independent
```
IF Corporate_Name IS NULL OR Corporate_Name = ''
  THEN Ownership_Type = "Independent"
```

#### Rule 2: "INDEPENDENT" Placeholder → Independent
```
IF UPPER(Corporate_Name) = "INDEPENDENT"
  THEN Ownership_Type = "Independent"
```

#### Rule 3: Multi-Facility Chains → Corporate
```
IF COUNT(Corporate_Name) > 1 across entire database
  THEN Ownership_Type = "Corporate"
```

#### Rule 4: Single-Facility Operators → Independent
```
IF COUNT(Corporate_Name) = 1 across entire database
  THEN Ownership_Type = "Independent"
```

**Critical Distinction:**

| Ownership Type | Definition | Example |
|---------------|------------|---------|
| Corporate | Operates 2+ facilities | TRILOGY HEALTH SERVICES (186 facilities) |
| Independent | Operates 1 facility only | HERITAGE MANOR, LLC (1 facility) |

**CRITICAL**: Do NOT use `Corporate_Name` column presence to determine ownership. The `Corporate_Name` field may be populated for Independent facilities (particularly single-facility LLCs). Always use `Ownership_Type` column.

### 2.4 Facility Type Classification

**Column to Use:** `Source_Type`

| Value | Definition | V18.7 Count |
|-------|------------|-------------|
| SNF | Skilled Nursing Facility | 15,244 |
| ALF | Assisted Living Facility | 5,699 |

### 2.5 Service Status

**Column to Use:** `Do_We_Serve`

| Value | Definition | V18.7 Count |
|-------|------------|-------------|
| Yes | Currently served facility | 1,663 |
| No | Not currently served | 19,280 |

### 2.6 Service Flags

| Column | Values | Definition |
|--------|--------|------------|
| `Integrated_Flag` | Yes/No | Facility receives both PCP and MH services |
| `PCP_Flag` | Yes/No | Facility receives PCP services only |
| `MH_Flag` | Yes/No | Facility receives MH services only |

**Service Configuration Rules:**
- Integrated_Flag = Yes → PCP_Flag = Yes AND MH_Flag = Yes
- PCP_Flag = Yes, MH_Flag = No → PCP-only facility
- MH_Flag = Yes, PCP_Flag = No → MH-only facility
- All flags = No → Not served

**NULL Handling:** Service flag NULL values should be treated as 'No' for business logic purposes.

### 2.7 Barrier System

**Column to Use:** `Barrier_Category` (or equivalent barrier indicator)

**V18.7 Barrier Count:** 848 facilities

**Barrier Impact on Revenue:**
- Current Revenue: **NEVER affected** (preserves existing business)
- Integration Revenue: **$0** (blocked)
- New Business Revenue: **$0** (blocked)
- Total Potential Revenue: **$0** (blocked)

**Propagation Rule:** If one facility under a corporate entity has a barrier, all facilities under that entity should have the same barrier applied.

---

## 3. Fee Structure - AUTHORITATIVE VALUES

### 3.1 Base Service Fees

| Service | SNF | ALF |
|---------|-----|-----|
| PCP | $3,078.00 | $2,084.00 |
| MH | $1,211.00 | $1,431.00 |
| CCM | $360.00 | $360.00 |
| SS | $4,800.00 | $4,800.00 |

### 3.2 Permanent Adjusters

| Service | Adjuster | Calculation |
|---------|----------|-------------|
| PCP | 1.00 | No adjustment |
| MH | 0.50 | Base × 0.50 |
| CCM | 0.30 | Base × 0.30 |
| SS | 0.165 | Base × 0.50 × 0.33 |

### 3.3 Adjusted Service Fees

| Service | SNF Calculation | SNF Result | ALF Calculation | ALF Result |
|---------|-----------------|------------|-----------------|------------|
| PCP | $3,078.00 × 1.00 | $3,078.00 | $2,084.00 × 1.00 | $2,084.00 |
| MH | $1,211.00 × 0.50 | $605.50 | $1,431.00 × 0.50 | $715.50 |
| CCM | $360.00 × 0.30 | $108.00 | $360.00 × 0.30 | $108.00 |
| SS | $4,800.00 × 0.165 | $792.00 | $4,800.00 × 0.165 | $792.00 |
| **TOTAL** | | **$4,583.50** | | **$3,699.50** |

---

## 4. Scenario Calculation Methodology

### 4.1 Governing Principles

**No Double Counting:** Each service component (PCP, MH, CCM, SS) can only be counted once per facility. If a service is included in Current Revenue, it cannot also appear in Integration Revenue.

**Adjusted Values:** Throughout this section, (adj) indicates the service fee with permanent adjusters applied (see Section 3.2).

**TOTAL:** The sum of all adjusted service fees: PCP + MH(adj) + CCM(adj) + SS(adj)

**Revenue Types:**
- **Current Revenue:** Revenue from facilities we currently serve. NEVER affected by barriers.
- **Integration Revenue:** Remaining services that could be added to current customers.
- **New Business Revenue:** Potential revenue from facilities we do not currently serve.

### 4.2 Service Package Definitions by Scenario

**CRITICAL:** Scenarios differ by SERVICE PACKAGES, NOT by fee multipliers. The fee amounts are identical across scenarios. What differs is which services are included in each service type.

| Service Type | Scenario 1 (Baseline) | Scenario 2 (PCP Enhanced) | Scenario 3 (Comprehensive) |
|--------------|----------------------|---------------------------|----------------------------|
| PCP Only | PCP | PCP + CCM(adj) + SS(adj) | PCP + CCM(adj) + SS(adj) |
| MH Only | MH(adj) | MH(adj) | MH(adj) + CCM(adj) |
| Integrated | PCP + MH(adj) + CCM(adj) + SS(adj) | PCP + MH(adj) + CCM(adj) + SS(adj) | PCP + MH(adj) + CCM(adj) + SS(adj) |

### 4.3 Current Revenue Formulas

| Service Type | Scenario 1 | Scenario 2 | Scenario 3 |
|--------------|------------|------------|------------|
| PCP Only | Census × PCP | Census × (PCP + CCM(adj) + SS(adj)) | Census × (PCP + CCM(adj) + SS(adj)) |
| MH Only | Census × MH(adj) | Census × MH(adj) | Census × (MH(adj) + CCM(adj)) |
| Integrated | Census × TOTAL | Census × TOTAL | Census × TOTAL |

### 4.4 Integration Revenue Formulas

| Service Type | Scenario 1 | Scenario 2 | Scenario 3 |
|--------------|------------|------------|------------|
| PCP Only | Census × (MH(adj) + CCM(adj) + SS(adj)) | Census × MH(adj) | Census × MH(adj) |
| MH Only | Census × (PCP + CCM(adj) + SS(adj)) | Census × (PCP + CCM(adj) + SS(adj)) | Census × (PCP + SS(adj)) |
| Integrated | $0 | $0 | $0 |
| With Barrier | $0 | $0 | $0 |

### 4.5 New Business Revenue

New Business Revenue represents potential revenue from facilities we do not currently serve. New customers always receive the full integrated package.

**Formula (All Scenarios):** Census × TOTAL

| Condition | Result |
|-----------|--------|
| Not Served, No Barrier | Census × TOTAL |
| Not Served, Has Barrier | $0 |
| Served | $0 |

**CRITICAL:** New Business Revenue is IDENTICAL across all three scenarios because new customers always receive the full integrated package at the same fee rates.

### 4.6 Total Potential Revenue

**Formula:** Integration Revenue + New Business Revenue

**Note:** Does NOT include Current Revenue.

### 4.7 Scenario Behavior Patterns

| Behavior | S1 → S2 → S3 |
|----------|--------------|
| Current Revenue | Increases |
| Integration Revenue | Decreases |
| New Business Revenue | **Unchanged** |
| Total Potential | Decreases (Integration decrease > 0) |

**Key Insight:** As service packages are enhanced (S1→S3), current customer value increases but integration opportunity decreases proportionally. New Business remains constant.

---

## 5. V19.1 Established Baselines

### 5.1 Database Metrics

| Metric | V19.1 Value |
|--------|-------------|
| Total Facilities | 20,943 |
| SNF Facilities | 15,244 |
| ALF Facilities | 5,699 |
| Facilities We Serve | 1,663 |
| Corporate Facilities | 12,053 |
| Independent Facilities | 8,890 |
| Corporate Chains | 1,026 |
| Barrier Facilities | 848 |

### 5.2 Scenario 1 Revenue (Baseline Service Packages)

| Metric | Value |
|--------|-------|
| Current Revenue | $172.1M |
| Integration Revenue | $154.3M |
| New Business Revenue | $6,915.6M |
| **Total Potential** | **$7,069.9M** |

### 5.3 Scenario 2 Revenue (PCP Enhanced)

| Metric | Value |
|--------|-------|
| Current Revenue | $182.4M |
| Integration Revenue | $144.9M |
| New Business Revenue | $6,915.6M |
| **Total Potential** | **$7,060.6M** |

### 5.4 Scenario 3 Revenue (Comprehensive)

| Metric | Value |
|--------|-------|
| Current Revenue | $187.7M |
| Integration Revenue | $140.6M |
| New Business Revenue | $6,915.6M |
| **Total Potential** | **$7,056.3M** |

### 5.5 Pattern Verification

✅ New Business Revenue: IDENTICAL across scenarios ($6,915.6M)  
✅ Integration Revenue: DECREASES S1→S2→S3 ($154.3M → $144.9M → $140.6M)  
✅ Current Revenue: INCREASES S1→S2→S3 ($172.1M → $182.4M → $187.7M)  
✅ Total Potential: DECREASES S1→S2→S3 ($7,069.9M → $7,060.6M → $7,056.3M)

---

## 6. Core QC Validation Protocol

**MANDATORY: Complete this protocol before any Report Compendium work begins.**

### 6.1 Pre-Validation Checklist

| Check | Criteria | Status |
|-------|----------|--------|
| Database file present | Combined_Database_FINAL_V18.7.xlsx exists | ☐ |
| Scenario files present | All 3 scenario files exist with matching version | ☐ |
| Fee Schedule present | Fee_Schedule_Reference_Vxx.xlsx exists | ☐ |
| Version consistency | All files share same major version number | ☐ |

### 6.2 Database Validation

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| Total Facilities | 20,943 | _____ | ☐ |
| SNF Count | 15,244 | _____ | ☐ |
| ALF Count | 5,699 | _____ | ☐ |
| Served Facilities | 1,663 | _____ | ☐ |
| Barrier Facilities | 848 | _____ | ☐ |
| SNF + ALF = Total | True | _____ | ☐ |
| Served + Not Served = Total | True | _____ | ☐ |

### 6.3 Fee Structure Validation

| Fee Component | Expected | Actual | Pass/Fail |
|---------------|----------|--------|-----------|
| SNF PCP | $3,078.00 | _____ | ☐ |
| SNF MH (adj) | $605.50 | _____ | ☐ |
| SNF CCM (adj) | $108.00 | _____ | ☐ |
| SNF SS (adj) | $792.00 | _____ | ☐ |
| SNF TOTAL | $4,583.50 | _____ | ☐ |
| ALF PCP | $2,084.00 | _____ | ☐ |
| ALF MH (adj) | $715.50 | _____ | ☐ |
| ALF CCM (adj) | $108.00 | _____ | ☐ |
| ALF SS (adj) | $792.00 | _____ | ☐ |
| ALF TOTAL | $3,699.50 | _____ | ☐ |

### 6.4 Scenario Calculation Validation

**Scenario Pattern Check:**

| Pattern | Expected | Actual | Pass/Fail |
|---------|----------|--------|-----------|
| S1 New Biz = S2 New Biz | True | _____ | ☐ |
| S2 New Biz = S3 New Biz | True | _____ | ☐ |
| S1 Current < S2 Current | True | _____ | ☐ |
| S2 Current < S3 Current | True | _____ | ☐ |
| S1 Integration > S2 Integration | True | _____ | ☐ |
| S2 Integration > S3 Integration | True | _____ | ☐ |

**Scenario 1 Revenue Check:**

| Metric | Expected | Tolerance | Actual | Pass/Fail |
|--------|----------|-----------|--------|-----------|
| Current Revenue | $172.1M | ±$1M | _____ | ☐ |
| Integration Revenue | $154.3M | ±$1M | _____ | ☐ |
| New Business Revenue | $6,915.6M | ±$10M | _____ | ☐ |
| Total Potential | $7,069.9M | ±$10M | _____ | ☐ |

### 6.5 Barrier Logic Validation

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| Barrier facilities with $0 Integration | 848 | _____ | ☐ |
| Barrier facilities with $0 New Business | 848 | _____ | ☐ |
| Served facilities with barriers retain Current Revenue | True | _____ | ☐ |

### 6.6 Sign-Off Criteria

**All checks must pass before proceeding to Report Compendium work.**

| Gate | Requirement | Status |
|------|-------------|--------|
| Database Gate | All Section 6.2 checks pass | ☐ |
| Fee Gate | All Section 6.3 checks pass | ☐ |
| Scenario Gate | All Section 6.4 checks pass | ☐ |
| Barrier Gate | All Section 6.5 checks pass | ☐ |

**Sign-Off:**

- Validated By: _________________
- Date: _________________
- Version: V19.1
- Ready for Report Generation: ☐ Yes ☐ No

---

## 7. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| **V19.1** | Nov 2025 | Restructured to Core Rulebook with embedded QC; V18.7 database (20,943 facilities); corrected scenario methodology (service packages not fee multipliers) |
| V19.0 | Nov 2025 | Initial V18.7 integration, scenario calculation error (fee multipliers - corrected in V19.1) |
| V18.7 | Nov 2025 | PowerBI reconciliation + strategic barrier removals (-80 facilities, -535 barriers) |
| V18.0 | Nov 2025 | V17.1 database (21,023 facilities), updated fee structure |
| V15.0 | Nov 2025 | TAM/SAM/SOM methodology refined |

---

**END OF CORE RULEBOOK**

*This document is the authoritative reference for database, fee structure, and scenario calculations. Report-specific methodology is documented in separate Report Compendiums.*

*Deviations require written authorization.*
