# Retail Sales & Profitability Analytics

**End-to-End Data Analytics Case Study**

Python · SQL · Power BI · Excel · Pandas · NumPy

---

## Overview

This project analyzes **9,994 retail transactions** from the Sample Superstore dataset to understand sales performance, profitability, discount behaviour, product economics, and regional performance.

The analysis is structured around one business question:

> **Where is the business generating revenue, and where is that revenue failing to translate into profit?**

The project moves from data validation and exploratory analysis to business diagnosis and actionable recommendations.

---

## Executive Snapshot

| Sales | Profit | Profit Margin | Orders | Customers |
|---:|---:|---:|---:|---:|
| **$2.30M** | **$286.40K** | **12.47%** | **5,009** | **793** |

| Additional KPI | Value |
|---|---:|
| Products | 1,862 |
| Quantity Sold | 37,873 |
| Average Order Value | $458.61 |

---

## Business Questions

This analysis investigates:

1. Is sales growth translating into profit growth?
2. Which categories and sub-categories create the most value?
3. Which products generate losses?
4. How does discounting relate to profitability?
5. Which regions and customer segments perform best?
6. Where are profitability problems concentrated?

---

## Key Findings

### 1. Furniture generates revenue, but weak profit

| Category | Sales | Profit | Margin |
|---|---:|---:|---:|
| Technology | $836.15K | **$145.45K** | **17.40%** |
| Office Supplies | $719.05K | **$122.49K** | **17.04%** |
| Furniture | $742.00K | **$18.45K** | **2.49%** |

Furniture generated approximately **$742K in sales**, but only **$18.45K in profit**.

A deeper sub-category analysis shows where the problem is concentrated.

| Furniture Sub-category | Profit | Margin |
|---|---:|---:|
| **Tables** | **-$17.73K** | **-8.56%** |
| **Bookcases** | **-$3.47K** | **-3.02%** |
| Furnishings | $13.06K | 14.24% |
| Chairs | $26.59K | 8.10% |

**Tables is the largest sub-category profitability concern.**

---

### 2. Higher discounts are associated with weaker profitability

| Discount Band | Profit Margin | Loss-making Record Rate |
|---|---:|---:|
| **0%** | **29.51%** | **0%** |
| 1–10% | 16.61% | 4.26% |
| 11–20% | 11.58% | 13.99% |
| 21–30% | **-10.05%** | 91.63% |
| 31–40% | **-19.44%** | 88.84% |
| 41–60% | **-40.74%** | 100% |
| >60% | **-122.63%** | 100% |

The Pearson correlation between **Discount and Profit is approximately -0.220**.

> This is a descriptive association, not proof of causation. Product mix, category, region, and customer composition may also influence profitability.

---

### 3. Regional profitability is uneven

| Region | Sales | Profit | Margin |
|---|---:|---:|---:|
| **West** | $725.46K | **$108.42K** | **14.94%** |
| East | $678.78K | $91.52K | 13.48% |
| South | $391.72K | $46.75K | 11.93% |
| Central | $501.24K | $39.71K | **7.92%** |

The weakest Region × Category combination identified in the analysis is:

**Central × Furniture**

- Sales: approximately **$163.80K**
- Profit: approximately **-$2.87K**
- Margin: approximately **-1.75%**

This shows why regional performance needs to be analyzed together with category performance.

---

### 4. Sales growth should be evaluated with profitability

Sales increased from approximately **$484K in 2014** to approximately **$733K in 2017**.

However, sales and profit did not move proportionally in every year.

In **2015**:

- Sales decreased by approximately **2.83%**
- Profit increased by approximately **24.37%**

This demonstrates why revenue growth alone is not sufficient to evaluate business performance.

---

### 5. Profit is concentrated

| Product Group | Share of Total Profit |
|---|---:|
| Top 10 products | **23.21%** |
| Top 20 products | **32.23%** |

A meaningful share of total profit comes from a relatively small group of products, making product-level profitability and concentration important areas for management attention.

---

## Analytical Approach

```text
Raw Data
   ↓
Data Quality Audit
   ↓
Data Cleaning & Preparation
   ↓
Exploratory Data Analysis
   ↓
KPI & Time Analysis
   ↓
Category / Sub-category Analysis
   ↓
Product Profitability
   ↓
Discount Analysis
   ↓
Regional & Customer Analysis
   ↓
Business Diagnosis
   ↓
Recommendations
```

---

## Data Quality

The dataset was audited before analysis.

| Check | Result |
|---|---:|
| Records | 9,994 |
| Columns | 21 |
| Duplicate Rows | **0** |
| Missing Values | **0** |
| Invalid Dates | **0** |
| Ship Before Order | **0** |
| Negative / Zero Sales | **0** |
| Negative / Zero Quantity | **0** |
| Negative-profit Records | **1,871** |

Negative-profit records were intentionally retained because they are necessary for understanding the true profitability picture.

---

## Business Recommendations

### Pricing & Discount Governance
Review high-discount transactions and evaluate category-specific discount thresholds.

### Furniture Profitability
Investigate Tables and Bookcases at product, discount, and regional level before making pricing or assortment decisions.

### Regional Strategy
Investigate Central × Furniture separately rather than treating the entire Central region as underperforming.

### Executive KPI Reporting
Track **Sales, Profit, and Profit Margin together**.

### Product Concentration
Monitor dependence on high-profit products and identify opportunities to broaden the profit base.

---

## Technical Stack

| Area | Tools |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Querying | SQL |
| Business Intelligence | Power BI, DAX |
| Spreadsheet Analysis | Microsoft Excel |
| Methods | Data Cleaning, EDA, KPI Analysis, Time-Series Analysis, Profitability Analysis |

---

## Repository Structure

```text
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
```

---

## Project Status

| Component | Status |
|---|:---:|
| Data Quality Audit | Complete |
| Data Cleaning | Complete |
| KPI Analysis | Complete |
| Time Trend Analysis | Complete |
| Category Analysis | Complete |
| Sub-category Analysis | Complete |
| Product Profitability | Complete |
| Discount Analysis | Complete |
| Regional Analysis | Complete |
| Customer Analysis | Complete |
| Business Diagnosis | Complete |
| SQL Analysis Layer | Complete |
| Power BI Dashboard | Next |
| Predictive Modelling | Future |

---

## What This Project Demonstrates

This case study demonstrates an end-to-end approach to data analytics:

**Business Question → Data Validation → Analysis → Evidence → Insight → Recommendation**

The focus is not only on producing visualizations, but on identifying **where performance changes, where profitability is concentrated or lost, and what business questions should be investigated next**.

---

## Future Enhancements

- Interactive Power BI executive dashboard
- Advanced SQL analysis and window functions
- Statistical testing of discount-profit relationships
- Customer segmentation
- Predictive profitability modelling
- Automated reporting

---

## Project Context

**Type:** Independent Portfolio Project  
**Domain:** Retail Analytics  
**Dataset:** Sample Superstore  
**Analysis Period:** 2014–2017

This project is an independent portfolio case study created to demonstrate practical data analytics skills. The dataset is a public/sample dataset and does not represent employer or client work.
