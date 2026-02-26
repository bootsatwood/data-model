# V17 Corporate Name Matching & Contract Status Propagation
## Critical Component for V17 Merge

**Date**: November 20, 2025  
**Issue Identified**: Cannot blindly set new facilities to "GREEN" - must check corporate relationships first

---

## EXECUTIVE SUMMARY

**The Problem**: Original V17 plan would set all ~2,709 new facilities to Contract_Status = "GREEN"

**Why That's Wrong**: If a new Eventus facility belongs to a corporate entity that has RED or YELLOW facilities in V16, the new facility should inherit that risk status.

**The Solution**: Implement corporate name matching and status propagation BEFORE setting Contract_Status.

---

## 1. UNDERSTANDING CONTRACT STATUS

### Definitions (from Book1.xlsx origin)

| Status | Meaning | Count in V16 | Business Impact |
|--------|---------|--------------|-----------------|
| **RED** | Terminated contract | 14 facilities (10 corporates) | Exclude from projections |
| **YELLOW** | At-risk contract | 40 facilities (30 corporates) | Conservative projections only |
| **GREEN** | Healthy contract | 17,380 facilities | Normal projections |

### Corporate-Level Risk Examples from V16

| Corporate Name | Total Facilities | RED | YELLOW | Status Rule |
|----------------|------------------|-----|---------|-------------|
| CCH HEALTHCARE | 40 | 3 | 1 | RED (worst status wins) |
| BRIGHTON | 5 | 2 | 0 | RED |
| AMERICAN SENIOR COMMUNITIES | 150 | 0 | 1 | YELLOW |
| PRUITT HEALTH | 18 | 0 | 3 | YELLOW |
| SABER HEALTHCARE GROUP | 159 | 0 | 1 | YELLOW |

**Key Principle**: If ANY facility under a corporate has RED/YELLOW, ALL facilities under that corporate inherit that risk level.

---

## 2. V16 RED & YELLOW CORPORATE ENTITIES

### 🔴 RED Status Corporate Names (10 entities, 14 facilities)

| Corporate Name | Facilities | Notes |
|----------------|------------|-------|
| BRICKYARD | 7 total (1 RED) | |
| GREENTOWN VOLUNTEER FIRE COMPANY | 1 total (1 RED) | |
| PRINCIPLE | 13 total (1 RED) | |
| SIGNATURE HEALTH | 14 total (1 RED) | |
| BRIGHTON | 5 total (2 RED) | Multiple RED flags |
| SOUTHERN HEALTHCARE MANAGEMENT, LLC | 4 total (1 RED) | |
| COMMUNICARE | 12 total (1 RED) | |
| WAVERLY CARE CENTER, INC | 2 total (2 RED) | All facilities RED |
| BLUE CENTRAL GROUP | 1 total (1 RED) | |
| CCH HEALTHCARE | 40 total (3 RED, 1 YELLOW) | Both RED and YELLOW |

### 🟡 YELLOW Status Corporate Names (30 entities, 40 facilities)

| Corporate Name | Facilities | Notes |
|----------------|------------|-------|
| MAGNOLIA | 3 total (1 YELLOW) | |
| GARDANT | 1 total (1 YELLOW) | |
| AMERICAN SENIOR COMMUNITIES | 150 total (1 YELLOW) | Large operator |
| MAJESTIC CARE | 49 total (1 YELLOW) | |
| INFINITY HEALTHCARE CONSULTING | 107 total (1 YELLOW) | |
| TRADITIONS | 3 total (1 YELLOW) | |
| CLEARVIEW | 6 total (1 YELLOW) | |
| MFA | 12 total (1 YELLOW) | |
| SABER HEALTHCARE GROUP | 159 total (1 YELLOW) | Large operator |
| PRUITT HEALTH | 18 total (3 YELLOW) | Multiple YELLOW flags |
| NAVION | 18 total (1 YELLOW) | |
| LIBERTY | 14 total (3 YELLOW) | Multiple YELLOW flags |
| SUNRISE SENIOR LIVING | 11 total (2 YELLOW) | |
| SINGH | 6 total (1 YELLOW) | |
| AVARDIS | 6 total (1 YELLOW) | |
| MOMENTUS HEALTH | 4 total (1 YELLOW) | |
| ASPIRE | 2 total (1 YELLOW) | |
| *(+13 more single-facility entities)* | | See analysis output |

---

## 3. CONTRACT STATUS PROPAGATION LOGIC

### Decision Tree for NEW Eventus Facilities

```
START: New facility from Eventus with "Owner Name" = X

STEP 1: Match Owner Name to V16 Corporate Names
  ↓
  ├─→ EXACT MATCH found
  │     ↓
  │     Lookup worst Contract_Status for that corporate in V16
  │     ↓
  │     ├─→ Has RED facility → Set new facility = RED
  │     ├─→ Has YELLOW facility (no RED) → Set new facility = YELLOW
  │     └─→ Only GREEN facilities → Set new facility = GREEN
  │
  ├─→ FUZZY MATCH found (85%+ similarity)
  │     ↓
  │     Flag for manual review + inherit status provisionally
  │     ↓
  │     Data_Quality_Flag = "Corporate_Fuzzy_Match_Review"
  │
  └─→ NO MATCH found
        ↓
        Set Corporate_Name = Eventus "Owner Name"
        Set Contract_Status = "GREEN" (new entity, optimistic default)
        Data_Quality_Flag = "New_Corporate_Entity"
```

### Hierarchy of Status (Worst Wins)

```
RED > YELLOW > GREEN

If corporate has ANY RED facility → Corporate status = RED
Else if corporate has ANY YELLOW facility → Corporate status = YELLOW
Else → Corporate status = GREEN
```

---

## 4. CORPORATE NAME MATCHING METHODOLOGY

### Challenge: Name Variations

| V16 Corporate_Name | Possible Eventus Owner_Name |
|--------------------|-----------------------------|
| AMERICAN SENIOR COMMUNITIES | American Senior Communities LLC |
| PRUITT HEALTH | Pruitt Health Inc |
| CCH HEALTHCARE | CCH Healthcare LLC |
| SOUTHERN HEALTHCARE MANAGEMENT, LLC | Southern Healthcare Management |
| SUNRISE SENIOR LIVING | Sunrise Senior Living Inc |

### Multi-Tier Matching Strategy

#### Tier 1: Exact Match
```python
# Case-insensitive, normalized
V16_normalized = V16_name.upper().strip()
Eventus_normalized = Eventus_name.upper().strip()

IF V16_normalized == Eventus_normalized:
    Match_Confidence = "Exact"
    Use_Match = TRUE
```

#### Tier 2: Stripped Match
```python
# Remove common suffixes
suffixes = ["LLC", "INC", "CORP", "LP", "LLP", "CO", "COMPANY"]

V16_stripped = remove_suffixes(V16_name)
Eventus_stripped = remove_suffixes(Eventus_name)

IF V16_stripped == Eventus_stripped:
    Match_Confidence = "High" 
    Use_Match = TRUE
```

#### Tier 3: Fuzzy Match
```python
# Levenshtein distance or similar
similarity = calculate_similarity(V16_name, Eventus_name)

IF similarity >= 0.85:
    Match_Confidence = "High"
    Use_Match = TRUE
    Flag_For_Review = "Corporate_Fuzzy_Match"
ELIF similarity >= 0.70:
    Match_Confidence = "Medium"
    Use_Match = FALSE  # Too risky, manual review required
    Flag_For_Review = "Corporate_Fuzzy_Match_Manual_Required"
```

#### Tier 4: No Match
```python
Match_Confidence = "None"
Use_Match = FALSE
# New corporate entity
```

---

## 5. V17 REVISED WORKFLOW WITH CORPORATE MATCHING

### Updated Merge Process

```
STEP 1: Load Databases
  V16 = 17,434 facilities × 23 columns
  Eventus = 23,142 facilities

STEP 2: Build V16 Corporate Status Lookup Table
  Extract unique Corporate_Name from V16
  For each corporate:
    Find worst Contract_Status (RED > YELLOW > GREEN)
  Result: Corporate_Lookup_Table
    Columns: Corporate_Name, Worst_Status, RED_Count, YELLOW_Count, Total_Count

STEP 3: GPS Match (dedupe)
  Identify ~2,709 NEW Eventus facilities

STEP 4: Corporate Name Matching
  For each NEW Eventus facility:
    a. Get Eventus "Owner Name"
    b. Try to match to V16 Corporate_Name (Exact → Stripped → Fuzzy)
    c. Record match confidence
    d. If matched:
        - Inherit V16 Corporate_Name
        - Inherit Worst_Status from Corporate_Lookup_Table
    e. If not matched:
        - Corporate_Name = Eventus "Owner Name"
        - Contract_Status = "GREEN" (default)
        - Data_Quality_Flag = "New_Corporate_Entity"

STEP 5: Build V17
  Combine V16 (17,434) + NEW with inherited statuses (2,709)
  Total = 20,143 facilities

STEP 6: QC Validation
  - Check for high-value corporates (AMERICAN SENIOR COMMUNITIES, etc.)
  - Review all fuzzy matches
  - Verify RED/YELLOW propagation worked correctly
```

---

## 6. REVISED V17 COLUMN STRUCTURE (NO NEW COLUMNS)

### Columns Affected by Corporate Matching

| # | Column Name | Population for NEW Facilities |
|---|-------------|-------------------------------|
| 3 | Corporate_Name | **Matched from V16 OR Eventus Owner Name** |
| 20 | Contract_Status | **Inherited from V16 corporate OR "GREEN"** |
| 19 | Data_Quality_Flag | Add flags: "Corporate_Fuzzy_Match", "New_Corporate_Entity" |

All other columns (1-2, 4-18, 21-23) populate as originally planned.

---

## 7. EXPECTED OUTCOMES

### Contract Status Distribution After Matching

| Status | V16 Count | Expected NEW from Eventus | Expected V17 Total |
|--------|-----------|---------------------------|---------------------|
| GREEN | 17,380 | ~2,600 (estimated) | ~19,980 |
| YELLOW | 40 | ~50 (if corporates matched) | ~90 |
| RED | 14 | ~20 (if corporates matched) | ~34 |

**Note**: Actual numbers depend on match success rate.

### Match Confidence Distribution (Estimated)

| Confidence | Expected % | Expected Count | Action |
|------------|------------|----------------|--------|
| Exact | 60% | ~1,625 | Auto-accept |
| High (stripped) | 15% | ~406 | Auto-accept with flag |
| High (fuzzy 85%+) | 5% | ~135 | Accept with manual review flag |
| Medium/Low | 5% | ~135 | Manual review required |
| None | 15% | ~406 | New corporate entities |

---

## 8. DELIVERABLES FOR CORPORATE MATCHING

### New Reports Required

1. **Corporate_Status_Lookup_V16.xlsx**
   - Corporate_Name
   - Worst_Status  
   - RED_Count
   - YELLOW_Count
   - GREEN_Count
   - Total_Facilities

2. **V17_Corporate_Match_Log.xlsx**
   - Eventus_Owner_Name
   - V16_Corporate_Name_Matched
   - Match_Confidence
   - Match_Method
   - Contract_Status_Inherited
   - Needs_Manual_Review (Y/N)

3. **V17_Fuzzy_Matches_For_Review.xlsx**
   - Only facilities with Medium/Low confidence
   - Side-by-side name comparison
   - Recommended action

4. **V17_New_Corporate_Entities.xlsx**
   - Facilities with no V16 match
   - Set to GREEN by default
   - May need vetting

---

## 9. CRITICAL CORPORATES TO WATCH

### High-Priority Matches (Large Operators)

| Corporate Name | V16 Facilities | Status | Must Match? |
|----------------|----------------|--------|-------------|
| AMERICAN SENIOR COMMUNITIES | 150 | YELLOW | ✅ Critical |
| SABER HEALTHCARE GROUP | 159 | YELLOW | ✅ Critical |
| INFINITY HEALTHCARE CONSULTING | 107 | YELLOW | ✅ Critical |
| MAJESTIC CARE | 49 | YELLOW | ✅ Critical |
| CCH HEALTHCARE | 40 | RED | ✅ Critical |
| PRUITT HEALTH | 18 | YELLOW | ✅ Important |
| NAVION | 18 | YELLOW | ✅ Important |

If we miss these matches, we could incorrectly classify hundreds of new facilities as GREEN when they should be YELLOW or RED.

---

## 10. ANSWER TO YOUR ELIGIBILITY QUESTION

### Integration_Eligible

**Definition**: Facility is served AND could expand services (add PCP or MH)

**Criteria**:
- Do_We_Serve = "Yes"
- NOT Integrated_Flag = "Yes" (already have all services)
- NO Barrier
- Geographic_Tier = "A_Metro" or "B_Highway" (not rural)
- Total_Beds ≥ threshold (30 for PCP-only, 20 for MH-only)
- Contract_Status = "GREEN" (exclude RED/YELLOW for conservative projections)

**For NEW Facilities**: Always FALSE (not served yet)

### New_Business_Eligible

**Definition**: Unserved facility that is a viable new business target

**Criteria**:
- Do_We_Serve = "No"
- NO Barrier
- Geographic_Tier = "A_Metro" or "B_Highway" (not rural)
- Total_Beds ≥ 30 (size threshold)
- NO Corporate Barrier
- Contract_Status = "GREEN" or "YELLOW" (exclude RED if termed)

**For NEW Facilities**: Calculated based on above criteria after Contract_Status is set

**Current V16 Issue**: All eligibility flags = FALSE suggests criteria are very strict or need recalculation.

---

## 11. NEXT STEPS

1. ✅ Confirm this corporate matching approach
2. Build Corporate_Status_Lookup_Table from V16
3. Implement matching algorithm (Exact → Stripped → Fuzzy)
4. Run match process on ~2,709 NEW facilities
5. Generate match confidence reports
6. Manual review of Medium/Low confidence matches
7. Build V17 with inherited Contract_Status
8. Recalculate eligibility flags for ALL 20,143 facilities
9. QC validation
10. Deliver V17 package

---

**Document Status**: READY FOR REVIEW & APPROVAL  
**Key Change**: Added corporate name matching and status propagation  
**Date**: November 20, 2025

---

## APPENDIX: Matching Algorithm Pseudocode

```python
def match_corporate_name(eventus_owner, v16_lookup_table):
    """
    Match Eventus Owner Name to V16 Corporate Name
    Returns: (matched_name, confidence, worst_status)
    """
    
    # Normalize
    eventus_norm = normalize(eventus_owner)
    
    # Tier 1: Exact match
    for v16_corp in v16_lookup_table:
        if normalize(v16_corp) == eventus_norm:
            return (v16_corp, "Exact", lookup_status(v16_corp))
    
    # Tier 2: Stripped match
    eventus_stripped = strip_suffixes(eventus_norm)
    for v16_corp in v16_lookup_table:
        if strip_suffixes(normalize(v16_corp)) == eventus_stripped:
            return (v16_corp, "High", lookup_status(v16_corp))
    
    # Tier 3: Fuzzy match
    best_match = None
    best_similarity = 0
    for v16_corp in v16_lookup_table:
        similarity = calculate_similarity(eventus_norm, normalize(v16_corp))
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = v16_corp
    
    if best_similarity >= 0.85:
        return (best_match, "High_Fuzzy", lookup_status(best_match))
    elif best_similarity >= 0.70:
        return (best_match, "Medium_Fuzzy", "MANUAL_REVIEW")
    
    # Tier 4: No match
    return (eventus_owner, "None", "GREEN")
```

---

**END OF CORPORATE MATCHING METHODOLOGY**
