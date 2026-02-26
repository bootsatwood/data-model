# Facility Count Discrepancy Investigation Summary
## Database vs CRM Reconciliation

### The Core Problem
- **Our Database**: 1,743 facilities served
- **Your CRM**: ~1,200 facilities
- **GAP**: 543 facilities (31% difference)

### Key Findings

#### 1. Database Counts UNITS, CRM Counts CAMPUSES
- **200 facilities** are SNF/ALF pairs at same address
- If consolidated to campuses: **-100 facilities**
- Example: ASC has 30 campus locations with 60 individual units

#### 2. Duplicate/Aggregate Records Identified
- **81 facilities** at addresses with 3+ records
- **9 addresses** where largest census ≈ sum of others
- Heritage Park confirmed duplicate (148.7 ≈ 24+115)

#### 3. Top Served Corporates (Potential Issues)
| Corporate | Served Count | SNF/ALF Pairs |
|-----------|-------------|---------------|
| INDEPENDENT | 149 | 0 |
| ASC | 95 | 30 |
| ALG | 65 | 0 |
| SABER | 60 | 4 |
| BROOKDALE | 49 | 0 |

### ASC Deep Dive
- **Database**: 95 facilities
- **CRM**: 58 entries
- **Explanation**: 
  - 30 campus pairs (60 facilities → 30 campuses)
  - 1 Heritage Park duplicate
  - Different Heritage facilities (Place, Point, Post)

### Enriched Top 60 Insights
Your modified table shows:
- **Orange highlights**: SC exit if no M&A
- **Yellow highlights**: Multi-unit operators needing confirmation
- **Metro opportunities**: Quantified for most corporates
- **Expansion states**: PA, Michigan, Minnesota opportunities

### Path to ~1,200 Count
To align with CRM:
1. Consolidate SNF/ALF campus pairs: **-100**
2. Remove identified duplicates: **-40**
3. Review "INDEPENDENT" served status: **-100 to -150**
4. Clean remaining duplicates: **-50 to -100**
5. Review service definitions (what counts as "served")

### Critical Questions Remaining
1. Does CRM count administrative/employee records?
2. Are there timing differences (recently added/removed)?
3. Different service definitions between systems?
4. Should we maintain unit-level or campus-level counting?

### Next Steps
1. **Await ASC extract** to confirm their methodology
2. **Focus on Top 60 corporates** for business development
3. **Create cleaned dataset** with campus consolidation
4. **Standardize counting methodology** across systems

### Files Created This Session
- ASC_All_Records.xlsx (95 ASC facilities with all columns)
- This summary document

### Business Impact
Despite count discrepancy, strategic targets remain clear:
- **$6.94B total potential** (Scenario 1)
- **Top corporates identified** with metro expansion opportunities
- **State expansion targets**: PA, MI, MN
- **Integration opportunities**: $137.7M across served facilities

---
*Continue investigation in next session with ASC extract and campus consolidation logic*
