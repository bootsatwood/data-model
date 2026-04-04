# Alternative 11-Step Corporate Owner Verification Process

**Created:** 2026-04-03
**Context:** Derived from the Lyon / Hill Valley / Bedrock investigation during the New Door & New Logo Reconciliation. The standard linear methodology failed to connect three CMS chains operating as one corporate family. This two-pass approach discovered what the linear approach could not.

**Companion documents:**
- `DB_Verification_Procedures.md` — original 8-step reconciliation + dedup procedures
- `Vault/05_Board_and_Leadership/NB_LOB_Report_March_2026/Verification_Methodology.html` — Compendium (linear 11-step)
- `MUO_Corporate_History.md` — Lyon/Hill Valley/Bedrock entry (full evidence chain)

---

## Why an Alternative Process

The standard 11-step process is linear: CMS → ProPublica → NIC MAP → NPI → investigate → website → state registry → DB cross-reference → classify → document. It works well when:

- The facility has a single, clearly identified operator
- CMS chain data matches the DB
- Sources agree or have minor name variants

It breaks down when:

- One ownership family operates under multiple CMS chain IDs
- The connection between chains is not visible in any single structured source
- Web research reveals names that make structured data meaningful retroactively

The Lyon / Hill Valley / Bedrock case exposed this gap. Three separate CMS chains (270, 837, 73), three separate brands, three separate geographies — but one family (Chopp) controlling all of them. No single structured lookup would have revealed this. The connection required web research that fed back into CMS ownership filings.

---

## The Two-Pass Structure

### Pass 1 — Structured Lookups (What do the databases say?)

The goal of Pass 1 is to collect every structured data point available. You are not trying to reach a conclusion yet. You are building an inventory of names, chain IDs, LLCs, and ownership percentages.

**Step 1. Identify the facility.**
Match across Monday.com, Finance, GLR, and the Forward Universe. Confirm by address and CCN. Note every name variant across sources.

**Step 2. Pull CMS Provider Info.**
Record CCN, legal business name, ownership type, chain name, chain ID, CHOW flag. If chain name is blank, note it — that's a signal, not an answer.

**Step 3. Pull ProPublica ownership.**
Record every direct owner (with %), every indirect owner, every managing entity, every managing employee, and their dates. Note the LLC names — they become search terms for Pass 2.

**Step 4. Check NIC MAP.**
Search by facility name or address. Record Operator Name (col 41) and Owner Name (col 18). Note whether operator is self-referencing, unknown, stale, or current. For ALFs this is the starting point; for SNFs it's supplemental.

**Step 5. Check NPI Registry.**
Record organization name and authorized official. The authorized official's name becomes a search term for Pass 2 (LinkedIn, web).

**Step 6. Cross-reference the Forward Universe.**
Query all facilities under the identified corporate name. Count total and served. Check whether the corporate name in the DB matches what CMS/ProPublica say. Note any entity fragmentation (same owner, different DB names).

**At the end of Pass 1 you have:** A set of names, chain IDs, LLCs, individuals, and counts. You may have conflicting information. You may have three different names for what might be one entity. That's normal. Pass 2 resolves it.

---

### Pass 2 — Investigative (What's behind the names?)

The goal of Pass 2 is to connect the dots that structured data cannot. You are using web research, corporate websites, REIT filings, news, and court records to answer: are these separate entities, or one family?

**Step 7. Check operator websites and HTML metadata.**
Go to every website identified in Pass 1. Check:
- Does the facility list match what CMS says?
- Who is in the footer? ("Serviced by X", copyright notice)
- View page source — what does the HTML metadata say? (Schema publisher, og:site_name, title tags)
- Check logo file names (right-click → inspect element → image source URL)
- Are multiple websites built on the same template? (Same WordPress theme, same Elementor layouts, same copy)

**Step 8. Check REIT and real estate filings.**
If the facility is leased (most SNFs are), identify the REIT or landlord. Check their portfolio page — REITs list the **operator/tenant** name, which may differ from the CMS chain. Strawberry Fields, Sabra, CareTrust, Welltower, Omega, and NHI all publish portfolio pages.

**Step 9. Search industry news, court filings, investigative journalism.**
Search Senior Housing News, McKnight's, Skilled Nursing News, The Real Deal, local news, and court record databases for:
- Every individual name from ProPublica ownership filings
- Every LLC name from CMS
- Every chain brand name
- Combine names: "Chopp + healthcare", "Lyon + Hill Valley", etc.

This is where lawsuits, receiverships, acquisitions, and corporate connections surface that no structured database contains.

**Step 10. Return to structured sources with new names.**
This is the critical step that the linear process misses. Take every new name, LLC, or individual discovered in Steps 7-9 and search them back through:
- CMS ownership filings (do these names appear on OTHER facilities?)
- ProPublica (do these individuals own other chains?)
- Forward Universe (are these LLCs coded as corporate names elsewhere in the DB?)

This feedback loop is what connected Lyon → Hill Valley → Bedrock. Web research gave us the Chopp family names. Searching those names back through CMS ownership filings revealed they appeared on all three chains.

**Step 11. Apply classification and document.**
Using the complete picture from both passes:
- Do we serve this specific facility? → Integration
- Do we serve any facility under this verified corporate owner OR any entity in the same corporate family? → New Door
- Neither? → New Logo

Document every source checked, what it returned, where sources agree and disagree, the corporate family map if applicable, and the final classification with confidence level.

---

## Case Study: Lyon Healthcare / Hill Valley Healthcare / Bedrock Healthcare

### The Problem

Two facilities in the Q1 reconciliation — Green Meadows (Mount Washington, KY) and Elkhorn (Elkhorn City, KY) — had three different corporate names across sources:

| Source | Green Meadows | Elkhorn |
|---|---|---|
| Finance | Hill Valley Healthcare | Hill Valley Healthcare |
| GLR | Lyon Healthcare | A&M Healthcare Investment LLC |
| DB V25.6 | Lyon Healthcare | A&M Healthcare Investment LLC |
| CMS chain | Bedrock Healthcare (Chain 73) | Lyon Healthcare (Chain 837) |
| CMS affiliate | Lyon Healthcare | — |

Three chain IDs (73, 270, 837). Three brand names. Are they connected or coincidental?

### Pass 1 Results

| Step | Green Meadows | Elkhorn |
|---|---|---|
| CMS | Chain = Bedrock Healthcare (73), affiliate = Lyon Healthcare | Chain = Lyon Healthcare (837), legal name "Not Available" |
| ProPublica | Ownership not disclosed | Ownership not disclosed |
| NIC MAP | Not found | Not found |
| NPI | (not searched at this stage) | (not searched at this stage) |
| DB | Lyon Healthcare, 9 facs, 3 served | A&M Healthcare Investment LLC, 1 fac, 0 served |

**Pass 1 conclusion:** Ambiguous. Lyon and Bedrock are two different CMS chains. Both facilities refused ownership disclosure. A&M Healthcare is a single-facility LLC (likely PropCo). The Lyon affiliate connection on Green Meadows is a signal but not proof.

Under the linear process, this would have been classified as MEDIUM confidence New Door (Lyon, 3 served) and moved on.

### Pass 2 Results

**Step 7 — Websites:**
- lyonhc.com HTML metadata: publisher = "Hill Valley Healthcare." Lyon's site was built under Hill Valley's identity.
- Parkwood (Lyon chain facility) logo file: "HVH_lyon_parkwood_web_logo.png" — HVH = Hill Valley Healthcare.
- hillvalleyhc.com: identical WordPress/Elementor template, near-identical copy to lyonhc.com.
- bedrockhcs.com/our-team/: Sol Chopp (CDO), Kenny Nichols (COO).
- Facility sites (greenmeadowshr.com, chestnutridgehr.com, parkwoodhr.com): footer says "Serviced by Lyon Healthcare."

**Step 8 — REIT:**
- Strawberry Fields REIT portfolio page lists **Hill Valley Healthcare** as operator/tenant for 11 Kentucky properties — the same facilities CMS shows under Lyon Healthcare Chain 837.

**Step 9 — News and court filings:**
- Hill Valley Healthcare acquisition history: $35.25M Woodland CCRC (VA, 2022), $50M TLC Care Center (NV, 2022), Riverside VA facilities (2021), Cortland Acres WV (2024). Co-CEOs: Shimmy Idels, Steven Schwartz.
- Bedrock Wisconsin receivership (Jul 2025): 4 facilities, 384 deficiencies, $2.6M+ owed.
- GPH v. Chopp lawsuit (May 2025): names Lynn, Martin, Pnina, Rachel, Sarah, Solomon Chopp.
- Nussbaum v. Chopp (Feb 2026): $6.3M claim, $1M linked to Opal Healthcare WI — "a nursing home venture in Wisconsin controlled by [Tzali] Chopp."
- Bacon's Rebellion: investigative series on Hill Valley's Virginia nursing home acquisitions.

**Step 10 — Return to structured sources:**
Armed with "Chopp" as the family name:
- CMS ownership filings for Green Meadows (185464): owners = Abraham Chopp, Lynn Chopp, Martin Chopp, Pnina Chopp, Rachel Chopp, Kenneth Nichols. Chain = Lyon (837).
- CMS ownership filings for Indigo Manor FL (105570): owners = Martin Chopp, Pnina Chopp, Solomon Chopp. Chain = Bedrock (73).
- CMS ownership filings for Hill Valley chain (270): 37-38 facilities held through Lion 26 Holdings LLC, Sabrina 1818 Holdings LLC, Saessy Irrevocable Trust, Tatiriq Irrevocable Trust — Chopp family vehicles.
- MC Capital = Martin Chopp, SC Capital = Solomon Chopp, TC Capital = Tzali Chopp.

**The Chopp family name appeared on ownership filings across all three CMS chains.** This is the proof that the linear process could not produce — because you need the family name first, and the family name only surfaces through web/news research.

### Pass 2 Conclusion

Lyon Healthcare, Hill Valley Healthcare, and Bedrock Healthcare are one corporate family controlled by the Chopp family (Tzali/Martin, Pnina, Solomon). Combined footprint: ~59 facilities. We serve 3 under Lyon. Both Green Meadows and Elkhorn are **New Door, HIGH confidence**.

### What the Linear Process Would Have Concluded

MEDIUM confidence New Door based on Lyon affiliation alone. The Hill Valley and Bedrock connections, the Chopp family ownership, the 59-facility combined footprint, and the risk factors (receivership, lawsuits) would have remained undiscovered.

---

## When to Use Each Process

| Scenario | Use |
|---|---|
| Sources agree, single chain, no ambiguity | Linear 11-step (faster) |
| Sources disagree on corporate name | Alternative two-pass (dig deeper) |
| Ownership undisclosed to CMS/ProPublica | Alternative two-pass (web fills the gap) |
| Multiple chain IDs appear for related facilities | Alternative two-pass (look for shared ownership) |
| Independent/null in DB | Alternative two-pass (verify it's truly independent) |
| Facility has LLC as corporate name | Alternative two-pass (LLC is probably PropCo, not operator) |

The linear process is the default. The two-pass process is the escalation when something doesn't add up.
