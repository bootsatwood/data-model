# Documentation Architecture V19.1
## Modular Rulebook System Overview

**Version**: 19.1  
**Date**: November 2025

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      CORE RULEBOOK V19.1                        │
│  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐         │
│  │   Database    │ │ Fee Structure │ │   Scenario    │         │
│  │    Spec       │ │   & Adjusters │ │  Methodology  │         │
│  └───────────────┘ └───────────────┘ └───────────────┘         │
│  ┌─────────────────────────────────────────────────────┐       │
│  │              CORE QC PROTOCOL (Section 6)           │       │
│  │  Database → Fee → Scenario → Sign-Off Gate          │       │
│  └─────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────┘
                              │
                    MUST PASS BEFORE
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    REPORT COMPENDIUMS                           │
│                                                                 │
│  ┌────────────────────┐  ┌────────────────────┐                │
│  │   Comprehensive    │  │   Metro Priority   │                │
│  │  Report Compendium │  │ Targets Compendium │  ← [Future]    │
│  │   (Tables 1-25)    │  │                    │                │
│  ├────────────────────┤  ├────────────────────┤                │
│  │  Embedded QC       │  │  Embedded QC       │                │
│  │  Protocol          │  │  Protocol          │                │
│  └────────────────────┘  └────────────────────┘                │
│                                                                 │
│  ┌────────────────────┐  ┌────────────────────┐                │
│  │   State Expansion  │  │   [Additional      │                │
│  │   Compendium       │  │    Reports]        │  ← [Future]    │
│  │                    │  │                    │                │
│  ├────────────────────┤  ├────────────────────┤                │
│  │  Embedded QC       │  │  Embedded QC       │                │
│  │  Protocol          │  │  Protocol          │                │
│  └────────────────────┘  └────────────────────┘                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Document Inventory

### Currently Documented

| Document | Status | Purpose |
|----------|--------|---------|
| **Core_Rulebook_V19.1.md** | ✅ Complete | Database, fees, scenarios, Core QC |
| **Comprehensive_Report_Compendium_V19.1.md** | ✅ Complete | Tables 1-25 methodology, Report QC |
| **Report_Compendium_TEMPLATE.md** | ✅ Complete | Template for new report compendiums |

### Future Compendiums (Not Yet Documented)

| Report Type | Priority | Notes |
|-------------|----------|-------|
| Metro Priority Targets | High | Roian has worked on this extensively |
| State Expansion Analysis | Medium | Geographic growth targeting |
| Geographic Tier Analysis | Medium | Metro/Highway/Rural breakdown |
| Corporate Deep Dive | Low | Individual chain analysis |

---

## Workflow Integration

### Stage 1: Core Validation
```
1. Load Combined Database
2. Load Fee Schedule
3. Generate Scenarios (S1, S2, S3)
4. Run Core QC Protocol (Core Rulebook Section 6)
5. Sign-off → Proceed to Reports
```

### Stage 2: Report Generation
```
For each report type needed:
1. Confirm Core QC sign-off exists
2. Reference appropriate Report Compendium
3. Generate report per compendium methodology
4. Run Report QC Protocol (embedded in compendium)
5. Sign-off → Deliver
```

---

## Version Control

### Independent Tracks

| Track | Current | Increment Triggers |
|-------|---------|-------------------|
| Database | V18.7 | Facility changes, barrier changes |
| Core Rulebook | V19.1 | Fee changes, methodology changes |
| Comprehensive Report | V19.1 | Table structure changes, filter logic changes |
| [Other Reports] | Per compendium | Report-specific changes |

### Compatibility Matrix

| Core Rulebook | Compatible Database | Compatible Reports |
|---------------|--------------------|--------------------|
| V19.1 | V18.7 | V19.x compendiums |
| V19.0 | V18.7 | V19.x compendiums |
| V18.x | V17.1 | V18.x compendiums |

---

## Handoff Procedures

### Core → Report Handoff

**Gate Criteria:**
- [ ] Core Rulebook QC Protocol Section 6 complete
- [ ] All database validation checks pass
- [ ] All fee structure validation checks pass
- [ ] All scenario calculation validation checks pass
- [ ] Sign-off recorded with date and validator

**Handoff Artifact:**
- Signed Core QC Protocol (Section 6.6)
- Version number confirmed
- Scenario files validated

### Report → Delivery Handoff

**Gate Criteria:**
- [ ] Core handoff complete
- [ ] Report Compendium QC Protocol complete
- [ ] All report-specific validation checks pass
- [ ] Sign-off recorded with date and validator

**Handoff Artifact:**
- Signed Report QC Protocol
- Output file(s) validated
- Version number confirmed

---

## Adding New Report Types

When a new report type needs documentation:

1. **Copy Template**: Start with `Report_Compendium_TEMPLATE.md`
2. **Fill Sections**: Complete all template sections
3. **Add QC Protocol**: Design validation checks specific to report
4. **Test QC**: Run QC protocol on actual output
5. **Version**: Assign version number matching Core Rulebook major version
6. **Register**: Add to this architecture document's inventory

---

## Benefits of This Architecture

| Benefit | Description |
|---------|-------------|
| **Atomic Handoffs** | One document = complete package for that stage |
| **Version Alignment** | QC embedded means methodology and validation can't drift |
| **Scalability** | New reports get own compendium without bloating Core |
| **Audit Trail** | Each stage has explicit sign-off |
| **Parallel Work** | Different reports can version independently |
| **Maintenance** | Update only affected compendium, not entire system |

---

## Migration Notes

### From V18 Monolithic Rulebook

The original `Final_Model_Rulebook_V18.md` (and V19.1) contained:
- Sections 1-4: Now in **Core Rulebook**
- Sections 5-6: Now in **Comprehensive Report Compendium**
- Section 7: Version history split across documents

QC validation was previously in separate `QC_Validation_Workbook_V18.xlsx`. Now:
- Core QC embedded in Core Rulebook Section 6
- Report QC embedded in each Report Compendium

---

*This architecture document serves as the map for the modular documentation system.*
