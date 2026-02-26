# Handoff Document: Geographic Integration Analysis
## Reconciling $38.6M Model to $29.3M Email Target

---

## 🎯 OBJECTIVE
We're trying to match an email's stated integration opportunity of **$29,281,327** by applying the same filters they used. Our geographic model shows **$38,635,544**, creating a **$9.35M gap** to explain.

---

## 📁 CRITICAL FILES NEEDED FOR NEXT CONVERSATION

### Primary Files (Upload these)
1. **Combined_Database_FINAL_V15.xlsx** - Main database with 17,434 facilities
2. **Book1.xlsx** - Contains Client Status (Red/Yellow/Green) for terms analysis
3. **Geographic_Layer_Methodology_and_Presentation_Guide.md** - Layer approach
4. **Economic_Justification_Size_Thresholds.md** - Threshold rationale

### Generated Files (Already in outputs folder)
- `/mnt/user-data/outputs/geographic_layers/` - Contains 28 CSV files with GPS coordinates
- `/mnt/user-data/outputs/prepared_data_v15.csv` - Preprocessed data with metro regions

---

## 📊 CURRENT STATUS: CLOSING THE GAP

### What We've Identified

| Adjustment | Impact | Status |
|------------|--------|---------|
| **Start: Our Model** | $38,635,544 | ✅ Complete |
| **Add: Differentiated Thresholds** | +$1,626,150 | ✅ Calculated |
| **Subtotal** | $40,261,694 | |
| **Remove: RED Status (termed)** | -$1,516,676 | ✅ Identified in Book1 |
| **Remove: YELLOW Status (at risk)** | -$3,205,636 | ✅ Identified in Book1 |
| **Subtotal after terms** | $35,539,382 | |
| **Need to remove (geographic)** | -$6,258,055 | ❓ TO DO |
| **Target** | $29,281,327 | |

---

## 🗺️ NEXT STEPS: GEOGRAPHIC RESTRICTIONS

### Current Geographic Definition (Too Broad)
```python
geographic_regions = {
    'IN-1': {'lat_min': 41.2, 'lat_max': 41.8, 'lon_min': -87.5, 'lon_max': -85.5},
    'IN-2': {'lat_min': 39.5, 'lat_max': 40.2, 'lon_min': -86.5, 'lon_max': -85.8},
    # ... etc for 19 regions
}
```
**Result**: 497 facilities in metros → $40.3M

### Need to Test Tighter Boundaries
1. **Reduce radius from city centers** 
   - Current: ~15-20 mile equivalent boxes
   - Test: 10-mile radius
   - Test: 5-mile radius

2. **Exclude edge counties**
   - Remove facilities in "Semi" rural areas
   - Focus on urban cores only

3. **Apply stricter "metro-adjacent" definition**
   - Current: All facilities in metro regions = metro-adjacent
   - Need: Actual distance calculation from city centers

---

## 🔧 CODE TO RUN IN NEXT CONVERSATION

### Step 1: Load and Prepare Data
```python
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

# Load files
v15_df = pd.read_excel('Combined_Database_FINAL_V15.xlsx')
book1_barriers = pd.read_excel('Book1.xlsx', sheet_name='SNF PCP PullThru')

# Get Client Status from Book1 for all sheets
def get_client_status():
    sheets = ['ALF MH PullThru', 'ALF PCP PullThru', 'SNF PCP PullThru', 'SNF MH PullThru']
    all_status = []
    for sheet in sheets:
        df = pd.read_excel('Book1.xlsx', sheet_name=sheet)
        if 'Client Status' in df.columns:
            status_df = df[['Facility Name', 'Client Status']]
            all_status.append(status_df)
    return pd.concat(all_status).drop_duplicates()
```

### Step 2: Define City Centers for Distance Calculation
```python
city_centers = {
    'Indianapolis': (39.7684, -86.1581),
    'Columbus_OH': (39.9612, -82.9988),
    'Cleveland': (41.4993, -81.6944),
    'Cincinnati': (39.1031, -84.5120),
    'Louisville': (38.2527, -85.7585),
    'Charlotte': (35.2271, -80.8431),
    'Richmond_VA': (37.5407, -77.4360),
    # Add more as needed
}

def haversine(lon1, lat1, lon2, lat2):
    """Calculate distance in miles between two points"""
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956  # Radius of earth in miles
    return c * r
```

### Step 3: Test Different Geographic Restrictions
```python
def apply_geographic_filters(df, max_distance_miles):
    """Apply distance-based filtering from city centers"""
    filtered = []
    for _, facility in df.iterrows():
        distances = []
        for city, (lat, lon) in city_centers.items():
            dist = haversine(facility['Longitude'], facility['Latitude'], lon, lat)
            distances.append(dist)
        
        # Keep if within max_distance of ANY city center
        if min(distances) <= max_distance_miles:
            filtered.append(facility)
    
    return pd.DataFrame(filtered)

# Test different radii
for radius in [15, 10, 7, 5]:
    filtered = apply_geographic_filters(served_facilities, radius)
    revenue = calculate_integration_revenue(filtered)
    print(f"{radius} miles: {len(filtered)} facilities, ${revenue:,.0f}")
```

### Step 4: Apply ALL Filters Together
```python
def calculate_final_opportunity(df, radius_miles):
    """Apply all email filters"""
    # 1. Served facilities only
    served = df[df['Do_We_Serve'] == 'Yes']
    
    # 2. Geographic restriction
    metro = apply_geographic_filters(served, radius_miles)
    
    # 3. Differentiated thresholds
    mh = metro[(metro['MH_Flag'] == 'Yes') & (metro['Census'] >= 20)]
    pcp = metro[(metro['PCP_Flag'] == 'Yes') & (metro['Census'] >= 30)]
    combined = pd.concat([mh, pcp])
    
    # 4. Remove barriers
    no_barriers = combined[combined['Barrier'].isna()]
    
    # 5. Remove RED/YELLOW status (terms)
    # Need to merge with Book1 Client Status
    client_status = get_client_status()
    merged = no_barriers.merge(client_status, left_on='Facility_Name', 
                              right_on='Facility Name', how='left')
    green_only = merged[(merged['Client Status'] == 'Green') | 
                        (merged['Client Status'].isna())]
    
    return green_only['Revenue_Opportunity'].sum()
```

---

## 📈 EXPECTED OUTCOME

By testing different radius restrictions (15 → 10 → 7 → 5 miles), we should find that somewhere around **7-8 miles** from city centers will remove the needed $6.3M and get us to the $29.3M target.

---

## 💡 KEY DISCOVERIES FROM THIS CONVERSATION

1. **Barriers transferred correctly** from Book1 → V15 (111 → 1,383 through propagation)

2. **Client Status = Terms indicator**:
   - RED (15 facilities) = Termed/Critical
   - YELLOW (39 facilities) = <12 month contracts  
   - GREEN (564 facilities) = Stable

3. **Differentiated thresholds matter**: 20 beds for MH, 30 for PCP (adds $1.6M)

4. **Book1.xlsx is incomplete** (622 facilities vs 1,743 served) - explains why its raw calc = $9.8M

5. **Geographic boundaries are key** - Need ~$6.3M reduction through tighter metro definitions

---

## 🎯 FINAL GOAL

Match the email's $29,281,327 by:
1. ✅ Using differentiated thresholds (+$1.6M)
2. ✅ Removing RED/YELLOW status (-$4.7M)  
3. ⏳ Tightening geographic boundaries (-$6.3M)
4. = $29.3M ✓

---

## 📝 NOTES FOR NEXT CONVERSATION

- We generated 28 CSV files with GPS coordinates for mapping
- Integration Story: 261 facilities → $38.6M
- New Business Story: 1,099 facilities → $361M
- The metro regions need refinement to match operational reality
- Consider using actual drive time vs straight-line distance

---

**Generated**: November 19, 2025
**Current Conversation Capacity**: ~10% remaining
**Ready for handoff**: YES
