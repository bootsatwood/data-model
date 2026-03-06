# Phantom Triage — Served Facilities (12 ALF Rows)

Cross-referenced against Eventus internal Facility Database on 2026-03-03.

## Background

NIC enrichment identified 50 confirmed phantom ALF rows (NC-only buildings, zero AL/MC units).
12 of these are marked Do_We_Serve=Yes. Each was paired with the SNF row at the same
address and reviewed against the internal Facility Database to determine safe removal vs
service flag migration.

## Four Shared-Address Patterns Discovered

| Pattern | Description | Example |
|---------|-------------|---------|
| 1. Trailing Type, Two Records | Facility DB has "Name - SNF - ST" and "Name AL - ST" as separate records. Combined DB has 3 rows (1 SNF + 2 ALFs, one phantom). | Four Seasons, Heritage Park, Wesley Manor |
| 2. Combined Type Attribute | Facility DB has 1 record with facility type = "AL/SNF". Combined DB has 2 rows. | Westminster Village, Wesley Pines |
| 3. Two Different Names | Facility DB has 2 records with distinct names, no type suffix. Combined DB has 2 matching rows. | Holston |
| 4. Placeholder IL | Facility DB has an IL record with no address/info. NIC confirms IL units exist at address. | Wesley Manor IL |

## Removals (5 ALF Rows)

| ALF Row | Facility | Address | City, State | Category |
|---------|----------|---------|-------------|----------|
| 4760 | Four Seasons Retirement Center - SNF | 1901 Taylor Rd | Columbus, IN | Pattern 1 phantom |
| 4879 | Heritage Park SNF | 2001 Hobson Rd | Fort Wayne, IN | Pattern 1 phantom |
| 5368 | Wesley Manor SNF | 1555 N Main St | Frankfort, IN | Pattern 1 phantom |
| 4895 | Hoosier Health & Living | 621 S Sugar St | Brownstown, IN | Service mismatch — migrate to SNF |
| 17212 | Glenwood Healthcare Center SNF/NF | 1924 Glenwood Park Rd | Princeton, WV | Service mismatch — migrate to SNF |

## SNF Row Updates (4 Rows — Before Corresponding Removal)

These SNF rows must be updated BEFORE removing the paired ALF row so service
flags are not lost.

| SNF Row | Facility | Changes |
|---------|----------|---------|
| 18779 | Hoosier Christian Village (Brownstown IN) | Corporate_Name → "CHI Living", Do_We_Serve → Yes, MH_Flag → Yes |
| 5200 | Timbercrest Church of the Brethren Home (North Manchester IN) | Do_We_Serve → Yes, MH_Flag → Yes |
| 20792 | Wesley Pines (Lumberton NC) | Do_We_Serve → Yes, Integrated_Flag → Yes |
| 17209 | Glenwood Healthcare Center (Princeton WV) | Do_We_Serve → Yes, PCP_Flag → Yes, Facility_Name → "Glenwood Healthcare Center SNF/NF" |

## Keep As-Is (2 Rows)

| Rows | Facility | City, State | Notes |
|------|----------|-------------|-------|
| 20939 + 20940 | Holston Health and Rehab / Holston Senior Living | Wytheville, VA | Both confirmed accurate in Facility DB (Pattern 3) |

## Flag for Facility DB Owner Review (2 Facilities, 4 Rows)

| Rows | Facility | City, State | Issue |
|------|----------|-------------|-------|
| 5325 + 5372 | Westminster Village | Terre Haute, IN | Facility DB has 1 combined AL/SNF record; Combined DB has 2 rows. Corporate mismatch: ALF="Rush Memorial" (correct), SNF=blank. (Pattern 2) |
| 5244 + 5200 | Timbercrest | North Manchester, IN | Facility DB SNF entry has combined AL/MC/IL attribute. Two real facilities but type classification is ambiguous. (Pattern 2) |

## Additional Notes

- **Naming alignment:** Combined DB should adopt Facility DB naming convention (e.g., "Four Seasons Retirement Center - SNF - IN") since Facility DB has consent authority.
- **Census vs Consents:** "Census" in Facility DB = consents (signed patients). "Census" in Combined DB = CMS average daily residents. Different numbers, different authority. Need consistent terminology going forward.
- **Corporate "THE" prefix:** Wesley Pines has "The United Methodist Retirement Homes, Inc" (ALF) vs "Methodist Retirement Homes Inc" (SNF). Same owner. Standardize in Wave 2 corporate fix.
- **Heritage Park flag swap:** ALF row 4879 (removed) had MH=Yes, but Facility DB confirms both facilities are Integrated. MH flag was incorrect data on the phantom.
- **Placeholder ILs:** Wesley Manor (Frankfort IN) has an IL placeholder in Facility DB with no data. NIC shows IL=72 units at that address.
- **NIC Operator discrepancy (Glenwood):** NIC says real operator is Stonerise, not CommuniCare. CommuniCare may be PROPCO. Wave 2 item.

## Remaining Work

- 38 non-served confirmed phantoms still need triage (less urgent — no service relationship at risk)
- Build `phantom_fix.py` with preview/apply mode implementing the above actions
- All removals and updates require QC snapshot before/after validation
