# SNF Cleanse

**Author:** Roian Atwood
**Date:** October–November 2025
**Type:** Working process notes — original data cleansing and ALF integration

> [!note] Future cleanup
> This document preserves original working notes from the initial database build. A future naming convention pass may rename/consolidate foundation docs into a cleaner structure (e.g., "Process Notes — Steps 1–3" or similar).

---

## SNF File Cleansing (Steps 1–6)

### Manual Steps (Roian)

- **Step 1** – Removed columns Z–DA (extra data columns)
- **Step 2** – Removed columns M–R (Finance columns)
- **Step 3** – Removed row 14,724
- **Step 4** – Added a Macro Type column in Column A

**FILE:** `SNF Database with Revenue Q4 2025_V2`

### Claude/ChatGPT-Assisted Steps

**Step 5 — File Lineage:**

| Version | File Name | Purpose | Status |
|---------|-----------|---------|--------|
| 1 — Original Source | `SNF Database with Revenue Q4 2025_V2.xlsx` | Raw working file with main sheet + 6 state tabs (IN, KY, NC, OH, SC, VA) | Keep (Authoritative Source) |
| 2 — Intermediary Merge | `SNF_Master_WithEnhancements_BH_ServeFix.xlsx` | First merged master that correctly pulled "Do we serve" values (after broadening "serve" detection). Used to fix missing VA flags. | Superseded |
| 3 — Clean Uniform | `SNF_Master_Final_Uniform_v1.xlsx` | Cleaned version of v2 — removed "NaN," converted "X/Y/TRUE" → "Yes." Used for initial QC. | Superseded by v2 |
| 4 — Corrected Final | `SNF_Master_Final_Uniform_v2.xlsx` | Final master merge with both "serve" and "integrated" broadened detection, plus full uniform cleanup. | Active working master |

**Step 6 — Content Integrity Summary:**

| Component | Status | Source / Method |
|-----------|--------|-----------------|
| Service Flags (Integrated / PCP / BH) | Fully restored and validated | Derived from the original 6-state source tabs — manual flags preserved and rechecked via the Serve-but-No-Flag diagnostic |
| "Do we serve" Logic | Confirmed consistent | Field harmonized under merge rule (any column with "serve") |
| Barrier Field | Fully restored (state-specific) | Pulled from correct state columns: SC, VA, KY, OH → Col AA; IN → Col U; NC → Col AA (Barrier) |
| Corporate Entity Fields | Unchanged (previously validated) | Chain Name, Legal Business Name, Ownership Type remain consistent from the uniform model |
| Operational Market Tabs (6 states) | Integrated | All six states (SC, VA, KY, IN, OH, NC) now have complete barrier + flag data |
| Audit Trail | Included | "Barrier_Overwrite_Audit" tab lists every facility where data was restored or overwritten (68 rows total) |

We found some missing flags in the file so Brooke was able to go in and update.

---

## ALF File — "In States We Serve"

### Step 1 — Created a Master Tab

### Step 2 — Bring over NC

Changed the naming conventions. They had:
- Name of Licensee Legal Name
- DBA Name

And the SNF file has three names:
- Provider Name
- Legal Business Name
- Chain Name

So I matched them as such — I changed the heads of the ALF file to read:
- DBA Name → Provider Name
- Name of Licensee Legal Name → Legal Business Name
- [NONE] → [added] Chain Name

And then I made my own observations on the Chain Names and grouped them like with like to the best of my ability — many small operators.

### Step 3 — Bring over KY

KY had:
- Company
- Parent Organization

Mapped as:
- Company → Provider Name
- Parent Organization → Chain Name

AND:
- Changed "AL bed Count" to "Bed Count" to match
- Bed count numbers were weird, many options in the workbook (column headers to choose from)
- Noticed that a significant number of the facilities did not have a bed count number
- **Will need to set a rule to use 35 average**

### Ohio edits

- Noticed that a significant number of the facilities did not have a bed count number
- Fairly simple transfer, we didn't have a lot of data to parse out, a single name field
- This should be gone through more extensively with a Chain entity type of analysis. I did not hand code like I did in NC

### Indiana

There are two bed counts, one for AL and the other for SNFs. The number of beds in SNFs was significant, so it made me wonder if these were true ALFs or if it was a combo of both SNFs and ALFs, not sure.

After all the states were combined to a single file there were actually several locations that were identified that were outside of the service area.

---

## ALFs We Serve — Service Volume Observation

On the ALFs we serve file, there is a column called "G's primary account care ALF volume" and "high psychiatric volume" which doesn't necessarily map well to our general architecture, but we've assumed that primary care is PCP and psychiatric is mental health or behavioral health.

The interesting thing is it's numeric — it actually gives a percentage of the total beds. Well, actually that's not true — it shows how much service we provide. You don't total them up, but it shows how much saturation for each of the different services that we provide.

**This is interesting and different than the other report.** I wonder if it's a different system because it doesn't have the CMS code the same way that the SNF database does. But it's worth noting that this level of detail is actually quite useful because there's no better way to understand the size of prize than understanding exactly how many residents you could potentially have. It's essentially a service-by-bed level of detail — a level of detail greater than the SNFs.

---

## Facility Type Distribution

There was a code to sort on facility type and include ALF and SNF both, so I did a customized screen and this is what it revealed (from `ALFs_We_Serve_Clean_v4.xlsx`):

| Facility Type | Count |
|---------------|-------|
| AL | 494 |
| SNF | 384 |
| SNFMD | 184 |
| AL/MC | 53 |
| IL | 32 |
| MC | 32 |
| AL/SNF | 23 |
| (blank) | 12 |
| AL/SNF MD | 11 |
| AL/MC/IL | 6 |
| AL/SNF/NF | 5 |
| AL/Clinic | 4 |
| SNF/NF | 4 |
| Personal Care Home | 3 |
| Other | 2 |
| CCRC | 2 |
| CRCC | 1 |
| ALF | 1 |
| **Total** | **1,243** |

---

## ALF–SNF Dedup

Bumped the ALF file against the SNF file to determine overlap. Ran a query, then manually reviewed a small group still in question and coded them duplicate or not duplicate. Revealed about eight more in the population. By removing close to 600 records from the merge, that prevents data model contamination.

### Results

| Metric | Count |
|--------|-------|
| Rows before cleanup | 1,253 |
| Duplicate rows removed | 598 |
| Rows remaining (valid ALFs) | 655 |

### Key Changes
- City → City/Town (header standardized to match SNF schema)
- All rows marked "DUP" or detected via overlap audit (exact + fuzzy) have been removed
- File is now clean, symmetrical with the SNF master, and ready for Phase 3 reconciliation

**Outcome file:** `ALFs_We_Serve_Clean_v5.xlsx`

### ALF Merger — Final File

`ALF_Master_Combined_v2B_CorpTier_20251104.xlsx`

---

*Converted from `SNF Cleanse.docx`. Original working notes preserved as-is.*
*Last updated: 2026-02-27*
