# ♻️ AI Waste Segregation Guide

> **An intelligent, computer vision-assisted waste classification and sustainability platform built for residential, municipal, and educational segregation workflows.**

[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Web Standards: HTML5/ES6/CSS3](https://img.shields.io/badge/Frontend-HTML5%20%2F%20ES6%20%2F%20CSS3-green.svg)](#)
[![UN SDG: 11 & 12](https://img.shields.io/badge/UN%20SDG-11%20%26%2012-orange.svg)](https://sdgs.un.org/)

---

## 🌟 Overview

The **AI Waste Segregation Guide** addresses one of the most critical urban environmental crises: **source-level waste contamination**. When households discard food remnants, greasy cartons, or hazardous lithium batteries into general recycling streams, entire batches at Material Recovery Facilities (MRFs) become contaminated and are diverted to open landfills.

This project delivers a zero-latency, high-accuracy web application combining **real-time camera scanning**, **50+ item municipal encyclopedia**, **carbon offset analytics**, **a 60-second gamified sorting challenge**, and **interactive GIS facility mapping**.

---

## 🚀 Key Features

### 1. 🔬 AI Vision Waste Scanner
- **Dual Input Capability**: Live WebRTC camera feed with animated scanning reticle HUD or drag-and-drop file upload.
- **Quick Test Tray**: 1-click evaluator demo tray featuring common benchmark items (PET bottles, banana peels, batteries, soda cans, pizza boxes, etc.).
- **AI Recognition Engine**: Instant client-side visual classification with confidence scoring, matched against an extensive 50+ item municipal environmental knowledge base.
- **Actionable Guidance**: Automatic bin stream assignment (**Green**, **Blue**, **Red**, **Black**), decomposition countdown, contamination hazard rating, and pre-disposal preparation protocols (e.g. rinsing, flattening, terminal taping).

### 2. 💬 Conversational AI Waste Chatbot ("EcoBot AI")
- **Domain-Specific Conversational Assistant**: Users can ask natural language questions about any waste item, tricky materials, or municipal segregation rules.
- **Intelligent Guidance Engine**: Understands complex scenarios (e.g. clean vs. greasy pizza boxes, broken ceramics, blister packs, electronics, composting ratios).
- **Interactive Prompts**: Quick question chips, typing indicator, clear chat history, and instant synthesized audio chimes.

### 3. 📚 Interactive Waste Encyclopedia
- 50+ household and industrial waste items mapped to standard municipal color codes.
- Real-time search by item name, material keyword, or decomposition period.
- Comprehensive preparation checklists and circular economy upcycling tips.

### 4. 📊 Eco-Impact Tracker & Analytics Dashboard
- Persistent browser storage (`localStorage`) tracking items segregated, daily streaks, and cumulative avoided carbon emissions ($kg \text{ CO}_2$).
- Dynamic stream ratio bars and gamified achievement milestone badges.
- **Exportable Eco-Audit Certificate**: Generates a clean, formal printable verification document for academic or municipal audits.

### 5. 🎮 "Bin The Waste" Gamified Challenge
- Interactive 60-second waste sorting simulator.
- Real-time combo multipliers, dynamic audio feedback synthesized via the Web Audio API, and educational correction tips for mistaken categories.

### 6. 📍 Nearby Recycling Facility Locator
- Interactive Leaflet.js GIS map with custom pins for Material Recovery Facilities (MRFs), Municipal Composting Plants, and Authorized E-Waste Drop-offs.
- Radius search, accepted materials listing, and contact details.

### 7. 📄 Academic Project Dossier
- Built-in SRS documentation, System Architecture, DFD Level 0 & 1 diagrams, and mathematical carbon formulation viewable directly in the app.

---

## 📁 Project Directory Structure

```text
ai-waste-segregation-guide/
├── index.html              # Main Single-Page Application (SPA)
├── server.py               # Lightweight Python 3.11 HTTP local server
├── start.bat               # One-click Windows launch script
├── README.md               # GitHub project repository documentation
├── css/
│   └── styles.css          # Eco-futuristic dark glassmorphism design system
├── js/
│   ├── app.js              # Master coordinator, sound synthesizer, router
│   ├── waste-data.js       # 50+ item knowledge base & municipal bins rules
│   ├── scanner.js          # WebRTC camera, canvas capture, AI vision logic
│   ├── chatbot.js          # Conversational EcoBot AI assistant engine
│   ├── tracker.js          # Carbon calculation, badges, audit certificate
│   ├── quiz.js             # "Bin The Waste" 60-second interactive challenge
│   └── map.js              # Leaflet GIS facility locator & custom markers
└── docs/
    ├── PROJECT_REPORT.md   # Formal academic internship project report
    └── VIVA_PRESENTATION_CHEATSHEET.md # Viva Q&A preparation guide
```

---

## ⚡ Quickstart Guide

### Running on Windows
1. Double-click **`start.bat`**.
2. The Python HTTP server will initialize on `http://127.0.0.1:8000/index.html` and automatically open your default browser.

### Running via Terminal
```bash
# Navigate to the project folder
cd C:\Users\sahil\.gemini\antigravity-ide\scratch\ai-waste-segregation-guide

# Start the server
python server.py
```

---

## 🧮 Carbon Offset Formulation

The system estimates carbon savings using standard Life Cycle Assessment (LCA) emission differentials:

$$C_{\text{offset}} = \sum_{i=1}^{n} \left( W_i \times (E_{\text{landfill}} - E_{\text{recycled}}) \right)$$

- Diverting organic wet waste prevents anaerobic methane ($CH_4$) generation ($GWP_{100} = 28$).
- Recycling aluminum cans saves **95%** of the electrical energy required to smelt virgin bauxite ore.

