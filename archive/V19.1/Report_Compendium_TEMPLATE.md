# [Report Name] Compendium Template
## [Brief Description]

**Version**: X.X  
**Date**: [Month Year]  
**Status**: [DRAFT / IN REVIEW / PRODUCTION READY]  
**Prerequisite**: Core Rulebook VX.X QC Protocol must pass before using this compendium

---

## Document Purpose

[Describe what this report produces, who uses it, and what business questions it answers]

**Source Data:** [Which scenario files? Which database version?]  
**Primary Output:** [Output filename pattern]

---

## 1. Report Overview

### 1.1 Business Context

[Why does this report exist? What decision does it support?]

### 1.2 Audience

[Who receives this report? What do they do with it?]

### 1.3 Frequency

[One-time? Quarterly? On-demand?]

### 1.4 Dependencies

| Dependency | Version Required | Purpose |
|------------|------------------|---------|
| Core Rulebook | VX.X+ | Database and scenario validation |
| Combined Database | VX.X | Source facility data |
| Scenario Files | VX.X | Revenue calculations |
| [Other] | [Version] | [Purpose] |

---

## 2. Filter Definitions

### 2.1 Geographic Filters

[Document any geographic filtering - states, metros, regions]

| Filter Name | Definition | Included Values |
|-------------|------------|-----------------|
| [Filter 1] | [Description] | [Values] |
| [Filter 2] | [Description] | [Values] |

### 2.2 Facility Filters

[Document facility-level filtering]

| Filter Name | Column | Criteria |
|-------------|--------|----------|
| [Filter 1] | [Column name] | [Logic] |
| [Filter 2] | [Column name] | [Logic] |

### 2.3 Ownership Filters

| Analysis Type | Corporate | Independent |
|---------------|-----------|-------------|
| [Analysis 1] | [Include/Exclude] | [Include/Exclude] |
| [Analysis 2] | [Include/Exclude] | [Include/Exclude] |

### 2.4 Barrier Treatment

[How are barriers handled in this report?]

| Barrier Scenario | Treatment |
|------------------|-----------|
| Has Barrier | [Include/Exclude/Flag] |
| No Barrier | [Include] |

---

## 3. Output Specifications

### 3.1 Output Structure

[Describe the structure of the output file - sheets, sections, tables]

| Sheet/Section | Content | Row Count |
|---------------|---------|-----------|
| [Sheet 1] | [Description] | [Expected rows] |
| [Sheet 2] | [Description] | [Expected rows] |

### 3.2 Column Definitions

[Define each column in the output]

| Column | Data Type | Source | Calculation |
|--------|-----------|--------|-------------|
| [Column A] | [Text/Number/Currency] | [Source column] | [Formula if calculated] |
| [Column B] | [Text/Number/Currency] | [Source column] | [Formula if calculated] |

### 3.3 Formatting Standards

| Element | Format |
|---------|--------|
| Currency | $X,XXX,XXX or $X.XM (state which) |
| Percentages | X.X% |
| Counts | X,XXX |
| Dates | [Format] |

### 3.4 Sort Order

[How should output be sorted?]

| Level | Column | Direction |
|-------|--------|-----------|
| Primary | [Column] | [Asc/Desc] |
| Secondary | [Column] | [Asc/Desc] |

---

## 4. Methodology

### 4.1 Data Extraction

[Step-by-step process for extracting source data]

1. [Step 1]
2. [Step 2]
3. [Step 3]

### 4.2 Calculations

[Document any calculations specific to this report]

**[Calculation Name]:**
```
Formula: [Formula]
Example: [Worked example]
```

### 4.3 Aggregation Rules

[How is data aggregated?]

| Metric | Aggregation Method |
|--------|-------------------|
| [Metric 1] | [SUM/COUNT/AVG/etc.] |
| [Metric 2] | [SUM/COUNT/AVG/etc.] |

### 4.4 Edge Cases

[Document known edge cases and how to handle them]

| Scenario | Handling |
|----------|----------|
| [Edge case 1] | [How to handle] |
| [Edge case 2] | [How to handle] |

---

## 5. Report QC Validation Protocol

**PREREQUISITE:** Core Rulebook VX.X QC Protocol must pass before running this protocol.

### 5.1 Pre-Validation Checklist

| Check | Criteria | Status |
|-------|----------|--------|
| Core QC Passed | Core Rulebook Section 6 sign-off complete | ☐ |
| Source data available | [Required files] accessible | ☐ |
| Output file generated | [Output filename] exists | ☐ |

### 5.2 Row Count Validation

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| [Sheet 1] row count | [Expected] | _____ | ☐ |
| [Sheet 2] row count | [Expected] | _____ | ☐ |

### 5.3 Sum Validation

| Check | Expected | Tolerance | Actual | Pass/Fail |
|-------|----------|-----------|--------|-----------|
| Total [Metric 1] | [Value] | ±[X]% | _____ | ☐ |
| Total [Metric 2] | [Value] | ±[X]% | _____ | ☐ |

### 5.4 Reconciliation to Source

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| Report total = Scenario total (filtered) | True | _____ | ☐ |
| Facility count matches filter criteria | True | _____ | ☐ |

### 5.5 Business Logic Validation

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| [Business rule 1] | [Expected result] | _____ | ☐ |
| [Business rule 2] | [Expected result] | _____ | ☐ |

### 5.6 Sign-Off Criteria

**All checks must pass before report delivery.**

| Gate | Requirement | Status |
|------|-------------|--------|
| Count Gate | All Section 5.2 checks pass | ☐ |
| Sum Gate | All Section 5.3 checks pass | ☐ |
| Reconciliation Gate | All Section 5.4 checks pass | ☐ |
| Logic Gate | All Section 5.5 checks pass | ☐ |

**Sign-Off:**

- Validated By: _________________
- Date: _________________
- Version: X.X
- Report Ready for Delivery: ☐ Yes ☐ No

---

## 6. Usage Notes

### 6.1 Common Modifications

[Document common customizations users might request]

| Modification | How to Implement |
|--------------|------------------|
| [Modification 1] | [Instructions] |
| [Modification 2] | [Instructions] |

### 6.2 Known Limitations

[Document what this report cannot do or known issues]

1. [Limitation 1]
2. [Limitation 2]

### 6.3 Related Reports

[Link to other report compendiums that might be relevant]

| Report | Relationship |
|--------|--------------|
| [Report Name] | [How they relate] |

---

## 7. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| X.X | [Date] | [Description] |

---

**END OF [REPORT NAME] COMPENDIUM**

*This compendium documents [Report Name]. For database, fee structure, and scenario methodology, see Core Rulebook VX.X.*

*Deviations require written authorization.*
