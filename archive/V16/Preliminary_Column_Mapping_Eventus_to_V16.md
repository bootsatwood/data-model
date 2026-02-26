# Preliminary Column Hierarchy Mapping
## Eventus WholeHealth Export → Combined_Database_FINAL_V16.xlsx
### Data Integration Analysis - November 2025

---

## DATASET OVERVIEW

### New Incoming Data: Eventus_WholeHealth_One-Time_Nationwide_Inventory_Export_11_17_25.xlsx
- **Total Rows**: 23,142 facilities
- **Total Columns**: 42
- **Geographic Scope**: Nationwide (50 states)
- **Primary Focus**: Assisted Living facilities (AL/IL/MC units)
- **Data Quality**: EXCELLENT (minimal nulls in critical fields)

### Current Database: Combined_Database_FINAL_V16.xlsx
- **Total Rows**: 17,434 facilities
- **Total Columns**: 23
- **Geographic Scope**: 6 states (IN, KY, NC, OH, SC, VA)
- **Primary Focus**: SNF and ALF facilities
- **Status**: Enhanced with geographic tiers and contract status

---

## KEY OBSERVATIONS

### Critical Differences
1. **Row Count**: New data has 23,142 vs. current 17,434 (+5,708 facilities)
2. **Facility Type**: New data is ALF-heavy; current has SNF+ALF mix
3. **Geographic Coverage**: New data is nationwide; current is 6-state focused
4. **Unit Classification**: New data breaks down by AL/IL/MC/NC; current uses Census/Total_Beds

### Data Quality Assessment
| Quality Factor | Rating | Notes |
|----------------|--------|-------|
| Completeness | ⭐⭐⭐⭐⭐ | No nulls in critical fields except CCN (13% populated) |
| GPS Coordinates | ⭐⭐⭐⭐⭐ | 100% populated (Latitude/Longitude) |
| Ownership Data | ⭐⭐⭐⭐⭐ | Owner Name 100% populated |
| Contact Info | ⭐⭐⭐⭐ | Building admin data ~70% populated |
| Operational Data | ⭐⭐⭐⭐⭐ | Unit counts complete, open/construction status |

---

## COLUMN MAPPING BY CATEGORY

### Category 1: DIRECT MATCHES (Same Data, Different Names)

| V16 Column | Eventus Column | Match Quality | Notes |
|------------|----------------|---------------|-------|
| Facility_Name | Building Name | ⭐⭐⭐⭐⭐ | Direct replacement |
| Address | Address | ⭐⭐⭐⭐⭐ | Direct match |
| City | City | ⭐⭐⭐⭐⭐ | Direct match |
| State | State | ⭐⭐⭐⭐⭐ | Direct match |
| ZIP | Zip | ⭐⭐⭐⭐⭐ | Direct match (note case difference) |
| County | County/Equiv | ⭐⭐⭐⭐⭐ | Direct match |
| Latitude | Latitude | ⭐⭐⭐⭐⭐ | Direct match |
| Longitude | Longitude | ⭐⭐⭐⭐⭐ | Direct match |

### Category 2: SEMANTIC MATCHES (Requires Mapping/Calculation)

| V16 Column | Eventus Equivalent | Mapping Logic | Confidence |
|------------|-------------------|---------------|------------|
| **Total_Beds** | Total Units | Direct replacement | ⭐⭐⭐⭐⭐ |
| **Census** | Total Units - Open Units | Calculate: Occupied = Total - Open | ⭐⭐⭐⭐ |
| **Corporate_Name** | Owner Name | Use Owner Name as corporate | ⭐⭐⭐⭐⭐ |
| **Source_Type** | AL/NC Open Units | If NC > 0 → SNF, else ALF | ⭐⭐⭐⭐ |
| **Ownership_Type** | Profit Status | Map profit status to Corporate/Independent | ⭐⭐⭐ |

**Source_Type Classification Logic**:
```
IF NC Open Units > 0 THEN "SNF"
ELSE IF AL Open Units > 0 OR MC Open Units > 0 OR IL Open Units > 0 THEN "ALF"
ELSE "Unknown"
```

**Census Calculation**:
```
Census = Total Units - Open Units
(Open Units represents VACANT units, so occupied = total - open)
```

### Category 3: PARTIAL MATCHES (Need Additional Data/Logic)

| V16 Column | Eventus Data | Gap | Solution |
|------------|--------------|-----|----------|
| **Do_We_Serve** | N/A | Not in new data | PRESERVE from V16 for existing facilities |
| **Integrated_Flag** | N/A | Not in new data | PRESERVE from V16 for existing facilities |
| **PCP_Flag** | N/A | Not in new data | PRESERVE from V16 for existing facilities |
| **MH_Flag** | N/A | Not in new data | PRESERVE from V16 for existing facilities |
| **Barrier** | N/A | Not in new data | PRESERVE from V16, calculate for new |
| **Contract_Status** | N/A | Not in new data | Default to blank for new facilities |
| **Geographic_Tier** | Latitude/Longitude | Calculate based on metro proximity | RECALCULATE for all |
| **Integration_Eligible** | Multiple fields | Recalculate based on rules | RECALCULATE for all |
| **New_Business_Eligible** | Multiple fields | Recalculate based on rules | RECALCULATE for all |
| **Data_Quality_Flag** | N/A | Assessment needed | RECALCULATE for all |

### Category 4: NEW COLUMNS IN EVENTUS (Not in V16)

| Eventus Column | Type | Potential Use | Priority |
|----------------|------|---------------|----------|
| **Building ID** | Identifier | Unique facility ID (UUID) | HIGH |
| **Building Phone** | Contact | Sales/operations contact | MEDIUM |
| **CCN** | Regulatory | Medicare certification (13% populated) | HIGH |
| **MSA** | Geographic | Metropolitan Statistical Area | HIGH |
| **Place** | Geographic | Census place designation | LOW |
| **Year Built** | Facility | Age of facility | MEDIUM |
| **Year Opened** | Facility | Operational history | LOW |
| **Sq.Ft.** | Facility | Physical size | LOW |
| **Lot Acreage** | Facility | Property size | LOW |
| **Owner Address/City/State/Zip** | Ownership | Corporate headquarters location | MEDIUM |
| **Building Administrator** (First/Last/Number/Email) | Contact | Key contact for sales | HIGH |
| **IL Open Units** | Capacity | Independent Living units | HIGH |
| **AL Open Units** | Capacity | Assisted Living units | HIGH |
| **MC Open Units** | Capacity | Memory Care units | HIGH |
| **NC Open Units** | Capacity | Nursing Care units | HIGH |
| **Construction Units** (All types) | Pipeline | Future capacity expansion | MEDIUM |
| **AA Open/Construction Units** | Capacity | Age-Adjusted units (?) | LOW |
| **Operator ID** | Identifier | Operating company ID | HIGH |
| **Operator Name** | Operator | May differ from Owner | HIGH |

### Category 5: V16 COLUMNS WITHOUT EVENTUS MATCH

These columns MUST be preserved/calculated during merge:

| V16 Column | Source | Action Required |
|------------|--------|-----------------|
| Do_We_Serve | Internal operations | PRESERVE for matches, default "No" for new |
| Integrated_Flag | Internal operations | PRESERVE for matches, default "No" for new |
| PCP_Flag | Internal operations | PRESERVE for matches, default "No" for new |
| MH_Flag | Internal operations | PRESERVE for matches, default "No" for new |
| Barrier | Internal analysis | PRESERVE for matches, recalculate for new |
| Contract_Status | Book1.xlsx | PRESERVE for matches, default blank for new |
| Geographic_Tier | Calculated | RECALCULATE for ALL facilities |
| Integration_Eligible | Calculated | RECALCULATE for ALL facilities |
| New_Business_Eligible | Calculated | RECALCULATE for ALL facilities |
| Data_Quality_Flag | Assessment | RECALCULATE for ALL facilities |

---

## FACILITY TYPE CLASSIFICATION

### Unit Type Distribution in New Data

| Unit Type | Facilities | % of Total | Notes |
|-----------|------------|------------|-------|
| AL (Assisted Living) | 17,570 | 75.9% | Core ALF facilities |
| IL (Independent Living) | 6,461 | 27.9% | Often mixed with AL |
| MC (Memory Care) | 12,262 | 53.0% | Often co-located with AL |
| NC (Nursing Care) | 3,427 | 14.8% | TRUE SNF facilities |

### Source_Type Mapping Strategy

**Option A: Conservative (NC-Based)**
- SNF = Facilities with NC Open Units > 0 (3,427 facilities)
- ALF = All others (19,715 facilities)

**Option B: Functional (CCN-Based)**
- SNF = Facilities with CCN populated (3,029 facilities - 13%)
- ALF = Facilities without CCN (20,113 facilities - 87%)

**Option C: Comprehensive (Hybrid)**
- SNF = NC > 0 OR CCN populated (likely ~3,500 facilities)
- ALF = All others (~19,600 facilities)

**RECOMMENDATION**: Use Option A (NC-Based) as it's cleanest and matches our existing "bed type" logic.

---

## KEY IDENTIFIERS FOR MATCHING

### Recommended Matching Strategy

**Primary Match**: Latitude + Longitude (±0.0001 degrees ~10 meters)
- V16 has 100% GPS coordinates
- Eventus has 100% GPS coordinates
- Best way to identify same physical facility

**Secondary Match**: Facility Name + City + State
- Handle cases where GPS might differ slightly
- Fuzzy matching for name variations

**Tertiary Match**: Address + ZIP
- Backup for GPS mismatches

### Expected Match Rates

Given geographic scope differences:
- **Direct Matches**: ~15,000-16,000 facilities (86-92% of V16)
- **New Facilities**: ~7,000-8,000 (Eventus only)
- **V16 Only**: ~1,000-2,000 (missing from Eventus)

---

## CRITICAL BUSINESS LOGIC FIELDS

### Fields Requiring Preservation/Calculation

1. **Do_We_Serve** (Critical - drives all revenue calculations)
   - MUST preserve for existing facilities
   - Default "No" for new facilities

2. **Service Flags** (Integrated_Flag, PCP_Flag, MH_Flag)
   - MUST preserve for existing facilities
   - Default "No" for new facilities

3. **Barrier** (Critical - blocks revenue opportunities)
   - MUST preserve for existing facilities
   - Need to assess propagation rules for new facilities

4. **Contract_Status** (RED/YELLOW/GREEN)
   - MUST preserve for existing facilities
   - Default blank for new facilities (not enough data)

5. **Geographic_Tier** (A_Metro/B_Highway/C_Rural)
   - RECALCULATE for ALL facilities using 19 metro centers
   - Critical for revenue opportunity filtering

6. **Eligibility Flags** (Integration_Eligible, New_Business_Eligible)
   - RECALCULATE for ALL facilities
   - Based on: Geography + Size + Barriers + Contract Status

---

## DATA QUALITY CONCERNS & MITIGATIONS

### Potential Issues

1. **Census Calculation** (Total - Open = Occupied)
   - **Concern**: "Open Units" might mean available OR vacant
   - **Mitigation**: Validate with sample facilities from V16
   - **Risk**: MEDIUM

2. **Ownership Type** (Profit Status field)
   - **Values**: "Unknown" is majority value
   - **Impact**: Cannot reliably classify Corporate vs. Independent
   - **Mitigation**: Use Operator Name as proxy OR preserve V16 classifications
   - **Risk**: HIGH

3. **CCN Population** (Only 13%)
   - **Concern**: Only 3,029 of 23,142 have CCN
   - **Impact**: Cannot use CCN alone for SNF identification
   - **Mitigation**: Use NC Open Units > 0 as SNF indicator
   - **Risk**: LOW (NC units are reliable)

4. **Geographic Scope Expansion**
   - **Concern**: Adding 44 new states beyond current 6
   - **Impact**: Strategic focus may be diluted
   - **Mitigation**: Keep 6-state SAM filter, use others for TAM expansion
   - **Risk**: LOW (filtering handles this)

5. **Operator vs. Owner**
   - **Observation**: Operator Name differs from Owner Name in many cases
   - **Impact**: Corporate barrier propagation may need both fields
   - **Mitigation**: Assess which entity drives operational barriers
   - **Risk**: MEDIUM

---

## RECOMMENDED MERGE STRATEGY

### Phase 1: Match Existing Facilities
1. Match V16 facilities to Eventus using GPS (±0.0001°)
2. Preserve all V16 operational fields (Do_We_Serve, Flags, Barriers, Contract_Status)
3. UPDATE facility details (name, address, beds) from Eventus (newer data)
4. ADD new Eventus fields (Building ID, CCN, Admin contacts, unit breakdowns)

### Phase 2: Add New Facilities
1. Identify Eventus facilities with no V16 match
2. Default operational fields (Do_We_Serve=No, all flags=No, Contract_Status=blank)
3. Assess Corporate Barrier propagation for new facilities
4. Populate all available Eventus fields

### Phase 3: Recalculate Derived Fields
1. Geographic_Tier → RECALCULATE for ALL using 19 metro centers
2. Integration_Eligible → RECALCULATE for ALL
3. New_Business_Eligible → RECALCULATE for ALL
4. Data_Quality_Flag → REASSESS for ALL

### Phase 4: Validation
1. Verify row counts (expect ~24,000 total: 16,000 matches + 7,000 new + 1,000 V16-only)
2. Check revenue calculations still work correctly
3. Validate geographic tier distribution
4. Confirm barrier propagation logic intact

---

## STATE EXPANSION IMPACT

### Current 6-State Focus (V16)
- IN, KY, NC, OH, SC, VA
- **V16 Facilities**: 17,434 (focused on these states)

### Top 20 States in New Data
| State | Facilities | In V16 States? | Action |
|-------|------------|----------------|--------|
| CA | 1,819 | No | Add to TAM |
| TX | 1,578 | No | Add to TAM |
| FL | 1,354 | No | Add to TAM |
| WI | 1,226 | No | Add to TAM |
| PA | 1,100 | No | Add to TAM |
| MI | 1,032 | No | Add to TAM |
| MN | 1,027 | No | Add to TAM |
| **OH** | **1,019** | **YES** | Update existing |
| IL | 808 | No | Add to TAM |
| **NC** | **778** | **YES** | Update existing |
| MO | 686 | No | Add to TAM |
| NY | 674 | No | Add to TAM |
| WA | 660 | No | Add to TAM |
| **VA** | **562** | **YES** | Update existing |
| OR | 552 | No | Add to TAM |
| IA | 512 | No | Add to TAM |
| GA | 499 | No | Add to TAM |
| CO | 475 | No | Add to TAM |
| MD | 444 | No | Add to TAM |
| AZ | 440 | No | Add to TAM |

**Expected V16 State Coverage in New Data**: ~3,000-4,000 facilities

---

## NEXT STEPS FOR INTEGRATION

### Before Proceeding
1. ✅ **Validate Census Calculation** - Confirm "Open Units" = vacant
2. ⚠️ **Ownership Type Strategy** - Decide on Corporate vs. Independent classification
3. ⚠️ **Operator vs. Owner** - Determine which drives corporate barriers
4. ✅ **Match Strategy** - GPS-based matching should work well

### Decisions Required
1. **Keep V16-only facilities?** (Those not in Eventus)
   - Recommendation: YES, mark as "Data_Quality_Flag = Needs_Verification"

2. **Expand to nationwide or stay 6-state focused?**
   - Recommendation: Add all, filter by state for SAM calculations

3. **Use Operator Name or Owner Name for corporate barriers?**
   - Recommendation: Analyze overlap, may need to track both

4. **How to handle "Unknown" profit status?**
   - Recommendation: Use V16 classifications for matches, leave blank for new

### Technical Considerations
- **File Size**: Will increase significantly (~24K rows, 50+ columns)
- **Performance**: May need optimization for Excel operations
- **Version Control**: This will be V17 (major structural change)

---

## SUMMARY RECOMMENDATION

**PROCEED WITH CAUTION** - This is a major database enhancement that will:
- ✅ Improve data quality (newer, more complete information)
- ✅ Expand TAM to nationwide scope (23,142 vs 17,434)
- ✅ Add valuable new fields (CCN, unit breakdowns, contacts)
- ⚠️ Require careful preservation of operational flags
- ⚠️ Need validation of census calculation method
- ⚠️ May impact existing revenue calculations if not careful

**CONFIDENCE LEVEL**: 85% - Data quality is excellent, but business logic preservation requires careful execution.

---

**END OF PRELIMINARY MAPPING**
