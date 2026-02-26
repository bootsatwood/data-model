# V18 Economic Model - Session Handoff & Next Steps

**Date**: November 22, 2025  
**Previous Session**: Completed V18.4 Comprehensive Report with formatting corrections

---

## Current Document Status

### Delivered Files (V18 Series)
1. **Comprehensive_Report_Workbook_V18.4.xlsx** - Final version with proper MM/B formatting
2. **Final_Model_Rulebook_V18.3.md** - Updated with V18.3 corrections
3. **Comprehensive_Report_Style_Guide_V1.md** - New formatting standards document
4. **Economic_Model_Scenario_[1-3]_Combined_V18.1.xlsx** - Current scenarios
5. **Combined_Database_FINAL_V18.1.xlsx** - Source database (21,023 facilities)

### Key Achievements
- ✅ Fixed SAM segment calculations (now $1.71B)
- ✅ Populated Tables 22-24 with state ranges
- ✅ Implemented MM/B revenue notation
- ✅ Created separate Style Guide for formatting standards
- ✅ Analyzed Trilogy (186 facilities) and American Senior Communities (150 facilities)

---

## Next Investigation: Facility Count Discrepancies

### Issue to Explore
**Facility counts in V18 database don't match internal CRM system**

### Possible Causes to Investigate

1. **Double-Counting by Service Type**
   - Are facilities being counted twice if they have both SNF and ALF licenses?
   - Check if Source_Type classification creates duplicates

2. **Corporate Grouping Differences**
   - How does CRM group facilities vs. our Corporate_Name field?
   - Are some facilities grouped differently in parent/child relationships?

3. **Geographic or Operational Filters**
   - Does CRM exclude certain facility types?
   - Are closed/inactive facilities included in our count?

4. **Data Source Timing**
   - When was CRM last updated vs. V17.1 database?
   - Recent M&A activity affecting counts?

---

## Proposed Analysis Approach

### Step 1: Corporate Account Deep Dive
Run detailed facility lists for specific corporate entities to compare:

```python
# Example investigation for a corporate entity
corporate_name = "TRILOGY HEALTH SERVICES"  # or any entity
facilities = df[df['Corporate_Name'] == corporate_name]

# Show full facility list with key fields
facilities[['Facility_Name', 'Address', 'City', 'State', 
           'Source_Type', 'Do_We_Serve', 'Census']].to_excel('facility_list.xlsx')
```

### Step 2: Look for Duplicates
Check if facilities appear multiple times:

```python
# Check for duplicate facility names
duplicates = df[df.duplicated(['Facility_Name', 'City', 'State'], keep=False)]
if len(duplicates) > 0:
    print(f"Found {len(duplicates)} potential duplicate entries")
```

### Step 3: Compare Specific Corporate Counts

| Corporate Entity | V18 Database Count | CRM Count | Difference | Investigation Needed |
|-----------------|-------------------|-----------|------------|---------------------|
| Trilogy Health Services | 186 | ? | ? | List all facilities |
| American Senior Communities | 150 | ? | ? | Check for duplicates |
| SABER Healthcare | 159 | ? | ? | Verify all locations |
| [Add more as needed] | | | | |

---

## Questions for Next Session

1. **Which corporate accounts show the biggest count discrepancies?**
2. **Can we get a CRM export to compare facility-by-facility?**
3. **Are there specific states where counts don't match?**
4. **Do we need to adjust our counting methodology?**

---

## Recommended Next Actions

1. **Start with 2-3 corporate entities** where counts differ most
2. **Export full facility lists** from both systems
3. **Compare facility-by-facility** to identify:
   - Missing facilities
   - Duplicate entries
   - Different groupings
4. **Document patterns** to update database or counting rules

---

## Technical Context for Next Chat

- Database has 21,023 total facilities
- Uses V17.1 database with V18.1 cleanup (NULL→'No', SABER unblocked, "unknown" reclassified)
- Corporate/Independent classification uses Four-Rule methodology
- Barriers affect 1,383 facilities

**Key columns to investigate**:
- `Corporate_Name` - Parent company grouping
- `Facility_Name` - Individual facility identification  
- `Source_Type` - SNF vs ALF classification
- `Do_We_Serve` - Service status
- `Address`, `City`, `State` - Geographic identifiers

---

## Session Handoff Notes

**For next Claude session**: Start by loading Economic_Model_Scenario_1_Combined_V18.1.xlsx and investigating specific corporate entities where facility counts don't match CRM. Focus on creating detailed facility lists that can be compared line-by-line with CRM exports.

**Priority**: Understand WHY counts differ before making any database changes. The issue might be methodology rather than data accuracy.
