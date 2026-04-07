# MUO Corporate History Log

Tracks corporate-level events — mergers, acquisitions, divestitures, rebrands, name changes — for operators in the Combined Database. Entries are added during V23 scoring research, fuzzy match reconciliation (Punchlist #4), MUO candidate evaluations, and facility dedup review.

**Purpose:** Preserve research so it doesn't have to be repeated. When an operator comes up in scoring, pipeline review, or stakeholder conversations, check here first.

**Companion files:**
- `reference/Facility_Acquisitions_Log.md` — facility-level CHOW events (individual facility ownership changes)
- `scripts/audit_reports/Corporate_Name_Dedup_Review_ra_v2.xlsx` — fuzzy match decisions and canonical names
- `changelogs/V22_8_to_V22_9_Fuzzy_Match_Consolidation.md` — confirmed same/different determinations from V22.9
- `Vault/03_Corporate_Accounts/MUO_Profiles/` — 22 standardized MUO Profile markdown files (Wave 1-3)
- `current/6.3_Corporate_Scoring_Methodology_V23.md` — V23 scoring methodology (V23.8)
- `changelogs/2026-03-11_RS_Score_Reconciliation_V20_vs_V23.md` — Brooke vs Tom RS reconciliation

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

## UNITED METHODIST CLUSTER (disambiguation)

**Not a single entity.** The DB contains 7 distinct organizations that share "United Methodist" in their name due to denominational affiliation. Each is an independently governed nonprofit with its own board, EIN, and covenant relationship with a regional United Methodist Conference. No corporate parent-child relationship exists between any of them.

### THE UNITED METHODIST RETIREMENT HOMES, INC (UMRH) — umrh.org
**Canonical DB name:** `THE UNITED METHODIST RETIREMENT HOMES, INC`
**Also in DB as:** `UNITED METHODIST RETIREMENT HOMES INC` (row 94 resolved → SAME)
**Location:** NC (Durham, Lumberton, Greenville)
**Communities:** Croasdaile Village (Durham), Wesley Pines (Lumberton), plus Greenville campus
**Served:** 6 facilities (Croasdaile Clinic, Croasdaile Village SNF/ALF, Wesley Pines SNF/ALF)
**CMS:** No chain ID. SNFs operate under UMRH legal name directly.
**GLR:** Wesley Pines (109 pts), Croasdaile Village (31 pts), Croasdaile Clinic (0 pts), Croasdaile Friendship House (0 pts)
**Leadership:** Jonathan P. Erickson, Corporate Executive Director (since 2007)
**Notes:** Faith-based nonprofit, serves ~1,800 seniors across NC. Three Life Plan Communities + one affordable housing community.

### ALDERSGATE UNITED METHODIST RETIREMENT COMMUNITY, INC — aldersgateliving.org
**DB names:** `ALDERSGATE UNITED METHODIST RETIREMENT COMMUNITY, INC`, `ALDERSGATE UMRC, INC`
**Location:** Charlotte, NC (3800 Shamrock Dr)
**EIN:** 56-0547462
**Served:** 0
**CMS:** No chain ID.
**GLR:** Aldersgate Retirement Community - Asbury (SNF, 46 pts) — listed under "Life Plan Community," not UMRH.
**Notes:** Founded 1945 as "The Methodist Home." ~$40M annual revenue. 346 IL/AL units, 125 SNF beds, 61 memory support. Near insolvency 2023 — NC DOI issued order of supervision. Affiliating with Givens Communities (Asheville-based nonprofit) as of 2025. Completely separate from UMRH.

### UNITED METHODIST HOMES (UMH) — unitedmethodisthomes.org
**DB name:** `UNITED METHODIST HOMES`
**Location:** Binghamton, NY / NE Pennsylvania
**Facilities:** 5 (Elizabeth Church Campus Binghamton NY, Hilltop Campus Johnson City NY, Tunkhannock PA, Wesley Village Pittston PA, plus 1)
**Served:** 0
**CMS:** Chain ID 534 (2 SNFs: Elizabeth Church Manor 120 beds, Wesley Village 160 beds)
**Notes:** Founded 1958 in Scranton PA. Serves 1,100+ residents, 1,000+ employees. Entirely outside our 6-state footprint.

### WESBURY UNITED METHODIST COMMUNITY — wesbury.com
**DB name:** `WESBURY UNITED METHODIST COMMUNITY`
**Location:** Meadville, PA (31 North Park Ave, 110-acre campus)
**Served:** 0
**Notes:** Founded 1913. Covenant with East Ohio UM Conference. Full CCRC — IL, personal care, SNF, memory care, rehab. Standalone single-campus nonprofit. Outside footprint.

### COPELAND OAKS (Copeland United Methodist) — copelandoaks.com
**DB name:** `COPELAND UNITED METHODIST`
**Location:** Sebring, OH (250-acre campus)
**Served:** 0
**Notes:** Founded 1963 (Cope family land donation), opened 1967 as "The Cope Methodist Home." Covenant with East Ohio UM Conference (same as Wesbury, but independent org). Includes Crandall Medical Center (SNF). In footprint (OH) but single campus.

### QUINCY UNITED METHODIST HOME
**DB name:** `QUINCY UNITED METHODIST HOME`
**Location:** Quincy, PA
**Served:** 0
**Notes:** Small nursing home. Web research suggests may now be affiliated with or acquired by Presbyterian Senior Living (Quincy Village). Outside footprint.

### UNITED METHODIST RETIREMENT (KY)
**DB name:** `UNITED METHODIST RETIREMENT`
**Location:** KY (1 facility)
**Served:** 0
**Notes:** Single facility in KY. Minimal footprint.

### Also related: PINNACLE LIVING (VA)
Formerly "Virginia United Methodist Homes, Inc." — separate entry in this file. Rebranded, no longer uses Methodist name. 6 VA campuses, fails 7+ gate.

**Resolved:** 2026-03-21, Punchlist #4 rows 77/95/97/106/109/110/112/127/132/135/136/140. All 12 pairs → NOT THE SAME. Row 94 (UMRH internal variant) was previously resolved → SAME.

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

# Pre-V23 Corporate Research History (November 2025 - January 2026)

The MUO profiling and corporate scoring work did not begin with V23. The research arc started in November 2025 during the initial database build and evolved through several methodology iterations before reaching the standardized V23 framework.

---

## Foundation Phase (November 2025)

### Eventus Corporate Initiative Technical Brief
- **Date:** November 2025
- **File:** `archive/foundation/Eventus_Corporate_Initiative_Technical_Brief_Nov2025.md`
- **Database:** V18.1 Economic Model
- **Scope:** Established the Phase 3C Corporate Tiering framework using the integrated SNF + ALF model. Defined the financial computation layer (Phase 3B) with fixed ALF rates ($1,875 PCP, $1,898 MH), the TAM/SAM/SOM barrier-sensitive funnel model, and the market framework for corporate revenue opportunity assessment.
- **Significance:** This is where corporate-level analysis first became a formal workstream — before this, the database was facility-level only.

### American Senior Communities Analysis (Earliest Dated Corporate Deep Dive)
- **Date:** November 22, 2025
- **File:** `Vault/03_Corporate_Accounts/MUO_Profiles/Reference/American_Senior_Communities_Analysis.pdf`
- **Database:** V18.1
- **Scope:** Deep dive covering American Senior Communities (150 facilities, $32.78M opportunity), American Health Communities, American Healthcare LLC, and smaller American-branded entities.
- **Significance:** First standalone corporate operator research document. Predates the scoring framework by a month.

---

## V20 Scoring Framework (December 2025)

### Brooke's Working Scoresheet
- **Date:** December 19, 2025
- **File:** `Vault/03_Corporate_Accounts/Tiering/Archive/2025-12-19_Scoring_Tiering_Working.xlsx`
- **Scope:** Hand-scored entries using the 6-dimension weighted framework. First application of Enterprise Reach, Integration Readiness, Strategic Influence, Revenue Potential, Relationship Strength, and AI/Tech Adoption dimensions to real entities.

### V20 Core Rulebook & Scoring Methodology
- **Date:** December 2025 (marked PRODUCTION READY)
- **Files:**
  - `current/6_Core_Rulebook_V20_0.md` — governs fee structure, scenario calculations, QC protocol
  - `current/6.3_Corporate_Scoring_Methodology_V20.md` — scoring specifics, dimension definitions, weighting rationale
- **Database:** V20.0 Combined (20,943 facilities)
- **Coverage:** 70 corporate entities in initial scoring universe
- **Significance:** First formalized, documented methodology. Established the 6-dimension model, the weighting scheme (ER×4, IR×3, SI×3, RP×4, RS×3, AI×3), and the tier thresholds that V23 later refined.

### First Formal Tiered Ranking
- **Date:** December 2025
- **File:** `Vault/03_Corporate_Accounts/Tiering/Archive/Final_MUO_Tiering_V20.xlsx`
- **Scope:** T1, T2, T3 rankings for 70 entities. First time corporate operators were formally ranked for BD prioritization.

### MUO Consolidated Revenue Scoring Workbook
- **Date:** December 16, 2025
- **File:** `Vault/03_Corporate_Accounts/MUO_Profiles/Reference/MUO_Consolidated_Revenue_Scoring.xlsx`
- **Trigger:** December 8 board request for corporate revenue opportunity data
- **Scope:** Top 5 MUOs with detailed revenue breakdowns. Built in 8 days for board consumption.

---

## V21 Methodology Debates (January 2026)

### V21 Alternative Methodology — Ops View
- **Date:** January 6, 2026
- **File:** `Vault/03_Corporate_Accounts/Tiering/Archive/V2 with Roians surrogate values/6.4_Corporate_Tiering_Methodology_Ops_View_V21_2 1.md`
- **Scope:** Rule-based segmentation (Geography + Revenue Potential) as an alternative to V20's weighted-scoring approach. Separated objective criteria (facility count, revenue) from subjective factors ("% Eventus Fit").
- **Requested by:** Clinical Ops team, for capacity planning purposes
- **Outcome:** Not adopted as primary. BD tiering (V20 weighted model) retained as governance layer.

### BD vs Clinical Tiering Alignment
- **Date:** January 14, 2026
- **File:** `Vault/03_Corporate_Accounts/Tiering/Archive/BD_Clinical_Tiering_Alignment.md`
- **Issue:** Sales (V20) and Clinical (V21) had conflicting tier assignments for the same accounts
- **Resolution:** BD tiering (V20) governs strategic prioritization. Clinical owns execution within the BD tier structure. One truth, two lenses.
- **Significance:** Established the principle that scoring is a governance layer, not a departmental tool — a precursor to the Data Domain Definitions (Sales) initiative.

---

## Original Research Artifacts (Pre-Standardization)

These DOCX/PDF source documents predate the standardized markdown template and are preserved in `Vault/03_Corporate_Accounts/MUO_Profiles/Reference/`:

| File | Format | Subject | Notes |
|------|--------|---------|-------|
| `American_Senior_Communities_Analysis.pdf` | PDF (142KB) | ASC deep dive | Nov 22, 2025 — earliest dated |
| `ClearView_Healthcare_Management_MUO_Profile.docx` | DOCX (17KB) | ClearView | Original profile before MD conversion |
| `Primrose_Retirement_Communities_Profile.docx` | DOCX (15KB) | Primrose | Original profile before MD conversion |
| `Zanziper_Portfolio_Analysis.docx` | DOCX (41KB) | Zanziper | Regulatory/ownership analysis |
| `Trilogy.pdf` | PDF (182KB) | Trilogy | Supporting documentation |
| `Majestic_Email_Would_Like_Your_Perspective.pdf` | PDF (323KB) | Majestic Care | Client correspondence |
| `MUO_Consolidated_Revenue_Scoring.xlsx` | XLSX (6.5KB) | Top 5 MUOs | Dec 16, 2025 board response |
| `Corporate_Scoring_Reference_Slide.md` | MD (6.5KB) | Scoring visual | Reference for presentations |

---

# V23 MUO Scoring Research (February-March 2026)

22 corporate entities received deep-dive research during the V23 Corporate Scoring update. Research included CMS federal data cross-reference, state Secretary of State filings, company websites, industry press (McKnight's, Senior Housing News, Healthcare Finance News), ownership records, and LinkedIn. Each entity received a standardized MUO Profile (10-section Kisco template) saved to `Vault/03_Corporate_Accounts/MUO_Profiles/`.

**Scoring outputs:**
- MUO Scoring Workbook V23 (v8) — Finance 60 universe, 9 tabs with facility-level detail
- Final MUO Tiering V23 — BD universe, 84 entities (21 T1, 34 T2, 6 T3, 7 T4, 16 T5)
- BD Complete MUO Universe V23 — 100-entity HTML view with stacked tiers and entity hyperlinks
- BD MUO Breakouts — individual entity deep-dive pages (business desc, leadership, service penetration, scoring)

---

## Wave 1: Profile Conversions (8 entities, completed March 2, 2026)

Legacy DOCX/PDF profiles converted to standardized markdown template with full research refresh.

### ALG SENIOR LIVING
**V23 Tier:** T1 (Score: 64)
**Footprint:** NC | 65 facilities, 65 served
**Research focus:** Financial distress analysis. LTC Properties REIT acquired majority ownership after 2024 restructuring. Evaluated stability risk and implications for service continuity.
**Profile:** `ALG_MUO_Profile.md`

---

### AMERICAN SENIOR COMMUNITIES
**V23 Tier:** T1 (Score: 83)
**Footprint:** IN | 150 DB / ~102 public
**Research focus:** Ownership history (Jackson family / David Justice operator; HHC facilities). I-SNP analysis — launched largest provider-owned I-SNP network Jan 2025. Significant strategic influence signal.
**Profile:** `American_Senior_Communities_MUO_Profile.md`

---

### KISCO SENIOR LIVING
**V23 Tier:** T1* (Score: 58, proposed)
**Footprint:** NC, FL | 19 DB / 32 public
**Research focus:** Nationally significant operator substantially undercounted in DB. Welltower REIT partnership. NIC board representation. Public research confirmed portfolio much larger than DB reflects.
**Profile:** `Kisco_Senior_Living_MUO_Profile.md`

---

### LIBERTY HEALTH
**V23 Tier:** T1 (Score: 63 → 82 in V23)
**Footprint:** NC, SC, TN, FL | 76 facilities (V22.4)
**Research focus:** Leadership team research. Liberty Advantage ISNP analysis. RS upgrade based on Tom's field notes — RFP proposal activity indicating growing engagement.
**Profile:** `Liberty_Health_MUO_Profile.md`

---

### LUTHERAN LIFE VILLAGES
**V23 Tier:** T2* (Score: 39, proposed)
**Footprint:** IN | 10 DB / 6 campuses
**Research focus:** V22.4 DB + public research. T4 classification — 6 qualifying campuses, 1 short of MUO gate. Faith-based nonprofit.
**Profile:** `Lutheran_Life_Villages_MUO_Profile.md`

---

### SOUTHERN HEALTHCARE MANAGEMENT
**V23 Tier:** T2 (Score: 32 → 61 in V23)
**Footprint:** FL, GA, NC | 46 DB / 33 public
**Research focus:** **Identity consolidation deep dive.** Discovered Sovereign Healthcare Holdings was the same entity as Southern Healthcare Management — different name layers for the same operator. Split existed since V20 (separate T2 entries for "Southern Assisted Living LLC" and "Sovereign Healthcare Holdings"). Consolidated using CMS federal data matching + address verification + corporate history. IR upgrade (+6 points) recognizing integrated campus operations.
**Profile:** `Southern_Healthcare_Management_MUO_Profile.md`

---

### TRIPLE CROWN SENIOR LIVING (formerly Vitality Senior Services)
**V23 Tier:** T2* (Score: 41, proposed)
**Footprint:** KY, IN, OH, TN, TX | 4 DB / 14 public
**Research focus:** V22.4 DB + public research. T4 classification (4 qualifying campuses at time of V23). Louisville's #1 fastest-growing private company (2025). CEO/President research. Rebrand from Vitality Senior Services discovered.
**Profile:** `Triple_Crown_Senior_Living_MUO_Profile.md`
**Note:** Later passed 7+ gate after V24.2 corrections (9 footprint campuses). See MUO Candidate Evaluation entry above.

---

### ZANZIPER / PORTOPICCOLO GROUP (Simcha Hyman & Naftali Zanziper)
**V23 Tier:** T2* (Score: 39, proposed)
**Footprint:** 10 states | 115 DB / 200+ public | 131 CMS-affiliated (as of March 2025)
**Research focus:** **Regulatory and ownership structure deep dive.** CON mapping, regulatory analysis, consolidated facility list. 100% barriered — owns provider group + alliance. $12M+ CMS fines since 2021. The Ivy at Great Falls closure. Opaque layered ownership (Portopiccolo Group / 980 Investments). T5 barrier classification.
**Profile:** `Zanziper_MUO_Profile.md`

#### Ownership & Holding Structure (confirmed 2026-03-30)
- **Principals:** Simcha Hyman (CEO) & Naftali Zanziper (President)
- **Parent entity:** Portopiccolo Group LLC (NY-based PE, formed ~2016 after selling medical supply company)
- **Holding chain:** Portopiccolo Group → Accordius SNF Holdco LLC → MC M53 Spe Opco Holdco → individual facility OpCo LLCs
- **Related trusts/entities:** HC Family Trust, SHNZ Holdings LLC, Wyncote LLC, Zanziper Family Trust
- **Key individuals on CMS filings:** Kimberly Morrow (W2 managing employee), Batya Gorelick (corporate officer)

#### Regional Management Brands
Portopiccolo does not operate under a single brand. Facilities are managed through regional management companies that do not reference Portopiccolo in their public-facing materials:

| Brand | Region | HQ | Website | Notes |
|---|---|---|---|---|
| **Accordius Health LLC** | NC (primary) | — | — | Largest NC brand; also used as CMS "operator" name nationally. Down to 1 facility in DB footprint (Midwood, Charlotte). |
| **August Healthcare** / August Healthcare Group | Eastern NC + VA | Englewood Cliffs NJ (shared address with Portopiccolo) | augusthcg.com | 9 facilities (6 NC, 3 VA). Founded Sept 2021 by Ben Cohen (ex-Hyman company ACG). CMS shows Augustnc Holdco LLC / Itamar Cohen as owner. Portopiccolo spokesman denied ownership but shared HQ, direct Accordius transfers, PropCo still Portopiccolo. Confirmed via UC Berkeley investigative journalism, ProPublica CMS filings. |
| **YAD Healthcare** | NC, SC, VA | — | yadhealth.com | 19+ facilities in DB. Operates Clayton, Eden, Goldsboro, Wallace, Wilson (Downing St) + others. NC East Holding LLC / Tzvi Alter ownership per CMS. Websites say "A proud member of YAD Healthcare." |
| **Alliance Health Group** | NC, FL | — | alliancehealthgrp.com | 10+ facilities in DB. Operates Cypress Valley, Lotus Village, Ridge Valley + Camellia Gardens, Cedar Hills, Dahlia Gardens, Linden Place, Magnolia Gardens, Mill Creek, Piedmont Hills, Pine Acres, Willow Valley. Facility websites redirect to alliancehealthgrp.com. |
| **Clearview Healthcare Management** | KY / TN | Louisville, KY | clearviewhcmgmt.com | 28 facilities in DB (8 already coded CLEARVIEW + 20 recoded from Hyman/Zanziper). All KY Portopiccolo facilities. |
| **Maple Health Group** | NC (some facilities) | Unknown | — | Copyright notice on glenwoodrnc.com and salisburyrnc.com. 2 facilities: Glenwood (Mooresville), Salisbury. Not found as registered entity. Salisbury may have CHOWed to Hill Valley (Meadowbrook SNF Ops, 5/1/2025). |
| **Citadel** | Facility-level LLCs | — | — | Used in OpCo names (Citadel Mooresville LLC, Citadel at Myers Park LLC). Myers Park CMS-decertified Mar 2025, reopened under CARE Management. |
| **Pelican Health** | NC (some facilities) | — | — | Charlotte-area facilities. Pelican Health Randolph and Pelican Health at Charlotte both CHOWed to Hill Valley. Pelican Health Henderson (Camellia Gardens ALF, Durham) — verification pending. |

#### DB Corporate Name Standardization (Phase 3, completed 2026-04-01)
All 39 rows coded "SIMCHA HYMAN & NAFTALI ZANZIPER" recoded to actual operator brand. Decision: code the clinical/business decision-maker (regional operator), not the PE parent (Portopiccolo) or CMS-listed owner principals.

| New Corp Name | Rows Recoded | Region |
|---|---|---|
| CLEARVIEW | 20 | KY (joins 8 existing) |
| YAD HEALTHCARE | 5 | NC (joins 19 existing) |
| AUGUST HEALTHCARE | 4 | NC (1 Rose Manor) + VA (2) + NC (1 variant fix) |
| ALLIANCE HEALTH GROUP | 3 | NC (joins 10 existing) |
| HILL VALLEY HEALTHCARE | 1 | NC Concord (new CHOW #7) |
| CARE MANAGEMENT | 1 | NC Myers Park (CMS decertified, new operator) |
| MAPLE HEALTH GROUP | 2 | NC Glenwood + Salisbury (Salisbury may be Hill Valley) |
| ACCORDIUS HEALTH | 1 | NC Midwood (last Accordius facility) |

Previously standardized (Phase 2): 6 rows ACCORDIUS HEALTH LLC/PORTOPICCOLO GROUP → HILL VALLEY HEALTHCARE.
Also corrected: 1 row AUGUST HEALTHCARE GROUP → AUGUST HEALTHCARE (variant fix), 1 row MONROE PROPCO LLC deleted (PropCo, dedup Pair 16).
Remaining after Phase 3 (verified 2026-04-04):
- **Camellia Gardens Durham NC (PELICAN HEALTH HENDERSON):** RESOLVED → ALLIANCE HEALTH GROUP. ProPublica shows Alliance Health Group LLC managerial control since Aug 2024. alliancehealthgrp.com has dedicated community page. Recode to ALLIANCE HEALTH GROUP.
- **Beavercreek Health & Rehab OH (SIMCHA HYMAN & NAFTALI ZANZIPER):** Still Portopiccolo. ProPublica: Flyer 1 Operations Holdings LLC (100%), Naftali Zanziper indirect. Chain = Hyman/Zanziper. OH management brand unknown — no regional brand mapped for OH. Website behind CAPTCHA. Logged to follow-up tracker.
- **Achieve Rehabilitation SC (SIMCHA HYMAN & NAFTALI ZANZIPER):** Still Portopiccolo. ProPublica: Hyman 50% + Zanziper 50% direct. No managing entity listed. SC management brand unknown — single SC facility. Website returned 403. Logged to follow-up tracker.
- **Salisbury Rehab & Nursing NC (MAPLE HEALTH GROUP):** Likely Hill Valley CHOW #8. meadowbrook-hr.com follows the Hill Valley URL convention ([name]-hr.com) but site is currently down (ECONNREFUSED). Logged to follow-up tracker — confirm when site comes back online.

#### Hill Valley Healthcare CHOW — 7 NC Facilities Divested (2024-2025)
Between December 2024 and May 2025, Portopiccolo divested **7** NC skilled nursing facilities to **Hill Valley Healthcare** (see separate entry below). An 8th (Salisbury) may also have transferred (closing date 5/1/2025, pending confirmation).

| DHSR Record | Former DB Name | Address | New Facility Name | New OpCo LLC | CHOW Date |
|---|---|---|---|---|---|
| 4648 | Accordius Health at Monroe | 204 Old Hwy 74 E, Monroe | Stratford Manor H&R | Rock Rest SNF Ops LLC | Dec 1, 2024 |
| 4649 | Accordius Health at Charlotte | 5939 Reddman Rd, Charlotte | Redwood H&R | Eastland SNF Ops LLC | Dec 1, 2024 |
| 4650 | Pelican Health Randolph / Sherwood | 4801 Randolph Rd, Charlotte | Sherwood H&R | Randolph Gardens SNF Ops LLC | Dec 1, 2024 |
| 4651 | Pelican Health at Charlotte | 2616 E 5th St, Charlotte | Plaza H&R | Eastover SNF Ops LLC | Dec 1, 2024 |
| 4652 | Accordius Health at Gastonia | 416 N Highland St, Gastonia | Belmont H&R | Heights SNF Ops LLC | Dec 1, 2024 |
| 4743 | Accordius Health at Mooresville | 752 E Center Ave, Mooresville | Crestview H&R | Crestview SNF Ops LLC | May 1, 2025 |
| TBD | Accordius Health at Concord | 515 Lake Concord Rd NE, Concord | Copperfield H&R | Copperfield SNF Ops LLC | May 1, 2025 |
| TBD | Salisbury Rehabilitation & Nursing | 635 Statesville Blvd, Salisbury | Meadowbrook H&R (?) | Meadowbrook SNF Ops LLC (?) | May 1, 2025 (?) |

**Source:** NC DHSR Certificate of Need exemption filings (Records 4648-4652 filed Oct 30, 2024; Record 4743 filed 2025). Concord discovered via copperfield-hr.com (Twin Pines branding) during Phase 3 research. Salisbury flagged via meadowbrook-hr.com — pending confirmation.

#### Other Portopiccolo Departures (non-Hill Valley)
- **The Citadel at Myers Park** (300 Providence Rd, Charlotte) — CMS terminated provider agreement March 7, 2025 (Immediate Jeopardy findings Dec 2024 / Feb 2025). Reopened as **Myers Park Nursing Center** under **CARE Management Company** (myersparknc.com). No longer Portopiccolo.
- **17 VA facilities** divested to Eastern Healthcare Group in 2023 (per SoVaNOW reporting). 12 of 17 had 1-star CMS ratings at time of transfer.

#### Facility Name History Chains (confirmed 2026-03-30)
- CCN 345179 (Mooresville): Brian Center H&R → Accordius Health at Mooresville → **Crestview Health & Rehabilitation** (current, Hill Valley)
- CCN 345134 (Charlotte): Avante at Charlotte → Sherwood Health and Rehab → Pelican Health Randolph → **Sherwood Health & Rehabilitation** (current, Hill Valley)
- CCN 345345 (Monroe): Brian Center H&R Monroe → Accordius Health at Monroe → **Stratford Manor Health & Rehabilitation** (current, Hill Valley)
- CCN 345406 (Gatesville): Down East Living & Rehab → Accordius Health and Rehabilitation → **Gates Health and Rehab** (current, still Portopiccolo/August Healthcare)
- CCN 345283 (Mooresville Glenwood): The Citadel Mooresville → **Glenwood Rehabilitation and Nursing Center** (current, still Portopiccolo/Maple Health Group)

#### Dup Pairs Discovered During This Research (2026-03-30)
5 address-level dup pairs found within the Portopiccolo footprint — all resolved in dedup decisions log (Pairs 14-18).

---

### HILL VALLEY HEALTHCARE
**V23 Tier:** Not scored (new to our footprint via CHOW)
**Footprint:** 6 states (MD, NV, TN, VA, WA, WV) + NC as of Dec 2024 | 39+ CMS-affiliated facilities (ProPublica affiliate a-270)
**Canonical DB name:** TBD — recommend HILL VALLEY HEALTHCARE

#### Company Profile (researched 2026-03-30)
- **Founded:** 2018, Flushing NY
- **Type:** Boutique national SNF operator
- **Description:** "Healthcare support platform that enhances senior living communities through compassionate, personalized care"
- **Size:** ~110 employees, 39+ facilities
- **Services:** Skilled nursing, assisted living, memory care, clinical support
- **Recent M&A:** 3 Riverside Lifelong Health facilities VA (2021), Cortland Acres WV (Sept 2024), 2 VA SNFs for $82.4M (2026), 6 Portopiccolo NC facilities (Dec 2024 / May 2025)

#### NC Operations — Twin Pines Healthcare
Hill Valley operates its NC facilities through a consulting/management brand called **Twin Pines Healthcare**:
- **Website:** twinpineshc.com (metadata identifies Hill Valley Healthcare as parent org)
- **Phone:** (704) 773-5085 (Charlotte area code)
- **Description:** "Consulting company dedicated to supporting senior care communities"
- **Focus:** North Carolina's senior care communities

Evidence chain: NC DHSR CHOW filings → NPI registrations (authorized official Joseph Lieberman, VP Procurement at Hill Valley Healthcare per LinkedIn) → facility websites ([name]-hr.com pattern, all with "Serviced by Twin Pines Healthcare" footer) → Twin Pines website metadata identifying Hill Valley Healthcare as organization name.

#### 6 NC Facilities (all acquired from Portopiccolo/Accordius)
See CHOW table in Portopiccolo entry above. All carry [name]-hr.com websites with Twin Pines Healthcare branding.

#### Scoring Consideration
6 NC SNFs in our footprint. None currently served. All have Barrier=Alliance or Own Provider Group from the Portopiccolo era — barrier status may have changed under new ownership. Evaluate for scoring board when freeze lifts (June 6, 2026).

---

## Wave 2: Strawman Profiles (12 entities, March 2, 2026)

Entity research complete with proposed scoring. Facility lists and revenue calculations pending full build.

### ARBORS OF OHIO
**V23 Tier:** T2 (Score: 49)
**Footprint:** OH | 16 facilities
**Profile:** `Arbors_of_Ohio_MUO_Profile.md`

---

### ATRIUM CENTERS
**V23 Tier:** Scoring pending
**Footprint:** MI, OH, WI, KY | 27 DB / 26 CMS
**Research focus:** Database verification analysis — 27 facilities confirmed. T4 classification investigation (barrier status pattern similar to CommuniCare).
**Profile:** `Atrium_Centers_MUO_Profile.md`

---

### BHP / ENCORE
**V23 Tier:** T4
**Research focus:** Entity clarification investigation.
**Profile:** `BHP_Encore_MUO_Profile.md`

---

### BROOKDALE SENIOR LIVING
**V23 Tier:** T1 (Score: 69)
**Footprint:** Multi-state | 58 facilities
**Research focus:** NYSE: BKD analysis. Largest US senior living company. REIT partnerships (Welltower, DHC). Leadership research.
**Profile:** `Brookdale_Senior_Living_MUO_Profile.md`

---

### CARING PLACE HEALTHCARE
**V23 Tier:** T3 (Score: 17)
**Footprint:** OH | 10 facilities
**Research focus:** Psychosocial specialization analysis.
**Profile:** `Caring_Place_Healthcare_MUO_Profile.md`

---

### CASTLE HEALTHCARE
**V23 Tier:** T2 (Score: 47)
**Footprint:** IN | 12 facilities
**Research focus:** Market analysis. Brooke/Ian involvement notes.
**Profile:** `Castle_Healthcare_MUO_Profile.md`

---

### CLEARVIEW HEALTHCARE MANAGEMENT
**V23 Tier:** T2 (Score: 27)
**Footprint:** KY, TN | 5 DB / ~31 public
**Research focus:** **Data gap analysis.** Only 5 of ~31 CMS facilities in database. Tennessee entirely missing. Partnership research (Telos process).
**Profile:** `ClearView_Healthcare_Management_MUO_Profile.md`

---

### LIONSTONE CARE
**V23 Tier:** T2 (Score: 46)
**Footprint:** OH, NJ | 23 facilities
**Research focus:** Regional operator analysis. Relationship status.
**Profile:** `LionStone_Care_MUO_Profile.md`

---

### MAJESTIC CARE
**V23 Tier:** T1 (Score: 100)
**Footprint:** IN, OH, KY, MI, PA | 43 DB / 48 public
**Research focus:** **High-value opportunity deep dive.** Highest score in V20 universe (100/100). Marx Development Group parent company. $60M WV state facility acquisition (Nov 2025). $3.7M integration cross-sell opportunity identified (15 of 19 served are MH-only, conversion to integrated model).
**Profile:** `Majestic_MUO_Profile.md`

---

### PRIMROSE RETIREMENT COMMUNITIES
**V23 Tier:** T2* (Score: 47, proposed)
**Footprint:** OH, IN | 11 DB / ~34 public
**Research focus:** ALF operator shift analysis. Four new ownership partners (Jan 2025). Mishawaka, IN active lead ($142K PCP-only). Data quality issue — facilities misclassified as independent in DB.
**Profile:** `Primrose_Retirement_Communities_MUO_Profile.md`

---

### PRUITT HEALTH
**V23 Tier:** T1 (Score: 81)
**Footprint:** GA, NC, SC, FL | 27 facilities
**Research focus:** PruittHealth Premier ISNP analysis. CMS documentation review.
**Profile:** `PruittHealth_MUO_Profile.md`

---

### SABER HEALTHCARE GROUP
**V23 Tier:** T1 (Score: 91)
**Footprint:** OH, PA, VA, NC, IN, DE | 120 facilities
**Research focus:** Omega Healthcare Investors 49% JV ownership structure. RS discrepancy identified — Brooke scored 5 (strong relationship), Tom scored 2 (weak). Delta itself is a signal worth investigating.
**Profile:** `Saber_Healthcare_Group_MUO_Profile.md`

---

## Wave 3: Additions (2 entities, March 5, 2026)

Built from V22.4 DB + public research. Discovered during complete universe build.

### LUTHERAN SERVICES CAROLINAS
**V23 Tier:** T1 (Score: 68)
**Footprint:** NC | 12 campuses, 8 served
**Research focus:** **Critical entity recovery.** Present in Finance workbook the entire time but missing from the BD view — never profiled, never scored. Deep-dive research during complete universe build. Faith-based nonprofit (ELCA). 65+ year history. 8 AHCA Bronze awards (2024). CEO Ted W. Goins Jr. (36 years tenure). $3M total revenue opportunity identified.
**Profile:** `Lutheran_Services_Carolinas_MUO_Profile.md`

---

### TRILOGY HEALTH SERVICES
**V23 Tier:** T1 (Score: 79)
**Footprint:** IN, OH, KY, MI, WI | 186 DB / ~144 public
**Research focus:** **#1 Growth Opportunity.** American Healthcare REIT (NYSE: AHR) owner ($258M deal Sept 2024). Kingston Healthcare acquisition (Dec 2025, added 14 campuses). Synchrony Health Services vertically integrated pharmacy/rehab/lab subsidiary. $41.8M total revenue potential — largest single opportunity in the database.
**Profile:** `Trilogy_Health_Services_MUO_Profile.md`

---

## Special Research Initiatives During V23

### Identity Consolidation
- **Sovereign Healthcare Holdings = Southern Healthcare Management** — same entity, different name layers. Split existed since V20 as two separate T2 entries. Consolidated using CMS federal data + address matching.
- **Heritage Hall = American Healthcare, LLC** — operating name vs. parent company name. CMS-sourced records used one name, GLR-sourced used another. Chain ID 265 confirmed single operator.

### Data Gap Discovery
- **Lutheran Services Carolinas** — missing from BD view despite Finance tracking. Recovered as T1.
- **ClearView Healthcare Management** — only 5 of ~31 CMS facilities in DB. Tennessee entirely absent.
- **Triple Crown Senior Living** — only 4 of 14 public communities in DB.
- **Kisco Senior Living** — nationally significant operator substantially undercounted.
- **Choice Health Management** — 18 facilities (15 SNF + 2 ALF + 1 IL) across NC/SC, only 7 in DB. See full entry below.

---

## CHOICE HEALTH MANAGEMENT

**Canonical DB name:** TBD (currently fragmented across `MFA` and `YAD` corporate_name_raw values)
**DB variants found:** MFA (5 facilities), YAD (2 facilities), "EAST CAROLINA REHAB AND WELLNESS, LLC" (1 facility, coded Independent)
**DB facility count:** 7-8 (of ~18 actual)
**Served:** Yes (all GLR-tracked facilities have active Eventus service)
**Website:** [choice-health.net](https://www.choice-health.net)
**HQ:** 2929 N Oxford St, Claremont, NC 28610 | (828) 459-2977
**Revenue:** ~$375M (Kona Equity) / ~$108M (ZoomInfo) — discrepancy likely reflects parent vs. management entity
**Founded:** 1999, family-owned

### Corporate Structure (Key Finding)

Choice Health Management Services, LLC is the **owner/operator** of 18 facilities (15 SNF, 2 ALF, 1 IL) in NC and SC. However, it does NOT appear in CMS data under its own name. Instead:

- **CMS Chain "LIFEWORKS REHAB" (ID 768, 59 facilities)** — a rehab services provider, not an owner. CMS assigns many Choice Health SNFs to this chain because LifeWorks provides therapy services. This is a **CMS chain attribution error** — LifeWorks is a vendor, not an operator.
- **CMS Chain "CHOICE HEALTH MANAGEMENT" (ID 140)** — appears in NIC MAP / phantom audit data for 3 facilities (Blumenthal, Fletcher, Brian Center/St. Andrews) but does NOT appear in the Feb 2026 CMS Provider Info file.
- **CMS Chain "YAD HEALTHCARE" (ID 640, 13 facilities)** — CMS assigns Fletcher Rehab (345522) and St Andrews Operator LLC (425129) to YAD. YAD provides administrative/consulting services.
- **Several facilities have NO chain assignment** in CMS — Greenville Health & Rehab (345181), Lenoir Health & Rehab (345138), Lillington Health & Rehab (345213), Universal Health Care/Fuquay-Varina (345561).

**Key brand names used:**
- "Universal Health Care" / "Universal Healthcare" — primary SNF brand (Concord, King, Raleigh, North Raleigh, Fuquay-Varina, Greenville, Ramseur, Lillington)
- Facility-specific names — Blumenthal, Belaire, Alamance, Guilford, Charlotte, Oxford, Lexington, Huntersville, Carolina Rehab (Cumberland, Burke), Lenoir Healthcare
- "Brian Center" — SC facility (Brian Center Nursing Care/St. Andrews, Columbia)

**Management companies used:**
- **MFA (Medical Facilities of America)** — manages majority of NC SNFs. Staff emails often @mfa.net. MFA is a VA/NC-based management company (42 locations). MFA is NOT the owner.
- **YAD Healthcare** — manages some facilities (Fletcher, Ramseur, St. Andrews SC, Windsor, Laurel Park). Staff emails at facility-specific domains. YAD is NOT the owner.

### DB-to-CMS Reconciliation (NC/SC Facilities)

**IN our DB with corporate attribution (7 facilities):**

| DB Name | DB Corporate | City | State | CMS CCN | CMS Chain | CMS Beds | GLR Universal Name |
|---|---|---|---|---|---|---|---|
| Alamance Health Care Center | MFA | Burlington | NC | 345420 | LIFEWORKS REHAB | 180 | ALAMANCE HEALTH CARE CENTER |
| Belaire | MFA | Gastonia | NC | 345457 | LIFEWORKS REHAB | 80 | BELAIRE HEALTH CARE CENTER |
| Blumenthal Nursing and Rehab | MFA | Greensboro | NC | 345006 | CHOICE HEALTH MGMT | 134 | BLUMENTHAL NURSING AND REHAB |
| Cabarrus Health & Rehab Center | MFA | Concord | NC | 345183 | LIFEWORKS REHAB | 120 | UNIVERSAL HEALTHCARE CONCORD |
| King Health and Rehab Center | MFA | King | NC | 345449 | LIFEWORKS REHAB | 96 | UNIVERSAL HEALTHCARE KING |
| Fletcher Rehab and Healthcare | YAD | Fletcher | NC | 345522 | YAD HEALTHCARE | 90 | Fletcher Rehab and Healthcare |
| Seven Oaks Rehab & Healthcare | YAD | Columbia | SC | 425129 | YAD HEALTHCARE | 108 | Brian Center/St. Andrews |

**IN GLR (served) but NOT in DB with correct corporate link (5 facilities):**

| GLR Name | City | State | CMS CCN | CMS Chain | CMS Beds | GLR Universal Name |
|---|---|---|---|---|---|---|
| Greenville Health and Rehab | Greenville | NC | 345181 | (none) | 120 | UNIVERSAL HEALTHCARE GREENVILLE |
| Guilford Health Care Center | Greensboro | NC | 345460 | LIFEWORKS REHAB | 110 | GUILFORD HEALTH CARE CENTER |
| Carolina Rehab Center of Cumberland | Fayetteville | NC | 345505 | LIFEWORKS REHAB | 136 | CAROLINA REHAB CENTER OF CUMBERLAND |
| Ramseur Rehab and Healthcare | Ramseur | NC | 345523 | YAD HEALTHCARE | 90 | UNIVERSAL HEALTHCARE RAMSEUR |
| Lenoir Healthcare | Lenoir | NC | 345138 | (none) | 120 | LENOIR HEALTHCARE |

Note: Greenville (345181) staff use @choice-health.net emails. Lenoir (345138) staff use @choice-health.net emails.

**IN GLR (served) but corporate likely miscoded (1 facility):**

| GLR Name | DB Corporate | City | State | CMS CCN | Note |
|---|---|---|---|---|---|
| Fuquay Varina Health & Rehab | (unknown) | Fuquay-Varina | NC | 345561 | GLR shows "UNIVERSAL HEALTHCARE FUQUAY VARINA"; CMS has no chain; DB may have as independent |

**IN GLR (served) but NOT in phantom audit — likely in DB under different name (1 facility):**

| GLR Name | City | State | CMS CCN | CMS Chain | CMS Beds |
|---|---|---|---|---|---|
| Lexington Health Care Center | Lexington | NC | 345419 | LIFEWORKS REHAB | 100 |

**NOT in GLR and NOT in DB — CMS-confirmed LIFEWORKS/Choice facilities missing entirely (5 facilities):**

| CMS Provider Name | City | State | CMS CCN | CMS Chain | CMS Beds |
|---|---|---|---|---|---|
| Charlotte Health & Rehabilitation Center | Charlotte | NC | 345405 | LIFEWORKS REHAB | 90 |
| Oxford Health and Rehabilitation Center | Oxford | NC | 345291 | LIFEWORKS REHAB | 160 |
| Carolina Rehab Center of Burke | Connelly Spring | NC | 345526 | LIFEWORKS REHAB | 90 |
| Huntersville Health & Rehabilitation Center | Huntersville | NC | 345570 | LIFEWORKS REHAB | 90 |
| Litchford Falls Health and Rehab Center | Raleigh | NC | 345499 | LIFEWORKS REHAB | 90 |

Also missing: Universal Health Care/North Raleigh (345529, 132 beds, LIFEWORKS REHAB, SFF status).

**East Carolina Rehab and Wellness (separate facility, same address):**
Located at 2575 W 5th St, Greenville, NC (CMS CCN 345377, 130 beds). In our DB as Independent. Directly adjacent to Greenville Health & Rehab (2578 W 5th St). CMS shows no chain. May or may not be Choice Health — needs verification.

### Revenue Analysis

The $375M revenue figure (Kona Equity) is plausible for 15 SNFs + 2 ALFs + 1 IL if average facility revenue is ~$20M. ZoomInfo reports $108M, which may reflect the management services entity vs. total facility revenue. The 17 NC/SC facilities claim aligns with 15 SNF + 2 ALF. The "18 facilities" on their website likely includes 1 IL community.

### Timeline

| Date | Event | Source |
|---|---|---|
| 1999 | Choice Health Management Services founded, family-owned, Claremont NC | [choice-health.net](https://www.choice-health.net/The-Choice-Difference/) |
| 2018 | WRAL report: Medicare fines totaling $567,976 at 6 Choice Health facilities since 2015 (Fuquay-Varina $234K, Lillington $151K top offenders) | [WRAL](https://www.wral.com/story/hefty-medicare-fines-levied-against-nursing-home-chain-accused-of-patient-abuse/17620037/) |
| 2025 | CMS: Universal Health Care/North Raleigh (345529) designated SFF (Special Focus Facility) | CMS Provider Info Feb 2026 |
| 2026 | Self-reported: 18 facilities (15 SNF, 2 ALF, 1 IL) across NC and SC | [choice-health.net](https://www.choice-health.net) |

### 7+ Threshold Gate

Total NC/SC facility count (SNF only): **15-17 confirmed SNFs** in NC + 1 in SC = **16-18 total**
This **easily clears the 7+ threshold** for MUO consideration.

### Recommendations

1. **Create canonical entity:** Establish `CHOICE HEALTH MANAGEMENT` as the corporate_name_raw for all Choice Health facilities. Currently fragmented across MFA, YAD, Independent, and missing entries.
2. **Recode existing 7 DB facilities:** Change corporate_name_raw from MFA/YAD to CHOICE HEALTH MANAGEMENT for: Alamance, Belaire, Blumenthal, Cabarrus/Concord, King, Fletcher, Seven Oaks/St. Andrews.
3. **Add missing facilities:** At minimum, add the 6 CMS-confirmed NC SNFs not in our DB: Charlotte H&R, Oxford H&R, Carolina Rehab Burke, Huntersville H&R, Litchford Falls, UHC/North Raleigh.
4. **Verify GLR-only facilities:** Confirm Greenville H&R, Guilford, Carolina Rehab Cumberland, Ramseur, Lenoir, Fuquay-Varina, Lexington are in the DB and correctly attributed.
5. **Investigate East Carolina Rehab and Wellness:** Same street as Greenville H&R — determine if Choice Health or truly independent.
6. **CMS chain attribution note:** Do NOT trust CMS chain = "LIFEWORKS REHAB" as operator identity. LifeWorks is a therapy vendor. The true operator is Choice Health Management via MFA/YAD management.
7. **Score for MUO candidacy:** With 16-18 facilities and $375M revenue, Choice Health Management warrants immediate MUO evaluation.

**Researched:** 2026-03-22, Choice Health Management gap analysis.

### Barrier/Strategic Research
- **Pavilion Healthcare** — alliance + 29% own provider group (T5 barrier)
- **Zanziper** — 100% barriered, own provider group + alliance, $12M+ regulatory history, opaque ownership

### RS Reconciliation (March 11, 2026)
Brooke (BD perspective) vs Tom (Sales Success perspective) — 50 entities scored side-by-side. 11 big divergences identified:
- Otterbein (delta -4), Arbors of Ohio (-3), Pavilion (-3), Saber (-3)
- Divergences treated as signals, not errors — BD sees growth potential, SS sees operational depth

### V20 → V23 Movers Analysis
10 upgrades, 15 downgrades tracked across scoring versions. 3 root causes identified: RS methodology change (dual-scorer), IR recalculation (service flag audit), and ER campus count corrections.

---

## V25.1/V25.2 Research Findings (2026-03-22)

### WHITE OAK MANAGEMENT → NHC (National Healthcare Corporation)
**Event:** Full acquisition
**Date:** August 1, 2024
**Value:** $220 million
**Broker:** Blueprint Healthcare Real Estate Advisors
**Scope:** All 15 White Oak facilities (6 NC, 9 SC), 1,928 SNF beds + 48 ALF + 302 ILU
**History:** Family-owned since 1964, founded by Oliver Kent Cecil in Spartanburg, SC
**Impact:** NHC gains NC as new state. NHC footprint goes from ~20 to ~35 campuses in EWH footprint.
**DB action:** V25.2 — 16 rows reattributed WHITE OAK MANAGEMENT → NATIONAL HEALTHCARE CORPORATION
**Sources:** BusinessWire (Aug 6, 2024), Bass Berry & Sims, Skilled Nursing News, NHC press (nhccare.com)

### HCMG (Health Care Management Group) → LIONSTONE CARE
**Event:** Ownership transition
**Date:** ~2025 (Greg Miller LinkedIn announcement after 31 years at HCMG)
**Scope:** All 7 HCMG facilities — 5 OH (Cincinnati metro) + 1 KY (Florence) + Alois MC
**History:** Founded 1984, locally owned Cincinnati/NKY operator
**Facilities:** Alois Alzheimer Center, Brookwood Retirement Community, Covenant Village, Florence Park, Loveland HC, Arlington Pointe, Ohio Valley Manor
**Impact:** Lionstone gains metro Cincinnati/NKY geography (was rural OH only). Lionstone also closed separate $230M acquisition of 19-property OH SNF/AL portfolio in July 2025.
**DB action:** V25.2 — 7 rows reattributed HEALTH CARE MANAGEMENT GROUP → LIONSTONE CARE
**Sources:** Greg Miller LinkedIn, Commercial Observer (Dwight Mortgage Trust), facility websites (hcmg.com)

### CHOICE HEALTH MANAGEMENT — RETRACTED (Not a Real Operator)
**Original finding (2026-03-22):** Believed to be a hidden MUO with 18 NC/SC facilities coded under MFA/YAD.
**Correction (2026-03-25):** Per-facility ProPublica CMS ownership verification proved Choice Health Management (Donald Beaver) was the **building owner**, not the operator. MFA (Medical Facilities of America) is the operator — confirmed by GLR (Parent Company = MFA) and CMS (Chain = LIFEWORKS REHAB, which is MFA's therapy brand). Beaver sold 5 facilities to RSBRM South/Norman 5571 trusts (May 2021), 1 to Milano/Bridgewater (June 2024), and retains only 2 (Cabarrus, King) — but MFA operates all of them. Per operator attribution rule: code the operator, not the building owner. All 23 CHOICE HEALTH MANAGEMENT rows reverted to MFA in V25.4.
**Lesson:** CMS legal business name distinguishes owners — "Universal Health Care [City], Inc." = Beaver, "[City] Operator LLC" = RSBRM South. But the OPERATOR is MFA regardless of who owns the building.
**Discovery date (original):** 2026-03-22
**HQ:** Claremont, NC
**Founded:** 1999, family-owned
**Revenue:** ~$375M (Kona Equity)
**Facilities:** ~18 in NC (17) + SC (1) — operates under "Universal Health Care" brand plus facility-specific names (Blumenthal, Belaire, Alamance, Cabarrus, Guilford, etc.)
**Root cause of gap:** MFA (Medical Facilities of America) and YAD Healthcare are management companies retained by Choice Health. CMS, NIC, and our DB all inherited the management company attribution instead of the owner. LIFEWORKS REHAB also manages some Choice Health facilities.
**Staff confirmation:** Multiple facilities use @choice-health.net email addresses
**MUO gate:** PASS — 16-18 campuses in footprint
**DB action:** V25.2 — 28 rows recoded (16 MFA NC → Choice, 10 YAD → Choice, 2 LIFEWORKS → Choice). 9 uncertain rows flagged for V25.3.
**Note:** MFA also has 1 VA row and LIFEWORKS has DE/MD/PA/VA rows — these are NOT Choice Health.

### OAK GROVE HEALTHCARE CENTER (Rutherfordton, NC) — Greencroft Misattribution
**Finding:** NOT Greencroft. Greencroft Communities is exclusively Indiana-based nonprofit.
**Real operator:** SNF Care Centers, LLC (CMS Chain ID 816, 6 facilities: 2 MS, 1 NC, 3 PA)
**Legal entity:** 518 Old US Highway 221 Opco LLC
**Root cause:** Name-collision error — GLR data entry confused "Oak Grove" with Greencroft's "Oak Grove Christian Retirement Village" in DeMotte, IN
**Additional finding:** Second DB row at same address coded as Consulate/Nspire legacy was also wrong (ownership changed from Consulate orbit to SNF Care Centers)
**DB action:** V25.1 — ALF duplicate deleted, SNF row updated to SNF CARE CENTERS

### SPRING ARBOR MANAGEMENT — "Missing 9" Resolution
**Finding:** No facilities are missing. All 11 Spring Arbor-operated facilities are in the DB (15 FP rows = 14 campuses after Cary AL+MC collapse).
**Root cause of perceived gap:** Brooke counted ~24 "Spring Arbor" properties during walkthrough, but 15 of those are Spring Arbor-BRANDED buildings operated by OTHER companies:
- Foundry Commercial: 8 buildings (MD, NC, VA)
- Wickshire Senior Living: 2 buildings (NC)
- HHHunt: 1 building (NC)
- Allegro Management Company: 2 buildings (NC)
**Key insight:** "Spring Arbor" is a property brand, not always the operating company. NIC Maps operator field confirms only 11 are actually operated by Spring Arbor Senior Living.

### ENTITY NAME PAIR INVESTIGATIONS (2026-03-22)
All 4 investigated pairs are **DIFFERENT entities** — no consolidation needed:

| Pair | Verdict | Reasoning |
|---|---|---|
| WINDSOR (CA, 18 rows) vs WINDSOR HOUSE, INC. (OH, 18 rows) | DIFFERENT | Entirely different states, different operators |
| CERTUS HEALTHCARE (OH, 14 rows SNFs) vs Certus Senior Living (FL, 5 rows memory care) | DIFFERENT | Different states, different care types, different branding |
| SOUTHERN HEALTHCARE MGMT (FL/GA/NC, 46 rows) vs SOUTHERN ADMINISTRATIVE SERVICES (AR, 35 rows) | DIFFERENT | Zero geographic overlap, no address matches |
| PRIORITY (IN, 10), PRIORITY LIFE CARE (multi-state, 42), PRIORITY MANAGEMENT (LA/TX, 38), PRIORITY HEALTHCARE GROUP (PA/NE, 15) | 4 DIFFERENT operators | Completely different geographies; PRIORITY LIFE CARE is the V23 scored entity |

### CORPORATE RISK ANALYSIS CROSS-REFERENCE (2026-03-26)
Source: Cary Trainor (COO) LOB termination data cross-referenced against V25 PostgreSQL DB.
Context: 42 corporate groups with 2025 termination history, $17.5M revenue at risk.

**Name mismatch confirmed:**
- "American Healthcare" in LOB data = **Heritage Hall** (T1, entity 17366, 23 campuses). Legal holding company name vs. operator brand.

**Barrier findings (T5 candidates):**
---

### GENESIS HEALTHCARE — T5 (Own Provider Group / AlignMed Partners)

**Full 8-step reconciliation completed 2026-04-07. External verification: HIGH CONFIDENCE.**

**Canonical DB name:** `GENESIS`
**CMS Chain ID:** 237 (195 SNFs nationally as of Feb 2026)
**HQ:** 101 East State Street, Kennett Square, PA 19348
**Footprint in 6 states:** 7 campuses (5 NC, 2 VA). Zero in SC, KY, OH, IN.
**DB rows:** 210 true Genesis rows across 24 states. 198 of 210 carry "Own Provider Group" barrier.
**Served:** 4 facilities (Siler City NC SNF+ALF, Westwood VA SNF+ALF)
**Tier:** T5 — Brooke confirmed 3/27 call. Added to Monday.com board 2026-04-07.

**OPG Barrier — AlignMed Partners:**
AlignMed Partners (formerly Genesis Physician Services, rebranded) is Genesis's in-house clinical subsidiary. HQ: 101 East State Street, Kennett Square PA — same building as Genesis corporate. CEO Bill Schultz. COO Flora Cauley Petillo. President Al Shaine. 340+ physicians/NPs/PAs nationally. Trademark filed under "Genesis Eldercare Physician Services LLC" (USPTO TM 98330284). AlignMed provides all clinical staffing in-house — Genesis does not contract with external providers like Eventus. This IS the OPG barrier.

**Ownership timeline:**
| Date | Event | Source |
|---|---|---|
| 2007 | JER Partners + Formation Capital (PE) acquire Genesis HealthCare | PESP, Wikipedia |
| 2011 | PE firms sell 180 facilities / ~20,000 beds to healthcare REIT for $2.4B | PESP |
| 2015 | Genesis merges with Skilled Healthcare Group Inc. | PR Newswire |
| Mar 2021 | ReGen Healthcare (Joel Landau) invests $100M for 93% equity + 2 board seats | PESP, SNN |
| 2023 | ReGen acquires 3rd board seat for additional $25M | PESP |
| Jul 2025 | Genesis files Chapter 11 bankruptcy. 175 facilities across 18 states. $2.3B debt. | SNN, Healthcare Dive, NHPR |
| Dec 2025 | Bankruptcy judge rejects initial insider sale (Genie 3 / Landau). "Too many irregularities." | Eleven Flo, McKnight's |
| Jan 21, 2026 | Judge Jernigan approves sale to **NewGen Health** (operating as "101 West State Street LLC"). CEO Shawn Zhou, California-based. $1.015B ($343M cash + $100M promissory note + $572M assumed liabilities). | SNN, Bloomberg Law, McKnight's, CRE Daily, Yahoo Finance |
| Feb 2020 | Genesis sells/transfers 19 West Coast facilities (CA/WA/NV) to NewGen Health for $79M. First business relationship between the two. | McKnight's, GlobeNewsWire, genesishcc.com press release |
| Spring 2026 | Original estimate for transition closing. | SNN (Genesis spokesperson, Jan 2026) |
| Apr 2026 | Genesis spokeswoman Nerida Brennan emails: transition now expected **"this summer or later."** Pushed back from spring. State-by-state CHOW filings required across 18 states. | McKnight's, Central Maine (Apr 2, 2026) |

**NewGen Health background:** Los Angeles-based healthcare consulting/operating firm. CEO/CFO Shawn Zhou. Already operates the 19 West Coast facilities acquired from Genesis in 2020. Limited public profile — Boston Globe described them as a "little-known firm." The shared history between NewGen and Genesis raised scrutiny during the bankruptcy process (McKnight's: "New docs reveal Genesis HealthCare, selected bidder's shared history").

**Transition status (as of 2026-04-07):** Sale is court-approved but **NOT closed**. Requires state-by-state regulatory approvals (CHOW filings). No specific NC or VA transfer news found. Maine (11 facilities) still pending per April 2 reporting. Timeline pushed to "summer or later."

**What happens when NewGen closes:** Every facility coded GENESIS in the DB may need a recode to NEWGEN or whatever operating brand they establish. The OPG barrier (AlignMed) status under new ownership is unknown — NewGen may retain, restructure, or eliminate the in-house physician model. The 2020 West Coast precedent suggests NewGen operates under its own brand, not Genesis. **Monitor: check quarterly for state CHOW filings in NC (DHSR) and VA (VDH).** Next check: July 2026.

**Operating LLCs (CMS legal business names):**
- NC: Sunbridge Regency - North Carolina LLC (4 fac: Meridian, Abbotts Creek, Mount Olive, Siler City), Sunbridge Retirement Care Associates LLC (1 fac: Pembroke)
- VA: Westwood Medical Park Operations LLC (Westwood/Bluefield), 11 Dairy Lane Operations LLC (Woodmont/Fredericksburg)

**Facilities in our 6 states (CMS + web verified):**

| Facility | City, ST | CCN | Beds | Census | Served | CMS Stars | In DB? |
|---|---|---|---|---|---|---|---|
| Siler City Center (SNF) | Siler City, NC | 345143 | 150 | 139 | **Yes** | — | Row 9436 |
| Siler City Center (ALF) | Siler City, NC | — | 103 | 82 | **Yes** | — | Row 9474 |
| Westwood Center (SNF) | Bluefield, VA | 495200 | 60 | 49.5 | **Yes** | — | Row 16265 |
| Westwood Center (ALF) | Bluefield, VA | — | 3 | 2 | **Yes** | — | Row 16277 |
| Woodmont Center | Fredericksburg, VA | 495246 | — | — | No | — | Row (exists) |
| Meridian Center | High Point, NC | 345172 | 199 | 167.6 | No | 1-star | **NOT IN DB — V25.9 INSERT** |
| Abbotts Creek Center | Lexington, NC | 345333 | 64 | 59.6 | No | 3-star | **NOT IN DB — V25.9 INSERT** |
| Mount Olive Center | Mount Olive, NC | 345126 | 150 | 117.2 | No | 1-star | **NOT IN DB — V25.9 INSERT** |
| Pembroke Center | Pembroke, NC | 345409 | 84 | 74.0 | No | 1-star, Abuse icon | **NOT IN DB — V25.9 INSERT** |

**V25.9 action:** INSERT 4 missing NC SNFs. Source_Type=CMS/SNF. Corporate_Name=GENESIS. Barrier=Own Provider Group. Do_We_Serve=No. Addresses, beds, census, coordinates from CMS Feb 2026 extract. V25.9 punchlist items #34-37.

**Ashland KY distinction — CONFIRMED SEPARATE ENTITY (2026-04-07):** Genesis HCR of Ashland One (row 5803, corp="Genesis Health of Ashland LLC") and Two (row 5804, corp="INDEPENDENT") are a LOCAL FAMILY-OWNED personal care home, NOT Genesis Healthcare Chain 237. Evidence: (1) genesishcc.com does not list any Ashland KY facility, (2) Genesis Healthcare has zero KY presence in CMS, (3) KY CHFS licenses these as personal care homes (22 beds, exp 04/30/2026), (4) LLC registered agent is Victor Matthew Mitchell (KY company dir, formed Apr 2023) — "Mitchell" surname matches NIC MAP owner "Artrip Mitchell A," suggesting family operation, (5) NIC MAP owner for Two is "Hamilton Anesteine B" — another local individual. Both are small ALFs (13 and 15 beds), both served, both coded correctly as local/independent. **V25.9 action:** Recode row 5804 from "INDEPENDENT" to "GENESIS HEALTH OF ASHLAND, LLC" to match row 5803. Sources: KY CHFS Personal Care Home Directory Feb 2026, CareListings, KY Company Directory, genesishcc.com (Ashland not listed).

**Sources:** Wikipedia, SNN (Jul 2025 bankruptcy, Jan 2026 sale, dealbook), PESP (PE ownership history), Healthcare Dive, McKnight's, Bloomberg Law, CRE Daily, Yahoo Finance, NHPR, Eleven Flo, genesishcc.com (facility pages), alignmedpartners.com, The Org (AlignMed leadership), USPTO (TM 98330284), CMS Provider Info Feb 2026 (Chain 237).
- **Alliance Health Group** (id 16888): 9 campuses NC, 0 served. 3 of 9 facilities flagged "Alliance" + "Own Provider Group."

**Entity consolidation candidates identified:**
- **Cogir**: Cogir USA (id 16895, 16 fac) + COGIR SENIOR LIVING (id 16893, 2 fac) — same parent, split entities in DB.
- **Commonwealth**: COMMONWEALTH SENIOR LIVING (id 17395, 25 fac VA) vs COMMONWEALTH CARE OF ROANOKE (id 17367, 11 fac) — relationship unclear, needs investigation.
- **Traditions**: TRADITIONS (id 16622, 13 fac) + Tradition Senior Living (id 17984, 1 fac) — likely same operator.

**Scoring board gaps — RESOLVED 2026-03-27 (Brooke call):**
- Sonida Senior Living → **T1** (34 camp V25.5, 6 states, 4 served. NYSE: SNDA, CNL merger Nov 2025)
- Harmony Senior Services → **T2** (26 camp V25.5 exact match, 6 states, 5 served. Family-owned Smith/Packett)
- Spring Arbor Management → **T2** (14 camp V25.5, 3 states, 5 served. Brand vs operator split confirmed)
- Traditions → **T3** (12 camp V25.5, 3 states, 3 served. Entity consolidation still pending)
- Mainstay Senior Living → **T3** (8 camp V25.5, 2 states, 4 served)
- Carlyle Senior Care → **T4** (7 camp V25.5, SC only, 0 served)

**NOTE:** 3/26 campus counts used V25 PG data + included naming-layer contamination. V25.5 exact-match counts corrected above. Pipeline counts from 3/26 were CRM board data, not DB Contract_Status field (which uses Green/Yellow/Red).

**T4 classification review — RESOLVED 2026-04-07:**

### BHI SENIOR LIVING — T4 CONFIRMED (8 campuses in footprint, passes gate but nonprofit CCRC model)

**Full 8-step reconciliation completed 2026-04-07. External verification: HIGH CONFIDENCE (all 8 claims verified with 2+ independent sources).**

**Canonical DB name:** `BHI SENIOR LIVING`
**Legal entity:** BHI Senior Living, Inc. (EIN 35-0931432), 501(c)(3) nonprofit
**Former names:** Crawford Baptist Industrial School (1905) → Baptist Homes of Indiana, Inc. (1960s) → BHI Senior Living, Inc. (Sept 21, 2011)
**HQ:** 8330 Allison Pointe Trail Suite 300, Indianapolis, IN 46250
**CEO:** John S. Dattilo. **CFO:** Roger E. Weideman II.
**Model:** Life Plan Communities (CCRCs) — IL + AL + MC + SNF on single campuses. Faith-based (American Baptist).
**Revenue (FY2024):** $87.2M. **Assets:** $394.7M.

**Portfolio (12 communities):**
- 10 Life Plan Communities: Hoosier Village (Indianapolis IN), Barrington of Carmel (IN), Towne House (Fort Wayne IN), Wesley Manor (Frankfort IN), Four Seasons (Columbus IN), Westminster Village North (Indianapolis IN), Maple Knoll Village (Cincinnati OH), Knolls of Oxford (OH), Clark at Franklin (Grand Rapids MI), Clark at Keller Lake (Grand Rapids MI)
- 2 Active Adult (no licensed beds): Prairie Landing (Fort Wayne IN), Athens Crossing (Columbus IN)

**Affiliation timeline:**
- 2019: Prairie Landing Community Inc (BHI affiliate) acquires Barrington of Carmel from SQLC bankruptcy for $61M (Sources: McKnight's, GlobeSt, IBJ)
- Jan 2022: Clark Retirement Community affiliates (Sources: HJ Sims, Senior Living News, Crain's Grand Rapids)
- Oct 2021 / effective July 2022: Maple Knoll Communities affiliates (Sources: HJ Sims, DealFlow, mapleknoll.org "A BHI Affiliate", IRS 990 shared officers)
- Feb 2024: Westminster Village North affiliates — BHI's "fourth time in seven years" (Sources: BHI press release, Senior Living News)

**Subsidiary legal entities in DB:**
- PRAIRIE LANDING COMMUNITY INC (Barrington ALF row 19559) — BHI entity, EIN 26-2053830, same officers as BHI
- Clark Retirement (Clark at Keller Lake row 21510) — BHI affiliate
- MAPLE KNOLL COMMUNITIES (Knolls of Oxford rows 11951/12608/12609, Maple Knoll Village row 12052) — BHI affiliate
- Blank/INDEPENDENT (Maple Knoll Village SNF row 12051, row 12052) — should be coded BHI or Maple Knoll

**Clinical services:** BHI co-owns Care Plus Home Health Care (CPHC) with Healthcare Therapy Services Inc (HTS) since 2022. HTS provides PT/OT/speech therapy across BHI campuses. NOT a full OPG — no captive physician group, no barrier to external clinical providers. (Sources: careplus-hhc.com, bhiseniorliving.org, htstherapy.com)

**Footprint in 6 states:** 8 campuses (6 IN + 2 OH). MI facilities (2) outside footprint. Passes 7+ gate.
**Tier: T4 (Brooke 3/27).** Passes gate but CCRC/nonprofit model with primarily IL census — clinical opportunity concentrated in SNF wings which are small (8-148 beds per campus). Brooke's T4 assignment reflects the business reality even though campus count exceeds threshold.

**DB issues (V25.9 punchlist):**
- Row 5200: Trustwell Living at Settler's Place (LaPorte IN) MISATTRIBUTED to BHI. Trustwell Living LLC is a separate for-profit company (CEO Lori Colwell Jones, Chairman Lawrence Cohen). Founded 2021, ~45 communities. Confirmed by trustwellliving.com, A Place for Mom, Senior Housing News. Zero connection to BHI.
- Entity fragmentation: BHI facilities split across 4+ Corporate_Name values (BHI SENIOR LIVING, PRAIRIE LANDING COMMUNITY INC, Clark Retirement, MAPLE KNOLL COMMUNITIES, INDEPENDENT, blank). Consolidation needed.

**Sources:** bhiseniorliving.org, mapleknoll.org, CauseIQ EIN 35-0931432, ProPublica Nonprofit Explorer (EIN 26-2053830 Prairie Landing, EIN 31-0544277 Maple Knoll), HJ Sims (Maple Knoll May 2021, Clark Jan 2022), McKnight's Senior Living, Senior Living News, Crain's Grand Rapids Business, GlobeSt, Indianapolis Business Journal, EIN Presswire (Smarter Service Apr 2025)

---

### KISSITO HEALTHCARE — T4 CONFIRMED (6 campuses VA, fails gate as standalone)

**Full 8-step reconciliation completed 2026-04-07. External verification: HIGH CONFIDENCE (10 claims verified, 1 name correction).**

**Canonical DB name:** `Kissito Healthcare`
**Founded:** 1989 by Tom Clarke (President/CEO until ~2016)
**HQ:** Virginia (western region)
**Structure:** For-profit. Mixed ownership types per CMS — 3 nonprofit corporation, 3 for-profit LLC.
**OpCo LLCs:** 5x "RBM OPCO OF [city] LLC" + 1x "AFS OF HOT SPRINGS, INC."
**CMS Chain ID:** 302

**CHOW — January 1, 2026:** Acquired by **Larry H. Miller Senior Health** (LHMSH), Salt Lake City, UT. Simultaneously, **CareTrust REIT** (NYSE: CTRE) purchased the real estate for ~$142M and leases back to LHM under a long-term triple-net lease (9% stabilized yield).
- Prior owner: Robert McClintic II (CEO since 2016, purchased buildings ~2022)
- LHM retained nearly all senior leadership, all operational leadership, all regional clinical leadership, all direct care employees
- Facilities continue under the **Kissito brand name**
- **Mary Ferrell** — VP of Operations, retained (30+ years post-acute, licensed NHA, fka VP Ops at Stonerise Healthcare and Genesis Healthcare)
- Sources: SNN Dealbook Jan 2026, LHM press release, kissito.org blog, CareTrust investor relations, Virginia Business, SignalBase

**Operator attribution analysis (2026-04-07):**
LHM Senior Health is the **parent/holding company**, NOT the operator. LHM is an auto dealership/real estate/sports conglomerate (Larry H. Miller, 1944-2009; Utah Jazz owner 1985-2020) that entered healthcare in Jan 2021 by acquiring Advanced Health Care Corporation. Created "LHMSH" as a business platform in March 2023. LHM provides capital and strategic direction. Kissito's ops team (Mary Ferrell et al.) makes the facility-level clinical and business decisions. **This is the Portopiccolo pattern — PE/holding parent, independent operator subsidiaries.**

**LHM Senior Health portfolio (for reference, NOT for scoring as one entity):**
- Kissito Healthcare: 6 SNFs + ALFs in VA (acquired Jan 2026)
- Advanced Health Care (AHC): ~23 SNF/transitional rehab facilities in 13 states including 2 in OH (Cincinnati, Landerhaven/Mayfield Heights). Founded 2001, Idaho. Andy Frasure is President of AHC AND COO of LHMSH.
- Advanced Home Health and Hospice: 16 teams
- Aspen Ridge Senior Living: 1 ALF, Lehi UT
- LHM leadership: Joe Walker (President), Andy Frasure (COO), Jess Dalton (CSO, joined Nov 2024, fka VP Ensign Services)

**Why Kissito and AHC are separate operators (not one LHM entity):**
Both pass the operator test — own websites, own leadership, own CMS chains, own OpCo LLCs, own state licensing. If you pulled either out of LHM, it would still be an operating company. LHM does not make facility-level clinical decisions. Coding them as one entity would misrepresent who actually runs the facilities. Per operator attribution rule: code the entity that makes clinical and business decisions at the facility level.

**Kissito footprint in 6 states:** 6 campuses, all VA. Does NOT pass 7+ gate.
**AHC footprint in 6 states:** 2 campuses, OH. Does NOT pass 7+ gate.
**Tier: T4 for both (Brooke's 3/27 assignment confirmed).**

**Warsaw Nursing & Rehab (NC):** Formerly Kissito, divested ~July 2025 (before LHM deal). Now under **YAD Healthcare** (CMS Chain 640, owner Tzvi Alter 80% via Warsaw Holdco LLC). Confirmed by warsawrehab.com (YAD branding), ProPublica ownership data, kissito.org locations (Warsaw not listed).

**"Baroco" from Cary's note:** Best lead is **Dr. Patrick E. Baroco Jr., MD** — Roanoke VA internist/geriatrician with Premier Geriatric Solutions. Serves as SNF medical director at Kendal at Lexington (since Aug 2023). Premier Geriatric Solutions covers the exact Kissito territory (Roanoke, Lynchburg, New River Valley VA + northwestern NC). Likely an attending physician or medical director at one or more Kissito facilities. His wife Dr. Allison Baroco is Health Director for the Central Shenandoah Health District (overlapping geography). (Sources: Doximity, Kendal at Lexington, US News Doctors, premiergeriatric.com, VDH)

**Name correction:** Cary's note said "Steve" — the LHM COO is **Andy Frasure** (Andrew Frasure), not Steve. Confirmed by SNN interview March 2026, LinkedIn, The Org.

**6 Kissito campuses (all VA, all Do_We_Serve=Yes, 0 barriers):**

| Campus | City | SNF Beds (CMS) | ALF Beds (DB) | CMS CCN | CMS Stars |
|---|---|---|---|---|---|
| Bland County NRC | Bastian | 57 | 56 | 495191 | — |
| Brian Center of Fincastle | Fincastle | 60 | 51 | 495218 | — |
| Brian Center of Alleghany | Low Moor | 89 | 84 | 495221 | — |
| Maple Grove NRC | Lebanon | 60 | 58 | 495365 | 3-star |
| Mulberry Creek NRC | Martinsville | 300 | 36 | 495426 | — |
| The Springs NRC | Hot Springs | 60 | 58 | 495220 | — |

**DB issues:** None for Kissito proper. All 12 rows (6 SNF + 6 ALF campus pairs) are correctly coded. CMS CHOW flag hasn't updated yet (still shows "N" as of Feb 2026 extract — acquisition was Jan 1, 2026).

**Sources:** kissito.org, lhm.com press releases, SNN Dealbook Jan 2026, SNN March 2026 (Frasure interview), CareTrust REIT investor relations, Virginia Business, Salt Lake Tribune (Jazz sale/AHC acquisition Jan 2021), McKnight's Senior Living (LHMSH platform Mar 2023), ahcfacilities.com, Ohio HCA, ProPublica (Warsaw ownership), Doximity/US News (Dr. Baroco), premiergeriatric.com, warsawrehab.com, SignalBase M&A

---

## MORNING POINTE SENIOR LIVING

**Canonical DB name:** `MORNING POINTE SENIOR LIVING`
**Parent entity:** Independent Healthcare Properties (IHP), LLC
**Founded:** 1997 by Greg A. Vital and Franklin Farrow, Chattanooga TN
**Footprint:** 27 communities per morningpointe.com (checked 2026-04-06) across 5 states: KY (8 including Owensboro), TN (16), GA (2), IN (1), AL (1). Press release says "42 assisted living and Alzheimer's memory care communities" — discrepancy may reflect Lantern MC units counted separately.
**Business model:** ALF + Lantern memory care. PropCo entities follow "[City] Medical Investors LLC" naming convention (e.g., Owensboro Medical Invtrs LLC, Lexington East Medical Investors LLC, Brentwood Medical Investors LLC).
**Website:** morningpointe.com
**Leadership:** Greg A. Vital (Co-Founder), Franklin Farrow (Co-Founder)

### Timeline
| Date | Event | Source |
|---|---|---|
| 1997 | Founded by Greg A. Vital and Franklin Farrow in Chattanooga, TN | morningpointe.com/about-morning-pointe/ |
| 2024 (Sep) | Acquired Heritage Place (ALF, 66 beds) in Owensboro KY from Encore Communities. $2.5M renovation planned. 39th community overall. | Owensboro Times (owensborotimes.com, Sep 2024) |
| 2025 (Aug 14) | Grand Opening of Morning Pointe of Owensboro (formerly Heritage Place). Deficiency-free KY licensure survey. Executive Director: Karleigh Roby. 40 jobs in Daviess County. $15M+ annual local economic contribution. | morningpointe.com/press/morning-pointe-senior-living-expands-to-western-kentucky/ |

### Ownership Structure — Morning Pointe of Owensboro (3362 Buckland Sq, Owensboro KY)

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | Unknown — ALF, no CMS/ProPublica | TBD (likely IHP LLC entity) |
| **PropCo** | NIC MAP (Owner col 18) | Owensboro Medical Invtrs LLC (IHP/Morning Pointe PropCo pattern) |
| **Management Company** | NIC MAP (Operator col 41) — **STALE** | Genesis HealthCare (NIC MAP data error — never operated this facility) |
| **Management Sub-brand** | — | N/A |
| **Operator** | FU + GLR + morningpointe.com + press release (HIGH confidence) | **MORNING POINTE SENIOR LIVING** |

**Confidence: HIGH.** 3+ sources agree (Forward Universe served row, GLR Parent Company, morningpointe.com community listing, Morning Pointe press release with specific details — date, ED name, investment, licensure survey). Genesis on NIC MAP is confirmed stale (NIC MAP export Nov 2025; Heritage Place was under Encore Communities before Sep 2024 acquisition; Genesis never operated). ALF confidence ceiling exception: operator website explicitly lists the facility AND press release provides licensure confirmation.

### DB Notes
- **NIC MAP misattribution:** NIC-A row (Row 5934) coded operator as GENESIS HEALTHCARE. Genesis has zero relationship to this facility. NIC MAP export Nov 2025 still shows stale Heritage Place / Genesis assignment 14 months after the Morning Pointe acquisition. PropCo "Owensboro Medical Invtrs LLC" on NIC row correctly maps to IHP/Morning Pointe PropCo pattern.
- **Heritage Place → Morning Pointe of Owensboro** rebrand confirmed. Heritage Place was the facility name under Encore Communities. Morning Pointe acquired Sep 2024 and rebranded following $2.5M renovation.
- **Encore Communities** was prior operator of Heritage Place (Pacific Northwest-based, ~43 communities in IL, WI, MN, OH, MI). Unrelated to Genesis.
- **KY CHFS gap:** Morning Pointe of Owensboro does NOT appear in the KY Personal Care Home Directory (Feb 2026 PDF). Possible explanations: license issued after directory compilation, listed under different entity name, or directory incomplete. Press release confirms deficiency-free licensure survey. Flag for follow-up.
- **Bed count source question:** DB has 14 beds (appears to be patient count, not bed count). Prior dedup decision (Pair 11) set beds to 66 (from NIC-A Heritage Place row). GLR Licensed Bed = 0 (data gap). 66 is the pre-renovation Heritage Place capacity and likely still correct, but needs independent KY CHFS confirmation since the source row (5934) is being deleted.

### Sources (current-standard documentation, 2026-04-06)
- morningpointe.com/communities/ (checked 2026-04-06): Owensboro KY listed as active community
- morningpointe.com/press/morning-pointe-senior-living-expands-to-western-kentucky/ (checked 2026-04-06): Grand opening Aug 14 2025, ED Karleigh Roby, deficiency-free survey, 40 jobs, $15M+ annual local impact
- GLR Facility Dump 2026-03-13: Parent Company = MORNING POINTE SENIOR LIVING, 20 pts (15 PC, 11 Psych), census 23
- NIC MAP (Nov 2025 export): Property = Heritage Place Assisted Living Center, Owner = Owensboro Medical Invtrs LLC, Operator = Genesis HealthCare (STALE)
- KY CHFS Personal Care Home Directory (Feb 2026 PDF): NOT LISTED — gap
- Forward Universe V25.7: 2 rows at this address (served + unserved duplicate)
- Owensboro Times (Sep 2024): Heritage Place acquisition announcement

**Originally documented:** 2026-03-27 (dedup session, Pair 11)
**Updated to current procedure standard:** 2026-04-06 (ALF dedup cluster review, Cluster 6)

---

## ARCADIA COMMUNITIES

**Canonical DB name:** `ARCADIA COMMUNITIES`
**Headquarters:** 4360 Brownsboro Rd Ste 305, Louisville, KY 40207
**Phone:** (502) 357-7000
**Website:** arcadia-communities.com (corporate), individual facility sites: arcadiabowlinggreen.com, arcadiaclarksville.com, arcadiapace.com, stilleyhouse.com
**Type:** Private, for-profit senior living developer and operator
**Leadership:** Brian Durbin, President. Also serves as Chairman of the Board of the Kentucky Senior Living Association.
**Founded:** Louisville KY. Nearly 100 years of combined leadership experience per corporate website.
**Services:** Independent Living, Assisted Living, Memory Care

#### Recognition
- Great Place to Work Certified (2020, 2022, 2023 — 3 consecutive years)
- Business First Louisville Fast 50 — ranked 35th, 5th time on the list
- U.S. News & World Report: 7 Arcadia Communities named among Best Senior Living 2023-2024

#### Portfolio (per arcadia-communities.com + facility websites + news, checked 2026-04-06)
Communities in KY, TN, FL, MI:

| Community | City | State | DB Row | DB Corp Name | Notes |
|---|---|---|---|---|---|
| Arcadia Senior Living Bowling Green | Bowling Green | KY | 5633 (served) | INDEPENDENT → ARCADIA COMMUNITIES | **Cluster 7 recode.** arcadiabowlinggreen.com. 618 Lovers Ln. 87 beds. 23 pts (21 Psych). |
| Arcadia Senior Living of Louisville | Louisville | KY | 5635 | ARCADIA COMMUNITIES | Already correctly coded. 901 Blankenbaker Pkwy. 83 beds. Acquired from Wickshire Senior Living (WHAS11 fire incident coverage). |
| Arcadia of Benton (Stilley House) | Benton | KY | 17115 | ARCADIA OF BENTON PROP LLC | **PropCo LLC — needs recode to ARCADIA COMMUNITIES.** stilleyhouse.com. Per-facility verification needed. |
| Arcadia Senior Living Clarksville | Clarksville | TN | 17117 | ARCADIA OF CLARKSVILLE PROP LLC | **PropCo LLC — needs recode to ARCADIA COMMUNITIES.** arcadiaclarksville.com. $10M new build (news). Per-facility verification needed. Outside 6-state footprint. |
| Arcadia of Pace | Pace | FL | — | — | arcadiapace.com. "Louisville Based Arcadia Communities Acquires First Local Senior Living Campus" (press release). Not in DB (outside footprint). |
| Arcadia (Pensacola area) | near Pensacola | FL | 2253 | BENJAMIN LANDA | "Arcadia Communities Acquires Assisted Living Community Near Pensacola FL" (press release). DB row 2253 = ARCADIA HEALTH AND REHABILITATION CENTER, SNF, 170 beds, coded BENJAMIN LANDA. **Possible misattribution — investigate.** Outside footprint. |
| Michigan community(ies) | TBD | MI | — | — | Corporate website mentions MI. No specific facility identified. |

**Note on DB entity "ARCADIA CARE":** 11 IL SNF rows coded ARCADIA CARE (rows 3899-3910). This is a **completely different company** — an IL-based SNF operator unrelated to Arcadia Communities (KY-based ALF operator). Name similarity does NOT determine attribution (procedure rule #8). Do not consolidate.

**Note on "Arcadia Assisted Living" (MD):** 5 rows in MD coded "Arcadia Assisted Living" (rows 20519-20525). Small residential ALFs (15-16 beds each). Different company from Arcadia Communities. Do not consolidate.

#### Ownership Structure — Arcadia Senior Living Bowling Green (618 Lovers Ln, Bowling Green KY)

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | Unknown — ALF, no CMS/ProPublica | TBD |
| **PropCo** | NIC MAP (Owner col 18) | Wolfe Karen S Trust (individual/family trust) |
| **Management Company** | NIC MAP (Operator col 41) | "Arcadia" (self-referencing, reliability pattern #2) |
| **Management Sub-brand** | — | N/A |
| **Operator** | Operator website + corporate website + news (MEDIUM confidence) | **ARCADIA COMMUNITIES** |

**Confidence: MEDIUM.** 3 sources agree on Arcadia Communities as operator: arcadiabowlinggreen.com (Brian Durbin, President Arcadia Communities), arcadia-communities.com (corporate site, Louisville HQ), news coverage (Chairman KY Senior Living Assoc, Fast 50, Great Place to Work, Wickshire acquisition, WHAS11 fire coverage). ALF confidence ceiling applies — no KY CHFS directory listing, no NPI registration found. DB row 5635 (Louisville) already coded ARCADIA COMMUNITIES provides internal consistency.

#### Full 11-Step Source Sequence (2026-04-06)

| Step | Source | Finding |
|---|---|---|
| 1 | Forward Universe | INDEPENDENT (served row 5633), NULL (unserved rows 17116, 5634). 1 other DB row coded ARCADIA COMMUNITIES (Louisville, row 5635). 2 rows coded PropCo LLCs (Benton 17115, Clarksville 17117). |
| 2 | GLR Export | Parent Company = INDEPENDENT. Facility name = "Arcadia Senior Living." 87 beds, 87 census, 23 pts (21 Psych). Address = "618 Lovers Lane" (vs DB "618 Lovers Ln" — normalization gap). |
| 3 | MUO Corporate History | No prior entry. |
| 4 | Operator Research Log | Not previously researched. |
| 5 | CMS Provider Info | N/A — ALF, no CCN. |
| 6 | ProPublica | N/A — ALF. |
| 7 | NIC MAP (Nov 2025) | Property = "Arcadia Senior Living", Owner = "Wolfe Karen S Trust" (PropCo — individual/family trust), Operator = "Arcadia" (self-referencing, reliability pattern #2 — corporate parent hidden). |
| 8 | State Registry (KY CHFS) | NOT LISTED in KY Personal Care Home Directory (Feb 2026 PDF). Warren County only shows Fern Terrace of Bowling Green. Gap — same pattern as Morning Pointe and Shady Lawn. |
| 9 | NPI Registry | No results for "Arcadia Senior Living", "Arcadia Communities", or "Arcadia" in KY. Expected for ALF — not CMS-participating provider. |
| 10 | Operator website | arcadiabowlinggreen.com: Brian Durbin identified as "President Arcadia Communities." Copyright "Arcadia Senior Living Bowling Green © 2026." Powered by ConversionFormula (web vendor). Contact: poakes@arcadiabowlinggreen.com. "Certified from the Commonwealth of Kentucky." arcadia-communities.com: HQ 4360 Brownsboro Rd Ste 305, Louisville KY 40207. (502) 357-7000. info@arcadia-communities.com. Communities in KY, TN, FL, MI. Nearly 100 years combined leadership experience. |
| 11 | News / journalism | Brian Durbin = Chairman of Board, Kentucky Senior Living Association. Business First Louisville Fast 50 (35th, 5th time). Great Place to Work certified 2020/2022/2023. WHAS11: fire at Louisville facility, Durbin quoted as spokesperson. arcadia-communities.com/news: "Louisville Based Arcadia Communities Acquires First Local Senior Living Campus" (Pace FL), "Arcadia Communities Acquires Assisted Living Community Near Pensacola FL." U.S. News: 7 Arcadia Communities among Best Senior Living 2023-2024. |

#### DB Impact
- Row 5633 (Bowling Green KY, served): Recode INDEPENDENT → ARCADIA COMMUNITIES. Beds 26→87. **Cluster 7.**
- Row 5635 (Louisville KY, unserved): Already coded ARCADIA COMMUNITIES. No change.
- Row 17115 (Benton KY, unserved): Coded ARCADIA OF BENTON PROP LLC — PropCo LLC, needs recode to ARCADIA COMMUNITIES. Per-facility verification required.
- Row 17117 (Clarksville TN, unserved): Coded ARCADIA OF CLARKSVILLE PROP LLC — PropCo LLC, needs recode to ARCADIA COMMUNITIES. Per-facility verification required. Outside 6-state footprint.
- Rows 17116, 5634 (Bowling Green KY duplicates): DELETE.

#### GLR Discrepancy
GLR Parent Company = INDEPENDENT for Bowling Green. Should be ARCADIA COMMUNITIES. Correction logged to glr_change_log.csv.

#### Sources
- arcadiabowlinggreen.com (checked 2026-04-06): Brian Durbin President Arcadia Communities, facility page, contact info
- arcadia-communities.com (checked 2026-04-06): corporate site, Louisville HQ, portfolio, mission, leadership
- arcadia-communities.com/news: Pace FL acquisition, Pensacola FL acquisition press releases
- arcadiaclarksville.com: $10M new build, Clarksville TN facility page
- stilleyhouse.com: Benton KY facility page (Arcadia of Benton / Stilley House)
- NIC MAP (Nov 2025 export): Owner = Wolfe Karen S Trust, Operator = Arcadia (self-referencing)
- KY CHFS Personal Care Home Directory (Feb 2026 PDF): NOT LISTED
- NPI Registry API: No results
- GLR Facility Dump 2026-03-13: Parent Company = INDEPENDENT, 87 beds, 87 census, 23 pts
- WHAS11 (Louisville news): fire incident at Arcadia Senior Living Louisville
- Business First Louisville: Fast 50 listing
- Forward Universe V25.7: 5 rows with "Arcadia" in facility name across KY/TN footprint

**Discovered during:** ALF dedup cluster review, Cluster 7, punchlist item #1, 2026-04-06

---

## TOPAZ HEALTHCARE (Topaz Financial Services LLC / fka Sapphire Care Group)

> **CORRECTION (2026-04-07): Original finding (2026-04-06) incorrectly characterized Topaz as a "phantom fiscal agent, not an operator." This was WRONG. Topaz IS a real Kentucky nursing home operator. The correction below documents the full evidence chain. The error occurred because initial research found only the fiscal services arm without checking facility websites, the KY state directory, or field intelligence. Brooke's field knowledge that Topaz is "buying stuff left and right in Kentucky" was the signal that triggered re-investigation. Lesson: always complete the full 11-step source sequence and incorporate field intelligence before concluding.**

### What Topaz Is

**Topaz Healthcare / Topaz Financial Services LLC** is a real Kentucky nursing home operator — the management/fiscal arm of the Landa/Platschek/Chafetz ownership network. They acquired 21 Preferred Care Kentucky SNFs out of bankruptcy in July 2018 (originally as **Sapphire Care Group**), and are actively expanding (bid $11.15M for Metcalfe Healthcare Center, Sep 2025).

**Canonical DB name:** `TOPAZ HEALTHCARE`
**Legal entity:** Topaz Financial Services LLC (KY registered corporation, OpenCorporates #1019317)
**HQ:** 6085 Strickland Avenue, Mill Basin, Brooklyn, NY 11234
**Key personnel:** Hal Brecher (provider contact for all KY facilities, email hbrecher@topazfs.com), Richard Platschek (member per OpenCorporates)
**Website:** topazfiscalservices.com (presents as "Nursing Home Financial Services Company" — but KY state directory confirms them as the registered Corporation for 21+ facilities)
**LinkedIn:** linkedin.com/company/topaz-fiscal-services-llc (~30 employees)
**Formerly known as:** Sapphire Care Group (Buffalo NY area, 2018 acquisition entity)

**Disambiguation — NOT the same as:**
- Topaz Healthcare (topazhealthcare.com) — California home health company, Cupertino/Saratoga CA. PT/OT/SLP services. Completely unrelated.
- Topaz Healthcare Services (topazhealthcareservices.com) — Maryland home care provider. Completely unrelated.

### Ownership Network

Topaz is the management/operating arm of a private ownership network based in Brooklyn NY:

| Entity | Role | Key People |
|---|---|---|
| **Topaz Financial Services LLC** | KY state-registered Corporation, fiscal management, operator | Hal Brecher, Richard Platschek |
| **Benjamin Landa** | CMS chain affiliation (55 affiliated facilities in FL/KY/NJ/NY) | Benjamin Landa (44%), Goldie Platschek (25%), Alexander Platschek (15%), David Rubenstein (7%) |
| **Emerald Healthcare LLC** | CMS chain affiliation (14 facilities KY/NE/OK). Also described as "third-party fiscal consulting company" | Yisroel Chafetz |
| **Noble Healthcare Management LLC** | Managing entity on ProPublica filings (Louisville KY, est. 2014) | — |
| **Limestone Fiscal Services LLC** | Managing entity (appeared at Pikeville since Jul 2024) | — |
| **Prestige Administrative Services LLC** | Managing entity on ProPublica filings | — |
| **Sapphire Care Group** | Former acquisition entity (2018 Preferred Care bankruptcy purchase) | — |

The CMS chain names (Emerald Healthcare, Benjamin Landa) are ownership-layer designations within this network, not separate operators. The GLR correctly codes all these facilities under one Parent Company: TOPAZ HEALTHCARE.

### Acquisition History

| Date | Event | Source |
|---|---|---|
| Jul 2018 | Sapphire Care Group acquires 21 Preferred Care Inc. KY facilities out of Chapter 11 bankruptcy. $0 purchase price. Must employ 70% of staff. Shielded from 163 pending lawsuits ($28M largest judgment). | Skilled Nursing News (Jul 2018) |
| Oct 2018 | Benjamin Landa (44%), Platschek family (40%), Rubenstein (7%) registered as direct owners on ProPublica filings for Henderson, Elizabethtown, and other KY facilities. | ProPublica h-185402, h-185266 |
| 2018-present | Topaz Financial Services LLC registered as Corporation in KY state directory for all facilities. Hal Brecher listed as provider contact. | KY DMS LTC Facility Listing |
| Sep 2025 | Topaz Fiscal Services bids $11.15M for Metcalfe Healthcare Center (Edmonton KY). Awarded to "Topaz Health" (corrected to "Topaz Corporation" by County Attorney). Approved unanimously by magistrates. | Jobe for Kentucky (jpinews.com, Sep 16 2025) |

### KY State Directory Facilities (21+ as of Feb 2026)

All registered with Corporation = "Topaz Financial Services, LLC", contact = Hal Brecher, 6085 Strickland Ave, Brooklyn NY 11234, hbrecher@topazfs.com:

| # | Facility | City | County |
|---|---|---|---|
| 1 | Bowling Green Nursing and Rehabilitation | Bowling Green | Warren |
| 2 | Brandenburg Nursing and Rehabilitation | Brandenburg | Meade |
| 3 | Campbellsville Nursing and Rehabilitation | Campbellsville | Taylor |
| 4 | Christian Heights Nursing and Rehabilitation | Pembroke | Christian |
| 5 | Cumberland Nursing and Rehabilitation | Somerset | Pulaski |
| 6 | Elizabethtown Nursing and Rehabilitation | Elizabethtown | Hardin |
| 7 | Fordsville Nursing and Rehabilitation | Fordsville | Ohio |
| 8 | Franklin-Simpson Nursing and Rehabilitation | Franklin | Simpson |
| 9 | Hardinsburg Nursing and Rehabilitation | Hardinsburg | Breckinridge |
| 10 | Henderson Nursing and Rehabilitation | Henderson | Henderson |
| 11 | Irvine Nursing and Rehabilitation | Irvine | Estill |
| 12 | Kenwood Health and Rehabilitation | Richmond | Madison |
| 13 | Madison Health and Rehabilitation | Richmond | Madison |
| 14 | Morganfield Nursing and Rehabilitation | Morganfield | Union |
| 15 | River Haven Nursing and Rehabilitation | Paducah | McCracken |
| 16 | Salyersville Nursing and Rehabilitation | Salyersville | Magoffin |
| 17 | Shady Lawn Nursing and Rehabilitation | Cadiz | Trigg |
| 18 | Springfield Nursing and Rehabilitation | Springfield | Washington |
| 19 | Stanton Nursing and Rehabilitation | Stanton | Powell |
| 20 | Twin Rivers Nursing and Rehabilitation | Owensboro | Daviess |
| 21 | Woodcrest Nursing and Rehabilitation | Elsmere | Kenton |

**Note:** GLR carries 15 of these 21 under TOPAZ HEALTHCARE as Parent Company. The remaining 6 (Cumberland, Fordsville, Kenwood, Madison, Morganfield, Shady Lawn Cadiz) may not be in the GLR or may be coded differently. Also: Pikeville Nursing and Rehab is in the GLR under Topaz but NOT in the KY state directory under Topaz — may have a different state registration structure or may have changed since the directory was compiled.

**Also note:** "Shady Lawn Nursing and Rehabilitation" in Cadiz KY (Trigg County) is a DIFFERENT facility from "Shady Lawn" in Cynthiana KY (Harrison County) that we evaluated in Cluster 4. The Cynthiana Shady Lawn is a PCH (personal care home / ALF) operated by Shady Lawn I LLC / Kim Perez. The Cadiz Shady Lawn is an NF (nursing facility) under Topaz.

### GLR Presence (15 served facilities, ~720+ patients)

The GLR carries TOPAZ HEALTHCARE as Parent Company on 15 served KY facilities. This is **correct** — Topaz is the operator. The GLR attribution should be maintained.

### DB Impact

The Forward Universe likely has some of these 21 facilities coded under different corporate names (Emerald Healthcare, Benjamin Landa, or individual facility LLCs) based on CMS chain data. **V25.9 action:** Verify which DB rows correspond to the 21 Topaz KY facilities and recode to TOPAZ HEALTHCARE where appropriate. Per-facility verification required — the CMS chains vary (Emerald, Benjamin Landa) but the operator is Topaz across all.

**Metcalfe Healthcare Center (Cluster 8):** The original dedup analysis coded this facility as WELLS HEALTH SYSTEMS based on the ProPublica managing entity. Wells Health Services INC has been the managing entity since Jan 2008 — but Topaz bid to acquire Metcalfe in Sep 2025. If the acquisition closed, Metcalfe transitions to Topaz. Current ProPublica still shows Wells. **Status: transitional — verify whether Topaz acquisition has closed before recoding.**

### Scoring Board Implications

Topaz Healthcare operates 21+ KY SNFs with 720+ served patients across 15 GLR-tracked facilities. This easily passes the 7+ campus gate. **Topaz should be evaluated for the corporate scoring board when the freeze lifts (June 6, 2026).**

### How the Original Error Happened and What We Learned

The original investigation (2026-04-06) found Topaz Fiscal Services LLC on LinkedIn and topazfiscalservices.com, both describing it as a "Nursing Home Financial Services Company." Three ProPublica checks showed different CMS chains (Emerald, Benjamin Landa, Wells Health Services). The conclusion was that Topaz was a fiscal agent, not an operator.

**What was missed:**
1. The KY DMS Long-Term Care Facility Listing — which shows Topaz Financial Services LLC as the registered **Corporation** for 21 facilities. This is a state regulatory filing, not just an accounting vendor entry.
2. Facility operator websites — none were checked for Topaz branding (most showed no corporate affiliation, but the website design firm IlluminAge is shared across all Topaz facilities — a centralized management signal)
3. Field intelligence — Brooke identified Topaz as a real entity "buying stuff left and right in Kentucky" and named specific facilities (Henderson, Franklin-Simpson)
4. The Sapphire Care Group → Topaz transition history (2018 Preferred Care bankruptcy acquisition, Skilled Nursing News)
5. The active Metcalfe bid (Sep 2025, jpinews.com)

**The different CMS chains (Emerald, Benjamin Landa) are ownership-layer designations within the same network** — similar to how Portopiccolo operates through regional CMS chains but is one economic entity. The error was assuming different CMS chains = different operators. The correct interpretation: one operator (Topaz) with a complex ownership structure reflected through multiple CMS chain affiliations.

**Procedure lesson:** The 11-step source sequence must be completed fully — including state registry (step 8) and ALL facility websites (step 10) — before concluding. Field intelligence from the BD team is a valid source that should be incorporated. And different CMS chains at different facilities does NOT necessarily mean different operators — it can mean one operator with a multi-entity ownership structure.

### Sources
- KY DMS Long-Term Care Facility Listing (Excel, Feb 2026): Corporation = "Topaz Financial Services, LLC" on 21 facilities, Hal Brecher provider contact
- Skilled Nursing News (Jul 2018): "Sapphire Care Group to Take Over 21 Preferred Care Locations in Kentucky"
- Jobe for Kentucky / jpinews.com (Sep 16 2025): "Metcalfe Healthcare Center Sold: A Fresh Chapter Begins" — Topaz bid $11.15M, awarded
- ProPublica h-185094 (Pikeville): Chain = Emerald Healthcare, Key: Yisroel Chafetz
- ProPublica h-185266 (Elizabethtown): Chain = Benjamin Landa, Owners = Landa/Platschek/Rubenstein
- ProPublica h-185402 (Henderson): Chain = Benjamin Landa, same ownership structure
- ProPublica h-185217 (Metcalfe): Managing = Wells Health Services INC (transitional — Topaz bid Sep 2025)
- OpenCorporates: Topaz Financial Services LLC, KY registration #1019317, member Richard Platschek
- GLR Facility Dump 2026-03-13: 15 entries with Parent Company = TOPAZ HEALTHCARE
- topazfiscalservices.com: "Nursing Home Financial Services Company" (misleading — actually operator)
- linkedin.com/company/topaz-fiscal-services-llc: ~30 employees, Brooklyn NY
- Brooke Ritchie (field intelligence, 2026-04-07): confirmed Topaz as active KY operator, named Henderson and Franklin-Simpson

**Originally documented:** 2026-04-06 (ALF dedup Cluster 8, incorrectly as "phantom fiscal agent")
**Corrected:** 2026-04-07 (re-investigation triggered by Brooke's field intel, confirmed via KY state directory + acquisition history)

---

## WELLS HEALTH SYSTEMS (Wells Health Services INC)

**Canonical DB name:** `WELLS HEALTH SYSTEMS`
**Also known as:** Wells Health Services INC (ProPublica managing entity name)
**HQ:** 725 Harvard Drive, Owensboro, KY 42301
**Type:** Corporation, for-profit. Nursing home management and consulting.
**Founded:** October 10, 1991 (BBB)
**Leadership:** Jack T. Wells, President (BBB). Gregory Wells (ProPublica, since Jan 2008 — likely family).
**BBB:** A+ rating, not accredited. 34 years in business.
**Website:** wellshealthsystems.com (certificate error as of 2026-04-07)

#### Ownership Structure — Metcalfe Health Care Center (701 Skyline Dr, Edmonton KY, CCN 185217)

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | ProPublica (nonprofit corporation) | Unknown nonprofit entity (no direct owner disclosed) |
| **PropCo** | — | N/A (nonprofit) |
| **Management Company** | ProPublica managing entity (since Jan 2008) | Wells Health Services INC |
| **Management Sub-brand** | — | N/A |
| **Operator** | ProPublica + BBB (MEDIUM confidence) | **WELLS HEALTH SYSTEMS** |

**Confidence: MEDIUM.** ProPublica managing entity (since Jan 2008) + BBB business profile (Jack T. Wells, President, Owensboro KY, since 1991). No operator website accessible (cert error). No NPI found. KY CHFS PCH directory does not list this facility. CMS certified beds = 71.

**ProPublica personnel (CCN 185217):** Courtney Britt (Nov 2020), Cody Brooks (Jan 2022), Kaye Hope (Jan 2012), Sharon Howard (Jan 2023), Janine Lehman (Jan 2008), Benny Lile (May 2014), Jackie Parker (Jun 2024), Terry Skaggs (Jan 2008), Nancy Steele (Aug 2018), Gregory Wells (Jan 2008), Larry Wilson (Jan 2023).

**DB impact:** 2 rows at 701 Skyline Dr Edmonton KY. Row 5924 (AL, 2 beds) recode NULL → WELLS HEALTH SYSTEMS. Row 5925 (SNF mistyped ALF, 64 beds) retype ALF→SNF, recode INDEPENDENT → WELLS HEALTH SYSTEMS, beds 64→71.

**GLR discrepancy:** AL entry carries Parent Company = TOPAZ HEALTHCARE (fiscal agent, not operator — see Topaz systemic finding above). SNF entry carries Parent Company = INDEPENDENT (incorrect — Wells Health Systems is the managing entity). Both need GLR correction.

**Open question:** Wells Health Systems also operates an ALF at 725 Harvard Dr, Owensboro KY (per ElderLife listing). Not clear if they manage other nursing homes beyond Metcalfe. ProPublica only checked for this CCN. A broader search of Wells Health Systems across all KY CCNs could reveal additional facilities — but this is beyond the scope of Cluster 8.

#### Full 11-Step Source Sequence (2026-04-07)

| Step | Source | Finding |
|---|---|---|
| 1 | Forward Universe | NULL (AL row 5924), INDEPENDENT (SNF row 5925) |
| 2 | GLR Export | AL: Parent Co = TOPAZ HEALTHCARE. SNF: Parent Co = INDEPENDENT. Disagree with each other. |
| 3 | MUO Corporate History | No prior entry |
| 4 | Operator Research Log | Not previously researched |
| 5 | CMS Provider Info | CCN 185217. Nonprofit corporation. 71 certified beds. |
| 6 | ProPublica (h-185217) | Managing entity = Wells Health Services INC (since Jan 2008). No chain. No direct/indirect owners disclosed. |
| 7 | NIC MAP | No entry for Metcalfe Health Care Center in Edmonton KY. |
| 8 | State Registry (KY CHFS) | NOT LISTED in PCH directory (Feb 2026). Metcalfe County only has Harper's Home For The Aged. |
| 9 | NPI Registry | No results for Metcalfe Health Care, Wells Health Services, or Topaz Healthcare. |
| 10 | Operator website | No dedicated Metcalfe website. wellshealthsystems.com has cert error. Facebook page exists (metcalfehealthcarecenter). Chamber listing. |
| 11 | News / web | Wells Health Systems Inc: BBB A+ Owensboro KY, Jack T. Wells President, since 1991. ElderLife: ALF at 725 Harvard Dr Owensboro. Greg & Noreen Wells Bluegrass Hospice Care Center (separate entity, Wells family philanthropy). |

#### Sources
- ProPublica: projects.propublica.org/nursing-homes/homes/h-185217
- BBB: bbb.org/us/ky/owensboro/profile/nursing-home/wells-health-systems-inc-0402-159154279
- Owensboro Chamber: business.chamber.owensboro.com (Wells Health Systems member listing)
- ElderLife: elderlifefinancial.com (ALF listing at 725 Harvard Dr)
- KY CHFS PCH Directory (Feb 2026 PDF): NOT LISTED
- NPI Registry API: no results
- NIC MAP (Nov 2025): no entry for Edmonton KY
- GLR Facility Dump 2026-03-13: 2 entries — AL (Topaz), SNF (Independent)

**Discovered during:** ALF dedup cluster review, Cluster 8, punchlist item #1, 2026-04-07

---

## PHOENIX SENIOR LIVING

**Canonical DB name:** `PHOENIX SENIOR LIVING`
**HQ:** Roswell, Georgia
**Phone:** (678) 214-2900
**Website:** phoenixsrliving.com (redirects from phoenixseniorliving.com)
**Type:** For-profit. Owner-operator-developer of senior housing.
**Founded:** 2010 by Jesse Marinko
**Portfolio:** 45 properties across 9 southeastern states (per news Jan 2025); 29 communities per website; Seniorly lists 38. Count varies by source — may reflect development pipeline vs operating.
**Services:** Assisted Living, Independent Living, Memory Care, Skilled Nursing

**Leadership:**
- Jesse Marinko — CEO & Founder (25+ years senior living experience)
- Seth Pesek — EVP / Chief Financial Officer
- Summer Blizzard — SVP of Administration
- Caren Kiage — VP of Systems Integrations
- Dean Slye — VP of Human Resources
- Justin Harden — VP of Sales & Marketing
- Craig Streipe — VP of Financial Planning & Analysis
- Jennifer Roth — VP of Clinical Services

#### Ownership Structure — The Bungalos at Bowling Green (981 Campbell Ln, Bowling Green KY)

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | Unknown — ALF, no CMS/ProPublica | TBD |
| **PropCo** | NIC MAP (Owner col 18) | Msd-bowling Green LLC |
| **Management Company** | — | N/A (owner-operator model) |
| **Management Sub-brand** | — | N/A |
| **Operator** | FU + GLR + NIC MAP + website (HIGH confidence) | **PHOENIX SENIOR LIVING** |

**Confidence: HIGH.** 4 sources converge: Forward Universe, GLR Parent Company ("A Phoenix Senior Living Community"), NIC MAP Operator = PHOENIX SENIOR LIVING, phoenixsrliving.com dedicated facility page. News confirms real operator with 25-year CEO, 45 properties, Roswell GA HQ.

**NIC MAP presence:** Phoenix Senior Living appears as Operator on 10+ NIC MAP entries across AL, AR, GA, KY, MO, SC, VA. "The Bungalows" is a Phoenix brand used for multiple locations (Bowling Green KY, Branson MO, Chesterfield Village MO, Nevada MO, Springfield East MO).

**DB impact:** Attribution confirmed correct. No recode needed. Row 6100 (typo duplicate "Bungalows") deleted. Row 6098 kept, beds 19→28.

#### Full 11-Step Source Sequence (2026-04-07)

| Step | Source | Finding |
|---|---|---|
| 1 | Forward Universe | PHOENIX SENIOR LIVING on both rows |
| 2 | GLR Export | Parent Company = "A Phoenix Senior Living Community" |
| 3 | MUO Corporate History | No prior entry |
| 4 | Operator Research Log | Not previously researched |
| 5 | CMS | N/A — ALF |
| 6 | ProPublica | N/A — ALF |
| 7 | NIC MAP | Owner = Msd-bowling Green LLC (PropCo). Operator = PHOENIX SENIOR LIVING. |
| 8 | KY CHFS | NOT LISTED in Feb 2026 PCH directory |
| 9 | NPI Registry | No results |
| 10 | Operator website | phoenixsrliving.com/communities/the-bungalows-at-bowling-green/ — dedicated page, 981 Campbell Lane |
| 11 | News | Jesse Marinko CEO & Founder (since 2010), Roswell GA HQ, 45 properties, 9 states, SHN interview Jan 2025 |

#### Sources
- phoenixsrliving.com/communities/the-bungalows-at-bowling-green/ (checked 2026-04-07)
- phoenixsrliving.com/communities/ (checked 2026-04-07)
- NIC MAP (Nov 2025 export): Operator = PHOENIX SENIOR LIVING, Owner = Msd-bowling Green LLC
- GLR Facility Dump 2026-03-13: Parent Company = "A Phoenix Senior Living Community"
- Senior Housing News (Jan 21 2025): "Voices: Jesse Marinko, CEO and Founder, Phoenix Senior Living"
- CBInsights: phoenixsrliving company profile
- Seniorly: 38 properties listed

**Discovered during:** ALF dedup cluster review, Cluster 9, punchlist item #1, 2026-04-07

---

## LIFE CARE SERVICES (LCS) — Cypress Glen Campus

**Canonical DB name:** `LIFE CARE SERVICES`
**Parent entity:** LCS (Life Care Services LLC), Des Moines IA — second-largest senior living operator in the US
**Type:** Nonprofit CCRC management company. Manages communities for nonprofit boards. LLC legal entity type does NOT indicate PropCo — LCS is a major operator organized as an LLC.

#### Cypress Glen Retirement Community (100/1000 Hickory St, Greenville NC)

**Campus type:** CCRC / Life Plan Community. Est. 1987. 95 acres. The only Life Plan Community in eastern NC.
**Care levels:** IL (cottages, garden villas, apartments — bulk of campus), AL (~16 beds), MC (~12 beds, "Memory Care Cottage"), SNF (6 beds, CCN 345512, short-term rehab)
**GLR type:** CRCC. GLR beds=72, census=70 (campus aggregate across all licensed care). 9 patients, all Psychiatry.
**Average daily census (SNF):** 2 residents. This is a captive CCRC rehab unit, not a standalone SNF.

#### Ownership Structure

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | ProPublica (100%, since Oct 2013) | The United Methodist Retirement Homes, Incorporated (nonprofit) |
| **PropCo** | NIC MAP Owner = "Cypress Glen Retirement Community" | Self-owned by nonprofit — no separate PropCo |
| **Management Company** | ProPublica (since Jan 2000), CMS Chain, NIC MAP Operator, lcsliving.com | Life Care Services LLC |
| **Management Sub-brand** | — | N/A |
| **Operator** | CMS + ProPublica + NIC MAP + lcsliving.com (HIGH) | **LIFE CARE SERVICES** |

**Confidence: HIGH.** CMS chain = Life Care Services (SNF row 8810). ProPublica h-345512: managing entity = Life Care Services LLC since Jan 2000. NIC MAP Operator = Life Care Services. lcsliving.com/location-finder/north-carolina/greenville/cypress-glen/. DB SNF row already coded correctly.

**Key personnel (ProPublica):** Laurie Stallings (since Jan 1994), Terry Hayes (since Dec 2022), Gerardo Gonzalez Rodriguez (since Apr 2023). Stallings has been associated with this campus for 32 years.

**CCRC characterization:** This is NOT a market-competitive ALF/SNF. It is a captive care wing inside an entrance-fee CCRC. Residents enter through IL with a buy-in and transition to AL/MC/SNF as needs change. The 16 AL beds and 12 MC beds serve the existing CCRC resident population, not the open market. EWH's 9 Psych patients represent a minimal presence. All 3 DB rows should be flagged as CCRC units for punchlist item 12.

**DB impact:** Row 8810 (SNF) already coded LIFE CARE SERVICES — no change. Row 8901 (AL) recode INDEPENDENT → LIFE CARE SERVICES. Row 8902 (MC) recode NULL → LIFE CARE SERVICES. All 3 flagged as CCRC campus units.

**Address note:** SNF at "1000 HICKORY STREET" vs AL/MC at "100 Hickory St" — different building entrances on the 95-acre campus, not a data error. Both valid.

#### LLC ≠ PropCo Pattern Note

**Life Care Services LLC is an operator, not a PropCo, despite the LLC suffix.** This is an important refinement to punchlist item 9 (LLC audit): the LLC legal entity type is a signal to investigate, not a signal to reclassify. Detection criteria for distinguishing operator LLCs from PropCo LLCs:

| Signal | PropCo LLC | Operator LLC |
|---|---|---|
| Facility count | Usually 1 facility | Multiple facilities |
| Website | None or placeholder | Corporate site with portfolio, leadership, careers |
| CMS chain affiliation | No chain | Named chain |
| NIC MAP Operator field | Listed as Owner, not Operator | Listed as Operator |
| NPI | None | May have organizational NPI |
| ProPublica role | Listed as Direct Owner | Listed as Managing Entity |
| Industry recognition | None | Awards, news coverage, trade association membership |

Examples of operator LLCs: Life Care Services LLC, Emerald Healthcare LLC, Spring Arbor Management LLC. Examples of PropCo LLCs: Msd-bowling Green LLC, Elkhart AL Investors LLC, Shady Lawn I LLC.

**This distinction must be applied during the punchlist item 9/10 deep scrub.** Not every LLC in the corporate_name_raw field is a PropCo artifact. Some are legitimate operators with LLC as their legal entity type.

#### Sources
- ProPublica: projects.propublica.org/nursing-homes/homes/h-345512 (CCN 345512, 6 beds, nonprofit, LCS since Jan 2000, UMRH owner)
- lcsliving.com/location-finder/north-carolina/greenville/cypress-glen/ (LCS community listing)
- cypressglen.org (facility website, "Life Plan Community," 95 acres)
- NIC MAP (Nov 2025): Owner = Cypress Glen Retirement Community, Operator = Life Care Services
- GLR Facility Dump 2026-03-13: Type = CRCC, Parent Company = INDEPENDENT (wrong for AL), 72 beds, 9 pts
- U.S. News: health.usnews.com/best-nursing-homes/area/nc/cypress-glen-retirement-community-345512 (5-star CMS rating)
- CMS (DB row 8810 corp_attribution_source): Chain = Life Care Services

**Discovered during:** ALF dedup cluster review, Cluster 10, punchlist item #1, 2026-04-07

---

## FERN TERRACE (Davco Homes Inc.)

**Canonical DB name:** `FERN TERRACE`
**Legal entity:** Davco Homes Inc. (corporate), Simpson Family Holdings LLC / Simpson Family Holdings II LLC (KY licensee entities)
**Founded:** 1963 by Jack Simpson, Owensboro KY — Kentucky's oldest and largest personal care home chain
**Leadership:** Rob Simpson (owner/operator, admin at Bowling Green), Darin Simpson (co-operator). Jack Simpson (founder, still involved).
**Website:** fernterrace.com (copyright Davco Homes Inc.)
**Type:** Private, family-owned. Personal Care Homes (ALF).

#### Portfolio (KY CHFS + fernterrace.com, checked 2026-04-07)

| Facility | City | KY License | Licensee | Admin | Beds | DB Row | DB Corp (current) |
|---|---|---|---|---|---|---|---|
| Davco Rest Home | Owensboro | 100084PC | Simpson Family Holdings LLC | Stacey Helton | 92 | 17776 | DAVCO |
| Fern Terrace of Owensboro | Owensboro | 100096PC | Simpson Family Holdings II LLC | Shirley Carrico | 68 | 5784 | FERN TERRACE OF OWENSBORO, LLC |
| Fern Terrace of Mayfield | Mayfield | 100148PC | Simpson Family Holdings LLC | Kimberly Young | 140 | 5783 | FERN TERRACE OF OWENSBORO, LLC |
| Fern Terrace of Bowling Green | Bowling Green | 100403PC | Simpson Family Holdings LLC | Rob Simpson | 114 | 5785 | DAVCO |
| Fern Terrace of Murray | Murray | — | — | — | — | — | CLOSED (2021, staff shortage per WKMS/Murray Ledger) |

**Entity fragmentation in DB:** Same operator coded under 2 different corporate names: "FERN TERRACE OF OWENSBORO, LLC" (facility-level LLC applied to Owensboro + Mayfield) and "DAVCO" (corporate name applied to Bowling Green + Davco Rest Home). All 4 surviving rows recode to `FERN TERRACE`.

#### Ownership Structure

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | KY CHFS (licensee) | Simpson Family Holdings LLC / Simpson Family Holdings II LLC |
| **PropCo** | NIC MAP (Owner col 18) | Maf Real Estate LLC (Mayfield), Oft Real Estate LLC (Owensboro), Bgf Real Estate LLC (BG) |
| **Management Company** | NIC MAP (Operator col 41) | Davco Homes Inc. |
| **Management Sub-brand** | — | Fern Terrace (consumer brand across all locations) |
| **Operator** | NIC MAP + KY CHFS + fernterrace.com + news (HIGH) | **FERN TERRACE** |

**Confidence: HIGH.** NIC MAP Operator = Davco Homes Inc. (all 3 NIC entries). KY CHFS: all 4 facilities licensed to Simpson Family Holdings LLC entities. fernterrace.com: copyright Davco Homes Inc., locations page lists all facilities. News: Bowling Green Daily News, WKMS, Murray Ledger all reference Davco Homes / Simpson family.

#### Full 11-Step Source Sequence (2026-04-07)

| Step | Source | Finding |
|---|---|---|
| 1 | Forward Universe | 5 rows under 2 corp names: FERN TERRACE OF OWENSBORO LLC (3 rows), DAVCO (2 rows). Entity fragmentation. |
| 2 | GLR | Parent Company = FERN TERRACE OF OWENSBORO, LLC (on Mayfield entry). 124 pts at Mayfield. |
| 3 | MUO Corporate History | No prior entry |
| 4 | Operator Research Log | Not previously researched |
| 5 | CMS | N/A — ALF |
| 6 | ProPublica | N/A — ALF |
| 7 | NIC MAP | Operator = Davco Homes Inc. on all 3 entries. Owners = PropCo real estate LLCs. |
| 8 | KY CHFS (PCH Directory Feb 2026) | All 4 facilities licensed. Licensee = Simpson Family Holdings LLC / II LLC. Admins: Rob Simpson (BG), Kimberly Young (Mayfield), Shirley Carrico (Owensboro), Stacey Helton (Davco). Beds confirmed: 140, 68, 114, 92. |
| 9 | NPI | Not checked (ALF — low yield expected) |
| 10 | Operator website | fernterrace.com: copyright Davco Homes Inc. Lists Owensboro, Mayfield, Bowling Green, Davco. Founded 1963 Jack Simpson. |
| 11 | News | BG Daily News: Fern Terrace BG closing article (2023). WKMS: Murray closure (2021). Rob Simpson identified as owner of Davco Homes. Jack Simpson integrated KY personal care homes in 1960s. Served 10,000+ people since 1963. |

#### Sources
- KY CHFS Personal Care Home Directory (Feb 2026 PDF): Licenses 100084PC, 100096PC, 100148PC, 100403PC
- NIC MAP (Nov 2025): Operator = Davco Homes Inc. on all 3 entries
- fernterrace.com (checked 2026-04-07): copyright Davco Homes Inc., About page, DAVCO page
- fernterrace.com/davco-states-oldest-largest-personal-care-chain/: founding history
- GLR Facility Dump 2026-03-13: Parent Company = FERN TERRACE OF OWENSBORO, LLC
- Bowling Green Daily News (Dec 2023): Fern Terrace closure article
- WKMS (Oct 2021): Murray closure, Rob Simpson quoted
- Murray Ledger: staff shortage closure coverage

**Discovered during:** ALF dedup Pair 10 cleanup (V25.8 prep), punchlist item #1, 2026-04-07

---

## TRADITIONS MANAGEMENT (Traditions Management LLC)

**Canonical DB name:** `TRADITIONS MANAGEMENT`
**Note:** Communities are branded "Traditions Senior Living" — consumer-facing name. Corporate entity is Traditions Management LLC. No slash — same entity, not a parent/regional split.
**Legal entity:** Traditions Management LLC
**HQ:** Indiana (locally owned)
**Website:** traditionsmgmt.net
**Type:** Private, locally owned. ALF (Independent Living, Assisted Living, Memory Care).
**Portfolio:** 25 communities across IN (13), OH (8), KY (1), MI (2), FL (1). Growing — 4 more under construction.

**V25.8 action:** Recode 14 rows TRADITIONS → TRADITIONS MANAGEMENT.

**DISAMBIGUATION — Three companies share the "Traditions" name:**
1. **Traditions Senior Living / Traditions Management LLC** (IN/OH/KY/MI/FL) — this entity. 25 communities. traditionsmgmt.net.
2. **Tradition Senior Living** (TX) — Texas luxury CCRC developer. Perlman family (Jonathan Sr., Jonathan Jr., Holt). traditionseniorliving.com. Dallas/Houston/Fort Worth. COMPLETELY UNRELATED.
3. **Traditions Assisted Living** (Thorp WI) — single 16-bed facility. Contact references Sunlight Assisted Living. COMPLETELY UNRELATED.

DB row coded "Tradition Senior Living" (1 row, SC, HIGHPOINT AT FORT MILL) is a **misattribution** — neither the TX company nor the IN/OH company operates Highpoint. Highpoint is operated by HCC/Highpoint Property Group. Needs Procedure 3 investigation.

**Verified during:** V25.8 entity standardization, 8-step reconciliation, 2026-04-07

---

## ARBORS AT OHIO (Ark Opco Group LLC)

**Canonical DB name:** `ARBORS AT OHIO`
**CMS chain name:** Arbors At Ohio
**Legal entity:** Ark Opco Group LLC (100% owner since Jul 2015)
**Managing entities:** Noble Healthcare Management LLC (since Jul 2015), Prestige Administrative Services LLC (since Jan 2016)
**Principals:** Craig Flashner + Yitzchok Perlstein (since Jul 2015)
**Type:** For-profit. SNF + ALF. Ohio only.
**Website:** arborsofohio.com (timed out 2026-04-07)

**Portfolio:** 16 nursing homes in Ohio per web search + 9 ALF rows in DB = mixed SNF/ALF operator. All facilities follow "Arbors at [City]" naming convention.

**DB entity fragmentation:** ALF rows coded "ARBORS" (9 rows, 7 served), SNF rows from CMS coded "ARBORS AT OHIO" (11 rows, 3 served). Same operator split by source type. Some facilities appear under both (Carroll OH, Springfield OH — ALF row under ARBORS, SNF row under ARBORS AT OHIO at same campus).

**V25.8 action:** Recode 9 rows ARBORS → ARBORS AT OHIO.

**ProPublica verification (CCN 365527, Arbors at Springfield):** Chain = "Arbors At Ohio". Direct owner = Ark Opco Group LLC (100%). Indirect: B&Y Healthcare S Corp, B&Y Trust, Cody Healthcare S Corp, Craig Flashner 2007 Trust. Managing: Noble Healthcare Management LLC + Prestige Administrative Services LLC. Officers: Flashner + Perlstein.

**NOT the same as:** ARBOR COMPANY (36 rows), ARBOR CARE CENTERS (9 rows), ARBORETA HEALTHCARE (8 rows), or any other "Arbor" variant in the DB. Name similarity does NOT determine attribution.

**Verified during:** V25.8 entity standardization, 8-step reconciliation, 2026-04-07

---

## HARMONY SENIOR SERVICES

**Canonical DB name:** `HARMONY SENIOR SERVICES`
**Parent entity:** Smith/Packett Med-Com LLC (development arm) + Wessex Capital Investments (PE arm)
**Founded:** 1982 by James R. "Jim" Smith, Roanoke VA
**Ownership:** Family-owned (Smith family). NOT PE-backed. Hunter Smith (Jim's son) is President/Principal.
**HQ:** 34 Broad Street, Suite 200, Charleston SC 29401 (also Roanoke VA office)
**Website:** harmonyseniorservices.com
**Footprint:** ~48-50 communities across 12 states (VA, NC, SC, PA, WV, TN, GA, DE, IN, OH, KY, MD)
**Business model:** ALF/IL/MC only — does NOT operate SNFs. Memory care branded "Harmony Square." Growth is organic via Smith/Packett ground-up development, not acquisitive.
**PropCo naming convention:** "[City] AL Investors LLC" (e.g., Elkhart AL Investors LLC, Greensboro AL Investors LLC, Cumberland AL Investors LLC)

### Leadership (notable churn — 5 CEOs in ~7 years)
| Period | CEO |
|---|---|
| ~2018-2019 | Stephanie Handelson |
| 2019-2022 | Terry Howard (ex-MBK Senior Living) |
| 2022-2024 | Margaret Cabell (promoted from Chief Sales & Marketing Officer) |
| May 2024-late 2025 | Kenneth Segarnick (ex-Brandywine, 21 years) |
| Dec 2025-present | Traci Taylor-Roberts (ex-Sodalis Senior Living President) |

### DB Notes (2026-03-27 Cary Trainor reconciliation)
- **V22.7→V22.8:** GLR typo corrected "HARMONY SENOR SERVICES" → "HARMONY SENIOR SERVICES" (5 rows)
- **Elkhart misattribution:** "Elkhart AL Investors LLC" is PropCo — facility is HSS-operated per website. Needs recode → HARMONY SENIOR SERVICES. (V25.6 punchlist #13)
- **Harmony Hall Kinston NC misattribution:** Both SNF (175 beds) and ALF (50 beds) at 312 Warren Ave coded to HSS. SNF = Principle LTC (CMS Chain 423). HSS doesn't list Kinston, doesn't operate SNFs, and "Harmony Hall" doesn't follow HSS naming pattern ("Harmony at [City]"). Both rows likely should be Principle LTC. (V25.6 punchlist #14)
- **Rosewood Harmony (Harmony, NC):** NOT HSS. Independent family-owned ALF. "Harmony" is the town name. Correctly coded INDEPENDENT.
- **Naming-layer contamination:** 12 FP facilities have "Harmony" in the name but are operated by Heritage Place Business LLC, August Healthcare Group, Blue Central Group, Hillstone Healthcare, Palm Gardens, Harmony Residential Care Center (separate entity), etc.
- **V25.5 exact-match footprint:** 29 FP rows, 26 campuses, 5 served (VA 15, NC 6, SC 5, KY 1, OH 1, IN 1). After Elkhart recode and Harmony Hall removal: ~28 rows, 26 campuses.
- **Website lists 2 VA communities not in DB:** The Crossings at Ironbridge (Chester) and The Chamberlin (Hampton). Possible newer openings.

---

## PRINCIPLE LONG TERM CARE

**Canonical DB name:** Not yet in DB — needs evaluation
**Parent entity:** Hillco, Ltd.
**Founded:** 1956 by Robert Hill Sr., Kinston NC. Formerly operated as **Britthaven**.
**Ownership:** Family-owned (Hill family — Stephen B. Hill President, Robert Hill Jr. VP, R. Gregg Hill VP). NOT PE-backed.
**HQ:** 1435 US-258, Kinston NC 28504
**Website:** principleltc.com
**CMS Chain ID:** 423 (44 facilities at time of CMS extract)
**Footprint (post-KY sale):** ~37-38 SNFs in NC + 1-2 in VA
**Business model:** SNF-only. Also operates Cardinal Hospice Care (6 NC locations) and Principle Therapy Services.
**Subsidiary:** Redwood LTC Group LLC (facility-level licensee shell)

### Timeline
| Date | Event |
|---|---|
| 1956 | Hillco Ltd founded by Robert Hill Sr., Kinston NC |
| 1982+ | Developed nursing homes as Britthaven across VA, FL, Carolinas |
| ~2010s | Rebranded to Principle Long Term Care |
| 2025 Oct | Sold entire KY portfolio (7 facilities, 818 beds) to NJ-based buyer. Blueprint Healthcare brokered. Ends 40-year KY presence. |
| 2026 | 4 new NC facilities under construction (CON approved) |

### DB Notes (2026-03-27 Cary Trainor reconciliation)
- **Discovered via Harmony Hall investigation.** CMS Chain 423 identifies Harmony Hall Kinston SNF as Principle LTC, not HSS.
- **Meets 7+ gate easily (~37 campuses).** Needs evaluation for scoring board.
- **V25.6 punchlist #15:** Add as new entity, evaluate for tier.
- **KY portfolio sold Oct 2025** — CMS data (Feb 2026 extract) may still show 7 KY facilities under Chain 423 that are no longer Principle LTC.

### 8-Step Corporate Reconciliation (2026-04-04, punchlist #15)
1. **DB fuzzy name scan:** 56 rows under "PRINCIPLE" — NC (43), KY (10), VA (1), PA (1), MI (1). Also found under RICHMOND PINES HEALTHCARE (CCN 345293, stale corporate "Herndon Billy L" but current operator is Principle/Spruce LTC Group LLC per punchlist #3 research).
2. **CMS cross-reference:** Chain 423, 44 facilities at time of Feb 2026 extract. Includes KY facilities that were sold Oct 2025.
3. **Web validation:** principleltc.com confirms NC + VA operations. KY sold. HQ 1435 US-258 Kinston NC. Principle Therapy Services subsidiary (confirmed on harmonyhallcare.com). Cardinal Hospice Care subsidiary (6 NC locations).
4. **Consolidation:** 44 NC+VA rows in our operating states (post-KY-sale).
5. **Footprint filter:** NC (43 rows) + VA (1 row) = 44 rows in operating states. KY (10 rows) excluded — sold Oct 2025.
6. **Campus collapse:** 39 unique campus addresses in NC+VA, all 15+ beds.
7. **7+ gate: PASS (39 campuses).** Well above threshold.
8. **Score:** Scoring board frozen until June 6. Evaluate for tier when freeze lifts. Profile suggests T1-T2 based on campus count (39), geography (core NC + VA), business maturity (70 years), and operator type (family-owned SNF specialist).

### KY Portfolio Post-Sale Investigation (2026-04-04)

10 DB rows coded PRINCIPLE in KY across 6 addresses. Investigated per-facility via NPI, KY state licensing, and web research.

**Finding: Two separate outcomes, not one buyer.**

| Facility | City | Beds | Served | New Entity | Authorized Official | NPI Date | Assessment |
|---|---|---|---|---|---|---|---|
| Essex | Louisville | 128 | Yes | Hanging Rock LTC LLC | Gale Boice (CFO) | — | **PRINCIPLE internal restructuring.** Boice = Principle CFO = Hillco CFO. Same family. |
| Mountain View | Pineville | 115 | Yes | Hanging Rock LTC LLC | Gale Boice | — | Same as Essex |
| Somerwoods | Somerset | 166 | No | Hanging Rock LTC LLC | Gale Boice | — | Same as Essex |
| Tri-Cities | Cumberland | 69 | No | Hanging Rock LTC LLC | Gale Boice | — | Same as Essex |
| Rivers Edge | Prospect | 100 | Yes | Rivers Edge SNF Operations LLC | Menucha Goodman | Jul 16, 2025 | **NJ-based buyer (unknown identity).** "[Name] SNF Operations LLC" convention. |
| Lake Way | Benton | 96 | Yes | Lake Way SNF Operations LLC | Menucha Goodman | Jul 16, 2025 | Same buyer as Rivers Edge — both NPIs same day, same authorized official. |

**Hanging Rock LTC LLC (4 facilities):** NOT a sale to an external buyer. Gale Boice is CFO of Principle LTC, Hanging Rock LTC, and Hillco Ltd simultaneously. This is an internal restructuring — the Hill family retains control through a new operating LLC. **Keep coded as PRINCIPLE LONG TERM CARE.**

**Rivers Edge + Lake Way SNF Operations LLC (2 facilities):** These appear to be the facilities that actually transferred to the NJ-based buyer described in the Blueprint/SNN article. Both NPIs enumerated July 16, 2025 with Menucha Goodman as authorized official. Goodman does not surface publicly (no LinkedIn, no news, no industry presence). The "[Name] SNF Operations LLC" naming convention appears at other facilities nationally (Osprey FL, Bride Brook CT, Highland VA, RB/Red Bank NJ) but with different authorized officials — may be a common legal convention, not a single operator.

**Trail goes cold.** Buyer identity cannot be confirmed from public sources. CMS/ProPublica ownership data (Feb 2026 extract) has not yet updated. NJ state filings (RB SNF Operations LLC / Red Bank Center) are PDF documents that didn't parse.

**Action:** Rivers Edge and Lake Way remain coded PRINCIPLE for now. Logged to pending_followups.csv (IDs 1-2) with trigger = CMS/ProPublica update, check by July 2026.

**Sources:**
- SNN Dealbook Oct 2025: skillednursingnews.com (Blueprint brokered, NJ-based buyer, 818 beds, 7 facilities)
- NPI Registry API: Rivers Edge SNF Operations LLC (1487546487), Lake Way SNF Operations LLC (1699667691) — both Menucha Goodman, both Jul 16, 2025
- NPI Registry: Hanging Rock LTC LLC — multiple NPIs, all Gale Boice CFO
- KY Long-Term Care Directory Feb 2026: Essex owner = Robert Flatt / Hanging Rock LTC LLC; Lake Way = Lake Way SNF Operations LLC
- SNN Mar 2023: Gale Boice identified as Principle LTC CFO
- LinkedIn: Gale Boice = CFO at Principle LTC

### Harmony Hall Verification (2026-04-04, punchlist #14)
Per-facility verification confirmed both DB rows at 312 Warren Ave, Kinston NC are misattributed to HARMONY SENIOR SERVICES:
- **SNF (175 beds):** ProPublica confirms Principle IT Services Inc (50%) + Principle Long Term Care Inc (50%), Hill family ownership (Robert 21%, Stephen 20%, Raymond 18%). Managing entity = Principle LTC. CMS Chain 423. NC DHSR license NH0355 under Redwood LTC Group LLC. Recode to PRINCIPLE LONG TERM CARE.
- **ALF (50 beds):** No NC DHSR adult care home license found at 312 Warren Ave. HSS does not list Kinston and does not operate SNFs. "Harmony Hall" is the facility's historical name, coincidentally similar to "Harmony Senior Services" but unrelated. ALF row is a phantom (NIC MAP Trailing Type pattern). Flag for deletion.

Sources: ProPublica h-345156, harmonyhallcare.com, NC DHSR facility search, harmonyseniorservices.com/senior-living/nc/ (Kinston not listed).

---

## OAK HOLLOW HEALTHCARE MANAGEMENT (correction from "Brothers Healthcare / CJM Advisors")

**Canonical DB name:** `OAK HOLLOW HEALTHCARE MANAGEMENT`
**Current (incorrect) DB name:** `Brothers Healthcare / CJM Advisors`
**DB facility count:** 2
**Served:** 2 (both won Q1 2026 by Chad Vukelich)

### Facilities
| CCN | Facility Name (DB) | Facility Name (Monday.com) | Legal Business Name (CMS) | Location | Beds |
|---|---|---|---|---|---|
| 425310 | OAK HOLLOW OF SUMTER REHABILITATION CENTER | Pinewood Nursing Care | SUMTER OPERATIONS LLC | 1761 Pinewood Road, Sumter, SC | 96 |
| 425048 | OAK HOLLOW OF GEORGETOWN REHABILITATION CENTER LLC | Elderwood Rehabilitation and Nursing Center | GEORGETOWN OPERATIONS LLC | 2715 South Island Road, Georgetown, SC | 84 |

### Research Findings (2026-03-31)
- **"Brothers Healthcare"** is a specialty hemophilia/infusion pharmacy (brothershealthcare.com) founded by two brothers from hemophilia camp. **Zero connection to nursing homes.** Name in DB is a data source error.
- **"CJM Advisors"** has no web presence, no business filings found. Untraceable entity — possibly a former advisor or holding company that got coded as operator.
- **Oak Hollow Healthcare Management** (oakhollowhcm.com) is the actual operator. Established 2022. CEO: James Allen Cunningham. Mailing address: 416 Nuway Cir, Lenoir, NC 28645.
- **CMS chain affiliation: NONE.** Both facilities have blank Chain Name and Chain ID in CMS Provider Info (Mar 2026 extract). Each is a separate LLC with no registered chain link.
- **CMS quality:** Sumter has 1-star overall, 41 deficiencies. Georgetown has 2-star overall.
- Both facilities appear to have rebranded on Monday.com (Pinewood Nursing Care, Elderwood Rehabilitation) — these are NOT the DB-recorded names and are NOT the Elderwood chain (NY-based, unrelated).
- Managerial control at Sumter changed May 2025 to Brent Morrison, Loreli Munford, Traci Pollard (per CMS/ProPublica).

### Corporate Structure
```
Oak Hollow Healthcare Management (management company, Lenoir NC)
├── Sumter Operations LLC → Oak Hollow of Sumter (CCN 425310, Sumter SC)
└── Georgetown Operations LLC → Oak Hollow of Georgetown (CCN 425048, Georgetown SC)
```

### DB Actions Required (V25.6)
1. Rename Corporate_Name: `Brothers Healthcare / CJM Advisors` → `OAK HOLLOW HEALTHCARE MANAGEMENT` (both rows)
2. Update Corp_Attribution_Source to reflect CMS/web verification 2026-03-31
3. Update Do_We_Serve to `Yes` for both facilities (won Q1 2026)
4. Note Monday.com name discrepancy: AEs are using rebranded names, DB retains CMS-registered names

### Sale Type Classification
- Sumter (won 2026-01-23): **New Logo** — first facility under this operator
- Georgetown (won 2026-02-06): **New Door** — second facility under same operator, won after Sumter

**Discovered during:** BD Slides sale type reconciliation, 2026-03-31

---

## BHP/ENCORE → BLUEGRASS/ENCORE (corporate name normalization)

**Canonical DB name:** `BLUEGRASS/ENCORE`
**Incorrect DB variant:** `BHP/Encore`
**DB facility count under variant:** 1
**DB facility count under canonical:** 92 (50 served)

### Facilities Affected
| Facility | Current Corp | Correct Corp | Location | CCN |
|---|---|---|---|---|
| BELMONT TERRACE NURSING AND REHABILITATION CENTER | BHP/Encore | BLUEGRASS/ENCORE | 7300 Woodspoint Drive, Florence, KY | — |

### Research Findings (2026-03-31)
- BHP/Encore is a name variant of Bluegrass/Encore. The facility is in Florence, KY — squarely in the Bluegrass/Encore Kentucky footprint.
- BLUEGRASS/ENCORE operates 92 facilities in the DB (50 served), almost all in Kentucky with some in OH, WI, MI, IL, MN.
- Belmont Terrace was won as EST (Integration/Cross-sell) by Adam Sabie, established 2026-02-09, 90 MH consents.
- The split into two corp names is a data source artifact.

### DB Actions Required (V25.6)
1. Rename Corporate_Name: `BHP/Encore` → `BLUEGRASS/ENCORE` (1 row)
2. Update Do_We_Serve to `Yes` (facility is EST, actively served as of Feb 2026)

**Discovered during:** BD Slides sale type reconciliation, 2026-03-31

---

## BROOKDALE SENIOR LIVING — Ohio INDEPENDENT Coding Issue

**Canonical DB name:** `BROOKDALE SENIOR LIVING`
**Issue:** 9 Brookdale-branded facilities in Ohio coded as `INDEPENDENT` instead of `BROOKDALE SENIOR LIVING`

### Facilities Affected
| Facility | City | State | Current Corp | Beds |
|---|---|---|---|---|
| BROOKDALE ALLIANCE | Alliance | OH | INDEPENDENT | 50 |
| BROOKDALE BEAVERCREEK | Dayton | OH | INDEPENDENT | 60 |
| BROOKDALE CAMELOT MEDINA | Medina | OH | INDEPENDENT | 150 |
| BROOKDALE CENTENNIAL PARK | Englewood | OH | INDEPENDENT | 60 |
| BROOKDALE GREENVILLE | Greenville | OH | INDEPENDENT | 96 |
| BROOKDALE LAKEVIEW CROSSING | Groveport | OH | INDEPENDENT | 99 |
| BROOKDALE SPRINGDALE ASSISTED LIVING | Springdale | OH | INDEPENDENT | 72 |
| BROOKDALE SPRINGDALE MEMORY CARE | Springdale | OH | INDEPENDENT | 42 |
| BROOKDALE TRILLIUM CROSSING | Columbus | OH | INDEPENDENT | 120 |

### Research Context (2026-03-31)
- Brookdale Lakeview Crossing was won by Adam Sabie (established 2026-03-05, 45 ALF PCP consents).
- Other Brookdale facilities in the same Ohio metro (Pinnacle, Westerville, Muirfield) are correctly coded as `BROOKDALE SENIOR LIVING`.
- Brookdale Muirfield (Dublin, OH) — 10 miles from Lakeview Crossing — is coded BROOKDALE SENIOR LIVING and Do_We_Serve = Yes.
- Likely a NIC MAP sourcing artifact: these may be independently owned properties with Brookdale management/branding, coded by PropCo instead of operator.
- Per operator attribution rule: if Brookdale is the clinical/business decision-maker, these should be `BROOKDALE SENIOR LIVING`.

### Verification (2026-04-04)
All 9 facilities confirmed on brookdale.com with full Brookdale branding and "© Brookdale Senior Living Inc" copyright. These are Brookdale-operated communities, not independently owned with Brookdale management. The INDEPENDENT coding was a NIC MAP artifact (PropCo LLC as corporate name → count of 1 → classified Independent).

| Facility | Brookdale URL | Confirmed |
|---|---|---|
| Brookdale Alliance | brookdale.com/en/communities/brookdale-alliance.html | Yes |
| Brookdale Beavercreek | brookdale.com/en/communities/brookdale-beavercreek.html | Yes |
| Brookdale Camelot Medina | brookdale.com/en/communities/brookdale-camelot-medina.html | Yes |
| Brookdale Centennial Park | brookdale.com/en/communities/brookdale-centennial-park.html | Yes |
| Brookdale Greenville | brookdale.com/en/communities/brookdale-greenville-oh.html | Yes |
| Brookdale Lakeview Crossing | brookdale.com/en/communities/brookdale-lakeview-crossing.html | Yes |
| Brookdale Springdale (AL) | brookdale.com/en/communities/brookdale-springdale.html | Yes (covers AL + MC) |
| Brookdale Springdale (MC) | (same URL — one campus, two DB rows) | Yes |
| Brookdale Trillium Crossing | brookdale.com/en/communities/brookdale-trillium-crossing.html | Yes |

**Action:** Recode all 9 rows INDEPENDENT → BROOKDALE SENIOR LIVING. Update Lakeview Crossing Do_We_Serve → Yes. Sale type changes from New Logo to New Door. Ready for V25.7.

### DB Actions Required (V25.6)
1. **Verify operator** for all 9 facilities — confirm Brookdale Senior Living is the clinical operator, not just the brand licensee
2. If confirmed: recode Corporate_Name from `INDEPENDENT` → `BROOKDALE SENIOR LIVING` (9 rows)
3. Update Do_We_Serve for Brookdale Lakeview Crossing to `Yes` (won Mar 2026)
4. Sale type impact: Lakeview Crossing changes from New Logo → **New Door** (we serve 45 Brookdale facilities)
5. **NIC MAP confirmation (2026-04-01):** NIC MAP Owner = "NHP McClain LLC" (PropCo), Operator = "Brookdale Senior Living Inc." — confirms Brookdale is the operator, not INDEPENDENT.

**Discovered during:** BD Slides sale type reconciliation, 2026-03-31

---

## TRIPLE CROWN SENIOR LIVING / CHANDLER MEMORY CARE (CHOW confirmation)

**Canonical DB name:** `TRIPLE CROWN SENIOR LIVING`
**Previous operator:** Chandler Memory Care (pre-July 2022)
**NIC MAP name (Nov 2025 export):** Chandler Memory Care (stale — 3+ years post-acquisition)

### Facilities Affected
| Facility | Location | Current Name | Previous Name |
|---|---|---|---|
| Cardinal Landing Memory Care | 1310 Campbell Lane, Bowling Green, KY | Cardinal Landing Memory Care | Chandler Memory Care |
| Chandler Park Assisted Living | Bowling Green, KY | Chandler Park Assisted Living | Chandler Park Assisted Living |

### Timeline
| Date | Event | Source |
|---|---|---|
| Pre-2022 | Facilities operated as Chandler Memory Care and Chandler Park Assisted Living | NIC MAP, Kentucky Senior Living Association |
| July 2022 | Denton Floyd Real Estate Group and Triple Crown Senior Living closed acquisition of both communities (92 total units: 61 AL + 31 MC) | triplecrownseniorliving.com |
| Post-2022 | Chandler Memory Care rebranded to Cardinal Landing Memory Care | aplaceformom.com, cardinallandingmemorycare.com |

### NIC MAP Cross-Reference (2026-04-01)
- NIC MAP Owner: Chandler Senior LLC (PropCo)
- NIC MAP Operator: Chandler Memory Care (STALE — pre-acquisition name, 3+ years behind)
- DB: TRIPLE CROWN SENIOR LIVING (correct, post-acquisition)
- NIC MAP export date: Nov 17, 2025

### Notes
- Triple Crown Senior Living: 10 communities, 872 units, KY/IN/OH/TN. Established 2017.
- Chandler Park Assisted Living (sister community) in Monday.com pipeline: Samantha Roark, Consenting, March 2026.
- NIC MAP PropCo entity (Chandler Senior LLC) retains the pre-acquisition name.

**Discovered during:** NIC MAP cross-reference during sale type verification, 2026-04-01

---

## HILL VALLEY / LYON / BEDROCK — Chopp Family Corporate Family

**Canonical DB names:** `LYON HEALTHCARE` (Chain 837, KY/TN), `HILL VALLEY HEALTHCARE` (Chain 270, MD/NV/TN/VA/WA/WV), `BEDROCK HEALTHCARE` (Chain 73, WI/FL)
**DB facility count:** Lyon 9 (KY), Hill Valley ~39 (multi-state), Bedrock ~6 (WI/FL). Combined ~59 facilities.
**Served:** 3 under Lyon (Chestnut Ridge, Hartland Park x2 in KY)
**Controlling family:** Tzali "Martin" Chopp, Pnina Chopp, Solomon Chopp (Suffern, NY / Lakewood, NJ)

### The Corporate Structure

These are **three CMS chain registrations operated by one family** using layered holding entities. Lyon Healthcare is not an independent company — it is a consumer-facing brand for the Chopp family's Kentucky/Tennessee operations. Hill Valley Healthcare is the primary national brand. Bedrock Healthcare is the secondary brand for Wisconsin and Florida.

```
CHOPP FAMILY (Tzali/Martin, Pnina, Solomon)
  |
  |-- Opal Healthcare (management/holding umbrella)
  |     |-- Opal Healthcare WI LLC (Wisconsin)
  |     |-- Opal Healthcare FL LLC (Florida)
  |
  |-- HOLDING ENTITIES
  |     |-- MC Capital 2 LLC / MC Capital Trust (Martin Chopp)
  |     |-- SC Capital 2 LLC / SC Capital Trust (Solomon Chopp)
  |     |-- TC Capital 2 / TC Capital Trust (Tzali Chopp)
  |     |-- Lion 26 Holdings LLC (5%+ indirect in 37+ Hill Valley facs)
  |     |-- Sabrina 1818 Holdings LLC (5%+ indirect in 38+ Hill Valley facs)
  |     |-- Saessy Irrevocable Trust
  |     |-- Tatiriq Irrevocable Trust
  |
  |-- OPERATING CHAINS (3 separate CMS Chain IDs)
  |     |-- Hill Valley Healthcare (Chain 270) — 39 facs: MD, NV, TN, VA, WA, WV
  |     |     Co-CEOs: Shimmy Idels, Steven Schwartz (Woodmere/Flushing NY)
  |     |
  |     |-- Lyon Healthcare (Chain 837) — 14 facs: KY, TN
  |     |     Brand only. No independent leadership. Website metadata = "Hill Valley Healthcare"
  |     |     Facility LLCs are "Bedrock HC at [Name]" entities owned by Chopp family
  |     |
  |     |-- Bedrock Healthcare (Chain 73) — 6-8 facs: WI, FL
  |           COO: Kenny Nichols, CDO: Sol Chopp
  |           HQ: Abbotsford, WI
  |
  |-- REAL ESTATE (leased, not owned)
        |-- Strawberry Fields REIT (KY facilities — lists Hill Valley as operator/tenant)
        |-- Golden Living (WI facilities, retained ownership post-Dycora)
```

### Evidence Chain

| Evidence | What It Proves |
|---|---|
| CMS ownership filings for Green Meadows (185464) | Legal entity = "Bedrock HC at Green Meadows LLC." Owners: Abraham, Lynn, Martin, Pnina, Rachel Chopp + Kenneth Nichols. Chain affiliation = Lyon Healthcare (837). |
| CMS ownership filings for Indigo Manor FL (105570) | Legal entity = "Bedrock HCS at Daytona FL LLC." Owners: Martin, Pnina, Solomon Chopp. Chain = Bedrock (73). Same family on both chains. |
| CMS ownership filings for Hill Valley (Chain 270) | 37-38 facilities held through Lion 26 Holdings LLC, Sabrina 1818 Holdings LLC, Saessy Irrevocable Trust, Tatiriq Irrevocable Trust — all Chopp family vehicles. |
| lyonhc.com HTML metadata | Publisher field = "Hill Valley Healthcare." Lyon site built under Hill Valley identity. |
| Parkwood facility logo file | Named "HVH_lyon_parkwood_web_logo.png" — HVH = Hill Valley Healthcare. |
| Strawberry Fields REIT portfolio | Lists Hill Valley Healthcare as operator/tenant for 11 KY properties that CMS shows under Lyon Healthcare Chain 837. |
| Lyon facility websites (chestnutridgehr.com, greenmeadowshr.com, parkwoodhr.com) | Footer: "Serviced by Lyon Healthcare." Strawberry Fields says Hill Valley. CMS says Lyon. All the same facilities. |
| bedrockhcs.com/our-team/ | Sol Chopp = CDO, Kenny Nichols = COO. CMS filings confirm both as owners/managers on Bedrock AND Lyon facilities. |

### Management Teams

| Entity | Leadership | Notes |
|---|---|---|
| Hill Valley Healthcare | Shimmy Idels (Co-CEO, LNHA), Steven Schwartz (Co-CEO/Principal) | Idels previously at Centers Health Care network (NY). HQ Woodmere/Flushing NY. |
| Bedrock Healthcare | Kenny Nichols (Co-Founder/COO), Sol Chopp (CDO), Benny Waknin (Dir Ops), Mitzie Cannon RN-BC (CNO) | Nichols previously SVP Ops at Infinity Healthcare Mgmt + Brookdale. |
| Lyon Healthcare | None published | Brand facade. No independent leadership. |

### Timeline

| Date | Event | Source |
|---|---|---|
| 2018 | Hill Valley Healthcare founded (Flushing/Woodmere, NY). Lion 26 Holdings LLC filed in LA, CA and Lawrence, NY. | D&B, state filings |
| Nov 2018 | Bedrock Healthcare founded by Kenny Nichols | bedrockhcs.com |
| 2018-2019 | Green Meadows (KY) and Spring Meadows (TN) — first Bedrock facilities, filed as "Bedrock HC at [Name] LLC," chain-affiliated under Lyon Healthcare | CMS |
| 2019 | HJ Sims $4M HUD Plus loan for Hill Valley JV portfolio (2 SNFs + 1 ALF) | Senior Housing News |
| Oct 2019 | Bedrock assumes operations of 7 former Dycora facilities in Wisconsin (receivership) | Industry news |
| Jul 2021 | Bedrock acquires Indigo Manor, Daytona Beach FL | CMS ownership filings |
| Jan 2021 | Hill Valley acquires 3 Riverside Lifelong Health facilities in Virginia | Industry news |
| May 2022 | Hill Valley acquires The Woodland CCRC, Farmville VA ($35.25M, Ziegler-advised). 10th VA facility, 20th overall. | Senior Housing News / Ziegler |
| 2022 | Hill Valley acquires TLC Care Center, Las Vegas NV ($50M, 255 beds) — first NV facility | Industry news |
| Sep 2024 | Hill Valley acquires Cortland Acres, Thomas WV (corporate asset purchase) | Industry news |
| May 2025 | GPH v. Chopp lawsuit filed (NJ District Court) naming Lynn, Martin, Pnina, Rachel, Sarah, Solomon Chopp and Bedrock HC WI LLC | Court filings |
| Jul 2025 | 4 Wisconsin Bedrock facilities placed in court-ordered receivership. 384 cited deficiencies. $2.6M+ owed in rent/backpay. | WI DHS, news |
| Feb 2026 | Nussbaum v. Chopp lawsuit — $6.3M claim, $1M linked to Opal Healthcare WI | The Real Deal |

### Risk Factors

- **4 Wisconsin Bedrock facilities in receivership** (Jul 2025): Silver Springs (Glendale), Heritage Square (Greenfield), Riverdale (Muscoda), Fort Atkinson. 384 deficiencies, resident death and alleged sexual assault cited, $270K+ federal fines at Fort Atkinson.
  - Source: Wisconsin DHS / local news coverage of receivership proceedings
- **GPH v. Chopp lawsuit** (May 2025): GPH Muscoda LLC, GPH Greenfield LLC, GPH Fort Atkinson LLC, Silver Spring Acquisition LLC v. Bedrock HC WI LLC, Lynn Chopp, Martin Chopp, Pnina Chopp, Rachel Chopp, Sarah Chopp, Solomon Chopp, Avrohom Prager, Shulamit Prager. NJ District Court.
- **Nussbaum v. Chopp** (Feb 2026): Mark Nussbaum (via liquidator Sheldon Eisenberger) suing Tzali Chopp for $6.3M (originally $3M loan + interest). $1M of the loan went to Opal Healthcare WI.
  - Source: The Real Deal (therealdeal.com) — "Mark Nussbaum turns on nursing home magnate Tzali Chopp" (Feb 2026)
- **Bacon's Rebellion investigative series**: Hill Valley's rapid acquisition of 18 Virginia nursing homes flagged for complex LLC structures obscuring true ownership and underfunded state oversight allowing out-of-state for-profit chains to operate with minimal scrutiny.
  - Source: baconsrebellion.com — series on Virginia nursing home ownership opacity

### DB Impact

- Lyon Healthcare (9 DB rows, 3 served in KY) and Hill Valley Healthcare (~39 facilities, multi-state) are the **same corporate family**
- For sale type classification: any facility under Lyon, Hill Valley, OR Bedrock should check served status across ALL THREE chains
- Green Meadows and Elkhorn verified as **New Door** (HIGH confidence after this research — we serve 3 Lyon/Hill Valley/Bedrock family facilities)
- Consider whether DB should carry a parent entity field linking Lyon/Hill Valley/Bedrock, or consolidate under one canonical name
- Risk factors (receivership, lawsuits) are relevant for corporate scoring and should be flagged for Brooke/Cary

### Sources (with URLs)

| Source | URL | What It Shows |
|---|---|---|
| CMS Provider Info | data.cms.gov — CCN 185464 (Green Meadows), 445402 (Spring Meadows), 105570 (Indigo Manor) | Chopp family ownership filings across Lyon and Bedrock chains |
| ProPublica | projects.propublica.org/nursing-homes/homes/h-185464, h-105570 | Ownership %, managing entities, dates |
| Strawberry Fields REIT | strawberryfieldsreit.com (portfolio page) | Lists Hill Valley Healthcare as operator/tenant for 11 KY properties |
| Bedrock Healthcare | bedrockhcs.com | Facility list, team page (Sol Chopp CDO, Kenny Nichols COO) |
| Bedrock Team Page | bedrockhcs.com/our-team/ | Named leadership with email addresses |
| Lyon Healthcare | lyonhc.com | HTML source: publisher = "Hill Valley Healthcare" |
| Parkwood facility site | parkwoodhr.com | Logo file: "HVH_lyon_parkwood_web_logo.png" |
| Hill Valley Healthcare | hillvalleyhc.com | Corporate site, identical template to lyonhc.com, jobs via Apploi |
| Hill Valley Jobs | jobs.apploi.com/profile/hill-valley-healthcare-corporate | Job postings confirming operational footprint |
| Green Meadows facility | greenmeadowshr.com | Footer: "Serviced by Lyon Healthcare" |
| Chestnut Ridge facility | chestnutridgehr.com | Footer: "Serviced by Lyon Healthcare" |
| Spring Meadows facility | springmeadowshr.com | Footer: "Serviced by Lyon Healthcare" — also listed on bedrockhcs.com |
| Senior Housing News | seniorhousingnews.com — search "Hill Valley Healthcare" | Acquisition history (Woodland CCRC, TLC Care Center, Riverside) |
| The Real Deal | therealdeal.com — "Mark Nussbaum turns on nursing home magnate Tzali Chopp" (Feb 2026) | $6.3M lawsuit, Opal Healthcare WI link |
| Bacon's Rebellion | baconsrebellion.com — Hill Valley Virginia investigation series | LLC opacity, regulatory gaps |
| D&B | Hill Valley Healthcare LLC profile — Woodmere NY 11598, key principal Steven Schwartz | Corporate registration, industry classification |
| Ziegler | ziegler.com — May 2022 Woodland CCRC advisory | $35.25M acquisition, confirms Hill Valley as buyer |

**Discovered during:** Verification Report V3, NB/LOB Reconciliation, 2026-04-03
**Confidence:** HIGH — CMS ownership filings directly link Chopp family members across all three chains

---

## MARX DEVELOPMENT GROUP / MAJESTIC CARE / BLUEGRASS CONSULTING GROUP — Corporate Family

**Proposed DB canonical names:** `MAJESTIC / MAJESTIC CARE` (IN, OH, MI, FL, WI), `MAJESTIC / BLUEGRASS CONSULTING GROUP` (KY)
**Current DB names:** MAJESTIC CARE (53 rows), DAVID MARX (8 rows), MAJESTIC MANAGEMENT LLC (2 rows) = 63 rows
**DB facility count:** 63 (IN 26, KY 17, OH 15, MI 4, FL 1)
**Served:** 29 (IN 12, KY 17)
**Parent:** Marx Development Group (MDG), David Marx CEO, NYC
**Operating umbrella:** Majestic Management, Paul Pruitt CEO, Westfield IN

### The Corporate Structure

Marx Development Group is a vertically integrated NYC real estate developer (founded 1986 by David Marx, attorney/JD Fordham). MDG owns the physical properties (PropCo) and operates healthcare facilities through subsidiaries. Majestic Management is the operating umbrella with two consumer-facing brands that are deliberately separated by geography.

```
MARX DEVELOPMENT GROUP (David Marx, CEO — NYC)
  |-- Real estate owner (PropCo) — per-facility realty LLCs (e.g., "Howard Creek Road SNF Realty LLC")
  |-- Manhattan Regional Center (EB-5 immigrant investor capital)
  |-- Rockhall Funding Corp (HUD-licensed mortgage lender, $700M+)
  |-- Atria Builders LLC (construction)
  |-- DSM Design Group (architecture)
  |
  +-- MAJESTIC MANAGEMENT (Paul Pruitt, CEO — Westfield, IN)
        |-- Operating parent for all healthcare operations
        |-- HQ: 777 E Main Street, Westfield, IN 46074
        |
        +-- MAJESTIC CARE (brand for IN/OH/MI/WV)
        |     ~48 locations branded "Majestic Care of [City]"
        |     Website: majesticcare.com
        |     Title tag: "Indiana, Ohio, Michigan, and West Virginia"
        |     Kentucky deliberately excluded from this brand
        |
        +-- BLUEGRASS CONSULTING GROUP (brand for KY)
              10-11 locations branded "[City] Nursing and Rehabilitation"
              or standalone names (Seneca Place, Wellington Parc)
              No standalone website. LinkedIn: linkedin.com/company/bluegrass-consulting-group
              Formed: July 25, 2019 in Indiana (not Kentucky)
              HQ: 777 E Main Street, Westfield, IN (same as Majestic Care)
              Email domain: bluegrasscg.com (but compliance hyperlink leaks to majesticcare.com)
```

### Evidence Chain

| Evidence | What It Proves |
|---|---|
| McKnight's (2025): "Through its subsidiaries, Majestic Care and Bluegrass Consulting Group, [MDG] owns 55 properties with more than 5,000 licensed beds" | MDG is the parent. Majestic Care and BCG are both subsidiaries. |
| Mountain State Spotlight Q&A: Pruitt confirms "Majestic Care is a subsidiary of Marx Development Group" | Direct CEO confirmation of MDG parentage. |
| Wellington Parc press release (Owensboro Times, Sep 2025): BCG is "a Majestic Management company," Pruitt quoted as "CEO of Majestic Management" | BCG operates under Majestic Management umbrella. Pruitt is CEO of both. |
| Margaret Chamberlain profile (American Healthcare Leader, 2025): "General Counsel of Majestic Care and Bluegrass Consulting Group" | Shared legal counsel across both brands. |
| Elliott NR privacy notice (elliottnr.com): compliance email hyperlink points to compliance@majesticcare.com while displaying compliance@bluegrasscg.com | Shared compliance infrastructure. |
| BCG Holdings LLC (Indiana filing, July 25, 2019): principal office 777 E Main, Westfield IN. CEO: Bernie McGuinness. | Same HQ as Majestic Care. Same founder. |
| NPI records for all KY facilities: authorized official = Paul Pruitt, mailing address = 100 Boulevard of Americas, Lakewood NJ 08701 | Pruitt (Majestic CEO) controls KY facility NPI registrations. Lakewood NJ = LTC Consulting Services (back-office hub). |
| David Marx CMS ownership (Chain 179): 46 facilities across IN/KY/MI/OH. IN/OH/MI branded "Majestic Care of [City]", KY branded "[City] Nursing and Rehabilitation" | Same owner, different brands by state. |
| majesticcare.com title: "Indiana, Ohio, Michigan, and West Virginia" | Kentucky deliberately excluded from Majestic Care brand. |
| Paul Pruitt bio on majesticcare.com: member of KHCA (Kentucky Health Care Association) | Only KY reference on the entire Majestic Care website — he's on the KY board but the brand doesn't claim KY. |
| J. David Alexander (COO, Majestic Care): ZoomInfo also lists him as "President, Business Development, Marx Development Group" | Direct MDG-to-Majestic executive bridge. |
| NIC Spring Conference 2026 (McGuinness bio): "co-founder of both Majestic Care and Bluegrass Consulting Group" | Co-founder confirms both entities created together. |
| FlippingBook digital publication: "Majestic Care and Bluegrass Consulting Group" (joint corporate flipbook) | Presented together as one corporate family in marketing materials. |
| All KY facility websites (elliottnr.com, boydnr.com, carternr.com, etc.): identical WordPress "health-theme" template. Wellington Parc schema markup references "Elliott Nursing and Rehabilitation" — sites cloned from one template. | Centralized web management across all KY facilities. |

### Leadership

| Entity | Name | Title | Notes |
|---|---|---|---|
| MDG | David Marx | CEO/Founder | JD Fordham, attorney since 1986. 5,000+ beds across IN/KY/MI/NY/OH/WV. |
| Majestic Management | Paul Pruitt, MBA, NHA | CEO | Since June 2023. Formerly COO Mission Point Healthcare Services (MI). KHCA/IHCA/OHCA/HCAM board. |
| Majestic Care | J. David Alexander | COO | Also "President, Business Development, Marx Development Group" per ZoomInfo. Direct MDG bridge. |
| Majestic Care | Anzhelika Shatrov | CFO | Operations, finance, corporate governance. |
| Majestic Care | Eric Wolfe, RN, DNP | CNO | Nursing administration. |
| Majestic Care | Dr. Robert Russell | CMO | Also listed as CMO on Elliott Nursing website. |
| Both MC + BCG | Margaret Chamberlain | General Counsel | Dual title explicitly stated. 25 yrs post-acute care law. |
| Majestic Care | Angie Rewa, MBA, CHC, CHIAP | Compliance/Privacy Officer | Since Oct 2023. |
| Majestic Care | Patricia Sirmon | VP Human Resources | Formerly VP HR Medxcel and Meridian Title. |
| BCG | Jordan Vinson | VP of Operations | Central City, KY. BCG-specific role. |
| BCG | Michelle Jarboe, RN, LNHA | Regional VP of Operations | Lexington, KY. Email: bluegrasscg.com domain. |

**Former leadership:**
- Bernie McGuinness — Co-founder, CEO 2018-May 2023. Now President/CEO of Journey (new SNF operator, Noblesville IN, 21 buildings by Nov 2024).
- Donn Kump — Co-founder, CFO 2018-June 2025. Now VP Reimbursement at Journey.

### Timeline

| Date | Event | Source |
|---|---|---|
| 1986 | Marx Development Group founded by David Marx (attorney, NYC) | MDG website, Manhattan Regional Center |
| Jun 2018 | Majestic Care founded by Bernie McGuinness and Donn Kump | SNN, American Healthcare Leader |
| Jul 25, 2019 | Bluegrass Consulting Group LLC and BCG Holdings LLC formed in Indiana (consecutive entity numbers) | Indiana SOS filings |
| May 2019 | Diversicare announces exit from Kentucky — 10 SNFs (~885 beds). Omega Healthcare Investors (REIT landlord) selects replacement operator. | SNN |
| Aug 6-7, 2019 | New NPI records created for all KY facility LLCs. Authorized official: Paul Pruitt. Mailing: Lakewood NJ. | NPI Registry |
| Aug 30, 2019 | Diversicare completes Kentucky exit. BCG assumes operations of 9 KY SNFs. | SNN |
| Sep 2019 | BCG effective date as CMS managing entity on KY facilities. | CMS ownership filings |
| Jul 2021 | Majestic acquires 5 facilities (3 IN, 2 MI). David Marx identified as purchaser. 21 SNFs + 5 ALFs at this point. | SNN |
| Apr 2022 | Majestic at 27 SNFs + 7 ALFs across IN/OH/MI. | SNN |
| May 2023 | McGuinness resigns as CEO. Paul Pruitt named CEO. | SNN |
| Jan 2025 | Majestic adds 6 Ohio facilities. | SNN Dealbook |
| Sep 2, 2025 | BCG acquires Wellington Parc, Owensboro KY ($9.475M). Buyer entity: "Majestic Care of Wellington Parc LLC." | Owensboro Times |
| 2025 | Majestic acquires 4 WV state-owned facilities ($60M). Enters West Virginia. | McKnight's, WV Watch |
| Jun 2025 | Donn Kump departs for Journey. | LinkedIn |

### Diversicare-to-Marx Transition (2019)

Diversicare Health Services operated in Kentucky for 25 years before announcing its exit in May 2019. Omega Healthcare Investors (NYSE: OHI) was the REIT landlord. Omega selected the replacement operator (not publicly named in industry press). The NPI evidence proves it was the Marx/BCG entities — all new NPI records were created August 6-7, 2019, just weeks before Diversicare's August 30 close. Whether Omega sold the real estate to Marx or retained it as REIT landlord with Marx as tenant is not confirmed in public sources. The per-facility PropCo LLC naming pattern (e.g., "Howard Creek Road SNF Realty LLC") suggests Marx may have purchased the real estate.

### DB Impact — Entity Fragmentation

The DB currently has 4 names for one corporate family:

| Current DB Name | Rows | States | Source of Name |
|---|---|---|---|
| MAJESTIC CARE | 53 | IN (19 SNF + 7 ALF), KY (2 SNF + 7 ALF), OH (15), MI (4), FL (1) | CMS chain (IN/OH/MI) + NIC MAP operator (ALFs) |
| DAVID MARX | 8 | KY (8 SNF) | CMS Chain ID 179 (individual owner name) |
| MAJESTIC MANAGEMENT, LLC | 2 | IN (2 ALF — Carmel, Crown Point) | NIC MAP operator variant |
| MAJESTIC HEIGHTS ASSISTED LIVING | 2 | WI (2 ALF — Hartford) | **NOT CONNECTED.** Independent CBRF owned by Lori Ball and Margo Pritzlaff (local RN sisters). Coincidental name. Do not recode. |

The KY split is the most significant fragmentation: 9 KY rows coded MAJESTIC CARE (7 ALFs + 2 SNFs) alongside 8 KY rows coded DAVID MARX (SNFs). Same operator, same campuses in several cities (Ashland, Sandy Hook, Wurtland, Louisville), split by data source.

**Proposed recode (63 rows):**
- MAJESTIC CARE (IN/OH/MI/FL) + MAJESTIC MANAGEMENT LLC (IN) → `MAJESTIC / MAJESTIC CARE` (48 rows)
- MAJESTIC CARE (KY) + DAVID MARX (KY) → `MAJESTIC / BLUEGRASS CONSULTING GROUP` (17 rows — all 17 served)
- MAJESTIC HEIGHTS ASSISTED LIVING (WI) → no change (2 rows, unrelated)

### Risk Factors

- **Majestic Care of Fairfield (OH):** 3+ active wrongful death lawsuits alleging understaffing. 6 written deficiencies for actual harm (June 2019-Jan 2023). Worst CMS ratings for Overall, Health Inspection, and Staffing.
- **Elliott Nursing (Sandy Hook, KY):** CMS 1-star overall (vs KY avg 2.96, national avg 3.32). $35,695 in fines. Serious deficiency April 2024.
- **David Marx chain aggregate (ProPublica):** Average 1.8 serious deficiencies per home (vs national 0.7). Average nurse staffing 3.3 hrs/resident/day (vs national 3.9). Average turnover 51.1% (vs national 46.4%). 4 facilities with possible abuse per CMS.
- **West Virginia acquisition scrutiny:** WV Senate president raised concerns about employee pensions. A WV senator filed suit against Governor Morrisey over the sale. Communication failures during the process questioned.

### Majestic Heights Assisted Living — NOT Connected

Two ALFs in Hartford, WI (rows 23057-23058) coded MAJESTIC HEIGHTS ASSISTED LIVING. These are small CBRFs (26 beds each) owned by Lori Ball, RN and Margo Pritzlaff, RN (sisters). Independent, locally owned. Website: majesticheights.info. No affiliation with Majestic Care, MDG, or Bedrock Healthcare. Coincidental "Majestic" name. **Do not recode.**

### Sources (with URLs)

| Source | URL | What It Shows |
|---|---|---|
| McKnight's LTC News | mcknights.com — "Majestic Care enters WV" | "Through its subsidiaries, Majestic Care and Bluegrass Consulting Group, [MDG] owns 55 properties" |
| Mountain State Spotlight | mountainstatespotlight.org/2025/09/07/majestic-ceo-qa/ | Pruitt confirms "Majestic Care is a subsidiary of Marx Development Group" |
| Owensboro Times | owensborotimes.com — "Bluegrass Consulting Group acquires Wellington Parc" (Sep 2025) | BCG is "a Majestic Management company," Pruitt = "CEO of Majestic Management" |
| American Healthcare Leader | americanhealthcareleader.com/2025/margaret-chamberlain-majestic-care/ | Chamberlain = General Counsel of both Majestic Care and BCG |
| SNN — Majestic Growth 2021 | skillednursingnews.com/2021/07/majestic-continues-rapid-growth/ | David Marx identified as purchaser |
| SNN — CEO Transition 2023 | skillednursingnews.com/2023/05/majestic-care-names-new-ceo/ | McGuinness to Pruitt |
| SNN — Diversicare KY Exit | skillednursingnews.com/2019/05/diversicare-to-exit-kentucky/ | 10 SNFs, ~885 beds, Omega selects replacement |
| SNN — Diversicare KY Completion | skillednursingnews.com/2019/09/diversicare-completes-kentucky-exit/ | Transfer completed Aug 30, 2019 |
| SNN Dealbook Jan 2025 | skillednursingnews.com/2025/01/ | "Majestic Management added six Ohio facilities" |
| NIC Spring Conference 2026 | springconference.nic.org/speakers/bernie-mcguinness/ | McGuinness = co-founder of both Majestic Care and BCG |
| David Marx bio | ny-eb5.com/our-team/david-e-marx/ | MDG portfolio: 4M+ sqft, 5,000+ beds, EB-5 center |
| ProPublica — David Marx chain | projects.propublica.org/nursing-homes/affiliate/a-179 | 46 facilities, quality metrics, staffing data |
| NursingHomeReport.org — David Marx | nursinghomereport.org/ownername-david-marx/ | Full 46-facility roster by state |
| NursingHomeReport.org — BCG | nursinghomereport.org/ownername-bluegrass-consulting-group-llc/ | 9 KY facilities with operational/managerial control |
| Indiana SOS — BCG LLC | indiana-company.com/co/bluegrass-consulting-group-llc | Filed Jul 25, 2019. RA: Corporation Service Company. Office: 17437 Carey Rd, Westfield IN |
| Indiana SOS — BCG Holdings | city-data.com — BCG Holdings LLC 201907251336888 | Same day filing. Office: 777 E Main, Westfield IN (= Majestic HQ). CEO: McGuinness |
| Elliott NR Privacy Notice | elliottnr.com/notice-of-privacy-practices/ | Compliance hyperlink leaks to majesticcare.com |
| Elliott NR Website | elliottnr.com | CMO = Dr. Robert Russell (same as Majestic Care CMO) |
| Wellington Parc Website | wellingtonparcnr.com/wellington-parc/ | Schema markup references "Elliott Nursing and Rehabilitation" — cloned template |
| Majestic Care About Us | majesticcare.com/about-us/ | Leadership team, no KY references except Pruitt KHCA membership |
| Majestic Care Locations | majesticcare.com/location/ | Meta: "fifteen locations throughout Indiana and Ohio" — no KY, MI, WV in tagline |
| FlippingBook | user-jbdbkvi.cld.bz/Majestic-Care-and-Bluegrass-Consulting-Group | Joint corporate publication (30 pages, JS-rendered) |
| Majestic Heights (unrelated) | majesticheights.info | Independent Hartford WI CBRF, Lori Ball + Margo Pritzlaff RNs |

**Discovered during:** Verification Report V3, Facility 14 (Elliott Nursing) two-pass investigation, 2026-04-03
**Confidence:** HIGH — multiple public sources confirm MDG as parent, Majestic Management as operating umbrella, Majestic Care and BCG as sister brands

---

### PUTNAM COUNTY HOSPITAL — Multi-Operator Owner (Not an Operator)
**Type:** Nonprofit county hospital (Government - Hospital district)
**HQ:** 1542 S Bloomington St, Greencastle, IN 46135
**CEO:** Dennis Weatherford (since 2000)
**CMS ownership:** 100% direct owner of 16+ Indiana SNFs (no chain ID registered)

#### Critical Finding (2026-04-04)
Putnam County Hospital is a **legal owner, not an operator.** It owns the buildings and contracts different management companies to operate them. Prior research (V25.6 punchlist #23) incorrectly assumed all 19 DB facilities should be consolidated under one name. Per-facility ProPublica verification revealed **at least 8 different managing entities** across the portfolio.

**Additionally:** Paoli Health & Living Community (CCN 155333, 559 W Longest St, Paoli IN) was coded to PUTNAM COUNTY HOSPITAL in the DB but is actually owned by **Riverview Hospital** and managed by **Cardon Management Company LLC.** This is a misattribution — Paoli has no ownership connection to Putnam County Hospital.

#### Per-Facility Managing Entity Verification

| Facility | City | CCN | Managing Entity (ProPublica) | Operator Brand | Since |
|---|---|---|---|---|---|
| Richland Bean-Blossom HCC | Ellettsville | 155523 | HHSS Management LLC | HutsonWood | Apr 2020 |
| Hutsonwood at Brazil (Towne Park) | Brazil | TBD | (likely HHSS — branded HutsonWood) | HutsonWood | Jun 2015 |
| Mill Pond Health Campus | Greencastle | 155736 | Trilogy Healthcare Ops of Greencastle LLC | Trilogy Health Services | May 2015 |
| Cobblestone Crossings HC | Terre Haute | 155772 | Trilogy Healthcare of Vigo LLC | Trilogy Health Services | Nov 2014 |
| Harrison's Crossing HC | Terre Haute | 155830 | RHS Partners of Terre Haute LLC | **Trilogy Health Services** (website: trilogyhs.com, © 2026 Trilogy Health Services LLC. RHS Partners is a facility-level LLC.) | Jul 2015 |
| Northview Health & Living | Anderson | 155718 | Community LTC Inc / Health Mgmt Advisors Inc | Essential Senior H&L | Oct 2018 |
| Elwood Health & Living | Elwood | 155522 | Community LTC Inc / Health Mgmt Advisors Inc | Essential Senior H&L | Oct 2018 |
| Summit Health & Living | Summitville | 155839 | Community LTC Inc / Health Mgmt Advisors Inc | Essential Senior H&L | Oct 2018 |
| Century Villa Health Care | Greentown | 155510 | Medical Rehabilitation Centers LLC | **Exceptional Living Centers** (website: exceptionallivingcenters.com, HQ Lexington KY, 12 facilities KY/IN/OH/TN. MRC is a facility-level LLC.) | Feb 2018 |
| Providence Health Care Ctr | St Mary of the Woods | 155802 | Providence Health Care Inc | **Sisters of Providence of Saint Mary-of-the-Woods** (website: phcwoods.com, nonprofit, owner-operated, no third-party mgmt. "Sponsored by the Sisters of Providence.") | Dec 2013 |
| Owen Valley Rehab & HC | Spencer | 155661 | Clayshire LLC / LT Care Acquisition Corp | Clayshire/LT Care | Sep 2022 |
| Waters of Princeton | Princeton | 155275 | County Hospital Manager LLC | **Infinity Healthcare Consulting** (ihconsulting.com client list confirms. County Hospital Manager LLC is legal entity; IHC is the operator.) | Sep 2012 |
| Waters of Martinsville | Martinsville | 155183 | County Hospital Manager LLC | **Infinity Healthcare Consulting** (ihconsulting.com client list confirms) | May 2014 |
| Waters of Greencastle | Greencastle | 155202 | County Hospital Manager LLC | **Infinity Healthcare Consulting** (ihconsulting.com client list confirms) | May 2014 |
| Waters of Huntingburg | Huntingburg | 155217 | The Waters of Huntingburg II LLC / Infinity HC | **Infinity Healthcare Consulting** (ihconsulting.com client list confirms) | Nov 2020 |
| Waters of Scottsburg | Scottsburg | 155494 | Waters of Scottsburg II LLC | **Infinity Healthcare Consulting** (ihconsulting.com client list confirms) | Nov 2020 |

**NOT Putnam County Hospital:**
| Facility | City | CCN | Actual Owner | Managing Entity |
|---|---|---|---|---|
| Paoli Health & Living Community | Paoli | 155333 | Riverview Hospital (100%) | Cardon Management Company LLC |

#### DB Coding Implications

Per the operator attribution rule and owner-vs-management-company guidance: code the management company (the entity making clinical/business decisions), not Putnam County Hospital (the legal owner that contracts management companies).

- Trilogy facilities (Mill Pond, Cobblestone Crossings, Harrison's Crossing) → TRILOGY HEALTH SERVICES (already scored T1 MUO — **3 facilities, not 2.** Harrison's Crossing confirmed via trilogyhs.com; RHS Partners is a facility-level LLC)
- HutsonWood facilities (Richland Bean-Blossom, Towne Park/Brazil) → HUTSONWOOD (or HHSS MANAGEMENT)
- Essential Senior H&L facilities (Northview, Elwood, Summit) → ESSENTIAL SENIOR HEALTH AND LIVING (or COMMUNITY LTC)
- Exceptional Living Centers (Century Villa) → EXCEPTIONAL LIVING CENTERS (website: exceptionallivingcenters.com, HQ Lexington KY, 12 facilities KY/IN/OH/TN. MRC is a facility-level LLC)
- Sisters of Providence (Providence Health Care Ctr) → SISTERS OF PROVIDENCE (nonprofit, owner-operated per phcwoods.com, no third-party management)
- Infinity Healthcare Consulting (Waters of Princeton, Martinsville, Greencastle, Huntingburg, Scottsburg) → INFINITY HEALTHCARE CONSULTING (ihconsulting.com — ~85 SNFs across IL/IN/KY/MI/OK/TN. "County Hospital Manager LLC" is the legal entity but IHC is the operator per their own client facility list. All 5 "Waters of" PCH facilities are IHC-operated.)
- Clayshire/LT Care (Owen Valley) → website (owenvalleyhcr.com) shows independent branding, no parent company visible. ProPublica shows Clayshire LLC since Jan 2023. Needs further research — Clayshire may be the operator or another facility-level LLC.
- Paoli → recode from PUTNAM COUNTY HOSPITAL to CARDON (or RIVERVIEW HOSPITAL — needs operator-vs-owner determination)

#### Ownership Table (Entity Level)

| Layer | What It Is |
|---|---|
| **Legal Owner** | Putnam County Hospital (nonprofit county hospital) |
| **PropCo** | N/A (hospital owns directly, no PropCo/REIT structure) |
| **Management Companies** | Infinity Healthcare Consulting (5 fac — all "Waters of" brand), Trilogy Health Services (3 fac), Essential Senior H&L/Community LTC (3 fac), HutsonWood/HHSS (2 fac), Exceptional Living Centers/MRC (1 fac), Sisters of Providence (1 fac, nonprofit owner-operated), Clayshire LLC (1 fac, needs verification) |
| **Operator brands** | Vary by management company — see per-facility table |

**Key lesson:** An owner is not an operator. One owner can contract multiple management companies. "Consolidate all facilities under the owner's name" is the wrong approach when the owner delegates operations. Always verify managing entity per-facility.

**Sources:**
- ProPublica Nursing Home Inspect: CCNs 155523, 155736, 155772, 155830, 155718, 155522, 155839, 155510, 155802, 155661, 155275, 155183, 155217, 155494, 155202, 155333
- HutsonWood website: hutsonwood.org (senior living page lists only 2 IN communities)
- Putnam County Hospital website: pchosp.org (no mention of SNF operations)
- Essential Senior Health & Living website: essentialseniorhealthandliving.org

**Website verification (2026-04-04):**
- trilogyhs.com: Harrison's Crossing listed as Trilogy facility (© 2026 Trilogy Health Services LLC). RHS Partners is facility-level LLC. 3 PCH facilities are Trilogy, not 2.
- exceptionallivingcenters.com: Century Villa branded as Exceptional Living Centers (HQ Lexington KY, 12 facilities KY/IN/OH/TN). MRC is facility-level LLC. Also shows Century Fields Retirement Community in same town — possible campus.
- phcwoods.com: Providence HC operated by Sisters of Providence of Saint Mary-of-the-Woods (nonprofit, no third-party mgmt, schema markup confirms sponsorship).
- hutsonwood.org: Only 2 IN senior living communities listed (Richland Bean-Blossom + Towne Park). Not 19.
- pchosp.org: No mention of SNF operations. Hospital only.
- essentialseniorhealthandliving.org: Northview, Elwood, Summit listed. Community LTC Inc is the ProPublica managing entity.

**Discovered during:** Comprehensive scrub procedure test, punchlist #23 verification, 2026-04-04

---

### CARLYLE SENIOR CARE
**CMS Chain:** 599 (8 facilities, all SC)
**Legal Owner:** New Day Health Ventures LLC (100%) — Richard Cranford (67%), Braxton W. Barnette (33%)
**Brand:** Carlyle Senior Care of [City]
**V23 Tier:** T4 (7 campuses V25.5, SC only, 0 served)

#### McCoy Memorial Resolution (Punchlist #24, 2026-04-04)
McCoy Memorial Nursing Center (CCN 425174, Bishopville SC) was coded in the Forward Universe as CONCIERGE HEALTHCARE. GLR also carries "Concierge Healthcare."

**"Concierge Healthcare" is a phantom corporate name.** Per-source verification:
- CMS: Chain = Carlyle Senior Care (599). Legal business name = New Day Health Ventures LLC. No "Concierge" anywhere.
- ProPublica: Owner = New Day Health Ventures LLC (100%). No managing entity named Concierge.
- SC State Registry (DHEC License NCF-0986): Admissions email = mboykin@carlyleseniorcare.com. Facility also known as "Carlyle Senior Care of Bishopville."
- Web: "Concierge Healthcare" returns zero results connected to Cranford, Barnette, New Day Health, or any SC nursing facility. Does not exist.

**Origin of phantom name unknown.** Possibly a prior management company name that persisted in the GLR after the relationship ended, or a data entry error. No evidence it was ever a real operator.

**Action:** Recode CONCIERGE HEALTHCARE → CARLYLE SENIOR CARE on the McCoy Memorial row. Flag GLR correction needed (internal communication trigger).

**Ownership table:**
| Layer | Entity |
|---|---|
| Legal Owner | New Day Health Ventures LLC (Cranford 67% / Barnette 33%) |
| PropCo | N/A (same entity owns and operates) |
| Management Company | Carlyle Senior Care (operating brand) |
| Sub-brand | N/A |
| Operator / Chain | CARLYLE SENIOR CARE (CMS Chain 599) |

**Sources:**
- ProPublica: projects.propublica.org/nursing-homes/homes/h-425174
- ProPublica (Blackville): projects.propublica.org/nursing-homes/homes/h-425319
- ProPublica (Fork): projects.propublica.org/nursing-homes/homes/h-425093
- SC State Registry: nfbl.sc.gov/FacilityInformation.php?FacID=174
- Carlyle websites: carlyleflorence.com, carlylekingstree.com (Wix-built, branded)

**Discovered during:** Comprehensive scrub procedure test, punchlist #24 verification, 2026-04-04

---

### SEVEN ACRES SENIOR LIVING AT CLIFTON — Independent (Klingerman Family Investment)
**CCN:** 366316
**Address:** 476 Riddle Road, Cincinnati, OH 45220
**Type:** For-profit LLC, 58 SNF beds + 35 IL apartments
**CMS Chain:** None
**V25.6 DB:** Corporate_Name = null, Ownership_Type = Independent

#### Ownership (ProPublica, since March 2023)
- **Direct owner:** Lackawanna Healthcare Associates LLC (100%)
- **Indirect owner:** David W. Klingerman Jr. (10%)
- **Managing entity:** Not disclosed in ProPublica
- **Mortgage:** Jersey Shore State Bank

#### History
Formerly St. Paul's Archbishop Leibold Home for the Aged, operated by the Little Sisters of the Poor (Catholic religious order). Purchased March 2023 by Lackawanna Healthcare Associates LLC. Rebranded as Seven Acres Senior Living.

#### Klingerman Family / Liberty Group Connection
David W. Klingerman Jr. is COO of The Liberty Group and Managing Partner of Liberty Healthcare Management (LHM). The Liberty Group is a PE holding/investment company founded 2002 by Daniel Klingerman (Bloomsburg PA), $500M+ assets, 6,000+ workers, 50+ subsidiary companies. LHM manages 9 SNF locations in Northeastern/Central PA + Susquehanna Valley, plus consulting/management for other facilities. Predecessor entity: JDK Management Company (founded 1982, nursing homes + restaurants in PA/OH/NY/WV/FL/NJ/IN).

Lackawanna Healthcare Associates LLC is a Klingerman family ownership vehicle also used for Marywood Heights (Scranton PA, 72 beds), where Liberty Healthcare Mgt LLC is explicitly listed as managing entity in ProPublica since Dec 2019.

**However:** Liberty Healthcare Management does NOT list Seven Acres, Cincinnati, or any Ohio location on their corporate site (thelibertygroup.net). Their 9 facilities are exclusively in PA. No public source connects Liberty Group operations to Seven Acres. This appears to be a personal/family investment by the Klingermans in a facility that operates independently, not a Liberty Group-managed property.

#### Prior CMS Names (stale)
- CMS previously showed "Hamilton Healthcare Associates LLC" — not current. ProPublica (Mar 2023) shows Lackawanna, not Hamilton.
- NIC MAP showed "Hamilton Healthcare Associate LLC" — self-referencing, also stale.

#### DB Coding Decision
**Code: INDEPENDENT.** Seven Acres is a single-facility operation with no chain affiliation, no disclosed management company, and no public connection to Liberty Group operations. The Klingerman/Lackawanna ownership is documented here for future reference — if Liberty Group expands into Ohio or if additional Klingerman-owned facilities surface, reassess.

Do NOT code as "Lackawanna Healthcare Associates LLC" (legal wrapper, not an operator identity) or "Hamilton Healthcare Associates LLC" (stale CMS data) or "Liberty Healthcare Management" (not confirmed as operator here).

**Sources:**
- ProPublica: projects.propublica.org/nursing-homes/homes/h-366316
- ProPublica (Marywood Heights): projects.propublica.org/nursing-homes/homes/h-395625
- Seven Acres website: sevenacresseniorliving.org (independent branding, no parent company)
- The Liberty Group: thelibertygroup.net/market/healthcare/ (9 PA locations, no OH)
- Commonwealth University profile of Daniel Klingerman
- PA Business Central profile of Daniel Klingerman
- NPI: npiprofile.com/npi/1386292035 (Lackawanna Healthcare Associates, Danville PA, David Klingerman authorized official)

**Discovered during:** Comprehensive scrub procedure test, punchlist #25 verification, 2026-04-04

---

## TLC Management (Tender Loving Care Management Inc)

**Also known as:** TLC Management, Tender Loving Care Management INC, Tlc Management (CMS chain)
**Headquarters:** 1800 N. Wabash Avenue, Marion, Indiana 46952
**Incorporated:** 1987
**Type:** Private management company — operates SNFs, ALFs, and independent retirement communities
**Website:** tlcmgmt.com

#### Portfolio (per tlcmgmt.com, checked 2026-04-05)
~20+ communities across IN, OH, FL:
- **Indiana:** Blue Heron Senior Living, Oak Hill Senior Living, Addison Pointe H&R, Albany Pointe H&R, Ashton Creek H&R, Avon H&R, Bethel Pointe H&R, Bridgewater Park, Colonial Oaks H&R + Retirement Community, Creekside H&R, Englewood H&R, **Hamilton Pointe**, Homeview H&R, Mason H&R, Ossian H&R, Parker H&R, Rolling Meadows H&R, Wesleyan H&R
- **Ohio:** Washington Court House (The Village at Vienna Square)
- **Florida:** Winter Haven, Copper Knoll H&R

#### Ownership Structure — Hamilton Pointe (3800 Eli Pl, Newburgh IN, CCN 155803)

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | ProPublica (100%, since Aug 2014) | Riverview Hospital (county government hospital) |
| **PropCo** | — | N/A |
| **Management Company** | ProPublica managing entity (since Aug 2014), CMS chain, tlcmgmt.com | Tender Loving Care Management Inc |
| **Management Sub-brand** | — | N/A |
| **Operator** | CMS chain + ProPublica + website (HIGH confidence) | **TLC MANAGEMENT** |

**DB impact:** 3 rows (AL, MC, SNF) at Hamilton Pointe coded RIVERVIEW HOSPITAL → should be TLC MANAGEMENT. Riverview Hospital is the legal owner (county government hospital), not the operator.

**GLR discrepancy:** AL and SNF carry Parent Company = RIVERVIEW HOSPITAL (wrong — owner, not operator). MC carries Parent Company = TLC Management (correct). Corrections logged to glr_change_log.csv.

**Corporate officers (ProPublica):** Jayna Friend (since Jun 2021), Seth Warren (since Apr 2016). W2 managing employees: Tamara Bledsoe (since Aug 2014), Jayna Friend, Seth Warren.

#### Sources
- ProPublica: projects.propublica.org/nursing-homes/homes/h-155803
- Operator website: tlcmgmt.com (portfolio page lists Hamilton Pointe)
- CMS chain affiliation: TLC Management
- GLR Facility Dump 2026-03-13 (Parent Company field)

**Discovered during:** ALF dedup cluster review, Cluster 1, punchlist item #1, 2026-04-05

---

## Lutheran Life Villages (Lutheran Homes, INC.)

**Also known as:** Lutheran Homes INC (ProPublica legal name), LLV
**Headquarters:** NE Indiana (Fort Wayne area)
**Type:** Nonprofit, faith-based senior living organization
**Website:** lutheranlifevillages.org

#### Ownership Structure — South Anthony Campus (6723 S Anthony Blvd, Fort Wayne IN, CCN 155586)

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | ProPublica (100%, since Jul 2012) | Adams County Memorial Hospital (nonprofit) |
| **PropCo** | — | N/A |
| **Management Company** | ProPublica managing entity (since Jul 2012) | Lutheran Homes INC |
| **Management Sub-brand** | — | N/A |
| **Operator** | FU + GLR + website (HIGH confidence) | **LUTHERAN LIFE VILLAGES** |

Other ProPublica managing entities at this CCN: Healthcare Therapy Services INC (therapy vendor, since Jul 2012), Forvis Mazars LLP (accounting firm, since Jun 2023). Neither are operators.

**Corporate officers (ProPublica):** Russell Flueckiger (since Jan 2006), Larry Macklin (since Jan 2008), Scott Smith (since Jan 2020), Kyle Sprunger (since Jan 2018), Dane Wheeler (since Sep 2009).

#### Portfolio (per lutheranlifevillages.org, checked 2026-04-05)
All NE Indiana:
- The Village at Anthony Boulevard (6701/6723 S Anthony Blvd, Fort Wayne) — SNF + ALF + Homes/Clinic
- The Village at Pine Valley (Coldwater Rd, Fort Wayne) — SNF + ALF
- The Village at Pine Valley Assisted Living (11430 Coldwater Rd, Fort Wayne) — ALF
- The Village at Kendallville (351 N Allen Chapel Rd, Kendallville) — SNF
- Piper Trail (Fort Wayne)
- The Village at Inverness (Fort Wayne)
- The Apartments at Anthony Boulevard (Fort Wayne)

**DB impact:** 9 rows under LUTHERAN LIFE VILLAGES. Attribution confirmed correct — no recode needed.

**Signal:** Wittenberg Village (1200 Luther Dr, Crown Point IN, 122 beds, unserved, row 20162) is coded LUTHERAN LIFE VILLAGES but Crown Point is NOT listed on lutheranlifevillages.org. Possible misattribution — needs investigation.

**Signal:** Row 5173 (THE VILLAGE AT ANTHONY BOULEVARD, 6701 S Anthony Blvd, 107 beds, unserved) is at same campus as Cluster 2 but different street number. ProPublica address = 6701. GPS proximity check needed.

#### Sources
- ProPublica: projects.propublica.org/nursing-homes/homes/h-155586
- Operator website: lutheranlifevillages.org (portfolio page)
- GLR Facility Dump 2026-03-13 (Parent Company = Lutheran Life Villages)
- Forward Universe V25.7 (9 rows)

**Discovered during:** ALF dedup cluster review, Cluster 2, punchlist item #1, 2026-04-05

---

## Carmelite System (The Carmelite System INC)

**Also known as:** The Carmelite System INC (ProPublica legal name)
**Headquarters:** Germantown, NY (Carmelite Sisters Motherhouse: 600 Woods Rd, Germantown NY 12526)
**Type:** Nonprofit management arm of The Carmelite Sisters For The Aged And Infirm (Catholic religious order, founded 1929)
**Website:** carmelitesystem.org (DOWN as of 2026-04-05, ECONNREFUSED); carmelmanor.com (Fort Thomas facility)

#### Ownership Structure — Carmel Manor (100 Carmel Manor Rd, Fort Thomas KY, CCN 185208)

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | ProPublica (100%, since Jan 1966) | The Carmelite Sisters For The Aged And Infirm (religious nonprofit) |
| **PropCo** | — | N/A |
| **Management Company** | ProPublica managing entity (since Jan 2013) | The Carmelite System INC |
| **Management Sub-brand** | — | N/A |
| **Operator** | FU + GLR + ProPublica (HIGH confidence) | **CARMELITE SYSTEM** |

Other ProPublica managing entities: Anthony Ughetti (W2 employee, since Mar 2023).

**Corporate officers (ProPublica):** Jeffrey Brauley (since Apr 2018), Margaret Haley (since Apr 2021), Rose Marie Kasper (since May 2023), Catherine Millette (since Apr 2018), Theresa Pfeffer (since Oct 2023). 12 corporate directors.

#### National Portfolio (per Forward Universe V25.7, 20 rows)
FL (1), IA (1), IL (1), KY (3 — Carmel Manor campus), MA (3), MO (1), NY (2), OH (4), PA (2), WI (1).

Only KY and OH are in the 6-state operational footprint. OH has 4 rows in Columbus (Villas at Saint Therese, Mother Angeline McCrory Manor campus) — signal: 2 ALF rows at 25 Noe Bixby Rd may be a dedup pair.

**DB impact:** Attribution CARMELITE SYSTEM confirmed correct for KY campus. Row 5686 (CARMEL MANOR, SNF) deleted as duplicate — does not correspond to GLR entry. Row 5714 retyped ALF→SNF, beds 87→95. Row 5713 (AL) kept.

**Signal:** carmelmanor.com logo file references "stpatricks-home-logo" — shared template/branding with St. Patrick's Residence (Naperville IL) and St. Patrick's Manor (Framingham MA), confirming centralized Carmelite System management.

#### Sources
- ProPublica: projects.propublica.org/nursing-homes/homes/h-185208
- Facility website: carmelmanor.com
- Carmelite Sisters website: carmelitesisters.com (references "The Carmelite System" link)
- GLR Facility Dump 2026-03-13 (Parent Company = Carmelite System)
- Forward Universe V25.7 (20 rows)

**Discovered during:** ALF dedup cluster review, Cluster 3, punchlist item #1, 2026-04-05

---

## Shady Lawn (Cynthiana KY) — INDEPENDENT

**Facility:** Shady Lawn, 108 S Miller St, Cynthiana KY 41031
**Type:** Personal Care Home (ALF), 75 beds
**KY CHFS License:** 100170PC
**Licensee:** SHADY LAWN I LLC
**Administrator:** Kim Perez

#### Ownership Structure

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | KY CHFS (License 100170PC) | Shady Lawn I LLC |
| **PropCo** | NIC MAP (Owner col 18) | Shady Lawn II LLC |
| **Management Company** | NIC MAP (Operator col 41) | unknown |
| **Management Sub-brand** | — | N/A |
| **Operator** | All sources evaluated → INDEPENDENT | No corporate operator identified |

**LLC variant inventory:** DB carried "SHADY LAWN, LLC" / GLR carries "SHADY LAWN LLC" / NIC MAP Owner = "Shady Lawn II LLC" / KY CHFS License = "SHADY LAWN I LLC". Four different LLC name variants across sources — none is a corporate operator. All are facility-level legal entities.

**Kim Perez connection:** Administrator of both Shady Lawn (100170PC) and Parkside Manor I LLC (317 Oddville Ave, Cynthiana KY, License 100168PC). Same person, same town. May be a small local operator running 2 facilities through separate LLCs. No corporate identity beyond the facility-level LLCs.

**DB impact:** Recode SHADY LAWN, LLC → INDEPENDENT. Per Corporate Name Standardization rule #6: single-facility LLC with no public presence, no website, no CMS chain, NIC MAP operator = unknown. Ownership documented here for future reference.

#### Sources
- KY CHFS Personal Care Home Directory (Feb 2026 PDF): License 100170PC, licensee Shady Lawn I LLC, administrator Kim Perez
- NIC MAP (Nov 2025 export): Owner = Shady Lawn II LLC, Operator = unknown
- GLR Facility Dump 2026-03-13: Parent Company = SHADY LAWN LLC
- Web search (2026-04-05): No dedicated website. shadylawnliving.com ECONNREFUSED. A Place for Mom, Seniorly, CareListings — no operator info.
- Forward Universe V25.7

**Discovered during:** ALF dedup cluster review, Cluster 4, punchlist item #1, 2026-04-05

---

## Dominion Senior Living (DSL)

**Parent company:** Dominion (dominion.us) — Knoxville TN-based real estate development, acquisition, and management company. $1B+ properties under management and development. 4 brands: Dominion Development Group (DDG), Dominion Management Group (DMG), Dominion Senior Living (DSL), DGA Residential.
**Leadership:** Mark Taylor (CEO), Peter Hall (President), Sean Chalmers (COO), Jordana Nelson (VP Development), Natalie Cudzilo (VP Finance), Dale Torry (VP Property Mgmt), Stephanie Haynes (VP Property Mgmt), Craig Cobb (VP Affordable Housing).
**Type:** For-profit, private. Southeastern US focus (TN, AL, SC, KY, NC).
**Website:** dominionseniorliving.com (facility pages — returned 401 for Frankfort 2026-04-05, may be transitioning to dominion.us), dominion.us (parent company, active).

#### DSL Portfolio (per dominion.us/our-brands, checked 2026-04-05)
1,175 units across 17 communities. Two sub-brands: DSL (assisted living + memory care) and Everlan (premium amenities).

| Community | City | State | DB Row | DB Match? |
|---|---|---|---|---|
| DSL Anderson | Anderson | SC | 17820 | Yes |
| DSL Athens | Athens | TN | 17821 | Yes (outside footprint) |
| DSL Bristol | Bristol | TN | 17822 | Yes (outside footprint) |
| DSL Crossville | Crossville | TN | 17823 | Yes (outside footprint) |
| DSL Florence | Florence | KY | — | No DB match found under Dominion — investigate |
| DSL Frankfort | Frankfort | KY | 5757 | Yes — **Cluster 5** |
| DSL Hixson | Hixson | TN | 17816 | Yes (outside footprint, named "Dominion of Hixson") |
| DSL Johnson City | Johnson City | TN | 17824 | Yes (outside footprint) |
| DSL Louisville | Louisville | KY | 5754 | Yes (600 Hunting Rd) |
| DSL Richmond | Richmond | KY | 5755 | Yes |
| DSL Sevierville | Sevierville | TN | 17819 | Yes (outside footprint) |
| DSL at Patrick Square | Clemson | SC | 17818 | Yes |
| Everlan of Clemson | Clemson | SC | — | Not in DB under Dominion — may be new or under different name |
| Everlan of Hixson | Hixson | TN | — | Not in DB under Dominion (outside footprint) |
| Everlan of Johnson City | Johnson City | TN | — | Not in DB under Dominion (outside footprint) |
| Everlan of Louisville | Louisville | KY | 17902 | Yes (5900 Hunting Rd, named "EVERLAN OF LOUISVILLE") |
| Clover Hill Senior Living | (location TBD) | TBD | — | Not identified |

**DB impact:** 15 rows coded DOMINION SENIOR LIVING in DB. 6 in KY (footprint), 2 in SC (footprint), 7 in TN (outside footprint). Attribution confirmed correct for DSL Frankfort (Cluster 5). Other facilities not individually verified in this session.

**Note on Louisville KY addresses:** DB has 3 rows in Louisville under Dominion at 3 different addresses: 600 Hunting Rd (DSL Louisville, row 5754), 5900 Hunting Rd (Everlan of Louisville, row 17902), 6000 Hunting Rd (DSL of Louisville, row 17825). Dominion's website lists DSL Louisville and Everlan of Louisville. The 3 addresses may be campus variants or distinct communities — needs investigation.

#### The Spring Arbor / Foundry Commercial / Allegro Living Relationship

**This facility (DSL Frankfort) appears on allegroliving.com as "Spring Arbor of Frankfort" operated by Allegro Senior Living.** Investigation revealed this is a **property brand layer**, not an operator change:

**Timeline:**
- **May 2022:** Foundry Commercial (Jacksonville FL, real estate investor) acquired 24 Spring Arbor Senior Living communities in NC, VA, MD as a JV with an institutional equity partner. Foundry assumed operational responsibility through Spring Arbor Senior Living, which they also acquired. Capitalization: $350M+ across 29 total senior housing communities since 2020.
- **Aug 2023:** Foundry added 16 communities to the Spring Arbor Management platform (Senior Housing News, Aug 24 2023). Details of which communities were added not confirmed — may include former Dominion-branded buildings where Foundry acquired the property and applied the Spring Arbor brand.
- **Mar 4, 2025:** Spring Arbor Management and Allegro Management Company merged to form **Allegro Living** (holding company). Combined: 53 communities, 4,500+ units, ~4,000 associates, 13 states. Communities continue under legacy brands (Allegro, Alto, RoseWood Village, Spring Arbor). Leadership: Douglas Schiffer (President & CEO, Allegro Living), Kevin Maddron (President of Healthcare Services, Foundry Commercial). Allegro backed by Love Companies (St. Louis). Advisor: Lisa Widmier, Vant.Age Pointe Capital Management.

**What this means for DSL Frankfort:** Foundry Commercial likely owns the real estate (PropCo layer) and applies the "Spring Arbor" property brand. Dominion Senior Living manages day-to-day operations (Operator layer). allegroliving.com listing reflects the property owner's brand, not the operator. dominion.us/our-brands confirms DSL Frankfort as an active Dominion community as of 2026-04-05.

**The Spring Arbor brand has three distinct contexts in our data:**
1. **Spring Arbor Management** (now part of Allegro Living) — operates 11 facilities directly (17 DB rows under SPRING ARBOR MANAGEMENT). These are facilities where Spring Arbor is both the brand AND the operator.
2. **Spring Arbor as property brand under other operators** — buildings branded "Spring Arbor" but operated by Foundry, Wickshire, HHHunt, Allegro, or Dominion. The brand is a real estate asset, not an operator identity. Per MUO Corporate History: "Spring Arbor is a property brand, not always the operating company."
3. **Allegro Living Spring Arbor portfolio** — allegroliving.com lists 9 Spring Arbor communities (Anderson SC, Sevierville TN, Florence KY, Athens TN, Bristol TN, Crossville TN, Maryville TN, Frankfort KY, Richmond KY). 7 of these match DB rows currently coded DOMINION SENIOR LIVING. This overlap requires investigation: does Allegro Living hold the property brand while Dominion operates, or has Allegro Living assumed operations? dominion.us listing of these facilities as active DSL communities supports the former interpretation, but per-facility verification is needed.

**Open question:** The relationship between Dominion (operator) and Foundry/Allegro (property owner/brand) at these 7+ overlapping facilities is not fully resolved. It may be: (a) Foundry owns the buildings and brands them Spring Arbor, Dominion manages operations under contract — similar to a REIT/operator split; or (b) Allegro Living has assumed or is in the process of assuming operations from Dominion. The dominion.us website listing these as active DSL communities suggests (a), but a WJHL article (Johnson City TN) references "Dominion Senior Living and Everlan of Johnson City operating under new names" — which could signal (b) for at least some facilities. Per-facility verification required before any recode.

#### Ownership Structure — DSL Frankfort (122 Leonardwood Dr, Frankfort KY)

| Ownership Layer | Source | Entity |
|---|---|---|
| **Legal Owner** | Unknown — ALF, no CMS/ProPublica | TBD (likely a Foundry Commercial entity or local LLC) |
| **PropCo** | allegroliving.com (inferred) | Foundry Commercial (Spring Arbor brand) |
| **Management Company** | dominion.us/our-brands | Dominion Senior Living |
| **Management Sub-brand** | — | N/A |
| **Operator** | dominion.us + GLR Parent Company (MEDIUM confidence) | **DOMINION SENIOR LIVING** |

**Confidence: MEDIUM.** 2 sources agree on Dominion as operator (dominion.us portfolio page, GLR Parent Company). ALF confidence ceiling applies. Allegro website contradicts — logged as property brand layer, not operator layer. KY CHFS licensing would elevate to HIGH but not yet checked for this specific facility.

#### Sources
- dominion.us/our-brands (checked 2026-04-05): DSL Frankfort listed as active community
- dominionseniorliving.com/frankfort/ (checked 2026-04-05): returned 401
- allegroliving.com/communities (checked 2026-04-05): lists "Spring Arbor of Frankfort" at same address
- allegroliving.com/communities/spring-arbor-frankfort-ky (checked 2026-04-05): operated by Allegro Senior Living, Google Maps reference still says "Dominion Senior Living of Frankfort"
- foundrycommercial.com case study (May 2022 Spring Arbor acquisition)
- foundrycommercial.com press release (Mar 4 2025 Allegro Living merger)
- Senior Housing News (Aug 24 2023): "Foundry Commercial Adds 16 Communities to Growing Spring Arbor Management Platform"
- Senior Housing News (Mar 18 2025): "Allegro, Spring Arbor Bringing Complementary Senior Living Strengths to New Merger"
- McKnight's Senior Living (Mar 2025): "Spring Arbor Senior Living, Allegro Management merge to form Allegro Living"
- GLR Facility Dump 2026-03-13: facility name = "Spring Arbor Assisted Living of Frankfort", Parent Company = "Dominion"
- Forward Universe V25.7: 15 rows under DOMINION SENIOR LIVING

**Discovered during:** ALF dedup cluster review, Cluster 5, punchlist item #1, 2026-04-06
