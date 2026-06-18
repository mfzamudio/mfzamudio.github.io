# Mario Zamudio – Portfolio

**Live site:** [www.mzamudio.com](https://www.mzamudio.com) · [mfzamudio.github.io](https://mfzamudio.github.io)

---

## About

Solution Architect and ML/Data Engineer based in Niagara Falls, ON, Canada. Currently architecting cloud-native integration and AI systems at **Corus Consulting** (Sep 2025, remote) — deploying IBM webMethods on Kubernetes (Helm), building LLM-powered diagnostic agents, and delivering CI/CD pipelines for financial services clients across Latin America.

Completed a **Master of Data Analytics** at the University of Niagara Falls Canada (GPA 4.13, President's Distinction List, 2024–2026). Capstone: production-grade ML system with Random Forest (AUC 0.98), K-Means segmentation, and a live Streamlit dashboard on Google BigQuery.

15 years of hands-on delivery for Bell Canada, AT&T, and Claro: Hadoop/Spark/Hive ETL (48+ hours → 2 hours), OpenShift/OpenStack provisioning (3 months → 2 days), Jenkins/Ansible CI/CD (10 days → 1 day).

---

## Design

Dark, sober "tech" theme — vanilla HTML/CSS/JS, no frameworks, no build step.

- **Palette:** near-black navy (`--bg #0a0e17`) with a single cyan→violet accent.
- **Type:** Space Grotesk (display) · Inter (body) · JetBrains Mono (labels/metrics).
- **Structure:** sticky header + dynamically-injected `partials/`; a home hero with animated particle-flow "delivery delta" metric cards; a blog-style **Writing** index.
- Fully token-driven in `style.css`, responsive (800px breakpoint), and respects `prefers-reduced-motion`.

---

## Featured Projects

| Project | Tools | Links |
|---------|-------|-------|
| [Profit Erosion from E-Commerce Returns](projects/project-profiterosion.html) | Python, scikit-learn, BigQuery, Streamlit, GitHub Actions | [Live App](https://profiterosion.streamlit.app) · [GitHub](https://github.com/mfzamudio/unfc-mda-capstone-project) |
| [Warzone Armory – AI-Native Full-Stack](projects/project-warzone-armory.html) | Python, GitHub Actions, Claude Code, Vanilla JS | [Live App](https://mfzamudio.github.io/warzone-armory/frontend/) |
| [LR Presets Catalog](projects/project-lr-presets.html) | Python, Pillow, OpenCV, Chart.js, Claude Code | [Live Site](https://mfzamudio.github.io/lr-mz-presets) |
| [LAPD Crime Data Analysis](projects/project-lapdcrimes.html) | Python, Random Forest, EDA | — |
| [Traffic Accident Prediction](projects/project-accidents.html) | Python, Regression | — |
| [Global Trade Analytics](projects/project-global-trade-analytics.html) | Python, Tableau, Random Forest | — |
| [Sales Forecasting Dashboard](projects/project-salesforecast.html) | Power BI, DAX | — |
| [Electric Vehicles Analysis](projects/project-electricvehicles.html) | Python, Power BI | — |
| [Superstore Sales Analysis](projects/project-superstore-tableau.html) | Tableau | — |
| [Global Superstore Analysis](projects/project-global-superstore-tableau.html) | Tableau | — |
| [Global Orders & Profit Dashboard](projects/project-globalorders-tableau.html) | Tableau | — |
| [Spotify Top Songs Analysis](projects/project-spotify.html) | SPSS, Python | — |

### Other Projects

| Project | Tools |
|---------|-------|
| [Bicycle Store SQL Analysis](projects/project-bicycles.html) | SQL |
| [Bus Scheduling Optimization](projects/project-operations.html) | Python, LP solvers |
| [Sales Modeling & DAX](projects/project-powerbi1.html) | Power BI |
| [Iris Dataset Analysis](projects/project-iris.html) | Python, Power BI |
| [Housing Prices & Bike Sharing](projects/project-housing-bikeshare.html) | Python, Power BI |
| [Advanced Visualizations & Insights](projects/project-masterycheck1-tableau.html) | Tableau |
| [Heart Attack Risk Dashboard](projects/project-heartattack-tableau.html) | Tableau |
| [Sales Decline Analysis Dashboard](projects/project-salesdecline-tableau.html) | Tableau |

---

## Publications

**Learn the Pattern, Not the Product** — 12-Part Series (June 2026)
Platform-agnostic data engineering fundamentals that transfer across Snowflake, Databricks, BigQuery, and Microsoft Fabric. Each concept is explained "in 60 seconds," visualized with an animated particle-flow diagram, and mapped across all four platforms.

| Part | Title |
|------|-------|
| Landing | [Series Overview](publications/learn-the-pattern.html) |
| Part 1 | [Anatomy of a Data Platform](publications/pattern-data-platform-layers.html) |
| Part 2 | [Storage vs Compute](publications/pattern-storage-vs-compute.html) |
| Part 3 | [ETL vs ELT](publications/pattern-etl-vs-elt.html) |
| Part 4 | [Batch vs Streaming](publications/pattern-batch-vs-streaming.html) |
| Part 5 | [Data Modeling 101](publications/pattern-data-modeling-101.html) |
| Part 6 | [Dimensional Modeling & the Star Schema](publications/pattern-dimensional-modeling.html) |
| Part 7 | [Lake vs Warehouse vs Lakehouse](publications/pattern-lake-warehouse-lakehouse.html) |
| Part 8 | [Open Table Formats](publications/pattern-open-table-formats.html) |
| Part 9 | [Partitioning & Clustering](publications/pattern-partitioning-clustering.html) |
| Part 10 | [Data Quality & Testing](publications/pattern-data-quality.html) |
| Part 11 | [Orchestration & CDC](publications/pattern-orchestration-cdc.html) |
| Part 12 | [Governance, Catalog & Lineage](publications/pattern-governance-lineage.html) |

**The Modern Data Ecosystem** — 4-Part Series (June 2026)
A practitioner's guide to the three specialized engineering roles shaping data organizations.

| Part | Title |
|------|-------|
| Landing | [The Modern Data Ecosystem — Series Overview](publications/modern-data-ecosystem.html) |
| Part 1 | [The Evolution of Data Architecture](publications/data-evolution.html) |
| Part 2 | [Data Engineer: The Builder](publications/data-engineer.html) |
| Part 3 | [Data Architect: The Strategist](publications/data-architect.html) |
| Part 4 | [ML/AI Engineer: The Deployer](publications/ml-ai-engineer.html) |

**Descriptive Analytics Series** (July 2025) — [Data Analytics: Tackling the Data](publications/descriptive-analytics.html)

---

## Technical Skills

- **Languages & ML:** Python, SQL, R, scikit-learn, Pandas, NumPy, Java, Shell, C++
- **Data Engineering:** PySpark, Apache Airflow, dbt, Apache Kafka, AWS Kinesis, Snowflake, Google BigQuery, Databricks, Delta Lake, Apache Iceberg
- **AI & LLM Engineering:** Claude, Claude Code, LangChain, LangGraph, Pinecone, Weaviate, MLflow, FastAPI, LangSmith, deepeval, Prompt Engineering, RAG
- **BI & Visualization:** Power BI (DAX), Tableau, Streamlit, Chart.js, MicroStrategy, Jupyter, SPSS
- **Cloud:** AWS (ECS, EKS, Lambda, S3, Glue, Kinesis), Azure, GCP, OpenStack, OpenShift
- **DevOps & IaC:** Docker, Podman, Kubernetes, Helm, Terraform, Jenkins, Ansible, Maven, GitHub Actions
- **Databases:** Oracle 19c, PostgreSQL, MySQL, Vertica, SQL Server, TimesTen
- **Observability:** Prometheus, Grafana, Elasticsearch, Kibana
- **Architecture:** TOGAF, Data Mesh, Medallion Architecture, DAMA-DMBOK, SOA, ESB, Microservices, API Gateway, TM Forum SID
- **Integration:** IBM webMethods, TIBCO EAI/BPM, Siebel CRM, Salesforce

---

## Education & Certifications

- Master of Data Analytics – University of Niagara Falls Canada (2024–2026, completed) · GPA 4.13 · President's Distinction List
- Bachelor of Electronic Engineering – Universidad Nacional de Colombia (1996–2002) · WES evaluated, Canada
- Certified SAFe® 6 Product Owner/Product Manager – Scaled Agile (2023)
- webMethods API Management Technical Sales Intermediate – IBM (Oct 2025)
- webMethods Hybrid Integration Sales Foundation – IBM (Nov 2025)
- webMethods Hybrid Integration Intermediate – IBM (Nov 2025)
- Microsoft Azure AI Essentials Professional Certificate – in progress (2026)

---

## Contact & Links

| Platform | Link |
|----------|------|
| Email | [mzamudio@gmail.com](mailto:mzamudio@gmail.com) |
| LinkedIn | [linkedin.com/in/mzamudio](https://linkedin.com/in/mzamudio) |
| GitHub | [github.com/mfzamudio](https://github.com/mfzamudio) |
| Portfolio | [www.mzamudio.com](https://www.mzamudio.com) |

**CV:** [`CV - MARIO ZAMUDIO.pdf`](./CV%20-%20MARIO%20ZAMUDIO.pdf)

---

*Static site — HTML/CSS/JS, dark theme, published via GitHub Pages. Last updated: June 2026.*
