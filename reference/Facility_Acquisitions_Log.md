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

## Owensboro, KY — Heritage Place → Morning Pointe Senior Living

**Date of acquisition:** September 2024
**Date identified in DB review:** 2026-03-27 (Pair 11), updated to current procedure standard 2026-04-06 (Cluster 6)
**Address:** 3362 Buckland Sq, Owensboro, KY 42301

**Prior operator:** Encore Communities (Pacific Northwest-based, ~43 communities in IL, WI, MN, OH, MI)
**New operator:** Morning Pointe Senior Living (Chattanooga TN, founded 1997 by Greg Vital / Franklin Farrow)
**Transaction:** Acquisition + $2.5M renovation. Grand opening as "Morning Pointe of Owensboro" Aug 14 2025. Deficiency-free KY licensure survey. ED: Karleigh Roby.

**Removed (1 row):**

| Old Row | Facility Name | Corp | Source_Type | Total_Beds | Served |
|---------|--------------|------|-------------|------------|--------|
| 5934 | MORNING POINTE OF OWENSBORO | GENESIS | ALF | 66 | No |

**Notes:**
- Row 5934 carried GENESIS as corporate name — NIC MAP misattribution. Genesis never operated this facility. NIC MAP inherited stale assignment from Encore/Heritage Place period or pure data error. NIC MAP export Nov 2025 still showed Genesis 14 months post-acquisition.
- NIC MAP property name still "Heritage Place Assisted Living Center" as of Nov 2025 export.
- NIC MAP Owner = "Owensboro Medical Invtrs LLC" — correctly maps to IHP/Morning Pointe PropCo pattern ("[City] Medical Investors LLC").
- Kept row 5928 (MORNING POINTE OWENSBORO, served, GLR-sourced) with beds 14→66.

**Sources:** morningpointe.com/press/morning-pointe-senior-living-expands-to-western-kentucky/, Owensboro Times (Sep 2024), NIC MAP (Nov 2025), GLR (Mar 2026), KY CHFS (not listed in Feb 2026 directory — gap).

---

## Edmonton, KY — Metcalfe Health Care Center → Topaz Healthcare

**Date of acquisition:** September 2025 (sale approved by Metcalfe County magistrates, $11,150,000)
**Date identified in DB review:** 2026-04-07 (Cluster 8 + Topaz re-investigation)
**Address:** 701 Skyline Dr, Edmonton, KY 42129 (CCN 185217)

**Prior operator:** Wells Health Services INC (managing entity since Jan 2008, under nonprofit ownership — The United Methodist Retirement Homes? / county-owned)
**New operator:** Topaz Healthcare (Topaz Financial Services LLC, fka Sapphire Care Group, Landa/Platschek/Chafetz network, Brooklyn NY)
**Transaction:** Sale for $11.15M. Four bids received. Topaz (corrected to "Topaz Corporation" by County Attorney) awarded unanimously.

**CMS/ProPublica lag:** As of 2026-04-07, ProPublica still shows Wells Health Services INC as managing entity. KY DMS directory (Feb 2026) shows no external Corporation. Expected — CMS lags 6-12 months behind actual ownership changes. Same pattern as Hill Valley CHOWs.

**DB action:** Rows 5924 (AL) and 5925 (SNF) recode to TOPAZ HEALTHCARE.

**Sources:** jpinews.com (Sep 16 2025): "Metcalfe Healthcare Center Sold: A Fresh Chapter Begins"

---

*This log supplements the Combined Database by preserving lineage for deleted facilities. See `1_Combined_Database.md` for the active database companion.*
