# START_HERE.md
## Eventus Healthcare Economic Model V18.0

**Version**: 18.0  
**Date**: November 2025  
**Status**: PRODUCTION READY

---

## 1. Document Hierarchy & Reading Order

**Read in this sequence before any work:**

| Order | Document | Purpose | Action |
|-------|----------|---------|--------|
| 1 | START_HERE_V18.md | Engagement workflow | You are here |
| 2 | Final_Model_Rulebook_V18.md | Authoritative reference | Read Section 1 (Governance) fully |
| 3 | Relevant rulebook sections | Task-specific rules | Reference as needed |

**Authority:** The Final_Model_Rulebook is the single authoritative reference. When in doubt, defer to the rulebook. This document provides sequencing only.

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
Combined_Database_FINAL_V18.xlsx (Source of Truth - V17.1, 21,023 facilities)
              ↓
Fee_Schedule_Reference_V18.xlsx ──→ Economic_Model_Scenario_[1,2,3]_Combined_V18.xlsx
                                                    ↓
                                    ┌───────────────┼───────────────┐
                                    ↓               ↓               ↓
                         Comprehensive_Report    QC_Validation    Custom Reports
                         _Workbook_V18.xlsx     _Workbook_V18.xlsx
```

### File Permissions

| File | Read | Modify | Notes |
|------|------|--------|-------|
| Combined_Database | ✓ | ✓ | All changes start here |
| Fee_Schedule_Reference | ✓ | Auth required | Independent of database |
| Economic_Model_Scenarios | ✓ | Regenerate only | Never edit directly |
| Comprehensive_Report | ✓ | Regenerate only | Output from scenarios |
| QC_Validation_Workbook | ✓ | Regenerate only | Validation output |

### Documentation Files

| File | Purpose |
|------|---------|
| Final_Model_Rulebook_V18.md | All rules and specifications |
| START_HERE_V18.md | Engagement workflow (this file) |
| V17_to_V18_Comparison_Report.md | Change documentation |
| V17_0_to_V17_1_Comparison_Report.md | Database evolution context |

---

## 4. Engagement Workflow

### BEFORE Starting Any Task

1. **Read this document** completely
2. **Read Rulebook Section 1** (System Overview & Governance)
3. **Read Rulebook Section 2** (Combined Database) - NEW in V18
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
| Total Facilities | 21,023 | Section 4.8 |
| SNF Facilities | 15,234 | Section 2.2 |
| ALF Facilities | 5,789 | Section 2.2 |
| Facilities We Serve | 1,743 | Section 2.5 |
| Corporate Facilities | 12,053 | Section 2.3 |
| Independent Facilities | 8,970 | Section 2.3 |
| Corporate Chains | 1,026 | Section 2.3 |
| SNF Total Fee (S1) | $4,583.50 | Section 3.3 |
| ALF Total Fee (S1) | $3,699.50 | Section 3.3 |
| QC Validation Workbook | All PASS | Section 1.5 |
| Files versioned correctly | V18.x | Section 1.3 |
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
| SNF/ALF fee tables | 3.1, 3.3 |
| Adjusters | 3.2 |
| Current Revenue calculation | 4.3 |
| Integration Revenue calculation | 4.4 |
| New Business Revenue calculation | 4.5 |
| Total Potential calculation | 4.6 |
| Market definitions (states) | 5.1 |
| Ownership classification (reporting) | 5.2 |
| Barrier types and counts | 5.3 |
| TAM/SAM/SOM filters | 5.4 |
| Report generation methodology | 6.1-6.6 |

---

## 7. V18 Key Changes

**Database Expansion:**
- V15: 17,434 facilities (14,750 SNF + 2,684 ALF)
- V18: 21,023 facilities (15,234 SNF + 5,789 ALF)
- Change: +3,589 facilities (+20.6%)

**Fee Structure Updates:**
- SNF Total (S1): $4,311.98 → $4,583.50 (+6.3%)
- ALF Total (S1): $3,724.00 → $3,699.50 (-0.7%)
- PCP SNF: $2,600 → $3,078 (+18.4%)
- PCP ALF: $1,875 → $2,084 (+11.1%)
- MH SNF: $1,624 → $1,211 (-25.4%)
- MH ALF: $1,898 → $1,431 (-24.6%)

**Ownership Reclassification (V17.1):**
- 2,327 facilities reclassified (11.1%)
- Single-facility LLCs: Corporate → Independent
- Consistent Four-Rule hierarchy applied to all facilities
- Result: 12,053 Corporate (1,026 chains), 8,970 Independent

**Documentation Enhancements:**
- NEW Section 2: Combined Database with source file evolution
- Section 1.6: Production Package Requirements (10-file compendium)
- Section 2.3: Four-Rule Ownership Classification methodology

**Full details:** See V17_to_V18_Comparison_Report.md and V17_0_to_V17_1_Comparison_Report.md

---

## 8. Version History

| Version | Date | Facilities | Key Changes |
|---------|------|------------|-------------|
| **V18.0** | Nov 2025 | 21,023 | V17.1 database, updated fees, Section 2 documentation |
| V15.0 | Nov 2025 | 17,434 | Tables 1-3 include Independent in SAM/SOM |
| V14.0 | Nov 2025 | 17,434 | Corrected scenario calculations |
| V12.0 | Nov 2025 | 17,434 | Correct file formats, barrier calculations |
| V11.0 | Nov 2025 | 17,434 | Integrated Barrier propagation |
| V10.0 | Nov 2025 | 17,434 | ALF fees corrected, QC validation |

---

**END OF START_HERE**

*Proceed to Final_Model_Rulebook_V18.md for complete specifications.*
