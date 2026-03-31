# GLR Change Log — Narrative Notes

Companion to `glr_change_log.csv`. These notes explain the research behind each change and are intended to support conversations with the GLR team about upstream data corrections.

---

## Background: Portopiccolo Group — Who They Are

Portopiccolo Group LLC is a New York-based private equity firm founded in 2016 by Simcha Hyman (CEO) and Naftali Zanziper (President). They operate 131+ nursing homes across 10+ states through an opaque layered ownership structure: Portopiccolo Group → Accordius SNF Holdco LLC → MC M53 Spe Opco Holdco → individual facility OpCo LLCs. Related trusts include HC Family Trust, SHNZ Holdings LLC, Wyncote LLC, and Zanziper Family Trust.

Critically for GLR purposes, Portopiccolo does not operate under a single brand. Their facilities are managed through regional management companies that do not reference Portopiccolo in public-facing materials:

- **Accordius Health LLC** — primary NC brand (also appears as CMS operator name nationally)
- **August Healthcare** — eastern NC + VA facilities (Gatesville, Wilson, Ahoskie, Scotland Neck, Wilmington)
- **Clearview Healthcare Management** — KY/TN facilities (Louisville HQ, clearviewhcmgmt.com, confirmed managing 8 KY Portopiccolo SNFs)
- **Maple Health Group** — some NC facilities (appears in website copyright for Glenwood Rehab Mooresville)
- **Pelican Health** — Charlotte-area NC facilities
- **Citadel** — used in facility-level OpCo names (Citadel Mooresville LLC, Citadel at Myers Park LLC)

This means GLR records may code the same parent company under different names depending on which management brand was visible at the time of data collection. All of these are Portopiccolo.

## Background: Portopiccolo → Hill Valley Healthcare (6-Facility NC Transfer)

Between December 2024 and May 2025, six skilled nursing facilities in North Carolina transferred from Portopiccolo Group / Accordius Health LLC to Hill Valley Healthcare, a New York-based national SNF operator founded in 2018. Hill Valley runs its North Carolina facilities through a consulting brand called **Twin Pines Healthcare** (twinpineshc.com, Charlotte NC area code 704). Twin Pines Healthcare's website metadata identifies Hill Valley Healthcare as the parent organization.

Each transferred facility was assigned a new operating entity following the pattern "[Name] SNF Operations LLC" and a website following the pattern "[name]-hr.com", all branded under Twin Pines Healthcare with the footer "Serviced by Twin Pines Healthcare."

The transfer was documented in NC DHSR Certificate of Need exemption filings:
- **Records 4648-4652** (filed October 30, 2024): 5 facilities, effective December 1, 2024
- **Record 4743** (filed 2025): 1 facility, effective May 1, 2025

Evidence chain for each CHOW: NC DHSR filing → NPI registration (authorized official Joseph Lieberman, VP Procurement at Hill Valley Healthcare per LinkedIn) → facility website with Twin Pines branding → Twin Pines website metadata confirming Hill Valley parentage.

CMS records and ProPublica still show Accordius Health LLC as the operator for most of these facilities — typical CHOW data lag. The GLR dump also still carries Accordius/Portopiccolo as the parent company. These notes document the evidence for each facility so the GLR team can update their records.

---

## CCN 345179 — 752 E Center Ave, Mooresville NC (Iredell County)

**GLR currently shows:** Crestview Health & Rehabilitation, parent = ACCORDIUS HEALTH LLC/PORTOPICCOLO GROUP

**Should be:** Crestview Health & Rehabilitation, parent = HILL VALLEY HEALTHCARE

This facility has had three names: Brian Center Health and Retirement, then Accordius Health at Mooresville, and now Crestview Health & Rehabilitation. The GLR has the current facility name correct but the corporate attribution is stale. NC DHSR Record 4743 confirms the CHOW to Crestview SNF Operations LLC, effective May 1, 2025. The operator website (crestview-hr.com) carries Twin Pines Healthcare branding. CMS certified beds = 131, but the facility appears to be operating at 71 beds / 57 census based on current data.

---

## CCN 345134 — 4801 Randolph Rd, Charlotte NC (Mecklenburg County)

**GLR currently shows:** Sherwood Health and Rehab, parent = ACCORDIUS HEALTH LLC/PORTOPICCOLO GROUP

**Should be:** Sherwood Health and Rehab, parent = HILL VALLEY HEALTHCARE

Name history: Avante at Charlotte → Sherwood Health and Rehab → Pelican Health Randolph LLC (CMS still shows this) → current consumer-facing name is Sherwood Health & Rehabilitation. The OpCo entity is Randolph Gardens SNF Operations LLC, but the facility's own website (sherwood-hr.com) uses the Sherwood name with Twin Pines Healthcare branding. NC DHSR Record 4650 confirms the CHOW effective December 1, 2024. GLR has the correct facility name; only the parent company needs updating. 100 beds, 75 census, 48 patients (41 PC, 34 Spec).

---

## CCN 345345 — 204 Old Hwy 74 E, Monroe NC (Union County)

**GLR currently shows:** No GLR record at this address.

**Action needed:** If/when this facility enters the GLR, it should be coded as Stratford Manor Health & Rehabilitation, parent = HILL VALLEY HEALTHCARE.

There is one skilled nursing facility at this address with CMS certification number 345345 and 60 licensed beds. Our database had two rows for it because they came in through two different data pipelines. Row 8590 came from the CMS/SNF pipeline and landed as "ACCORDIUS HEALTH AT MONROE" under the corporate name "SIMCHA HYMAN & NAFTALI ZANZIPER" — which is accurate, because Simcha Hyman and Naftali Zanziper are the two principals behind the Portopiccolo Group, which operates Accordius Health facilities. Row 19465 came from the LEGACY pipeline and landed as "STRATFORD MANOR HEALTH & REHABILITATION" under "MONROE PROPCO LLC" — which is a property company, not an operator. The LEGACY pipeline picked up the PropCo entity from a licensing or property record rather than the clinical operator. It also tagged it as "Independent" ownership, which is wrong — CMS confirms this is a for-profit corporate facility.

This facility has been renamed multiple times — it started as Brian Center Health and Retirement (a Portopiccolo brand), became Accordius Health at Monroe (another Portopiccolo rebrand), and as of December 1, 2024, it's Stratford Manor Health & Rehabilitation. We know about that last name change because of NC DHSR Record 4648, part of the 5-facility batch transfer. The new operating entity is Rock Rest SNF Operations LLC. The facility's own website (stratfordmanor-hr.com) carries the Twin Pines Healthcare branding, confirming Hill Valley Healthcare as the actual operator.

---

## CCN TBD — 5939 Reddman Rd, Charlotte NC (Mecklenburg County)

**GLR currently shows:** Needs verification — DB coded as ACCORDIUS HEALTH AT CHARLOTTE under SIMCHA HYMAN & NAFTALI ZANZIPER

**Should be:** Redwood Health & Rehabilitation, parent = HILL VALLEY HEALTHCARE

This facility was part of the 5-facility batch CHOW filed October 30, 2024 (NC DHSR Record 4649), effective December 1, 2024. The new operating entity is Eastland SNF Operations LLC. The facility was renamed from Accordius Health at Charlotte to Redwood Health & Rehabilitation. The operator website (redwood-hr.com) carries Twin Pines Healthcare branding ("Serviced by Twin Pines Healthcare"), confirming Hill Valley Healthcare as the parent operator. CMS source, 116 beds. Not served by EWH. Barrier flags carried from Portopiccolo era: Alliance + Own Provider Group — these are confirmed as real barriers under Hill Valley and are flagged for future barrier review (DB punchlist #17).

---

## CCN TBD — 2616 E 5th St, Charlotte NC (Mecklenburg County)

**GLR currently shows:** Needs verification — DB coded as PELICAN HEALTH AT CHARLOTTE under SIMCHA HYMAN & NAFTALI ZANZIPER

**Should be:** Plaza Health & Rehabilitation, parent = HILL VALLEY HEALTHCARE

This facility was part of the 5-facility batch CHOW filed October 30, 2024 (NC DHSR Record 4651), effective December 1, 2024. The new operating entity is Eastover SNF Operations LLC. The facility was renamed from Pelican Health at Charlotte to Plaza Health & Rehabilitation. The operator website (plaza-hr.com) carries Twin Pines Healthcare branding ("Serviced by Twin Pines Healthcare"), confirming Hill Valley Healthcare as the parent operator. CMS source, 120 beds. Not served by EWH. Barrier flags: Alliance + Own Provider Group — flagged for future barrier review (DB punchlist #17).

---

## CCN 345162 — 416 N Highland St, Gastonia NC (Gaston County)

**GLR currently shows:** Needs verification — DB coded as ACCORDIUS HEALTH AT GASTONIA under SIMCHA HYMAN & NAFTALI ZANZIPER

**Should be:** Belmont Health & Rehabilitation, parent = HILL VALLEY HEALTHCARE

This facility was part of the 5-facility batch CHOW filed October 30, 2024 (NC DHSR Record 4652), effective December 1, 2024. The new operating entity is Heights SNF Operations LLC. The facility was renamed from Accordius Health at Gastonia to Belmont Health & Rehabilitation. The operator website (belmont-hr.com) carries Twin Pines Healthcare branding ("Serviced by Twin Pines Healthcare"), confirming Hill Valley Healthcare as the parent operator. NC DHSR confirms CCN 345162, 118 licensed beds. Not served by EWH. Barrier flags: Alliance + Own Provider Group — flagged for future barrier review (DB punchlist #17).

---

## Document History

| Date | Action | Details |
|---|---|---|
| 2026-03-30 | Created | GLR change log initiated during dedup Pair 14 (Mooresville). Portopiccolo → Hill Valley CHOW research. |
| 2026-03-30 | Added entries | CCN 345179 (Mooresville), CCN 345134 (Charlotte Randolph), CCN 345345 (Monroe) |
| 2026-03-31 | Added entries | 3 remaining CHOW facilities: Redwood (Charlotte Reddman), Plaza (Charlotte 5th), Belmont (Gastonia) |
| 2026-03-31 | Added background | Portopiccolo ownership structure, regional brand mapping, evidence chain methodology |
| 2026-03-31 | Added punchlist ref | Barrier review (DB punchlist #17) flagged for all 6 CHOW facilities |
