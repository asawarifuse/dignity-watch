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
50+ Sources → Scraping → NLP Pipeline → PostgreSQL + Neo4j → FastAPI → React Dashboard


## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Scraping | Scrapy, Selenium |
| NLP | HuggingFace, spaCy |
| Backend | FastAPI, PostgreSQL + PostGIS, Neo4j, Redis |
| Frontend | React, TailwindCSS, MapLibre GL |
| DevOps | Docker, GitHub Actions, Render |

## 🚧 Status

🟡 **Phase 0: Foundation** — In Progress (16-week build)

## 👤 Author

**Asawari Vasantrao Fuse**  
B.Tech CSE (Data Science), Year 3

## 📄 License

MIT