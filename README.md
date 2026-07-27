# DIGNITY Watch

**India's first AI-powered human rights intelligence platform tracking manual scavenging deaths.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/build-in%20progress-orange)](https://github.com/asawarifuse/dignity-watch)

---

## 🎯 The Problem

Manual scavenging — cleaning sewers and septic tanks by hand — has been illegal in India since 2013. Yet hundreds of workers die every year. There is **no centralized, publicly accessible database** tracking these deaths.

## 💡 The Solution

DIGNITY Watch automatically collects, verifies, and publishes structured data on manual scavenging incidents from 50+ multilingual news sources, government reports, and court judgments.

## 🏗 Architecture

```
50+ News Sources + Govt Reports + Court Judgments + NGO Reports
        │
        ▼
   Web Scraping (Scrapy + Selenium)
        │
        ▼
   Language Detection → Translation → NER → Dedup → Confidence Scoring
        │
        ▼
   PostgreSQL + PostGIS + Neo4j
        │
        ▼
   FastAPI Backend + React Dashboard + PDF Reports
        │
        ▼
   Public API + Interactive Map + Automated Alerts
```


## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Scraping | Scrapy, Selenium, BeautifulSoup |
| NLP | XLM-RoBERTa, IndicBERT, IndicTrans2, spaCy |
| Backend | FastAPI, PostgreSQL + PostGIS, Neo4j, Redis |
| Frontend | React, TailwindCSS, MapLibre GL, Recharts |
| DevOps | Docker, GitHub Actions, Render |
| Monitoring | Prometheus, Grafana |

## 📊 Features

- 🤖 Automated multilingual scraping from 50+ sources in 8 Indian languages
- 🧠 NLP pipeline: Language detection → Translation → NER → Dedup → Validation
- 🗺️ Interactive GIS dashboard with heatmaps and temporal trends
- ⚖️ Legal compliance tracking (PPE, FIR, compensation)
- 🔍 Full-text search across all incidents
- 📄 Auto-generated PDF reports
- 🔌 Public REST API
- 🛠 Admin panel for verification

## 🚧 Project Status

🟡 **Phase 0: Foundation** (In Progress — 16-week build)

## 👤 Author

**Asawari Vasantrao Fuse**
B.Tech CSE (Data Science), 3rd year

## 📄 License

MIT
