# V22.13 -> V22.14: ALF Same-Address Different-Corp Deduplication

**Date:** 2026-03-06
**Script:** `scripts/v22_14_alf_diffcorp_dedup.py`
**Input:** `1_Combined_Database_FINAL_V22_13.xlsx`
**Output:** `1_Combined_Database_FINAL_V22_14.xlsx`

---

## Summary

Removes 37 duplicate ALF rows where the same facility appears 2+ times at the same address with the same facility name but different corporate names. These are primarily PROPCO/OPCO duplicates from NIC Maps data, where both the property-holding entity and the operating company created separate records for the same physical facility.

## Why These Are Duplicates

NIC Maps data often has TWO records for the same ALF:
- One listing the **operating company** (who runs the facility)
- One listing the **property-holding company / PROPCO** (who owns the building)

When imported into our database, both records created separate rows. Same facility, same address, same name — but different Corporate_Name values. These are not two separate facilities.

## Patterns and Examples

### Pattern 1: INDEPENDENT vs Real Corp Name (11 pairs)

One source had no corporate attribution; the other did. Keep the one with data.

| Facility | City, State | Kept Corp | Removed Corp |
|---|---|---|---|
| THE COLONNADES | Charlottesville, VA | UNIVERSITY OF VIRGINIA FOUNDATION | INDEPENDENT |
| RAPPAHANNOCK WESTMINSTER-CANTERBURY | Irvington, VA | RAPPAHANNOCK WESTMINISTER CANTERBURY INC | INDEPENDENT |
| MALLARD COVE SENIOR LIVING | Cincinnati, OH | MALLARD COVE SENIOR DEVELOPMENT LLC | INDEPENDENT |
| MCGREGOR ASSISTED LIVING | East Cleveland, OH | MCGREGOR SENIOR ASSISTED | INDEPENDENT |
| KINGSTON RESIDENCE OF SYLVANIA | Sylvania, OH | KINGSTON RESIDENCE OF SYLVANIA LLC | INDEPENDENT |

### Pattern 2: Operating Company vs PROPCO/LLC (15+ pairs)

One row has the operator; the other has the real estate holding entity. Keep the operator.

| Facility | City, State | Kept Corp (operator) | Removed Corp (PROPCO) |
|---|---|---|---|
| AUTUMNFIELD OF BELHAVEN | Pinetown, NC | EASTERN RETIREMENT CENTERS, INC | 2421 TABULA RASA LLC |
| MITCHELL HOUSE | Spruce Pine, NC | MITCHELL HOUSE ONE, LLC | DOCENA REAL ESTATE INVESTMENTS LLC |
| OAK HILL LIVING CENTER | Angier, NC | THE AUTUMN GROUP, INC | JBS S COMPANY LLC |
| BARKLEY PLANTATION | Cadiz, KY | BARKLEY PLANTATION | M R & G LLC |
| RIVER'S BEND RETIREMENT COMMUNITY | Kuttawa, KY | RIVER'S BEND RETIREMENT COMMUNITY | LAKE CLOUGH DEV INC |
| PARKVIEW RETIREMENT CENTER | Sanford, NC | PARKVIEW RETIREMENT CENTER, INC | OSCAR & ELDERLENE KELLER FAMILY LLC |
| COVENANT CARE | Lumberton, NC | P. LAMB, INC | ROYAL WARD & GLEZEN LLC |
| PROVISION LIVING AT WEST CHESTER | West Chester, OH | INDEPENDENT | AEG WEST CHESTER PROPCO LLC |

### Pattern 3: Same Org, Variant Names (5+ pairs)

Both rows have the same parent organization under slightly different legal names.

| Facility | City, State | Kept Corp | Removed Corp |
|---|---|---|---|
| CROSS ROAD RETIREMENT COMMUNITY | Asheboro, NC | THE CROSS ROAD REST AND RETIREMENT CENTER, INC | CROSS ROAD REST & RETIREMENT CTR |
| GENERATIONS ASSISTED LIVING | West Jefferson, NC | ASHE SERVICES FOR AGING, INC | ASHE SERVICES FOR AGING FOUNDATION INC |
| MCALPINE ADULT CARE | Morganton, NC | INTEGRITY-MCALPINE ADULT CARE, LLC | INTEGRITY-MORGANTON LLC |
| CYPRESS MANOR | Roper, NC | STAR CARE NETWORK - CYPRESS MANOR, LLC | STAR CARE NETWORK-CM REALTY LLC |

### Pattern 4: Corp Name vs "unknown" (4 pairs)

| Facility | City, State | Kept Corp | Removed Corp |
|---|---|---|---|
| Royal Estates Assistive Living | Dolton, IL | Royal Estates Assistive Living | unknown |
| Ravenswood Senior Living | Chicago, IL | Evergreen Real Estate Services, LLC | unknown |
| Lacey Creek Supportive Living | Downers Grove, IL | Garden Management | unknown |
| Arden Rose Senior Living | Lake in the Hills, IL | Arden Rose Senior Living | unknown |

## Keep/Remove Logic

The scoring system determines which row to keep:
1. **Served rows always win** (+1000 points) — only Pantego Rest Home was served; its served row was kept
2. **Real corp name beats INDEPENDENT/unknown** (+10 vs +1/+0)
3. **PROPCO names penalized** (-7 for real estate / investor / holdings / properties keywords)
4. **Attribution source scored** (GLR +8, CMS +6, NIC +4, LEGACY +2)
5. **Field completeness** (+1 per non-empty field)

## Change Counts

| Metric | Count |
|---|---|
| Addresses processed | 36 |
| Rows removed | 37 (36 pairs + 1 triple) |
| Served rows removed | 0 |

## Row Counts

| Metric | V22.13 | V22.14 | Delta |
|---|---|---|---|
| Total | 25,709 | 25,672 | -37 |
| SNF | 14,984 | 14,984 | 0 |
| ALF | 10,665 | 10,628 | -37 |
| ILF | 60 | 60 | 0 |
| Served | 1,657 | 1,657 | 0 |

## State Distribution

| State | Removed |
|---|---|
| NC | 22 |
| OH | 8 |
| KY | 3 |
| VA | 2 |
| IL | 1 |
| MN | 1 |
