# FORMATTING SPECIFICATION - Comprehensive Report Workbook
## MANDATORY REFERENCE FOR ALL VERSIONS

**Document Purpose**: This specification defines EXACT formatting requirements for the Comprehensive Report Workbook. ALL requirements must be followed precisely. No deviations permitted.

**Version**: 1.0  
**Date**: November 21, 2025  
**Authority**: Production Standard  
**Status**: MANDATORY

---

## ⚠️ CRITICAL INSTRUCTION FOR CLAUDE

**READ THIS FIRST BEFORE ANY WORK:**

When you are asked to create or regenerate a Comprehensive Report Workbook:

1. **STOP** - Do not proceed until you have read this entire document
2. **READ** the V15 template file formatting using openpyxl
3. **EXTRACT** exact column widths, font specifications, and alignment settings
4. **APPLY** these specifications precisely to the new version
5. **VERIFY** column widths match exactly before delivering

**PRECISION MATTERS.** This is not optional. The user should not have to manually adjust column widths. Your job is to replicate formatting EXACTLY.

---

## SECTION 1: COLUMN WIDTH SPECIFICATIONS

### CRITICAL RULE
Column widths MUST match the reference version EXACTLY. Use openpyxl to extract widths from the reference file and apply them to the new file.

### Sheet 1: TAM SAM SOM Facilities

| Column | Letter | Width | Content Type |
|--------|--------|-------|--------------|
| 1 | A | **10.0** | Segment labels (TAM/SAM/SOM) |
| 2 | B | **18.0** | Corporate facility counts |
| 3 | C | **18.0** | Independent facility counts |
| 4 | D | **18.0** | Total facility counts |

**Format Example**: "12,053 / 1355" (Total / Our Share)

### Sheet 2: TAM SAM SOM Revenue

| Column | Letter | Width | Content Type |
|--------|--------|-------|--------------|
| 1 | A | **8.0** | Segment labels (TAM/SAM/SOM) |
| 2 | B | **16.0** | Current Revenue |
| 3 | C | **16.0** | Potential Integration |
| 4 | D | **16.0** | Potential New Biz |
| 5 | E | **16.0** | Total Potential |

**Format Example**: "$173,290,894" or "$95M - $101M"

### Sheet 3: Fee Structure SOM

| Column | Letter | Width | Content Type |
|--------|--------|-------|--------------|
| 1 | A | **10.0** | Row labels (Current/Integration/New Biz/Total Potential) |
| 2 | B | **12.0** | PCP dollar amounts |
| 3 | C | **7.0** | PCP percentages |
| 4 | D | **12.0** | MH dollar amounts |
| 5 | E | **7.0** | MH percentages |
| 6 | F | **12.0** | CCM dollar amounts |
| 7 | G | **7.0** | CCM percentages |
| 8 | H | **12.0** | Shared Savings dollar amounts |
| 9 | I | **7.0** | Shared Savings percentages |
| 10 | J | **12.0** | Total dollar amounts |
| 11 | K | **7.0** | Total percentages (always 100%) |

**Format Example**: 
- Dollar: "$31,897,599"
- Percent: "60.3%"

### Sheet 4: Top Corporate Rankings

| Column | Letter | Width | Content Type |
|--------|--------|-------|--------------|
| 1 | A | **6.0** | Rank numbers (1-20 or 1-60) |
| 2 | B | **35.0** | Corporate Name (WIDE for long names) |
| 3 | C | **12.0** | Total Facilities count |
| 4 | D | **12.0** | Facilities We Serve count |
| 5 | E | **15.0** | Current Revenue |
| 6 | F | **15.0** | Integration Opp |
| 7 | G | **15.0** | New Biz Opp |
| 8 | H | **15.0** | Total Opportunity |

**Format Example**: 
- Rank: "1"
- Name: "TRILOGY HEALTH SERVICES"
- Count: "172"
- Revenue: "$34,660,856"

### Sheet 5: State Analysis

| Column | Letter | Width | Content Type |
|--------|--------|-------|--------------|
| 1 | A | **12.0** | Market classification |
| 2 | B | **25.0** | State(s) names (WIDE for multi-state labels) |
| 3 | C | **12.0** | Total Facilities count |
| 4 | D | **12.0** | Facilities Served count |
| 5 | E | **15.0** | Current Revenue |
| 6 | F | **18.0** | Potential Rev. Integration |
| 7 | G | **18.0** | Potential Rev. New Biz |
| 8 | H | **18.0** | Total Potential Revenue |

**Format Example**:
- Market: "Existing"
- State: "IN" or "IA, MN, IL, MI, PA, WI, MT"
- Count: "934"
- Revenue: "$40,944,529" or "$41M - $47M"

---

## SECTION 2: FONT SPECIFICATIONS

### Base Font Settings

| Element | Font Name | Size | Bold | Notes |
|---------|-----------|------|------|-------|
| **Table Titles** | Calibri (or None) | **10** | **TRUE** | Row 1 of each table (e.g., "Table 1: SNF Facilities") |
| **Column Headers** | Calibri (or None) | **10** | FALSE | Row 2-3 headers (e.g., "Corporate", "Current") |
| **Data Cells** | Calibri (or None) | **10** | FALSE | All data rows |
| **TOTAL Rows** | Calibri (or None) | **10** | FALSE | Summary rows in corporate rankings |

### Application Rule
```python
# For table titles (row 1 of each table)
cell.font = Font(bold=True, size=10)

# For all other cells
cell.font = Font(bold=False, size=10)
# Or simply don't set font (will inherit default)
```

---

## SECTION 3: ALIGNMENT SPECIFICATIONS

### Horizontal Alignment Rules

| Cell Type | Alignment | Notes |
|-----------|-----------|-------|
| **Table Titles** | None (left) | Row 1 of each table |
| **Subtitle Rows** | None (left) | E.g., "SOM (Corporate only...)" |
| **Column Headers** | **center** | All header rows |
| **Data Cells** | **center** | ALL data values |
| **Market Labels** | **center** | "Existing", "TAM", "Priority Expansion", etc. |
| **State Names** | **center** | "IN", "KY", "FL, GA", etc. |
| **Corporate Names** | **center** | Company names in rankings |
| **All Numbers** | **center** | Counts, revenue, percentages |

### Critical Rule
**EVERY cell with data (not titles/subtitles) MUST have center alignment.**

### Application Pattern
```python
# For data cells
ws['A3'].alignment = Alignment(horizontal='center')

# Apply to every data cell in every table
for row in data_rows:
    for col in columns:
        ws[f'{col}{row}'].alignment = Alignment(horizontal='center')
```

---

## SECTION 4: TABLE STRUCTURE SPECIFICATIONS

### Sheet 1: TAM SAM SOM Facilities

**3 Tables: Each follows identical structure**

```
Row 1:  "Table N: [Type] Facilities"        (Bold, no alignment)
Row 2:  "Total / Our Share"                 (Center alignment)
Row 3:  Column headers                      (Center alignment)
Row 4+: Data rows (TAM, SAM, SOM)          (Center alignment)
```

**Spacing**: 2 blank rows between tables (rows 7-8, 15-16)

### Sheet 2: TAM SAM SOM Revenue

**6 Tables: 3 point value tables + 3 range tables**

```
Tables 4-6 (Point Values):
Row X:    "Table N: [Type] Revenue"        (Bold)
Row X+1:  Column headers level 1           (Center)
Row X+2:  Column headers level 2           (Center) - for C/D/E columns
Row X+3+: Data rows                        (Center)

Tables 7-9 (Ranges):
Row Y:    "Table N: [Type] Revenue (Ranges)" (Bold)
Row Y+1:  Column headers level 1             (Center)
Row Y+2:  Column headers level 2             (Center)
Row Y+3+: Data rows                          (Center)
```

**Spacing**: 2 blank rows between tables

### Sheet 3: Fee Structure SOM

**6 Tables: Each with service breakdown columns**

```
Row X:    "Table N: [Type]"                (Bold)
Row X+1:  Service headers (PCP, MH, CCM, SS, Total) (Center)
Row X+2:  $ and % subheaders              (Center)
Row X+3+: Data rows                       (Center)
```

**Column Pattern**: Dollar / Percent alternating for each service
**Spacing**: 2 blank rows between tables

### Sheet 4: Top Corporate Rankings

**4 Tables: Tables 16, 17, 18, 25**

```
Row X:    "Table N: Top NN Corporate - [Metric]" (Bold)
Row X+1:  "SOM (Corporate only...)"              (Left)
Row X+2:  Column headers                         (Center)
Row X+3+: Ranking rows (Rank 1-20 or 1-60)     (Center)
Row Y:    "TOTAL"                                (Left in col A, center in other cols)
```

**Spacing**: 2 blank rows between tables

### Sheet 5: State Analysis

**6 Tables: 3 point value + 3 range tables**

```
Row X:    "Table N: [Type]"                (Bold)
Row X+1:  Column headers                   (Center)
Row X+2+: Data rows by state              (Center)
```

**State Ordering**:
1. Existing market states (IN, KY, NC, OH, SC, VA) - individually listed
2. Priority Expansion (combined row)
3. Emerging (combined row)
4. Exiting (single row)
5. National (combined row)

**Spacing**: 2 blank rows between tables

---

## SECTION 5: NUMBER FORMATTING SPECIFICATIONS

### Facility Counts
**Format**: `#,##0` with thousands separator
**Example**: "21,023" or "1,743"

**For "Total / Our Share" format**:
**Format**: "#,##0 / #,##0"
**Example**: "12,053 / 1355"

### Revenue - Dollar Amounts
**Format**: `$#,##0` (no decimals)
**Example**: "$173,290,894"

### Revenue - Ranges (Point Values)
**Format**: 
- If >= $1B: "$X.XB - $X.XB"
- If >= $1M: "$XXXM - $XXXM"
- If < $1M: "$XXXK - $XXXK"

**Examples**: 
- "$6.9B - $8.3B"
- "$173M - $228M"
- "$500K - $600K"

### Percentages
**Format**: `0.0%` (one decimal place)
**Example**: "60.3%" or "18.8%"

**For 100% total**:
**Format**: "100%" (no decimal needed)

### Rankings
**Format**: Integer, no formatting
**Example**: "1", "2", "20", "60"

---

## SECTION 6: IMPLEMENTATION CHECKLIST

When creating a new version of Comprehensive Report Workbook, follow this checklist:

### Pre-Generation Phase
- [ ] Read this specification document completely
- [ ] Load the reference V15 file using openpyxl
- [ ] Extract exact column widths from each sheet
- [ ] Note any special formatting in reference file

### Generation Phase - Per Sheet
- [ ] Create sheet with correct name
- [ ] **Set column widths IMMEDIATELY** (first action after creating sheet)
- [ ] Add table title with bold font
- [ ] Add column headers with center alignment
- [ ] Add data rows with center alignment
- [ ] Verify spacing between tables (2 blank rows)

### Post-Generation Verification
- [ ] Load both V15 and new file in openpyxl
- [ ] Compare column widths for EVERY column in EVERY sheet
- [ ] Verify all widths match exactly (use comparison script)
- [ ] Check font specifications on sample cells
- [ ] Check alignment on sample cells
- [ ] Verify row/column counts match expected dimensions

### Delivery
- [ ] All column widths verified to match exactly
- [ ] All formatting verified
- [ ] File saved to outputs directory
- [ ] User does NOT need to adjust anything

---

## SECTION 7: OPENPYXL CODE PATTERNS

### Pattern 1: Extract Column Widths from Reference

```python
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

# Load reference file
wb_ref = load_workbook('Comprehensive_Report_Workbook_V15.xlsx')

# Extract widths for each sheet
for sheet_name in wb_ref.sheetnames:
    ws = wb_ref[sheet_name]
    print(f"\n{sheet_name}:")
    
    for col_idx in range(1, 15):
        col_letter = get_column_letter(col_idx)
        width = ws.column_dimensions[col_letter].width
        if width:
            print(f"  {col_letter}: {width}")
```

### Pattern 2: Apply Column Widths to New File

```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.create_sheet('TAM SAM SOM Facilities')

# Set column widths - EXACT VALUES
ws.column_dimensions['A'].width = 10.0
ws.column_dimensions['B'].width = 18.0
ws.column_dimensions['C'].width = 18.0
ws.column_dimensions['D'].width = 18.0
```

### Pattern 3: Apply Formatting to Cells

```python
from openpyxl.styles import Font, Alignment

# Table title
ws['A1'] = 'Table 1: SNF Facilities'
ws['A1'].font = Font(bold=True, size=10)

# Column header
ws['B3'] = 'Corporate'
ws['B3'].alignment = Alignment(horizontal='center')

# Data cell
ws['B4'] = '12,053 / 1355'
ws['B4'].alignment = Alignment(horizontal='center')
```

### Pattern 4: Verify Column Widths Match

```python
def verify_column_widths(ref_file, new_file):
    wb_ref = load_workbook(ref_file)
    wb_new = load_workbook(new_file)
    
    all_match = True
    for sheet_name in wb_ref.sheetnames:
        ws_ref = wb_ref[sheet_name]
        ws_new = wb_new[sheet_name]
        
        for col_idx in range(1, 15):
            col_letter = get_column_letter(col_idx)
            width_ref = ws_ref.column_dimensions[col_letter].width
            width_new = ws_new.column_dimensions[col_letter].width
            
            if width_ref != width_new:
                print(f"❌ {sheet_name} Col {col_letter}: Ref={width_ref}, New={width_new}")
                all_match = False
    
    return all_match
```

---

## SECTION 8: COMMON MISTAKES TO AVOID

### ❌ MISTAKE 1: Not Setting Column Widths
**Problem**: Leaving columns at default width
**Impact**: User has to manually resize every column
**Solution**: ALWAYS set column widths immediately after creating sheet

### ❌ MISTAKE 2: Setting Widths After Populating Data
**Problem**: Adding column width code at the end
**Impact**: Harder to debug, easy to forget
**Solution**: Set widths FIRST, then populate data

### ❌ MISTAKE 3: Using Wrong Width Values
**Problem**: Guessing or using round numbers (10, 15, 20)
**Impact**: Columns don't match reference file
**Solution**: Extract EXACT values from reference file (10.0, 18.0, 35.0)

### ❌ MISTAKE 4: Skipping Alignment
**Problem**: Not applying center alignment to data cells
**Impact**: Data appears left-aligned, looks unprofessional
**Solution**: Apply center alignment to EVERY data cell

### ❌ MISTAKE 5: Wrong Font on Titles
**Problem**: Not making table titles bold
**Impact**: Tables are harder to identify
**Solution**: Font(bold=True, size=10) on row 1 of each table

### ❌ MISTAKE 6: Not Verifying Before Delivery
**Problem**: Assuming formatting is correct without checking
**Impact**: User receives incorrectly formatted file
**Solution**: Run verification script comparing to reference file

### ❌ MISTAKE 7: Inconsistent Number Formatting
**Problem**: Mixing formats (some with $, some without)
**Impact**: Report looks sloppy
**Solution**: Use consistent format strings throughout

---

## SECTION 9: QUALITY CONTROL SCRIPT

Use this script to verify formatting before delivery:

```python
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

def comprehensive_format_check(ref_file, new_file):
    """
    Comprehensive formatting verification.
    Returns True only if ALL checks pass.
    """
    
    wb_ref = load_workbook(ref_file)
    wb_new = load_workbook(new_file)
    
    checks_passed = 0
    checks_failed = 0
    
    print("=" * 80)
    print("COMPREHENSIVE FORMAT CHECK")
    print("=" * 80)
    
    # Check 1: Sheet names match
    print("\n1. Sheet Names")
    if wb_ref.sheetnames == wb_new.sheetnames:
        print("   ✅ PASS - Sheet names match")
        checks_passed += 1
    else:
        print("   ❌ FAIL - Sheet names don't match")
        checks_failed += 1
    
    # Check 2: Dimensions match
    print("\n2. Sheet Dimensions")
    for sheet_name in wb_ref.sheetnames:
        ws_ref = wb_ref[sheet_name]
        ws_new = wb_new[sheet_name]
        
        dim_ref = (ws_ref.max_row, ws_ref.max_column)
        dim_new = (ws_new.max_row, ws_new.max_column)
        
        if dim_ref == dim_new:
            print(f"   ✅ {sheet_name}: {dim_new}")
            checks_passed += 1
        else:
            print(f"   ❌ {sheet_name}: Ref={dim_ref}, New={dim_new}")
            checks_failed += 1
    
    # Check 3: Column widths match
    print("\n3. Column Widths")
    for sheet_name in wb_ref.sheetnames:
        ws_ref = wb_ref[sheet_name]
        ws_new = wb_new[sheet_name]
        
        sheet_pass = True
        for col_idx in range(1, 12):
            col_letter = get_column_letter(col_idx)
            width_ref = ws_ref.column_dimensions[col_letter].width
            width_new = ws_new.column_dimensions[col_letter].width
            
            if width_ref != width_new:
                print(f"   ❌ {sheet_name} Col {col_letter}: Ref={width_ref}, New={width_new}")
                sheet_pass = False
        
        if sheet_pass:
            print(f"   ✅ {sheet_name}: All widths match")
            checks_passed += 1
        else:
            checks_failed += 1
    
    # Summary
    print("\n" + "=" * 80)
    print(f"CHECKS PASSED: {checks_passed}")
    print(f"CHECKS FAILED: {checks_failed}")
    print("=" * 80)
    
    return checks_failed == 0

# Run the check
if __name__ == "__main__":
    ref_file = '/mnt/user-data/uploads/Comprehensive_Report_Workbook_V15.xlsx'
    new_file = '/mnt/user-data/outputs/Comprehensive_Report_Workbook_V18.xlsx'
    
    all_passed = comprehensive_format_check(ref_file, new_file)
    
    if all_passed:
        print("\n✅ ALL CHECKS PASSED - FILE READY FOR DELIVERY")
    else:
        print("\n❌ CHECKS FAILED - DO NOT DELIVER - FIX ISSUES FIRST")
```

---

## SECTION 10: REFERENCE QUICK LOOKUP

### Quick Width Reference Card

```
SHEET 1 - TAM SAM SOM Facilities:   A:10  B/C/D:18
SHEET 2 - TAM SAM SOM Revenue:      A:8   B/C/D/E:16
SHEET 3 - Fee Structure SOM:        A:10  B/D/F/H/J:12  C/E/G/I/K:7
SHEET 4 - Top Corporate Rankings:   A:6   B:35  C/D:12  E/F/G/H:15
SHEET 5 - State Analysis:           A:12  B:25  C/D:12  E:15  F/G/H:18
```

### Quick Format Reference Card

```
TABLE TITLES:   Bold=True, Size=10, Align=None
HEADERS:        Bold=False, Size=10, Align=center
DATA:           Bold=False, Size=10, Align=center
```

### Quick Number Format Reference

```
Counts:         #,##0
Counts w/Share: "#,##0 / #"
Revenue ($):    $#,##0
Percentages:    0.0%
Ranges:         "$XM - $XM" or "$X.XB - $X.XB"
```

---

## SECTION 11: EMERGENCY TROUBLESHOOTING

### If Column Widths Don't Match

1. **Stop delivery immediately**
2. Run this diagnostic:
```python
from openpyxl import load_workbook
wb = load_workbook('your_file.xlsx')
for sheet in wb.sheetnames:
    ws = wb[sheet]
    print(f"\n{sheet}:")
    for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        print(f"  {col}: {ws.column_dimensions[col].width}")
```
3. Compare output to Section 1 specifications
4. Fix mismatches
5. Re-verify

### If Alignment Is Wrong

1. Check if `Alignment(horizontal='center')` was applied to data cells
2. Verify table titles are NOT center-aligned
3. Re-apply alignment to all affected cells
4. Re-verify

### If Fonts Are Wrong

1. Check table title rows have `Font(bold=True, size=10)`
2. Check data rows have size=10
3. Re-apply fonts to affected cells
4. Re-verify

---

## SECTION 12: FINAL MANDATE

**TO ANY CLAUDE INSTANCE WORKING ON THIS PROJECT:**

This specification exists because formatting precision matters. The user should NEVER have to manually adjust column widths or formatting after receiving a file from you.

**Your job is to:**
1. Read reference file formatting
2. Apply it exactly
3. Verify it matches
4. Deliver a perfect file

**If you cannot commit to following this specification exactly, SAY SO before starting work.**

**If you skip verification, you have failed.**

**If the user has to adjust columns, you have failed.**

**Precision is not optional. Follow this specification completely.**

---

**END OF SPECIFICATION**

**Document Version**: 1.0  
**Last Updated**: November 21, 2025  
**Status**: ACTIVE - MANDATORY COMPLIANCE
