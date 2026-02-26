# Quick Import Guide for Google My Maps
## Geographic Layer Files - GPS Coordinate Mapping

---

## FILE NAMING CONVENTION
All files follow this pattern:
`[TYPE]_[STORY]_[LAYER]_[DESCRIPTION].csv`

- **TYPE**: SNF or ALF (at front for easy grouping)
- **STORY**: INT (Integration) or NB (New Business)
- **LAYER**: L1 through L6
- **DESCRIPTION**: What the layer represents

---

## RECOMMENDED IMPORT SEQUENCE

### Step 1: Create Your Base Map
1. Go to [Google My Maps](https://mymaps.google.com)
2. Create New Map
3. Title: "Eventus Healthcare Opportunities V15"

### Step 2: Import Integration Story
**Create Layer Group**: "Integration Opportunity"

Import in this order for best narrative flow:
1. `SNF_INT_L1_Current_Customers.csv` (Green circles)
2. `ALF_INT_L1_Current_Customers.csv` (Green diamonds)
3. Wait... then show L2 (Metro Focus)
4. Continue through L6

### Step 3: Import New Business Story  
**Create Layer Group**: "New Business Opportunity"

Import in this order:
1. `SNF_NB_L1_Not_Served.csv` (Gray circles)
2. `ALF_NB_L1_Not_Served.csv` (Gray diamonds)
3. Progress through layers to show filtering

---

## QUICK STATS FOR EACH LAYER

### Integration Progression
- L1: 1,743 → L2: 497 → L3: 497 → L4: 366 → L5: 261 → L6: 261

### New Business Progression  
- L1: 3,539 → L2: 1,516 → L3: 1,516 → L4: 1,295 → L5: 1,099 → L6: 1,099

---

## COLOR CODING FOR GOOGLE MAPS

### Integration Story
- **L1**: Light Green (#90EE90)
- **L2-L3**: Green (#00AA00) 
- **L4-L5**: Dark Green (#008800)
- **L6 Metro Adjacent**: Bright Green (#00FF00)

### New Business Story
- **L1**: Gray (#808080)
- **L2**: Purple (#9932CC)
- **L3 Corporate**: Blue (#0066CC)
- **L3 Independent**: Orange (#FF8C00)
- **L6 Metro Adjacent**: Bright Blue (#0080FF)

---

## MARKER SIZING

In Google Maps, after import:
1. Click layer options (3 dots)
2. "Style" → "Group places by" → Census
3. Set ranges:
   - Small: <40 beds
   - Medium: 40-100 beds
   - Large: >100 beds

---

## KEY FIELDS IN EACH FILE

Every CSV contains:
- **Reference_ID**: Unique identifier (SNF_00001, ALF_00234)
- **Facility_Name**: Display name
- **Latitude/Longitude**: GPS coordinates
- **Census**: Bed count (for sizing)
- **Revenue_Opportunity**: Dollar value
- **Metro_Region**: Geographic zone (IN-1, OH-2, etc.)
- **Total_Parent_Facilities**: For corporate chains

---

## PRESENTATION TIPS

### For Executive Presentation
1. Start with blank map
2. Add L1 - show scale of current operations
3. Add L2 - demonstrate metro focus
4. Progress through filters explaining each
5. End on L6 - the actionable opportunity

### For Sales Teams
1. Jump straight to L6 files
2. Filter by Metro_Region
3. Sort by Revenue_Opportunity
4. Export territory lists

### For Operations Planning
1. Focus on L6 Metro Adjacent files
2. Group by Metro_Region
3. Calculate drive times between clusters
4. Identify efficient routing

---

## TROUBLESHOOTING

**Issue**: Coordinates not mapping correctly
**Fix**: Ensure Latitude is selected for lat, Longitude for lon (not reversed)

**Issue**: Too many points to see clearly
**Fix**: Use layer visibility toggles, show one story at a time

**Issue**: Can't see difference between SNF/ALF
**Fix**: Use "Style" option to set different icons based on filename prefix

---

## TOTAL FILES: 36

✅ 18 Integration Story files (SNF_INT_* and ALF_INT_*)
✅ 18 New Business Story files (SNF_NB_* and ALF_NB_*)
✅ All contain GPS coordinates from V15 database
✅ Ready for immediate import

Location: `/mnt/user-data/outputs/geographic_layers/`

---

*Quick Reference Card - November 2025*
