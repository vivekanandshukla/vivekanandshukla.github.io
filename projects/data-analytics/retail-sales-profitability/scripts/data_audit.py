# DATA AUDIT & BUSINESS KPIs
# Retail Sales & Profitability Analytics

# Import libraries

import pandas as pd
from pathlib import Path

#  Load Dataset
DATA_PATH = Path("../data/cleaned_superstore.csv")

df = pd.read_csv(DATA_PATH)
print("RETAIL SALES & PROFITABILITY ANALYTICS")
print("01 — DATA AUDIT & BUSINESS KPIs")

# Dataset Overview
print("\n[1] DATASET OVERVIEW")
print(f"Rows : {df.shape[0]:,}")
print(f"Columns : {df.shape[1]:,}")

print("\nColumns:")
print(df.columns.tolist())

#  Data Types
print("\n[2] DATA TYPES")
print(df.dtypes)

#  Missing Values
print("\n[3] MISSING VALUES")
missing = df.isnull().sum()
print(missing[missing > 0])

if missing.sum() == 0:
    print("No missing values found.")

#  Duplicate Records
print("\n[4] DUPLICATE RECORDS")
duplicates = df.duplicated().sum()
print(f"Duplicate rows: {duplicates:,}")

#  Numerical Summary
print("\n[5] NUMERICAL SUMMARY")
numeric_columns = ["Sales","Quantity", "Discount", "Profit"]
print(df[numeric_columns].describe().round(2))

#  Business KPIs
print("\n[6] BUSINESS KPIs")
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_products = df["Product ID"].nunique()
profit_margin = total_profit / total_sales
average_order_value = total_sales / total_orders
average_profit_per_order = total_profit / total_orders

print("-" * 60)

print(f"Total Sales  : ${total_sales:,.2f}")
print(f"Total Profit : ${total_profit:,.2f}")
print(f"Profit Margin  : {profit_margin:.2%}")
print(f"Total Quantity  : {total_quantity:,}")
print(f"Total Orders : {total_orders:,}")
print(f"Total Customers : {total_customers:,}")
print(f"Total Products : {total_products:,}")
print(f"Average Order Value : ${average_order_value:,.2f}")
print(f"Average Profit/Order : ${average_profit_per_order:,.2f}")


#  Loss-Making Records
print("\n[7] PROFITABILITY CHECK")
loss_records = (df["Profit"] < 0).sum()
loss_percentage = loss_records / len(df)

print(f"Loss-making records : {loss_records:,}")
print(f"Loss-making rate    : {loss_percentage:.2%}")

#  Sales & Profit by Category
print("\n[8] CATEGORY PERFORMANCE")
category_analysis = (df.groupby("Category")
    .agg(Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    ).sort_values("Profit", ascending=False))

category_analysis["Profit Margin"] = (
category_analysis["Profit"] /
    category_analysis["Sales"])

print(category_analysis.round(2))

#  Regional Performance
print("\n[9] REGIONAL PERFORMANCE")
region_analysis = (df.groupby("Region")
    .agg(Sales=("Sales", "sum"),
        Profit=("Profit", "sum"))
    .sort_values("Profit", ascending=False))

region_analysis["Profit Margin"] = (
    region_analysis["Profit"] /
    region_analysis["Sales"])

print(region_analysis.round(2))

#  Customer Segment Performance
print("\n[10] CUSTOMER SEGMENT PERFORMANCE")
segment_analysis = (df.groupby("Segment")
    .agg(Sales=("Sales", "sum"),
        Profit=("Profit", "sum")).sort_values("Profit", ascending=False))

segment_analysis["Profit Margin"] = (
    segment_analysis["Profit"] /
    segment_analysis["Sales"])

print(segment_analysis.round(2))

#  Final Audit Summary
print("\n[11] AUDIT SUMMARY")
print(f"Records : {len(df):,}")
print(f"Duplicate rows  : {duplicates:,}")
print(f"Missing values  : {missing.sum():,}")
print(f"Loss-making records : {loss_records:,}")
print(f"Total sales : ${total_sales:,.2f}")
print(f"Total profit : ${total_profit:,.2f}")
print(f"Overall profit margin : {profit_margin:.2%}")

print("\nAudit completed successfully.")

