# **Part 2: SNF Stream Documentation (V0.5 to V2.5)**

**Focus:** This phase details the complete structural cleanup, data migration, and feature engineering for the Skilled Nursing Facility (SNF) data stream, starting from the enhanced source file and leading to the final production-ready **V2.5 artifact (The Final SNF Book)**. The project involved the enrichment of **2,595 facilities** across six states.

## **1. Phase Lineage: Source to Final Cleanup (Table D)**

This table serves as the audit trail, documenting the transformation of the SNF source file into a clean, standardized, and feature-rich format.

| Phase | Step | Focus / Description | Input Source(s) | Output Version / Artifact | Key Data Focus | Metrics / Impact |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Part 2 | **Step 0 (Source)** | Raw SNF source file. | SNF Workbook (Raw) | SNF Workbook (Raw) | Raw Data, State Tabs | Original Database Size: **14,752 facilities**. |
| Part 2 | **Step 1 (Migration)** | Enhancement Migration. Migrated all six states' enhancements from state-specific tabs back to the parent file/tab. | SNF Workbook (Raw) | SNF Workbook V0.5 (Internal) | State Enhancements | **2,595 facilities** (17.6% of total) were enriched. |
| Part 2 | **Step 2 (Structure)** | Structural Transformation. Created the standard column hierarchy/template. | SNF Workbook V0.5 | SNF Workbook V1.0 | Column Standardization | Critical Reduction: **111 columns** → **19 columns**. Final row count: **14,750** (2 records removed for cleanup). |
| Part 2 | **Step 3 (Beds/Census)** | Capacity Standardization and Data Quality Flagging (V2.0). Addressed over-capacity and missing Census values. | SNF Workbook V1.0, Census\_Adjustments\_Log\_v2.0 | SNF Workbook V2.0 | Total Beds, Census, Data\_Quality\_Flag | **125 Census values adjusted**. **217 facilities flagged** for Beds/Census review. |
| Part 2 | **Step 4 (Corporate)** | Corporate Name Normalization (V2.1). Collapsed/standardized chain names to improve reporting fidelity. | SNF Workbook V2.0, Corp Name Match Reports | SNF Workbook V2.1 | Corporate Names, Blanks | **4,037 facilities** assigned to chains. **30+ variations collapsed**. |
| Part 2 | **Step 5 (Ownership)** | **Ownership Type Flagging (V2.2)**. Defined corporate vs. independent facilities using business logic. | SNF Workbook V2.1 | SNF Workbook V2.2 | Ownership Type | **10,065 Corporate** and **4,685 Independent** facilities. **100%** coverage achieved. |
| Part 2 | **Step 6 (Address)** | **Address Hygiene (V2.3)**. Cleaned up addresses, ZIP codes, and flagged problematic entries. | SNF Workbook V2.2, Change\_Log\_v2\_3 | SNF Workbook V2.3 | Address/Spatial Data | **1,152** ZIP codes standardized. **399** addresses cleaned. **4** PO Box addresses flagged. |
| Part 2 | **Step 7 (Barriers)** | **Barrier Logic & Conversion (V2.4)**. Standardized barrier text and clarified flag values. | SNF Workbook V2.3, Change\_Log\_v2\_4 | SNF Workbook V2.4 | Barrier Standardization, Flag Clarification | Consolidated **17 barrier values** → **4 categories**. Changed **537 'x' flags** → **'yes'**. |
| Part 2 | **Step 8 (QC Fix)** | **Final Service Flag QC (V2.5)**. Resolved 34 service flag conflicts and one source file error. | SNF Workbook V2.4, Change\_Log\_v2\_5 | **Final SNF Book (V2.5)** | Service Coverage, Flag Accuracy | **34 service conflicts resolved**. Final served count: **562 facilities**. **100%** flag accuracy achieved. |

## **2. Compendium Narrative: Tracing the SNF Transformation**

This section provides a narrative detailing the sequential steps taken to transform the raw, multi-tab SNF source file into a single, clean, and highly structured data artifact.

### **Step 0: Source File (Raw)**

The process began with the raw SNF Workbook, containing **14,752 facilities** across multiple state-specific tabs with **111 columns** of mixed data quality. The source file required both structural consolidation and systematic data enrichment.

### **Step 1: Enhancement Migration (V0.5)**

**Goal:** Consolidate state-specific enhancements from individual state tabs back into the parent database.

This internal step successfully migrated enrichment data for **2,595 facilities** (17.6% of the database) from six state-specific worksheets back into the main data structure, preserving all manual research and data quality improvements performed at the state level.

### **Step 2: Structural Transformation (V1.0)**

**Goal:** Establish the production column structure for the database.

Step 2 was a critical architectural change. The original source file contained **111 columns**. This step created a new, streamlined hierarchy, reducing the final column count to **19 production columns** (as verified in the V1.0 Release Notes). This transformation involved selecting and renaming core fields (e.g., Chain Name became Corporate\_Name) and establishing new feature columns (e.g., Source\_Type, Do\_We\_Serve). The cleanup process also resulted in the removal of 2 invalid records, bringing the final row count to **14,750 facilities**.

### **Step 3: Beds & Census Standardization (V2.0)**

**Goal:** Implement robust data quality checks and systematic adjustments for Census and Capacity metrics.

This step, corresponding to the **V2.0 release**, introduced systematic data integrity fixes for the Total\_Beds and Census fields.

* **Data Quality Flagging:** A new column, Data\_Quality\_Flag, was added to track **217 facilities** (1.5% of the database) requiring review based on three criteria: **Total\_Beds < 5**, **Census > Total\_Beds**, and **Missing Census data**.
* **Census Adjustments:** A total of **125 Census values** were automatically adjusted. Facilities flagged as having Census > Total\_Beds (over-capacity) were corrected by applying a calculated value based on an industry-standard **80% occupancy rate** relative to the Total\_Beds value.

### **Step 4: Corporate Name Normalization (V2.1)**

**Goal:** Standardize the Corporate\_Name field to enable accurate aggregate reporting and reduce noise caused by minor textual variations.

This normalization step applied fuzzy matching and conditional logic to identify and collapse various spellings, abbreviations, and suffix differences within chain names. This process confirmed that **4,037 facilities** are associated with chains, preparing the field for the subsequent Ownership step.

### **Step 5: Ownership Type Flagging (V2.2)**

**Goal:** Populate the Ownership\_Type field for all 14,750 facilities using a definitive business rule.

This step, corresponding to the **V2.2 release**, applied business logic directly to the standardized Corporate\_Name field. The rule dictated: if Corporate\_Name was blank, the facility was Independent (4,685 facilities); otherwise, it was Corporate (10,065 facilities). This action achieved **100% population** of the field.

### **Step 6: Address Hygiene (V2.3)**

**Goal:** Standardize all address fields to ensure data consistency and prepare the data for downstream geocoding and spatial analysis.

This step, corresponding to the **V2.3 release**, focused on three critical address quality enhancements:

* **ZIP Code Standardization:** **1,152** short ZIP codes were fixed by adding leading zeros.
* **Address Standardization:** **399** addresses were cleaned by removing periods from abbreviations (e.g., ST. → ST).
* **PO Box Flagging:** **4** PO Box addresses were flagged in the Data\_Quality\_Flag field to enable easy exclusion from geocoding operations.

### **Step 7: Barrier Logic & Conversion (V2.4)**

**Goal:** Standardize text values and clarify binary flags for improved data usability.

This final feature engineering step, corresponding to the **V2.4 release**, made two critical improvements:

1. **Barrier Standardization:** **17 inconsistent barrier values** across **68 facilities** were consolidated into **4 clear, standardized categories** (Alliance, Own Provider Group, Competitor Contract, Refuses Service).
2. **Flag Clarification:** **537 flag values** in the PCP\_Flag, MH\_Flag, and Integrated\_Flag columns were changed from the shorthand value 'x' to the more intuitive and searchable value **'yes'**.

### **Step 8: Final Service Flag QC (V2.5)**

**Goal:** Resolve all remaining service flag conflicts to guarantee data integrity between the Do\_We\_Serve status and the service type flags, finalizing the database for production.

This final Quality Control step, corresponding to the **V2.5 release**, addressed an issue where facilities marked as Do\_We\_Serve = yes were sometimes missing service flags, or vice versa. The conflicts were resolved through a rigorous change log process:

| Action Type | Facilities Affected | Impact |
| :---- | :---- | :---- |
| **Service Flags Added** | 28 facilities | Added missing PCP, MH, or Integrated flags to served facilities. |
| **Do\_We\_Serve Status Corrected** | 6 facilities | Changed inconsistent Do\_We\_Serve status from 'yes' to 'No' (or corrected service flags). |
| **Source File Error Fixed** | 1 facility pair | Corrected a source file error where service flags were incorrectly assigned to a neighboring facility (Harvard Gardens / Harrison Trail). |

**Final Metrics:**

* **Total Conflicts Resolved:** **34 facilities** had field updates (39 total field updates).
* **Final Served Count:** The final count of served facilities was confirmed at **562**.
* **Result:** The **Final SNF Book (V2.5)** achieved **100% service flag accuracy**, guaranteeing that any facility marked Do\_We\_Serve = yes is accurately categorized by a specific service type.

## **3. Final Phase Scorecard (V2.5)**

This scorecard summarizes the final status of the output artifact, confirming that all key data quality and completeness objectives were met.

| Metric | Baseline Status (Raw Source) | Final Status (V2.5 Artifact) | Impact & Result | Status |
| :---- | :---- | :---- | :---- | :---- |
| **Total Facilities** | 14,752 | **14,750** | 2 invalid records removed | ✅ Verified Count |
| **Column Structure** | 111 columns | **19 columns** | Massive simplification and standardization | ✅ STANDARDIZED |
| **Census Data Quality** | Unknown over-capacity issues | **125 adjustments made**, **217 facilities flagged** | Systematic quality control implemented | ✅ VALIDATED |
| **Corporate Attribution** | Inconsistent naming | **4,037 facilities** in standardized chains | Chain grouping accuracy dramatically improved | ✅ NORMALIZED |
| **Ownership Classification** | 0% populated | **100% populated** (10,065 Corporate, 4,685 Independent) | Complete ownership visibility | 🏆 OBJECTIVE ACHIEVED |
| **Address Quality** | Inconsistent formatting | **1,152 ZIP codes** and **399 addresses** standardized | Geocoding-ready spatial data | ✅ STANDARDIZED |
| **Service Flag Accuracy** | 34 conflicts identified | **100% accuracy** (562 served facilities) | Zero conflicts remain | 🏆 OBJECTIVE ACHIEVED |
