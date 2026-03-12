# RS Score Decision Session

**Date:** 2026-03-12
**Analyst:** Roian Atwood
**Prereq:** `2026-03-11_RS_Score_Reconciliation_V20_vs_V23.md` (full analysis)

---

## Context

V23 swapped Brooke's BD-based Relationship Score for Tom's shared savings engagement score. Last night's reconciliation found:

- 50 entities compared, 24 agreed, 26 disagreed (Tom lower in 20 of 26)
- 11 big divergences (delta >= 2) — mostly Tom's blind spots or gap entities
- Only 1 tier shift if Brooke's RS restored: TerraBella T2 -> T1 (52 -> 55)
- Model is robust — other dimensions stabilize tiers

## Options on the Table

| # | Option | Summary |
|---|--------|---------|
| A | Keep Tom's (status quo) | Ground truth on SS engagement, penalizes MUOs Tom doesn't know |
| B | Restore Brooke's | BD relationship depth, misses SS reality |
| C | Blend (max of two) | Preserves strongest signal, may inflate |
| D | Dual-column | Full transparency, defers the decision |

---

## Session Notes

### 1. RS Lineage — Two Lenses, Neither Complete

**Brooke's RS (V20, Dec 2025)** — behavioral BD engagement scale:

| Score | Label | Signal |
|---|---|---|
| 1 | At-risk / Never Responds | Crickets or avoidance |
| 2 | Local, No Corp Alignment | Listens but never acts — "false hope" |
| 3 | Responsive When Prompted | Forward momentum but slow |
| 4 | Collaborative, Open | Proactive, identifying opportunities |
| 5 | Embedded Partnership | "They have the Eventus Bible" |

- Scored **50 of 70** tiered entities (T1-T3)
- Distribution: 6x5, 4x4, 20x3, 0x2, 20x1
- No 2s — Brooke jumped straight from "no relationship" to "responsive"
- ~20 entities got RS=0 or default 1 (her blind spots)

**Tom's RS (V23, Mar 2026)** — shared savings engagement scale:

| Score | Label | Signal |
|---|---|---|
| 1 | Don't really know well | No meaningful relationship |
| 2 | Tried, hit resistance | Rejected proposals, defensive posture |
| 3 | Have relationship, stalled | Mixed signals, early stage |
| 4 | Active engagement | Proposals/meetings in play, verbal commitments |
| 5 | Active SS agreement | On Eventus paper, strong partnership |

- Scored **51 entities** (hardcoded in build_scoring_workbook.py)
- Distribution: 20x1, 14x2, 11x3, 4x4, 2x5
- Skews heavily low — 67% scored 1 or 2
- "Don't really know well" = 20 entities — Tom's blind spots

### 2. Key Framing: This Evolves Over Time

Neither Brooke's nor Tom's scores are static snapshots that should be frozen. The question is: what's the right **structure** going forward?

- Tom's coverage will grow as he builds relationships
- Brooke's scores reflect a moment in time (Dec 2025) that's already aging
- The model needs a framework that accommodates evolving inputs, not a one-time swap

### 3. Coverage Comparison

| | Brooke (V20) | Tom (V23) |
|---|---|---|
| Total entities scored | 50 | 51 |
| Scored as 1 (no knowledge) | 20 | 20 |
| Effectively assessed | ~30 | ~31 |
| V20 tiered population | 70 (T1-T3) | — |

Both assessors left ~20 entities at default/unknown. Different 20 in many cases.

### 4. The Email Thread (Mar 7-11, 2026) — Three Voices on the Gap Entities

Source: `RE: Revised Corp Scoring - Updating Finance Board and our internal Workbook`

Roian identified **13 entities** defaulting to RS=1 despite served facilities. He asked Tom for gut-check scores on the 7 with 2+ served campuses, using a simplified 1-5 scale. Tom responded in red; Brooke added comments in blue.

| Entity | Campuses | Served | Tom's Response | Brooke's Response |
|---|---|---|---|---|
| **Brickyard Healthcare** | 22 | 6 | Existing relationship. Years of "fits and starts". Hoosier Alliance member, viable for IN. | Lost business to Rounding Providers (emotional decision by prior COO). Jami Patterson has great relationship with new COO — recovery meeting mid-end April. New AE Gunner Grider has churned up new opp via relationship with Regionals. |
| **HCF Management** | 24 | 5 | No HQ relationship I am aware of | *(no response)* |
| **Miller's Merry Manor** | 14 | 3 | Post-covid reduced dramatically. Hoosier Alliance member. Struggled to have meaningful dialogue. | True, but we do have facilities — many, even an employee clinic at one or two. Will double check. |
| **Sunrise Senior Living** | 36 | 4 | Established corporate relationship. Current opp in NJ/WI (outside footprint). VA awarded to Curana for entire state. Limited opp in our states. | Need to stay close — never know when incumbent could fail. Need to find terms of Curana partnership — auto renewal? |
| **Phoenix Senior Living** | 20 | 3 | Need input from Brooke and Ian | Two facilities in Charlotte NC. Going on EMR, currently don't want to give us access. Could be more to come. |
| **Envive Healthcare** | 11 | 2 | Need input from Brooke and Ian | Unknown |
| **Trio Healthcare** | 11 | 2 | Need input from Brooke and Ian | No relationship. Termed in a couple of VA facilities. VA-based only. Emailed corp but couldn't get a call back. |

**Key observations from the thread:**

1. **Tom and Brooke see different things on the same entities.** Brickyard is the clearest example — Tom sees "fits and starts," Brooke sees active recovery effort with named people and timelines.
2. **Tom deferred to Brooke on 3 of 7** (Phoenix, Envive, Trio) — he explicitly said "need input from Brooke and Ian." This validates that Tom knows his own coverage limits.
3. **Brooke's responses include actionable intel** — names (Jami Patterson, Gunner Grider), timelines (mid-end April), competitors (Rounding Providers, Curana), and strategic considerations (auto-renewal terms). Tom's are status assessments.
4. **The 13 entities were the original gap** — Roian flagged them in the Mar 7 email to Brooke as "the one remaining gap" in the model. Only 7 of the 13 had 2+ served campuses.

### 5. V20 Population Context

| Tier | V1 (Original) | V2 (Updated/BD) | Finance Workbook |
|---|---|---|---|
| T1 | 24 (31%) | 21 (25%) | 19 (32%) |
| T2 | 22 (29%) | 34 (40%) | 17 (28%) |
| T3 | 24 (31%) | 6 (7%) | 2 (3%) |
| T4 | — | 7 (8%) | 12 (20%) |
| T5 | 6 (8%) | 16 (19%) | 10 (17%) |
| **Total** | **76** | **84** | **60** |

T3 collapsed from 31% to 7% — higher thresholds (55/35 vs 50/25) and data-driven scoring pushed most into T2. T4 (MUO gate <7 campuses) and expanded T5 barriers are new in V2.

---

## Decision

**Option E: Living Relationship Tracker (evolutionary approach)**

Rather than choosing between Brooke and Tom's static snapshots, RS becomes a living, dual-perspective tracker:

- **Tom's RS** remains the production score driving the model (go-forward authority on SS engagement)
- **Brooke's RS** is preserved as a reference column capturing BD relationship depth
- **Both assessors** can update their scores and notes over time as relationships evolve
- **Coverage gaps** are visible — entities where neither assessor has real intel are flagged for outreach
- As Tom's coverage grows and Brooke's ages, the tracker naturally shows convergence (or continued divergence worth investigating)
- The "RS — Production" column can evolve its sourcing logic as the tracker matures (e.g., max of two, weighted blend, or assessor override)

**Why not A-D:**
- A (Tom only) erases Brooke's BD intel
- B (Brooke only) is a dead end — snapshot already aging
- C (Blend/max) is a formula hack, not a framework
- D (Dual-column) defers the decision without a path forward

Option E is D with direction and a living system to track it.

---

## Actions Taken

1. **Created Monday.com board:** "Corporate Relationship Tracker" in CRM workspace
   - URL: https://onsitecare.monday.com/boards/18403704088
   - Columns: Tier, Campuses, We Serve, RS-Tom(SS), Tom Notes, RS-Brooke(BD), Brooke Notes, RS-Production, Last Updated, Coverage
   - Groups: T1 Strategic Enterprise, T2 Growth & Expansion, T3 Retention/Watch
   - Populated with all 56 entities from both assessors' data

2. **Coverage status tagged on every entity:**
   - Both Assessed (green) — Tom and Brooke both have substantive scores
   - Tom Only (blue) — Tom assessed, Brooke defaulted to 1
   - Brooke Only (pink) — Brooke assessed, Tom defaulted to 1
   - Gap Entity (gray) — neither has real intel

3. **Email thread intel captured** — Tom and Brooke's Mar 11 responses on the 7 gap entities with 2+ served campuses are now in the tracker notes

4. **Session changelog created** — this file (`2026-03-12_RS_Decision_Session.md`)

---

## Next Steps

- [ ] Review the board in Monday.com — clean up default "Group Title" group
- [ ] Populate Campuses and We Serve columns for all entities (currently only set for the 7 email thread entities)
- [ ] Determine if RS-Production should stay as Tom's score or shift to a derived formula
- [ ] Schedule periodic refresh cycle — quarterly? When should Brooke and Tom next update their scores?
- [ ] Connect board to Corporate Scoring Reference via board relation column

---

*Scripts: `scripts/rs_comparison.py`, `scripts/rs_tier_impact.py`*
*Monday.com: https://onsitecare.monday.com/boards/18403704088*
*Email source: `RE: Revised Corp Scoring - Updating Finance Board and our internal Workbook` (Mar 7-11, 2026)*
