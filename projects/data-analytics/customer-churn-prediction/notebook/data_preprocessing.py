# Customer Churn Analysis

import pandas as pd
from pathlib import Path


# Data Auditing

# Load dataset

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATA_PATH = DATA_DIR / "Telco-Customer-Churn.csv"

df = pd.read_csv(DATA_PATH)

# checking shape of the data

print("Customer Churn Analysis")
print(f"Records: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")


# Dataset structure

print("\nColumns")
print(df.columns.tolist())


# Data types

print("\nData Types")
print(df.dtypes)


# Missing value check

print("\nMissing Values")
missing_values = df.isna().sum()
print(missing_values[missing_values > 0])


# Duplicate record check

print("\nDuplicate Rows")
print(df.duplicated().sum())


# Customer ID uniqueness check

print("\nDuplicate Customer IDs")
print(df["customerID"].duplicated().sum())


# Check blank TotalCharges values

print("\nBlank Total Charges")
blank_total_charges = (df["TotalCharges"].astype(str).str.strip().eq("").sum())

print(blank_total_charges)


# Churn distribution

print("\nChurn Distribution")
print(df["Churn"].value_counts())


# Churn percentage

print("\nChurn Percentage")
churn_percentage = df["Churn"].value_counts(normalize=True) * 100
print(churn_percentage.round(2))


# Numerical variables overview

print("\nNumerical Summary")
print(df[["SeniorCitizen", "tenure", "MonthlyCharges"]].describe().round(2))


# Categorical variables overview

print("\nCategorical Summary")
categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    print(f"\n{column}")
    print(df[column].value_counts(dropna=False))


# Data Cleaning

# Clean TotalCharges

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(0)


# Check cleaned data types

print("\nUpdated Data Types")
print(df.dtypes)


# Check remaining missing values

print("\nRemaining Missing Values")
remaining_missing = df.isna().sum()
print(remaining_missing[remaining_missing > 0])


# Check cleaned TotalCharges

print("\nTotal Charges Summary")
print(df["TotalCharges"].describe().round(2))


# Save cleaned dataset

OUTPUT_PATH = DATA_DIR / "processed_telco_churn.csv"

df.to_csv(OUTPUT_PATH, index=False)

print(f"\nCleaned dataset saved to: {OUTPUT_PATH}")