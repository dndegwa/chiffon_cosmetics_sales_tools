
## 💄 Chiffon Cosmetics – Sales Tools

### 📑 Table of Contents
1. [Purpose & Business Value](#-purpose--business-value)
2. [Tools & Technical Approach](#-tools--technical-approach)
3. [Folder Structure](#-folder-structure)
4. [Demo Videos & ETL Workflow](#-demo-videos--etl-workflow)
5. [Power BI Dashboards](#-power-bi-dashboards)
6. [Summary](#-summary)

 ---
   
⚠️ **Note:** This repository contains a **simplified demonstration** of the original *Chiffon Cosmetics* pricing and sales automation solution.  
All client data and proprietary logic have been replaced with mock datasets to illustrate the approach, technical design, and end-to-end workflow.

---

### 🎯 Purpose & Business Value
A lightweight, browser-based business intelligence (BI) solution built for small cosmetic retailers—designed to automate pricing, sales tracking, and reporting without paid infrastructure.

The system:
- **Calculates net selling prices** based on purchase costs, distribution, marketing, salaries, commissions, and taxes.  
- **Tracks daily sales** and exports monthly reports in CSV format.  
- **Generates Power BI–ready data** using browser-based tools and Power Query for ETL.  
- **Eliminates manual errors** and ensures consistent, reporting-ready outputs.

By combining a **Selling Price Calculator**, a **Sales Tracking Sheet**, and **Power BI Dashboards**, this project demonstrates how small businesses can achieve end-to-end automation—from pricing and data collection to visualization—entirely within the browser and Excel ecosystem.

⚡ **Key Advantage:** Zero setup, zero backend — all logic runs locally in the browser.

---

### 🛠 Tools & Technical Approach
This demonstration focuses on workflow design, data handling, and business logic, not on complex UI frameworks or backend systems.

**Key Technologies**  
💻 JavaScript + HTML/CSS – UI, Dynamic calculations, input validation, and user interactions.  
📂 PapaParse – Parses and generates CSV files for import/export.  
💾 Browser LocalStorage – Stores pricing and sales data across browser sessions.  
⚙️ Power Query + DAX – Perform ETL and data modeling for Power BI dashboard.

---

### 📂 Folder Structure
```
Chiffon-Cosmetics/
├─ data/
│  ├─ monthly_sales/
│  ├─ price_list/
│  └─ selling_price/
│ 
├─ CombinedSales.csv
├─ Chiffon Cosmetics - Sales Sheet.html
├─ Chiffon Cosmetics - Selling Price Calculator.html
├─ chiffon_sales_dashboard.pbix
├─ chiffon_sales_dashboard.pdf
│ 
└─ demo_videos/
    ├─ selling_price_calculator.mp4
    ├─ sales_sheet.mp4
    ├─ etl_process.mp4
    └─ powerbi_dashboard.mp4
```

---

### 🎥 Demo Videos & ETL Workflow

Segmented, silent demonstration videos showcase the workflow:

1️⃣ **Selling Price Calculator**  
[![Watch Video](demo_videos/selling_price_calculator_thumbnail.png)](demo_videos/selling_price_calculator.mp4)

2️⃣ **Sales Sheet**  
[![Watch Video](demo_videos/sales_sheet_thumbnail.png)](demo_videos/sales_sheet.mp4)

3️⃣ **Power Query ETL Process**  
[![Watch Video](demo_videos/etl_process_thumbnail.png)](demo_videos/etl_process.mp4)

4️⃣ **Power BI Dashboard**  
[![Watch Video](demo_videos/powerbi_dashboard_thumbnail.png)](demo_videos/powerbi_dashboard.mp4)

---

### 📊 Power BI Dashboards

View the full dashboard or the static preview:

📄 **Dashboard Preview (PDF):** [`chiffon_sales_dashboard.pdf`](chiffon_sales_dashboard.pdf)  
💾 **Power BI File:** [`chiffon_sales_dashboard.pbix`](chiffon_sales_dashboard.pbix)

---

### ✅ Summary
This repository demonstrates a **complete browser-based BI workflow**: from data generation to transformation to visualization using free, lightweight tools like HTML/JavaScript, Excel Power Query, and Power BI.  

It highlights **practical problem-solving, ETL design, and business logic implementation**, showing how small businesses can automate pricing and sales operations without costly infrastructure.
