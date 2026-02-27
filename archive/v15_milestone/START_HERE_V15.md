# START_HERE.md
## Eventus Healthcare Economic Model V15.0

**Version**: 15.0  
**Date**: November 2025  
**Status**: PRODUCTION READY

---

## 1. Document Hierarchy & Reading Order

**Read in this sequence before any work:**

| Order | Document | Purpose | Action |
|-------|----------|---------|--------|
| 1 | START_HERE_V15.md | Engagement workflow | You are here |
| 2 | Final_Model_Rulebook_V15.md | Authoritative reference | Read Section 1 (Governance) fully |
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
Combined_Database_FINAL_V15.xlsx (Source of Truth)
              ↓
Fee_Schedule_Reference_V15.xlsx ──→ Economic_Model_Scenario_[1,2,3]_Combined_V15.xlsx
                                                    ↓
                                    ┌───────────────┼───────────────┐
                                    ↓               ↓               ↓
                         Comprehensive_Report    QC_Validation    Custom Reports
                         _Workbook_V15.xlsx     _Workbook_V15.xlsx
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
| Final_Model_Rulebook_V15.md | All rules and specifications |
| START_HERE_V15.md | Engagement workflow (this file) |
| V14_to_V15_Change_Compendium.md | Change documentation |

---

## 4. Engagement Workflow

### BEFORE Starting Any Task

1. **Read this document** completely
2. **Read Rulebook Section 1** (System Overview & Governance)
3. **Identify task type:**
   - Database modification → Requires authorization
   - Report generation → Follow methodology in Rulebook Section 5
   - Fee change → STOP, requires written authorization
4. **Document baseline values** before making changes

### DURING Task Execution

1. **Follow data flow** - Changes start at database, flow downstream
2. **Reference rulebook sections** for specific rules:
   - Fee values: Section 2
   - Revenue calculations: Section 3
   - Reporting filters: Section 4
   - Report methodology: Section 5
3. **Never edit downstream files** to fix upstream problems
4. **Increment version numbers** for any file modifications

### BEFORE Delivery

1. **Run QC Validation** - All checks must PASS
2. **Complete Validation Gate** (Section 5 below)
3. **Create comparison report** documenting changes
4. **Verify file naming** includes correct version

---

## 5. Validation Gate

**All items must be verified before any delivery:**

| Check | Expected Value | Rulebook Reference |
|-------|----------------|-------------------|
| Total Facilities | 17,434 | Section 3.8 |
| Facilities We Serve | 1,743 | Section 3.8 |
| Total Barriers | 1,383 | Section 4.3 |
| ALF Current Revenue | $83,991,652 | Section 1.5 |
| SNF Current Revenue | $93,607,105 | Section 1.5 |
| Total Current Revenue | $177,598,757 | Section 3.8 |
| QC Validation Workbook | All PASS | Section 1.5 |
| Files versioned correctly | V15.x | Section 1.3 |
| Comparison report created | Yes | Section 1.3 |

---

## 6. Quick Reference Pointers

| Topic | Rulebook Section |
|-------|-----------------|
| Prohibited actions | 1.2 |
| Version control | 1.3 |
| Fee change process | 1.4 |
| QC requirements | 1.5 |
| SNF/ALF fee tables | 2.1, 2.3 |
| Adjusters | 2.2 |
| Current Revenue calculation | 3.3 |
| Integration Revenue calculation | 3.4 |
| New Business Revenue calculation | 3.5 |
| Total Potential calculation | 3.6 |
| Market definitions (states) | 4.1 |
| Ownership classification rules | 4.2 |
| Barrier types and counts | 4.3 |
| TAM/SAM/SOM filters | 4.4 |
| Report generation methodology | 5.1-5.6 |

---

## 7. V15 Key Changes

**Tables 1-3 (Facility Counts):**
- SAM and SOM now include BOTH Corporate AND Independent facilities
- Filters: Geographic (markets) and barriers apply; ownership filter removed
- Rationale: Shows complete addressable market by ownership type

**Tables 16-18, 25 (Corporate Rankings):**
- INDEPENDENT is now excluded from rankings
- These tables rank corporate entities (chains) only
- Rationale: Independent is not a corporate entity and cannot be meaningfully compared

**Full details:** See V14_to_V15_Change_Compendium.md

---

## 8. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| **V15.0** | Nov 2025 | Tables 1-3 include Independent in SAM/SOM; Tables 16-18 exclude INDEPENDENT |
| V14.0 | Nov 2025 | Corrected scenario calculations, consolidated barriers |
| V12.0 | Nov 2025 | Correct file formats, barrier calculations |
| V11.0 | Nov 2025 | Integrated Barrier propagation |
| V10.0 | Nov 2025 | ALF fees corrected, QC validation added |

---

**END OF START_HERE**

*Proceed to Final_Model_Rulebook_V15.md for complete specifications.*
