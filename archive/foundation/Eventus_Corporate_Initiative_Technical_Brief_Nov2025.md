# Eventus Corporate Initiative — Integrated SNF + ALF Model

**Technical Brief — Prepared: November 2025**

---

## 1. Project Overview & Purpose

**Objective:** Create a unified, revenue-driven dataset joining Skilled Nursing Facilities (SNF) and Assisted Living Facilities (ALF) to measure corporate footprint, service connectivity, barrier impact, and financial opportunity.

---

## 2. Phase Progress Summary

| Phase | Focus | Output | Status | Completion |
|-------|-------|--------|--------|------------|
| 1 | SNF Data Cleansing & Harmonization | SNF_Master_Final_BarrierRestored_v2_20251104_1602.xlsx | Complete | Nov 4 2025 |
| 2 | ALF Data Cleansing & Integration | ALF_Model_Clean_v1 | Complete | Nov 3 2025 |
| 3 A–C | Aggregation / Financial Computation / Corporate Tiering | Master_Combined_v1, Corporate_Metadata_v1 | 95% Complete | Nov 5 2025 |
| 4 | Output Framework (TAM / SAM / SOM) | Eventus_Phase4C_MarketFramework_v1_RevH.xlsx | Finalized | Nov 4 2025 |
| 5 | Output Generation & Validation | Combined SNF + ALF Funnel Workbook | Active | Nov 6–8 2025 |
| 6 | Automation & Maintenance Loop | QC + Refresh Scripts | Planned | — |

---

## 3. Model Logic & Schema Layers

This section summarizes the corporate, service, barrier, geography, and financial computation schema used in the unified Eventus model.

### Corporate Entity Logic

| Field | Purpose | Priority | Notes |
|-------|---------|----------|-------|
| Chain Name / Parent Company | Defines corporate affiliation | P1 | Blank → Independent Entity |
| Legal Business Name | Registered operating entity | P2 | Traceability only |
| Ownership Type | For-profit / Nonprofit / Govt | P2 | Contextual segmentation |

---

## 4. Financial Computation Layer (Phase 3B)

Defines formulas for FFS, CCM, and SS revenue components across SNF and ALF models.

### Financial Assumptions v1

| Parameter | Value | Description |
|-----------|-------|-------------|
| PCP_Rate_ALF | 1,875 | Fixed FFS rate (ALF) |
| MH_Rate_ALF | 1,898 | Fixed FFS rate (ALF) |
| MH_Coverage_Factor | 0.50 | Half coverage for MH only |
| Integrated_Add_On_ALF | 5,160 | Bundled CCM + SS per census |
| CCM_Collect_Factor | 0.30 | % of CCM revenue collectible |
| SS_Eligible_MedicareTraditional | 0.50 | ACO-eligible residents |
| SS_Conversion | 0.33 | Portion yielding SS |

### Unified Computation Logic (Pseudo-code)

```
IF Source_Type = "SNF":
    compute dynamic FFS via visit-based rates
ELSEIF Source_Type = "ALF":
    apply static 1,875 / 1,898 fixed formulas

IF Do_We_Serve = "Yes" AND PCP AND MH:
    include CCM + SS
ELSEIF Do_We_Serve = "Yes" AND (PCP XOR MH):
    FFS only
ELSE:
    potential = integrated proxy + CCM/SS add-on
```

---

## 5. Market Framework (TAM / SAM / SOM — Rev H)

Barrier-sensitive funnel model defining TAM, SAM, SOM, and Current Share tiers with geographic filters and corporate conditions.

---

## 6. Next Steps

1. Finalize Phase 5 combined SNF + ALF output workbook.
2. Produce stakeholder 'Validation & Funnel Summary' deck.
3. Freeze as Eventus_Output_v1.
4. Begin Phase 6 automation and refresh loop.

---

*Converted from original docx. Source: `01_Data Model/Archive/Data Challenges/Eventus_Corporate_Initiative_Technical_Brief_Nov2025.docx`*
