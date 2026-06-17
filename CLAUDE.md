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
| Entry point | `index.html` | Landing page — About bio, profile photo, and skill badges only |
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

### Colors (CSS custom properties in `style.css`)
| Token | Value | Usage |
|---|---|---|
| `--bg` | `#f8fafc` | Page background |
| `--surface` | `#ffffff` | Card / panel background |
| `--text` | `#0f172a` | Body text |
| `--text-muted` | `#475569` | Secondary text |
| `--border` | `#e2e8f0` | Dividers, card borders |
| `--accent` | `#2563eb` | Links, CTAs, primary highlights |
| `--accent-light` | `#eff6ff` | Accent backgrounds |
| `--accent-mid` | `#bfdbfe` | Accent borders |
| `--purple` | `#6d28d9` | Secondary accent, home-link |
| `--purple-light` | `#f5f3ff` | Purple backgrounds |

### Typography
- Font: `Inter` (Google Fonts), fallback `Segoe UI`, sans-serif
- Line height: `1.65–1.75` body, `1.2` headings

### Layout Patterns
- **Project grid**: `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))`
- **Cards**: `.card` — white, box-shadow, hover lift (`transform: translateY(-4px)`)
- **Responsive breakpoint**: `800px` (flex switches to column)
- **About section**: `.about-container` — flexbox, photo left + text right

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

- **`index.html`** — landing: About bio, profile photo, skill badges
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
- [ ] Create `publications/SLUG.html` (use `publications/data-engineer.html` as template — it has the hero, Mermaid diagram wrapper, concept sections, and series-nav pattern)
- [ ] Add link card to `publications/publications.html`

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
- **No inline styles** — use `style.css` or scoped `<style>` blocks in individual pages if truly isolated
- **Partial injection pattern** — every new HTML page must include `#header-placeholder` and `#footer-placeholder` divs and load `scripts/include-layout.js`
- **Image format** — use PNG for screenshots; keep thumbnails consistent in size with existing ones (~800×500px)
- **Large notebook exports** — Jupyter HTML exports can be several MB; that is acceptable and expected
- **Relative paths** — all asset links must use relative paths (no absolute URLs for local assets)
- **Accessibility** — always include descriptive `alt` text on images
- **Do not modify** `CNAME`, the PDF CVs, or `.tex` resume files unless explicitly asked
