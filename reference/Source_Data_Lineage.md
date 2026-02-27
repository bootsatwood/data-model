# Source Data Lineage

**Last updated:** 2026-02-27

This document records the upstream data sources that feed the Eventus Combined Database, as confirmed by Brooke Ritchie (Chief Strategic Sales & Marketing Officer) on February 27, 2026. Original email preserved in Vault at `new_02_Data_Model/Reference/Source_Brooke_SNF_Database_Email_2026-02-27.eml`.

---

## SNF Sources

### 1. CMS Provider Data — Nursing Facility Database

- **URL:** https://data.cms.gov/provider-data/dataset/4pq5-n9py
- **Maintainer:** Centers for Medicare & Medicaid Services (CMS)
- **Coverage:** All certified SNFs nationwide
- **Fields:** Facility addresses, operator detail
- **How used:** Brooke's team curated this into `SNF Database with Revenue Q4 2025_V2.xlsx` (14,752 facilities across 51 state tabs, 105+ columns) with Eventus-specific revenue overlays. Shared with Roian on October 31, 2025. This became the foundation for the Combined Database (V8.0+).
- **Status:** Authoritative upstream source. CMS updates regularly.

### 2. SNFData.com — State Statistics

- **URL:** https://www.snfdata.com/state_statistics.html
- **Coverage:** SNF facilities, beds, total patient days, gross patient revenue
- **Basis:** Each facility's most recent Medicare cost report
- **How used:** Referenced by Brooke as a supplemental validation source. Not directly ingested into the Combined Database but available for cross-reference and market sizing.

---

## ALF Sources

### 3. AHCA / NCAL — Assisted Living Facts & Figures

- **URL:** https://www.ahcancal.org/Assisted-Living/Facts-and-Figures/Pages/default.aspx
- **Maintainer:** American Health Care Association / National Center for Assisted Living
- **Coverage:** ALF community counts and beds/units by state (bottom section of page)
- **How used:** Identified by Brooke as the best available ALF market sizing reference. Brooke noted: "We didn't find much on the ALF side (and didn't find anything during our original diligence either)."

### 4. State Licensing Files (NC, KY, OH, IN)

- **Coverage:** ALF facilities in Eventus's original 4 service states
- **How used:** Roian manually standardized headers and corporate groupings from state-specific licensing files. After dedup against the SNF master (598 of 1,253 removed), 655 valid ALF records were integrated into the Combined Database (V8.0). See `archive/foundation/SNF_Cleanse.md` for detailed process notes.

### 5. NIC Maps — Nationwide Inventory Export

- **Coverage:** Senior housing inventory across all US states
- **Fields:** Facility name, address, operator, AL Open Units, MC Open Units
- **How used:** 5,328 ALF records from 8 expansion states (MI, IL, WI, MN, FL, MD, GA, MO) integrated in V21.0. Source file preserved in Vault at `new_02_Data_Model/Reference/Source_NIC_Maps_Nationwide_Inventory_Export_11.17.25.xlsx`.
- **Status:** Commercial dataset. Point-in-time export dated November 17, 2025.

---

## Lineage Summary

```
CMS Provider Data (4pq5-n9py)
  └─→ Brooke's team curates → SNF Database with Revenue Q4 2025_V2.xlsx
        └─→ Roian cleanses (Steps 1-6) → SNF Master
              └─┐
                ├─→ Combined Database V8.0 (SNF + ALF unified)
                │     └─→ ... → V20.0 → V21.0 → V21.1 (current)
                │
State Licensing Files (NC, KY, OH, IN)
  └─→ Roian standardizes + dedup → 655 ALF records
        └─┘

NIC Maps Export (Nov 2025)
  └─→ 5,328 ALF records (8 expansion states) → V21.0
```

---

*This document is a reference companion. It does not change with database versions unless new sources are introduced.*
