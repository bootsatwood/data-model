# 3 — Economic Model Compendium (Scenarios 1, 2 & 3)

**Vault companions:**
- `new_02_Data_Model/Current/3_Economic_Model_Scenario_1_Combined_V20_0.xlsx`
- `new_02_Data_Model/Current/4_Economic_Model_Scenario_2_Combined_V20_0.xlsx`
- `new_02_Data_Model/Current/5_Economic_Model_Scenario_3_Combined_V20_0.xlsx`

**Current version:** V20.0 (all three scenarios)
**Last updated:** 2026-02-26

---

## Purpose

The three Economic Model workbooks apply different service package assumptions to the Combined Database, producing TAM/SAM/SOM revenue projections. They share the same facility universe, fee structure, and barrier logic — what differs is which services are bundled into each service type.

## Scenario Definitions

Scenarios differ by **service packages**, not by fee multipliers. Fee amounts are identical across all three.

| Service Type | S1 — Baseline | S2 — PCP Enhanced | S3 — Comprehensive |
|---|---|---|---|
| PCP Only | PCP | PCP + CCM(adj) + SS(adj) | PCP + CCM(adj) + SS(adj) |
| MH Only | MH(adj) | MH(adj) | MH(adj) + CCM(adj) |
| Integrated | PCP + MH(adj) + CCM(adj) + SS(adj) | PCP + MH(adj) + CCM(adj) + SS(adj) | PCP + MH(adj) + CCM(adj) + SS(adj) |

**Key insight:** As service packages are enhanced (S1 → S3), current customer value increases but integration opportunity decreases proportionally. New Business remains constant because new customers always receive the full integrated package.

## Revenue Types

| Type | Definition | Barrier Impact |
|------|------------|----------------|
| **Current Revenue** | Revenue from facilities we currently serve | Never affected |
| **Integration Revenue** | Remaining services that could be added to current customers | $0 if barrier |
| **New Business Revenue** | Potential revenue from facilities we don't serve | $0 if barrier |
| **Total Potential** | Integration + New Business (excludes Current) | — |

## V20.0 Revenue Baselines

### Scenario 1 — Baseline Service Packages

| Metric | Value |
|--------|-------|
| Current Revenue | $172.1M |
| Integration Revenue | $152.4M |
| New Business Revenue | $6,903.7M |
| **Total Potential** | **$7,056.1M** |

### Scenario 2 — PCP Enhanced

| Metric | Value |
|--------|-------|
| Current Revenue | $182.4M |
| Integration Revenue | $143.2M |
| New Business Revenue | $6,903.7M |
| **Total Potential** | **$7,046.9M** |

### Scenario 3 — Comprehensive

| Metric | Value |
|--------|-------|
| Current Revenue | $187.7M |
| Integration Revenue | $138.9M |
| New Business Revenue | $6,903.7M |
| **Total Potential** | **$7,042.7M** |

## Pattern Verification

| Behavior | S1 → S2 → S3 |
|----------|---------------|
| Current Revenue | Increases ($172.1M → $182.4M → $187.7M) |
| Integration Revenue | Decreases ($152.4M → $143.2M → $138.9M) |
| New Business Revenue | **Unchanged** ($6,903.7M) |
| Total Potential | Decreases ($7,056.1M → $7,046.9M → $7,042.7M) |

## Governing Rules

1. **No double counting** — each service component counted once per facility
2. **Barrier impact** — Current Revenue preserved; Integration and New Business zeroed
3. **New Business is identical** across all scenarios (full integrated package)
4. **S2 is the business planning baseline** — point value tables in reports use S2, range tables show S1–S3
5. **Never edit scenario files directly** — changes must originate at database or fee schedule level

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| V20.0 | Dec 2025 | *Current production version (all three scenarios)* |

## Related Files

- **Vault:** `new_02_Data_Model/Current/1_Combined_Database_FINAL_V21_1.xlsx` — source data
- **Vault:** `new_02_Data_Model/Current/2_Fee_Schedule_Reference_V20_1.xlsx` — fee inputs
- **This repo:** `1_Combined_Database.md` — database documentation
- **This repo:** `2_Fee_Schedule_Reference.md` — fee schedule documentation
- **This repo:** `current/6.1_Comprehensive_Report_Compendium_V20_1.md` — downstream report methodology

---

*Compendium markdown companion covering all three Economic Model scenario workbooks. Git tracks version history.*
