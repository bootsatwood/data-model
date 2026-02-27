# Proposal: Multi-Service Facility Classification QC Review

**Date:** February 27, 2026
**Author:** Roian Atwood
**Status:** DEFERRED — Captured for future consideration
**Parent:** [[1_Combined_Database|Combined Database Companion]]

---

## Background

During the original ALF integration (October–November 2025), deduplication work revealed that many facilities operate multiple service types at a single address. The `ALFs_We_Serve` source file contained a rich Facility Type field with 17+ distinct values:

| Facility Type | Count | Notes |
|---------------|-------|-------|
| AL | 494 | Pure assisted living |
| SNF | 384 | Pure skilled nursing |
| SNFMD | 184 | SNF with medical director |
| AL/MC | 53 | Assisted living + memory care |
| IL | 32 | Independent living |
| MC | 32 | Pure memory care |
| AL/SNF | 23 | Combined AL and SNF |
| AL/SNF MD | 11 | Combined with medical director |
| AL/MC/IL | 6 | Three service types |
| AL/SNF/NF | 5 | AL + SNF + nursing facility |
| AL/Clinic | 4 | AL with clinic |
| SNF/NF | 4 | SNF + nursing facility |
| Personal Care Home | 3 | Distinct care type |
| CCRC | 2 | Continuing care retirement community |
| Other | 2 | Uncategorized |

*(Source: `SNF_Cleanse.docx` process notes, from `ALFs_We_Serve_Clean_v4.xlsx`)*

## Current State

The Combined Database (V21.1) classifies every facility as either **Source_Type = "SNF"** or **Source_Type = "ALF"**. Mixed-type facilities are handled by two mechanisms:

1. **Campus Sister Facility Rule** (V21, Key Decision #6): When an ALF and SNF share an address or are within 0.3 miles, they are treated as **separate rows** with different revenue computations (SNF: $4,583.50/bed/yr; ALF: $3,699.50/bed/yr).

2. **Source_Type flattening** (V21, Key Decision #1): All facilities with AL units, MC units, or both are classified as "ALF" regardless of subtype. The original NIC Maps distinction between AL-only, AL+MC, and MC-only was collapsed.

## The Lingering Issue

Not all multi-service combinations were fully decoded during the original dedup work. The campus sister facility rule handles the clean case (separate buildings at the same campus), but there are unresolved scenarios:

- **Single building, multiple services:** A facility that is genuinely one building offering AL + MC + IL. Should this be one row or multiple rows? Currently it's one row typed as "ALF."
- **Hybridized computation:** If a facility offers both SNF and ALF services in one building (AL/SNF type), neither the pure SNF nor the pure ALF revenue formula is accurate. The database doesn't have a hybridized computation path.
- **MC-only facilities:** 393 facilities in V21 are MC-only but classified as ALF. Memory care may warrant different revenue assumptions than standard assisted living.
- **CCRC / IL facilities:** Continuing care retirement communities and independent living facilities have different service models entirely. They're currently swept into ALF.

## Proposed Future Work

1. **Audit the V21.1 database** for facilities at shared addresses where both an SNF and ALF row exist. Validate that each pair represents genuinely separate buildings (campus sisters) vs. a single multi-service facility that was split into two rows.

2. **Cross-reference against the original Facility Type field** from the ALFs_We_Serve source. For the 23 AL/SNF, 11 AL/SNF MD, and 5 AL/SNF/NF facilities — are these currently represented as one row or two? If one, is the revenue computation correct?

3. **Evaluate whether Source_Type needs a third value** (e.g., "Mixed" or "CCRC") or whether a secondary flag (MC_Flag, IL_Flag) would better capture the service mix without changing the primary classification.

4. **Quantify the revenue impact.** How many facilities would be affected by a reclassification? Is this a material correction or an edge case?

## Relationship to Other Work

- The **True Duplicates Review** (`Archive/True_Duplicates_Review.xlsx`, 116 rows / 58 pairs) documents the original dedup edge cases. This proposal extends that work.
- The **V21 ALF Enhancement** campus sister facility rule (75 facilities) was the first systematic treatment of multi-service addresses. This proposal addresses the cases that rule doesn't cover.
- The **CMS Source Data Cross-Reference** proposal could provide additional facility type detail via the CMS Provider Type field.

---

*Last updated: 2026-02-27*
