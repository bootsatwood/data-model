# Facility Count Discrepancy: Database vs. CRM

**Parent:** [[00_Index/_00_Index|Master Index]]
**Related:** [[00_Index/Project History#Facility Count Discrepancies|Project History]], [[08_Archive/By Topic/Data Model V18.1/Facility_Count_Discrepancy_Analysis_V18.pdf|V18 Analysis PDF]]

---

## The Problem

Brooke indicated that the CRM shows approximately **~1,200 facilities served**, but the database and MUO deck report **1,658 facilities served**. This creates confusion when stakeholders see different numbers in different systems.

**The gap: ~458 facilities**

---

## Root Cause: Campus Co-Location Tracking Methodology

The discrepancy is **not an error** — it reflects different counting methodologies between systems:

| System | Count | What It Represents |
|--------|-------|-------------------|
| **Database (Deck)** | 1,658 | Service contracts (each facility type tracked separately) |
| **CRM** | ~1,200 | Customer relationships (campuses consolidated) |

### Why the Difference Exists

Many senior living campuses operate **multiple facility types under single management** but at the same physical address. The database tracks each as a separate service contract because:

1. Each facility type has different clinical service requirements
2. Each generates separate billing/revenue
3. Each requires distinct provider coverage and scheduling
4. Regulatory reporting often requires facility-type-level detail

The CRM, by contrast, consolidates these into a single "customer relationship" since they share one decision-maker and one contract negotiation.

---

## The Data Behind the Gap

### Summary Statistics

| Metric | Count |
|--------|-------|
| **Total facility records served** | 1,658 |
| **Unique physical addresses** | 1,479 |
| **Campus co-location effect** | 179 additional records |
| | |
| **Corporate/MUO facility records** | 1,276 |
| **Unique MUO locations** | 1,136 |

**Key Finding:** When counting unique MUO locations (1,136), the number aligns closely with Brooke's ~1,200 CRM figure. The ~64 difference can be explained by timing, independent facilities, or minor data source variations.

### Campus Type Combinations Found

| Combination | # of Campuses |
|-------------|---------------|
| SNF + ALF | 73 |
| ALF + ALF (e.g., AL + MC) | 45 |
| ALF + ALF + SNF | 12 |
| ALF + ALF + ALF (e.g., AL + MC + IL) | 10 |
| ALF + ALF + ALF + ALF | 2 |
| ALF + SNF + SNF | 2 |
| 5+ facility types at one address | 2 |

---

## Specific Examples: Multi-Facility Campuses

### Example 1: Four Facility Types at One Address
**LIFECARE - Indianapolis, IN**  
Address: 8140 Township Line Rd

| # | Facility Name | Type |
|---|--------------|------|
| 1 | MARQUETTE | SNF |
| 2 | MARQUETTE MANOR ALF | ALF |
| 3 | MARQUETTE MANOR IL | ALF* |
| 4 | MARQUETTE MANOR SNF | ALF* |

*Note: IL and SNF units at ALF-licensed campuses may be classified as ALF in state licensing data but operate as distinct service units.

**CRM sees:** 1 customer relationship (Marquette Manor)  
**Database sees:** 4 service contracts

---

### Example 2: Four Distinct Care Levels
**Windsor Point - Fuquay-Varina, NC**  
Address: 1221 Broad St

| # | Facility Name | Care Level |
|---|--------------|------------|
| 1 | WINDSOR POINT AL | Assisted Living |
| 2 | WINDSOR POINT IN | Independent Living |
| 3 | WINDSOR POINT MC | Memory Care |
| 4 | WINDSOR POINT SNF | Skilled Nursing |

**CRM sees:** 1 customer relationship (Windsor Point)  
**Database sees:** 4 service contracts

---

### Example 3: Continuing Care Retirement Community (CCRC)
**Warm Hearth Village - Blacksburg, VA**  
Address: 2387 Warm Hearth Dr

| # | Facility Name | Type |
|---|--------------|------|
| 1 | WARM HEARTH - SHOWALTER CENTER | ALF |
| 2 | WARM HEARTH - THE ARBORS | ALF |
| 3 | WARM HEARTH - THE COVE (SNF/NF) | ALF |
| 4 | WARM HEARTH - THE WILLOWS | ALF |

**CRM sees:** 1 customer relationship (Warm Hearth Village)  
**Database sees:** 4 service contracts

---

### Example 4: Large MUO Campus (Trilogy Health Services)
**St. Andrews Health Campus - Batesville, IN**  
Address: 1400 Lammers Pike

| # | Facility Name | Type |
|---|--------------|------|
| 1 | ST ANDREWS HEALTH CAMPUS | SNF |
| 2 | ST ANDREWS HEALTH CAMPUS - BATESVILLE ALF | ALF |
| 3 | ST ANDREWS HEALTH CAMPUS - BATESVILLE SNF | ALF* |

*Secondary SNF unit tracked under ALF license

**CRM sees:** 1 customer relationship  
**Database sees:** 3 service contracts

---

### Example 5: Five Facility Types at One Address
**Carrington Place / Holston - Wytheville, VA**  
Address: 990 Holston Rd

| # | Facility Name | Type |
|---|--------------|------|
| 1 | CARRINGTON PLACE AT WYTHEVILLE - BIRDMONT CENTER | SNF |
| 2 | CARRINGTON WYTHEVILLE - ALF | ALF |
| 3 | CARRINGTON WYTHEVILLE - SNF/NF | ALF |
| 4 | HOLSTON HEALTH AND REHAB | SNF |
| 5 | HOLSTON SENIOR LIVING | ALF |

**CRM sees:** 1-2 customer relationships  
**Database sees:** 5 service contracts

---

## The Reconciliation Logic

```
Starting Point:                    1,658 service contracts

Less: Campus co-location effect     (179) facilities at shared addresses
                                   -------
Unique physical locations:         1,479

Less: Independent facilities        (343) non-MUO facilities  
                                   -------
Unique MUO locations:              1,136

≈ CRM relationship count:          ~1,200
```

The remaining ~64 gap between 1,136 and ~1,200 can be attributed to:
- Timing differences between data pulls
- Rounding in Brooke's estimate
- Minor classification differences
- Recent additions not yet in CRM

---

## How This Is Documented in the MUO Deck

### Slide 3 Footnote (Current State)
> ³ Based on Scenario 2 fee assumptions with service modifiers: MH at 50%, CCM at 30%, Shared Savings at 16.5%. Annualized assumes 12 months of service per facility. Includes $34M from independent facilities. **Contract count (1,658) includes campus-based communities with separate AL, MC, IL, and SNF units tracked individually; CRM reflects ~1,200 customer relationships.**

### Appendix Item #1 - Key Assumptions
> - Contract count (1,658) includes campus communities with separate Assisted Living, Memory Care, Independent Living, Skilled Nursing tracked individually
> - CRM relationship count (~1,200) differs due to campus consolidation

---

## Recommendations

1. **Accept the difference as methodology-driven** — both numbers are correct for their intended purpose

2. **Use consistent language:**
   - When discussing service contracts/clinical coverage: use 1,658
   - When discussing customer relationships/sales pipeline: use ~1,200
   - When discussing unique locations: use 1,479

3. **Add clarifying language** in any presentation where the number might cause confusion

4. **Future enhancement:** Add a "Campus_ID" field to the database that links co-located facilities, enabling easy toggling between contract-level and relationship-level views

---

## Source Documentation

This discrepancy was first identified and discussed in a call between Roian and Brooke in November 2025. Key excerpts:

> **Brooke:** "Because it's on my roster, it says that we only serve 58... We serve a good team, 15 [for Trilogy]."
>
> **Roian:** "I'm showing one as well [for Ohio]. I'm showing eight in Indiana."
>
> **Brooke:** "It's just the way it's broke out. Because I've got it broke out by ALF and SNF and you've got it combined. So that's the difference."

The call confirmed that GLR (General Ledger Report) counts ALF and SNF separately when co-located, while the database was consolidating them. This led to the reconciliation methodology documented above.

**Full transcript:** [[05_Conversations/Brooke_Call_Transcript_Nov_2025_Metro_Markets_Facility_Reconciliation.docx|Brooke Call Transcript (Nov 2025)]]

---

## Campus Structure Verification Protocol

When new facilities are added to the database (especially via bulk integration from external sources like NIC Maps), co-located records at the same address should be verified to confirm they are structured correctly — not flagged as errors, since the facility-by-service model is intentional.

### Verification Tests

| # | Test | What It Catches | Expected Result |
|---|------|----------------|-----------------|
| 1 | **Same-type at same address** (SNF+SNF or ALF+ALF) | Ownership/name changes that created a stale duplicate, or multi-service campuses with multiple ALF care levels (AL, MC, IL) | Common and expected. ALF+ALF pairs typically represent distinct care levels (e.g., Assisted Living + Memory Care). SNF+SNF may indicate a CMS ownership transition where the old CCN record persists. |
| 2 | **SNF+ALF with identical bed count AND identical service flags** | A row that was copied rather than sourced independently — unlikely that two different service types at the same campus would have the exact same beds and the exact same Integrated/PCP/MH flags | Rare. Review individually to confirm each row was sourced from its respective data pipeline (CMS for SNF, NIC Maps for ALF). |
| 3 | **SNF+ALF with distinct beds or flags** | Nothing — this is the correct structure | Pass. Different bed counts and/or service flags confirm each row represents a genuine separate service contract. |

### V21.1 Verification Results (Feb 2026)

| Metric | Count |
|--------|-------|
| Addresses with both SNF + ALF | 673 |
| **Pass** (distinct beds or flags) | 668 (99.3%) |
| **Review** (identical beds AND flags) | 5 |
| Same-type at same address (all states) | 948 |

5 carbon-copy pairs were initially flagged. After review:

| Address | SNF | ALF | Beds | Flags | Disposition |
|---------|-----|-----|------|-------|-------------|
| 8140 Township Line Rd, Indianapolis, IN | Marquette | Marquette Manor SNF | 57 | PCP | **Deleted.** Carbon copy confirmed against internal data (3 buildings, not 4). Row removed from V21.1. |
| 990 Holston Rd, Wytheville, VA | Holston Health and Rehab | Holston Senior Living | None | Integrated | **Valid.** Confirmed SNF + ALF campus, both served Integrated. Beds were missing due to Carrington Place acquisition — populated Feb 2026 (SNF 115/92, ALF 84/67). |
| 921 Old Newnan Rd, Carrollton, GA | Oaks - Carrollton SNF (PruittHealth) | Pruittplace-Carrollton (unknown) | 42 | None | Unserved. Low priority — review in future increment. |
| 1135 Gambier Rd, Mount Vernon, OH | ALS Mount Vernon (Lionstone) | Mount Vernon Health & Rehab (Independent) | 20 | None | Unserved. Different corporate names suggest independent sourcing. |
| 36855 Ridge Rd, Willoughby, OH | Ohio Living Breckenridge Village | Nason Center of Breckenridge Village | 72 | None | Unserved. Different corporate names suggest independent sourcing. |

**Result:** 1 deletion (Marquette carbon copy), 1 validated and corrected (Holston beds), 3 unserved low-priority pairs remaining. Database count: 26,268 → 26,267.

### When to Run This Protocol

- After any bulk facility integration (e.g., NIC Maps, state licensing data)
- After any version increment that adds records from a new data source
- Not needed for corporate name standardization or service flag corrections (those don't create new address overlaps)

---

## Data Sources

- **Database Version:** Combined_Database_FINAL_V21_1.xlsx (verification protocol), Combined_Database_FINAL_V20_0.xlsx (original discrepancy analysis)
- **Analysis Date:** December 2024 (discrepancy analysis), February 2026 (verification protocol)
- **Scope:** Six existing states for discrepancy analysis; all states for verification protocol
- **Filter:** Do_We_Serve = 'Yes' (discrepancy analysis); all records (verification protocol)

---

*Document created to resolve confusion around facility count discrepancies between the MUO deck and CRM system. Campus Structure Verification Protocol added February 2026 after V21 expansion-state integration.*
