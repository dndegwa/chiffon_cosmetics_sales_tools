
## 💄 Chiffon Cosmetics – Sales Tools

⚠️ **Note:** This repository contains a **simplified demonstration** of the original *Chiffon Cosmetics* pricing and sales automation solution.  
All client data and proprietary logic have been replaced with mock datasets to illustrate the approach, technical design, and end-to-end workflow.

---

### 🎯 Purpose & Business Value
A lightweight, browser-based business intelligence (BI) solution built for small cosmetic retailers.  
Requires no installation and relies entirely on free-tier software such as Excel and Power BI for downstream analysis.

The system:
- Calculates net selling prices based on purchase costs, distribution, marketing, salaries, commissions, and taxes.  
- Tracks daily sales and exports monthly reports in CSV format.  
- Generates Power BI–ready data without a backend database or paid infrastructure.

This project demonstrates how small businesses can automate pricing and sales operations using browser technologies and familiar desktop tools—bridging data collection, transformation, and visualization in a single workflow.

### 🚀 Project Highlights
📦 **Selling Price Calculator** – Computes accurate net selling prices by incorporating distribution, marketing, and overhead costs.  
💄 **Sales Tracking Sheet** – Records daily transactions, calculates totals, and exports monthly CSVs.  
🧩 **End-to-End Workflow** – Connects pricing data to sales operations and Power BI dashboards.  
⚡ **No Infrastructure Costs** – Fully browser-based; no database or server required.

### 🛠 Tools & Technical Approach
This demonstration focuses on workflow design, data handling, and business logic, not on complex UI frameworks or backend systems.

**Key Technologies**  
💻 JavaScript – Dynamic calculations, input validation, and user interactions.  
🌐 HTML/CSS – Clean, responsive browser interface.  
📂 PapaParse – Parses and generates CSV files for import/export.  
💾 LocalStorage – Stores pricing and sales data across browser sessions.  
⚙️ Power Query + DAX – Perform ETL and data modeling for Power BI dashboards.

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

2️⃣ **Selling Price Calculator**  
<video width="600" controls>
  <source src="demo_videos/selling_price_calculator.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

3️⃣ **Sales Sheet**  
<video width="600" controls>
  <source src="demo_videos/sales_sheet.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

4️⃣ **Power Query ETL Process**  
<video width="600" controls>
  <source src="demo_videos/etl_process.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

5️⃣ **Power BI Dashboard**  
<video width="600" controls>
  <source src="demo_videos/powerbi_dashboard.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

### 📊 Power BI Dashboards

View the full dashboard or the static preview:

📄 **Dashboard Preview (PDF):** [`chiffon_sales_dashboard.pdf`](chiffon_sales_dashboard.pdf)  
💾 **Power BI File:** [`chiffon_sales_dashboard.pbix`](chiffon_sales_dashboard.pbix)

---

### ✅ Summary
This repository demonstrates a **complete browser-based BI workflow**: from data generation to transformation to visualization using free, lightweight tools like HTML/JavaScript, Excel Power Query, and Power BI.  

It highlights **practical problem-solving, ETL design, and business logic implementation**, showing how small businesses can automate pricing and sales operations without costly infrastructure.
