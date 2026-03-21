# MUO Corporate History Log

Tracks corporate-level events — mergers, acquisitions, divestitures, rebrands, name changes — for operators in the Combined Database. Entries are added during V23 scoring research, fuzzy match reconciliation (Punchlist #4), and MUO candidate evaluations.

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

### ZANZIPER (Simcha Hyman & Naftali Zanziper)
**V23 Tier:** T2* (Score: 39, proposed)
**Footprint:** 10 states | 115 DB / 200+ public
**Research focus:** **Regulatory and ownership structure deep dive.** CON mapping, regulatory analysis, consolidated facility list. 100% barriered — owns provider group + alliance. $12M+ CMS fines since 2021. The Ivy at Great Falls closure. Opaque layered ownership (Portopiccolo Group / 980 Investments). T5 barrier classification.
**Profile:** `Zanziper_MUO_Profile.md`

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

### Barrier/Strategic Research
- **Pavilion Healthcare** — alliance + 29% own provider group (T5 barrier)
- **Zanziper** — 100% barriered, own provider group + alliance, $12M+ regulatory history, opaque ownership

### RS Reconciliation (March 11, 2026)
Brooke (BD perspective) vs Tom (Sales Success perspective) — 50 entities scored side-by-side. 11 big divergences identified:
- Otterbein (delta -4), Arbors of Ohio (-3), Pavilion (-3), Saber (-3)
- Divergences treated as signals, not errors — BD sees growth potential, SS sees operational depth

### V20 → V23 Movers Analysis
10 upgrades, 15 downgrades tracked across scoring versions. 3 root causes identified: RS methodology change (dual-scorer), IR recalculation (service flag audit), and ER campus count corrections.
