# CLAUDE.md — Portfolio Context

## Owner

**Mario Zamudio** — Solution Architect & Data Analytics professional
- 23+ years in telecommunications and enterprise solution architecture
- Currently completing Master in Data Analytics, University of Niagara Falls (2024–2026), GPA 4.0
- Transitioning into data analytics roles while active as Solution Architect at Corus Consulting (Sep 2025–Present)
- Contact: mzamudio@gmail.com | mzamudio.com | GitHub: mfzamudio | LinkedIn: /in/mzamudio

---

## Project Goal

This is a **static GitHub Pages portfolio** (deployed at mzamudio.com) that showcases Mario's data analytics work. The primary objective for ongoing development is to **add new data analysis content in English** — projects, publications, and articles that demonstrate applied analytics skills across Python, SQL, Power BI, Tableau, and statistical methods.

---

## Site Architecture

| Layer | File(s) | Purpose |
|---|---|---|
| Entry point | `index.html` | Single-page portfolio; all sections live here |
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

### Colors
| Token | Value | Usage |
|---|---|---|
| Background | `#f5faff` | Page background |
| Text primary | `#0d1b2a` | Body text |
| Accent purple | `#522389` | Headings, highlights |
| Accent blue | `#2d2088` | Links, CTAs |
| Accent mid | `#456fc3` | Hover states, borders |

### Typography
- Font: `Segoe UI`, sans-serif
- Line height: `2` (double — important for readability)

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

### index.html Sections (in order)
1. **About** — bio, profile photo, background summary
2. **Publications** — links to articles in `publications/`
3. **Featured Projects** — 9 main projects in `.project-grid`
4. **Other Interesting Projects** — 8 additional projects
5. **Resume** — experience, skills, education, certifications
6. **Contact** — QR codes + direct links

### Adding a New Project — Checklist
- [ ] Create `projects/project-NAME.html` (use existing projects as template)
- [ ] Add thumbnail image to `images/NAME-thumbnail.png`
- [ ] Add card to the correct section in `index.html` (Featured or Other)
- [ ] Include: title, 2–3 sentence description, tools used, link to project page
- [ ] If Jupyter notebook: export HTML and place in `projects/`
- [ ] If SQL: include `.sql` source file in `projects/`

### Adding a New Publication — Checklist
- [ ] Create `publications/SLUG.html` (use `publications/descriptive-analytics.html` as template)
- [ ] Add link card to `publications/publications.html`
- [ ] Add reference in the Publications section of `index.html`

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

## Skills & Tools Inventory

| Category | Technologies |
|---|---|
| Languages | Python, SQL, Java, C++, Shell, COBOL |
| Analytics / BI | Jupyter, Power BI, Tableau, SPSS |
| Databases | Oracle, MySQL, PostgreSQL, Vertica |
| ML / Stats | Regression, Clustering, Random Forest, LP, EDA, Hypothesis Testing |
| DevOps | Git, Jenkins, Ansible |

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
