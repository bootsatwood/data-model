# Database Verification Procedures

**These procedures are MANDATORY for all database work. Never substitute pattern-matching, heuristics, or assumptions for verification.**

---

## Procedure 1: Facility Dedup

**Question answered:** Are these two rows the same building?

### Steps

1. **Check the source** — which pipeline did each row come from (NIC-A, NIC-B, GLR, CMS/SNF, LEGACY)
2. **Same source = likely campus pair** (separate licensed units loaded from the same dataset)
3. **Different source = likely duplicate** (same facility loaded from two pipelines)
4. **For SNFs — CMS CCN cross-reference** confirms identity (same CCN = same facility, period). This had a 100% confirmation rate in V22.12 (255 pairs, zero false positives).
5. **For ALFs — state licensing cross-reference** (NC DHSR, VA DSS, etc.) since ALFs have no CCN equivalent.
6. **Quality tiebreaker for confirmed dupes** — use the scoring system (see below)

### Authority Sources (mandatory, not optional)

| Source | What It Covers | When to Use |
|---|---|---|
| **CMS Provider Info** | SNF chain, legal business name, CCN | Every SNF pair — CCN is definitive |
| **ProPublica Nursing Home Inspect** | Ownership (direct, indirect, managerial control) | When corporate attribution is in question |
| **State Registry** (NC DHSR, VA DSS, etc.) | ALF licensed operator, license holder | Every ALF pair — only authority for ALFs |
| **GLR Export** | Served facilities, contract relationships | Every pair involving a served facility |

### Scoring System for Tiebreakers (from V22.13/V22.14)

| Factor | Points | Notes |
|---|---|---|
| Served = Yes | +1000 | Served rows ALWAYS win |
| Real corporate name | +10 | vs INDEPENDENT (+1) or unknown (+0) |
| PROPCO name detected | -7 | Keywords: real estate, investor, holdings, properties, LLC propco patterns |
| Attribution source: GLR | +8 | Ground truth for service relationships |
| Attribution source: CMS | +6 | Federal authority for SNFs |
| Attribution source: NIC | +4 | Market data |
| Attribution source: LEGACY | +2 | Older import, less reliable |
| Field completeness | +1 each | Per non-empty field (county, beds, census, etc.) |

### Four Documented Dedup Patterns (from V22.13→V22.14)

| Pattern | Description | Action |
|---|---|---|
| **1. INDEPENDENT vs Real Corp** | One row has corporate attribution, the other says INDEPENDENT or unknown | Keep the row with the real corp name |
| **2. Operator vs PROPCO/LLC** | One row has the operating company, the other has a real estate holding entity | Keep the operator. PROPCO is not the decision-maker. |
| **3. Same Org, Variant Names** | Both rows have the same parent organization under slightly different legal names | Keep the higher-scored row. Log the variant to MUO_Corporate_History.md. |
| **4. Corp vs "unknown"** | One row has a corporate name, the other is blank/unknown | Keep the row with data |

### Four Shared-Address Patterns (from Phantom Triage)

| Pattern | Description | Action |
|---|---|---|
| **1. Trailing Type, Two Records** | Facility DB has "Name - SNF" and "Name AL" as separate records. Combined DB has 3 rows (1 SNF + 2 ALFs, one phantom). | Remove the phantom ALF. Migrate service flags to SNF before deletion. |
| **2. Combined Type Attribute** | Facility DB has 1 record with type = "AL/SNF". Combined DB has 2 rows. | These are legitimate — keep both unless one is clearly a phantom. |
| **3. Two Different Names** | Facility DB has 2 records with distinct names at same address, no type suffix. | Legitimate campus pair — keep both. |
| **4. Placeholder IL** | Facility DB has an IL record with no address/info. NIC confirms IL units exist. | Flag for data enrichment, don't delete. |

### What is NOT a valid shortcut

- Bed count differences do NOT determine campus vs duplicate — NIC and GLR report different bed counts for the same facility
- Name similarity does NOT determine duplicate — "ALAMANCE HOUSE AL" and "ALAMANCE HOUSE MC" are separate buildings
- "One served, one not" does NOT automatically mean duplicate — it could be two buildings where we only serve one
- NEVER classify a pair without checking the source column first

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

### Authority Sources (mandatory, not optional)

| Source | What It Covers | When to Use |
|---|---|---|
| **CMS Provider Info** | Chain name, legal business name, CCN, ownership type | Every SNF evaluation |
| **ProPublica Ownership** | Beneficial owner, managerial control, ownership % | Every corporate attribution change |
| **State Registry** | Licensed operator for ALFs | Every ALF evaluation |
| **GLR Export** | Who we contract with at served facilities | Every served facility — ground truth |
| **Operator Website** | Current branding, community locator | Supplementary validation |

### What is NOT a valid shortcut

- CMS chain name ≠ operator (chains track holding companies or therapy vendors)
- Management company ≠ owner (MFA, YAD, LifeWorks manage for multiple owners)
- NIC MAP operator ≠ owner (NIC surfaces PropCo LLCs, not management companies)
- "All facilities under management company X belong to owner Y" is NEVER a safe assumption — always verify per-facility via ProPublica or state registry
- NEVER bulk-recode corporate attribution without per-facility verification

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

## Version History

- **2026-03-23:** Created after V25.2/V25.3 correction. Pattern-matching caused 10 incorrect corporate recodes that required emergency rollback.
- **2026-03-23:** Added documented dedup patterns from V22.11-V22.14 changelogs, phantom triage patterns, scoring system, and mandatory authority sources. These procedures existed but were not followed during V25.1/V25.2 work.
