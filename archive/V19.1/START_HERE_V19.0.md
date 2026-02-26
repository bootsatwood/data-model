# START_HERE.md
## Eventus Healthcare Economic Model V19.0

**Version**: 19.0  
**Date**: November 23, 2025  
**Status**: PRODUCTION READY

---

## 1. Document Hierarchy & Reading Order

**Read in this sequence before any work:**

| Order | Document | Purpose | Action |
|-------|----------|---------|--------|
| 1 | START_HERE_V19.md | Engagement workflow | You are here |
| 2 | Final_Model_Rulebook_V18.7.md | Authoritative reference | Read Section 1 (Governance) fully |
| 3 | Relevant rulebook sections | Task-specific rules | Reference as needed |

**Authority:** The Final_Model_Rulebook is the single authoritative reference. When in doubt, defer to the rulebook. This document provides sequencing only.

**Note:** V19 scenarios use V18.7 rulebook specifications. No rulebook changes from V18.7 to V19.0 - only database versions updated.

---

## 2. Critical Constraints

**Before ANY action, understand these non-negotiable rules:**

| Constraint | Consequence |
|------------|-------------|
| No unauthorized fee modifications | Full audit, rollback |
| No skipping QC validation | Delivery rejected |
| No overwriting files | Version integrity lost |
| No editing downstream files | Data corruption |

**Full details:** Rulebook Section 1.2 (Prohibited Actions)

---

## 3. File Inventory & Relationships

### Data Flow

```
Combined_Database_FINAL_V19.0.xlsx (Source of Truth - V18.7, 20,943 facilities)
              â†"
Fee_Schedule_Reference_V19.0.xlsx â"€â"€â†' Economic_Model_Scenario_[1,2,3]_Combined_V19.0.xlsx
                                                    â†"
                                    â"Œâ"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"¼â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"€â"
                                    â†"               â†"               â†"
                         Comprehensive_Report    QC_Validation    Custom Reports
                         _Workbook_V19.0.xlsx   _Workbook_V19.0.xlsx
                         (TO BE GENERATED)      (TO BE GENERATED)
```

### File Permissions

| File | Read | Modify | Notes |
|------|------|--------|-------|
| Combined_Database | âœ" | âœ" | All changes start here |
| Fee_Schedule_Reference | âœ" | Auth required | Independent of database |
| Economic_Model_Scenarios | âœ" | Regenerate only | Never edit directly |
| Comprehensive_Report | âœ" | Regenerate only | Output from scenarios |
| QC_Validation_Workbook | âœ" | Regenerate only | Validation output |

### Documentation Files

| File | Purpose |
|------|---------|
| Final_Model_Rulebook_V18.7.md | All rules and specifications |
| START_HERE_V19.md | Engagement workflow (this file) |
| V18_to_V19_Comparison_Report.md | Change documentation |

---

## 4. Engagement Workflow

### BEFORE Starting Any Task

1. **Read this document** completely
2. **Read Rulebook Section 1** (System Overview & Governance)
3. **Read Rulebook Section 2** (Combined Database)
4. **Identify task type:**
   - Database modification → Requires authorization
   - Report generation → Follow methodology in Rulebook Section 6
   - Fee change → STOP, requires written authorization
5. **Document baseline values** before making changes

### DURING Task Execution

1. **Follow data flow** - Changes start at database, flow downstream
2. **Reference rulebook sections** for specific rules:
   - Production package requirements: Section 1.6
   - Database structure & ownership: Section 2
   - Fee values: Section 3
   - Revenue calculations: Section 4
   - Reporting filters: Section 5
   - Report methodology: Section 6
3. **Never edit downstream files** to fix upstream problems
4. **Increment version numbers** for any file modifications

### BEFORE Delivery

1. **Run QC Validation** - All checks must PASS
2. **Complete Validation Gate** (Section 5 below)
3. **Create comparison report** documenting changes
4. **Verify file naming** includes correct version
5. **Verify complete package** - All 10 files (see Rulebook Section 1.6)

---

## 5. Validation Gate

**All items must be verified before any delivery:**

| Check | Expected Value | Rulebook Reference |
|-------|----------------|-------------------|
| Total Facilities | 20,943 | Section 2.2 |
| SNF Facilities | 15,244 | Section 2.2 |
| ALF Facilities | 5,699 | Section 2.2 |
| Facilities We Serve | 1,663 | Section 2.5 |
| Facilities with Barriers | 848 | Section 5.3 |
| SNF Total Fee (S1) | $4,583.50 | Section 3.3 |
| ALF Total Fee (S1) | $3,699.50 | Section 3.3 |
| Current Revenue (S2) | ~$200.7M | Section 4.8 |
| Total Potential (S2) | ~$7.77B | Section 4.8 |
| QC Validation Workbook | All PASS | Section 1.5 |
| Files versioned correctly | V19.0 | Section 1.3 |
| Complete package | 10 files | Section 1.6 |
| Comparison report created | Yes | Section 1.3 |

---

## 6. Quick Reference Pointers

| Topic | Rulebook Section |
|-------|------------------|
| Prohibited actions | 1.2 |
| Version control | 1.3 |
| Fee change process | 1.4 |
| QC requirements | 1.5 |
| Production package requirements | 1.6 |
| Database architecture | 2.1 |
| Source file evolution | 2.2 |
| Ownership classification (Four-Rule) | 2.3 |
| Facility type classification | 2.4 |
| Service status & flags | 2.5, 2.6 |
| Data quality flags | 2.7 |
| SNF/ALF fee tables | 3.1, 3.3 |
| Adjusters | 3.2 |
| Current Revenue calculation | 4.3 |
| Integration Revenue calculation | 4.4 |
| New Business Revenue calculation | 4.5 |
| Total Potential calculation | 4.6 |
| V18.7 key metrics | 4.8 |
| Market definitions (states) | 5.1 |
| Ownership classification (reporting) | 5.2 |
| Barrier types and counts | 5.3 |
| TAM/SAM/SOM filters | 5.4 |
| Report generation methodology | 6.1-6.6 |
| PowerBI reconciliation work | 8.1 |
| Strategic barrier removals | 8.2 |

---

## 7. V18 → V19 Key Changes

**Database Evolution (V18.0 → V18.7 → V19.0):**

| Version | Facilities | Served | Barriers | Key Change |
|---------|------------|--------|----------|------------|
| V18.0 | 21,023 | 1,743 | 1,383 | V17.1 database baseline |
| V18.5 | 20,930 | 1,651 | 1,203 | Removed 93 fake ALF duplicates |
| V18.6 | 20,943 | 1,663 | 1,203 | Added 13 PowerBI facilities |
| V18.7 | 20,943 | 1,663 | 848 | Removed 355 barriers (21 entities) |
| **V19.0** | **20,943** | **1,663** | **848** | **Scenario regeneration** |

**Major Changes V18.0 → V19.0:**
- Facilities: -80 (-0.4%)
- Served: -80 (-4.6%)
- Barriers: -535 (-38.7%)
- Addressable Market: +455 facilities (+2.3%)

**V19.0 Revenue Impact:**
- Current Revenue (S2): $200.7M (was $202.4M in V18.0)
- Total Potential (S2): $7.77B (was $7.68B in V18.0)
- Net Change: +$83M in Total Potential (+1.1%)

**Key Data Quality Improvements:**
1. **PowerBI Reconciliation** (V18.5-V18.6):
   - Removed 93 fake ALF duplicates
   - Added 13 missing facilities from PowerBI
   - Flagged 399 SNFs for verification

2. **Strategic Barrier Removals** (V18.7):
   - 21 corporate entities freed
   - 355 facilities now addressable
   - Major entities: INFINITY HEALTHCARE, ALG, CARDON, BRICKYARD
   - +$35-40M annual revenue opportunity

**Fee Structure:**
- SNF Total (S1): $4,583.50 (unchanged from V18.0)
- ALF Total (S1): $3,699.50 (unchanged from V18.0)
- No fee changes V18 → V19

**Full details:** See V18_to_V19_Comparison_Report.md

---

## 8. V19.0 Scenario Metrics

### Scenario 1 (Conservative - Baseline)

| Metric | Value |
|--------|-------|
| Current Revenue | $172.1M |
| Integration Revenue | $154.3M |
| New Business Revenue | $6,915.6M |
| **Total Potential** | **$7,069.9M** |

### Scenario 2 (Market Expansion +10%)

| Metric | Value |
|--------|-------|
| Current Revenue | $200.7M |
| Integration Revenue | $159.4M |
| New Business Revenue | $7,607.2M |
| **Total Potential** | **$7,766.6M** |

### Scenario 3 (Premium Services +20%)

| Metric | Value |
|--------|-------|
| Current Revenue | $225.3M |
| Integration Revenue | $168.8M |
| New Business Revenue | $8,298.8M |
| **Total Potential** | **$8,467.5M** |

---

## 9. Outstanding Items

### Files NOT Yet Generated (Hold for Business Review):

- Comprehensive_Report_Workbook_V19.0.xlsx
- QC_Validation_Workbook_V19.0.xlsx

**Rationale:** Awaiting business review of V19 scenario results before generating final reports.

### Outstanding Business Questions:

1. **399 Flagged SNFs** (V18.6): Are they actually served?
   - Critical for revenue accuracy
   - May impact Current Revenue by $15M-$20M

2. **Crestview Facility** (V18.6): Should it be marked as served?
   - Currently Do_We_Serve='No'
   - In PowerBI but no service volumes

3. **Corporate Rankings Validation**: Review new entities in top 20
   - INFINITY HEALTHCARE (101 facilities)
   - ALG (65 facilities, 100% served)
   - CARDON & ASSOCIATES (34 facilities)
   - BRICKYARD HEALTHCARE (23 facilities)

---

## 10. Version History

| Version | Date | Facilities | Key Changes |
|---------|------|------------|-------------|
| **V19.0** | Nov 2025 | 20,943 | Scenario regeneration with V18.7 database (barrier removals) |
| V18.7 | Nov 2025 | 20,943 | Barrier removals: 21 entities, 355 facilities freed |
| V18.6 | Nov 2025 | 20,943 | PowerBI additions: +13 facilities, 399 SNFs flagged |
| V18.5 | Nov 2025 | 20,930 | PowerBI reconciliation: Removed 93 fake ALF duplicates |
| V18.0 | Nov 2025 | 21,023 | V17.1 database, updated fees, Section 2 documentation |
| V15.0 | Nov 2025 | 17,434 | Tables 1-3 include Independent in SAM/SOM |
| V14.0 | Nov 2025 | 17,434 | Corrected scenario calculations |
| V12.0 | Nov 2025 | 17,434 | Correct file formats, barrier calculations |

---

**END OF START_HERE**

*Proceed to Final_Model_Rulebook_V18.7.md for complete specifications.*
