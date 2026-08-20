# Customer Churn Prediction & Risk Analysis

An end-to-end customer churn analytics and machine learning project using Python, SQL, and Power BI.

## Project Overview

This project analyzes customer behavior and develops a machine learning model to predict customer churn.

The project follows an end-to-end analytics workflow covering data preprocessing, exploratory data analysis, feature engineering, SQL analysis, machine learning, threshold optimization, customer risk segmentation, and interactive business intelligence reporting.

The objective is to transform raw customer data into actionable insights that can help businesses identify customers at risk of churn and prioritize retention efforts.

## Business Problem

Customer churn is a major business challenge because losing existing customers can directly impact revenue and customer lifetime value.

The key business question addressed in this project is:

> **Which customers are most likely to churn, what customer characteristics are associated with churn, and how can businesses prioritize customers for retention efforts?**

The analysis combines descriptive analytics with predictive modeling to answer both:

* **What is happening?**
* **Which customers are likely to churn?**

## Dataset

The project uses the **Telco Customer Churn** dataset.

The dataset contains information related to:

* Customer demographics
* Tenure
* Services subscribed
* Contract type
* Internet service
* Payment method
* Monthly charges
* Total charges
* Billing preferences
* Customer churn status

The dataset contains **7,043 customer records**.

## Tools & Technologies

* **Python** — Data preprocessing, EDA, feature engineering, and machine learning
* **Pandas** — Data manipulation and analysis
* **NumPy** — Numerical operations
* **Scikit-learn** — Machine learning and model evaluation
* **Matplotlib** — Data visualization
* **SQL Server** — Data analysis and business queries
* **Power BI** — Interactive dashboard and business reporting
* **DAX** — Power BI measures and calculations
* **Jupyter Notebook** — Analysis and development environment

## Project Workflow

```text
Raw Customer Data
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis
        ↓
SQL Analysis
        ↓
Feature Engineering
        ↓
Train/Test Split
        ↓
Machine Learning Models
        ↓
Model Comparison
        ↓
Threshold Optimization
        ↓
Final Random Forest Model
        ↓
Customer Churn Prediction
        ↓
Risk Segmentation
        ↓
Power BI Dashboard
```

## Data Preparation

The raw customer data was processed to prepare it for analysis and machine learning.

Key preparation activities included:

* Data type validation
* Missing value handling
* Data consistency checks
* Numerical data validation
* Categorical data preparation
* Processed dataset generation
* Model-ready dataset preparation

The processed datasets are stored in the `data` directory.

## Exploratory Data Analysis

Exploratory analysis was performed to understand customer behavior and identify patterns associated with churn.

The analysis focused on:

* Customer churn distribution
* Contract type
* Tenure
* Monthly charges
* Internet service
* Payment method
* Customer services
* Customer profile characteristics

The findings were used to guide feature engineering and machine learning analysis.

## Feature Engineering

Additional features were created to improve customer-level analysis and model interpretability.

Engineered features include:

* **TenureGroup**
* **MonthlyChargeGroup**
* **AverageMonthlyValue**
* **ServiceCount**
* **HasSecurityOrSupport**
* **IsLongTermContract**
* **UsesPaperlessBilling**

These features help transform raw customer attributes into more meaningful analytical variables.

## SQL Analysis

SQL Server was used to perform customer churn analysis and generate business insights.

The SQL analysis includes customer-level and segment-level churn queries covering areas such as:

* Overall churn
* Retained vs churned customers
* Churn by contract
* Churn by tenure
* Churn by payment method
* Churn by internet service
* Customer segmentation
* Churn-related business metrics

The SQL queries are available in:

`sql/churn-analysis.sql`

## Machine Learning

Three classification models were evaluated:

1. Logistic Regression
2. Random Forest
3. Gradient Boosting

The models were evaluated using classification metrics including:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

## Model Comparison

The initial model comparison showed that different models provide different trade-offs between accuracy, precision, recall, and F1 score.

For a churn prediction problem, identifying actual churners is particularly important because failing to identify a customer who is likely to churn can result in a missed retention opportunity.

Therefore, **churn recall** was given significant importance during model selection and threshold optimization.

## Final Model

**Random Forest** was selected as the final model.

The default classification threshold of **0.50** was optimized to **0.40** to improve churn detection while maintaining a reasonable balance between precision and recall.

### Final Model Performance

| Metric    | Score |
| --------- | ----: |
| Accuracy  |   74% |
| Precision |   51% |
| Recall    |   75% |
| F1 Score  |   61% |
| ROC-AUC   |   82% |

## Threshold Optimization

Threshold analysis was performed to evaluate the trade-off between precision, recall, and F1 score.

The selected threshold was **0.40**.

At this threshold:

* Recall: **75.13%**
* F1 Score: **60.69%**
* ROC-AUC: **81.96%**

## Churn Prediction & Risk Segmentation

The final Random Forest model was used to generate churn probabilities for the test dataset.

The prediction output includes:

* Actual churn status
* Churn probability
* Predicted churn status
* Customer risk level

Customers were segmented into three risk categories:

* **Low Risk**
* **Medium Risk**
* **High Risk**

The prediction dataset contains **1,409 test customers**.

## Model Evaluation

The final model produced the following confusion matrix:

| Actual \ Predicted |  No | Yes |
| ------------------ | --: | --: |
| No                 | 764 | 271 |
| Yes                |  93 | 281 |

This means:

* **True Negatives:** 764
* **False Positives:** 271
* **False Negatives:** 93
* **True Positives:** 281

The model correctly identified **281 of 374 actual churn customers**, resulting in approximately **75.13% churn recall**.

## Power BI Dashboard

The Power BI dashboard is organized into three analytical pages covering business insights, churn risk, and machine learning model performance.

### 1. Executive Overview

**Dashboard Title:** Customer Churn Prediction & Risk Analysis

Provides a high-level view of:

* Actual churn
* Predicted churn
* Prediction customers
* High-risk customers
* Churn rate analysis
* Actual vs predicted churn
* Confusion matrix
* Customer risk distribution

![Executive Overview](powerbi/screenshots/executive-overview.png)

### 2. Customer Churn Analysis

**Dashboard Title:** Customer Churn Drivers & Business Insights

Provides deeper analysis of churn drivers and customer characteristics across:

* Contract
* Monthly charges
* Service count
* Customer age group
* Partner status
* Dependents

![Customer Churn Analysis](powerbi/screenshots/customer-churn-analysis.png)

### 3. Model Performance

**Dashboard Title:** Churn Prediction Model Performance

Provides:

* Model comparison
* Final Random Forest performance
* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Threshold optimization
* Final confusion matrix

![Model Performance](powerbi/screenshots/model-performance.png)

## Key Business Objective

The primary objective is to identify customers who are likely to churn so that businesses can prioritize retention efforts.

The model emphasizes churn recall because failing to identify an actual churn customer can result in a missed retention opportunity.

## Key Business Insights

The analysis enables businesses to examine churn patterns across:

* Contract types
* Monthly charge groups
* Customer tenure
* Service adoption
* Internet service
* Payment methods
* Customer profile characteristics

The predictive component additionally enables customers to be prioritized according to their estimated churn risk.

## Key Outcome

The project combines data analytics, SQL, machine learning, and business intelligence into a single end-to-end customer churn solution.

The final solution moves from raw customer data to:

```text
Data
  ↓
Analysis
  ↓
Business Insights
  ↓
Prediction
  ↓
Risk Segmentation
  ↓
Retention Prioritization
```

## Project Structure

```text
customer-churn-prediction/
│
├── data/
│   ├── Telco-Customer-Churn.csv
│   ├── processed_telco_churn.csv
│   ├── model_ready_telco_churn.csv
│   ├── churn_predictions.csv
│   ├── customer_churn_model.pkl
│   └── churn_threshold.pkl
│
├── notebook/
│   ├── Data Preprocessing.py
│   ├── Churn Analysis.py
│   ├── Feature Engineering.py
│   └── Churn Model.py
│
├── sql/
│   └── churn-analysis.sql
│
├── powerbi/
│   ├── customer-churn-dashboard.pbix
│   └── screenshots/
│       ├── executive-overview.png
│       ├── customer-churn-analysis.png
│       └── model-performance.png
│
└── README.md
```

## Project Deliverables

The project includes:

* Processed customer datasets
* Feature-engineered model-ready dataset
* Python data analysis and machine learning scripts
* SQL analysis queries
* Trained Random Forest model
* Churn prediction output
* Optimized prediction threshold
* Interactive Power BI dashboard
* Dashboard screenshots
* Project documentation

## Conclusion

This project demonstrates an end-to-end approach to customer churn analysis by combining data preparation, exploratory analysis, SQL, feature engineering, machine learning, predictive risk segmentation, and Power BI reporting.

The final solution provides both **business-level churn insights** and a **predictive framework for identifying customers who may require proactive retention efforts**.
