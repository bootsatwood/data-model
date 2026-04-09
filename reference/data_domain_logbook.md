# Data Domain Logbook

A running record of data governance decisions, reconciliations, and definitions published across workstreams. Each entry captures what was decided, who was involved, and where the supporting documentation lives.

**Future home:** Keystone Data Governance tab (`/bd-data-governance/logbook`) — fifth sub-page alongside Overview, Defined Terms, Business Rules, and Change Log. See `memory/projects/bd_data_governance.md` for module architecture. Frontend: `feature/bd-dashboard-refinements` branch, `frontend/src/views/bd-data-governance/`.

---

| Date | Stakeholders | Topic | Key Outcomes / Decisions | Reference Files |
|---|---|---|---|---|
| 2026-04-08 | Malik, James, Brooke, Ian | Sale Type Classification (NL / ND / Integration) | Finance v4.6 label swap aligned 17/23 Jan+Feb facilities. 6 remain (EST items miscoded, corp owner data issues). Corporate-level definition adopted: NL = no prior relationship, ND = existing corp relationship, IG = existing served facility. Forward Universe recommended as corp owner source. | `Vault/05/NB_LOB_Report_March_2026/Sale_Type_Reconciliation_Report.pdf`, `BD_Sale_Type_Definitions.pdf`, `Verification_Methodology.pdf`, `Verification_Report_V4.html` |
| 2026-04-08 | James | Pipeline Conversion Rate Denominator | Keystone and NB Report use different pipeline totals (Jan: $8.35M vs $11.1M). Booked AR matches. Keystone pulls formula_mkyha5he from Monday.com snapshots stored in PG. James's Jan denominator appears estimated (no pull date, round number). Call to align on single source TBD. | `Vault/05/NB_LOB_Report_March_2026/`, Keystone API `/api/business-development/pipeline/summary` |
