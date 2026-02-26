# Recommended Rulebook Updates for V18.3

## Updates Needed for Final_Model_Rulebook_V18.3.md

### 1. Version History Update

Add to Section 7 (Version History):

| Version | Date | Key Changes |
|---------|------|-------------|
| **V18.3** | Nov 2025 | Comprehensive Report corrections: SAM segment calculations fixed, Tables 22-24 populated with state ranges. No changes to fees, database, or calculation methodologies |
| V18.1 | Nov 2025 | Service flag cleanup (NULL → 'No'), SABER barrier removal (159 facilities), "unknown" reclassification (121 facilities), Scenario 2 as baseline for single-value tables |

### 2. Section 1.3 Version Control Requirements

Add clarification:

**After existing text, add:**

"**Report-Only Updates:** When only correcting the Comprehensive Report Workbook without changing underlying data or calculations:
- Use sub-version increment (e.g., V18.1 → V18.3)
- Document corrections in Version History
- No need to regenerate Economic Model Scenarios if unchanged
- Maintain consistent version numbers across package for traceability"

### 3. Section 6. Comprehensive Report Outputs

Replace the vague "Content unchanged from V18.0" with explicit details. Add new subsection:

#### 6.7 Critical Implementation Notes

**Data Source Requirements:**
- **ALWAYS** pull fresh data from Economic Model Scenario files
- **NEVER** copy values from previous report versions
- **VERIFY** row counts match between scenarios and report tables

**SAM/SOM Filter Verification:**
```
SAM Filters (Revenue Tables 4-9):
- Geography: State IN (existing_states + priority_states)
- Ownership: Ownership_Type == 'Corporate'  ← CRITICAL
- Barriers: Barrier.isna()

SAM Filters (Facility Tables 1-3):
- Geography: State IN (existing_states + priority_states)
- Ownership: Both Corporate AND Independent  ← DIFFERENT
- Barriers: Barrier.isna()
```

**Table Population Checklist:**
- [ ] Tables 1-3: Facility counts present for all segments
- [ ] Tables 4-6: Revenue values populated for TAM/SAM/SOM
- [ ] Tables 7-9: Ranges showing "S1_value - S3_value" format
- [ ] Tables 10-15: State-by-state breakdown for SOM
- [ ] Tables 16-18, 25: Corporate rankings excluding "Independent"
- [ ] Tables 19-21: State analysis with individual Existing states
- [ ] Tables 22-24: **MUST contain state ranges - not be empty**

### 4. Section 4.8 Key Metrics

Update to V18.3 values:

| Metric | V18.3 Value |
|--------|-------------|
| **Scenario 2 (Market +10%)** | |
| Current Revenue | $202.4M |
| Integration Revenue | $151.1M |
| New Business Revenue | $7,532.3M |
| **Total Potential** | **$7,683.4M** |
| | |
| **SAM Segment (S2)** | |
| SAM Total | $1,709.2M |
| SAM SNF | $1,308.1M |
| SAM ALF | $401.0M |

### 5. New Section 9: Common Errors and Prevention

Add new section after V18.1 Specific Guidance:

## 9. Common Errors and Prevention

### 9.1 Comprehensive Report Generation Errors

**Error**: SAM segment showing incorrect values
**Cause**: Not applying Corporate-only filter for revenue tables
**Prevention**: Use apply_filters_revenue() function with explicit ownership check

**Error**: Tables 22-24 empty
**Cause**: Missing state-by-state range calculation logic
**Prevention**: Ensure all 6 table sets (19-24) have complete state iteration

**Error**: Facility counts not matching database
**Cause**: Incorrect filter application or row shifting
**Prevention**: Verify counts against Economic Model Scenarios before finalizing

### 9.2 Data Quality Checks

Before delivering any Comprehensive Report:
1. Sum of TAM Current Revenue should equal Economic Model Scenario total
2. SAM values should be less than TAM values
3. SOM values should be less than or equal to SAM values
4. Tables 22-24 must have visible revenue ranges
5. No cells should display #REF!, #VALUE!, or other Excel errors

---

## Summary of Rulebook Changes for V18.3

1. **Version History**: Add V18.3 entry
2. **Version Control**: Clarify report-only updates
3. **Section 6**: Expand with explicit implementation details
4. **Key Metrics**: Update to V18.3 values
5. **New Section 9**: Add common errors and prevention guide

These updates will help prevent the types of errors that required the V18.3 correction and provide clearer guidance for future report generation.
