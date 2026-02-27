# 2 — Fee Schedule Reference

**Vault companion:** `new_02_Data_Model/Current/2_Fee_Schedule_Reference_V20_1.xlsx`
**Current version:** V20.1
**Last updated:** 2026-02-26

---

## Purpose

The Fee Schedule Reference is the authoritative source for all service fees, adjusters, and rate calculations. It feeds directly into the three Economic Model Scenarios. No fee values should be hardcoded anywhere else — all downstream files reference this workbook.

## Base Service Fees

| Service | SNF | ALF |
|---------|-----|-----|
| PCP | $3,078.00 | $2,084.00 |
| MH | $1,211.00 | $1,431.00 |
| CCM | $360.00 | $360.00 |
| SS | $4,800.00 | $4,800.00 |

## Permanent Adjusters

| Service | Adjuster | Calculation |
|---------|----------|-------------|
| PCP | 1.00 | No adjustment |
| MH | 0.50 | Base x 0.50 |
| CCM | 0.30 | Base x 0.30 |
| SS | 0.165 | Base x 0.50 x 0.33 |

## Adjusted Service Fees (Applied Rates)

| Service | SNF Calculation | SNF Result | ALF Calculation | ALF Result |
|---------|-----------------|------------|-----------------|------------|
| PCP | $3,078.00 x 1.00 | **$3,078.00** | $2,084.00 x 1.00 | **$2,084.00** |
| MH | $1,211.00 x 0.50 | **$605.50** | $1,431.00 x 0.50 | **$715.50** |
| CCM | $360.00 x 0.30 | **$108.00** | $360.00 x 0.30 | **$108.00** |
| SS | $4,800.00 x 0.165 | **$792.00** | $4,800.00 x 0.165 | **$792.00** |
| **TOTAL** | | **$4,583.50** | | **$3,699.50** |

## Revenue Calculation Basis

- **All fees are ANNUAL rates per occupied bed**
- **Census** = Average daily occupied beds (not licensed bed capacity)
- **Formula:** Annual Facility Revenue = Census x Fee
- **Typical range:** $125,000–$300,000 per facility (27–65 occupied beds, SNF integrated)

| Example | Census | Fee (Integrated) | Annual Revenue |
|---------|--------|-------------------|----------------|
| SNF | 50 beds | x $4,583.50 | = $229,175 |
| ALF | 50 beds | x $3,699.50 | = $184,975 |

## Fee Change Management

**Mandatory for any fee modification:**
1. Written authorization from project owner
2. Impact analysis (calculate full downstream effect)
3. Documentation update (this file + Core Rulebook)
4. QC validation (Core QC Protocol)

## Related Files

- **This repo:** `1_Combined_Database.md` — source facility data
- **This repo:** `3_Economic_Model_Compendium.md` — scenario models that consume these fees
- **This repo:** `current/6_Core_Rulebook_V20_0.md` — Section 3 (Fee Structure) is the authoritative methodology

---

*One-to-one markdown companion for the Fee Schedule Reference. Git tracks version history.*
