# Proposal: CMS Source Data Cross-Reference for Corporate Completeness

**Date:** February 27, 2026
**Author:** Roian Atwood
**Status:** DEFERRED — Captured for future consideration
**Parent:** [[1_Combined_Database|Combined Database Companion]]

---

## Background

The original SNF source file (`SNF Database with Revenue Q4 2025.csv`, shared by Brooke Ritchie on October 31, 2025) has been identified as a **CMS Nursing Home Compare** dataset. The 105-column structure, field naming conventions (CCN, Provider Name, Overall Rating, Health Inspection Rating, etc.), and state-tab organization match the CMS Care Compare public data export exactly.

During early analysis sessions (November 2025), this file was informally referred to as the "NCA Workbook" — a label whose origin is unclear but may have been derived from the dataset's structure being recognized as a national care/CMS extract. The actual source is the CMS Care Compare (formerly Nursing Home Compare) public dataset, available at [data.cms.gov](https://data.cms.gov).

## Unused Attributes of Interest

The Combined Database (V21.1) used a subset of the source file's 105 columns. Several unused attributes could be valuable for future analysis:

### Corporate Ownership (Cols 23–29)

| Column | Description | Potential Use |
|--------|-------------|---------------|
| Chain Name | CMS-assigned corporate parent name | Cross-reference against our Corporate_Name taxonomy to identify mismatches, mergers, or name changes |
| Chain ID | CMS unique identifier for the corporate chain | Stable identifier that persists across name changes — could anchor corporate relationship tracking |
| Number of Facilities in Chain | CMS count of facilities under the chain | Compare against our Corporate_Name facility counts to assess completeness |
| Chain Average Overall 5-star Rating | Average star rating across the chain | Corporate quality scoring input |
| Chain Average Health Inspection Rating | Average inspection rating across the chain | Quality risk indicator |
| Chain Average Staffing Rating | Average staffing rating across the chain | Operational capacity indicator |
| Chain Average QM Rating | Average quality measure rating | Quality measure benchmarking |

### Quality and Risk Flags

| Column | Description | Potential Use |
|--------|-------------|---------------|
| Special Focus Status | CMS designation for persistently poor-performing facilities | Barrier identification, risk scoring |
| Abuse Icon | CMS abuse finding flag | Risk scoring, compliance overlay |
| Provider Changed Ownership in Last 12 Months | Recent ownership change flag | Corporate relationship change detection |
| Overall Rating (1–5 stars) | CMS five-star composite rating | Facility quality scoring, tiering input |
| Number of Fines / Total Amount of Fines | Penalty history | Risk and compliance overlay |
| Number of Substantiated Complaints | Validated complaint count | Quality indicator |

### Operational Detail

| Column | Description | Potential Use |
|--------|-------------|---------------|
| Staffing hours (RN, LPN, Aide — multiple cols) | Reported and case-mix adjusted staffing ratios | Workforce analysis, capacity assessment |
| Continuing Care Retirement Community | CCRC flag | Facility type refinement |
| Date First Approved | Medicare/Medicaid approval date | Facility maturity indicator |

## The Core Question

If CMS Nursing Home Compare is updating its Chain Name and Chain ID fields as corporate relationships change (mergers, acquisitions, rebranding), then pulling a fresh extract periodically could serve as a **cross-reference layer** for our Combined Database:

1. **Completeness check:** Are there facilities in the CMS universe that we're missing?
2. **Corporate currency:** Have chain relationships changed since our last update? Are operators we track now part of larger chains, or have chains split?
3. **Quality overlay:** Could CMS star ratings, staffing data, and penalty history enrich our corporate scoring or barrier identification?

This is especially relevant as the Combined Database grows (V21.1 = 26,271 facilities across 17+ states). The CMS dataset covers the full national SNF universe and updates quarterly.

## Recommended Next Steps

1. **Confirm CMS update cadence** — verify that Care Compare data refreshes quarterly and that Chain Name/Chain ID fields are maintained
2. **Pull a current extract** from data.cms.gov and compare Chain Name/Chain ID against our Corporate_Name field for the footprint states
3. **Quantify the delta** — how many of our Corporate entities have a different Chain Name in CMS? How many CMS chains are absent from our database?
4. **Evaluate integration effort** — if the cross-reference is valuable, design a lightweight reconciliation process (not a full merge, just a comparison report)

## Relationship to Other Proposals

- [[Proposal_Metro_Definition_Enhancement|Metro Definition Enhancement]] — geographic completeness is a parallel concern; CMS data includes Latitude/Longitude for all facilities
- The V21 ALF enhancement used NIC Maps as the ALF source. CMS Care Compare is SNF-only. Together they cover both facility types from authoritative national sources.

---

*Last updated: 2026-02-27*
