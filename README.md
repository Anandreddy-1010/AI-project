# 🌞⚡ AIRES — AI Powered Adaptive Renewable Energy Optimizer

### *Next-Gen Renewable Energy Intelligence System*

[![Run Live Notebook](https://img.shields.io/badge/Run-Live%20Notebook-blue?style=flat-square&logo=jupyter)](#-setup--installation)
[![View Notebook Online](https://img.shields.io/badge/View-Notebook%20Online-informational?style=flat-square&logo=jupyter)](#-setup--installation)
[![Live Site](https://img.shields.io/badge/Live-Website-success?style=flat-square&logo=github)](https://anandreddy-1010.github.io/renewable-energy-optimizer-project/)
[![Python](https://img.shields.io/badge/Backend-Python%20%2F%20Jupyter-3776AB?style=flat-square&logo=python)](https://python.org)
[![Plotly](https://img.shields.io/badge/Visualization-Plotly-3f4f75?style=flat-square&logo=plotly)](https://plotly.com)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-00ff88?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Anandreddy-1010/renewable-energy-optimizer-project?style=flat-square)](https://github.com/Anandreddy-1010/renewable-energy-optimizer-project/stargazers)

> *"Next-generation AI system for smarter renewable energy decisions."*

An AI-driven optimizer that forecasts renewable energy output, routes energy intelligently between grid, load, and storage, and runs entirely in the cloud — so mentors, judges, and clients can explore the full system without installing anything.

### ⚡ Quick Start (30 seconds, zero install)
1. Click **[Run Cloud Notebook](https://mybinder.org/v2/gh/Anandreddy-1010/renewable-energy-optimizer-project/HEAD?filepath=MODEL.ipynb)** and wait for Binder to build (~1–3 min)
2. Click **Run All** inside the notebook
3. Or just visit the **[Live Website](https://anandreddy-1010.github.io/renewable-energy-optimizer-project/)** — no waiting required
4. Or scan the QR code below with your phone

## 📱 Scan to Open

<p align="center">
  <img src="project_qr_code.png" alt="Scan to open AIRES live project" width="220"/>
</p>

<p align="center"><i>Scan with your phone camera to instantly open the live dashboard — no typing, no install.</i></p>

## 🔗 Project Access Links

- **Live Website:** https://anandreddy-1010.github.io/renewable-energy-optimizer-project/
- **Run Cloud Notebook (Binder):** https://mybinder.org/v2/gh/Anandreddy-1010/renewable-energy-optimizer-project/HEAD?filepath=MODEL.ipynb
- **View Notebook Online (nbviewer):** https://nbviewer.org/github/Anandreddy-1010/renewable-energy-optimizer-project/blob/main/MODEL.ipynb
- **GitHub Repository:** https://github.com/Anandreddy-1010/renewable-energy-optimizer-project

---

## 📋 Table of Contents

- [Quick Start](#-quick-start-30-seconds-zero-install)
- [Scan to Open](#-scan-to-open)
- [Project Access Links](#-project-access-links)
- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Core Capabilities](#-core-capabilities)
- [System Architecture](#-system-architecture)
- [Dashboard Tabs](#-dashboard-tabs)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Screenshots](#-screenshots)
- [Setup & Installation](#-setup--installation)
- [Sample Output](#-sample-output)
- [Scalability & Production Readiness](#-scalability--production-readiness)
- [Future Improvements](#-future-improvements)
- [FAQ](#-faq)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [Acknowledgments](#-acknowledgments)
- [Contact & Support](#-contact--support)
- [License](#-license)
- [Conclusion](#-conclusion)

---

## 🔎 Overview

**AIRES** is an interactive, AI-powered dashboard that forecasts solar and wind energy generation, models real-time energy routing across grid/load/storage, and translates the results into plain-language insights — all from a single Jupyter Notebook that runs entirely in the browser via Binder/nbviewer, with zero local installation required.

Unlike a static ML notebook, AIRES presents its output as a **live, tabbed control dashboard**: real-time and 7-day forecast charts, 3D sun-path and wind-vector visualizations, an explainable-AI status panel, an automatic billing/savings estimator, and a conversational AI assistant — all driven by the same underlying forecasting and optimization engine.

---

## ❗ Problem Statement

Households, small businesses, and campuses adopting solar/wind power face a common set of challenges:

| Challenge | Reality |
|---|---|
| **Unpredictable output** | Solar and wind generation vary hour-to-hour with weather, making manual planning unreliable |
| **Inefficient routing** | Without optimization, excess power is wasted or costly grid import happens needlessly |
| **Opaque savings** | Most homeowners have no clear, real-time view of how much they're actually saving vs. the grid |
| **Technical barrier** | Existing energy monitoring tools are either too simplistic (no forecasting) or too complex (require engineering expertise) |
| **No early warning** | Shortage risk (e.g., cloudy days, low wind) is rarely flagged before it causes a grid dependency spike |

AIRES addresses all of these by combining forecasting, optimization, explainability, and cost analytics into one system that's understandable to a non-technical user.

---

## 🎯 Objectives

- ✅ Forecast solar and wind output over a rolling **7-day horizon**, refreshed on demand
- ✅ Simulate intelligent **energy routing** between grid, load, and storage
- ✅ Estimate **shortage probability** and **maximum shortage magnitude** over the next 24 hours
- ✅ Generate a real-time **billing snapshot**: grid import/export costs, net bill, and savings vs. a pure-grid baseline
- ✅ Provide an **Explainable AI panel** — plain-language system status (efficiency, resource class, active alerts)
- ✅ Support **voice-guided** and **conversational (AI Assistant)** interaction
- ✅ Visualize sun position and wind vectors in **interactive 3D**
- ✅ Run entirely in the cloud (Binder/nbviewer) — zero installation required for a live demo

---

## 🧩 Core Capabilities

| Capability | Description |
|---|---|
| 📊 **Forecast Engine** | Predicts solar and wind energy trends for short-term power planning |
| ⚡ **Energy Routing Logic** | Balances grid power, local demand, and battery activity through smart optimization |
| 🗣️ **Guided Demo** | Interactive widgets and voice feedback explain system behavior in real time |
| 📄 **Automated Reporting** | Generates structured system insights for reviews and presentations |

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                     JUPYTER NOTEBOOK (MODEL.ipynb)                │
│                                                                    │
│  ┌────────────────┐   ┌───────────────────┐   ┌────────────────┐ │
│  │ Data Layer      │──▶│ Forecast Engine    │──▶│ Optimization   │ │
│  │ Solar / Wind /  │   │ Solar + Wind       │   │ Grid / Load /  │ │
│  │ Temp / Cloud    │   │ 7-day projection   │   │ Storage router │ │
│  └────────────────┘   └───────────────────┘   └───────┬────────┘ │
│                                                         │          │
│                                                         ▼          │
│                                          ┌───────────────────────┐│
│                                          │  Explainable AI Layer  ││
│                                          │  Efficiency, shortage  ││
│                                          │  probability, alerts   ││
│                                          └───────────┬───────────┘│
│                                                       ▼             │
│                                          ┌───────────────────────┐│
│                                          │  Billing Engine        ││
│                                          │  Tariffs → Net bill →  ││
│                                          │  Savings vs. pure-grid ││
│                                          └───────────┬───────────┘│
└──────────────────────────────────────────────────────┼────────────┘
                                                         ▼
┌──────────────────────────────────────────────────────────────────┐
│              INTERACTIVE DASHBOARD (ipywidgets + Plotly)          │
│  Overview · Solar · Wind · Optimization · AI Assistant tabs       │
│  3D Sun Path · 3D Wind Vector · Earth+Sun View · Theme switcher   │
│  Voice output (pyttsx3) · Auto-Opt toggle · Animation toggle      │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Dashboard Tabs

| Tab | Contents |
|---|---|
| **Overview** | Live + 7-day forecast chart (Solar, Wind, Temperature), Explainable AI snapshot, Billing snapshot |
| **Solar** | Solar history & 7-day forecast chart, 3D Sun Path (live position), Earth + Sun 3D view with your location |
| **Wind** | Wind history & 7-day forecast chart, 3D Wind Vector (live + forecast), particle-style wind flow chart |
| **Optimization** | Solar vs. Wind vs. Shortage vs. Grid Import/Export chart against active load |
| **AI Assistant** | Conversational interface for querying system status, plus AI Predictive Weather Vision summaries |

**Controls:** Theme switcher (Light / Dark / Neon / Solar / Wind / Eco) · Animation toggle · Auto-Opt toggle · Voice toggle · Refresh, Stop, and Generate Report buttons.

---

## ⭐ Features

### 🔬 Forecasting & Routing
- Live + 7-day rolling forecast for solar and wind output, refreshed on demand
- Grid import/export, load, and shortage tracked together on one optimization chart
- Configurable active load baseline for shortage/surplus comparison

### ⚛️ 3D Explainability
- **Sun Path (3D)** — live sun position and today's arc, rendered per your location
- **Earth + Sun View** — approximate 3D globe showing your location and current sun direction
- **Wind Vector (3D)** — live wind speed/direction plus a turbulence ring and average forecast strength
- **Wind Flow (particle style)** — forecast index vs. flow-band scatter for at-a-glance wind variability

### 🧠 Explainable AI Snapshot
- Real-time solar/wind stability status and efficiency classification
- Shortage probability (next 24h) and estimated maximum shortage (kWh)
- Active weather/resource alerts (e.g., high cloud warning)

### 💰 Billing Snapshot
- Configurable grid import/export tariffs (₹/kWh)
- Estimated next-24h and 7-day net bill
- Savings comparison vs. a pure-grid (no renewables) baseline

### 🗣️ AI Assistant & Voice
- Conversational tab for asking about current system status
- AI Predictive Weather Vision — plain-language 24h solar/wind trend summary
- Optional spoken output via `pyttsx3`

### 🎨 Interface
- Five selectable dashboard themes (Light, Dark, Neon, Solar, Wind, Eco)
- One-click PDF/report generation
- QR code for instant mobile access to the live notebook

---

## 🛠️ Tech Stack

### Core
| Technology | Purpose |
|---|---|
| **Python & Jupyter Notebook** | Environment for modeling, experiments, and documentation |
| **NumPy · Pandas** | Data processing and simulation |
| **Plotly** | Interactive 2D/3D charts (forecasts, sun path, wind vectors) |

### Interaction
| Technology | Purpose |
|---|---|
| **ipywidgets** | Interactive tab/button/dropdown controls |
| **pyttsx3** | Optional offline text-to-speech for voice guidance |

### Deployment
| Platform | Role |
|---|---|
| **Binder** | One-click cloud execution of the full live notebook |
| **nbviewer** | Static, non-interactive preview while Binder builds |
| **GitHub** | Source control |

> Fully built on open-source tools and cloud-based runtimes, allowing instant execution on any device with no local setup.

---

## 🖼️ Screenshots

> Add exported PNGs of your dashboard to an `assets/` or `screenshots/` folder and reference them here, e.g.:

```markdown
![Overview Dashboard](assets/overview.png)
![3D Sun Path](assets/sun-path-3d.png)
![Optimization Chart](assets/optimization.png)
![Explainable AI Snapshot](assets/explainable-ai.png)
```

Recommended shots to include:
1. Landing/title panel with Core Capabilities
2. Overview tab — live & 7-day forecast chart
3. Solar tab — 3D Sun Path + Earth/Sun view
4. Wind tab — 3D Wind Vector + particle flow chart
5. Optimization tab — Solar vs Wind vs Grid chart
6. Explainable AI + Billing snapshot panel
7. AI Assistant tab

---

## 🚀 Setup & Installation

### Option A — Run instantly in the cloud (recommended for demos)
No installation needed.

1. Open the **[Run Cloud Notebook](https://mybinder.org/v2/gh/Anandreddy-1010/renewable-energy-optimizer-project/HEAD?filepath=MODEL.ipynb)** link above
2. Wait for the environment to build (first load may take 1–3 minutes)
3. `MODEL.ipynb` will open automatically — click **Run All**

### Option B — View a static preview (no execution)
Open the **[View Notebook Online](https://nbviewer.org/github/Anandreddy-1010/renewable-energy-optimizer-project/blob/main/MODEL.ipynb)** link — good for a quick look at outputs without waiting for a live kernel.

### Option C — Visit the live website
The project also has a hosted landing page at **[anandreddy-1010.github.io/renewable-energy-optimizer-project](https://anandreddy-1010.github.io/renewable-energy-optimizer-project/)**.

### Option D — Run locally

```bash
# Clone
git clone https://github.com/Anandreddy-1010/renewable-energy-optimizer-project.git
cd renewable-energy-optimizer-project

# Install dependencies
pip install -r requirements.txt

# (Optional) enable spoken output
pip install pyttsx3

# Launch
jupyter notebook MODEL.ipynb
```

Then, inside the notebook:
1. Click **🔄 Refresh** to load live and forecast data
2. Explore the **Overview**, **Solar**, **Wind**, and **Optimization** tabs
3. Go to the **AI Assistant** tab to start chatting with the system
4. Optional: run `set_email_password()` in a new cell to enable real Gmail alerts

---

## 📊 Sample Output

**Explainable AI Snapshot**
```
Solar is currently stable by 0.0 kWh, wind is stable by 0.0 kWh.
Solar efficiency ≈ 0.0% (Very Poor), Wind class: High Resource.
Shortage probability next 24h ≈ 44.4%, max shortage ≈ 35.4 kWh.
Active alerts: ☁ High cloud warning
```

**Billing Snapshot**
```
Tariffs → Grid import: ₹6.00/kWh, Grid export: ₹3.00/kWh
Next 24h net bill: ≈ ₹1, savings vs pure-grid: ≈ ₹3675
7-day net bill: ≈ ₹-1090, savings vs pure-grid: ≈ ₹23965
```

**AI Predictive Weather Vision**
```
Next 24h solar trend: stable. Next 24h wind trend: decreasing.
Average cloud cover ≈ 100%, max ≈ 100%. High cloud episodes are
likely – expect dips in solar output. Possible strong wind
intervals – good for wind harvesting.
```

---

## 📈 Scalability & Production Readiness

### Current Deployment
- Runs on Binder (free tier) with automatic build from this GitHub repo
- Static fallback via nbviewer for instant, non-interactive preview

### Recommended Production Additions
- Migrate the dashboard logic to a persistent web app (e.g. **Streamlit** or **Flask + Plotly Dash**) for instant load times and no Binder cold-start
- Add a database layer (e.g. SQLite/Postgres) to persist forecast history instead of recomputing per session
- Add authentication for multi-user/multi-site deployments
- Integrate real weather API feeds (e.g. Open-Meteo, OpenWeatherMap) to replace simulated inputs
- Containerize with Docker for consistent deployment across environments

---

## 🔮 Future Improvements

| Improvement | Impact | Complexity |
|---|---|---|
| **Battery storage modeling** | Model charge/discharge cycles for true grid-independence estimates | Medium |
| **Real weather API integration** | Replace simulated cloud/wind data with live meteorological feeds | Medium |
| **Persistent web deployment (Streamlit/Dash)** | Instant load, no Binder cold-start, shareable public URL | Medium |
| **Multi-site dashboard** | Support monitoring multiple installations from one interface | High |
| **Mobile app / PWA** | Field-usable interface for on-site monitoring | Medium |
| **Historical accuracy tracking** | Compare forecasted vs. actual output over time to improve trust | Medium |
| **Grid-tariff auto-sync** | Pull live utility tariff rates instead of manual entry | Low |

---

## 📁 Project Structure

```
renewable-energy-optimizer-project/
├── MODEL.ipynb                  # Core notebook — forecasting, optimization, dashboard
├── app.py                       # Supporting application logic
├── index.html                   # Landing page frontend asset
├── requirements.txt              # Python dependencies
├── project_qr_code.png           # QR code linking to the live site
├── AIRES_LOGO.png / Project logo.jpg   # Branding assets
├── ttsMP3.com_VoiceText_*.mp3     # Sample voice-guidance audio
├── assests/                      # Supporting assets (screenshots, etc.)
├── LICENSE                       # MIT License
└── README.md
```

---

## ❓ FAQ

**Q: Do I need to install anything to try this?**
No — use the [Live Website](https://anandreddy-1010.github.io/renewable-energy-optimizer-project/) or [Run Cloud Notebook](https://mybinder.org/v2/gh/Anandreddy-1010/renewable-energy-optimizer-project/HEAD?filepath=MODEL.ipynb) link and everything runs in your browser.

**Q: Why is Binder sometimes slow to load?**
Binder builds a fresh cloud environment on each first visit (or after inactivity), which can take 1–3 minutes. The Live Website and nbviewer links load instantly as alternatives while Binder builds.

**Q: Is the forecast data real or simulated?**
Currently simulated for demonstration purposes. See [Recommended Production Additions](#-scalability--production-readiness) for integrating live weather APIs.

**Q: Can I use this for my own home/business setup?**
Yes — clone the repo, adjust the tariff and load parameters to match your setup, and re-run the notebook. See [Setup & Installation](#-setup--installation).

**Q: Does the voice feature work on Binder/cloud?**
`pyttsx3` requires local audio output, so voice guidance works best when running the notebook locally. Cloud sessions may not produce audible output depending on the platform.

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork this repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request describing your change

For major changes, please open an issue first to discuss what you'd like to change.

---

## 🙏 Acknowledgments

- **Dayananda Sagar University**, Department of Computer Science & Engineering (AIML), for academic support
- **Binder / mybinder.org** and **nbviewer.org** for free cloud notebook execution and viewing
- **Plotly** and the open-source Python data science ecosystem

---

## 📬 Contact & Support

For questions, feedback, or collaboration inquiries, please open an [issue](https://github.com/Anandreddy-1010/renewable-energy-optimizer-project/issues) on this repository.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🏁 Conclusion

AIRES demonstrates that a single Jupyter Notebook can be transformed into a genuinely interactive, presentation-ready AI product — combining forecasting, optimization, explainability, and cost analytics into one cloud-runnable system. With 3D visual explainability and zero-install cloud execution via Binder, it's built to be explored by mentors, judges, and non-technical stakeholders alike, without ever opening a line of code.

**Forecast. Optimize. Explain.**

---

*Built with Python · Jupyter · Plotly · ipywidgets · pyttsx3 · Binder*
