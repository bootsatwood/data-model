# Proposal: Facility Profile & CMS API Cross-Reference

**Status:** Deferred
**Created:** 2026-02-27
**Author:** Roian Atwood

---

## Problem

The Combined Database tracks 26,268 facilities (1,660 served) with service flags, census/bed counts, and corporate ownership that drive all downstream revenue calculations. Currently, these values are maintained manually with no systematic way to validate them against either:

1. **Internal source of truth** — the Facility Profile records in the Eventus database
2. **External source of truth** — CMS Provider Data, which publishes facility-level data via an open API

During the Feb 2026 QC review, 11 facilities were found with incorrect service flags. The corrections required manually looking up each facility one by one in the Facility Profile database. At scale, this approach does not work for the full 1,660 served population. Separately, 3 facilities were discovered to have changed ownership (Carrington Place → Hill Valley Healthcare), which was only confirmed through a Facebook post — not an ideal detection method.

## Part 1: Eventus Facility Profile Extract

Extract a periodic report from the Facility Profile module within the Eventus database that includes, at minimum:

| Field | Purpose |
|-------|---------|
| Facility Name | Match key |
| Address / City / State / ZIP | Match key (fuzzy) |
| Active PCP census beds | Validate PCP_Flag and census |
| Active MH census beds | Validate MH_Flag and census |
| Total beds / units | Validate Total_Beds |
| Service status | Validate Do_We_Serve |

This extract would allow:

1. **Service flag validation** — Confirm PCP, MH, or Integrated designation matches operational reality. A facility with both PCP and MH bed counts is Integrated; one service only is PCP or MH; no beds means not served.
2. **Census accuracy** — Replace surrogate census estimates with actual operational census from Eventus. Current database uses `Total_Beds x 0.80` for many ALF records.
3. **Served population reconciliation** — Identify facilities marked as served in the database that are no longer active in Eventus, and vice versa.
4. **Acquisition detection** — Facility name mismatches between the database and Eventus may indicate ownership changes that need to be reflected (see `Facility_Acquisitions_Log.md`).

### Dependencies

- Access to Eventus Facility Profile reporting (Roian or delegate)
- Export format: Excel or CSV
- Field mapping between Eventus column names and Combined Database column names

## Part 2: CMS Provider Data API

CMS publishes the same Nursing Home Compare dataset that our Combined Database was originally built from (dataset `4pq5-n9py`). This data is available via an open API — no authentication required.

**API endpoint:** `https://data.cms.gov/provider-data/api/1/datastore/query/4pq5-n9py`

This could be used to:

1. **Ownership change detection** — Compare `Organization Name` in CMS against `Corporate_Name` in our database. Mismatches flag acquisitions, rebrands, or corporate restructuring.
2. **Universe coverage** — Identify new SNF facilities that have appeared in CMS data since our last build, or facilities that have closed.
3. **Bed count refresh** — CMS reports certified bed counts that could validate or update our `Total_Beds` values.
4. **Address standardization** — CMS addresses are USPS-standardized, which could help clean up inconsistencies in our address fields (e.g., the "city, state, zip stuffed in address column" issues found in the Dec 2025 dedup batch).

### Approach

- **Phase 1 (manual):** Pull a one-time extract via the API, save as CSV/Excel, run a reconciliation against V21.1
- **Phase 2 (scripted):** Add a `crossref` mode to `qc_validator.py` that fetches from the API directly and produces a reconciliation report
- **Phase 3 (periodic):** Schedule quarterly pulls to detect drift between CMS and the Combined Database

### API Notes

- CMS Provider Data uses the DKAN open data platform
- The dataset is updated regularly by CMS
- No API key or authentication required
- Query supports filtering by state, provider type, etc. to reduce payload size
- See `reference/Source_Data_Lineage.md` for full source documentation

## Integration Vision

Both data sources serve different purposes and together provide full coverage:

| Source | Validates | Population |
|--------|-----------|------------|
| **Eventus Facility Profile** | Service flags, census, served status | 1,660 served facilities |
| **CMS Provider Data API** | Ownership, bed counts, universe coverage, closures | 15,243 SNFs (full universe) |

A future `crossref` mode in the QC Validator could ingest both sources and produce a unified reconciliation report, flagging:
- Service flag mismatches (Eventus vs Combined Database)
- Census/bed count drift (Eventus and CMS vs Combined Database)
- Ownership changes (CMS vs Combined Database → candidates for Acquisitions Log)
- New/closed facilities (CMS vs Combined Database)

## Relationship to Existing Work

- **QC Validator** (`scripts/qc_validator.py`) — Natural home for a `crossref` mode
- **Facility Acquisitions Log** (`reference/Facility_Acquisitions_Log.md`) — Ownership mismatches surface acquisition candidates
- **CMS Source Data Cross-Reference** (`reference/Proposal_CMS_Source_Data_Cross_Reference.md`) — Earlier proposal focused on CMS corporate completeness; this proposal is broader and subsumes it
- **Source Data Lineage** (`reference/Source_Data_Lineage.md`) — Documents the CMS dataset ID and URL

---

*This proposal documents an enhancement for future consideration. It does not require immediate action.*
