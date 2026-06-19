# CLAUDE.md — Portfolio Context

## Owner

**Mario Zamudio** — Solution Architect & ML/Data Engineer
- 15 years of hands-on delivery for Bell Canada, AT&T, and Claro; currently Solution Architect at Corus Consulting (Sep 2025–Present, remote)
- Master of Data Analytics, University of Niagara Falls Canada (2024–2026, completed), GPA 4.13, President's Distinction List
- Contact: mzamudio@gmail.com | mzamudio.com | GitHub: mfzamudio | LinkedIn: /in/mzamudio

---

## Project Goal

This is a **static GitHub Pages portfolio** (deployed at mzamudio.com) that positions Mario as a hands-on Solution Architect and ML/Data Engineer for the Canadian mid-senior market. The primary objective for ongoing development is to **add new cloud-native, AI, and data engineering content in English** — projects, publications, and articles that demonstrate delivery skills across Python, scikit-learn, BigQuery, Docker/Kubernetes, GitHub Actions, and enterprise integration.

---

## Site Architecture

| Layer | File(s) | Purpose |
|---|---|---|
| Entry point | `index.html` | Dark landing — hero (bio + portrait), "delivery deltas" metric cards, three numbered columns, skill chips |
| Page: Resume | `resume.html` | Education, Work Authorization, Key Projects, Experience, Skills, Certifications, Continuous Learning, Earlier Career |
| Page: Projects | `projects.html` | Full project grid (Featured + Other) |
| Page: Testimonials | `testimonials.html` | Professor / colleague testimonials |
| Page: Contact | `contact.html` | QR codes + direct contact links |
| Styles | `style.css` | Global styles, design tokens, responsive layout |
| Layout partials | `partials/header.html`, `partials/footer.html`, `partials/publications-nav.html`, `partials/projects-nav.html`, `partials/resume-nav.html` | Injected dynamically; the three `*-nav` partials are the left sidebar / table-of-contents (cross-page nav for publications **and** projects — projects links to each detail page; in-page anchor scroll-spy TOC for Resume) |
| Layout loader | `scripts/include-layout.js` | Fetches partials on `DOMContentLoaded` via `fetch()`; on `/publications/`, `projects.html` **+ every `/projects/` detail page**, and `resume.html` it wraps `<main>` in `.pub-layout` and injects the sticky `.pub-sidebar` TOC. **Publications & Projects** mark the current page `.active` by **filename** (cross-page nav — the projects sidebar links to the detail pages so it persists as you browse; both project groups stay expanded for orientation). **Resume** uses an **IntersectionObserver scroll-spy** highlighting the section in view (observing leaf links only, so a wide wrapping section never steals the highlight) |
| Projects | `projects/project-*.html` | Individual project detail pages |
| Notebooks | `projects/*.ipynb` | Jupyter notebooks (source) |
| SQL scripts | `projects/*.sql` | SQL analysis source files |
| Publications | `publications/*.html` | Articles and educational content |
| Images | `images/` | Thumbnails, screenshots, icons, QR codes |

**No build tools, no frameworks.** Vanilla HTML, CSS, and JavaScript only. Keep it that way unless explicitly asked to add a dependency.

---

## Design System

> **The site uses a DARK theme** (migrated June 2026). Everything is driven by CSS
> custom properties in `style.css` — pages and scoped `<style>` blocks must use the
> tokens, never hard-coded light colours. Legacy publication scoped styles are
> rethemed via `!important` overrides at the end of `style.css`.

### Colors (CSS custom properties in `style.css`)
| Token | Value | Usage |
|---|---|---|
| `--bg` | `#0a0e17` | Page background (near-black navy) |
| `--surface` | `#0e1422` | Card / panel background |
| `--surface-2` | `#111a2c` | Elevated panel |
| `--text` | `#e7ecf6` | Body text |
| `--text-muted` | `#94a3bd` | Secondary text |
| `--text-faint` | `#5d6b86` | Eyebrows, meta, captions |
| `--border` | `rgba(255,255,255,.08)` | Dividers, card borders |
| `--border-2` | `rgba(255,255,255,.14)` | Hover borders |
| `--accent` | `#56b6ff` | Links, CTAs, primary highlights |
| `--accent-light` | `rgba(86,182,255,.10)` | Accent backgrounds |
| `--accent-mid` | `rgba(86,182,255,.35)` | Accent borders |
| `--purple` | `#a78bfa` | Secondary accent |
| `--purple-light` | `rgba(167,139,250,.12)` | Purple backgrounds |
| `--mint` | `#4fd6a8` | Positive metric deltas |

A single cyan→violet gradient (`--accent` → `--purple`) is the signature accent — use sparingly.

### Typography (3 roles, all `@import`-ed at the top of `style.css`)
- **Display / headings:** `Space Grotesk` (`var(--disp)`)
- **Body:** `Inter` (`var(--body)`), fallback Segoe UI
- **Labels / eyebrows / metrics / nav / chips:** `JetBrains Mono` (`var(--mono)`)

### Layout Patterns
- **Header** `.site-header` — **sticky** (always visible), dark blur bar; brand (`.brand`: name + mono role line) + mono nav (`.main-nav`). The injected `#header-placeholder { display:contents }` so the sticky header has travel room.
- **Footer** `.site-footer` — darker band (`#070a12`) with a cyan→violet accent hairline on top; social icons in bordered tiles (LinkedIn uses the local `/images/icons/linkedin.png` — Simple Icons dropped LinkedIn).
- **Project grid**: `repeat(auto-fit, minmax(280px, 1fr))`; **Cards** `.card` — dark surface, hover lift + accent top border.
- **Home (`index.html`)**: scoped components — `.hero` (eyebrow + h1 + thesis + 2-paragraph lede + framed portrait), `.deltas` (delivery-delta cards with animated particle-flow SVG arrows), `.cols` (3 numbered columns) + `.chips`.
- **Publications index (`publications.html`)**: blog-style — `.post-card` grid with one full-width `.featured` card.
- **Back-links**: every project/publication detail page uses `class="home-link"` with text `← Back to …` (mono + accent, left-aligned). Project pages link to `/projects.html` ("← Back to Projects"), top + bottom; pattern pages link top → series overview, bottom → publications.
- **Responsive breakpoint**: `800px` (header/nav stack, grids collapse).

### Card Anatomy (for new projects)
```html
<div class="card">
  <a href="projects/project-NAME.html">
    <img src="images/NAME-thumbnail.png" alt="Project Title" />
  </a>
  <h3>Project Title</h3>
  <p>Short description (2–3 sentences).</p>
  <p><strong>Tools:</strong> Python, Tableau, SQL…</p>
  <a href="projects/project-NAME.html" class="btn">View Project</a>
</div>
```

---

## Content Structure

### Site is multi-page (split, not single-page)
The portfolio is split across standalone pages linked from the shared header. Each page
includes `#header-placeholder` / `#footer-placeholder` and loads `scripts/include-layout.js`.

- **`index.html`** — dark landing: hero (bio + portrait), delivery-delta metric cards, three numbered columns, skill chips
- **`projects.html`** — Featured Projects grid + Other Interesting Projects grid
- **`resume.html`** — Education, Work Authorization, Key Projects, Experience, Skills, Languages, Certifications, Continuous Learning, Earlier Career
- **`testimonials.html`** — professor / colleague testimonials
- **`contact.html`** — QR codes + direct contact links
- **`publications/`** — article pages and series landing pages

### Adding a New Project — Checklist
- [ ] Create `projects/project-NAME.html` (use existing projects as template)
- [ ] Add thumbnail image to `images/NAME-thumbnail.png`
- [ ] Add card to the correct grid in `projects.html` (Featured or Other)
- [ ] Include: title, 2–3 sentence description, tools used, link to project page
- [ ] If Jupyter notebook: export HTML and place in `projects/`
- [ ] If SQL: include `.sql` source file in `projects/`

### Adding a New Publication — Checklist
- [ ] Create `publications/SLUG.html` (for the particle-SVG series use `pattern-data-platform-layers.html` as template; for the Mermaid series use `data-engineer.html`)
- [ ] Keep scoped styles **dark** — use tokens, not light hex; the shared `.concept-section`/`.platform-table`/`.series-nav`/`.highlight-box`/`.diagram-wrap` are already rethemed dark via overrides in `style.css`
- [ ] Add a `← Back to …` link (`class="home-link"`) at top and bottom
- [ ] Add a `.post-card` to the blog-style grid in `publications/publications.html`

### Mermaid Diagrams in Publications
Publications can include architecture diagrams via Mermaid.js CDN. Load it at the bottom of `<body>`, before `include-layout.js`:
```html
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({
    startOnLoad: true, theme: 'base',
    themeVariables: { primaryColor: '#6d28d9', primaryTextColor: '#ffffff',
      primaryBorderColor: '#2563eb', lineColor: '#2563eb',
      clusterBkg: '#eff6ff', clusterBorder: '#bfdbfe', titleColor: '#0f172a' }
  });
</script>
```
Use `<pre class="mermaid">` blocks wrapped in a `<div class="diagram-wrap">` container.

---

## Existing Projects

### Featured
| Project | Tools |
|---|---|
| Data Analytics Library (project page `project-data-analytics-library.html`, SVG cover, GitHub-linked) | Python, pandas, scikit-learn, pytest, GitHub Actions — full analytics-lifecycle library, code companion to the Descriptive Analytics series |
| Spotify 2023 Analysis | SPSS, EDA, hypothesis testing |
| Traffic Accident Prediction | Python, regression |
| Sales Forecasting | Power BI, DAX |
| Electric Vehicles Analysis | Python, Power BI |
| LAPD Crime Data | Python, Random Forest |
| Superstore Sales | Tableau |
| Global Superstore | Tableau (advanced) |
| Global Orders & Profit | Tableau (dual dashboard) |
| Global Trade Analytics | Python EDA, Tableau (34-year dataset) |

### Other (8)
Bicycle Store SQL, Bus Scheduling Optimization (LP), Sales Modeling DAX, Iris Dataset, Housing Prices, Bike Sharing, Advanced Tableau Viz, Heart Attack Risk, Sales Decline Analysis

---

## Existing Publications

### Descriptive Analytics Series — *Data Analytics: Tackling the Data* (completed June 2026)
A 10-step walk-through of descriptive analytics, all sub-pages linked from `descriptive-analytics.html`. **Complete** — every step now has its own page, all using the **particle-flow inline SVG** diagram style (same SMIL technique as the "Learn the Pattern" series, **no PNG infographics, no Mermaid**) plus **Python/pandas + SQL code blocks**. A running **synthetic retail dataset** (orders → derived sales/profit) ties the examples across all pages.

| File | Step |
|---|---|
| `collecting-data.html` | 1 — Collecting Data |
| `cleaning-data.html` | 2 — Cleaning Data |
| `transforming-aggregation.html` | 3 — Transforming & Aggregation |
| `filtering-reducing-noise.html` | 4 — Filtering & Reducing Noise |
| `segmentation-clustering.html` | 5 — Segmentation & Clustering |
| `visualization-trending.html` | 6 — Visualization & Trending |
| `comparing.html` | 7 — Comparing |
| `reporting.html` | 8 — Reporting |
| `patterns-insights.html` | 9 — Patterns & Insights |
| `sharing-publishing.html` | 10 — Sharing & Publishing |

**Companion notebook:** `projects/descriptive-analytics-pipeline.ipynb` runs all 10 steps end-to-end on the synthetic dataset (seeded, reproducible, no external files; verified to execute clean). Linked for download from a "Putting It All Together" section on the landing page. These sub-pages are linked **only** from `descriptive-analytics.html` (not added to `publications.html`). The chapter pages now back-link to `descriptive-analytics.html` ("← Back to Descriptive Analytics"); the landing page itself still back-links to `publications.html`.

### Types of Analytics (4 mini-series) — June 2026
Four **mini-series** that extend the descriptive series across the full analytics lifecycle (ROADMAP Program B, W3–W6). **Each is a landing page + 4 detailed chapter pages** (20 pages total), modelled on `descriptive-analytics.html` (landing → sub-chapters). Landings carry the particle-flow SVG + a numbered chapter list and back-link to `publications.html`; chapter pages back-link to their landing (top + bottom) and chain via "Next →" links. Each series cross-links its **DataAnalyticsLibrary** module and the neighbouring lifecycle series. Each landing has a `.post-card` in `publications.html`.

**Key difference from the rest of the site:** chapters embed **real generated charts** — PNGs rendered by the example Python itself (matplotlib/seaborn/scikit-learn/scipy) on the shared synthetic retail dataset, served from `publications/images/analytics/`. Every statistic quoted (t = −55.6, χ², R² ≈ 0.96, AUC ≈ 0.70, linprog optimum) is **computed, not invented**; where the synthetic data lacks a real outcome (churn) the label is constructed and that is stated on the page. Images sit in `.diagram-wrap` and are constrained by `.diagram-wrap img { max-width:100% }` in `style.css` (added so PNGs don't overflow).

**Chart tooling** (`tools/charts/`, **dev-only, not served**): `_common.py` reproduces the seeded dataset (identical to the descriptive notebook) + a dark matplotlib style matching the site palette + brand colormap + `save()`; one script per series (`visualization.py`, `diagnostic.py`, `predictive.py`, `prescriptive.py`) regenerates that series' PNGs. Run from repo root, e.g. `python3 tools/charts/visualization.py`. ~27 PNGs total.

| Landing · module | Chapters (`publications/…`) |
|---|---|
| `visualization-analytics.html` · `datavisualization` | `viz-chart-selection` · `viz-perceptual-encoding` · `viz-advanced-charts` · `viz-dashboard-design`. (`visualization-trending.html`, descriptive step 6, cross-links here.) |
| `diagnostic-analytics.html` · `diagnosticanalysis` | `diag-correlation` · `diag-hypothesis-testing` · `diag-drilldown` · `diag-correlation-causation` |
| `predictive-analytics.html` · `predictiveanalysis` + `machinelearning` | `pred-framing` · `pred-train-test-split` · `pred-regression` · `pred-classification` |
| `prescriptive-analytics.html` · `prescriptiveanalysis` | `presc-scenarios` · `presc-business-rules` · `presc-optimization` · `presc-decision-constraints` |

### Capstone — From Notebook to Platform Pipeline — June 2026
`from-notebook-to-platform-pipeline.html` (ROADMAP Program D, W7). Hybrid page: descriptive-series anatomy (particle-flow SVG + code blocks) **plus** a Program-A-style **"same pattern, every platform"** `platform-table`. Thesis: take an exploratory notebook or the DataAnalyticsLibrary to a production pipeline on Fabric/Snowflake/Databricks/BigQuery **without rewriting the logic** — modularize → parameterize → package → orchestrate. Cross-links the DataAnalyticsLibrary project page and the Learn-the-Pattern series (the piece that ties Programs A + the library together). Carries a small scoped `<style>` for the table's base structure (dark tokens only — the global `.platform-table` overrides supply colours but not the box model).

### Learn the Pattern, Not the Product (12-Part Series) — June 2026
Platform-agnostic data engineering fundamentals. The through-line is **transferability** — each concept applies across Snowflake, Databricks, BigQuery, and Microsoft Fabric without vendor lock-in. Every concept page follows a fixed anatomy: an "In 60 seconds" box, "How it actually works" concept sections, an **animated particle-flow inline SVG diagram**, and a **"Same pattern, every platform"** mapping table.

**Diagram style (this series):** diagrams are hand-built inline `<svg>` with animated "particle" dots flowing along the connectors (SMIL `<animateMotion>` + `<mpath>`), on a dark gradient card — **no Mermaid, no JS, no libraries**. Copy the `<svg>` from `pattern-data-platform-layers.html` (Part 1) as the canonical template and adapt the shape. The older "Modern Data Ecosystem" series still uses Mermaid; don't mix the two on a page.

| File | Title |
|---|---|
| `learn-the-pattern.html` | Landing page — series overview, 6-layer particle-SVG diagram, 12-part grid |
| `pattern-data-platform-layers.html` | Part 1 — Anatomy of a Data Platform (6 universal layers) |
| `pattern-storage-vs-compute.html` | Part 2 — Storage vs Compute: The Great Divorce |
| `pattern-etl-vs-elt.html` | Part 3 — ETL vs ELT: Where Transformation Lives |
| `pattern-batch-vs-streaming.html` | Part 4 — Batch vs Streaming: Choosing Your Latency |
| `pattern-data-modeling-101.html` | Part 5 — Data Modeling 101 (normalized vs analytical) |
| `pattern-dimensional-modeling.html` | Part 6 — Dimensional Modeling & the Star Schema |
| `pattern-lake-warehouse-lakehouse.html` | Part 7 — Lake vs Warehouse vs Lakehouse |
| `pattern-open-table-formats.html` | Part 8 — Open Table Formats (Delta · Iceberg · Hudi) |
| `pattern-partitioning-clustering.html` | Part 9 — Partitioning & Clustering |
| `pattern-data-quality.html` | Part 10 — Data Quality & Testing |
| `pattern-orchestration-cdc.html` | Part 11 — Orchestration & CDC |
| `pattern-governance-lineage.html` | Part 12 — Governance, Catalog & Lineage |

### The Modern Data Ecosystem (4-Part Series) — June 2026
| File | Title |
|---|---|
| `modern-data-ecosystem.html` | Landing page — ecosystem map, role overview cards, series navigation |
| `data-evolution.html` | Part 1 — Evolution of Data Architecture (timeline diagram) |
| `data-engineer.html` | Part 2 — Data Engineer: The Builder (pipeline diagram, ETL/ELT, data contracts) |
| `data-architect.html` | Part 3 — Data Architect: The Strategist (Medallion diagram, Data Mesh, cloud table) |
| `ml-ai-engineer.html` | Part 4 — ML/AI Engineer: The Deployer (RAG pipeline diagram, MLOps lifecycle) |

---

## Skills & Tools Inventory

| Category | Technologies |
|---|---|
| Languages | Python, SQL, R, Java, Shell, C++ |
| ML / Data | scikit-learn, Pandas, NumPy, statsmodels, Jupyter, SPSS, Databricks, Google BigQuery |
| Data Engineering | PySpark, Apache Airflow, Prefect, dbt, Apache Kafka, AWS Kinesis, Snowflake, Delta Lake, Apache Iceberg |
| BI | Power BI (DAX), Tableau, Streamlit, Chart.js, MicroStrategy |
| AI / LLM | Claude, Claude Code, LangChain, LangGraph, Pinecone, Weaviate, MLflow, FastAPI, LangSmith, deepeval |
| Cloud | AWS (ECS/EKS/Lambda/S3/Glue/Kinesis), Azure, GCP, OpenStack, OpenShift |
| DevOps | Docker, Podman, Kubernetes, Helm, Jenkins, Ansible, Maven, GitHub Actions, Terraform |
| Databases | Oracle 19c, PostgreSQL, MySQL, Vertica, SQL Server, TimesTen |
| Observability | Prometheus, Grafana, Elasticsearch, Kibana |
| Architecture | TOGAF, SOA, ESB, Microservices, API Gateway, TM Forum SID, Data Mesh, Medallion, DAMA-DMBOK |
| Integration | IBM webMethods, TIBCO EAI/BPM, Siebel CRM, Salesforce |

---

## Content Language

**All new content must be written in English.** This includes:
- Project titles, descriptions, and detail pages
- Publication articles
- Code comments and notebook markdown cells
- Alt text for images
- Any UI copy added to the site

---

## Constraints & Conventions

- **No frameworks or build tools** — pure HTML/CSS/JS
- **Dark theme via tokens** — never hard-code light colours; use the `style.css` custom properties (see Design System)
- **No decorative emojis** in page content (headings, links, cards). They read as "AI-generated." Typographic arrows (`←` `→`) and functional glyphs inside SVG diagrams are fine.
- **Do not name the current employer ("Corus Consulting") on public-facing site pages** — it is a job-search portfolio. Describe current work generically (enterprise integration, AI-assisted development). Past employers (HPE) and verifiable metrics are fine. (Quotes in `testimonials.html` that mention it are left verbatim.)
- **Back-link convention** — `class="home-link"` + `← Back to …` (see Layout Patterns).
- **No inline styles** — use `style.css` or scoped `<style>` blocks in individual pages if truly isolated
- **Partial injection pattern** — every new HTML page must include `#header-placeholder` and `#footer-placeholder` divs and load `scripts/include-layout.js`
- **Image format** — use PNG for screenshots; keep thumbnails consistent in size with existing ones (~800×500px)
- **Large notebook exports** — Jupyter HTML exports can be several MB; that is acceptable and expected
- **Relative paths** — all asset links must use relative paths (no absolute URLs for local assets)
- **Accessibility** — always include descriptive `alt` text on images
- **Do not modify** `CNAME`, the PDF CVs, or `.tex` resume files unless explicitly asked

---

## Session History / Changelog

### June 19, 2026 — Side TOC extended to Projects & Resume + ROADMAP/content audit
Reused the publications left-sidebar pattern as an **in-page table of contents** on `projects.html` and `resume.html` (the user asked for "the same lateral content bar"), and audited the ROADMAP against the live pages.

- **`partials/projects-nav.html`** — two groups (Featured ×12 · Other ×9). **Revised** after first build: sub-items link to the **project detail pages** (`/projects/project-*.html`), not in-page anchors, so the sidebar persists and stays useful while browsing individual projects. **`partials/resume-nav.html`** — nine childless groups, each a `.pub-nav-series` anchoring to a section heading id (`#resume-*`, added to each `<h3>`). (Per-card `#proj-*` ids remain on `projects.html` but are no longer the nav targets.)
- **`scripts/include-layout.js`** — refactored: extracted `injectSidebar()` (shared `.pub-layout`/`.pub-sidebar` wrapping), `markActiveByFilename()`, and `initScrollSpy()`. **Publications** inject on `/publications/` (one series expands). **Projects** inject on `projects.html` **and every `/projects/` detail page** — mirrors the writing sidebar: groups start **collapsed**, only the group holding the current project expands (the "All Projects" grid matches nothing, so all stay collapsed), and the current project is highlighted by filename; section-header links are excluded from matching so the grid page doesn't false-highlight both headers. **Resume** uses an **IntersectionObserver** scroll-spy (`rootMargin: -120px 0 -65% 0`) observing leaf links only.
- **Collapsible first level (follow-up):** `wireCollapsibles(aside, headerNavigates)` in `include-layout.js` wraps every group header that has sub-items in a `.pub-nav-series-row` and prepends a `.pub-nav-toggle` chevron **button**. A header click **always** toggles `.active-group` (drives the `<ul>`; `aria-expanded` synced); `headerNavigates` then decides whether it also follows the link. **Writing** (`headerNavigates=true`): one click does **both** — toggles the group **and** navigates to the series landing (which then shows it expanded). **Projects** (default): toggles **in place** only (`preventDefault`) — projects headers point at the grid, not a per-group landing. The chevron always toggles in place on both. Resume groups are childless, so unaffected. Styled in `style.css` (`.pub-nav-series-row` / `.pub-nav-toggle`); the old `::before` arrow is hidden inside a row.
- **`style.css`** — one rule added: `.pub-layout > main [id] { scroll-margin-top: 100px }` so anchor jumps clear the sticky header. (Projects' grids now sit inside the shared `max-width:880px` main, same as publications — narrower than before, consistent.)
- **ROADMAP audit (step 3):** all 26 referenced publication pages (12 pattern + descriptive + 4 landings + 16 analytics chapters + capstone) exist with sensible `<title>`s; the B4 launch URLs resolve to the live **landing** pages; the 5 landing `.post-card`s are present in `publications.html`. No corrections needed — ROADMAP matches the live content.
- **Validation:** `node --check` passes; all 24 projects-nav + 10 resume-nav anchors resolve to real ids. **Not visually verified** (no headless browser in env) — needs a browser hard-refresh pass.

### June 19, 2026 — Publications left sidebar (table of contents)
Added a persistent **left sidebar / location map** to every `/publications/` page (and the `publications.html` index), so readers can see where they are and jump to any page.

- **`partials/publications-nav.html`** — single-source nav tree: 8 `.pub-nav-group` blocks (Learn the Pattern · Modern Data Ecosystem · Descriptive · Visualization · Diagnostic · Predictive · Prescriptive · Capstone). First level is a plain `<a class="pub-nav-series">` straight to the **series landing** (no separate "overview" item); the `<ul>` of numbered chapters is the second level.
- **`scripts/include-layout.js`** — on `/publications/` paths only, fetches the nav, wraps the existing `<main>` in a `.pub-layout` flex container, injects `.pub-sidebar`, then marks the current page `.active` (matched by filename) and adds `.active-group` to its group.
- **`style.css`** — `.pub-layout` is **left-aligned** (`margin:0`, not centered) so the bar hugs the page's left. `.pub-sidebar` is sticky (`top:92px`, **320px** wide so chapter titles fit on one line). Children are hidden by default and only shown for `.active-group` (the series you're in) — so other series collapse to just their name; the active series auto-expands. Active link = accent + left border + `--accent-light`. Mobile (`≤800px`): sidebar stacks on top.
- **Header enlarged** the same session: `.header-bar` padding 14→20px, `.brand .name` 1.12→1.5rem, `.brand .role` 0.6→0.66rem, `.main-nav a` 0.74→0.8rem (sidebar sticky `top` bumped to clear the taller header).
- Card grids earlier in the day: also note `style.css` now has global `.series-parts`/`.part-link` base styles so any landing uses the learn-the-pattern card format (Part for the older series, Chapter for the analytics mini-series, Step for descriptive).
- **Cannot screenshot locally** (no headless browser in env); validated structurally — JS `node --check` passes, all 51 nav links resolve, active-state selector matches exactly one link per page. **Needs a visual pass in the browser** (hard-refresh for cached CSS/JS).

### June 19, 2026 — Rebuilt "Types of Analytics" as mini-series with generated charts
The four flat type-pages from earlier the same day were judged too basic. Rebuilt each into a **landing + 4 chapters** (20 pages total), modelled on the descriptive series, and — the key change — every chapter embeds a **real chart generated by its own example code** (no stock infographics).

- **Chart tooling** added at `tools/charts/` (dev-only): `_common.py` (seeded dataset identical to the descriptive notebook + dark matplotlib theme matching `style.css` tokens + brand colormap) and one script per series. ~27 PNGs in `publications/images/analytics/`.
- **All numbers are computed, not invented:** t = −55.6 (p<0.001) and ~$188 profit gap, χ² association, regression R² ≈ 0.96 / MAE ≈ $1,550, churn AUC ≈ 0.70 / precision 0.63 / recall 0.64, linprog optimum West $50K + Paid $50K → $257.5K. Honesty notes added where a label is constructed (churn) or an input is illustrative (channel returns, demand). Confounder chart (ice-cream vs drownings) explicitly labelled illustrative.
- **`style.css`**: added `.diagram-wrap img { max-width:100%; height:auto }` — the only CSS change — so generated PNGs scale to the card instead of overflowing (the prior rule only constrained `svg`). Reported by Mario as horizontal-scroll; fixed.
- The 4 landing `.post-card`s in `publications.html` updated to "· 4 parts / Start the series". Docs synced (README, this file).
- **Still open:** schedule the LinkedIn posts (Programs A & C copy ready in ROADMAP; B/D launch posts can go out now). The B4 LinkedIn copy in ROADMAP still references the single-page URLs — those URLs are now the series landings, so the copy still resolves, but could be refreshed to mention the chapters.

### June 19, 2026 — "Types of Analytics" pages + capstone (ROADMAP Programs B & D)
Built the 5 remaining buildable items on the roadmap (W3–W7). Programs A & C are LinkedIn-posting tasks (manual), so this covered all the page-build work.

- **4 "Types of Analytics" pages** (Program B): `visualization-analytics.html`, `diagnostic-analytics.html`, `predictive-analytics.html`, `prescriptive-analytics.html` — descriptive-series anatomy (particle-flow SVG + Python/pandas + SQL on the shared synthetic retail dataset), each cross-linking its DataAnalyticsLibrary module and neighbouring lifecycle pages.
- **1 capstone page** (Program D): `from-notebook-to-platform-pipeline.html` — descriptive anatomy **+** a Program-A-style `platform-table` (with a small scoped dark-token `<style>` for the table box model). Ties the library to the Learn-the-Pattern series.
- **`publications/publications.html`**: 5 new `.post-card`s (cats: "Types of Analytics" ×4, "Capstone" ×1).
- **`visualization-trending.html`** (descriptive step 6): added a cross-link to the new broad `visualization-analytics.html`.
- Stat accuracy held to the global rules: Cleveland & McGill (1984) referenced as a real source for the perceptual-encoding ranking; t-test/chi-square/p-value/R²/MAE/precision/recall described precisely; platform tables kept capability-level with a "verify vs docs" note; no fabricated metrics.
- Docs updated: `README.md`, this file. **ROADMAP.md** W3–W7 flipped to done.
- **Still pending (manual, Mario):** schedule the LinkedIn posts (Programs A & C copy is ready in ROADMAP; B/D launch posts can now go out since the pages are live).

### June 19, 2026 — Added "Data Analytics Library" project
Added Mario's GitHub repo [`DataAnalyticsLibrary`](https://github.com/mfzamudio/DataAnalyticsLibrary) (local at `/home/devuser/Projects/DataAnalyticsLibrary`) as a portfolio project — a full analytics-lifecycle Python library (10 modules, **81 pytest tests** verified, CI on 3.10–3.12), positioned as the code companion to the Descriptive Analytics series.

- New detail page `projects/project-data-analytics-library.html` (dark, GitHub-linked, lifecycle table + code blocks + honest scope).
- New **Featured #1** card in `projects.html`; the previous 11 featured cards renumbered 2–12.
- On-brand **SVG cover** `images/data-analytics-library.svg` used as the thumbnail (no PNG generated).
- Cross-linked both ways: a "Reference Library" block added to `publications/descriptive-analytics.html`, and the project page links back to the series.
- README featured table updated. NOTE: the repo's own `README.md` says "71 tests" but the suite actually has **81** — flag to fix upstream.

### June 19, 2026 — Descriptive Analytics series completed
Finished the *Data Analytics: Tackling the Data* series (steps 4–10 were previously pending).

- **7 new chapter pages** created (`filtering-reducing-noise`, `segmentation-clustering`, `visualization-trending`, `comparing`, `reporting`, `patterns-insights`, `sharing-publishing`), each with an animated **particle-flow SVG** diagram + **Python/pandas + SQL** code blocks.
- **3 original pages re-done** (`collecting-data`, `cleaning-data`, `transforming-aggregation`): PNG infographics replaced with particle-flow SVGs and code blocks added, for series homogeneity. Old PNGs left unused in `publications/images/`.
- **`style.css`**: added dark `pre.code-block` / `.code-label` / inline `code` styling and base `.diagram-wrap` / `.diagram-caption` box model (the prior overrides only set colours).
- **`descriptive-analytics.html`**: wired the 7 remaining bullets to their pages; added a "Putting It All Together" 10-node pipeline SVG + companion-notebook download link.
- **`projects/descriptive-analytics-pipeline.ipynb`**: new end-to-end notebook on a synthetic retail dataset (verified to run; `.style` export degrades gracefully without `jinja2`; no HTML export — `nbconvert` unavailable locally).
- Docs updated: `README.md`, `ROADMAP.md` (§8 appendix), this file.

### June 2026 — Dark redesign (merged to `main`)
A full visual migration of the site from the original light theme to a **dark, sober, "tech" aesthetic** (built with the `frontend-design` guidance, anchored in Mario's own world — his measurable "delivery deltas" and particle-flow diagram language).

- **`style.css`** rewritten with dark tokens + Space Grotesk / JetBrains Mono / Inter; added publication dark-overrides so all series pages retheme without per-file edits.
- **New partials**: sticky `.site-header` (brand + mono nav) and higher-contrast `.site-footer` (accent hairline, local LinkedIn icon).
- **`index.html`** migrated to the dark home — hero, **delivery-delta** cards (48h→2h, 3mo→2d, 10 TPS→40k TPS, all `[medido]`), three numbered columns, skill chips. Hook: *"Solution Architect — Integration · Data Engineering · Cloud · ML · AI."*
- **`publications/publications.html`** redesigned as a **blog index** (featured card + `.post-card` grid).
- **Removed all decorative emojis** from content pages (SVG diagram glyphs preserved).
- **Unified all back-links** to `← Back to …` (`home-link`, left-aligned); project pages → `/projects.html`, top + bottom.
- **`demo-format-a-full-publication.html`** — a standard long-form article template for adapting LinkedIn posts into on-site articles (the LinkedIn-integration thread is still open: need real post text + traction numbers).
- Content decisions confirmed with Mario: keep the existing colour direction; do not name Corus on public pages; no language toggle (site stays English for the Canadian market).
- Cross-checked against the Master Profile at `C:\github\mid-resume\profile\Master_Profile-20260614.md` (single source of truth for facts/metrics).

**Still open:** align `resume.html` content (still names Corus / says "available for roles"); real LinkedIn post integration.
