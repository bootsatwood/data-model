# Comprehensive Report Workbook Style Guide
## Formatting Standards for Economic Model Reports

**Version**: 1.0  
**Date**: November 22, 2025  
**Status**: PRODUCTION STANDARD

---

## Executive Summary

This style guide defines mandatory formatting standards for the Comprehensive Report Workbook. These standards ensure professional presentation, consistent formatting across versions, and eliminate manual adjustments by users.

**Key Principle**: Precision in formatting is as important as accuracy in data.

---

## 1. Number Formatting Standards

### 1.1 Revenue Formatting

**Critical Rule**: Use abbreviated notation for millions and billions

| Value Range | Format | Example |
|------------|--------|---------|
| Under $1M | Full dollars with commas | $346,229 |
| $1M - $999M | Millions with MM | $173.1MM |
| $1B and above | Billions with B | $7.68B |

**Decimal Precision**: Maximum 1 decimal place (tenth)
- ✅ Correct: $173.1MM, $7.7B
- ❌ Wrong: $173.14MM, $7.683B

### 1.2 Ranges

**Format**: "Value1 - Value2" with consistent notation
- Same notation on both sides: "$95.3MM - $101.7MM"
- Not mixed: Never "$95.3MM - $1.02B"

### 1.3 Facility Counts

**Format**: Always use comma separators
- Single count: "1,743"
- With share: "12,053 / 1,355"

### 1.4 Percentages

**Format**: One decimal place with % symbol
- Example: "60.3%"
- Never: "60.34%" or "60%"

---

## 2. Column Width Specifications

### Critical Implementation Rule

**Set column widths IMMEDIATELY after creating sheet, BEFORE adding any data**

```python
# CORRECT - Set widths first
ws = wb.create_sheet("Sheet Name")
ws.column_dimensions['A'].width = 10.0
ws.column_dimensions['B'].width = 18.0
# Then add data...

# WRONG - Setting widths after data
ws = wb.create_sheet("Sheet Name")
# Add data first...
ws.column_dimensions['A'].width = 10.0  # Too late!
```

### Sheet-Specific Widths

| Sheet | Columns | Widths |
|-------|---------|--------|
| **TAM SAM SOM Facilities** | A / B / C / D | 10 / 18 / 18 / 18 |
| **TAM SAM SOM Revenue** | A / B / C / D / E | 8 / 16 / 16 / 16 / 16 |
| **Fee Structure SOM** | A / B-H | 10 / 12,7 alternating |
| **Top Corporate Rankings** | A / B / C-D / E-H | 6 / 35 / 12 / 15 |
| **State Analysis** | A / B / C-D / E / F-H | 12 / 25 / 12 / 15 / 18 |

---

## 3. Font Specifications

### Universal Standards

| Element | Font | Size | Bold | Application |
|---------|------|------|------|-------------|
| Table Titles | Calibri | 10 | **Yes** | First row of each table |
| Headers | Calibri | 10 | No | Column headers |
| Data | Calibri | 10 | No | All data cells |
| TOTAL rows | Calibri | 10 | **Yes** | Summary rows only |

### Implementation

```python
from openpyxl.styles import Font

# Table titles
cell.font = Font(bold=True, size=10)

# Data cells (or leave default)
cell.font = Font(size=10)
```

---

## 4. Alignment Standards

### Universal Rule

**ALL data cells must be center-aligned**

### Exceptions

- Table titles: Left-aligned (default)
- Subtitle rows: Left-aligned

### Implementation

```python
from openpyxl.styles import Alignment

# For all data cells
cell.alignment = Alignment(horizontal='center')
```

---

## 5. Table Structure Standards

### 5.1 Spacing Between Tables

**Standard**: 2 blank rows between tables

### 5.2 Table Components

```
Row N:   Table Title (Bold, Left-aligned)
Row N+1: Headers Level 1 (Center-aligned)
Row N+2: Headers Level 2 if needed (Center-aligned)
Row N+3+: Data rows (All center-aligned)
```

### 5.3 Specific Table Requirements

#### Tables 1-3: Facility Counts
- Format: "Total / Our Share"
- Example: "12,053 / 1,355"

#### Tables 4-9: Revenue
- Single values use Scenario 2
- Ranges show S1 - S3

#### Tables 22-24: State Ranges
- **MUST be populated** (common error: leaving empty)
- Individual rows for Existing states
- Combined rows for other markets

---

## 6. Quality Control Checklist

### Before Delivery

- [ ] All revenue values use MM/B notation
- [ ] No more than 1 decimal place anywhere
- [ ] Facility counts have comma separators
- [ ] Column widths match specification exactly
- [ ] All data cells are center-aligned
- [ ] Table titles are bold
- [ ] Tables 22-24 contain data
- [ ] No #REF! or #VALUE! errors

### Verification Script

```python
def verify_formatting(wb):
    issues = []
    
    # Check column widths
    for sheet_name, expected_widths in SHEET_WIDTHS.items():
        ws = wb[sheet_name]
        for col, width in expected_widths.items():
            actual = ws.column_dimensions[col].width
            if actual != width:
                issues.append(f"{sheet_name} Col {col}: Expected {width}, Got {actual}")
    
    # Check for empty tables 22-24
    ws_state = wb['State Analysis']
    if not has_data_in_tables_22_24(ws_state):
        issues.append("Tables 22-24 are empty")
    
    return issues
```

---

## 7. Common Errors and Prevention

### Error 1: Wrong Number Format

**Issue**: Using full dollar amounts instead of MM/B
- Wrong: "$7,683,431,134"
- Right: "$7.7B"

**Prevention**: Always use format_revenue() function

### Error 2: Missing Commas in Counts

**Issue**: Facility counts without separators
- Wrong: "12053 / 1355"
- Right: "12,053 / 1,355"

**Prevention**: Use f"{value:,}" formatting

### Error 3: Tables 22-24 Empty

**Issue**: State range tables not populated

**Prevention**: Ensure state iteration logic runs for all scenarios

### Error 4: Inconsistent Alignment

**Issue**: Some cells left-aligned, others centered

**Prevention**: Apply center alignment systematically to all data cells

---

## 8. Version-Specific Notes

### V18.4 Updates

- Implemented MM/B notation throughout
- Fixed comma formatting in Tables 1-3
- Populated Tables 22-24 with state ranges
- Applied consistent center alignment
- Limited all values to 1 decimal place

### Future Versions

When creating V19 or later:
1. Start with this style guide
2. Use V18.4 as formatting reference
3. Verify against checklist before delivery

---

## 9. Implementation Template

```python
def format_revenue(value):
    """Standard revenue formatter with MM/B notation"""
    if pd.isna(value) or value == 0:
        return "$-"
    
    if value >= 1_000_000_000:  # Billions
        return f"${value/1_000_000_000:.1f}B"
    elif value >= 1_000_000:  # Millions
        return f"${value/1_000_000:.1f}MM"
    else:  # Under 1M
        return f"${value:,.0f}"

def format_revenue_range(val1, val2):
    """Format range with consistent notation"""
    return f"{format_revenue(val1)} - {format_revenue(val2)}"

def format_facility_count(total, served):
    """Format facility count with commas"""
    return f"{total:,} / {served:,}"
```

---

## 10. Final Mandate

**This style guide is MANDATORY for all Comprehensive Report Workbook generation.**

Key commitments:
1. Column widths must be exact
2. Number formats must follow standards
3. All data cells must be centered
4. Tables 22-24 must contain data
5. User should NEVER need to adjust formatting

**Quality Standard**: If the user has to manually adjust any formatting element, the delivery has failed.

---

**END OF STYLE GUIDE**

*This document supersedes formatting instructions in the rulebook. Use this as the primary reference for all formatting requirements.*
