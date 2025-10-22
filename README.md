
## 💄 Chiffon Cosmetics – Sales Tools

⚠️ **Note:** This repository contains a **simplified demonstration** of the original *Chiffon Cosmetics* pricing and sales automation solution.  
All client data and proprietary logic have been replaced with mock datasets to illustrate the approach, technical design, and end-to-end workflow.

---

### 🎯 Purpose & Business Value
A lightweight, browser-based business intelligence (BI) solution built for small cosmetic retailers.  
The tools require **no installation** and rely entirely on **free-tier software** such as Excel and Power BI for downstream analysis.

The system:
- Calculates **net selling prices** by factoring in purchase costs, distribution, marketing, salaries, commissions, and taxes.  
- Tracks **daily sales** and exports monthly reports in CSV format.  
- Generates **Power BI–ready** data without needing a backend database or paid infrastructure.

This project demonstrates how small businesses can automate pricing and sales operations using only browser technologies and familiar desktop tools—bridging data collection, transformation, and visualization in a single workflow.

---

### 🛠 Tools & Technical Approach
This demonstration focuses on **workflow design, data handling, and business logic**, not on complex UI frameworks or backend systems.

**Key Technologies**
- 💻 **JavaScript** – Handles dynamic calculations, input validation, and user interactions.  
- 🌐 **HTML/CSS** – Builds a responsive, easy-to-use browser interface.  
- 📂 **PapaParse** – Parses and generates CSV files for import/export.  
- 💾 **LocalStorage** – Stores pricing and sales data locally across browser sessions.  
- ⚙️ **Power Query + DAX** – Perform ETL and data modeling for Power BI dashboards.

---

### 🚀 Project Highlights
- 📦 **Selling Price Calculator** – Factors in distribution, marketing, salaries, commissions, taxes, and other overheads to compute accurate net selling prices.  
- 💄 **Sales Tracking Sheet** – Browser-based sales log for daily transactions; calculates totals and exports monthly CSVs.  
- 🔄 **Automation & Consistency** – Reduces manual data entry errors and maintains consistent, reporting-ready outputs.  
- 🧩 **End-to-End Workflow** – Demonstrates how pricing data feeds into sales operations and Power BI dashboards using a zero-dependency, in-browser solution.  
- 🪶 **No Infrastructure Costs** – Operates entirely within the browser, avoiding database setup or server hosting.  

---

### 📂 Folder Structure
```
Chiffon-Cosmetics/
├─ data/
│  ├─ monthly_sales/
│  ├─ price_list/
│  └─ selling_price/
├─ CombinedSales.csv
├─ Chiffon Cosmetics - Sales Sheet.html
├─ Chiffon Cosmetics - Selling Price Calculator.html
├─ chiffon_sales_dashboard.pbix
├─ chiffon_sales_dashboard.pdf
└─ demo_videos/
    ├─ selling_price_calculator.mp4
    ├─ sales_sheet.mp4
    ├─ etl_process.mp4
    └─ powerbi_dashboard.mp4
```

---

### 🎥 Demo Videos & ETL Workflow

This project includes **segmented, silent demonstration videos** embedded directly for playback in GitHub.

#### 📹 Video Segments

2️⃣ **Selling Price Calculator**  
- Demonstrates loading a sample product CSV, automatic cost breakdown, and net price computation.  
- Exports the computed prices to CSV.  

```html
<video width="600" controls>
  <source src="demo_videos/selling_price_calculator.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

3️⃣ **Sales Sheet**  
- Imports the price list from the calculator output.  
- Records daily sales, updates totals dynamically, and exports monthly CSV reports.

```html
<video width="600" controls>
  <source src="demo_videos/sales_sheet.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

4️⃣ **Power Query ETL Process**  
- Combines multiple monthly CSVs using Power Query.  
- Renames columns and reformats dates (`dd/mm/yyyy` → `yyyy-mm-dd`) for Power BI.  
- Outputs a consolidated `CombinedSales.csv`.

```html
<video width="600" controls>
  <source src="demo_videos/etl_process.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

5️⃣ **Power BI Dashboard**  
- Demonstrates data refresh and navigation in Power BI.

```html
<video width="600" controls>
  <source src="demo_videos/powerbi_dashboard.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

---

### 📊 Power BI Dashboards
Include screenshots or link to the static PDF for reviewers who cannot open `.pbix` files:

📄 **Dashboard Preview (PDF):** [`chiffon_sales_dashboard.pdf`](chiffon_sales_dashboard.pdf)  
💾 **Power BI File:** [`chiffon_sales_dashboard.pbix`](chiffon_sales_dashboard.pbix)

---

### ✅ Summary
This repository demonstrates a **complete browser-based BI workflow**: from data generation to transformation to visualization using free, lightweight tools like HTML/JavaScript, Excel Power Query, and Power BI.  

It highlights **practical problem-solving, ETL design, and business logic implementation**, showing how small businesses can automate pricing and sales operations without costly infrastructure.
