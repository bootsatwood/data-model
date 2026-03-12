# RS Score Reconciliation: V20 (Brooke) vs V23 (Tom)

**Date:** 2026-03-11
**Analyst:** Roian Atwood
**Scope:** Relationship Score (RS) dimension — comparing two assessor baselines

---

## Background

In V23, the Relationship Score (RS) was replaced wholesale with Tom's shared savings / ACO engagement assessment. The prior V20 RS reflected Brooke's qualitative scoring from her original tiering exercise. This replacement was done without a side-by-side reconciliation.

This analysis compares both assessments and evaluates tier impact.

### Scoring Methodology

| Version | Assessor | Basis |
|---------|----------|-------|
| V20 | Brooke | BD relationship knowledge — familiarity, strategic potential, existing engagement |
| V23 | Tom | Field intel — shared savings participation, ACO interest, active conversations |

**RS weight in the model:** x3 (each RS point = 3 points on total score)

**Tier boundaries:** T1 >= 55, T2 = 35-54, T3 < 35

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Entities compared | 50 |
| Same score | 24 |
| Tom scored higher | 6 |
| Tom scored lower | 20 |
| Big divergence (delta >= 2) | 11 |

**Pattern:** Tom systematically scored lower than Brooke. Of the 26 disagreements, 20 went in Tom's direction (lower), only 6 higher.

---

## Big Divergences (|Delta| >= 2)

These are the entities where Brooke and Tom fundamentally disagree on relationship strength.

### Tom Scored Lower (10 entities)

| Entity | V20 Tier | Brooke RS | Tom RS | Delta | Tom's Notes |
|--------|----------|-----------|--------|-------|-------------|
| Otterbein Senior Life | T1 | 5 | 1 | -4 | Do not really know well |
| Arbors | T2 | 4 | 1 | -3 | Do not really know well |
| Pavilion Healthcare | T1 | 4 | 1 | -3 | Do not really know well |
| Saber Healthcare Group | T1 | 5 | 2 | -3 | Not very focused, not working |
| AOM Healthcare | T2 | 3 | 1 | -2 | *(gap entity — no Tom notes)* |
| Aperion Care | T2 | 3 | 1 | -2 | *(gap entity — no Tom notes)* |
| Majestic Care | T1 | 5 | 3 | -2 | Expressed interest but has not gone anywhere |
| Ohio Living Communities | T2 | 3 | 1 | -2 | *(gap entity — no Tom notes)* |
| Priority | T2 | 3 | 1 | -2 | Do not really know well |
| Sunrise Senior Living | T1 | 3 | 1 | -2 | *(gap entity — no Tom notes)* |

### Tom Scored Higher (1 entity)

| Entity | V20 Tier | Brooke RS | Tom RS | Delta | Tom's Notes |
|--------|----------|-----------|--------|-------|-------------|
| Clearview | T2 | 1 | 3 | +2 | In process of partnering with Telos |

### Interpretation

- **4 of 11 divergences are gap entities** (AOM, Aperion, Ohio Living, Sunrise) where Tom had no notes and defaulted to 1. These may not reflect his actual assessment.
- **Otterbein (-4), Arbors (-3), Pavilion (-3):** Tom annotated all three as "do not really know well" — suggesting Tom's blind spots rather than informed downgrades.
- **Saber (-3):** A genuine disagreement. Brooke scored 5 (top tier MUO, 120 facilities); Tom says "not very focused, not working."
- **Majestic Care (-2):** Brooke scored 5; Tom says "expressed interest but has not gone anywhere." Both could be right — strategic priority vs current engagement status.

---

## Tier Impact Analysis

If Brooke's RS replaced Tom's RS in the V23 model (keeping all other dimensions unchanged):

### Tier Shifts

| Entity | Current Tier | Current Score | Tom RS | Brooke RS | Score Impact | New Score | New Tier |
|--------|-------------|---------------|--------|-----------|-------------|-----------|----------|
| **TerraBella Senior Living** | **T2** | **52** | **2** | **3** | **+3** | **55** | **T1** |

**Only 1 entity changes tier.** TerraBella sits right on the T1/T2 boundary (52 → 55).

### Notable Within-Tier Score Shifts (no tier change)

| Entity | Tier | Current Score | Impact | New Score | Notes |
|--------|------|---------------|--------|-----------|-------|
| Otterbein Senior Life | T1 | 60 | +12 | 72 | Biggest point swing |
| Saber Healthcare Group | T1 | 79 | +9 | 88 | |
| Arbors | T2 | 43 | +9 | 52 | Close to T1 boundary but doesn't cross |
| Majestic Care | T1 | 81 | +6 | 87 | |
| AOM Healthcare | T2 | 42 | +6 | 48 | |
| Ohio Living Communities | T2 | 37 | +6 | 43 | |
| Priority | T2 | 36 | +6 | 42 | |
| Sunrise Senior Living | T1 | 57 | +6 | 63 | |

### Entities Where Brooke's Score Would Lower the V23 Total

| Entity | Tier | Current Score | Impact | New Score |
|--------|------|---------------|--------|-----------|
| Infinity Healthcare Consulting | T1 | 69 | -3 | 66 |
| Liberty | T1 | 73 | -3 | 70 |
| YAD | T2 | 46 | -3 | 43 |

None of these downgrades cross a tier boundary.

---

## Full Side-by-Side Comparison

| Entity | V20 Tier | Brooke RS | Tom RS | Delta | Tom's Notes |
|--------|----------|-----------|--------|-------|-------------|
| Otterbein Senior Life | T1 | 5 | 1 | -4 | Do not really know well |
| Arbors | T2 | 4 | 1 | -3 | Do not really know well |
| Pavilion Healthcare | T1 | 4 | 1 | -3 | Do not really know well |
| Saber Healthcare Group | T1 | 5 | 2 | -3 | Not very focused, not working |
| AOM Healthcare | T2 | 3 | 1 | *(gap entity)* |
| Aperion Care | T2 | 3 | 1 | *(gap entity)* |
| Clearview | T2 | 1 | 3 | +2 | In process of partnering with Telos |
| Majestic Care | T1 | 5 | 3 | -2 | Expressed interest but has not gone anywhere |
| Ohio Living Communities | T2 | 3 | 1 | *(gap entity)* |
| Priority | T2 | 3 | 1 | -2 | Do not really know well |
| Sunrise Senior Living | T1 | 3 | 1 | *(gap entity)* |
| ALG | T1 | 3 | 2 | -1 | Presented SS, Charlie not interested |
| Avardis | T1 | 3 | 2 | -1 | Do not really know well, do not want SS |
| CCH Healthcare | T1 | 3 | 2 | -1 | Talk to them defensively |
| Caring Place Healthcare | T3 | 1 | 2 | +1 | Psych only, will not do PC |
| Infinity Healthcare Consulting | T1 | 1 | 2 | +1 | Getting nowhere |
| JAG | T2 | 3 | 2 | -1 | Not much growth opp |
| Kissito Healthcare | T2 | 1 | 2 | +1 | COO not interested in SS |
| Liberty | T1 | 3 | 4 | +1 | Gave them proposal in RFP, Liberty Advantage ISNP |
| Lutheran Services Carolinas | T2 | 5 | 4 | -1 | Verbal commitment for SS |
| Morning Pointe Senior Living | T2 | 3 | 2 | -1 | Not a great fit |
| Peak Resources | T2 | 3 | 2 | -1 | Not responsive or interested in SS |
| Pruitt Health | T1 | 4 | 3 | -1 | Getting more PC, focused on own ISNP |
| Sanstone | T2 | 3 | 2 | -1 | Presented SS, canceled meetings |
| TerraBella Senior Living | T1 | 3 | 2 | -1 | Would have to drive growth |
| YAD | T2 | 1 | 2 | +1 | Tried but never gotten an audience |
| American Healthcare LLC | T2 | 3 | 3 | 0 | Tom to talk to Colvin |
| American Senior Communities | T1 | 5 | 5 | 0 | Have it on our paper, they are happy |
| BHI Senior Living | T2 | 1 | 1 | 0 | All psych |
| Brickyard Healthcare | T2 | 1 | 1 | 0 | *(gap entity)* |
| Brookdale Senior Living | T1 | 5 | 5 | 0 | Have on our paper |
| Carecore Health | T3 | 1 | 1 | 0 | *(gap entity)* |
| Carespring | T2 | 1 | 1 | 0 | *(gap entity)* |
| Castle Healthcare | T2 | 3 | 3 | 0 | Brooke and Ian more involved |
| Ciena Healthcare | T1 | 1 | 1 | 0 | *(gap entity)* |
| Envive Healthcare | T3 | 1 | 1 | 0 | *(gap entity)* |
| HCF Management | T2 | 1 | 1 | 0 | *(gap entity)* |
| Lifecare | T1 | 1 | 1 | 0 | Do not really know well |
| Lionstone Care | T2 | 3 | 3 | 0 | Tom needs to talk to Kim B |
| Miller's Merry Manor | T3 | 1 | 1 | 0 | *(gap entity)* |
| National Healthcare Corp | T1 | 1 | 1 | 0 | *(gap entity)* |
| Navion | T1 | 3 | 3 | 0 | Good to start talking, growing |
| PACS Group | T1 | 1 | 1 | 0 | *(gap entity)* |
| Phoenix Senior Living | T2 | 1 | 1 | 0 | *(gap entity)* |
| Principle | T1 | 3 | 3 | 0 | Meeting scheduled on the 17th |
| Southern Healthcare Mgmt | T2 | 1 | 1 | 0 | Not in MUO Data notes |
| TLC Management | T1 | 3 | 3 | 0 | Part of Hoosier Alliance, active contact |
| Topaz Healthcare | T2 | 1 | 1 | 0 | Do not really know well |
| Trilogy | T1 | 4 | 4 | 0 | Already covered, speaking with Dr. McNamara |
| Trio Healthcare | T3 | 1 | 1 | 0 | *(gap entity)* |

---

## Key Takeaways

1. **The swap had minimal tier impact** — only TerraBella crosses a boundary (T2 → T1 at score 55, right on the line).

2. **Brooke and Tom are measuring different things.** Brooke's scores reflect BD relationship depth and strategic priority. Tom's scores reflect shared savings engagement reality. Neither is wrong — they're complementary lenses.

3. **Tom has blind spots.** 4 of the 11 big divergences are gap entities he didn't assess. Another 3 he marked "do not really know well" where Brooke had strong scores (Otterbein, Arbors, Pavilion).

4. **Brooke's scores skew higher.** Tom scored lower in 20 of 26 disagreements. This is consistent with Tom grading on current engagement while Brooke grades on potential/priority.

5. **The model is robust to this disagreement.** Despite 11 entities diverging by 2+ RS points (6-12 total score points), only one tier boundary gets crossed. The other dimensions (revenue, beds, footprint) carry enough weight to stabilize the tiers.

---

## Decision Needed

How should RS be handled going forward?

| Option | Pros | Cons |
|--------|------|------|
| **Keep Tom's (status quo)** | Ground truth on SS engagement | Erases Brooke's BD intel; penalizes MUOs Tom doesn't know |
| **Restore Brooke's** | Reflects BD relationship depth | Doesn't capture SS engagement reality |
| **Blend (max of two)** | Preserves strongest signal from each | May inflate scores |
| **Dual-column (both in output)** | Full transparency, defer decision | Doesn't resolve which one drives the tier |

---

*Scripts: `scripts/rs_comparison.py`, `scripts/rs_tier_impact.py`*
*Source data: `Final_MUO_Tiering_V20.xlsx` (Brooke), `build_scoring_workbook.py` TOM_RS_SCORES (Tom)*
