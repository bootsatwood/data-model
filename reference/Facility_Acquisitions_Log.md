# Facility Acquisitions Log

Records of facilities removed from the Combined Database due to ownership changes (acquisitions, rebrands). The acquiring entity's record is the keeper; the old record is deleted to prevent it appearing as a false sales opportunity.

---

## Wytheville, VA — Carrington Place → Hill Valley Healthcare

**Date identified:** Feb 2026 (Facebook post from Oct 16, 2025 confirms transition)
**Address:** 990 Holston Rd, Wytheville, VA 24382

**Removed (3 rows):**

| Old Row | Facility Name | Source_Type | Total_Beds | Census | Service Flag |
|---------|--------------|-------------|------------|--------|-------------|
| 16213 | Carrington Place at Wytheville - Birdmont Center | SNF | 137 | 97.5 | MH |
| 16215 | Carrington Wytheville ALF | ALF | 74 | 59 | Integrated |
| 16216 | Carrington Wytheville-SNF/NF | ALF | 104 | 83 | MH |

**Kept (2 rows — Hill Valley Healthcare, Corporate):**

| Row | Facility Name | Source_Type | Total_Beds | Census | Service Flag |
|-----|--------------|-------------|------------|--------|-------------|
| 20943→20940 | Holston Health and Rehab | SNF | — | 101 | Integrated |
| 20944→20941 | Holston Senior Living | ALF | — | 75 | Integrated |

**Notes:**
- All five records shared the same address (990 Holston Rd)
- Carrington rows were Independent; Holston rows are Corporate (Hill Valley Healthcare)
- Holston rows are missing `Total_Beds` — Carrington had 137 (SNF) and 74+104 (ALF). These should be reconciled when a Facility Profile export is available.
- Row 16216 was tagged Source_Type=ALF but named "SNF/NF" — a data quality issue that became moot with deletion
- The Dec 2025 dedup exercise deactivated rows 16213 and 16215 with DUPLICATE-DEACTIVATED barriers but missed row 16216 entirely

---

*This log supplements the Combined Database by preserving lineage for deleted facilities. See `1_Combined_Database.md` for the active database companion.*
