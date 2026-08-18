Retail Sales & Profitability Analytics

End-to-End Data Analytics Case Study

Python · Pandas · SQL · Excel · Power BI · Exploratory Data Analysis

A practical analysis of 9,994 retail transactions to understand sales growth, profitability, discount behavior, product performance, and regional business performance.

Executive Summary

This project examines retail transaction data from 2014–2017 to answer a core business question:

Where is the business generating revenue, and where is that revenue failing to translate into profit?

The analysis moves from overall KPIs to time trends, category and sub-category performance, product profitability, discount behavior, regional performance, and customer segments.

Business Snapshot

Metric

Result

Sales

$2.30M

Profit

$286.40K

Profit Margin

12.47%

Orders

5,009

Customers

793

Products

1,862

Quantity Sold

37,873

Average Order Value

$458.61

Business Problem

Strong sales do not necessarily indicate strong business performance.

The analysis therefore focuses on the relationship between:

Revenue → Profit → Margin → Discount → Product → Region → Customer

The objective is to identify areas where management may need to review pricing, discounting, product performance, and regional strategy.

Key Business Questions

Is sales growth translating into profit growth?

Which categories and sub-categories create the most value?

Which products are generating losses?

How strongly is discounting associated with profitability?

Which regions and customer segments perform best?

Where are the major profitability risks concentrated?

Analytical Approach

Raw Transaction Data
        │
        ▼
Data Quality Audit
        │
        ▼
Data Cleaning & Preparation
        │
        ▼
Exploratory Data Analysis
        │
        ├── Time Trends
        ├── Category / Sub-category
        ├── Product Profitability
        ├── Discount Analysis
        ├── Regional Analysis
        └── Customer Analysis
        │
        ▼
Business Diagnosis
        │
        ▼
Recommendations

Data Quality

The dataset was audited before analysis.

Quality Check

Result

Records

9,994

Columns

21

Duplicate Rows

0

Missing Values

0

Invalid Dates

0

Ship Before Order

0

Negative / Zero Sales

0

Negative / Zero Quantity

0

Negative-Profit Records

1,871

Important: Loss-making records were retained. Removing them would artificially improve the profitability picture.

Key Findings

01 — Sales Growth Did Not Always Mean Better Profitability

Sales increased from approximately $484K in 2014 to $733K in 2017.

However, sales and profit did not move proportionally every year.

In 2015:

Sales decreased by approximately 2.83%

Profit increased by approximately 24.37%

This demonstrates why sales growth should be evaluated together with profitability and margin.

02 — Furniture Is the Major Category-Level Profitability Concern

Category

Sales

Profit

Margin

Technology

$836.15K

$145.45K

17.40%

Office Supplies

$719.05K

$122.49K

17.04%

Furniture

$742.00K

$18.45K

2.49%

Furniture generates substantial revenue but comparatively little profit.

The analysis therefore goes one level deeper.

Furniture Sub-category

Sub-category

Profit

Margin

Tables

-$17.73K

-8.56%

Bookcases

-$3.47K

-3.02%

Furnishings

$13.06K

14.24%

Chairs

$26.59K

8.10%

Tables is the largest profitability problem within Furniture.

03 — Discounting Shows a Strong Negative Profitability Association

Discount Band

Profit Margin

0%

29.51%

1–10%

16.61%

11–20%

11.58%

21–30%

-10.05%

31–40%

-19.44%

41–60%

-40.74%

>60%

-122.63%

At 0% discount, there were no loss-making records.

At discounts above 40%, all records in the corresponding bands were loss-making in this dataset.

The Pearson correlation between Discount and Profit is approximately -0.220.

This is a descriptive association, not proof that discounting alone causes the observed losses. Product mix, category, region, and customer composition may also influence profitability.

04 — Regional Performance Is Uneven

Region

Sales

Profit

Margin

West

$725.46K

$108.42K

14.94%

East

$678.78K

$91.52K

13.48%

South

$391.72K

$46.75K

11.93%

Central

$501.24K

$39.71K

7.92%

The Central × Furniture combination is particularly weak:

Sales: ~$163.80K
Profit: ~-$2.87K
Margin: -1.75%

This suggests that regional analysis should not stop at region-level totals; category-level decomposition is necessary.

05 — Profit Is Concentrated Across Products

The most profitable products contribute a meaningful share of total profit:

Top 10 products: ~23.21% of total profit

Top 20 products: ~32.23% of total profit

This creates an additional management question:

How dependent is overall profitability on a relatively small group of products?

Business Recommendations

1. Review high-discount transactions

Introduce stronger discount governance, particularly for transactions with discounts above 20%.

2. Investigate Tables and Bookcases

Review pricing, discounting, product cost structure, and regional performance before making assortment decisions.

3. Monitor margin alongside revenue

Executive reporting should track Sales + Profit + Profit Margin, rather than revenue alone.

4. Investigate Central × Furniture

This combination should receive targeted analysis rather than treating the entire Central region as underperforming.

5. Identify loss-making products

Products with persistent negative profitability should be reviewed for pricing, discounting, demand, and strategic importance.

6. Use category-specific discount policies

A single discount policy may not be appropriate across all product categories.

Technical Implementation

Data Analysis

Python

Pandas

NumPy

Exploratory Data Analysis

Data Cleaning

Data Transformation

Business Intelligence

Power BI

DAX

KPI Design

Dashboard Development

Database / Querying

SQL

Aggregation

Business Queries

Customer / Product Analysis

Spreadsheet Analysis

Microsoft Excel

Data Validation

Analytical Calculations

Repository Structure

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

Project Outputs

Data Preparation

Raw data audit

Data quality assessment

Cleaned analytical dataset

Derived analytical fields

Analysis

KPI analysis

Time-series analysis

Category analysis

Sub-category analysis

Product profitability

Discount analysis

Regional analysis

Customer analysis

Business Outcome

Profitability diagnosis

Risk areas

Business recommendations

Reproducible analytical workflow

Future Enhancements

Build an interactive Power BI executive dashboard

Add advanced SQL analysis

Add statistical testing for discount-profit relationships

Build customer segmentation

Develop predictive profitability models

Automate recurring business reporting

Add drill-through and interactive dashboard views

What This Project Demonstrates

This case study demonstrates the ability to move beyond basic visualization and follow an end-to-end analytical process:

Business Question → Data → Analysis → Evidence → Insight → Recommendation

Disclaimer

This is an independent portfolio project created to demonstrate practical data analytics skills.

The findings are calculated from the supplied Sample Superstore dataset. They do not represent professional employment work or employer/client data.
