# Customer Churn Feature Engineering

import pandas as pd
from pathlib import Path


# Load processed data

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATA_PATH = DATA_DIR / "processed_telco_churn.csv"
OUTPUT_PATH = DATA_DIR / "model_ready_telco_churn.csv"

df = pd.read_csv(DATA_PATH)


print("Customer Churn Feature Engineering")
print(f"Records: {df.shape[0]:,}")
print(f"Columns before feature engineering: {df.shape[1]}")


# Tenure groups

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 6, 12, 24, 48, float("inf")],
    labels=["0-6 Months",
            "7-12 Months",
            "13-24 Months",
            "25-48 Months",
            "49+ Months"])


# Monthly charge groups

df["MonthlyChargeGroup"] = pd.cut(df["MonthlyCharges"],
    bins=[-1, 30, 60, 90, float("inf")],
    labels=["Below $30",
            "$30-$59",
            "$60-$89",
            "$90+"])


# Check numeric values before calculating average monthly value

print("\nTotalCharges data type")
print(df["TotalCharges"].dtype)

print("\nMissing TotalCharges")
print(df["TotalCharges"].isna().sum())

print("\nMissing tenure")
print(df["tenure"].isna().sum())

print("\nInfinite TotalCharges")
print(df["TotalCharges"].isin([float("inf"), float("-inf")]).sum())


# Average monthly value based on total charges

df["AverageMonthlyValue"] = (df["TotalCharges"] / df["tenure"].replace(0, 1))


# Validate average monthly value

print("\nAverageMonthlyValue validation")

print("Missing values:", df["AverageMonthlyValue"].isna().sum())
print("Infinite values:", df["AverageMonthlyValue"].isin([float("inf"), float("-inf")]).sum())

print(df["AverageMonthlyValue"]
    .describe()
    .round(2))


# Count subscribed services

service_columns = ["PhoneService",
                   "MultipleLines",
                   "OnlineSecurity",
                   "OnlineBackup",
                   "DeviceProtection",
                   "TechSupport",
                   "StreamingTV",
                   "StreamingMovies"]

df["ServiceCount"] = (df[service_columns]
    .apply(lambda row: sum(str(value).strip() == "Yes"
            for value in row),axis=1))


# Security and support availability

df["HasSecurityOrSupport"] = ((df["OnlineSecurity"] == "Yes")
    | (df["TechSupport"] == "Yes")).astype(int)


# Long-term contract indicator

df["IsLongTermContract"] = (df["Contract"].isin(
        ["One year", "Two year"])).astype(int)


# Paperless billing indicator

df["UsesPaperlessBilling"] = (df["PaperlessBilling"] == "Yes").astype(int)


# Feature engineering summary

new_features = ["TenureGroup",
                "MonthlyChargeGroup",
                "AverageMonthlyValue",
                "ServiceCount",
                "HasSecurityOrSupport",
                "IsLongTermContract",
                "UsesPaperlessBilling"]

print("\nNew Features")

for feature in new_features:
    print(feature)


# Feature overview

print("\nFeature Summary")
print(df[new_features].describe(include="all").transpose())


# Save model-ready dataset

df.to_csv(OUTPUT_PATH, index=False)

print(f"\nModel-ready dataset saved to: {OUTPUT_PATH}")
print(f"Columns after feature engineering: {df.shape[1]}")