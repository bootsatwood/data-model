# Database Verification Procedures

**These two procedures are MANDATORY for all database work. Never substitute pattern-matching, heuristics, or assumptions for verification.**

---

## Procedure 1: Facility Dedup

**Question answered:** Are these two rows the same building?

### Steps

1. **Check the source** — which pipeline did each row come from (NIC-A, NIC-B, GLR, CMS/SNF, LEGACY)
2. **Same source = likely campus pair** (separate licensed units loaded from the same dataset)
3. **Different source = likely duplicate** (same facility loaded from two pipelines)
4. **For SNFs — CMS CCN cross-reference** confirms identity (same CCN = same facility, period)
5. **For ALFs — state licensing cross-reference** (NC DHSR, VA DSS, etc.)
6. **Quality tiebreaker for confirmed dupes:** keep the row with served=Yes > county filled > fewer DQ flags > real beds over surrogate

### What is NOT a valid shortcut
- Bed count differences do NOT determine campus vs duplicate — NIC and GLR report different bed counts for the same facility
- Name similarity does NOT determine duplicate — "ALAMANCE HOUSE AL" and "ALAMANCE HOUSE MC" are separate buildings
- "One served, one not" does NOT automatically mean duplicate — it could be two buildings where we only serve one

---

## Procedure 2: 8-Step Corporate Operator Reconciliation

**Question answered:** Who operates this facility?

### Steps

1. **DB fuzzy name scan** — query DB for corporate_name_raw + facility_name variants
2. **CMS cross-reference** — query CMS Provider Info (14,710 SNFs) — AUTHORITY SOURCE for SNFs
3. **Web validation** — check operator website + A Place for Mom + state licensing + SEC
4. **Consolidation** — merge DB + CMS + web into single facility list with source citations
5. **Footprint filter** — count only 6 operating states (NC, SC, VA, KY, OH, IN)
6. **Campus collapse** — street-number matching (same street + city = 1 campus), 15-bed minimum
7. **7+ gate** — pass/fail on collapsed campus count
8. **Score** — apply V23 formula (6 dimensions) for operators that pass

### What is NOT a valid shortcut
- CMS chain name ≠ operator (chains track holding companies or therapy vendors)
- Management company ≠ owner (MFA, YAD, LifeWorks manage for multiple owners)
- NIC MAP operator ≠ owner (NIC surfaces PropCo LLCs, not management companies)
- "All facilities under management company X belong to owner Y" is NEVER a safe assumption — always verify per-facility

---

## When to use which

| Situation | Procedure |
|---|---|
| Two rows at same address, same corp | Dedup |
| Two rows at same address, different corp | Dedup THEN 8-step |
| Evaluating a new MUO candidate | 8-step |
| Recoding corporate attribution | 8-step (per facility, not bulk) |
| Scoring board rescore | 8-step for any entity with ownership changes |

---

## Operator Attribution Rule

We code the entity that makes clinical and business decisions at the facility level — the operator — regardless of who owns the building, holds the license, or appears in CMS chain records.

---

*Created 2026-03-23 after V25.2/V25.3 correction. These procedures exist because pattern-matching caused 10 incorrect corporate recodes that required emergency rollback.*
