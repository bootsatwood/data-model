# Developer's Notebook

> A complete reference for how data and code move through the Eventus BD/Market Intel
> ecosystem. Written for a non-developer audience. Each chapter covers one lifecycle.

---

## Table of Contents

- **Chapter 1:** The Database Change Lifecycle — how facility data gets researched, verified, and applied
- **Chapter 2:** The Keystone Platform — how the application works and how code gets to production
- **Chapter 3:** The Database Architecture — why three databases, what each does, and how data flows between them
- **Chapter 4:** The Monday.com Pipeline Sync — how pipeline data gets pulled, snapshotted, and tracked
- **Chapter 5:** The Monday.com MCP Connection — Claude's direct line to Monday.com boards
- **Chapter 6:** The Keystone Modules — what's built, who uses it, and where the data comes from
- **Appendix A:** Glossary — every term defined in this notebook, alphabetized

---

```
══════════════════════════════════════════════════════════════════════
  CHAPTER 1: THE DATABASE CHANGE LIFECYCLE
══════════════════════════════════════════════════════════════════════

  How facility data gets researched, verified, scripted, executed,
  loaded downstream, and backed up.

  Enhanced from the original "From Excel to Forward Universe"
  diagram (2026-04).


  PHASE 1: THE 11-STEP VERIFICATION
  (Procedure 3 — Operator Attribution, Source Sequence)
  ─────────────────────────────────────────────────────────────────

  INTERNAL — know what you already know:

    Step 1   Forward Universe        What does our DB currently say?
                                     Corporate_Name, facility count,
                                     served count, name variants

    Step 2   GLR Export              What does the GLR carry as
                                     Parent Company? (served facs only)

    Step 3   MUO Corporate History   Have we researched this entity
                                     before? What did we find?

    Step 4   Operator Research Log   Already fully verified? Apply
                                     established attribution.

       ⚠  Internal agreement is NOT validation.
          McCoy Memorial: DB + GLR + Finance all agreed on
          "Concierge Healthcare" — an entity that doesn't exist.

  AUTHORITATIVE STRUCTURED SOURCES:

    Step 5   CMS Provider Info       CCN, legal business name,
             (SNFs only)             chain name/ID, ownership type,
                                     CHOW flag

    Step 6   ProPublica              Direct/indirect owners with %,
             Nursing Home Inspect    managing entity + dates.
                                     More granular than CMS chain.
                                     ⚠ Managing entity is often a
                                     facility-level LLC — resolve
                                     to parent brand via website.

    Step 7   NIC MAP                 Owner Name = PropCo (NEVER the
                                     operator). Operator Name =
                                     management company candidate.
                                     Export: Nov 17 2025 — stale
                                     after any CHOW since then.

    Step 8   State Registry          License holder, licensed admin.
             (KY CHFS, IN QAMIS,     THE ONLY authority for ALFs.
              NC DHSR, SC DHEC)

    Step 9   NPI Registry            Authorized official name/title
                                     → LinkedIn → employer reveals
                                     the operating company

  EXTERNAL WEB — mandatory, not optional:

    Step 10  Operator Website        Go to the website. Check:
                                     • Footer ("Serviced by [Brand]")
                                     • Portfolio/locations page
                                     • HTML source (og:site_name)
                                     • Logo file names
                                     • Shared templates across sites

    Step 11  News / Journalism       McKnight's, Senior Housing News,
                                     PESP reports, court records,
                                     local news. Search by operator
                                     name AND individual owner names.

  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  ESCALATION: If sources conflict or refuse disclosure →
  Two-Pass Investigative Approach (Pass 1: structured,
  Pass 2: web research, then FEED NEW NAMES BACK into Pass 1)

  EVIDENCE STANDARD:
    • 2-source minimum for any attribution change
    • HIGH = 3+ sources, no contradictions
    • MEDIUM = 2 sources or 3 with minor discrepancies
    • LOW = 1 source or contradictions — do NOT act
    • NEVER bulk-recode — verify per-facility (V25.2 lesson)

  ─────────────────────────────────────────────────────────────────
  OUTPUT OF PHASE 1:

  Every verified finding becomes one of:
    • RECODE       change a value (corp name, ownership type, etc.)
    • DELETE       remove a row (duplicate, phantom, closed)
    • INSERT       add a missing facility
    • BEDS UPDATE  fix bed count (census vs. licensed)

  Logged CONCURRENTLY (not after) to:
    ┌──────────────────────────────────────────────────────────┐
    │  dedup_decisions_log.csv    ← recode/delete decisions    │
    │  glr_change_log.csv        ← GLR discrepancies           │
    │  MUO_Corporate_History.md  ← corporate intel (M&A, etc.) │
    │  pending_followups.csv     ← can't resolve yet           │
    │  propco_llc_inventory.md   ← LLC → true operator maps    │
    │  operator_research_log.md  ← fully verified entities     │
    └──────────────────────────────────────────────────────────┘


  PHASE 2: SCRIPT & DRY RUN
  ─────────────────────────────────────────────────────────────────

  All verified findings get baked into a migration script:

  ┌─────────────────────┐     v26_1_migration.py      ┌─────────────────────┐
  │                     │     (dry_run = True)         │                     │
  │  Excel (V26.0)      │ ──────────────────────────►  │  CHANGE REPORT      │
  │  25,497 rows        │     READS ONLY               │  (v26_1_report.csv) │
  │                     │     WRITES NOTHING            │                     │
  └─────────────────────┘                              └────────┬────────────┘
                                                                │
                                                                ▼
                                                       Roian reviews report
                                                       "Does this look right?"


  PHASE 3: EXECUTE
  ─────────────────────────────────────────────────────────────────

  ┌─────────────────────┐     v26_1_migration.py      ┌─────────────────────┐
  │                     │     (dry_run = False)        │                     │
  │  Excel (V26.0)      │ ──────────────────────────►  │  Excel (V26.1)      │
  │  25,497 rows        │     APPLIES CHANGES          │  new row count      │
  │  (UNTOUCHED)        │                              │  (new file)         │
  └─────────────────────┘                              └────────┬────────────┘
                                                                │
          V26.0 stays. You can always go back.                  │
                                                                │

  PHASE 4: LOAD DOWNSTREAM
  ─────────────────────────────────────────────────────────────  │
                                                                │
                                                                ▼
                                                       load_vXX_to_pg.py
                                                                │
                                                                ▼
                                                       PostgreSQL (bd schema)
                                                                │
                                                                ▼
                                                       Keystone (dashboards)
                                                                │
                                                                ▼
                                                       Monday.com (downstream)


  PHASE 5: BACKUP TO GITHUB
  ─────────────────────────────────────────────────────────────────

  git commit  →  snapshot the scripts, logs, research
  git push    →  backed up to github.com/bootsatwood/data-model

  What gets committed:   migration scripts, decision logs,
                         corporate history, audit reports
  What does NOT:         Excel files (too large — live in Vault)


══════════════════════════════════════════════════════════════════════
                         WHERE THINGS LIVE
══════════════════════════════════════════════════════════════════════

  Vault (OneDrive)          │  data-model (Git)         │  GitHub
  ──────────────────────────│───────────────────────────│──────────────
  Excel DB files            │  Migration scripts        │  Cloud backup
  V26.0, V26.1, etc.        │  Decision logs (CSV)      │  of everything
  THE source of truth       │  Procedures               │  in data-model
  for facility data         │  Corporate history        │
                            │  Audit reports (HTML)     │

  Excel is upstream.  PG is downstream.  Python is the pipe.
  OneDrive protects the data.  GitHub protects the work.

══════════════════════════════════════════════════════════════════════
                      THE PROBLEM THIS CREATES
══════════════════════════════════════════════════════════════════════

  - Every version change requires a MANUAL PG reload
  - No automated sync — fix Excel, forget to reload,
    PG/Keystone show stale data
  - "Scoring architecture" decision (PG = SOT → Keystone →
    Monday.com) is the INTENDED future state, but Excel is
    still king today
  - Scripts folder: 120+ files, many one-off, hard to tell
    current vs. old

══════════════════════════════════════════════════════════════════════




══════════════════════════════════════════════════════════════════════
  CHAPTER 2: THE KEYSTONE PLATFORM
══════════════════════════════════════════════════════════════════════

  How the application works, how code gets from your laptop to
  production, and where everything lives in Azure.


WHAT IS KEYSTONE
──────────────────────────────────────────────────────────────────────

  Keystone is the internal web application that Eventus employees
  use to view dashboards, manage clinical data, run reports, and
  (increasingly) manage BD/market intelligence.

  When someone opens equip.eventuswh.com in a browser, they are
  using Keystone.

  It is not one program. It is TWO programs that work together:

    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │  FRONTEND          The part you SEE.                        │
    │  (React)           Pages, buttons, charts, tables, forms.   │
    │                    Runs inside the user's web browser.      │
    │                    Built with React — a JavaScript          │
    │                    FRAMEWORK (a pre-built toolkit that      │
    │                    gives you building blocks for making     │
    │                    interactive web pages).                  │
    │                                                             │
    ├─────────────────────────────────────────────────────────────┤
    │                                                             │
    │  BACKEND           The part you DON'T see.                  │
    │  (FastAPI)         Fetches data, checks permissions,        │
    │                    runs calculations, talks to databases.   │
    │                    Runs on a server — always on, waiting.   │
    │                    Built with FastAPI — a Python            │
    │                    FRAMEWORK for building APIs.             │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘

  TERM: API (Application Programming Interface)
  ─────────────────────────────────────────────
  An API is a set of URLs that a program can call to get data
  or trigger actions. When the frontend needs pipeline numbers,
  it doesn't query a database — it calls a backend URL like
  /api/business-development/pipeline/summary and gets back
  structured data (JSON). Think of it as a waiter: you don't
  go to the kitchen, you ask the waiter, the waiter brings
  your food.

  TERM: JSON (JavaScript Object Notation)
  ────────────────────────────────────────
  The format the backend sends data in. It's just structured
  text that both programs can read:

    { "total_ar": 10060000, "facility_count": 112,
      "stage": "Contracting" }

  Every chart, every number, every table you see in Keystone
  started as JSON that the backend sent to the frontend.


══════════════════════════════════════════════════════════════════════
                       THE THREE LAYERS
══════════════════════════════════════════════════════════════════════

  Keystone exists in three layers. Each layer is a different
  ENVIRONMENT — meaning a different place the same code runs,
  with different rules.

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  LAYER 1: DEVELOPMENT                                      │
  │  (Your laptop)                                              │
  │                                                             │
  │  WHO:     You (and Josh, on his machine)                    │
  │  WHERE:   ~/keystone-platform/ folder                       │
  │  PURPOSE: Build and test changes before anyone else sees    │
  │           them. Break things safely.                        │
  │  ACCESS:  Only you. No login required (auth is bypassed).   │
  │                                                             │
  │  You run two commands in two PowerShell windows:            │
  │                                                             │
  │    Window 1 (backend):                                      │
  │    cd ~/keystone-platform/backend                           │
  │    .\venv\Scripts\python.exe -m uvicorn app.main:app \      │
  │        --port 8000 --workers 2                              │
  │                                                             │
  │    Window 2 (frontend):                                     │
  │    cd ~/keystone-platform/frontend                          │
  │    npm run dev                                              │
  │                                                             │
  │  TERM: uvicorn                                              │
  │  ──────────────────                                         │
  │  The program that RUNS the FastAPI backend. FastAPI is the  │
  │  code you wrote; uvicorn is the engine that serves it.      │
  │  Like how a .py file is your script, but python.exe is      │
  │  what actually executes it.                                 │
  │                                                             │
  │  TERM: npm run dev                                          │
  │  ──────────────────                                         │
  │  Starts a local web server for the frontend. npm is the     │
  │  package manager for JavaScript (like pip for Python).      │
  │  "run dev" means "start in development mode" — it watches   │
  │  for file changes and refreshes the browser automatically.  │
  │                                                             │
  │  TERM: venv (Virtual Environment)                           │
  │  ──────────────────                                         │
  │  An isolated Python installation inside the project folder. │
  │  It has its own copy of every library the backend needs     │
  │  (FastAPI, psycopg2, etc.) so they don't conflict with      │
  │  anything else on your machine.                             │
  │                                                             │
  │  RESULT:                                                    │
  │    Frontend → http://localhost:3000 (or 3001, 3002...)      │
  │    Backend  → http://127.0.0.1:8000                         │
  │    Open the frontend URL in your browser. You're running    │
  │    Keystone.                                                │
  │                                                             │
  │  GOTCHAS (Windows-specific):                                │
  │    • --workers 2 is required — single worker freezes        │
  │    • Use 127.0.0.1 not localhost (IPv6 mismatch)            │
  │    • Kill zombie python.exe processes before restarting     │
  │    • Frontend port creeps up if old Node processes linger   │
  │                                                             │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  LAYER 2: PRODUCTION                                        │
  │  (Azure cloud — what everyone else uses)                    │
  │                                                             │
  │  WHO:     All Eventus employees with Azure AD login         │
  │  WHERE:   Microsoft Azure (cloud servers)                   │
  │  PURPOSE: The real thing. Live data, real logins,           │
  │           real dashboards.                                  │
  │  ACCESS:  Azure AD Single Sign-On (SSO) — same credentials │
  │           as Outlook, Teams, etc.                           │
  │                                                             │
  │  TERM: Azure                                                │
  │  ──────────────────                                         │
  │  Microsoft's cloud platform. Instead of running Keystone    │
  │  on a physical server in an office, it runs on Microsoft's  │
  │  computers somewhere in a data center. You rent the         │
  │  compute, storage, and networking by the hour.              │
  │                                                             │
  │  TERM: Azure AD / SSO                                       │
  │  ──────────────────                                         │
  │  Azure Active Directory — the system that manages who can   │
  │  log in to Eventus systems. SSO (Single Sign-On) means     │
  │  one login works everywhere: Outlook, Teams, Keystone.      │
  │  When Keystone asks "who are you?", it sends you to         │
  │  Microsoft's login page, Microsoft confirms your identity,  │
  │  and sends you back.                                        │
  │                                                             │
  │  Production runs on TWO separate Azure services:            │
  │                                                             │
  │  ┌──────────────────────────────────────────────────────┐   │
  │  │  Azure Static Web Apps         (Frontend)            │   │
  │  │  salmon-coast-020c9bc0f.3.azurestaticapps.net        │   │
  │  │                                                      │   │
  │  │  This is a FILE HOST. When your browser requests     │   │
  │  │  the Keystone URL, Azure sends it the React files    │   │
  │  │  (HTML, JavaScript, CSS). Your browser downloads     │   │
  │  │  them and runs the frontend locally — in your        │   │
  │  │  browser. Azure Static Web Apps doesn't "run" the    │   │
  │  │  frontend. It just serves the files. Your browser    │   │
  │  │  does the work.                                      │   │
  │  │                                                      │   │
  │  │  Think of it like downloading an app from an app     │   │
  │  │  store — the store doesn't run the app, your phone   │   │
  │  │  does. Except here, the "app" is a website and the   │   │
  │  │  "phone" is your browser.                            │   │
  │  └──────────────────────────────────────────────────────┘   │
  │                                                             │
  │  ┌──────────────────────────────────────────────────────┐   │
  │  │  Azure App Service             (Backend)             │   │
  │  │  keystone-platform.azurewebsites.net                 │   │
  │  │                                                      │   │
  │  │  This IS a running program. It's a server that is    │   │
  │  │  always on, always listening. When the frontend      │   │
  │  │  (running in your browser) needs data, it sends an   │   │
  │  │  HTTP request to this URL. The backend processes     │   │
  │  │  the request, queries databases, and sends JSON      │   │
  │  │  back.                                               │   │
  │  │                                                      │   │
  │  │  This is the equivalent of you running uvicorn on    │   │
  │  │  your laptop — except Azure runs it 24/7, and it     │   │
  │  │  requires real login credentials.                    │   │
  │  └──────────────────────────────────────────────────────┘   │
  │                                                             │
  │  THE CONVERSATION IN PRODUCTION:                             │
  │                                                             │
  │  User opens         Azure Static       Azure App Service    │
  │  equip.eventuswh    Web Apps            (Backend)            │
  │  .com               (Frontend files)                        │
  │    │                    │                    │               │
  │    │── GET page ──────►│                    │               │
  │    │◄── HTML/JS/CSS ──│                    │               │
  │    │                    │                    │               │
  │    │  (browser now runs the React app)      │               │
  │    │                                         │               │
  │    │── "who am I?" ─────────────────────────►│               │
  │    │◄── redirect to Microsoft login ────────│               │
  │    │── (user logs in with Eventus creds) ──►│               │
  │    │◄── "you're ratwood, role: Admin" ──────│               │
  │    │                                         │               │
  │    │── "give me pipeline summary" ──────────►│               │
  │    │                    │                    │── query PG    │
  │    │                    │                    │◄─ results     │
  │    │◄── { total_ar: 10060000, ... } ────────│               │
  │    │                                         │               │
  │    │  (browser renders charts from JSON)     │               │
  │                                                             │
  │  IMPORTANT: The frontend and backend are on DIFFERENT        │
  │  DOMAINS (azurestaticapps.net vs azurewebsites.net).        │
  │  This is called CROSS-ORIGIN and it creates complications   │
  │  with cookies and security. You don't need to understand    │
  │  the details, but it's why auth bugs are tricky and why     │
  │  the backend has special CORS configuration.                │
  │                                                             │
  │  TERM: CORS (Cross-Origin Resource Sharing)                 │
  │  ──────────────────                                         │
  │  A browser security rule: by default, a webpage on one      │
  │  domain cannot talk to a server on a different domain.      │
  │  CORS is the mechanism that says "it's OK, the backend      │
  │  on azurewebsites.net trusts requests from the frontend     │
  │  on azurestaticapps.net." Without it, every API call        │
  │  would be blocked by the browser.                           │
  │                                                             │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  LAYER 3: DATABASES                                         │
  │  (Where the actual data lives)                              │
  │                                                             │
  │  Keystone talks to TWO completely separate databases.       │
  │  They serve different purposes and have nothing to do       │
  │  with each other.                                           │
  │                                                             │
  │  ┌──────────────────────────────────────────────────────┐   │
  │  │  DATABASE A: PostgreSQL (Azure Database for PG)      │   │
  │  │  keystone-platform-postgres.postgres.database.azure  │   │
  │  │  .com                                                │   │
  │  │                                                      │   │
  │  │  WHAT'S IN IT:                                       │   │
  │  │    bd schema — YOUR data. Market intel facilities    │   │
  │  │    (25,497 rows), corporate entities (3,988),        │   │
  │  │    metros, expansion states, pipeline snapshots.     │   │
  │  │                                                      │   │
  │  │  WHO FEEDS IT:                                       │   │
  │  │    You. Via Python load scripts                      │   │
  │  │    (load_v26_to_pg.py, load_scoring_to_pg.py)       │   │
  │  │    Excel → Python → PostgreSQL                       │   │
  │  │                                                      │   │
  │  │  WHO READS IT:                                       │   │
  │  │    Keystone backend — BD Pipeline Dashboard,         │   │
  │  │    MUO Universe, Market Intel views, Data            │   │
  │  │    Governance module                                 │   │
  │  │                                                      │   │
  │  │  ALSO STORES:                                        │   │
  │  │    keystone schema — feedback, app config            │   │
  │  │    glr schema — GLR form data                        │   │
  │  │    pims schema — PIMs data                           │   │
  │  │                                                      │   │
  │  │  WHO MANAGES IT:                                     │   │
  │  │    Josh provisioned it. You have your own user       │   │
  │  │    (ratwood) with table creation rights in bd        │   │
  │  │    schema.                                           │   │
  │  └──────────────────────────────────────────────────────┘   │
  │                                                             │
  │  ┌──────────────────────────────────────────────────────┐   │
  │  │  DATABASE B: Azure SQL Server                        │   │
  │  │  asqls-ewh-apps-dev-01.database.windows.net          │   │
  │  │                                                      │   │
  │  │  WHAT'S IN IT:                                       │   │
  │  │    Clinical / EQuIP data. Clinician performance,     │   │
  │  │    patient measures, ACO scheduling, pharmacy,       │   │
  │  │    HR onboarding — everything that is NOT your       │   │
  │  │    BD/market intel work.                             │   │
  │  │                                                      │   │
  │  │  WHO FEEDS IT:                                       │   │
  │  │    Upstream clinical systems (ChartPath, UKG,        │   │
  │  │    Synapse) via automated pipelines that Josh and    │   │
  │  │    the data team manage.                             │   │
  │  │                                                      │   │
  │  │  WHO READS IT:                                       │   │
  │  │    Keystone backend — EQuIP dashboards, Charta,      │   │
  │  │    Prior Auth, Employee Physicals, ACO views         │   │
  │  │                                                      │   │
  │  │  YOUR INTERACTION:                                   │   │
  │  │    Minimal. You don't load data here, don't manage   │   │
  │  │    it, rarely query it. It's Josh's world.           │   │
  │  │    One legacy script exists:                         │   │
  │  │    reports/scripts/load_v23_to_sql.py (superseded)   │   │
  │  └──────────────────────────────────────────────────────┘   │
  │                                                             │
  │  HOW THE BACKEND KNOWS WHICH DATABASE TO USE:               │
  │                                                             │
  │    The backend has two database CLIENTS (connector           │
  │    libraries):                                              │
  │                                                             │
  │    PgClient  → talks to PostgreSQL  → uses %s placeholders  │
  │    SqlClient → talks to Azure SQL   → uses ? placeholders   │
  │                                                             │
  │    Each API ROUTE (a URL endpoint like /api/pipeline/...)   │
  │    knows which client to use. BD routes use PgClient.       │
  │    EQuIP routes use SqlClient. They never cross.            │
  │                                                             │
  │    Config is in: backend/app/config.py                      │
  │    Connection credentials come from Azure Key Vault in      │
  │    production, from .env files in development.              │
  │                                                             │
  │  TERM: Key Vault                                            │
  │  ──────────────────                                         │
  │  Azure's password manager for servers. Instead of putting   │
  │  database passwords in code (dangerous), the backend asks   │
  │  Key Vault "what's the PG password?" at startup. Only the   │
  │  backend has permission to ask.                             │
  │                                                             │
  │  THE FULL PICTURE:                                           │
  │                                                             │
  │  ┌──────────┐    ┌───────────────┐    ┌─────────────────┐   │
  │  │ Browser  │───►│ Backend       │───►│ PostgreSQL      │   │
  │  │ (React)  │◄───│ (FastAPI)     │◄───│ (BD data)       │   │
  │  │          │    │               │    └─────────────────┘   │
  │  │          │    │               │    ┌─────────────────┐   │
  │  │          │    │               │───►│ Azure SQL       │   │
  │  │          │    │               │◄───│ (Clinical data) │   │
  │  └──────────┘    └───────────────┘    └─────────────────┘   │
  │                                                             │
  │  Both your laptop AND production use this same pattern.     │
  │  The only difference: your laptop points to the same        │
  │  databases using .env files; production uses Key Vault.     │
  │                                                             │
  │  ⚠  THERE IS NO SEPARATE DEV DATABASE.                     │
  │     When you run Keystone locally and see 25,497            │
  │     facilities, that's the REAL production data.            │
  │     If you ran a DELETE query from your laptop,             │
  │     it would delete real data. Be careful.                  │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘


══════════════════════════════════════════════════════════════════════
            HOW CODE GETS FROM YOUR LAPTOP TO PRODUCTION
══════════════════════════════════════════════════════════════════════

  TERM: Git / GitHub
  ──────────────────
  Git is version control — it tracks every change to every
  file, who made it, and when. Like "Track Changes" in Word
  but for code, and it never forgets.

  GitHub is where the Git history lives in the cloud.
  The Keystone repo is at:
  github.com/Eventus-Whole-Health/keystone-platform

  TERM: Branch
  ──────────────────
  A parallel copy of the codebase where you can make changes
  without affecting the "real" version. Like duplicating a
  spreadsheet tab to try something, then merging your changes
  back when you're happy.

  The "real" version is called MAIN.

  TERM: Commit
  ──────────────────
  A saved snapshot of your changes with a message describing
  what you did. Like clicking "Save" but with a note attached:

    feat(market-intel): add facilities table
    fix(pipeline): L2 defaults to Monthly view

  Commits are permanent. You can always go back.

  TERM: Pull Request (PR)
  ──────────────────
  A formal request to merge your branch into main. It shows
  everyone exactly what changed, lets reviewers comment, and
  runs automated checks. Josh must approve before it merges.

  ─────────────────────────────────────────────────────────────────

  THE FULL DEPLOYMENT LIFECYCLE — STEP BY STEP

  PHASE 1: LOCAL DEVELOPMENT
  ─────────────────────────────────────────────────────────────────

    You're on your laptop, working in ~/keystone-platform/.

    You create a BRANCH (or already have one):

      git checkout -b feature/bd-dashboard-refinements

    Your current branch:
      feature/bd-dashboard-refinements    (YOUR branch)
          ↑
          branched from: main             (the "real" version)

    You edit files. You run Keystone locally. You test.
    You make COMMITS as you go:

      git add frontend/src/views/business-development/...
      git commit -m "feat(bd): add pipeline stage flow card"

    Each commit is a checkpoint you can return to.


  PHASE 2: PUSH TO GITHUB
  ─────────────────────────────────────────────────────────────────

    When you're ready for others to see your work:

      git push origin feature/bd-dashboard-refinements

    TERM: origin
    ──────────────────
    A shorthand for "the GitHub copy of this repo." Your laptop
    has a local copy; origin is the cloud copy. Push sends your
    commits from local → cloud.

    ┌──────────────┐   git push    ┌──────────────────────────┐
    │ Your laptop  │──────────────►│ GitHub                   │
    │ (local repo) │               │ Eventus-Whole-Health/    │
    │              │               │ keystone-platform        │
    │ feature/bd-  │               │                          │
    │ dashboard-   │               │ feature/bd-dashboard-    │
    │ refinements  │               │ refinements now visible  │
    └──────────────┘               └──────────────────────────┘


  PHASE 3: OPEN A PULL REQUEST
  ─────────────────────────────────────────────────────────────────

    On GitHub (or via gh CLI), you open a PR:

      "BD Dashboard fixes + Data Governance module (V1)"
      feature/bd-dashboard-refinements → main

    This is currently PR #163 (Draft).

    What a PR shows:
      • Every file changed (red = removed, green = added)
      • Every commit included
      • A description of what and why
      • Comments from reviewers

    TERM: Draft PR
    ──────────────────
    A PR marked as "not ready for review." It still triggers
    preview builds (so you can test), but signals to Josh
    "I'm still working on this — don't merge yet."


  PHASE 4: AUTOMATED PREVIEW (CI/CD)
  ─────────────────────────────────────────────────────────────────

    The moment you open a PR (or push new commits to it),
    GitHub Actions kicks in AUTOMATICALLY.

    TERM: GitHub Actions
    ──────────────────
    A system built into GitHub that runs scripts (called
    WORKFLOWS) when certain things happen — like opening a
    PR or pushing to main. It's a robot that does your
    deployment work.

    TERM: CI/CD
    ──────────────────
    Continuous Integration / Continuous Deployment.
    CI = automatically test code when it changes.
    CD = automatically deploy code when it's approved.
    Together: push code → tests run → deploys if passing.

    What happens when you push to a PR:

    ┌─────────────────────────────────────────────────────────┐
    │  FRONTEND WORKFLOW                                      │
    │  .github/workflows/frontend-deployment.yml              │
    │                                                         │
    │  1. Checks out your branch code                         │
    │  2. Installs JavaScript dependencies (npm ci)           │
    │  3. Builds the React app (npm run build)                │
    │  4. Deploys to a PREVIEW URL unique to your PR:         │
    │                                                         │
    │     salmon-coast-020c9bc0f-163.eastus2.3                │
    │         .azurestaticapps.net                            │
    │                   ↑                                     │
    │              PR number                                  │
    │                                                         │
    │  This preview URL is a REAL running copy of Keystone's  │
    │  frontend with YOUR changes — anyone with the link      │
    │  can see it.                                            │
    └─────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────┐
    │  BACKEND WORKFLOW                                       │
    │  .github/workflows/backend-deployment.yml               │
    │                                                         │
    │  1. Checks if the STAGING SLOT is available             │
    │                                                         │
    │     TERM: Staging Slot                                  │
    │     ──────────────────                                  │
    │     A second copy of the backend server that runs in    │
    │     parallel to production. Only ONE PR can use it at   │
    │     a time — there's a queue system with labels:        │
    │                                                         │
    │       staging:active  = this PR owns the staging slot   │
    │       staging:queued  = waiting for the slot            │
    │                                                         │
    │  2. If staging is free → claim it, deploy your backend  │
    │     code to:                                            │
    │     keystone-platform-staging.azurewebsites.net         │
    │                                                         │
    │  3. If staging is busy → your PR's preview frontend     │
    │     points to the PRODUCTION backend instead            │
    │     (safe for read-only testing)                        │
    │                                                         │
    │  4. Posts a comment on the PR with preview URLs:        │
    │                                                         │
    │     Frontend: salmon-coast-...-163.azurestaticapps.net  │
    │     Backend:  keystone-platform-staging...              │
    │                                                         │
    │  5. When PR is closed/merged → staging slot released,   │
    │     next queued PR auto-promoted                        │
    └─────────────────────────────────────────────────────────┘


  PHASE 5: REVIEW AND MERGE
  ─────────────────────────────────────────────────────────────────

    Josh (or another admin) reviews your PR on GitHub:
      • Reads the code changes (the DIFF)
      • Tests the preview URL
      • Leaves comments or requests changes
      • Approves

    TERM: Diff
    ──────────────────
    The difference between your branch and main. Shows exactly
    what lines were added, removed, or changed. GitHub renders
    this visually — red lines = removed, green = added.

    Once approved, Josh clicks "Merge" (or you do, with
    permission). Your branch's commits become part of MAIN.

    ⚠  PRODUCTION PASSPHRASE: The Keystone repo has a rule —
       no one (including AI) can push directly to main or
       trigger production deploys without the passphrase
       "magnolia." This is a safety gate.


  PHASE 6: AUTOMATIC PRODUCTION DEPLOYMENT
  ─────────────────────────────────────────────────────────────────

    The moment code merges to main, GitHub Actions fires again:

    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │  IF frontend/** files changed:                          │
    │    → Build React app                                    │
    │    → Deploy to Azure Static Web Apps (production)       │
    │    → Live at salmon-coast-020c9bc0f...                  │
    │                                                         │
    │  IF backend/** files changed:                           │
    │    → Package Python app                                 │
    │    → Login to Azure via OIDC (certificate-based, no     │
    │      passwords in the workflow)                         │
    │    → Deploy to Azure App Service (production)           │
    │    → Live at keystone-platform.azurewebsites.net        │
    │                                                         │
    │  Both trigger independently based on which files        │
    │  changed. A frontend-only PR won't redeploy the         │
    │  backend.                                               │
    │                                                         │
    └─────────────────────────────────────────────────────────┘

    TERM: OIDC (OpenID Connect)
    ──────────────────
    A secure way for GitHub Actions to prove to Azure "I am
    the Keystone repo's deployment workflow" without storing
    a password. It uses cryptographic certificates instead.
    This is why you never see Azure passwords in the workflow
    files.

    Within minutes, the changes are live. Anyone opening
    equip.eventuswh.com sees the new version.


  THE FULL PIPELINE — ONE PICTURE:

  ┌──────────┐  push   ┌────────┐  PR    ┌──────────┐
  │ Laptop   │────────►│ GitHub │───────►│ Review   │
  │ (dev)    │         │ branch │        │ (Josh)   │
  └──────────┘         └────────┘        └────┬─────┘
                            │                  │ merge
                       ┌────┴──────┐          ▼
                       │ Preview   │    ┌──────────┐
                       │ (staging) │    │ main     │
                       │ PR-163    │    │ branch   │
                       └───────────┘    └────┬─────┘
                                             │ auto-deploy
                            ┌─────────────────┼────────────────┐
                            ▼                                  ▼
                  ┌──────────────────┐            ┌────────────────────┐
                  │ Azure Static     │            │ Azure App Service  │
                  │ Web Apps         │            │                    │
                  │ (frontend)       │            │ (backend)          │
                  └──────────────────┘            └────────────────────┘
                            │                                  │
                            └──────────┬───────────────────────┘
                                       │ users open browser
                                       ▼
                                equip.eventuswh.com


══════════════════════════════════════════════════════════════════════
                      WHERE THINGS LIVE
══════════════════════════════════════════════════════════════════════

  REPO: keystone-platform
  ──────────────────────────────────────────────────────────────────
  github.com/Eventus-Whole-Health/keystone-platform
  Local: ~/keystone-platform/
  Branch: feature/bd-dashboard-refinements (yours)
  Main branch: main

  Contains BOTH frontend and backend in one repo.

    frontend/           React app (what you see)
    backend/            FastAPI app (data engine)
    .github/workflows/  CI/CD automation
    .claude/            AI agent guides
    .dev_files/         SQL data model, EQuIP schema

  This is Josh's repo. You are a contributor.
  PRs require admin approval to merge.

  Recent PRs (yours):
    #163  BD Dashboard fixes + Data Governance V1    DRAFT
    #155  Pipeline Dashboard — Session 2             MERGED 4/7
    #154  XSS security fix in pipeline report        MERGED 4/7

  REPO: data-model
  ──────────────────────────────────────────────────────────────────
  github.com/bootsatwood/data-model
  Local: ~/data-model/
  Branch: master (only branch)

  YOUR repo. Migration scripts, procedures, audit reports,
  decision logs, corporate history. Everything that feeds
  PostgreSQL.

  REPO: reports
  ──────────────────────────────────────────────────────────────────
  github.com/bootsatwood/reports
  Local: ~/reports/
  Branch: master (only branch)

  YOUR repo. Report compendiums, markdown → HTML pipeline,
  one legacy SQL Server loader (superseded).

  REPO: bd_facility_list
  ──────────────────────────────────────────────────────────────────
  github.com/Eventus-Whole-Health/bd_facility_list
  Local: ~/bd_facility_list/

  Org repo Josh created for BD work. Contains SCHEMA.md
  (the original table design) and archived loader scripts.
  Mostly historical now — active work happens in data-model
  and keystone-platform.


══════════════════════════════════════════════════════════════════════
                 WHO OWNS WHAT
══════════════════════════════════════════════════════════════════════

  JOSH KILPATRICK                      YOU (ROIAN)
  ─────────────────────────            ─────────────────────────
  Keystone platform (infra)            BD/Market Intel data
  Azure provisioning                   PostgreSQL bd schema
  Azure AD app registration            data-model repo (sole owner)
  Backend core (auth, middleware)       reports repo (sole owner)
  EQuIP / clinical features            Forward Universe (Excel)
  CI/CD workflows                      Migration scripts (Python)
  Azure SQL clinical data              Corporate verification
  App Service deployment               Monday.com BD boards
  PR approvals on keystone repo        Keystone BD views (code)
  Production passphrase (magnolia)     Load scripts (Excel → PG)

  Shared:
    PostgreSQL server (Josh provisioned, you use bd schema)
    Keystone frontend (you build BD views, Josh builds clinical)
    GitHub org (Eventus-Whole-Health)


══════════════════════════════════════════════════════════════════════
                 AZURE RESOURCE DIRECTORY
══════════════════════════════════════════════════════════════════════

  Resource Group: rg-keystone-platform

  ┌────────────────────────────────────────────────────────────────┐
  │  SERVICE                    │  URL / IDENTIFIER               │
  ├────────────────────────────────────────────────────────────────┤
  │  Frontend (production)      │  salmon-coast-020c9bc0f.3       │
  │                             │  .azurestaticapps.net           │
  │  Backend (production)       │  keystone-platform              │
  │                             │  .azurewebsites.net             │
  │  Backend (staging)          │  keystone-platform-staging      │
  │                             │  .azurewebsites.net             │
  │  PostgreSQL                 │  keystone-platform-postgres     │
  │                             │  .postgres.database.azure.com   │
  │  Azure SQL                  │  asqls-ewh-apps-dev-01          │
  │                             │  .database.windows.net          │
  │  Azure AD App               │  7d02f10f-a472-4b0a-9113-      │
  │                             │  82c12b2259a9                   │
  │  SEQ (logging)              │  apps-seq-instance.eastus2      │
  │                             │  .azurecontainer.io:5341        │
  └────────────────────────────────────────────────────────────────┘


══════════════════════════════════════════════════════════════════════
                 THE PROBLEMS / GAPS (HONEST)
══════════════════════════════════════════════════════════════════════

  1. NO DEV DATABASE
     Your laptop and production hit the same PostgreSQL.
     A bad query from local dev affects real data.
     Josh's world (Azure SQL) has the same issue.

  2. MANUAL PG RELOAD
     Every Excel version change requires you to run a load
     script manually. Forget to reload → PG/Keystone show
     stale data. No automation exists.

  3. EXCEL IS STILL KING
     The "scoring architecture" decision says PG is SOT,
     but in practice Excel is still the master. PG is a
     downstream copy. The intended future (PG → Keystone
     → Monday.com) is not yet real.

  4. BACKEND DEPLOYMENT BLOCKED
     Pipeline auto-sync (8x/week Monday.com pull) only
     fires when ENVIRONMENT=production. Keystone backend
     is not yet deployed as a hosted service by Josh.
     Until then, no auto-sync.

  5. AUTH PATCHES MAY BE STALE
     PR #128 fixed the root auth bug. Your local auth
     bypasses (AUTH_ENABLED=false, RBAC bypass) may no
     longer be needed. Untested since the fix.

  6. SNOWFLAKE IS FUTURE STATE
     Carey/Jeremy want Snowflake. Migration is assessed
     as low-effort (days not weeks). But no timeline,
     no decision, no Snowflake instance exists yet.
     All BD logic is in Python, not in the database,
     so the swap is mechanical when it happens.

  7. ONE PR AT A TIME FOR STAGING
     Only one PR gets the staging backend slot. Others
     test against production backend. Fine for frontend-
     only changes, limiting for backend work.

══════════════════════════════════════════════════════════════════════




══════════════════════════════════════════════════════════════════════
  CHAPTER 3: THE DATABASE ARCHITECTURE — WHY THREE?
══════════════════════════════════════════════════════════════════════


  FIRST: WHAT IS A DATABASE (THE 30-SECOND VERSION)
  ─────────────────────────────────────────────────────────────────

  A database is a program that stores structured data in tables
  (rows and columns, like Excel) and lets you ask questions
  about it using a language called SQL.

  TERM: SQL (Structured Query Language)
  ──────────────────
  The language you use to talk to a database. You've seen it:

    SELECT facility_name, corporate_name, state
    FROM bd.market_intel_facilities
    WHERE state = 'KY' AND beds > 100

  Every database product speaks SQL, but each has its own
  dialect — like American English vs. British English.
  The basics are the same; the edge cases differ.

  There are many database PRODUCTS — software made by different
  companies. Eventus uses three:


  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  AZURE SQL SERVER                                           │
  │  Made by: Microsoft                                         │
  │  Runs on: Azure cloud                                       │
  │  SQL dialect: T-SQL (Transact-SQL)                          │
  │                                                             │
  │  Think of it as: Excel on steroids, made by Microsoft,      │
  │  lives in the Microsoft cloud. The "enterprise default"     │
  │  — if a company uses Microsoft everything (Outlook, Teams,  │
  │  Azure), SQL Server is usually what IT picks for databases. │
  │                                                             │
  │  At Eventus: This is the CLINICAL database. It was here     │
  │  before you arrived. Josh and the data team built all the   │
  │  EQuIP dashboards, pharmacy workflows, ACO scheduling,      │
  │  and HR onboarding on top of it. Fed by ChartPath, UKG,     │
  │  and Synapse via automated pipelines.                       │
  │                                                             │
  │  Your interaction: Almost none. One legacy script            │
  │  (load_v23_to_sql.py) loaded BD data here once, back        │
  │  before the PostgreSQL pivot. That script is superseded.    │
  │                                                             │
  │  Python connector: pyodbc                                   │
  │  Keystone connector: SqlClient (uses ? placeholders)        │
  │                                                             │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  POSTGRESQL (often called "Postgres" or "PG")               │
  │  Made by: Open source community (free, no vendor)           │
  │  Runs on: Azure cloud (Azure Database for PostgreSQL)       │
  │  SQL dialect: PostgreSQL SQL (very close to standard)       │
  │                                                             │
  │  Think of it as: The database that developers love.         │
  │  Free, powerful, no licensing fees, runs anywhere.          │
  │  Azure just hosts it — PostgreSQL itself isn't a            │
  │  Microsoft product.                                        │
  │                                                             │
  │  At Eventus: This is YOUR database. Josh pivoted to PG      │
  │  for BD data in March 2026 specifically because:            │
  │    • He could control access without asking other admins    │
  │    • Better fit for your use case (simpler types — no       │
  │      BIT/VARCHAR(MAX) mapping needed)                       │
  │    • He could give you your own user (ratwood) with         │
  │      direct table creation rights                          │
  │                                                             │
  │  It was a POLITICAL decision as much as technical.           │
  │  Azure SQL access required going through gatekeepers.       │
  │  PostgreSQL let Josh give you a door of your own.           │
  │                                                             │
  │  Python connector: psycopg2                                 │
  │  Keystone connector: PgClient (uses %s placeholders)        │
  │                                                             │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  SNOWFLAKE                                                  │
  │  Made by: Snowflake Inc. (publicly traded, $SNOW)           │
  │  Runs on: AWS (Amazon), not Azure                           │
  │  SQL dialect: Snowflake SQL (close to standard + extras)    │
  │                                                             │
  │  Think of it as: A data warehouse — built for ANALYTICS,    │
  │  not for running applications. Designed to crunch massive   │
  │  datasets, run complex reports, and serve BI tools like     │
  │  Tableau or Power BI. Not designed to be the backend of a   │
  │  web app.                                                   │
  │                                                             │
  │  TERM: Data Warehouse                                       │
  │  ──────────────────                                         │
  │  A database optimized for reading and analyzing large       │
  │  volumes of data, not for rapid writes or serving a web     │
  │  app. You pour data IN periodically (nightly loads,         │
  │  weekly syncs), then analysts and BI tools query it.        │
  │  Contrast with an APPLICATION database (like PG or SQL      │
  │  Server) that handles thousands of reads AND writes per     │
  │  second from a live web app.                                │
  │                                                             │
  │  At Eventus: Does not exist yet. Carey DeMatteis and        │
  │  Jeremy Hess are advocates. The enterprise analytics        │
  │  vision is that Snowflake becomes the central analytics     │
  │  layer — all data from all systems pours into Snowflake,    │
  │  analysts query it, BI dashboards connect to it.            │
  │                                                             │
  │  No timeline. No instance provisioned. No decision made.    │
  │                                                             │
  │  Python connector: snowflake-connector-python               │
  │  (not currently installed anywhere)                         │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘


  WHY TWO DATABASES TODAY (AND MAYBE THREE TOMORROW)
  ─────────────────────────────────────────────────────────────────

  This is not an architecture anyone designed on a whiteboard.
  It's what happened:

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  TIMELINE                                                   │
  │                                                             │
  │  Before 2026     Josh builds Keystone on Azure SQL.         │
  │                  Clinical data (EQuIP, pharmacy, ACO).      │
  │                  No BD data in any database — Roian's       │
  │                  world lives in Excel on OneDrive.          │
  │                                                             │
  │  Jan-Feb 2026    Roian starts collaborating with Josh.      │
  │                  First attempt: load BD data into Azure     │
  │                  SQL alongside clinical data.               │
  │                  Problem: access requires other admins.     │
  │                  Script written: load_v23_to_sql.py         │
  │                  (pyodbc → Sandbox.bd_ tables).             │
  │                                                             │
  │  Mar 8, 2026     Josh pivots to PostgreSQL.                 │
  │                  Provisions Azure Database for PostgreSQL.   │
  │                  Creates ratwood user, bd schema.            │
  │                  Roian gets direct access.                  │
  │                  load_v23_to_sql.py is now superseded.      │
  │                                                             │
  │  Mar-Apr 2026    Roian builds 12+ Python scripts that      │
  │                  load Excel → PG. BD Pipeline Dashboard,    │
  │                  MUO Universe, Market Intel, Data           │
  │                  Governance module all built on PG data.    │
  │                  Azure SQL untouched by Roian.              │
  │                                                             │
  │  Apr 7, 2026     ARCHITECTURE DECISION:                     │
  │                  PG is source of truth for BD scoring.      │
  │                  Keystone manages it. Monday.com is         │
  │                  downstream. (Not yet fully implemented.)   │
  │                                                             │
  │  Apr 10, 2026    Snowflake migration assessed.              │
  │                  Result: low effort. All logic is in        │
  │                  Python, not in the database. PG is just    │
  │                  storage. If Snowflake happens, it's a      │
  │                  connector swap, not a rewrite.             │
  │                                                             │
  │  Future (TBD)    Snowflake may absorb analytics workloads.  │
  │                  Keystone may still need PG or SQL Server   │
  │                  for application data (fast reads/writes    │
  │                  that a web app needs). Snowflake would     │
  │                  be the analytical layer on top.            │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘


  THE DATA PIPELINES — HOW DATA GETS INTO EACH DATABASE
  ─────────────────────────────────────────────────────────────────

  DATABASE A: AZURE SQL (Clinical — Josh's world)
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
  │  ChartPath   │  │  UKG         │  │  Synapse     │
  │  (EHR)       │  │  (HR/payroll)│  │  (analytics) │
  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
         │                 │                 │
         ▼                 ▼                 ▼
  ┌──────────────────────────────────────────────────────┐
  │  Azure Data Factory / Function Apps                   │
  │  (automated pipelines — Josh & data team manage)     │
  │  Runs on schedules: nightly, weekly, on-demand       │
  └──────────────────────────┬───────────────────────────┘
                             │
                             ▼
  ┌──────────────────────────────────────────────────────┐
  │  Azure SQL Server                                     │
  │  asqls-ewh-apps-dev-01.database.windows.net           │
  │                                                       │
  │  50+ stored procedures (sp_equip_cache_*)             │
  │  Transform raw data → cache tables that Keystone      │
  │  queries. This is a CACHE LAYER — pre-computed        │
  │  results so the dashboard loads fast.                 │
  │                                                       │
  │  TERM: Stored Procedure                               │
  │  ──────────────────                                   │
  │  A SQL script saved INSIDE the database that you can  │
  │  execute by name. Like a Python function, but written │
  │  in SQL and living in the database itself.            │
  │  sp_equip_cache_performance takes raw clinical data   │
  │  and computes the numbers EQuIP dashboards display.   │
  │                                                       │
  │  TERM: Cache Layer                                    │
  │  ──────────────────                                   │
  │  Pre-computed results stored in tables so the web     │
  │  app doesn't have to recalculate every time someone   │
  │  opens a page. The stored procedures refresh these    │
  │  cache tables on a schedule.                         │
  └──────────────────────────────────────────────────────┘
         │
         ▼
  Keystone backend reads cache tables via SqlClient


  DATABASE B: POSTGRESQL (BD — Your world)
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  ┌──────────────────────────────────────────────────────┐
  │  Excel Forward Universe (V26.x)                       │
  │  Vault/02_Data_Model/Current/                         │
  │  THE master copy. ~25,500 rows.                      │
  └──────────────────────────┬───────────────────────────┘
                             │
                             │  YOU run a Python script
                             │  (manually, from your laptop)
                             │
                             ▼
  ┌──────────────────────────────────────────────────────┐
  │  Migration Script (v26_1_migration.py)                │
  │  dry_run=True → report only                          │
  │  dry_run=False → applies changes → new Excel version │
  └──────────────────────────┬───────────────────────────┘
                             │
                             │  YOU run the PG loader
                             │  (manually)
                             │
                             ▼
  ┌──────────────────────────────────────────────────────┐
  │  Load Script (load_v26_to_pg.py)                      │
  │  Reads Excel → TRUNCATES old PG data → INSERTs new   │
  │  Uses psycopg2 to connect directly to Azure PG       │
  │                                                       │
  │  TERM: TRUNCATE                                       │
  │  ──────────────────                                   │
  │  Deletes ALL rows from a table instantly, then the    │
  │  script re-inserts everything from the new Excel.     │
  │  This is a full reload, not an incremental update.    │
  │  Safe because the Excel file IS the source of truth   │
  │  — if PG gets wiped, you just reload.                │
  └──────────────────────────┬───────────────────────────┘
                             │
                             ▼
  ┌──────────────────────────────────────────────────────┐
  │  PostgreSQL (Azure)                                    │
  │  keystone-platform-postgres.postgres.database.azure   │
  │  .com                                                 │
  │                                                       │
  │  bd.market_intel_facilities      25,497 rows          │
  │  bd.market_intel_corporate_entities  3,988 rows       │
  │  bd.market_intel_metros          12 rows              │
  │  bd.pipeline_facilities          4,476 rows           │
  │                                                       │
  │  NO stored procedures. NO views. NO triggers.         │
  │  NO computed columns. Just flat tables.               │
  │  ALL logic lives in Python scripts (Git-versioned).   │
  │                                                       │
  │  This is what makes Snowflake migration easy —        │
  │  the database is DUMB STORAGE. Swap the connector,    │
  │  everything else stays.                               │
  └──────────────────────────────────────────────────────┘
         │
         ▼
  Keystone backend reads BD tables via PgClient
         │
         ▼
  BD Pipeline Dashboard, MUO Universe, Market Intel,
  Data Governance module


  MONDAY.COM — THE DOWNSTREAM GAP
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  The INTENDED architecture (decided April 7, 2026):

    PG (source of truth)
      → Keystone (management interface)
        → Monday.com (downstream mirror)

  The CURRENT reality:

    Excel (actual source of truth)
      → Python → PG (downstream copy)
      → Keystone (reads PG, display only)
      → Monday.com (MANUALLY maintained, drifts)

  The gap: There is NO automated write from PG or Keystone
  to Monday.com. When scoring changes, someone has to
  manually update the Monday.com Corporate Scoring Reference
  board (18401069716). This is why the April 7 reconciliation
  found 4 surfaces out of sync.

  PIPELINE SNAPSHOTS are different — the Keystone backend
  DOES pull from Monday.com CRM Pipeline board (9964956612)
  via Monday.com API, 8x/week, into PG pipeline tables.
  But that flow is Monday → PG (inbound), not PG → Monday
  (outbound). And it only runs in production (blocked until
  Josh deploys to App Service).


  DATABASE C: SNOWFLAKE (Future — does not exist yet)
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  ┌──────────────────────────────────────────────────────┐
  │                                                       │
  │  STATUS: No instance. No timeline. No decision.       │
  │                                                       │
  │  ADVOCATES: Carey DeMatteis, Jeremy Hess              │
  │  VISION: Central analytics warehouse that all         │
  │  systems pour data into. Analysts and BI tools        │
  │  query Snowflake, not individual databases.           │
  │                                                       │
  │  IF IT HAPPENS — WHAT CHANGES FOR YOU:                │
  │                                                       │
  │  Your Python scripts: swap psycopg2 for               │
  │  snowflake-connector-python. Change 4 SQL patterns:   │
  │    SERIAL        → AUTOINCREMENT                      │
  │    RETURNING id  → separate SELECT after INSERT       │
  │    TRUNCATE CASCADE → TRUNCATE (no CASCADE needed)    │
  │    NULLS LAST    → NULLS LAST (actually same!)        │
  │                                                       │
  │  Your data: identical. Same tables, same columns.     │
  │  Your logic: untouched. All scoring, entity           │
  │  resolution, metro assignment, data quality rules     │
  │  live in Python — the database never had any of it.   │
  │                                                       │
  │  Keystone: If Keystone also migrates to Snowflake,    │
  │  PgClient swaps for a Snowflake client. If not,       │
  │  you'd load to both PG (for Keystone) and Snowflake   │
  │  (for analytics).                                     │
  │                                                       │
  │  Estimated effort: days, not weeks.                   │
  │                                                       │
  │  POLITICAL NOTE: Always present your work as           │
  │  Snowflake-compatible. Carey and Jeremy are watching.  │
  │  The fact that all logic is in Python (not in the      │
  │  database) is the strongest argument — it proves the   │
  │  work is portable.                                    │
  │                                                       │
  └─────────────────────────────────────────────────────────┘


  THE FULL DATABASE MAP — ONE PICTURE
  ─────────────────────────────────────────────────────────────────

  ┌─────────────────────────────────────────────────────────────┐
  │                      UPSTREAM SOURCES                       │
  ├──────────────────┬──────────────────┬───────────────────────┤
  │  ChartPath/UKG/  │  Excel Forward   │  Monday.com CRM      │
  │  Synapse         │  Universe V26.x  │  Pipeline Board      │
  │  (clinical)      │  (BD master)     │  (BD pipeline)       │
  └────────┬─────────┴────────┬─────────┴──────────┬────────────┘
           │                  │                     │
           │ automated        │ manual              │ 8x/week
           │ pipelines        │ Python scripts      │ auto-sync
           │                  │                     │ (prod only)
           ▼                  ▼                     │
  ┌─────────────────┐  ┌──────────────────┐        │
  │  AZURE SQL      │  │  POSTGRESQL      │◄───────┘
  │  (clinical)     │  │  (BD)            │
  │                 │  │                  │
  │  50+ stored     │  │  NO stored       │
  │  procedures     │  │  procedures      │
  │  Cache layer    │  │  Flat tables     │
  │  Josh manages   │  │  Roian manages   │
  └────────┬────────┘  └────────┬─────────┘
           │                    │
           │  SqlClient         │  PgClient
           │  (? placeholders)  │  (%s placeholders)
           │                    │
           └────────┬───────────┘
                    │
                    ▼
           ┌─────────────────┐
           │  KEYSTONE       │
           │  BACKEND        │
           │  (FastAPI)      │
           └────────┬────────┘
                    │
                    │  JSON API responses
                    │
                    ▼
           ┌─────────────────┐
           │  KEYSTONE       │
           │  FRONTEND       │     ─ ─ ─►  Monday.com
           │  (React)        │             (manual today,
           └─────────────────┘              automated TBD)

                                   ─ ─ ─►  Snowflake
                                           (future, TBD)


══════════════════════════════════════════════════════════════════════




══════════════════════════════════════════════════════════════════════
  CHAPTER 4: THE MONDAY.COM PIPELINE SYNC
══════════════════════════════════════════════════════════════════════

  How pipeline data gets pulled from Monday.com, snapshotted
  into PostgreSQL, and used to detect movement across stages.


  WHAT THIS IS
  ─────────────────────────────────────────────────────────────────

  The CRM Pipeline board in Monday.com (board 9964956612) is
  where the BD team manages facilities through the sales
  pipeline. ~4,200+ facilities across 8 groups (stages).

  Keystone pulls a SNAPSHOT of that board into PostgreSQL
  on a schedule. This is the ONLY automated data flow
  between Monday.com and your systems.

  The direction matters:

    Monday.com ──────► PostgreSQL ──────► Keystone dashboards
      (source)          (snapshot)         (display)

  Monday.com is the source. PG stores snapshots. Keystone
  reads PG. Nobody writes BACK to Monday.com automatically.


  THE SYNC SCHEDULE
  ─────────────────────────────────────────────────────────────────

  8 syncs per week. Weekdays only. No weekends.
  All times are UTC (Eastern in parentheses):

    Monday       11:00 UTC (7 AM ET)    22:00 UTC (6 PM ET)
    Tuesday      16:00 UTC (12 PM ET)
    Wednesday    11:00 UTC (7 AM ET)    22:00 UTC (6 PM ET)
    Thursday     16:00 UTC (12 PM ET)   22:00 UTC (6 PM ET)
    Friday       11:00 UTC (7 AM ET)

  The scheduler is a BACKGROUND LOOP inside the Keystone
  backend process. It calculates "how many seconds until the
  next scheduled slot," sleeps, wakes, syncs, then sleeps
  again. 30-minute debounce after each sync prevents
  double-triggers.

  TERM: Background Loop
  ──────────────────
  A task running inside the backend program that operates
  independently of web requests. While the backend is
  answering API calls from the frontend, this loop is
  running alongside it — sleeping, waking at scheduled
  times, pulling data. If the backend restarts, the loop
  restarts too.

  ⚠  THIS ONLY RUNS IN PRODUCTION.
     The scheduler is gated behind ENVIRONMENT=production
     in main.py (line 244). On your laptop
     (ENVIRONMENT=development), it never starts. This is
     why the sync hasn't been firing — Josh hasn't
     deployed the backend to Azure App Service yet.

  You can also trigger a manual sync:

    POST /api/business-development/pipeline/sync
    (requires bd_admin role, 15-minute cooldown between syncs)


  WHAT HAPPENS DURING A SYNC — STEP BY STEP
  ─────────────────────────────────────────────────────────────────

  STEP 1: FETCH FROM MONDAY.COM
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  The backend calls Monday.com's GraphQL API.

  TERM: GraphQL
  ──────────────────
  A query language for APIs (created by Facebook). Instead
  of calling 10 different URLs to get 10 pieces of data,
  you send ONE request that describes exactly what you want:

    "Give me all items in board 9964956612, group 'new_lead',
     with columns: facility_name, estimated_ar, state, stage,
     corporate_owner, consent_counts..."

  Monday.com returns exactly that — nothing more, nothing less.

  TERM: API Token
  ──────────────────
  A long random string that proves "I am authorized to access
  this Monday.com account." Stored in environment variables
  (MONDAY_API_TOKEN), never in code. Sent with every request
  in the Authorization header.

  The sync fetches ALL 8 groups (pipeline stages):

    ┌─────────────────────────────────────────────────────┐
    │  GROUP             │  WHAT IT IS                     │
    ├─────────────────────────────────────────────────────┤
    │  new_lead          │  Just identified                │
    │  prospect          │  In conversation                │
    │  contracting       │  Paperwork in progress          │
    │  consenting        │  Getting patient consent        │
    │  scheduling        │  Scheduling first visits        │
    │  established       │  Active / Won                   │
    │  revisit           │  Previously exited, reconsidering│
    │  unqualified       │  Doesn't meet criteria          │
    └─────────────────────────────────────────────────────┘

  Each group is fetched separately with PAGINATION:

  TERM: Pagination
  ──────────────────
  Monday.com won't return 4,200 items in one response.
  It returns 200 at a time with a CURSOR (a bookmark) that
  says "send this back to get the next 200." The code loops
  until the cursor is null (no more pages).

    Page 1: items 1-200     + cursor "abc123"
    Page 2: items 201-400   + cursor "def456"
    Page 3: items 401-600   + cursor "ghi789"
    Page 4: items 601-680   + cursor null (done)

  5-second sleep between pages to avoid exhausting the
  complexity budget (see below).

  For each facility (up to ~120 columns extracted):
    • Facility name, state, beds
    • Estimated AR (revenue)
    • Consent counts (SNF Primary, SNF MH, ALF Primary, etc.)
    • Stage transition dates (date became new lead, prospect, etc.)
    • Clinical capacity (PC APC, PC MD, PM APC status)
    • Scoring fields (SNF Score, ALF Score, Account Scores)
    • Corporate owner, sale type, AE assignment


  STEP 2: TRANSFORM
  ─ ─ ─ ─ ─ ─ ─ ─ ─

  Raw Monday.com column values are messy — they come as
  JSON objects with labels, IDs, and formatting. The sync
  code normalizes everything:

    • AR: Uses "new rates" formula if available, falls back
      to older formula
    • Dates: Parsed into proper date objects
    • Velocity: Pre-calculates days between stage transitions
      (how fast a facility moves through the pipeline)
    • Booleans: Monday.com checkboxes → True/False
    • Nulls: Missing values → None (not empty strings)


  STEP 3: SNAPSHOT TO POSTGRESQL
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  TERM: Snapshot
  ──────────────────
  A point-in-time copy of the entire pipeline. Not a live
  connection — a frozen picture of "what did the pipeline
  look like at 7 AM on Monday?" Every sync creates a new
  snapshot. Old snapshots are kept forever.

  This is what enables time-travel queries: "What was the
  pipeline 30 days ago? How much AR was in Contracting
  last month?"

  The snapshot writes to 3 PostgreSQL tables:

  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  bd.pipeline_snapshots                                   │
  │  ────────────────────                                    │
  │  One row per sync. Metadata only.                        │
  │                                                          │
  │    id  │ snapshot_date │ total_facilities │ total_ar      │
  │    42  │ 2026-04-11    │ 2,345            │ $10,060,000   │
  │    41  │ 2026-04-10    │ 2,340            │ $9,980,000    │
  │    40  │ 2026-04-09    │ 2,338            │ $9,950,000    │
  │                                                          │
  ├──────────────────────────────────────────────────────────┤
  │                                                          │
  │  bd.pipeline_facilities                                  │
  │  ────────────────────                                    │
  │  Every facility in every snapshot. This is the big one.  │
  │  ~4,200 rows per snapshot × N snapshots = grows fast.    │
  │                                                          │
  │    snapshot_id │ monday_item_id │ facility_name │ stage   │
  │    42          │ 8837261543     │ Sunrise SNF   │ prospect│
  │    42          │ 8837261544     │ Oak Hills     │ contract│
  │    ...         │ ...            │ ...           │ ...     │
  │                                                          │
  │  50+ columns per row. Indexed on (snapshot_id,           │
  │  monday_item_id) for fast lookups.                       │
  │                                                          │
  │  CASCADE DELETE: if you delete a snapshot from            │
  │  pipeline_snapshots, all its facility rows auto-delete.  │
  │                                                          │
  ├──────────────────────────────────────────────────────────┤
  │                                                          │
  │  bd.pipeline_stage_summary                               │
  │  ────────────────────                                    │
  │  Aggregated rollup: facility count + total AR per stage  │
  │  per snapshot. Pre-computed so the dashboard doesn't     │
  │  have to re-aggregate every time.                        │
  │                                                          │
  │    snapshot_date │ stage        │ fac_count │ total_ar    │
  │    2026-04-11    │ new_lead     │ 450       │ $1,200,000  │
  │    2026-04-11    │ prospect     │ 680       │ $2,800,000  │
  │    2026-04-11    │ contracting  │ 340       │ $1,500,000  │
  │                                                          │
  └──────────────────────────────────────────────────────────┘

  The write uses an UPSERT pattern:

  TERM: Upsert
  ──────────────────
  "Update or Insert." If a snapshot for today already exists
  (from an earlier manual sync), delete it and replace it
  with fresh data. This means you can re-sync the same day
  without creating duplicates.

    DELETE FROM bd.pipeline_snapshots
      WHERE snapshot_date = '2026-04-11'   ← wipe today's old one
    INSERT INTO bd.pipeline_snapshots ...   ← write today's new one

  Facility rows are batch-inserted 500 at a time for
  performance.


  STEP 4: DETECT TRANSITIONS
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  After the snapshot is written, the code compares TODAY's
  snapshot to YESTERDAY's snapshot and classifies every
  change:

  ┌──────────────────────────────────────────────────────────┐
  │  TRANSITION TYPE     │  MEANING                          │
  ├──────────────────────────────────────────────────────────┤
  │  entry               │  New facility appeared in pipeline │
  │  entry_out_of_seq    │  New, but skipped stages           │
  │  advance             │  Moved forward (e.g. prospect →    │
  │                      │  contracting)                      │
  │  regress             │  Moved backward (contracting →     │
  │                      │  prospect)                         │
  │  exit                │  Left active pipeline (to          │
  │                      │  established, revisit, unqualified)│
  │  deletion            │  Disappeared entirely from board   │
  │  reentry             │  Returned from exit stage back     │
  │                      │  into active pipeline              │
  └──────────────────────────────────────────────────────────┘

  Written to: bd.pipeline_transitions

  Each transition has automated fields (from_stage, to_stage,
  detected_date) and MANUAL enrichment fields (loss_category,
  loss_detail, recoverable, follow_up_date) that humans fill
  in later via a Keystone UI.

  This is what powers the Movement Intelligence Report.


  STEP 5: BUILD EVENT TIMELINE
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  Separate from transitions (which compare snapshots), the
  EVENTS system reconstructs each facility's full history
  from the transition dates stored on Monday.com columns:

    date_new_lead → date_prospect → date_contracting → ...

  This builds an audit trail: "Facility X became a prospect
  on Feb 3, moved to contracting on Mar 15, was moved by
  Ian." The "moved by" comes from Monday.com's activity log
  API (who physically dragged the item between groups).

  Written to: bd.pipeline_events


  STEP 6: TRACK CAPACITY CHANGES
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  Three clinical capacity columns are tracked for
  state changes between snapshots:

    pc_apc_capacity    (Primary Care APC)
    pc_md_capacity     (Primary Care MD)
    pm_apc_capacity    (Psych Med APC)

  When a value changes (e.g. "Need Approval" → "Position
  Posted"), it's logged. This enables time-to-ready metrics:
  how long does it take from identifying a need to having a
  provider ready?

  Written to: bd.pipeline_capacity_transitions
  Added: PR #155, merged 2026-04-07


  THE FULL SYNC PIPELINE — ONE PICTURE
  ─────────────────────────────────────────────────────────────────

  ┌──────────────────┐
  │  Monday.com      │
  │  CRM Pipeline    │
  │  Board           │
  │  (9964956612)    │
  └────────┬─────────┘
           │
           │  GraphQL API (17 calls per sync)
           │  200 items/page, 5-sec delay between pages
           │  ~170K complexity cost (~1.7% of 10M budget)
           │
           ▼
  ┌──────────────────┐
  │  Keystone        │
  │  Backend         │
  │  (pipeline_      │
  │  sync.py)        │
  │                  │
  │  Transform:      │
  │  • Normalize AR  │
  │  • Parse dates   │
  │  • Calc velocity │
  │  • Clean nulls   │
  └────────┬─────────┘
           │
           │  psycopg2 → PostgreSQL
           │
           ├──────────────────────────────────────────────┐
           │                                              │
           ▼                                              ▼
  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
  │  pipeline_       │  │  pipeline_       │  │  pipeline_stage  │
  │  snapshots       │  │  facilities      │  │  _summary        │
  │  (1 row/sync)    │  │  (~4,200 rows/   │  │  (8 rows/sync)   │
  │                  │  │   sync)          │  │                  │
  └──────────────────┘  └──────────────────┘  └──────────────────┘
           │
           │  Compare to previous snapshot
           │
           ├──────────────────────────────────────────────┐
           │                    │                          │
           ▼                    ▼                          ▼
  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
  │  pipeline_       │  │  pipeline_       │  │  pipeline_       │
  │  transitions     │  │  events          │  │  capacity_       │
  │  (stage moves)   │  │  (audit trail)   │  │  transitions     │
  └──────────────────┘  └──────────────────┘  └──────────────────┘
           │
           │  Keystone frontend reads PG
           │
           ▼
  ┌──────────────────────────────────────────────────────────────┐
  │  BD Pipeline Dashboard                                       │
  │  • L1: Hero metrics (total AR, fac count, velocity)         │
  │  • L2: Stage breakdown, trailing performance, AE summary    │
  │  • L3: Facility cards, stage flow, movement intelligence    │
  │  • L4: Individual facility detail                           │
  └──────────────────────────────────────────────────────────────┘


══════════════════════════════════════════════════════════════════════
             THE COMPLEXITY BUDGET — MONDAY.COM'S METER
══════════════════════════════════════════════════════════════════════

  Monday.com doesn't charge per API call. It charges per
  COMPLEXITY UNIT — a measure of how much work the server
  did to answer your query. A simple "give me one item" costs
  ~100 complexity. "Give me 200 items with 120 columns each"
  costs ~10,000.

  TERM: Complexity
  ──────────────────
  Monday.com's way of metering API usage. Every GraphQL
  query has a cost. Your account has a budget. When the
  budget runs out, API calls fail until it resets.

  YOUR BUDGET:

    ┌──────────────────────────────────────────────────────┐
    │                                                      │
    │  Total budget:     10,000,000 complexity units        │
    │  Per sync cost:    ~170,000 units                    │
    │  Per sync %:       ~1.7% of total budget             │
    │                                                      │
    │  8 syncs/week:     ~1,360,000 units/week             │
    │  Monthly usage:    ~5,440,000 units/month            │
    │                                                      │
    │  Verdict:          WELL WITHIN LIMITS                │
    │                    Using ~54% of monthly budget       │
    │                    on pipeline syncs alone            │
    │                                                      │
    └──────────────────────────────────────────────────────┘

  Every API call returns complexity info in the response:

    complexity {
      query: 10057          ← what this call cost
      after: 9829943        ← budget remaining
      reset_in_x_seconds: 42 ← when budget refills
    }

  The code tracks this and logs it:

    Monday API call #17: complexity=10057,
      remaining=9,829,943/10,000,000, account=12345

  At the end of each sync, the API usage summary is
  included in the response:

    api_usage: {
      api_calls: 17,
      total_complexity: 170,000,
      complexity_budget: 10,000,000,
      budget_used_pct: 1.71
    }


  PROTECTION MECHANISMS
  ─────────────────────────────────────────────────────────────────

  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  BETWEEN PAGES:                                          │
  │  5-second sleep between each 200-item page fetch.        │
  │  Prevents rapid-fire calls that would spike complexity.  │
  │                                                          │
  │  RATE LIMIT RETRY:                                       │
  │  If Monday.com returns "Rate limit" error:               │
  │    Retry 1: wait 10 seconds                              │
  │    Retry 2: wait 20 seconds                              │
  │    Retry 3: wait 30 seconds                              │
  │    Then give up and raise error.                          │
  │                                                          │
  │  MANUAL SYNC COOLDOWN:                                   │
  │  POST /pipeline/sync returns HTTP 429 (Too Many          │
  │  Requests) if a sync completed less than 15 minutes ago. │
  │  Prevents someone from hammering the sync button.        │
  │                                                          │
  │  NO PRE-FLIGHT CHECK:                                    │
  │  The code does NOT check "do I have enough budget        │
  │  for this sync?" before starting. It just goes.          │
  │  If budget is exhausted mid-sync, Monday.com returns     │
  │  rate limit errors and the retry logic kicks in.         │
  │                                                          │
  │  NO AUTOMATIC CUTOFF:                                    │
  │  There is no "stop if we've used X% of budget" logic.    │
  │  Monitoring only — human reviews the logs.               │
  │                                                          │
  └──────────────────────────────────────────────────────────┘


  KEY FILES
  ─────────────────────────────────────────────────────────────────

  All in keystone-platform/backend/app/:

    services/pipeline_scheduler.py      The background loop
    services/shared/monday_client.py    GraphQL caller + complexity tracker
    routes/business_development/
      pipeline_sync.py                  Fetch, transform, snapshot
      pipeline_transition_sync.py       Stage change detection
      pipeline_events.py                Audit trail builder
      pipeline_capacity_sync.py         Clinical capacity tracking
      pipeline.py                       API endpoints (GET/POST)


  THE GAPS (HONEST)
  ─────────────────────────────────────────────────────────────────

  1. SYNC ISN'T RUNNING YET
     The scheduler only fires when ENVIRONMENT=production.
     Josh hasn't deployed the backend to Azure App Service.
     Until he does, no auto-sync. You can trigger manual
     syncs from your laptop, but it's a one-off.

  2. NO WRITE-BACK TO MONDAY.COM
     Data flows Monday → PG → Keystone. Nothing flows back.
     When scoring changes in PG, someone manually updates
     the Monday.com Corporate Scoring Reference board
     (18401069716). This is the #1 cause of data drift
     between surfaces.

  3. NO SNAPSHOT RETENTION POLICY
     Every sync adds ~4,200 rows to pipeline_facilities.
     8 syncs/week = ~33,600 rows/week = ~1.7M rows/year.
     No automatic cleanup. Table will grow indefinitely.
     Not a problem yet, but will need an archival strategy.

  4. SINGLE-PROCESS SCHEDULER
     The scheduler runs inside the backend process. If the
     backend crashes or restarts, the scheduler restarts too.
     If it restarts mid-sync, the 30-minute debounce prevents
     immediate re-sync, but partial data could be written.

  5. COMPLEXITY BUDGET IS SHARED
     The 10M budget is account-wide. If other integrations
     (Workflow Magic, Make.com, other apps) or Claude MCP
     calls use the same Monday.com account, they share the
     same budget. The ~54% monthly usage from pipeline syncs
     leaves room, but not unlimited room.

  6. GROUP, NOT STATUS
     The sync fetches by Monday.com GROUP (the lane a
     facility sits in), not by the Status column value.
     These can mismatch — a facility can be in the
     "prospect" group but have status "Contracting."
     The GROUP is authoritative. This is a known CRM
     hygiene issue.


══════════════════════════════════════════════════════════════════════




══════════════════════════════════════════════════════════════════════
  CHAPTER 5: THE MONDAY.COM MCP CONNECTION — CLAUDE'S DIRECT LINE
══════════════════════════════════════════════════════════════════════


  WHAT THIS IS
  ─────────────────────────────────────────────────────────────────

  Completely separate from Keystone's pipeline sync.

  The previous section described how KEYSTONE pulls data from
  Monday.com (backend Python code, scheduled syncs, PostgreSQL
  snapshots). That's a program talking to an API.

  THIS section describes how CLAUDE CODE talks to Monday.com
  directly — in real time, during your conversations. When you
  say "pull up the CRM Pipeline board" or "create an item on
  the scoring board," Claude doesn't go through Keystone. It
  calls Monday.com's API directly using an MCP server.

  TERM: MCP (Model Context Protocol)
  ──────────────────
  A standard for giving AI assistants (like Claude) access to
  external tools and services. Instead of Claude only being
  able to read files and run terminal commands, MCP lets it
  call APIs — Monday.com, Notion, Google Calendar, etc.

  Think of it as giving Claude a set of keys. Without MCP,
  Claude can see your files and run code. With MCP, Claude
  can also open doors to external services and interact
  with them on your behalf.

  TERM: MCP Server
  ──────────────────
  The "adapter" that translates between Claude and an external
  service. Monday.com runs an MCP server at mcp.monday.com
  that speaks Claude's protocol on one side and Monday.com's
  GraphQL API on the other. Claude sends a request like
  "get board info for board 9964956612" → the MCP server
  translates that into a Monday.com API call → returns the
  result to Claude.


  HOW IT'S CONFIGURED
  ─────────────────────────────────────────────────────────────────

  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  Server name:   monday                                   │
  │  Type:          Remote HTTP                              │
  │  URL:           https://mcp.monday.com/mcp               │
  │  Auth:          Personal API Token (Bearer header)       │
  │  Scope:         User-level (available in ALL projects,   │
  │                 not just this one)                        │
  │                                                          │
  │  Config lives in: ~/.claude/ settings (user scope)       │
  │  Added:         February 26, 2026                        │
  │                                                          │
  └──────────────────────────────────────────────────────────┘

  TERM: Bearer Token
  ──────────────────
  The API token from your Monday.com account, sent with
  every request to prove "this is Roian's account." It's
  the same type of token that Keystone's pipeline sync uses,
  but it's YOUR personal token — not a shared service
  account.

  ⚠  This token has WRITE access. Claude can not only
     read boards — it can create items, change column
     values, create boards, post updates. The permissions
     are "elevated" (automations enabled), not full admin.

  WHAT DIDN'T WORK FIRST:
  The initial plan was to run Monday.com's MCP server locally
  using their npm package (@mondaydotcomorg/monday-api-mcp).
  This is a STDIO approach — a program runs on your machine
  and Claude communicates with it through standard input/output.
  It failed because the package depends on `isolated-vm`, a
  native C++ module that requires build tools (Visual Studio
  Build Tools) and admin rights to compile. You don't have
  admin. The remote HTTP approach bypasses all of that —
  Monday.com hosts the server, you just send HTTP requests.

  TERM: STDIO vs HTTP (MCP connection types)
  ──────────────────
  Two ways Claude can talk to an MCP server:

    STDIO: A program runs on YOUR machine. Claude sends
    commands to it via text input/output (like a terminal).
    Requires installing the program locally. Can break if
    dependencies are missing.

    HTTP: The MCP server runs REMOTELY (on Monday.com's
    servers). Claude sends web requests to a URL. Nothing
    to install. More reliable, but requires internet.

    Your Monday.com MCP uses HTTP. It just works.


  WHAT CLAUDE CAN DO WITH IT
  ─────────────────────────────────────────────────────────────────

  39 tools are available. They break into categories:

  READ OPERATIONS (no risk — just looking):
  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  get_user_context        Who am I? What account?         │
  │  get_board_info          Board structure, columns, groups │
  │  get_board_items_page    Paginated items from a board    │
  │  get_full_board_data     Everything on a board at once   │
  │  get_board_activity      Activity log (who did what)     │
  │  get_column_type_info    Column definitions and types    │
  │  get_updates             Comments/updates on items       │
  │  board_insights          Board analytics/summary         │
  │  list_workspaces         All workspaces in the account   │
  │  workspace_info          Details about a workspace       │
  │  list_users_and_teams    All users and team memberships  │
  │  search                  Search across boards/items      │
  │  read_docs               Read Monday.com documents       │
  │  get_form                Form structure and questions     │
  │  get_graphql_schema      Monday.com's full API schema    │
  │  get_type_details        Detailed type definitions       │
  │                                                          │
  └──────────────────────────────────────────────────────────┘

  WRITE OPERATIONS (changes real data — use with care):
  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  change_item_column_values   Update fields on an item    │
  │  create_item                 Add a new item to a board   │
  │  create_update               Post a comment/update       │
  │  create_notification         Send a notification         │
  │  create_board                Create an entire new board   │
  │  create_column               Add a column to a board     │
  │  create_group                Add a group to a board      │
  │  create_dashboard            Create a dashboard          │
  │  create_doc                  Create a document           │
  │  create_folder               Create a folder             │
  │  create_form                 Create a form               │
  │  create_widget               Add a widget to a dashboard │
  │  create_workspace            Create a workspace          │
  │  move_object                 Move items between groups   │
  │  add_content_to_doc          Append to a document        │
  │  update_form                 Modify a form               │
  │  update_folder               Modify a folder             │
  │  update_workspace            Modify a workspace          │
  │  form_questions_editor       Edit form questions          │
  │                                                          │
  └──────────────────────────────────────────────────────────┘

  RAW API ACCESS:
  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  all_monday_api          Send any arbitrary GraphQL      │
  │                          query directly to Monday.com.   │
  │                          This is the escape hatch —      │
  │                          anything the structured tools   │
  │                          can't do, this can.             │
  │                                                          │
  └──────────────────────────────────────────────────────────┘


  HOW CLAUDE USES IT IN PRACTICE
  ─────────────────────────────────────────────────────────────────

  When you ask Claude something that involves Monday.com data,
  here's what actually happens:

  ┌──────────┐                ┌─────────────┐            ┌──────────┐
  │ You      │  "How many    │ Claude Code │  MCP call: │ Monday   │
  │ (prompt) │── facilities ►│             │── get_     │ .com MCP │
  │          │   are in      │  Decides    │  board_    │ Server   │
  │          │   Contracting │  which MCP  │  items_    │          │
  │          │   right now?" │  tool to    │  page()    │  Calls   │
  │          │               │  call       │  board:    │  Monday  │
  │          │               │             │  9964..    │  GraphQL │
  │          │               │             │  group:    │  API     │
  │          │               │             │────────────►          │
  │          │               │             │            │          │
  │          │               │             │◄── JSON ──│          │
  │          │               │             │   items    │          │
  │          │               │◄── parsed ──│            │          │
  │          │◄── "There are │   results   │            │          │
  │          │    340 fac in │             │            │          │
  │          │    Contracting│             │            │          │
  │          │    totaling   │             │            │          │
  │          │    $1.5M AR"  │             │            │          │
  └──────────┘               └─────────────┘            └──────────┘

  This happens in real time during the conversation.
  No database involved. No Keystone involved.
  Claude → Monday.com → Claude → you.

  EXAMPLES OF WHAT YOU'VE USED IT FOR:

    • Querying the CRM Pipeline board for facility counts,
      AR totals, stage breakdowns
    • Reading the Corporate Scoring Reference board
      (18401069716) for tier lookups
    • Updating column values on items (e.g., filling
      corporate owner, sale type)
    • Creating items on boards
    • Reading board activity logs (who moved what, when)
    • Pulling form structures for the GLR form
    • Searching across boards for specific facilities
    • Auditing board structure (columns, groups, automations)


  HOW THIS DIFFERS FROM KEYSTONE'S SYNC
  ─────────────────────────────────────────────────────────────────

  ┌─────────────────────┬────────────────────┬──────────────────┐
  │                     │ KEYSTONE SYNC      │ CLAUDE MCP       │
  ├─────────────────────┼────────────────────┼──────────────────┤
  │ Who calls Monday    │ Keystone backend   │ Claude Code      │
  │                     │ (Python)           │ (AI assistant)   │
  │                     │                    │                  │
  │ When                │ 8x/week scheduled  │ When you ask     │
  │                     │ + manual trigger   │ during a chat    │
  │                     │                    │                  │
  │ Data goes where     │ PostgreSQL tables  │ Claude's context │
  │                     │ (persisted)        │ (ephemeral)      │
  │                     │                    │                  │
  │ Can write to        │ No (read-only      │ Yes (create,     │
  │ Monday.com?         │ pull from Monday)  │ update, move)    │
  │                     │                    │                  │
  │ Keeps history       │ Yes (snapshots)    │ No (gone when    │
  │                     │                    │ chat ends)       │
  │                     │                    │                  │
  │ Powers dashboards   │ Yes                │ No               │
  │                     │                    │                  │
  │ Auth token          │ Service token      │ Your personal    │
  │                     │ (MONDAY_API_TOKEN) │ token (Bearer)   │
  │                     │                    │                  │
  │ Complexity budget   │ Same 10M pool      │ Same 10M pool    │
  │                     │ (shared!)          │ (shared!)        │
  └─────────────────────┴────────────────────┴──────────────────┘

  ⚠  THEY SHARE THE SAME COMPLEXITY BUDGET.
     Every MCP call Claude makes during a conversation
     counts against the same 10M complexity pool that
     Keystone's pipeline sync draws from. In practice
     this hasn't been a problem — conversational queries
     are much lighter than full board pulls — but it's
     worth knowing they're not independent meters.


  OTHER MCP SERVERS (CONFIGURED BUT NOT ACTIVE)
  ─────────────────────────────────────────────────────────────────

  Claude Code also has connections configured for:

    ┌──────────────────────────────────────────────────────┐
    │  SERVICE           │  STATUS                         │
    ├──────────────────────────────────────────────────────┤
    │  Notion            │  Needs authentication            │
    │  Candid            │  Needs authentication            │
    │  Canva             │  Needs authentication            │
    │  Google Calendar   │  Needs authentication            │
    │  Gmail             │  Needs authentication            │
    │  Monday.com        │  ✓ Connected (the only one)     │
    └──────────────────────────────────────────────────────┘

  These are claude.ai built-in integrations that ship with
  Claude Code. Only Monday.com has been authenticated.
  The others would need you to go through an OAuth flow
  to connect them.


  THE COMPLIANCE CONTEXT
  ─────────────────────────────────────────────────────────────────

  The MCP connection uses your personal API token, which has
  read/write access to boards you can access. The broader
  compliance concern is not about the API token — it's about
  the Monday.com TENANT being shared between BD and HR.

  HR stores employee-related data on two boards (Employee
  Corrective Action Tracking, Salaried APC Reporting) on
  the same Monday.com instance. Those boards never had
  permission restrictions — anyone on the tenant could see
  them. The API didn't bypass anything.

  The blocker is that third-party tools (marketplace apps,
  Make.com, etc.) get tenant-wide access when installed,
  which means they COULD touch HR data. That's what
  compliance objected to — not the API itself.

  STANDING RULE: Claude must NEVER access or surface content
  from HR boards. This is a policy rule, not a technical
  limitation.

  See projects/monday_marketplace_blocker.md for the full
  story: the three-layer problem, the two paths forward,
  and the meeting history with Monday.com's rep.


  THE PAGINATION RULE
  ─────────────────────────────────────────────────────────────────

  One critical behavior for Claude when using MCP:

  Monday.com returns paginated results (limited items per
  response). Claude MUST paginate completely — never present
  partial results as complete counts. If a board has 4,200
  items and the first page returns 200, Claude must fetch
  all 21 pages before reporting totals.

  This has bitten you before. It's now a standing feedback
  rule: "Always paginate completely — never present partial
  query results as complete counts."

  Similarly: ALWAYS query by Monday.com GROUP (the lane),
  never by status column alone. Status can mismatch group.
  The group is authoritative.


══════════════════════════════════════════════════════════════════════




══════════════════════════════════════════════════════════════════════
  CHAPTER 6: THE KEYSTONE MODULES — WHAT'S BUILT
══════════════════════════════════════════════════════════════════════

  Keystone is one application that serves many different teams.
  Each MODULE is a set of pages built for a specific purpose.
  They share the same login, the same sidebar, the same design
  language — but they serve completely different audiences with
  completely different data.

  Think of it like one building with many offices. Same front
  door, same hallways, but each room serves a different
  department.


  ══════════════════════════════════════════════════════════════
                 YOUR MODULES (BD / SALES)
  ══════════════════════════════════════════════════════════════

  These are the modules you built (with Claude) inside
  Keystone. They all read from PostgreSQL (bd schema).


  BD PIPELINE DASHBOARD
  ─────────────────────────────────────────────────────────────────

  The flagship BD module. A 4-level drill-down dashboard
  that shows the full sales pipeline from 30,000 feet down
  to individual facility detail.

  DATA SOURCE: bd.pipeline_snapshots + bd.pipeline_facilities
  (populated by the Monday.com sync described in Chapter 4)

  STATUS: Live in production. PR #155 merged 2026-04-07.
          PR #163 (Draft) has additional fixes + Data Governance.

  AUDIENCE: Brooke (BD team lead), Ian (sales ops),
            AEs (territory managers), Malik/James (finance)

  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  LEVEL 1 — THE HERO                                      │
  │  ──────────────────                                      │
  │  One screen. The "how's the pipeline?" answer.           │
  │                                                          │
  │  • Total active AR (sum of all active stages)            │
  │  • Total facility count                                  │
  │  • Pipeline velocity (avg days between stages)           │
  │  • Stage breakdown bar chart                             │
  │  • Trailing 30/60/90-day AR trend                        │
  │                                                          │
  │  Clicking any element drills to L2.                      │
  │                                                          │
  ├──────────────────────────────────────────────────────────┤
  │                                                          │
  │  LEVEL 2 — STAGE DETAIL                                  │
  │  ──────────────────                                      │
  │  One tab per stage. Shows the facilities in that stage.  │
  │                                                          │
  │  • Facility table (name, AR, days in stage, AE, corp)    │
  │  • Monthly/Weekly toggle (defaults to Monthly)           │
  │  • Fast Track vs Stalled indicators                      │
  │  • AE performance summary                                │
  │  • Trailing performance (won $, booked AR)               │
  │                                                          │
  │  Clicking a facility drills to L3.                       │
  │                                                          │
  ├──────────────────────────────────────────────────────────┤
  │                                                          │
  │  LEVEL 3 — FACILITY CARD                                 │
  │  ──────────────────                                      │
  │  Individual facility deep-dive.                          │
  │                                                          │
  │  • Facility details (beds, state, sale type, corp owner) │
  │  • Stage history timeline (when it moved, who moved it)  │
  │  • Consent counts (SNF/ALF, Primary/MH/Integrated)      │
  │  • Clinical capacity status (PC APC, PC MD, PM APC)      │
  │  • Scoring (SNF Score, ALF Score, Account Scores)        │
  │  • Stage flow visualization                              │
  │                                                          │
  ├──────────────────────────────────────────────────────────┤
  │                                                          │
  │  LEVEL 4 — MOVEMENT INTELLIGENCE                         │
  │  ──────────────────                                      │
  │  Cross-cutting views (not per-facility):                 │
  │                                                          │
  │  • Stage transitions grid (who moved where, when)        │
  │  • Drop-off analysis (exits, regressions)                │
  │  • Capacity pipeline (recruitment funnel)                │
  │  • Lost facility follow-up queue                         │
  │                                                          │
  └──────────────────────────────────────────────────────────┘

  KEY FILES:
    Frontend: frontend/src/views/business-development/
    Backend routes: backend/app/routes/business_development/
    Backend sync: (see Chapter 4 key files)


  MUO UNIVERSE
  ─────────────────────────────────────────────────────────────────

  The corporate entity management view. Shows all ~100+
  scored corporate operators (MUOs) with their tiers, scores
  across 6 dimensions, facility counts, and narratives.

  DATA SOURCE: bd.market_intel_corporate_entities +
               bd.market_intel_facilities
  (populated by your Python load scripts from Excel)

  STATUS: Live in production. Display-only — no edit capability.
          Tier management UI is a future Phase 4 goal.

  AUDIENCE: Brooke (tier assignments), Roian (analysis),
            Cary (corporate risk), Finance (board reporting)

  WHAT IT SHOWS:
    • Corporate entity list with tier (T1-T5)
    • 6 scoring dimensions per entity
    • Facility count linked to each entity
    • Narratives (corporate intel: M&A, ownership, leadership)
    • Barrier classifications (T5 only)

  WHAT IT DOESN'T DO (yet):
    • No edit capability — can't change tiers from Keystone
    • No write-back to Monday.com Scoring board
    • No scoring calculator — scores computed in Python,
      loaded to PG, displayed here

  ARCHITECTURE DECISION: This is where the "PG is SOT →
  Keystone manages → Monday.com downstream" vision is
  supposed to land. Today it's display-only. By June 6
  (scoring unfreeze), the goal is to make it the
  management interface.

  KEY FILES:
    Frontend: frontend/src/views/business-development/
      (MUO Universe components)
    Backend routes: backend/app/routes/market_intelligence/


  MARKET INTELLIGENCE
  ─────────────────────────────────────────────────────────────────

  The facility-level intelligence view. Shows all ~25,500
  facilities in the Forward Universe with geographic,
  corporate, and service data.

  DATA SOURCE: bd.market_intel_facilities +
               bd.market_intel_metros
  (populated by your Python load scripts from Excel)

  STATUS: Built. Data linkage fix needed (some entities
          show 0 linked facilities due to name matching).

  AUDIENCE: Roian (analysis), Brooke (territory strategy)

  WHAT IT SHOWS:
    • Facility search and filter
    • Geographic distribution (metro, state)
    • Corporate owner attribution
    • Service type breakdown (SNF, ALF, etc.)
    • Expansion state indicators

  KEY FILES:
    Frontend: frontend/src/views/business-development/
    Backend routes: backend/app/routes/market_intelligence/


  DATA GOVERNANCE MODULE
  ─────────────────────────────────────────────────────────────────

  The BD data dictionary and governance layer. A 4-page
  reference module built into Keystone that defines terms,
  documents rules, and tracks changes.

  DATA SOURCE: Frontend-only (no database). Content is
  hardcoded in the React components. This was a deliberate
  V1 decision — governance content doesn't need a database
  round-trip.

  STATUS: V1 built. PR #163 (Draft). Not yet merged to main.

  AUDIENCE: Roian (primary), Brooke, AEs (reference),
            anyone who asks "what does this field mean?"

  WHAT IT SHOWS:
    • Page 1: Data Dictionary — 38 terms defined
    • Page 2: Business Rules — 30 rules documented
    • Page 3: Changelog — 18 entries tracking data decisions
    • Page 4: Data Domain Logbook link

  WHY THIS EXISTS: Brooke's team and Finance kept asking
  "what does Estimated AR mean?" or "why did this facility's
  corporate owner change?" This module is the single place
  those questions get answered.

  KEY FILES:
    Frontend: frontend/src/views/business-development/
      data-governance/


  GLR FORM
  ─────────────────────────────────────────────────────────────────

  The Good Living Review intake form. Currently a standalone
  form being migrated into Keystone.

  DATA SOURCE: glr schema in PostgreSQL

  STATUS: Form built. Migration to Keystone in progress.
          Rick's team uses it for facility quality data
          collection.

  AUDIENCE: Rick (D&A team), field staff


  ══════════════════════════════════════════════════════════════
                 JOSH'S MODULES (CLINICAL / OPS)
  ══════════════════════════════════════════════════════════════

  These modules are Josh's domain. You don't build or
  maintain them, but they share the same platform, the same
  backend, and the same deployment pipeline. If Josh merges
  a PR that breaks the backend, your BD views go down too.

  ALL of these read from Azure SQL Server (not your PG).

  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  EQuIP                                                   │
  │  ─────                                                   │
  │  The biggest module. Clinician performance dashboards.    │
  │  Shows quality measures, patient outcomes, awards,        │
  │  productivity metrics. Role-based: clinicians see their   │
  │  own data, leads see their team, admins see everything.  │
  │  Fed by a complex cache layer (50+ stored procedures).   │
  │  This is what most Eventus users think of as "Keystone." │
  │                                                          │
  │  Charta / Charta 360                                     │
  │  ─────────────────                                       │
  │  Clinical auditing and quality assurance. Audit           │
  │  scheduling, question management, scoring, 360-degree     │
  │  facility views. Used by the clinical quality team.       │
  │                                                          │
  │  Prior Authorization (Pharmacy)                          │
  │  ──────────────────────────────                          │
  │  Pharmacy prior auth workflow. Tracks medication          │
  │  approvals, denials, and appeals. Used by the pharmacy   │
  │  team led by Monica Leriger.                             │
  │                                                          │
  │  ACO Scheduling                                          │
  │  ──────────────                                          │
  │  Patient visit scheduling for ACO clinicians. Calendar    │
  │  views, visit tracking, capacity planning.               │
  │                                                          │
  │  Employee Physicals                                      │
  │  ──────────────────                                      │
  │  Employee health screening tracker. Annual physical       │
  │  compliance, scheduling, status tracking.                │
  │                                                          │
  │  HR Onboarding                                           │
  │  ─────────────                                           │
  │  New employee onboarding workflows. Document tracking,    │
  │  training completion, credential verification.           │
  │                                                          │
  │  Admin                                                   │
  │  ─────                                                   │
  │  App-wide administration. User management, role           │
  │  assignment, system configuration.                       │
  │                                                          │
  │  Agent Chat                                              │
  │  ──────────                                              │
  │  AI-powered chat interface embedded in Keystone.          │
  │  Internal tool for querying data conversationally.       │
  │                                                          │
  └──────────────────────────────────────────────────────────┘


  THE MODULE MAP — ONE PICTURE
  ─────────────────────────────────────────────────────────────────

  ┌──────────────────────────────────────────────────────────────┐
  │                      KEYSTONE PLATFORM                       │
  │                (equip.eventuswh.com)                         │
  ├──────────────────────────┬───────────────────────────────────┤
  │                          │                                   │
  │  YOUR MODULES (BD)       │  JOSH'S MODULES (Clinical)       │
  │  Database: PostgreSQL    │  Database: Azure SQL              │
  │                          │                                   │
  │  ┌────────────────────┐  │  ┌─────────────────────────────┐ │
  │  │ Pipeline Dashboard │  │  │ EQuIP (clinician perf)      │ │
  │  │ (L1-L4)            │  │  │ Charta (auditing)           │ │
  │  ├────────────────────┤  │  │ Charta 360 (facility view)  │ │
  │  │ MUO Universe       │  │  │ Prior Auth (pharmacy)       │ │
  │  ├────────────────────┤  │  │ ACO Scheduling              │ │
  │  │ Market Intelligence│  │  │ Employee Physicals          │ │
  │  ├────────────────────┤  │  │ HR Onboarding               │ │
  │  │ Data Governance    │  │  │ Admin                       │ │
  │  ├────────────────────┤  │  │ Agent Chat                  │ │
  │  │ GLR Form           │  │  └─────────────────────────────┘ │
  │  └────────────────────┘  │                                   │
  │                          │                                   │
  ├──────────────────────────┴───────────────────────────────────┤
  │  SHARED INFRASTRUCTURE                                       │
  │  Auth (Azure AD) │ Sidebar │ API layer │ CI/CD │ SEQ logging │
  └──────────────────────────────────────────────────────────────┘

  KEY POINT: Your modules and Josh's modules are in the
  SAME CODEBASE, deployed in the SAME CI/CD pipeline,
  running on the SAME backend process. A broken import in
  a pharmacy route can crash the backend and take your
  pipeline dashboard offline. This is why PRs exist —
  code review catches cross-module breakage before it
  hits production.


══════════════════════════════════════════════════════════════════════




══════════════════════════════════════════════════════════════════════
  APPENDIX A: GLOSSARY
══════════════════════════════════════════════════════════════════════

  Every term defined in this notebook, alphabetized.
  Page references point to the chapter where the term is
  first explained in full.

  API (Application Programming Interface)            Ch. 2
    A set of URLs a program calls to get data or trigger
    actions. The waiter between frontend and database.

  API Token                                          Ch. 4
    A secret string proving identity to Monday.com.
    Stored in environment variables, never in code.

  Azure                                              Ch. 2
    Microsoft's cloud platform. Rented compute, storage,
    and networking in a data center.

  Azure AD / SSO (Azure Active Directory)            Ch. 2
    Microsoft's login system. One set of credentials for
    Outlook, Teams, Keystone, everything Eventus.

  Background Loop                                    Ch. 4
    A task inside the backend that runs independently of
    web requests — sleeps, wakes on schedule, does work.

  Bearer Token                                       Ch. 5
    An API token sent in the Authorization header to
    prove identity. "Bearer" means "whoever holds this
    token is authorized."

  Branch                                             Ch. 2
    A parallel copy of the codebase for making changes
    without affecting the main version.

  Cache Layer                                        Ch. 3
    Pre-computed results stored in tables so the web app
    doesn't recalculate on every page load.

  CI/CD (Continuous Integration / Continuous Deployment) Ch. 2
    Push code → tests run → deploys automatically.

  Commit                                             Ch. 2
    A saved snapshot of changes with a message. Permanent.
    Like "Save" with a note attached.

  Complexity                                         Ch. 4
    Monday.com's API metering unit. Every query has a cost.
    Account has a 10M budget that resets periodically.

  CORS (Cross-Origin Resource Sharing)               Ch. 2
    Browser security rule allowing a webpage on one domain
    to talk to a server on a different domain.

  Data Warehouse                                     Ch. 3
    A database optimized for reading/analyzing large volumes
    of data, not for running live web applications.

  Diff                                               Ch. 2
    The difference between two versions of code. Red lines
    removed, green lines added.

  Draft PR                                           Ch. 2
    A pull request marked "not ready" — triggers preview
    builds but signals "don't merge yet."

  Framework                                          Ch. 2
    A pre-built toolkit of building blocks. React is a
    JavaScript framework; FastAPI is a Python framework.

  Git / GitHub                                       Ch. 2
    Git: version control (tracks every change, who, when).
    GitHub: where Git history lives in the cloud.

  GitHub Actions                                     Ch. 2
    GitHub's built-in automation. Runs scripts (workflows)
    when events happen (PR opened, push to main).

  GraphQL                                            Ch. 4
    A query language for APIs. One request describes exactly
    what you want; server returns exactly that.

  JSON (JavaScript Object Notation)                  Ch. 2
    Structured text format for data exchange between
    programs. { "key": "value" } syntax.

  Key Vault                                          Ch. 2
    Azure's password manager for servers. Backend asks it
    for database credentials at startup.

  MCP (Model Context Protocol)                       Ch. 5
    A standard for giving AI assistants access to external
    tools and services via structured tool calls.

  MCP Server                                         Ch. 5
    The adapter between Claude and an external service.
    Translates Claude's requests into API calls.

  npm                                                Ch. 2
    Package manager for JavaScript. Like pip for Python.
    "npm run dev" starts the frontend in dev mode.

  OIDC (OpenID Connect)                              Ch. 2
    Secure way for GitHub Actions to prove identity to
    Azure without storing passwords. Uses certificates.

  origin                                             Ch. 2
    Git shorthand for "the GitHub copy of this repo."
    Push sends commits from local → origin.

  Pagination                                         Ch. 4
    Returning large results in pages (200 items at a time)
    with a cursor bookmark to fetch the next page.

  Pull Request (PR)                                  Ch. 2
    A formal request to merge a branch into main. Shows
    changes, gets reviewed, triggers automated builds.

  Snapshot                                           Ch. 4
    A point-in-time copy of data. Not live — frozen. Enables
    time-travel queries ("pipeline 30 days ago").

  SQL (Structured Query Language)                    Ch. 3
    The language for talking to databases. SELECT, INSERT,
    UPDATE, DELETE. Each database has its own dialect.

  Staging Slot                                       Ch. 2
    A second copy of the backend for testing PR changes.
    One PR at a time; others queue with labels.

  STDIO vs HTTP                                      Ch. 5
    Two MCP connection types. STDIO runs locally (fragile).
    HTTP runs remotely (reliable, needs internet).

  Stored Procedure                                   Ch. 3
    A SQL script saved inside the database, executable by
    name. Like a Python function but lives in the DB.

  TRUNCATE                                           Ch. 3
    Deletes all rows from a table instantly. Used in reload
    scripts: wipe old data, insert fresh from Excel.

  Upsert                                             Ch. 4
    "Update or Insert." Delete existing record for this
    date, then insert fresh. Prevents duplicates on re-sync.

  uvicorn                                            Ch. 2
    The program that runs the FastAPI backend. FastAPI is
    the code; uvicorn is the engine that serves it.

  venv (Virtual Environment)                         Ch. 2
    An isolated Python installation inside the project
    folder. Keeps dependencies separate from the system.


══════════════════════════════════════════════════════════════════════
```
