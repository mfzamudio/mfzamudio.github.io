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
| Layout partials | `partials/header.html`, `partials/footer.html` | Injected dynamically into every page |
| Layout loader | `scripts/include-layout.js` | Fetches partials on `DOMContentLoaded` via `fetch()` |
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

### Featured (9)
| Project | Tools |
|---|---|
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

### Descriptive Analytics Series
Sub-pages linked from `descriptive-analytics.html`: `collecting-data.html`, `cleaning-data.html`, `transforming-aggregation.html`. Steps 4–10 (Filtering, Segmentation, Visualization, Comparing, Reporting, Patterns, Sharing) do not yet have sub-pages — pending work.

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
