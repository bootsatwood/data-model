# Comprehensive Scrub Procedure

> **Usage note:** When following this procedure, if a situation does not match any documented pattern, if a step is ambiguous, or if you have to make an assumption the procedure does not address — stop and flag it. Describe what you encountered, what guidance you expected to find, and what you had to assume. These flags are how the procedure gets improved. Do not silently work around gaps.

## Procedure 1: Identify Candidate Clusters

The address is the anchor. Facilities don't move — ownership changes, names change, the spelling of names change, corporate structures change, but the physical location is the most stable fact in the database.

Identify all rows that may refer to the same physical location using three matching layers:

**Layer 1 — Exact match**
Same street number + street name + city + state.

**Layer 2 — Normalized match**
Same address after standardizing variations:
- Abbreviation variants: Street/St/ST, Avenue/Ave/AVE, Road/Rd, Boulevard/Blvd
- Directional variants: North/N, South/S, East/E, West/W
- Unit/suite notation: Ste/Suite, Apt/Unit, #
- Punctuation differences: periods, commas, hyphens

**Layer 3 — GPS proximity**
Different street addresses but geocoordinates within range:
- **Within 3,000 ft** → automatic campus confirmation. Same physical campus with different entry points, different buildings on the same property, or addresses assigned to different streets on the same parcel.
- **Beyond 3,000 ft** → flag for user review. Present the distance and let the user decide whether the facilities are campus-associated.

### Common patterns at shared addresses

When a cluster is identified, you'll typically see one of these four patterns:

| Pattern | What You See | What It Means |
|---|---|---|
| **Trailing Type, Two Records** | "Name - SNF" and "Name AL" as separate records, producing 3 rows (1 SNF + 2 ALFs) | One ALF is a phantom. The real facility is the SNF; NIC MAP duplicated it as an ALF. Migrate service flags before removing the phantom. |
| **Combined Type Attribute** | 1 record typed "AL/SNF", producing 2 rows | Usually legitimate — two licensed units at the same building. Keep both unless one is clearly a phantom. |
| **Two Different Names** | 2 records with distinct names at the same address, no type suffix | Legitimate campus pair — two separate buildings. Keep both. |
| **Placeholder IL** | An IL record with no address or minimal data, NIC confirms IL units exist | Real facility with incomplete data. Flag for enrichment, don't delete. |

These patterns help you interpret what the cluster is before you move to type validation in Procedure 2.

Clusters with three or more rows often exhibit multiple patterns simultaneously. For example, an address may have a Trailing Type phantom (SNF duplicated as ALF) AND a Two Different Names pair (two legitimate buildings). Evaluate each pair within the cluster independently — do not try to classify the entire cluster as a single pattern.

---

## Procedure 2: Validate Facility Type

For each row in a cluster, confirm the facility is correctly classified.

**Type verification:**
- Is this actually an ALF, or is it a SNF with "AL" appended by NIC MAP?
- Is this a CCRC campus aggregate carrying inflated bed counts from IL units? (Carol Woods 465 beds, Aldersgate 577 beds, Robin Run Village 530 beds — all were CCRC aggregates, not ALFs)
- Is this an Independent Living / Active Adult (55+) community that NIC MAP classified as an ALF? (Outside Eventus's serviceable market)
- Does the state licensing record confirm the facility type?

**Authority by facility type:**
- **SNFs** — CMS CCN is definitive for identity. CMS Provider Info confirms type.
- **ALFs** — State licensing is the only authority. NC DHSR license number, VA DSS license, IN QAMIS entry. ALFs have no federal identifier.

**Source check (for clusters with multiple rows):**
- **Same source** = likely campus pair (separate licensed units from the same dataset — e.g., AL wing and MC wing both from NIC)
- **Different source** = likely duplicate (same facility loaded from two pipelines — e.g., CMS/SNF and NIC-ALF)

The source check is a starting heuristic, not a rule. Stronger evidence overrides it. A CMS CCN match, a state licensing confirmation, or a clear phantom pattern (same name, same address, 0 census, NIC source alongside a CMS-confirmed SNF) takes precedence over the source-based signal. When the source heuristic conflicts with other evidence, go with the evidence.

Three SNFs at the same address, all with similar bed counts, is most likely a duplicate/triplicate row. The combination of Procedure 1 (they're at the same address) and Procedure 2 (they're all the same type) produces that evidence. Deduplication is not a separate procedure — it's a judgment that falls out of running Procedures 1 and 2.

### When duplicates are confirmed — which row survives?

| Step | Check | Outcome |
|---|---|---|
| 1 | Is one row served (Do_We_Serve = Yes)? | If no → skip to step 3 |
| 2 | Is that served row confirmed in the GLR? | If yes → keep the served row. If no → investigate the discrepancy before deciding. |
| 3 | Does one row have a real corporate name vs INDEPENDENT/unknown? | Keep the named row |
| 4 | Does one row have the operator vs a PropCo/LLC? | Keep the operator |
| 5 | Which row came from a more authoritative source? | GLR > CMS > NIC > LEGACY |
| 6 | Which row has more populated fields? | Keep the more complete row |

Step 1 decides the vast majority of cases. Steps 3-6 only matter when neither row is served.

For clusters with three or more rows: identify the strongest candidate first (usually the served, GLR-confirmed row), then compare each remaining row against it. You are not running a round-robin — you are confirming that the best row wins against all others and that every other row has a clear disposition (remove as duplicate, remove as phantom, or keep as legitimate campus pair).

---

## Procedure 3: Operator Attribution

For each facility, determine who operates it by populating the ownership structure across all layers and all sources.

### The ownership structure

Every facility has up to five layers of ownership. Each source may report a different entity at each layer. The goal is to populate what each source says, identify where they agree and disagree, and conclude who the operator is.

| Ownership Layer | What It Means |
|---|---|
| **Legal Owner** | The entity that legally owns the facility — often a local LLC |
| **PropCo** | The property company / REIT that owns the real estate — always distinct from the operator |
| **Management Company** | The company contracted to manage operations |
| **Management Sub-brand** | A regional or local brand under the management company (e.g., Twin Pines Healthcare under Hill Valley) |
| **Operator / Brand / Chain** | The entity that makes clinical and business decisions at the facility level — this is what we code in Corporate_Name |

### Populating the ownership table

For each facility, record what each source says at each layer:

| Ownership Layer | Forward Universe | CMS | NIC MAP | State Registry | GLR | ProPublica |
|---|---|---|---|---|---|---|
| **Legal Owner** | — | Legal Business Name | — | License Holder | — | Direct Owner (100%) |
| **PropCo** | — | — | Owner Name (col 18) | — | — | Indirect Owner |
| **Management Company** | — | — | Operator Name (col 41) | — | Parent Company | Managing Entity |
| **Management Sub-brand** | — | — | — | — | — | — |
| **Operator / Brand / Chain** | Corporate_Name | Chain Name | — | — | — | — |

### Source sequence

Check internal data first, then authoritative structured sources, then external web:

**Internal (know what you already know):**
1. **Forward Universe** — current Corporate_Name, facility count under that name, served count, name variants
2. **GLR Export** — Parent Company field for served facilities
3. **MUO Corporate History** — prior research on this entity
4. **Operator Research Log** — if already fully verified, apply established attribution

**Authoritative structured sources:**
5. **CMS Provider Info** (SNFs) — CCN, legal business name, chain name/ID, ownership type, CHOW flag
6. **ProPublica Nursing Home Inspect** (SNFs) — direct/indirect owners with %, managing entity, dates
7. **NIC MAP** (ALFs: starting point / SNFs: supplemental) — Owner Name (col 18) = PropCo, NEVER the operator. Operator Name (col 41) = management company candidate. See reliability patterns in `source_reference.md`.
8. **State Registry** — license holder, licensed administrator. The ONLY authority for ALFs.
9. **NPI Registry** — authorized official name/title → LinkedIn → employer reveals operating company

**External web (do not skip — these steps are mandatory, not optional):**
10. **Operator website** — go to the website. Do not cite what a prior session found — websites change. Check the footer for "Serviced by [Brand]" or copyright revealing management company. Check the portfolio/locations page and match every listed facility against the DB. Check HTML metadata (view source — schema publisher, og:site_name, title tags). Check logo file names (right-click → inspect element → image source URL). Note whether multiple facility websites share the same template. If the operator research log says this entity was previously verified, still check the website — the research log confirms the operator identity, but the website may reveal new information (rebrands, portfolio changes, acquisitions since last check).
11. **News / investigative journalism** — WBTV, NC Newsline, McKnight's, Skilled Nursing News, Senior Housing News, PESP reports, UC Berkeley, The Real Deal, local news, court record databases. Search by operator name, individual owner names, and facility names.

If the source sequence above resolves attribution with 2+ sources agreeing, proceed to the operator attribution rule. If sources conflict, refuse disclosure, or leave the operator ambiguous, escalate to the two-pass approach below.

### Escalation: Two-Pass Investigative Approach

The standard source sequence is linear — it works when a facility has a single, clearly identified operator and sources agree. It breaks down when:
- One ownership family operates under multiple CMS chain IDs
- The connection between chains is not visible in any single structured source
- Facilities refuse ownership disclosure to CMS/ProPublica
- An LLC or individual name appears as the operator but is actually a holding entity

When the linear sequence fails to resolve attribution, switch to a two-pass approach:

**Pass 1 — Structured lookups (what do the databases say?)**
Run steps 1-9 above. The goal is not to reach a conclusion — it is to build an inventory of every name, chain ID, LLC, individual, and ownership percentage associated with the facility. Collect everything. Note conflicts and unknowns.

**Pass 2 — Investigative (what's behind the names?)**
Use web research to connect what structured data cannot:

1. **Operator websites and HTML metadata** — check every website found in Pass 1. View source for publisher metadata, logo file names (e.g., "HVH_lyon_parkwood_web_logo.png" revealed Hill Valley behind Lyon). Are multiple facility sites built on the same template?
2. **REIT and real estate filings** — if the facility is leased, identify the REIT (Strawberry Fields, Sabra, CareTrust, Welltower, Omega, NHI). REITs publish portfolio pages listing the operator/tenant name, which may differ from the CMS chain.
3. **Industry news, court filings, investigative journalism** — search for every individual name from ProPublica ownership filings, every LLC name from CMS, every chain brand name. Combine names as search terms (e.g., "Chopp + healthcare", "Lyon + Hill Valley").
4. **Return to structured sources with new names** — this is the critical step the linear process misses. Take every new name, LLC, or individual discovered in steps 1-3 and search them back through CMS ownership filings, ProPublica, and the Forward Universe. Do these names appear on OTHER facilities? Do these individuals own other chains? Are these LLCs coded as corporate names elsewhere in the DB?

This feedback loop is what connects corporate families that operate under multiple CMS chain IDs. The Lyon / Hill Valley / Bedrock case required it: three separate CMS chains (270, 837, 73), three brands, three geographies — but one family (Chopp) controlling all of them, discovered only by searching ownership names back through CMS filings after web research surfaced the family name. See `reference/MUO_Corporate_History.md` for the full evidence chain and `reference/Alternative_11_Step_Verification_Process.md` for the detailed case study.

### The operator attribution rule

Code the entity that makes clinical and business decisions at the facility level — the operator — regardless of who owns the building, holds the license, or appears in CMS chain records.

- CMS chain name ≠ operator (chains track holding companies or therapy vendors)
- Management company ≠ owner (MFA, YAD, LifeWorks manage for multiple owners)
- NIC MAP Owner field ≠ operator (NIC surfaces PropCo LLCs, not management companies)
- "All facilities under management company X belong to owner Y" is NEVER a safe assumption — always verify per-facility
- "All facilities under owner X are managed by company Y" is EQUALLY unsafe — an owner may contract different management companies for different facilities. Verify per-facility.

### Owner vs. management company

When a facility's legal owner (per CMS/ProPublica) is a different entity from the management company (per ProPublica managing entity, operator website, or GLR), the question is: which do we code?

**Code the management company / operator, not the legal owner, when:**
- The legal owner is a hospital, nonprofit, REIT, or holding entity that owns the building but does not run day-to-day clinical operations
- The management company brands the facility as its own (facility appears on management company's website, carries their branding)
- The legal owner's own website does not mention the facility or long-term care operations

**Code the legal owner when:**
- The legal owner directly operates the facility (no separate management company in ProPublica or on the website)
- The legal owner's website lists the facility and describes operational involvement
- There is no managing entity in ProPublica or CMS

**Critical: do not assume one management company manages all facilities for a single owner.** The Putnam County Hospital case proved this: CMS shows Putnam County Hospital as 100% owner of 19 Indiana SNFs, and prior research assumed all 19 were managed by HutsonWood (HHSS Management LLC). But HutsonWood's own website lists only 2 Indiana communities. The other 17 facilities may have entirely different operators. Each facility's managing entity must be verified individually through ProPublica, operator websites, or state registry before any recode.

### Persistence and maintenance

The ownership table is populated once per facility and maintained over time — it is not rebuilt from scratch on every review. Once the full ownership structure is mapped (legal owner, PropCo, management company, sub-brand, operator), it becomes a living reference that is updated only when something changes (CHOW, merger, rebrand, divestiture).

This serves two purposes:

1. **Eliminates redundant research.** If the ownership structure for a facility has been fully mapped and documented, future inquiries reference the existing record rather than re-investigating from scratch.
2. **Provides relationship context.** When a stakeholder says "I think this facility is owned by X," the ownership table shows where X sits in the structure — X might be the PropCo, the legal owner, a former management company, or the actual operator. The relationships between all entities are documented, so the answer is a lookup, not a research project.

Updates to the ownership table are triggered by:
- A new source refresh (CMS extract, NIC MAP export, state registry pull) that shows a value change
- A CHOW or entity reconciliation finding during any procedure
- A stakeholder question that reveals new information

When the ownership table reveals that internal systems disagree — e.g., Finance carries a different corporate name than the Forward Universe, or the GLR uses a management sub-brand where we code the parent operator — that triggers a communication need. The discrepancy must be surfaced to the affected team (Finance, clinical ops, BD) so internal systems can be aligned. The ownership table provides the evidence and relationship context to explain why the names differ and which entity sits where in the structure. These corrections are logged to `scripts/audit_reports/glr_change_log.csv` for GLR-specific discrepancies and flagged directly to the relevant stakeholder for other systems.

### Variance detection

When ownership layer values conflict across sources, the variance is itself a signal:
- CMS chain ≠ Forward Universe Corporate_Name → possible CHOW or stale DB attribution
- NIC MAP operator ≠ Forward Universe Corporate_Name → possible stale NIC MAP data or stale DB data
- State registry license holder ≠ CMS legal business name → possible PropCo/OpCo split or recent transfer
- Multiple sources updating at different cadences means temporal gaps are expected — the question is which source has the most current information

### 3.1 Source Reconciliation

When external sources are refreshed (new CMS extract, new NIC MAP export, new state registry pull), diff the new values against the ownership table. Changes in source values surface CHOWs, entity name changes, and chain ID movements without requiring manual per-facility investigation.

### Sub-finding: Entity Reconciliation

During attribution work, you may discover that two corporate names in the DB are actually the same entity. Signals:

- Portfolio matching: Brand A's website lists facilities coded to Brand B in our DB
- Shared HQ address or shared personnel (same CEO, same authorized official on NPI)
- ProPublica shows the same holding entity above both brands
- Same PropCo LLC structure across facilities coded to different corporate names

When confirmed, log to `MUO_Corporate_History.md` and flag name variants for consolidation. Do NOT bulk-recode — verify each facility individually before changing attribution.

**Example:** Portopiccolo Group — 58 DB rows coded under 5 different corporate names (SIMCHA HYMAN & NAFTALI ZANZIPER, ACCORDIUS HEALTH LLC/PORTOPICCOLO GROUP, AUGUST HEALTHCARE, PELICAN HEALTH HENDERSON, MONROE PROPCO LLC). All the same economic entity, operating through regional management brands. Correct resolution: code each facility to its regional operator brand, not the PE parent.

### Sub-finding: Change of Ownership (CHOW)

During attribution work, you may discover that the operator has changed since data was last updated. Signals:

- CMS facility name or chain name differs from DB
- NC DHSR CON exemption filings show a transfer (most current source for NC — catches CHOWs before CMS)
- Facility website rebranded (new name, new footer, new management company)
- NPI authorized official has changed
- NIC MAP operator differs from DB (but NIC MAP can also be stale — verify the direction of the discrepancy)

When confirmed, identify the new operator using the full source sequence. Check for batch transfers — if one facility CHOWed, others in the same portfolio may have too (the Portopiccolo → Hill Valley pattern: 1 CHOW finding led to 6 more via NC DHSR CON filings).

**Example:** Pair 14, Mooresville NC — CMS still showed "Accordius Health at Mooresville," but NC DHSR CON filing and the facility website (crestview-hr.com, "Serviced by Twin Pines Healthcare") confirmed CHOW to Hill Valley Healthcare. NPI authorized official (Joseph Lieberman, VP Procurement) → LinkedIn → Hill Valley. Four independent sources converging.

### New MUO Candidate Evaluation (8-Step Corporate Reconciliation)

When operator attribution surfaces a new corporate entity that may qualify for the scoring board, run the full reconciliation:

1. **DB fuzzy name scan** — query DB for corporate_name_raw + facility_name variants
2. **CMS cross-reference** — query CMS Provider Info — AUTHORITY SOURCE for SNFs
3. **Web validation** — check operator website + A Place for Mom + state licensing + SEC
4. **Consolidation** — merge DB + CMS + web into single facility list with source citations
5. **Footprint filter** — count only 6 operating states (NC, SC, VA, KY, OH, IN)
6. **Campus collapse** — street-number matching (same street + city = 1 campus), 15-bed minimum
7. **7+ gate** — pass/fail on collapsed campus count. Below 7 = does not qualify for scoring board.
8. **Score** — apply V23 formula (6 dimensions) for operators that pass

### Corporate Name Standardization

When the verified operator is known, determine the correct corporate name for the DB:

1. **Code by the operating entity** — the entity that makes clinical and business decisions at the facility. Not the PE parent, not the PropCo, not the license-holding LLC, and not a consumer-facing marketing sub-brand.
2. **Distinguish operator from PropCo from sub-brand.** The ownership table has five layers for a reason. A PropCo owns the building but doesn't operate it — never code the PropCo (e.g., Portopiccolo Group). A marketing sub-brand is a consumer-facing label under the operator — never code the sub-brand. The test: does the entity have its own NPI registrations, its own OpCo LLCs, its own management structure, its own state licensing? If yes, it's an operator. If it's a label under an entity that has those things, it's a sub-brand. If you pulled the entity out of its parent, would it still be an operating company? If yes, it's an operator. If it would cease to exist, it's a marketing label.

   **Example — sub-brand that is NOT an operator (do not code):**
   Twin Pines Healthcare is Hill Valley's consumer-facing brand in NC. The website footer says "Serviced by Twin Pines Healthcare," but every piece of operational evidence traces to Hill Valley: the OpCo LLCs (Crestview SNF Operations LLC) are Hill Valley entities, the NPI authorized official works for Hill Valley, the website HTML metadata identifies Hill Valley as the parent. Twin Pines has no separate CMS registrations, no separate state licensing, no separate NPI. If Hill Valley rebranded from Twin Pines to something else tomorrow, nothing operational changes. **Code: HILL VALLEY HEALTHCARE.** Twin Pines is documented in the ownership table's Management Sub-brand row for reference.

   **Example — regional brand that IS an operator (code it):**
   Bluegrass Consulting Group operates 17 served facilities in KY under the Majestic Care corporate family. Bluegrass has its own management structure, its own operational presence, its own KY footprint that predates the Majestic relationship. If you pulled Bluegrass out of the Majestic family, it would still be an operating entity. **Code: MAJESTIC / BLUEGRASS CONSULTING GROUP.** The slash notation shows both the parent and the regional operator.

3. **Multiple corporate names for one economic entity is acceptable** if they reflect genuinely different operating entities with their own management structures (e.g., Portopiccolo's regional operators: Accordius in NC, Clearview in KY, August Healthcare in eastern NC/VA — each has its own facilities, its own compliance infrastructure, its own CMS registrations). Use the slash notation (`PARENT / REGIONAL OPERATOR`) when the regional brand is a real operator under a known parent.
4. **Check the GLR** — what corporate name does the GLR use? The GLR codes by operator, which confirms the approach.
5. **Log all name variants, mergers, rebrands, and corporate relationships** to `MUO_Corporate_History.md` immediately.

---

## Procedure 4: Validate Beds, Census, and Consents

For each facility, confirm the quantitative fields are accurate. Skip rows that have been flagged for removal in Procedure 2.

### Total Beds — reconciliation rule

Compare the DB bed count against the authoritative source (CMS for SNFs, state licensing for ALFs, GLR Licensed Bed # for served facilities):

- **Within 15 of each other** → take the larger number. Licensed capacity is the ceiling; small differences are rounding, timing, or data vintage.
- **Greater than 15 apart** → flag for review. Something structural may have changed — wing closure, expansion, decertification, campus aggregate, or data entry error.

### Bed count as a facility type cross-check

An unusually high bed count on an ALF is a signal that the row may be misclassified. ALFs above ~200 beds should be checked against Procedure 2 — the row may be a CCRC campus aggregate carrying IL units (Carol Woods 465, Aldersgate 577, Robin Run Village 530 were all this pattern). If the bed count cannot be verified against state licensing at that level, it is likely an aggregate that needs to be decomposed or reclassified.

### If served (Do_We_Serve = Yes)

We have GLR ground truth. The GLR carries three distinct quantitative fields:

| GLR Field | What It Is | What It Measures |
|---|---|---|
| **Licensed Bed #** | Licensed capacity | Total beds — should align with CMS/state licensing |
| **Current Census #** | Actual facility occupancy | How many residents are in the building |
| **Total Patients** | Eventus patient count | Our consents — a rollup of all service line volumes |

The GLR also carries consents broken out by service line: Primary Care Volume, Psychiatry Volume, Mental Health Volume, Podiatry Volume, Pain Volume, Wound Care Volume, Specialty Volume, and others. "Total Patients" is the sum. The service mix matters — a facility with 30 PC consents and 0 MH is a different profile than 15 PC and 15 MH.

**Validation checks for served facilities:**
- **Census** — this must reflect actual total facility occupancy, NOT Eventus consents. If the DB census value equals GLR Total Patients, the field is suspect — it is carrying our penetration, not the facility's occupancy. Flag for correction.
- **Total Beds** — apply the reconciliation rule above against GLR Licensed Bed #.
- **Consents** — the Forward Universe does not currently have a Consents column. Service line volumes live in the GLR. Until a consents structure is added to the DB, the GLR is the source of truth for this data. This is a known structural gap.

### If unserved (Do_We_Serve = No)

No GLR data. No consents. No operational relationship.

- **Total Beds** — apply the reconciliation rule above against CMS (SNF) or state licensing (ALF). Check for campus aggregate inflation (IL units bundled into ALF bed count).
- **Census** — this is an estimate of total facility occupancy from external sources. It is the basis for revenue potential estimation.
- **Consents** — should not exist for unserved facilities. If a value is present, it is a data error.

### What this procedure does NOT do

Procedure 4 validates that the numbers in these fields are accurate. It does not compute revenue potential, apply S2 modifiers, calculate penetration rates, or perform any downstream modeling. Those computations depend on Procedure 4 being done correctly, but they are not part of the cleansing procedure.

---

---

*Created: 2026-04-03. Consolidates content from DB_Verification_Procedures.md, portopiccolo_research_methodology.md, Verification_Methodology.html, source_lookup_howto.md, and dedup_review_workflow.md.*
