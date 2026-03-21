# MUO Corporate History Log

Tracks corporate-level events — mergers, acquisitions, divestitures, rebrands, name changes — for operators in the Combined Database. One section per entity. Entries are added during fuzzy match reconciliation (Punchlist #4) and MUO candidate evaluations.

**Purpose:** Preserve research so it doesn't have to be repeated. When an operator comes up in scoring, pipeline review, or stakeholder conversations, check here first.

**Companion files:**
- `reference/Facility_Acquisitions_Log.md` — facility-level CHOW events (individual facility ownership changes)
- `scripts/audit_reports/Corporate_Name_Dedup_Review_ra_v2.xlsx` — fuzzy match decisions and canonical names
- `changelogs/V22_8_to_V22_9_Fuzzy_Match_Consolidation.md` — confirmed same/different determinations from V22.9

---

## PROMEDICA

**Canonical DB name:** `PROMEDICA`
**DB variants found:** PROMEDICA, HCR ManorCare, HCR Manor Care/ Promedica, Promedica Health Systems, PROMEDICA SENIOR CARE
**DB facility count:** 48 (primarily Arden Courts memory care communities)
**Served:** 2 (Red Oak Manor ALF, Rocky Mount VA; Belles Place of Kenwood ALF, Kenwood OH)

### Timeline
| Date | Event | Source |
|---|---|---|
| 2018 | ProMedica Health System (Toledo, OH) acquires HCR ManorCare for ~$1.35B via Welltower JV. Expands to 30 states, 70,000 employees. HCR ManorCare portfolio included ~450 facilities: SNFs, ALFs, Arden Courts memory care, outpatient rehab, hospice, home health. | [Healthcare Finance News](https://www.healthcarefinancenews.com/news/promedica-welltower-partner-acquire-hcr-manorcare-and-create-7-billion-network) |
| 2020 | HCR ManorCare and Arden Courts rebranded to **ProMedica Senior Care**. Facility signage rollout over 18 months. | [McKnight's Senior Living](https://www.mcknightsseniorliving.com/news/promedica-senior-care-is-new-name-for-hcr-manorcare-arden-courts/) |
| 2025 (Sep) | ProMedica divests 147 SNFs into Welltower/Integra Health JV due to ongoing operating losses in Senior Care Division. Retains only 2 SNFs (1 FL, 1 OH). Continues to operate 58 private-pay Arden Courts memory care communities. 14 additional SNFs (CA, MD, SC) in transition to new operators. | [McKnight's Senior Living](https://www.mcknightsseniorliving.com/news/welltower-to-move-147-promedica-snfs-to-integra-health-jv-promedica-to-continue-to-operate-58-senior-living-communities/) |

### Cross-Reference
| Source | Result |
|---|---|
| CMS (Feb 2026) | No "ProMedica" chain in current CMS data. Former ManorCare SNFs now under other chains (PACS Group, Brookdale, BaneCare). |
| GLR (Mar 2026) | 2 facilities: Red Oak Manor ALF (Rocky Mount VA, 31 pts), Belles Place of Kenwood ALF (Kenwood OH, 18 pts) |

### Notes
- The DB Arden Courts portfolio is almost entirely outside our 6-state footprint (FL, IL, MD, MI, PA dominant)
- ProMedica Senior Care (3 CA facilities) are legacy ManorCare SNFs in divestiture — same company, not a separate entity
- ProMedica Health Systems (1 IL facility) is the parent company name — same entity

**Resolved:** 2026-03-21, Punchlist #4 rows 39/41/44. All 5 variants → SAME → canonical `PROMEDICA`.

---

## HERITAGE HALL

**Canonical DB name:** `HERITAGE HALL`
**DB entity ID:** 37
**DB variants found:** HERITAGE HALL (entity 37, 10 rows), AMERICAN HEALTHCARE, LLC (entity 1219, 11 rows), AHC (entity 1220, 2 rows)
**DB facility count:** 23 rows across 3 entities (should be consolidated under entity 37)
**Served:** 11 facilities (Clintwood, Lexington, Wise, Big Stone Gap, Blacksburg, Grundy, Laurel Meadows, Tazewell + ALF wings)
**SNFs:** Yes — 16 per CMS (Chain ID 265)
**Footprint campuses:** 16 (all VA)
**7+ Gate:** PASS (already on Corporate Scoring Reference board)

### Timeline
| Date | Event | Source |
|---|---|---|
| — | Heritage Hall operates 16 SNFs across rural/exurban Virginia under "[City] Life Care LLC/Corp" legal entities. For-profit. | CMS NH ProviderInfo Feb 2026, Chain ID 265 |
| — | "South Roanoke Nursing and Rehabilitation" (CCN 495002) operates under Heritage Hall chain but with non-Heritage branding. Legal entity: South Roanoke Life Care LLC. | CMS Chain ID 265 |

### Cross-Reference
| Source | Result |
|---|---|
| CMS (Feb 2026) | 16 SNFs, Chain ID 265. All VA. Total 1,848 certified beds, 86.6% avg occupancy. 3 five-star, 9 four-star. Legal entities follow "[City] Life Care LLC/Corp" pattern. |
| DB (V24.1) | 10 rows under HERITAGE HALL (entity 37) + 11 under AMERICAN HEALTHCARE (entity 1219) + 2 under AHC (entity 1220). Split is a data source artifact: CMS-sourced → entity 37, GLR-sourced → entities 1219/1220. |

### Notes
- **Corporate attribution split is the key issue.** The served Heritage Hall locations were ingested from GLR under "American Healthcare, LLC" while the unserved locations came from CMS under "Heritage Hall." Same operator, different source attribution.
- "AHC" (entity 1220) is an abbreviation of American Healthcare — same company as entity 1219. Only holds 2 South Roanoke rows.
- South Roanoke has ALF+SNF dual-row pattern (standard for Heritage Hall served sites). ALF row (15889) shows do_we_serve=True, mh_flag=True; SNF row (16246) shows do_we_serve=False — needs reconciliation.
- Heritage Hall's V23 scoring uses only 10 campuses (entity 37). Correct count is 16. ER dimension underscored by ~4 weighted points.

**V25 action:** Reattribute 13 rows (entities 1219+1220) to HERITAGE HALL (entity 37). Deprecate entities 1219 and 1220. Rescore Heritage Hall with 16 campuses.

**Researched:** 2026-03-21, MUO Candidate Evaluation (board review).

---

## HERITAGE SENIOR LIVING (disambiguation)

**Not a single entity.** The DB has 25 rows under "HERITAGE SENIOR LIVING" (entity 1088) across OH(4), PA(15), VA(3), WI(5). These belong to **four separate, unrelated companies:**

### Heritage Senior Living (WI) — heritagesenior.com
**Canonical DB name:** `Heritage Senior Living` (retain entity 1088 for WI)
**Owner:** MSP Real Estate / Milo Pinkerton (architect/CEO)
**Portfolio:** 15 AL/MC/IL communities, all Wisconsin
**DB rows:** 5 (WI)
**Footprint campuses:** 0 (WI not in footprint)
**SNFs:** No
**7+ Gate:** FAIL

### Heritage Senior Living LLC (PA) — heritagesl.com
**Proposed DB name:** `Heritage Senior Living LLC`
**Proposed entity ID:** 4111
**HQ:** Blue Bell, PA. CEO Kevin McCollum.
**Portfolio:** 17 AL/MC/IL communities — PA(14), NJ(2), VA(3). Three REIT JV partners: Invesque, American Healthcare REIT, ReNew REIT.
**DB rows:** 18 (15 PA + 3 VA)
**Footprint campuses:** 3 (VA only — Heritage Green Lynchburg, Heritage Green Hanover, Crossroads at Bon Air)
**SNFs:** No
**7+ Gate:** FAIL

### Heritage Senior Living of Marysville (OH) — heritageslm.com
**Proposed DB name:** `Heritage Senior Living of Marysville`
**Proposed entity ID:** 4113
**Owner:** Angie Sharp
**Portfolio:** 1-2 AL/MC/IL communities (Marysville + possibly Plain City under separate LLC "Seva Senior of Plain City")
**DB rows:** 1 (Marysville, OH)
**Footprint campuses:** 1 (OH)
**SNFs:** No
**7+ Gate:** FAIL

### Heritage Legacy Health Services (OH) — heritagepointeal.com
**Proposed DB name:** `Heritage Legacy Health Services`
**Proposed entity ID:** 4112
**Owners:** Deborah Voiers-Akers and Steven Akers
**Portfolio:** 1 AL facility — Heritage Pointe Assisted Living (DBA), 116 beds, New Boston OH. Ohio DOH License #1845R.
**DB rows:** 2 (Heritage Square ID 11962 + Heritage Point ID 11995 — same facility, merge to 1 row)
**Footprint campuses:** 1 (OH)
**SNFs:** No
**7+ Gate:** FAIL

### Cross-Reference
| Source | Result |
|---|---|
| CMS (Feb 2026) | Zero matches for any "Heritage Senior Living" variant. None operate SNFs. |
| DB (V24.1) | 25 rows under single entity 1088 — all misattributed as one company. |
| Web | Three distinct websites (heritagesenior.com, heritagesl.com, heritageslm.com), different ownership, non-overlapping geographies. |

**V25 action:** Split entity 1088 (25 rows) into 4 entities. Merge New Boston duplicate (delete row 11995). Fix Heritage Point missing county → Scioto.

**Researched:** 2026-03-21, MUO Candidate Evaluation (board review).

---

## HERITAGE RETIREMENT COMMUNITIES (OH) — heritage-rc.com

**Canonical DB name:** `Heritage Retirement Communities` (not currently in DB under this name)
**DB presence:** 2 rows under LK HERITAGE VILLAS LLC (entity 1574) + 1 row under INDEPENDENT (ID 11964, Heritage Villas, 905 Pittsburg Ave NW) + 1 row under EMBASSY HEALTHCARE (ID 18331, Heritage Health Care of Regent and Euclid)
**CEO:** Nathan Steinmetz. COO: Aaron Sonnenschein.
**HQ:** 905 Pittsburg Ave NW, North Canton, OH
**Portfolio:** 8 facilities in NE Ohio — 5 AL/MC + 3 SNF (formerly Embassy Healthcare SNFs)
**SNFs:** Yes — 3 (Heritage Healthcare of Lyndhurst CMS 366114, Heritage Healthcare of Euclid CMS 365730, Heritage Healthcare of Painesville CMS 365713)
**Footprint campuses:** 6 (OH) — North Canton, Shaker Heights, Westlake, Lyndhurst, Euclid, Painesville
**7+ Gate:** FAIL (6 campuses, one short)

### Cross-Reference
| Source | Result |
|---|---|
| CMS (Feb 2026) | 3 SNFs still show under EMBASSY HEALTHCARE chain (Chain ID 199). CMS ownership records lag actual transfers. |
| Ohio SOS | LK Heritage Villas LLC — registered agent Nathan Steinmetz. Delaware LLC registered in OH Aug 2021. |
| Web | heritage-rc.com confirms 8 facilities. SNFs acquired from Embassy Healthcare ~2024-2025 via Mission Management Services interim. |

### Notes
- LK Heritage Villas LLC is confirmed as Heritage Retirement Communities' holding entity (Steinmetz is registered agent).
- The 3 SNFs transitioned Embassy → Mission Management Services (interim turnaround) → Heritage Retirement Communities.
- "Heritage Villas" (ID 11964, entity INDEPENDENT) at 905 Pittsburg Ave NW is the same campus as LK Heritage Villas LLC rows (917/919 Pittsburg Ave NW) — 3 rows, 1 campus.

**V25 action:** Consolidate 4 DB rows under new entity "Heritage Retirement Communities." Investigate whether remaining Heritage HC SNFs in Lyndhurst/Painesville are in DB under Embassy.

**Researched:** 2026-03-21, MUO Candidate Evaluation (board review).

---

## PINNACLE LIVING (VA)

**Canonical DB name:** `Pinnacle Living`
**DB entity ID:** TBD (currently scattered across 4 corporate_name variants)
**DB variants found:** PINNACLE (3 rows), Pinnacle Living (5 rows), Pinnacle Senior Living (1 row), Pinnacle Supportive Living (1 row — misattributed, actually Vantage Senior Care)
**DB facility count:** 14 rows — only 8 are real Pinnacle Living (VA), 5 WI belong to Pennant Group, 1 IL belongs to Vantage Senior Care
**Portfolio:** 6 communities, all VA. Nonprofit, formerly Virginia United Methodist Homes, Inc.
**SNFs:** Yes — 2 small CCRCs (Cedarfield 20 beds CMS 495434, WindsorMeade 22 beds CMS 495402) under legal name "Virginia United Methodist Homes, Inc."
**Footprint campuses:** 6 (VA)
**7+ Gate:** FAIL (6 campuses)

### Cross-Reference
| Source | Result |
|---|---|
| CMS (Feb 2026) | 2 SNFs under legal name "Virginia United Methodist Homes, Inc." — Cedarfield (Richmond, 20 beds) and WindsorMeade (Williamsburg, 22 beds). No chain ID assigned. |
| Web | pinnacleliving.com confirms exactly 6 communities: Cedarfield, Hermitage Deep Run, Hermitage Richmond, Hermitage Roanoke, Hermitage Three Chopt, WindsorMeade. |

### DB Corrections Identified
| Facility | State | DB Corporate_Name | Correct Corporate_Name | Evidence |
|---|---|---|---|---|
| Madison Pointe Senior Living | WI | PINNACLE | The Pennant Group | pennantgroup.com portfolio |
| Kenosha Senior Living | WI | Pinnacle Living | The Pennant Group | pennantgroup.com portfolio |
| North Point Senior Living | WI | Pinnacle Living | The Pennant Group | pennantgroup.com portfolio; also city wrong (Racine → Somers) |
| Pleasant Point Senior Living | WI | Pinnacle Living | The Pennant Group | pennantgroup.com portfolio |
| Meadow View Assisted Living | WI | Pinnacle Senior Living | The Pennant Group | pennantgroup.com portfolio |
| New City Supportive Living | IL | Pinnacle Supportive Living | Vantage Senior Care | Gardant was original announced manager, Vantage took over |
| 3 Hermitage Roanoke rows | VA | PINNACLE | Pinnacle Living | GLR vs NIC-B source mismatch |

**V25 action:** Reattribute 5 WI → Pennant Group, 1 IL → Vantage Senior Care, normalize 3 VA naming inconsistencies.

**Researched:** 2026-03-20, MUO Candidate Evaluation (board review).

---

## NAVION SENIOR SOLUTIONS

**Canonical DB name:** `Navion Senior Solutions` (needs entity consolidation)
**DB entity IDs:** 12, 569, 590 (all same operator — consolidate)
**DB variants found:** NAVION SENIOR SOLUTIONS, Navion Senior Living, Navion Senior Solutions LLC
**DB facility count:** 57 rows (56 Navion + 1 misattributed to Brookdale)
**Legal entity:** Senior Ravn Solutions LLC
**HQ:** 5430 Wade Park Blvd Ste 402, Raleigh, NC
**CEO:** Beverly Janco Tuttle (Jan 2025). Chairman: Stephen Morton (founder).
**Portfolio:** 51 AL/MC/IL communities, 7 states. Family-owned, no PE.
**SNFs:** No (CMS confirmed zero matches)
**Footprint campuses:** 42 — NC(24), SC(16), KY(1), VA(1)
**7+ Gate:** PASS

### Timeline
| Date | Event | Source |
|---|---|---|
| 2015 (May) | Stephen Morton and Arick Morton co-found **Ravn Senior Solutions** in Raleigh, NC. Morton previously co-founded SALI (41 communities, sold to Brookdale 2006), then led Bell Senior Living (sold to Five Star 2012). | [SHN](https://seniorhousingnews.com/2025/01/13/navion-senior-solutions-names-new-ceo-preparing-for-rapid-growth-in-2025/) |
| 2017 | Rebranded from Ravn to **Navion Senior Solutions**. NHI purchased 2 NC communities for Navion. | [BusinessWire/NHI](https://www.businesswire.com/news/home/20171218005101/en/NHI-Announces-Acquisition-North-Carolina-Assisted-LivingMemory) |
| 2019 (Sep) | Partnered with Longview/Blackstone to manage 10 communities (KY, SC, TN, VA). Portfolio tripled ~4→14. | [SHN](https://seniorhousingnews.com/2019/09/23/navion-partners-with-blackstone-affiliate-to-manage-10-senior-living-properties/) |
| 2021 (Oct) | DHC transitions 5 former Five Star AL communities in SC to Navion management (259 units). | [CityBiz](https://www.citybiz.co/article/151547/diversified-healthcare-trust-announces-further-management-transition-progress/) |
| 2022 | Portfolio reaches 36 communities. 19 owned, rest managed (NHI, Blackstone/Longview, DHC). | [SHN](https://seniorhousingnews.com/2022/05/24/after-growing-to-36-communities-navion-senior-living-turns-focus-to-operations/) |
| 2025 (Jan) | Beverly Janco Tuttle named CEO. Morton transitions to Chairman. | [SHN](https://seniorhousingnews.com/2025/01/13/navion-senior-solutions-names-new-ceo-preparing-for-rapid-growth-in-2025/) |
| 2026 | 51 communities across 7 states (NC, SC, GA, TN, KY, VA, WV). | navionseniorsolutions.com, A Place for Mom, Seniorly |

### Cross-Reference
| Source | Result |
|---|---|
| CMS (Feb 2026) | Zero matches. No SNFs. |
| DB (V24.1) | 57 rows across 3 entity IDs. 1 misattribution (Navion of Goldsboro under Brookdale entity 3). |
| Web | 51 communities confirmed. Mixed ownership: ~19 owned, rest managed for NHI, Blackstone/Longview, DHC. |

### Notes
- **Not a Five Star rebrand.** Navion is an independent company. Morton's career path: SALI → Bell → Five Star (via sale) → founded Navion. Later took management of 5 former Five Star SC properties from DHC.
- "Five Star" DB search returned 5 Indiana operators — completely unrelated.
- "Diversified Healthcare" DB search returned 0 rows.
- Arick Morton left Navion to start VisionLTC (became NIC MAP Vision).

**V25 action:** Consolidate entity IDs 12/569/590. Reattribute Navion of Goldsboro (ID 9309) from Brookdale. DB-to-web facility-level matching pending.

**Researched:** 2026-03-21, MUO Candidate Evaluation (board review).

---

## GARDANT MANAGEMENT SOLUTIONS

**Canonical DB name:** `GARDANT MANAGEMENT SOLUTIONS` (needs entity merge)
**DB entity IDs:** 34, 465 (same operator — consolidate to 34)
**DB facility count:** 61 rows
**HQ:** Bourbonnais, IL
**Structure:** ESOP-owned. 5th largest AL/MC provider in US.
**Portfolio:** ~100 AL/MC/IL communities, 6 states (IL, IN, OH, MD, WV, VA). Zero SNFs.
**SNFs:** No (CMS confirmed zero matches)
**Footprint campuses:** 21 — IN(15), OH(5), VA(1)
**7+ Gate:** PASS

### Cross-Reference
| Source | Result |
|---|---|
| CMS (Feb 2026) | Zero matches. No SNFs. |
| DB (V24.1) | 61 rows, 2 entity IDs. 5 misattributed footprint facilities found under other corporate names (Pathways, INDEPENDENT, ProMedica, Frontier). |
| Web | ~100 communities. ESOP-owned. |

### Notes
- 5 misattributed facilities in EWH footprint need reattribution to Gardant (4 OH, 1 IN — currently under other corporate names)
- 2 duplicate rows in footprint need deletion
- Facility name error: "CARRIAGE COURT GROVE OF CITY" → "CARRIAGE COURT OF GROVE CITY"
- Missing county: Green Oaks of Goshen → Elkhart County

**V25 action:** Merge entity 465→34. Reattribute 5 misattributed facilities. Delete 2 duplicates. Fix name error and missing county.

**Researched:** 2026-03-21, MUO Candidate Evaluation (board review).

---

## RETIREMENT UNLIMITED, INC. (RUI)

**Canonical DB name:** `Retirement Unlimited, Inc.` (needs entity merge)
**DB entity IDs:** 1222, 1254 (same operator — consolidate to 1222)
**DB variants found:** Retirement Unlimited, Inc. (entity 1222, 16 rows), RUI (entity 1254, 2 rows)
**DB facility count:** 18 rows
**HQ:** Roanoke, VA
**Founders:** Fralin/Waldron families (est. 1982)
**Portfolio:** IL/AL/MC communities in VA + acquired Brandywine Living (31 communities NJ/CT/DE/MD/NY/PA) Dec 2023. Welltower partnership for Elance luxury brand.
**SNFs:** No (CMS confirmed zero matches)
**Footprint campuses:** 10 (all VA)
**7+ Gate:** PASS

### Cross-Reference
| Source | Result |
|---|---|
| CMS (Feb 2026) | Zero matches. No SNFs. |
| DB (V24.1) | 18 rows, 2 entity IDs. 3 FL misattributions, 1 phantom facility (never built), 4 duplicate pairs. |
| Web | VA-based family-owned. Brandywine acquisition Dec 2023 expanded to NJ/CT/DE/MD/NY/PA. |

### Notes
- 3 FL facilities misattributed to RUI: Watercrest Palm Beach Gardens (actual: Watercrest Senior Living), Capital Square Tallahassee and YOURLife of West Melbourne (actual: YourLife Senior Living)
- The Morgan at Ford's Village (ID 19866) — phantom facility, never built. RUI withdrew Jan 2025.
- 7 rows have surrogate bed counts (beds=72, census=58) — need real capacity data.
- 6 VA rows missing county values.
- 1 missing community: Elance at Old Town Alexandria (VA, RUI-managed) not in DB.

**V25 action:** Merge entity 1254→1222. Delete phantom + 4 duplicates (5 deletes). Reattribute 3 FL. Fix 6 missing counties. Add Elance Alexandria.

**Researched:** 2026-03-21, MUO Candidate Evaluation (board review).

---

## VITALITY LIVING

**Canonical DB name:** `Vitality Living`
**DB entity ID:** 605
**HQ:** Nashville/Brentwood, TN
**CEO:** Chris Guay
**Portfolio:** 30+ AL/MC/IL communities across southeastern US
**SNFs:** No (CMS confirmed zero matches)
**Footprint campuses:** 9 — KY(4), VA(4), SC(1)
**7+ Gate:** PASS

### Cross-Reference
| Source | Result |
|---|---|
| CMS (Feb 2026) | Zero matches. No SNFs. |
| DB (V24.1) | 26 rows under entity 605. 1 misattribution (Sunrise of Five Forks, ID 24632 — actual: Sunrise Senior Living). 2 stale corporate attributions (Watercrest Columbia SC acquired by Vitality May 2024; Acclaim at Belmont Bay VA management assumed Feb 2026). |

### Notes
- "Sunrise Of Five Forks" (ID 24632) is a Sunrise Senior Living facility wrongly attributed to Vitality Living.
- Vitality Living Columbia SC (ID 14192) still attributed to Watercrest — acquired by Vitality May 2024.
- Acclaim at Belmont Bay VA (ID 17123) still under Senior Lifestyle — Vitality assumed management Feb 2026.
- 3 facilities missing from DB: Aspen Alcove at Bardstown KY, Aspen Alcove at Elizabethtown KY, West End Richmond VA.
- Suspect bed count: Landing of Long Cove OH shows 17 beds in DB vs 82 units on website.

**V25 action:** Reattribute Sunrise misattribution. Update 2 stale corps. Add 3 missing facilities. Fix bed count.

**Researched:** 2026-03-21, MUO Candidate Evaluation (board review).

---

## TRIPLE CROWN SENIOR LIVING (formerly Vitality Senior Services)

**Canonical DB name:** `Triple Crown Senior Living` (needs entity merge + rename)
**DB entity IDs:** 434 ("VITALITY SENIOR SERVICES"), 544 ("Vitality Senior Services") — same company, consolidate
**DB variants found:** VITALITY SENIOR SERVICES, Vitality Senior Services
**HQ:** Louisville, KY
**CEO:** Todd Marsh
**Portfolio:** 14 AL/MC/IL communities
**SNFs:** No (CMS confirmed zero matches)
**Footprint campuses:** 9 — KY(5), IN(3), OH(1)
**7+ Gate:** PASS

### Cross-Reference
| Source | Result |
|---|---|
| CMS (Feb 2026) | Zero matches. No SNFs. |
| DB (V24.1) | Split across 2 entity IDs (434, 544) with stale brand name "Vitality Senior Services." |

### Notes
- **Completely unrelated to Vitality Living (entity 605).** Different ownership, different HQ, different markets.
- Rebranded from "Vitality Senior Services" to "Triple Crown Senior Living" — DB still uses old name.
- 3 duplicate pairs identified: Elizabethtown KY, Summit of Edgewood KY, Watercrest Columbia SC.
- 3 facilities missing from DB.

**V25 action:** Merge entity 544→434. Rename corporate_name_raw to "Triple Crown Senior Living." Delete duplicates. Add missing facilities.

**Researched:** 2026-03-21, MUO Candidate Evaluation (board review).

---
