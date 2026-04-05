# Forward Universe Data Cleansing Procedures

**Scope:** Procedures for maintaining the accuracy, completeness, and integrity of the Forward Universe (Combined Database). These procedures govern how facility records and corporate operator attributions are verified, corrected, and documented.

**Current production database:** `1_Combined_Database_FINAL_V25_6.xlsx` — 25,508 rows, 18 remediation versions applied.

---

## Problem Typology

Every data quality issue in the Forward Universe falls into one of two categories:

### 1. Facility Identity

Is this row correct? Specifically:

- **Deduplication** — Are two rows the same building? (phantom ALFs, cross-pipeline duplicates, campus roll-ups)
- **Classification** — Is this row the right facility type? (ALF coded as SNF, CCRC campus aggregate carrying inflated IL beds, ILF in the ALF population)
- **Campus Linkage** — Are related rows at the same physical campus correctly associated? (GPS proximity within 3,000 ft, address variations for the same property)

### 2. Operator Attribution

Who runs this facility? Specifically:

- **Corporate identification** — Is the corporate name in the database the actual operator, or is it a PropCo LLC, a management company, a CMS chain artifact, or a stale name?
- **Entity reconciliation** (sub-type) — Are two corporate names in the database actually the same operator? (mergers, rebrands, variant legal names, regional brand structures)
- **Change of ownership** (sub-type) — Has the operator changed since our data was last updated? (CHOWs that CMS hasn't caught up to, divestitures, acquisitions)

Entity reconciliation and CHOW detection are not separate procedures. They are findings that emerge during operator attribution work and have their own verification criteria within that workflow.

---

## Two Procedures, Two Entry Points

These problem types are addressed through two procedures, distinguished by **when and why** you use them — not by what you're checking.

### Comprehensive Scrub → `comprehensive_scrub.md`

**When:** Systematic, proactive pass through a defined segment of the database (an address cluster, a corporate entity portfolio, a state, a facility type population).

**Why:** To surface problems you don't yet know exist. The value is in completeness — at every stop, you evaluate both facility identity and operator attribution in a single pass.

**How it works:** You walk the database systematically. At each stop (address or entity), you run through identity verification and operator attribution sequentially. Identity resolves first (is this the same building? is the type correct?), then attribution (who operates the surviving, correctly-typed rows?). Both use the same sources in the same research pass.

**Examples:**
- V25.1–V25.5 cluster-by-cluster review (56 address clusters)
- Portopiccolo portfolio scrub (58 rows across 5 corporate name variants)
- Cary Trainor cross-DB reconciliation (66 corporate groups)

### Issue Investigation → `issue_investigation.md`

**When:** A specific signal triggers a question about one or more records.

**Why:** Something already looks wrong — a name mismatch, a sale type that doesn't reconcile, a Monday.com field that contradicts the DB, a CMS chain that doesn't match our corporate name. You chase that specific thread to resolution.

**How it works:** The investigation follows a diagnostic flow:

1. **Signal detection** — what triggered the investigation, matched against a catalog of known signal types
2. **Scope assessment** — is this one facility, one entity, or a systemic pattern?
3. **Verification** — run the relevant source checks to confirm or dismiss the signal
4. **Resolution** — if confirmed, determine the correct action (remove row, recode operator, reclassify type, correct field values)
5. **Escalation check** — did this investigation surface enough related anomalies that it should graduate into a comprehensive scrub?

The escalation check is a deliberate decision point. Not every issue investigation becomes a comprehensive scrub — but some should. Portopiccolo started as a single dedup pair (Pair 14, one address) and escalated into a 58-row portfolio scrub when the CHOW discovery revealed systematic misattribution across 5 corporate name variants.

**Examples:**
- Richland Bean-Blossom sale type discrepancy → Putnam County Hospital entity fragmentation (7 corporate names)
- Oak Hollow "Brothers Healthcare" phantom corporate name → operator verification
- Brookdale Ohio INDEPENDENT coding → 9-facility attribution check

---

## Source Reference and Evidence Standard

Source hierarchy (SNF vs ALF), NIC MAP reliability patterns, tier 2 supplemental sources, evidence standard (2-source minimum, confidence levels, per-facility verification rule), conflict resolution decision tree, and logging destinations are all embedded in `comprehensive_scrub.md` Procedure 3. They are not separate documents — they are integral to the operator attribution workflow.

---

## Relationship to Other Documents

| Document | Location | Relationship |
|---|---|---|
| Portopiccolo Research Methodology | `scripts/audit_reports/portopiccolo_research_methodology.md` | Case study illustrating both procedures in practice. Not a procedure itself. |
| Liberty ALF Risk Analysis | `reference/Risk_ALF_Corporate_Attribution_and_Data_Quality.md` | Discovery document identifying three systemic NIC MAP data quality risks. The "why" behind several procedure steps. |
| Source Data Lineage | `reference/Source_Data_Lineage.md` | Documents where our upstream data comes from. Reference, not procedure. |
| CMS Cross-Reference Results | `reference/Proposal_CMS_Source_Data_Cross_Reference.md` | One-time completeness analysis (99.65% SNF coverage). Informs but does not define procedure. |
| MUO Corporate History | `reference/MUO_Corporate_History.md` | Logging destination for corporate intel discovered during cleansing work. |
| Dedup Decisions Log | `scripts/audit_reports/dedup_decisions_log.csv` | Logging destination for facility-level decisions. |
| GLR Change Log | `scripts/audit_reports/glr_change_log.csv` | Logging destination for GLR upstream corrections. Triggers internal communication. |
| Pending Follow-ups | `scripts/audit_reports/pending_followups.csv` | Items that need future action. Check at start of every session. |
| Operator Research Log | Memory: `reference/operator_research_log.md` | Index of operators already fully researched — check before re-investigating. |

### Superseded Documents (preserved for historical reference)

| Document | Location | Superseded By |
|---|---|---|
| DB Verification Procedures | `reference/DB_Verification_Procedures.md` | `procedures/cleansing/comprehensive_scrub.md` |
| Alternative 11-Step Verification | `reference/Alternative_11_Step_Verification_Process.md` | `procedures/cleansing/comprehensive_scrub.md` Procedure 3 (two-pass escalation) |
| Verification Methodology HTML | `Vault/05_Board_and_Leadership/NB_LOB_Report_March_2026/Verification_Methodology.html` | `procedures/cleansing/comprehensive_scrub.md` (HTML retains value as the Sale Type Reconciliation deliverable) |
| Source Lookup How-To | Memory: `reference/source_lookup_howto.md` | `procedures/cleansing/comprehensive_scrub.md` Procedure 3 (source sequence + evidence standard) |

---

## Core Principles

1. **The database is a starting point, not a conclusion.** Every attribution must be verified against external sources before it is used for classification, scoring, or reporting.

2. **Identity resolves before attribution.** Confirm what's at an address before asking who operates it. Attributing ownership to a phantom record that should be deleted is wasted work.

3. **Verify per-facility, never bulk-assume.** The V25.2 YAD/Choice Health error proved that pattern-matching causes misattribution. Every facility gets its own evidence chain.

4. **Know what you know before going external.** Check the Forward Universe, GLR, MUO Corporate History, and the operator research log before querying CMS, NIC MAP, or the web. Context shapes how you interpret what external sources tell you.

5. **Log everything immediately.** Corporate intel, CHOW events, dedup decisions, GLR corrections — document findings as they occur. Research evaporates if it's not written down.

6. **No destructive changes without explicit approval.** Generate a read-only report first, let the user review, then execute with a transaction and verification step.

---

*Created: 2026-04-03. Consolidates methodology from DB_Verification_Procedures.md, portopiccolo_research_methodology.md, Verification_Methodology.html, and source_lookup_howto.md.*
