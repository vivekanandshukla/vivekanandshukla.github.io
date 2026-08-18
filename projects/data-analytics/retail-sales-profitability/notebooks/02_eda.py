# EXPLORATORY DATA ANALYSIS
# Retail Sales & Profitability Analytics

# Required libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Data Import
DATA_PATH = Path("../data/cleaned_superstore.csv")

df = pd.read_csv(DATA_PATH)

print("RETAIL SALES & PROFITABILITY ANALYTICS")
print("02 — EXPLORATORY DATA ANALYSIS")


# Prepare Dates & Derived Fields

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()
df["Year Month"] = df["Order Date"].dt.to_period("M").astype(str)

df["Profit Margin"] = df["Profit"] / df["Sales"]


# Yearly Performance

print("\nYEARLY PERFORMANCE")

yearly = (
    df.groupby("Year")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
)

yearly["Profit Margin"] = yearly["Profit"] / yearly["Sales"]

yearly["Sales Growth"] = yearly["Sales"].pct_change()
yearly["Profit Growth"] = yearly["Profit"].pct_change()

print(yearly.round(2))

plt.figure(figsize=(9, 5))

plt.plot(
    yearly.index,
    yearly["Sales"],
    marker="o",
    label="Sales"
)

plt.plot(
    yearly.index,
    yearly["Profit"],
    marker="o",
    label="Profit"
)

plt.title("Yearly Sales & Profit")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
plt.tight_layout()
plt.show()


# Monthly Performance

print("\nMONTHLY PERFORMANCE")

monthly = (
    df.groupby("Year Month")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

monthly["Profit Margin"] = monthly["Profit"] / monthly["Sales"]

print(monthly.round(2))

plt.figure(figsize=(11, 5))

plt.plot(
    monthly.index,
    monthly["Sales"],
    label="Sales"
)

plt.plot(
    monthly.index,
    monthly["Profit"],
    label="Profit"
)

plt.title("Monthly Sales & Profit")
plt.xlabel("Year-Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# Category Analysis

print("\nCATEGORY ANALYSIS")

category = (
    df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum"),
        Orders=("Order ID", "nunique")
    )
)

category["Profit Margin"] = category["Profit"] / category["Sales"]

category = category.sort_values(
    "Profit",
    ascending=False
)

print(category.round(2))

plt.figure(figsize=(8, 5))

plt.bar(
    category.index,
    category["Profit"]
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()


# Sub-category Analysis

print("\nSUB-CATEGORY PROFITABILITY")

subcategory = (
    df.groupby(["Category", "Sub-Category"])
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
)

subcategory["Profit Margin"] = (
    subcategory["Profit"] /
    subcategory["Sales"]
)

subcategory = subcategory.sort_values("Profit")

print(subcategory.round(2))

subcategory_chart = (
    subcategory
    .reset_index()
    .sort_values("Profit")
)

plt.figure(figsize=(9, 7))

plt.barh(
    subcategory_chart["Sub-Category"],
    subcategory_chart["Profit"]
)

plt.title("Profit by Sub-category")
plt.xlabel("Profit")
plt.ylabel("Sub-category")
plt.tight_layout()
plt.show()


# Top 10 Most Profitable Products

print("\nTOP 10 PROFITABLE PRODUCTS")

top_products = (
    df.groupby(["Product ID", "Product Name"])
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values(
        "Profit",
        ascending=False
    )
    .head(10)
)

top_products["Profit Margin"] = (
    top_products["Profit"] /
    top_products["Sales"]
)

print(top_products.round(2))

top_products_chart = (
    top_products
    .reset_index()
    .sort_values("Profit")
)

plt.figure(figsize=(9, 6))

plt.barh(
    top_products_chart["Product Name"],
    top_products_chart["Profit"]
)

plt.title("Top 10 Most Profitable Products")
plt.xlabel("Profit")
plt.ylabel("Product")
plt.tight_layout()
plt.show()


# Bottom 10 Products

print("\nBOTTOM 10 PRODUCTS")

bottom_products = (
    df.groupby(["Product ID", "Product Name"])
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Profit")
    .head(10)
)

bottom_products["Profit Margin"] = (
    bottom_products["Profit"] /
    bottom_products["Sales"]
)

print(bottom_products.round(2))

bottom_products_chart = (
    bottom_products
    .reset_index()
    .sort_values("Profit")
)

plt.figure(figsize=(9, 6))

plt.barh(
    bottom_products_chart["Product Name"],
    bottom_products_chart["Profit"]
)

plt.title("Bottom 10 Products by Profit")
plt.xlabel("Profit")
plt.ylabel("Product")
plt.tight_layout()
plt.show()


# Discount Analysis

print("\nDISCOUNT ANALYSIS")

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Records=("Order ID", "count")
    )
    .sort_index()
)

discount_analysis["Profit Margin"] = (
    discount_analysis["Profit"] /
    discount_analysis["Sales"]
)

discount_analysis["Loss Rate"] = (
    df.groupby("Discount")["Profit"]
    .apply(lambda x: (x < 0).mean())
)

print(discount_analysis.round(4))

plt.figure(figsize=(9, 5))

plt.plot(
    discount_analysis.index,
    discount_analysis["Profit Margin"],
    marker="o"
)

plt.axhline(
    0,
    linestyle="--"
)

plt.title("Discount vs Profit Margin")
plt.xlabel("Discount")
plt.ylabel("Profit Margin")
plt.tight_layout()
plt.show()


# Discount vs Profit Relationship

print("\nDISCOUNT VS PROFIT CORRELATION")

correlation = df["Discount"].corr(df["Profit"])

print(f"Pearson correlation: {correlation:.3f}")

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.3
)

plt.axhline(
    0,
    linestyle="--"
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()


# Region Analysis

print("\nREGION ANALYSIS")

region = (
    df.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
)

region["Profit Margin"] = (
    region["Profit"] /
    region["Sales"]
)

region = region.sort_values(
    "Profit",
    ascending=False
)

print(region.round(2))

plt.figure(figsize=(8, 5))

plt.bar(
    region.index,
    region["Profit"]
)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()


# Region × Category Analysis

print("\nREGION × CATEGORY ANALYSIS")

region_category = (
    df.groupby(["Region", "Category"])
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

region_category["Profit Margin"] = (
    region_category["Profit"] /
    region_category["Sales"]
)

region_category = region_category.sort_values("Profit")

print(region_category.round(2))

region_category_chart = (
    region_category
    .reset_index()
    .pivot(
        index="Region",
        columns="Category",
        values="Profit"
    )
)

plt.figure(figsize=(9, 5))

plt.imshow(
    region_category_chart,
    aspect="auto"
)

plt.xticks(
    range(len(region_category_chart.columns)),
    region_category_chart.columns
)

plt.yticks(
    range(len(region_category_chart.index)),
    region_category_chart.index
)

plt.title("Profit by Region & Category")
plt.xlabel("Category")
plt.ylabel("Region")
plt.colorbar(label="Profit")
plt.tight_layout()
plt.show()


# Customer Segment Analysis

print("\nCUSTOMER SEGMENT ANALYSIS")

segment = (
    df.groupby("Segment")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique"),
        Customers=("Customer ID", "nunique")
    )
)

segment["Profit Margin"] = (
    segment["Profit"] /
    segment["Sales"]
)

segment = segment.sort_values(
    "Profit",
    ascending=False
)

print(segment.round(2))

plt.figure(figsize=(8, 5))

plt.bar(
    segment.index,
    segment["Profit"]
)

plt.title("Profit by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()


# Customer Profitability

print("\nCUSTOMER PROFITABILITY")

customer = (
    df.groupby(["Customer ID", "Customer Name"])
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
)

customer["Profit Margin"] = (
    customer["Profit"] /
    customer["Sales"]
)

top_customers = (
    customer
    .sort_values(
        "Profit",
        ascending=False
    )
    .head(10)
)

print(top_customers.round(2))


# Profit Concentration

print("\nPROFIT CONCENTRATION")

product_profit = (
    df.groupby("Product ID")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

total_profit = product_profit.sum()

top_10_share = (
    product_profit.head(10).sum() /
    total_profit
)

top_20_share = (
    product_profit.head(20).sum() /
    total_profit
)

print(
    f"Top 10 products profit share : "
    f"{top_10_share:.2%}"
)

print(
    f"Top 20 products profit share : "
    f"{top_20_share:.2%}"
)


# Analysis Summary

print("\nEDA COMPLETED")

print("\nKey areas identified for further investigation:")

print("Furniture profitability")
print("Tables and Bookcases")
print("High-discount transactions")
print("Central × Furniture performance")
print("Product profit concentration")
