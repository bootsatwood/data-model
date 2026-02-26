# START_HERE.md
## Eventus Healthcare Economic Model V11.0

**Version**: 11.0  
**Date**: November 18, 2025  
**Status**: PRODUCTION READY

---

## QUICK REFERENCE

### Key Metrics (V11.0 - Scenario 1)

| Metric | Value |
|--------|-------|
| Total Facilities | 17,434 |
| Facilities We Serve | 1,743 |
| Current Revenue | $177,684,185 |
| Integration Revenue | $147,384,026 |
| New Business Revenue | $5,115,910,599 |
| **Total Potential** | **$5,263,294,625** |

### Critical Validation Points

| Check | Expected Value |
|-------|----------------|
| ALF Current Revenue | $83,991,652 |
| SNF Current Revenue | $93,692,533 |
| Corporate Barrier Facilities | 1,034 |
| **Integrated Barrier Facilities** | **786** |
| Served w/ Integrated Barrier | 306 |
| Not Served w/ Integrated Barrier | 480 |

---

## V11 KEY CHANGE: Integrated Barrier Propagation

V11 implements corporate-level propagation of operational barriers:

- **110 facility-specific barriers** → **786 facilities** (32 parent companies)
- **21.5% of Integration Revenue blocked** (~$40M in S1)
- **1.0% of New Business Revenue blocked** (~$50M in S1)

### Calculation Rule

Integrated Barriers block ALL potential revenue:
- Current Revenue: **UNCHANGED** (barriers don't affect existing business)
- Integration Revenue: **$0** (blocked)
- New Business Revenue: **$0** (blocked)

### CCH Healthcare Exception

Ohio facilities only receive Reputation barrier (20 facilities).  
North Carolina facilities have no barrier (20 facilities).

---

## FILE INVENTORY

### Core Data Files

| File | Purpose |
|------|---------|
| Combined_Database_FINAL_V11.xlsx | Source database with barrier propagation |
| Economic_Model_Scenario_1_Combined_V11.xlsx | Conservative growth |
| Economic_Model_Scenario_2_Combined_V11.xlsx | Market expansion (+10%) |
| Economic_Model_Scenario_3_Combined_V11.xlsx | Premium services (+20%) |

### Logs & Documentation

| File | Purpose |
|------|---------|
| V11_Propagation_Changes_Log.xlsx | Detailed log of 676 propagated barriers |
| V10_to_V11_Change_Compendium.md | Complete change documentation |
| Final_Model_Rulebook_V11.md | Authoritative reference - READ FIRST |
| START_HERE_V11.md | This file |

---

## GOVERNANCE PROTOCOLS

### Before Any Work

1. **Read Final_Model_Rulebook_V11.md** - Understand barrier systems
2. **Review V10_to_V11_Change_Compendium.md** - Understand propagation rules
3. **Get written authorization** - Any barrier or fee changes require approval

### Barrier Change Requirements

**MANDATORY for any barrier modification:**
- Written authorization from project owner
- Impact analysis on revenue calculations
- Update compendium with change rationale
- Regenerate all scenario workbooks

### Version Control Rules

**Numbering Protocol:**
- Minor fixes: V11.0 → V11.1 → V11.2
- Major changes: V11.x → V12.0

**Critical Rules:**
- ✗ NEVER overwrite existing files
- ✗ NEVER reuse version numbers
- ✓ ALWAYS increment version
- ✓ ALWAYS document changes in compendium

---

## QC CHECKLIST

Before any delivery, verify:

- [ ] ALF Current Revenue = $83,991,652
- [ ] SNF Current Revenue = $93,692,533
- [ ] Total facilities = 17,434
- [ ] Corporate Barrier facilities = 1,034
- [ ] Integrated Barrier facilities = 786
- [ ] CCH Ohio barriers = 20
- [ ] CCH NC barriers = 0
- [ ] Files named with correct version
- [ ] Change compendium updated

---

## BARRIER SYSTEMS OVERVIEW

### Two Complementary Systems

| System | Facilities | Effect |
|--------|------------|--------|
| Corporate Barrier | 1,034 | Blocks New Business only |
| Integrated Barrier | 786 | Blocks ALL potential (Integration + New Biz) |

### Integrated Barrier Categories

| Category | Facilities |
|----------|------------|
| Own Provider Group | 181 |
| MH Only Opportunity | 145 |
| Competitor Agreement | 115 |
| Alliance, Own Provider Group | 113 |
| Reputation | 97 |
| Alliance | 87 |
| Termination Risk | 29 |
| Alliance, MH Only Opportunity | 19 |

---

## TROUBLESHOOTING

### Issue: Integration Revenue too high

**Cause**: Integrated Barriers not applied correctly  
**Solution**: Verify facilities with `Integrated_Barrier_Category` have $0 Integration Revenue

### Issue: Barrier count mismatch

**Cause**: Propagation incomplete or CCH exception incorrect  
**Solution**: 
1. Check V11_Propagation_Changes_Log.xlsx
2. Verify CCH Ohio = 20, CCH NC = 0

### Issue: Current Revenue different from V10

**Cause**: Source data update (expected)  
**Solution**: V11 source has 1 SNF with both PCP+MH flags; difference is $174,650

---

## VERSION HISTORY

| Version | Date | Key Changes |
|---------|------|-------------|
| **V11.0** | Nov 18, 2025 | Integrated Barrier propagation (786 facilities), CCH Ohio exception |
| V10.0 | Nov 2025 | ALF fees corrected, QC validation added |
| V9.0 | Nov 2025 | Entity barriers, SNF PCP $2,600 |
| V8.0 | Nov 2025 | Baseline version |

---

## SUPPORT

- **Barrier rules**: See Final_Model_Rulebook_V11.md Section 3
- **Propagation details**: See V10_to_V11_Change_Compendium.md
- **Fee questions**: See Rulebook Section 1
- **Change log**: See V11_Propagation_Changes_Log.xlsx

---

**END OF START_HERE**
