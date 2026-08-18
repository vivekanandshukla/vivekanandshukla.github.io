# Retail Sales & Profitability Analytics

> Data Analytics Case Study | Python | SQL | Excel | Power BI

## 📌 Project Overview

This project analyzes retail transaction data to understand sales performance, profitability, customer behavior, product performance, regional performance, and the relationship between discounting and profit.

The objective is to convert raw transaction data into meaningful business insights that can support better pricing, product, and sales decisions.

---

## 🎯 Business Questions

- Where is revenue coming from?
- Where is profit generated or lost?
- Does higher sales always mean higher profit?
- How does discounting affect profitability?
- Which categories and sub-categories perform poorly?
- Which products generate losses?
- Which regions and customer segments are most profitable?
- How does business performance change over time?

---

## 📊 Dataset

**Dataset:** Sample Superstore

- **Records:** 9,994
- **Columns:** 21
- **Orders:** 5,009
- **Customers:** 793
- **Products:** 1,862
- **Order Period:** 2014–2017

---

## 🔍 Data Quality

The raw dataset was audited before analysis.

- Duplicate rows: **0**
- Missing values: **0**
- Invalid dates: **0**
- Ship-before-order records: **0**
- Negative/zero Sales: **0**
- Negative/zero Quantity: **0**
- Negative-profit records: **1,871**

Negative-profit records were intentionally retained because identifying loss-making transactions is an important part of profitability analysis.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- SQL
- Excel
- Power BI
- Exploratory Data Analysis
- Data Visualization
- Business Intelligence

---

## 🔄 Analytical Workflow

```text
Raw Dataset
     ↓
Data Quality Audit
     ↓
Data Cleaning
     ↓
- Exploratory Data Analysis
     ↓
Business KPI Analysis
     ↓
Category & Product Analysis
     ↓
Discount Analysis
     ↓
Regional & Customer Analysis
     ↓
Business Insights
     ↓
Recommendations

📈 Key KPIs
| KPI | Value |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Profit Margin | 12.47% |
| Total Quantity | 37,873 |
| Total Orders | 5,009 |
| Total Customers | 793 |
| Total Products | 1,862 |
| Average Order Value | $458.61 |
| Average Profit / Order | $57.18 |
💡 Key Findings
Category Performance

Technology generated the highest profit at approximately $145.45K with a 17.40% profit margin.

Office Supplies generated approximately $122.49K profit with a 17.04% margin.

Furniture generated approximately $18.45K profit despite approximately $742K in sales, resulting in only a 2.49% margin.

Sub-category Performance

Tables was the weakest sub-category by aggregate profit:

Sales: ~$206.97K
Profit: ~-$17.73K
Profit Margin: -8.56%

Bookcases also generated an aggregate loss:

Profit: ~-$3.47K
Profit Margin: -3.02%
Regional Performance

The West region generated the highest aggregate profit at approximately $108.42K.

The Central region generated approximately $39.71K profit on approximately $501.24K sales, resulting in a 7.92% margin.

The weakest Region × Category combination was:

Central × Furniture → approximately -$2.87K profit

Time Trend

Sales increased from approximately $484K in 2014 to approximately $733K in 2017.

However, sales growth did not always translate proportionally into profit growth.

For example, in 2015, sales decreased by approximately 2.83%, while profit increased by approximately 24.37%.

Discount & Profitability

A strong descriptive relationship was observed between higher discount levels and weaker profitability.

At 0% discount:

Sales: ~$1.088M
Profit: ~$321K
Margin: 29.51%
Loss-making records: 0%

At discounts above 40%, all records in the corresponding discount bands were loss-making in this dataset.

The Pearson correlation between Discount and Profit is approximately -0.220.

Correlation indicates association; it does not prove that discount alone causes the observed profit changes.

🎯 Business Recommendations
- Review high-discount transactions and discount approval policies.
- Investigate Tables and Bookcases at product and regional level.
- Monitor profit margin alongside sales growth.
- Analyze Central-region Furniture performance separately.
- Review loss-making products before making assortment or pricing decisions.
- Use category-specific discount strategies rather than applying one universal discount rule.
📁 Project Structure
retail-sales-profitability/
│
├── README.md
│
├── data/
│   └── cleaned_superstore.csv
│
├── notebooks/
│   ├── 01_audit_and_kpis.py
│   └── 02_eda.py
│
├── sql/
│   └── business_questions.sql
│
└── images/
    ├── 01_monthly_sales_profit.png
    ├── 02_profit_by_category.png
    ├── 03_profit_by_subcategory.png
    └── 04_profit_by_region.png
📚 What I Learned

Through this project, I worked through an end-to-end analytics workflow involving:

- Data quality assessment
- Data cleaning
- Exploratory Data Analysis
- KPI development
- Time-series analysis
- Product and category profitability
- Discount analysis
- Customer and regional analysis
- SQL-based business analysis
- Business insight generation
- Data-driven recommendations
🚀 Future Improvements
- Build an interactive Power BI executive dashboard
- Add advanced SQL analysis
- Add statistical analysis of discount and profitability
- Perform deeper customer segmentation
- Develop predictive profitability models
- Add automated reporting
⚠️ Project Disclaimer

This is an independent portfolio project created for learning and demonstrating practical data analytics skills.

The analysis and findings are based on the supplied Sample Superstore dataset and should not be interpreted as professional employment experience.
