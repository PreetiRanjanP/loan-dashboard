
# 💰 Loan Portfolio Analytics Dashboard
### End-to-End Data Engineering & Business Intelligence Project

An operational intelligence platform built for a Gold Loan NBFC (Non-Banking Financial Company) to monitor loan health, asset growth (AUM), and risk metrics (NPA).

---

## 🚀 Project Overview
This project demonstrates a full-stack data workflow—from generating synthetic banking data to hosting a live interactive dashboard and building a professional BI report. It helps stakeholders identify high-risk branches and track monthly disbursement trends.

live deploy :- https://loan-dashboardgit-4sdcdtg3jcshbw6hprjeyf.streamlit.app/

## 📸 Dashboard Preview (Power BI)
![Loan Portfolio Dashboard](https://github.com/PreetiRanjanP/loan-dashboard/raw/main/Screenshot%202026-04-06%20121624.png)
*Professional Power BI dashboard featuring KPI cards, trend analysis, and multi-dimensional slicers.*

---

## 🛠️ Tech Stack
| Category | Technology |
| :--- | :--- |
| **Data Generation** | Python (Faker, NumPy, Pandas) |
| **Database** | MySQL (Relational Schema Design) |
| **Visualization 1** | Streamlit (Python Web Framework) |
| **Visualization 2** | Power BI (DAX, Interactive Reporting) |
| **Deployment** | Vercel / GitHub Actions |

---

## 📊 Key Features & Metrics
- **AUM Tracking:** Real-time monitoring of Assets Under Management.
- **NPA Analysis:** Automated calculation of Non-Performing Assets (NPA Rate %) to assess portfolio risk.
- **Dynamic Filtering:** Slicers for Branch-wise (Kolkata, Bhubaneswar, etc.), Status, and Loan Type analysis.
- **Trend Forecasting:** Monthly disbursement line charts to identify seasonal growth.
- **Relational Integrity:** Python-to-MySQL pipeline for structured data storage.

## 🏗️ Project Architecture
1. **Data Layer:** Synthetic generation of 1000+ loan records using `Faker`.
2. **Database Layer:** Cleaned data loaded into MySQL using `mysql-connector-python`.
3. **Logic Layer:** Custom Python functions (`analysis/`) to calculate financial KPIs.
4. **Presentation Layer:** - **Streamlit:** Fast, code-based operational tool.
   - **Power BI:** Executive-ready visual report using DAX measures.

---

## ⚙️ How to Run Locally

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/PreetiRanjanP/loan-dashboard.git
   cd loan-dashboard
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run Pipeline:**
   ```bash
   python data/generate_data.py  # Generate Data
   python db/load_data.py        # Load to MySQL
   streamlit run dashboard/app.py # Launch Dashboard
   ```
👤 Author
Preeti Ranjan Pradhan | "KEEP LEARNING"
