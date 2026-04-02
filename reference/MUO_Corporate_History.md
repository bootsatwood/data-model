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
Remaining: 1 row PELICAN HEALTH HENDERSON (Camellia Gardens Durham) — pending verification. 2 rows (OH, SC) — pending verification.

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
- **Genesis** (id 16254): 9 campuses KY/NC/VA, 4 served. 7 of 10 facilities flagged "Own Provider Group." Cary lists as "Genesis/Alignmed."
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

**T4 classification review needed:**
- Kissito Healthcare (T4, 12 campuses) — meets gate. Cary notes: "Bought by Utah group; Baroco/Steve meeting Mary Ferrell."
- BHI Senior Living (T4, 9 campuses) — meets gate.

---

## MORNING POINTE SENIOR LIVING

**Canonical DB name:** `MORNING POINTE SENIOR LIVING`
**Parent entity:** Independent Healthcare Properties (IHP), LLC
**Founded:** 1997 by Greg A. Vital and Franklin Farrow, Chattanooga TN
**Footprint:** ~42-43 communities across 5 states (TN ~18, KY 8, GA 2, IN 1, AL 1)
**Business model:** ALF + Lantern memory care. PropCo entities follow "[City] Medical Investors LLC" naming convention (e.g., Owensboro Medical Invtrs LLC, Lexington East Medical Investors LLC, Brentwood Medical Investors LLC).

### Timeline
| Date | Event | Source |
|---|---|---|
| 1997 | Founded by Greg A. Vital and Franklin Farrow in Chattanooga, TN | [Morning Pointe About Us](https://morningpointe.com/about-morning-pointe/) |
| 2024 (Sep) | Acquired Heritage Place (ALF, 66 beds) in Owensboro KY from Encore Communities. $2.5M renovation planned. 39th community overall. | [Owensboro Times](https://www.owensborotimes.com/features/2024/09/heritage-place-acquired-by-morning-pointe-senior-living-company-planning-2-5m-renovation/) |
| 2025 (Aug) | Grand Opening of Morning Pointe of Owensboro (formerly Heritage Place). Deficiency-free KY licensure survey. | [Morning Pointe press release](https://morningpointe.com/press/morning-pointe-senior-living-expands-to-western-kentucky/) |

### DB Notes
- **NIC MAP misattribution:** NIC-A row for Owensboro coded operator as GENESIS. Genesis has zero relationship to this facility. NIC MAP likely inherited stale chain assignment from Heritage Place's Encore Communities period, or a pure data error. PropCo "Owensboro Medical Invtrs LLC" on NIC row correctly maps to IHP/Morning Pointe.
- **Heritage Place → Morning Pointe of Owensboro** rebrand confirmed Sep 2024.
- **Encore Communities** was prior operator of Heritage Place (Pacific Northwest-based, ~43 communities in IL, WI, MN, OH, MI).

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
