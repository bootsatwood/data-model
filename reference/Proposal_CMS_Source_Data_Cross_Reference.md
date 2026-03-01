# Proposal: CMS Source Data Cross-Reference for Corporate Completeness

**Date:** February 27, 2026
**Author:** Roian Atwood
**Status:** EXECUTED — Cross-reference completed March 1, 2026
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

This is especially relevant as the Combined Database grows (V21.1 = 26,267 facilities across 17+ states). The CMS dataset covers the full national SNF universe and updates quarterly.

## Cross-Reference Results (March 1, 2026)

### Source Data

- **CMS Extract:** NH_ProviderInfo_Feb2026.csv (downloaded March 1, 2026 from data.cms.gov)
- **CMS Records:** 14,710 SNFs (national, all states/territories)
- **Our Database:** 15,243 SNFs (V21.1, 8 production + 8 expansion states + territories)
- **Vault copy:** `02_Data_Model/Reference/Source_CMS_NH_ProviderInfo_Feb2026.csv`

### Test 1: Completeness — CMS facilities missing from our database

| Metric | Count |
|--------|-------|
| CMS SNFs in our footprint states | 15,192 |
| Matched to our database | 15,141 |
| **CMS facilities not in our DB** | **51** |
| Coverage rate | **99.65%** |

The 51 unmatched CMS facilities are predominantly recently certified facilities or facilities that changed addresses since our last source pull. None are in states where we currently serve patients. No action required — these will be captured in the next source refresh.

### Test 2: Staleness — Our SNFs not in CMS

| Metric | Count |
|--------|-------|
| Our SNFs not matching CMS | 292 |
| Of those, **served** (Do_We_Serve = Yes) | **5** |
| Of those, unserved | 287 |

The 287 unserved mismatches are primarily ALF-licensed facilities classified as SNF in our database, or facilities that have closed/merged since our source pull. Low priority.

### Test 3: Served facility resolution

All 5 served SNFs not initially matching CMS were resolved as **name/address formatting differences** — the facilities exist in CMS under slightly different references:

| Our Name | Our Address | CMS Name | CMS CCN | Issue |
|----------|-------------|----------|---------|-------|
| Pheasant Ridge Senior Living | 4001 Pheasant Ridge Dr NE, Roanoke VA | Pheasant Ridge | 495325 | Address format difference (NE suffix) |
| Madeira Care Center | 7085 Miami Ave, Madeira OH | Ayden Healthcare of Madeira | 365186 | Different facility name in CMS |
| Maple Hill Care Center | 11500 Grafton Rd, Grafton OH | Maple Hills Care Center | 366139 | "Hill" vs "Hills" + address format |
| Paulding Care Center | 250 Dooley Dr, Paulding OH | Gardens of Paulding The | 366044 | Different facility name in CMS |
| River Oaks Health & Rehab | 920 South 4th St, Louisville KY | River Oaks | — | Address corrected to match CMS format; corporate discrepancy flagged (CMS=Christian Care Communities, PowerBI=Hill Valley Healthcare) |

**Action taken:** CMS cross-reference notes (CCN numbers and CMS name variants) added to `Data_Quality_Flag` column for these 4 facilities (River Oaks flagged separately for corporate ownership verification with Brooke).

### Summary

The Combined Database has **99.65% completeness** against the authoritative CMS national SNF dataset. All 5 served facilities not initially matching were formatting mismatches, not missing facilities. The CMS extract is preserved in the Vault for future periodic comparison.

### Recommended Cadence

CMS Care Compare data refreshes quarterly. A lightweight cross-reference (completeness + served-facility check) should be run after each database version increment that adds or modifies SNF records. The matching script used normalized address+city+state as the primary key with facility name as a secondary matcher.

## Relationship to Other Proposals

- [[Proposal_Metro_Definition_Enhancement|Metro Definition Enhancement]] — geographic completeness is a parallel concern; CMS data includes Latitude/Longitude for all facilities
- The V21 ALF enhancement used NIC Maps as the ALF source. CMS Care Compare is SNF-only. Together they cover both facility types from authoritative national sources.

---

*Last updated: 2026-03-01*
