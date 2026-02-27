# Source Extract vs. Economic Model Comparison

**Prepared: November 2025**

> [!note] Lineage
> "Source extract" refers to `SNF Database with Revenue Q4 2025.csv`, the original SNF facility file shared by Brooke Ritchie on October 31, 2025. It contained 14,752 facilities across 51 state tabs with 105+ columns including pre-computed revenue fields. This document compares that raw extract's structure against the Eventus Economic Model built on top of it.
>
> Original filename: `Eventus_Model_Comparison_TheirModel_vs_Ours.docx`

---

## How to Use This Comparison

This document helps analysts, data owners, and leadership understand how the original source extract differs from the Eventus Economic Model. The comparison identifies conceptual, structural, and computational differences and provides guidance for harmonizing datasets.

---

## 1. Executive Summary

The source extract serves as a static ledger, summarizing realized revenue through fixed values for PCP, MH/BH, and Integrated care. The Eventus Economic Model, in contrast, dynamically computes revenue streams using defined rates, adjusters, and service flags. The Eventus model can represent both earned and unearned revenue (current and potential), supporting scenario forecasting and market opportunity analysis.

---

## 2. Structural Comparison

| Dimension | Source Extract | Eventus Economic Model | Implication |
|-----------|--------------|----------------------|-------------|
| Revenue Buckets | Single-stream values (PCP, BH/MH, Integrated) | Distinct computed outputs (Current, Potential - Integration, Potential - New Business, Total) | Our model separates earned vs. potential revenue; the extract only represents realized revenue |
| Driver Logic | Manual entry of service flags | Programmatic triggers driven by data (Do_We_Serve, PCP, MH) | Eventus flags dynamically control computation, ensuring consistency |
| Rate Handling | Embedded static rates within values | Explicit rate tables for ALF and SNF with CCM and SS modifiers | Our model is tunable and transparent |
| Potential vs. Earned Split | No concept of potential revenue | Explicit split between current and potential revenue streams | Supports whitespace and opportunity modeling |
| CCM / Shared Savings | Bundled or excluded | Separate parameters (CCM_Base, CCM_Factor, SS_Base, SS_Factor) | Enables complete value capture |
| Calculation Unit | Manual per-facility entries | Dynamic formula: Beds x Rate x Adjusters | Scalable for all facilities and states |
| Schema Objective | Operational snapshot (ledger) | Forecasting and strategic opportunity model | The extract is descriptive; our model is predictive |

---

## 3. Narrative Analysis

The source extract reflects realized revenue but lacks the logic to compute unrealized opportunities. It aggregates values for each service type without deriving them from a standard rate structure. The Eventus Economic Model builds on the same base facility data but introduces controlled rates, occupancy adjustments, and adjustable factors to compute total financial potential. This design supports full transparency and the ability to perform sensitivity testing.

---

## 4. Implications for Analytics and Forecasting

Because the source extract lacks a potential revenue dimension, it cannot be used to assess growth capacity or value-based care opportunity. Its manual nature also limits reproducibility. The Eventus Model allows for consistent, scenario-driven forecasting and supports barrier and market-tier filtering for TAM, SAM, and SOM segmentation.

---

## 5. Next Steps

1. Retain the source extract as a static reference baseline for historical validation.
2. Validate parity between realized (source extract) and computed current (Eventus) revenue.
3. Apply Eventus rate logic to extend the dataset for integrated opportunity modeling.
4. Document all differences for transparency and governance.

---

*Converted from `Eventus_Model_Comparison_TheirModel_vs_Ours.docx`. Reframed to clarify that "Their Model" was the original SNF source extract, not a competing model.*
*Last updated: 2026-02-27*
