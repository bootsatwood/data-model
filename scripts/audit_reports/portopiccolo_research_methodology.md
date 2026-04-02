# Portopiccolo Ownership Research — Findings and Methodology

**Date:** March 29 – April 1, 2026
**Researcher:** Roian Atwood + Claude Code
**Starting point:** Facility dedup Pair 14 (752 E Center Ave, Mooresville NC)
**Ending point:** 39 corporate recodes, 7 confirmed CHOWs, 8 operator brands mapped, GLR change log established

---

## How This Started

We were doing routine facility dedup work — reviewing address-level duplicate pairs in the Combined Database one at a time. Pair 14 was three rows at 752 E Center Ave, Mooresville NC, all coded to ACCORDIUS HEALTH LLC/PORTOPICCOLO GROUP. Two rows said "Accordius Health at Mooresville" and one said "Crestview Health & Rehabilitation."

The standard dedup procedure says: for SNFs, check the CMS CCN to confirm identity. CMS CCN 345179 confirmed one facility. But then the question became: which name is current — Accordius or Crestview?

That question launched everything that followed.

---

## Phase 1: The CHOW Discovery (Pairs 14-18)

### Step 1: Verify the current facility name

We searched for CCN 345179 across CMS, ProPublica, and the web. CMS and ProPublica still showed "Accordius Health at Mooresville" — but a Nursa.com listing and an NC DHSR filing showed "Crestview Health & Rehabilitation." The NC DHSR Certificate of Need exemption filing (Record 4743) confirmed a Change of Ownership (CHOW) to a new entity called "Crestview SNF Operations LLC."

**Key learning:** CMS data lags behind actual ownership changes. NC DHSR filings are more current for NC facilities.

### Step 2: Identify the new operator

"Crestview SNF Operations LLC" is a shell entity — who's actually behind it? We checked:
- The NPI registration (1093518086): authorized official was Joseph Lieberman, VP of Procurement
- LinkedIn: Joseph Lieberman works at **Hill Valley Healthcare**
- The facility website (crestview-hr.com): footer says "Serviced by **Twin Pines Healthcare**"
- Twin Pines Healthcare's website (twinpineshc.com): HTML metadata identifies **Hill Valley Healthcare** as the parent organization

**Evidence chain:** NPI → LinkedIn → facility website → Twin Pines website → Hill Valley Healthcare. Four independent sources converging on the same answer.

### Step 3: Check for a pattern

If Portopiccolo sold one facility to Hill Valley, did they sell others? We searched NC DHSR CON exemption filings and found Record 4648-4652 — a **5-facility batch** transfer from Portopiccolo to Hill Valley, all filed October 30, 2024, effective December 1, 2024. Combined with the Mooresville filing, that made 6 total.

Each transferred facility followed the same pattern:
- New OpCo named "[Something] SNF Operations LLC"
- New website at "[something]-hr.com"
- All branded "Serviced by Twin Pines Healthcare"

### Step 4: Match the CHOW facilities to our DB

The CHOW filings used the facility names at time of filing, not necessarily the names in our DB. We had to match by address:
- Sherwood Health and Rehab → 4801 Randolph Rd, Charlotte → DB rows 9286 + 20198
- Stratford Manor → 204 Old Hwy 74 E, Monroe → DB rows 8590 + 19465
- Redwood Health and Rehab → 5939 Reddman Rd, Charlotte → DB row 8586
- Plaza Health and Rehab → 2616 E 5th St, Charlotte → DB row 9285
- Belmont Health and Rehabilitation → 416 N Highland St, Gastonia → DB row 8588

Three of those addresses had **duplicate rows** — which meant the CHOW research also surfaced new dedup pairs (Pairs 15-16) that we hadn't found in the original dedup index.

### Step 5: Additional dedup pairs

During the address sweeps, we also found:
- Gatesville (38 Carters Rd): 2 rows, same facility, both CMS source — Pair 17
- Mooresville Glenwood (550 Glenwood Dr): 2 rows, Citadel vs Glenwood — Pair 18

These weren't CHOW facilities but were duplicate rows under different Portopiccolo brand names at the same address.

**Key learning:** Corporate-lens research surfaces dedup pairs that per-facility or per-address dedup doesn't catch, because the facilities have different names and came through different pipelines.

---

## Phase 2: The Ownership Structure

### Step 6: Map the full Portopiccolo footprint in our DB

We searched the V25.5 database for all known Portopiccolo corporate name variants:
- SIMCHA HYMAN & NAFTALI ZANZIPER
- ACCORDIUS HEALTH LLC/PORTOPICCOLO GROUP
- AUGUST HEALTHCARE / AUGUST HEALTHCARE GROUP
- PELICAN HEALTH HENDERSON
- MONROE PROPCO LLC

Result: **58 rows** across NC (34), KY (20), VA (2), OH (1), SC (1). All coded under 5 different corporate names for the same parent entity.

### Step 7: Map the regional management brands

Portopiccolo doesn't operate under a single name. We discovered the regional structure by:

1. **Checking operator websites.** Each facility has its own website. The footer or copyright notice reveals the management company:
   - crestview-hr.com → "Serviced by Twin Pines Healthcare" (Hill Valley)
   - gatesrehab.com → August Healthcare compliance hotline
   - glenwoodrnc.com → "Maple Health Group" copyright
   - maplehealthandrehab.com (Greenville KY) → "Clearview Management" copyright

2. **Following the Clearview thread.** The Greenville KY facility's copyright led to clearviewhcmgmt.com. Their portfolio page listed 8 facilities — every single one matched a DB row coded to SIMCHA HYMAN & NAFTALI ZANZIPER. That confirmed Clearview = Portopiccolo's KY management brand.

3. **Cross-referencing ProPublica.** For each facility, ProPublica shows the CMS ownership chain. We could verify whether the holding structure (MC M53 Spe Opco Holdco, Accordius SNF Holdco LLC, HC Family Trust, etc.) matched across facilities.

**Brands confirmed:**
| Brand | Region | How Confirmed |
|---|---|---|
| Accordius Health LLC | NC | CMS, ProPublica, news articles |
| August Healthcare | Eastern NC + VA | CMS (Augustnc Holdco LLC), augusthcg.com, UC Berkeley journalism, shared HQ address |
| Clearview Healthcare Management | KY/TN | Portfolio matching against DB rows, PESP report, KY Lantern |
| Maple Health Group | NC (some) | Website copyright (glenwoodrnc.com, salisburyrnc.com) |
| YAD Healthcare | NC, SC, VA | Facility websites ("A proud member of YAD Healthcare"), CMS |
| Alliance Health Group | NC, FL | Facility websites redirect to alliancehealthgrp.com |
| Pelican Health | NC (Charlotte) | WBTV, PESP, Washington Post |
| Citadel | Facility-level LLCs | CMS OpCo names, WBTV |

---

## Phase 3: The Standardization Decision

### Step 8: Choose the right corporate name

With the ownership structure mapped, we had to decide: what goes in the Corporate_Name field?

**Option considered and rejected: PORTOPICCOLO GROUP.** This would consolidate all 46 remaining rows under one name, making the full footprint visible at a glance. But Portopiccolo is the PE holding layer — they own the buildings (PropCo LLCs). Our operator attribution rule says: code the clinical/business decision-maker, not the PropCo or license holder. Coding everything as "Portopiccolo" would be coding the landlord, not the operator.

**Option chosen: Regional operator brand.** Code each facility to the entity that actually makes clinical and business decisions at that facility. This means multiple corporate names in our DB for what is economically one entity — but it correctly reflects who is operating each facility.

### Step 9: Verify before recoding

We didn't just assume. For each batch:

- **KY (20 rows) → CLEARVIEW:** Verified via Clearview's own portfolio page listing these exact facilities.
- **NC YAD (5 rows):** Verified via individual facility websites showing "A proud member of YAD Healthcare."
- **NC Alliance (3 rows):** Verified via facility websites redirecting to alliancehealthgrp.com.
- **NC August (1 row + VA 2 rows):** Verified via augusthcg.com facilities page.
- **NC Maple (2 rows):** Verified via website copyright notices.
- **NC Midwood (1 row):** Confirmed still branded Accordius, no CHOW, no rebrand.

And the verification surfaced two more surprises:
- **Concord** had CHOWed to Hill Valley (copperfield-hr.com, Twin Pines branding) — a 7th Hill Valley facility we didn't know about.
- **Myers Park** had been CMS-decertified (Immediate Jeopardy, March 2025) and reopened under CARE Management Company — entirely new operator.

### Step 10: Check the GLR

Before finalizing, we checked what the GLR (our upstream data source) uses for corporate names. The GLR uses regional brand names (CLEARVIEW, ACCORDIUS HEALTH LLC/PORTOPICCOLO GROUP, August Healthcare Group) — not the principal names. This confirmed our approach: the GLR also codes by operator, not by PE parent.

---

## What We Learned About Portopiccolo's Structure

Portopiccolo Group LLC is a New York-based PE firm founded in 2016 by Simcha Hyman and Naftali Zanziper. They own 131+ nursing homes across 10+ states. Their operating model:

1. **PropCo/OpCo split.** Portopiccolo owns buildings through property LLCs (e.g., "Wilson NC Propco LLC"). A separate operating LLC runs the facility (e.g., "Accordius Health at Wilson LLC"). This insulates the real estate from operational liability.

2. **Regional management brands.** Instead of one national operator brand, they use different management companies in different regions. This makes it difficult to see the full footprint — no single brand name appears on all facilities.

3. **Brand rotation.** When a brand accumulates negative press or regulatory penalties, facilities are transferred to a new brand. August Healthcare was created in September 2021 after Accordius faced negative coverage; facilities were transferred directly from Accordius to August. Portopiccolo's spokesman publicly stated "August isn't owned by Portopiccolo Group" — but August Healthcare shared Portopiccolo's Englewood Cliffs NJ address, and the PropCo LLCs remained Portopiccolo-owned.

4. **CMS data opacity.** CMS ownership filings list the principals (Hyman/Zanziper) or the holding entities (MC M53 Spe Opco Holdco) — not the consumer-facing brand. The word "Portopiccolo" does not appear in CMS data. This is by design.

5. **Divestiture in progress.** As of early 2025, Portopiccolo is actively divesting NC facilities. 7 (possibly 8) went to Hill Valley Healthcare. 17 VA facilities went to Eastern Healthcare Group in 2023. The Citadel at Myers Park was CMS-decertified. The remaining NC footprint is smaller than it was 2 years ago.

---

## The Evidence Hierarchy

When researching facility ownership, we found that different sources have different reliability for different questions:

| Question | Best Source | Second Best | Unreliable |
|---|---|---|---|
| Is this the same building? | CMS CCN (SNFs) / state licensing (ALFs) | Address + Campus_ID match | Name alone (facilities rename) |
| Who owns it now? | NC DHSR CON filings (most current for NC) | ProPublica / CMS (lags 6-12 months) | NIC MAP / GLR (can lag years) |
| What's the current name? | Operator's own website | NCHCFA directory | CMS (holds old names after CHOW) |
| Who is the operator? | Operator website footer ("Serviced by...") | NPI registration (authorized official) | CMS ownership chain (lists owners, not operators) |
| Are two brands the same entity? | Portfolio matching (brand's facility list vs DB rows) | Shared HQ address / personnel overlap | Name similarity (unreliable) |

---

## Methodology Reusable for Future Corporate Research

The approach we used here can be applied to any corporate operator investigation:

1. **Start with what the DB says.** Pull all rows for the corporate name. Note variants.
2. **Check CMS/ProPublica.** For each SNF, pull the ownership chain. Look for common holding entities, trusts, individuals.
3. **Check the operator's website.** Look at the footer — who provides management services? What other facilities are listed?
4. **Follow the management company.** If a management brand is named, check their website for a portfolio or facility list. Match every facility against the DB.
5. **Check NC DHSR (for NC facilities).** CON exemption filings show CHOWs before CMS catches up.
6. **Search news/investigative journalism.** WBTV, NC Newsline, McKnight's, Skilled Nursing News, PESP reports, UC Berkeley — these name brands that CMS data hides.
7. **Verify each facility individually.** Don't bulk-assume. The V25.2 YAD/Choice Health error happened because we pattern-matched instead of verifying per-facility.
8. **Log everything.** MUO_Corporate_History.md, GLR change log, decisions log, memory files. Research evaporates if it's not written down.

---

## Files Produced

| File | Purpose |
|---|---|
| `scripts/audit_reports/dedup_decisions_log.csv` | Every dedup and recode decision with evidence citations |
| `scripts/audit_reports/glr_change_log.csv` | Structured list of upstream GLR corrections needed |
| `scripts/audit_reports/glr_change_log_notes.md` | Narrative evidence for GLR team conversations |
| `reference/MUO_Corporate_History.md` | Portopiccolo + Hill Valley corporate entries (permanent record) |
| `scripts/audit_reports/portopiccolo_research_methodology.md` | This document |

---

## Open Items

1. **Camellia Gardens** (Durham NC, ALF) — coded PELICAN HEALTH HENDERSON. Operator verification pending.
2. **Beavercreek Health and Rehab** (OH) — coded SIMCHA HYMAN & NAFTALI ZANZIPER. Operator verification pending.
3. **Achieve Rehabilitation** (Anderson SC) — coded SIMCHA HYMAN & NAFTALI ZANZIPER. Operator verification pending.
4. **Salisbury** — may have CHOWed to Hill Valley (Meadowbrook SNF Ops LLC, closing 5/1/2025). Pending confirmation.
5. **Barrier review** (DB punchlist #17) — all Hill Valley facilities carry Portopiccolo-era barriers that may no longer apply.
