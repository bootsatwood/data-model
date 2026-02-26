# KML Mapping Files - V9 Data (Nov 18, 2025)

## CRITICAL VERSION GAP

These KML files were generated from **Combined_Database_FINAL_V9.xlsx** on November 18, 2025 and **were never regenerated** as the data model evolved through V15, V16, V18.x, V19.x, and V20.x.

| When Created | Data Version | Current Data Version | Gap |
|--------------|--------------|---------------------|-----|
| Nov 18, 2025 | V9 | V20.0 | ~11 versions behind |

**If you use these KML files for Google Maps/Earth visualization, you are working with outdated data.**

---

## What's Here

### KML Layer Files (16 total)
Eight layers, each split by facility type (SNF/ALF):

| Layer | Name | Color | Strategy | Files |
|-------|------|-------|----------|-------|
| 1 | Metro Corporate New Business | Blue | PRIMARY TARGET | `Layer1_SNF_Metro_Corp_NewBiz.kml`, `Layer1_ALF_Metro_Corp_NewBiz.kml` |
| 2 | Metro Independent New Business | Orange | SECONDARY | `Layer2_SNF_Metro_Indep_NewBiz.kml`, `Layer2_ALF_Metro_Indep_NewBiz.kml` |
| 3 | Metro Corporate Integration | Green | UPSELL TARGET | `Layer3_SNF_Metro_Corp_Integration.kml`, `Layer3_ALF_Metro_Corp_Integration.kml` |
| 4 | Metro Independent Integration | Purple | UPSELL | `Layer4_SNF_Metro_Indep_Integration.kml`, `Layer4_ALF_Metro_Indep_Integration.kml` |
| 5 | Rural Corporate Integration | Red | MAINTAIN | `Layer5_SNF_Rural_Corp_Integration.kml`, `Layer5_ALF_Rural_Corp_Integration.kml` |
| 6 | Rural Corporate New Business | Yellow | OTHER GROUP | `Layer6_SNF_Rural_Corp_NewBiz.kml`, `Layer6_ALF_Rural_Corp_NewBiz.kml` |
| 7 | Rural Independent Integration | Gray | LOW PRIORITY | `Layer7_SNF_Rural_Indep_Integration.kml`, `Layer7_ALF_Rural_Indep_Integration.kml` |
| 8 | Rural Independent New Business | Gray | EXCLUDED | `Layer8_SNF_Rural_Indep_NewBiz.kml`, `Layer8_ALF_Rural_Indep_NewBiz.kml` |

### Supporting Files
- `Google_Maps_Layer_Guide.md` - Detailed usage guide with presentation talking points
- `Metro_Centers_19_GPS_Coordinates.csv` - GPS coordinates for 19 metro centers (useful reference)

---

## V9 Statistics (Outdated)

| Layer | Total | SNF | ALF | Revenue Opportunity |
|-------|-------|-----|-----|---------------------|
| 1. Metro Corporate New Business | 792 | 610 | 182 | $178.5M |
| 2. Metro Independent New Business | 729 | 244 | 485 | $0 |
| 3. Metro Corporate Integration | 496 | 152 | 344 | $26.5M |
| 4. Metro Independent Integration | 137 | 32 | 105 | $4.5M |
| 5. Rural Corporate Integration | 849 | 310 | 539 | $45.3M |
| 6. Rural Corporate New Business | 1,086 | 877 | 209 | $209.5M |
| 7. Rural Independent Integration | 256 | 68 | 188 | $12.1M |
| 8. Rural Independent New Business | 932 | 305 | 627 | $0 |
| **TOTAL** | **5,277** | **2,598** | **2,679** | **$476.4M** |

---

## Why This Gap Exists

The mapping visualization approach evolved rapidly:

1. **Nov 18 (V9)**: KML files created for Google Maps/Earth visualization - 8-layer strategic framework
2. **Nov 19 (V15)**: Shifted to CSV format for Google My Maps import (36 files, L1-L6 per story)
3. **Nov 20-21 (V16)**: Combined SNF+ALF into unified Integration/NewBusiness stories
4. **Nov 22 (V18.1)**: Simplified to Map1/Map2 master CSV approach
5. **Nov 24+ (V19)**: Moved to Excel-based Metro Priority Targets for practical sales use

The KML format was abandoned after V9 because:
- CSV import to Google My Maps was simpler
- Excel targets were more practical for sales consumption
- Nobody went back to regenerate KML files with updated data

---

## To Regenerate (If Needed)

To create V20-accurate KML files:
1. Export facility data from `Combined_Database_FINAL_V20_0.xlsx`
2. Apply the 8-layer segmentation logic (see [[Google_Maps_Layer_Guide]])
3. Convert to KML format with GPS coordinates
4. Rebuild Google Maps layers

**Estimated effort**: Moderate - requires re-running the layer generation scripts against V20 data.

---

## Related Files

- **Current data**: [[01_Data Model/Current/1_Combined_Database_FINAL_V20_0.xlsx]]
- **Current metro targets**: V19_Metro_Priority_Targets_Final_V19_2 (3)_with screenshots.xlsx (Downloads)
- **CSV layer approach**: [[08_Archive/By Topic/Data Model V15/|Data Model V15]] and [[08_Archive/By Topic/Data Model V16/|Data Model V16]]
- **Full mapping evolution**: [[08_Archive/By Topic/Geographic Mapping Evolution/Geographic_Mapping_Evolution_Index|Geographic Mapping Evolution Index]]

## Cross-References

- [[00_Index/Project History#Geographic Visualization Evolution|Project History - Geographic Visualization Evolution]] - Timeline narrative
- [[00_Index/Document Lineage#Geographic Visualization Files|Document Lineage]] - File inventory
- [[00_Index/_00_Index|Master Index]] - Main navigation

---

*Archived: January 11, 2026*
*Original location: Downloads/_Mapping/*
