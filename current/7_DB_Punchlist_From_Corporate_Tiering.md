# DB Punchlist — Observations from Corporate Tiering Analysis (V23)

**Created:** 2026-03-07
**Source:** MUO Corporate Scoring V23 analysis, Brooke walkthrough transcript, build script observations
**Status:** All items are NEW — identified during tiering, not yet applied to DB

---

## Entity Naming Issues

### 1. American Healthcare LLC → Heritage Hall
- **DB name:** "AMERICAN HEALTHCARE, LLC"
- **Field name:** Heritage Hall (used by Tom, Brooke, original workbook, MUO Data)
- **Impact:** Entity is unrecognizable to BD team under its corporate name
- **Recommendation:** Add Heritage Hall as display alias or rename to Heritage Hall with corporate name as secondary field

### 2. Cedarhurst — Inconsistent Facility Naming
- **DB has 4+ naming patterns:** Cedar Creek, Cedar Hurst, Cedar Ridge, Cedarhurst
- **All are the same corporate entity:** Cedarhurst Senior Living
- **V22.7 fix:** Corrected "SENOR" → "SENIOR" typo and removed 3 dupes, but naming variants remain
- **Impact:** Difficult to identify full Cedarhurst portfolio at a glance; campus counts may be wrong
- **Recommendation:** Normalize all variants to "CEDARHURST SENIOR LIVING"

### 3. Spring Harbor → Spring Arbor Management (Misspelling)
- **1 GA row** coded as "Spring Harbor" instead of "Spring Arbor Management"
- **Out of footprint** (GA), so no scoring impact, but still a data quality issue
- **Recommendation:** Rename to "SPRING ARBOR MANAGEMENT"

### 4. Avardis — Legacy Chain Name Still in DB
- **Some rows still carry:** "CONSULATE HEALTH CARE/INDEPENDENCE LIVING CENTERS/NSPIRE HEALTHCARE/RAYDIANT HEALTH CARE"
- **V22.5 fix:** Corrected "AVARDIS HEALTH" → "AVARDIS" (4 rows), but the long legacy name persists on other rows
- **MUO Data notes:** "pulled as old name Consulate"
- **Recommendation:** Rename all remaining Consulate/Nspire/Raydiant rows to "AVARDIS"

---

## Missing / Miscoded Facilities

### 5. Spring Arbor — ~9 Missing Footprint Facilities
- **Brooke counted ~24 properties** in footprint during walkthrough
- **DB has only 15 FP rows** (after V22.7 dedup from 21 → 16)
- **Gap:** ~9 facilities missing from DB
- **Impact:** Suppresses both campus count (ER score) and revenue (RP score)
- **Recommendation:** Cross-reference Spring Arbor website/state licensing against DB to find missing facilities

### 6. Greencroft — NC Facility Verification Needed
- **Oak Grove Healthcare Center** in Rutherfordton, NC is coded as Greencroft in DB
- **Not on Greencroft's website** — may be an unaffiliated facility that shares the name
- **Impact if miscoded:** Greencroft drops from 9 to 8 qualifying campuses (still passes MUO gate, no tier change)
- **Recommendation:** Verify ownership via state licensing records; if not Greencroft, reassign corporate name

### 7. Atrium Health — Wilkesboro Swing Bed
- **Wilkes Regional Medical Center** — 10-bed SNF unit in Wilkesboro, NC
- **Excluded by 15-bed minimum rule** in scoring, but still in DB
- **Not on Atrium's senior living website** — likely a hospital swing bed, not a standalone SNF
- **Brooke flagged this** during walkthrough
- **Recommendation:** Consider removing from DB entirely rather than relying on rule-based exclusion

---

## Barrier Flags

### 8. Four New T5 Barriers Identified from DB
Identified during V23 corporate scoring from service flags and Tom's Notes. These entities have hard barriers to doing business and are classified as T5 in the tiering model. If the DB has a barrier field, these should be formalized:

| Entity | Barrier Type | Severity |
|--------|-------------|----------|
| Cardon & Associates | Own provider group | 91% of facilities |
| Eastern Healthcare Group | Termination risk | 100% of facilities |
| Clearview | Alliance + own provider group | 38% of facilities |
| Pavilion Healthcare | Alliance + own provider group | 29% of facilities |

**Recommendation:** Add or update a `Barrier_Flag` field on these corporate entities in the DB

---

## Address & Campus Normalization

### 9. Street Name Spelling Variations Inflate Campus Counts
- **Problem:** Co-located SNF + ALF at the same physical address count as separate campuses because of format differences
- **Examples:** "12019 Verhoeff Dr" vs "12019 Verhoeff Drive", "100 Main Street" vs "100 Main St", "Boulevard" vs "Blvd"
- **Current workaround:** Scoring scripts use `normalize_address()` and `extract_street_number()` functions to collapse variants
- **Impact:** Any downstream consumer (Monday.com board, BD reports, Finance workbook) that doesn't run the normalization logic will overcount campuses
- **Recommendation:** Standardize address formatting in the DB itself — pick one convention (abbreviations or full words) and normalize all rows

### 10. Co-Located Facilities Need a Campus/Site ID
- **Problem:** SNF + ALF + MC at the same campus appear as separate facility rows with no linkage
- **Current workaround:** Scripts derive campus keys by matching street numbers at runtime
- **Impact:** Every analysis that needs campus-level rollups (ER scoring, facility counts, Monday.com board) must re-derive the campus key independently
- **Recommendation:** Add a `Campus_ID` or `Site_ID` field to the DB so co-located facilities are permanently linked. Compute once, reuse everywhere.

### 11. GPS Coordinate Proximity Matching
- **Problem:** Buildings on the same physical campus sometimes have legitimately different street addresses (e.g., SNF at 100 Main St, ALF at 102 Main St, or buildings facing different streets)
- **Street-number matching misses these** because the addresses are technically different
- **Recommendation:** Geocode DB addresses (or pull lat/long from CMS/state licensing data if available) and use a distance threshold (~0.1 miles) to identify co-located facilities that address matching can't catch. Results feed into the Campus_ID field above.

---

## Summary

| # | Category | Item | Priority |
|---|----------|------|----------|
| 1 | Naming | Heritage Hall alias | Medium |
| 2 | Naming | Cedarhurst variants | Medium |
| 3 | Naming | Spring Harbor typo | Low |
| 4 | Naming | Avardis legacy name | Medium |
| 5 | Missing | Spring Arbor ~9 FP gaps | High |
| 6 | Miscoded | Greencroft NC verification | Medium |
| 7 | Miscoded | Atrium swing bed removal | Low |
| 8 | Barriers | 4 new T5 barrier flags | Medium |
| 9 | Address | Street name normalization | High |
| 10 | Address | Campus/Site ID field | High |
| 11 | Address | GPS proximity matching | Medium |
