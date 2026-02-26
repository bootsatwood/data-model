# Proposed Addition to Final Model Rulebook V12

## New Section 5A: Database Column Definitions

*Recommended placement: After Section 5 (Market Definitions), before Section 6 (Barrier Entities)*

---

### 5A.1 Ownership Classification

**Column to Use**: `Ownership_Type`

| Value | Definition |
|-------|------------|
| Corporate | Facility owned by a corporate entity |
| Independent | Facility independently owned |

**CRITICAL**: Do NOT use `Corporate_Name` column for ownership determination. The `Corporate_Name` field may be populated for Independent facilities (particularly ALFs) and does not indicate ownership type.

### 5A.2 Facility Type Classification

**Column to Use**: `Source_Type`

| Value | Definition |
|-------|------------|
| SNF | Skilled Nursing Facility |
| ALF | Assisted Living Facility |

### 5A.3 Service Status

**Column to Use**: `Do_We_Serve`

| Value | Definition |
|-------|------------|
| Yes | Currently served facility |
| No | Not currently served |

### 5A.4 Service Flags

| Column | Values | Definition |
|--------|--------|------------|
| `Integrated_Flag` | Yes/No | Facility receives both PCP and MH services |
| `PCP_Flag` | Yes/No | Facility receives PCP services only |
| `MH_Flag` | Yes/No | Facility receives MH services only |

---

*End of proposed addition*
