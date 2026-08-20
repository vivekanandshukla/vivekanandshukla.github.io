# Customer Churn Analysis

import pandas as pd
import matplotlib.pyplot as plt


# Load processed data

DATA_PATH = "../data/processed_telco_churn.csv"

df = pd.read_csv(DATA_PATH)


print("Customer Churn Analysis")
print(f"Records: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")


# Overall churn

print("\nChurn Overview")

churn_summary = (df["Churn"].value_counts()
    .rename_axis("Churn").reset_index(name="Customers"))

churn_summary["Percentage"] = (churn_summary["Customers"] / churn_summary["Customers"].sum()* 100)

print(churn_summary.round(2))

plt.figure(figsize=(6, 4))

churn_summary.plot(x="Churn",y="Customers",kind="bar",legend=False)
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Churn by contract

print("\nChurn by Contract")

contract_churn = (pd.crosstab(df["Contract"],
        df["Churn"],normalize="index") * 100)

print(contract_churn.round(2))

contract_churn.plot(kind="bar",figsize=(8, 5))
plt.title("Churn Rate by Contract")
plt.xlabel("Contract")
plt.ylabel("Customers (%)")
plt.xticks(rotation=0)
plt.legend(title="Churn")
plt.tight_layout()
plt.show()


# Churn by tenure

print("\nTenure by Churn")

tenure_summary = (df.groupby("Churn")["tenure"]
    .agg(Customers="count",Average_Tenure="mean",Median_Tenure="median"))

print(tenure_summary.round(2))


df.boxplot(column="tenure",by="Churn",figsize=(7, 5))
plt.title("Tenure Distribution by Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Tenure (Months)")
plt.tight_layout()
plt.show()


# Churn by monthly charges
print("\nMonthly Charges by Churn")

monthly_charges = (df.groupby("Churn")["MonthlyCharges"]
    .agg(Customers="count", Average_Charges="mean", Median_Charges="median"))

print(monthly_charges.round(2))

df.boxplot(column="MonthlyCharges", by="Churn", figsize=(7, 5))
plt.title("Monthly Charges by Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.show()


# Churn by internet service
print("\nChurn by Internet Service")

internet_churn = (pd.crosstab(df["InternetService"],
        df["Churn"],normalize="index") * 100)

print(internet_churn.round(2))

internet_churn.plot(kind="bar",figsize=(8, 5))
plt.title("Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Customers (%)")
plt.xticks(rotation=0)
plt.legend(title="Churn")
plt.tight_layout()
plt.show()


# Churn by payment method

print("\nChurn by Payment Method")
payment_churn = (pd.crosstab(df["PaymentMethod"],
                             df["Churn"],normalize="index") * 100)

print(payment_churn.round(2))


payment_churn.plot(kind="bar",figsize=(9, 5))
plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Customers (%)")
plt.xticks(rotation=20, ha="right")
plt.legend(title="Churn")
plt.tight_layout()
plt.show()


# Churn by senior citizen status
print("\nChurn by Senior Citizen Status")

senior_churn = (pd.crosstab(df["SeniorCitizen"],df["Churn"],
                            normalize="index") * 100)

print(senior_churn.round(2))

senior_churn.plot(kind="bar",figsize=(7, 5))
plt.title("Churn Rate by Senior Citizen Status")
plt.xlabel("Senior Citizen")
plt.ylabel("Customers (%)")
plt.xticks(ticks=[0, 1],labels=["No", "Yes"],rotation=0)
plt.legend(title="Churn")
plt.tight_layout()
plt.show()


# Churn by partner and dependents

print("\nChurn by Partner")
partner_churn = (pd.crosstab(df["Partner"],
                             df["Churn"], normalize="index") * 100)

print(partner_churn.round(2))


print("\nChurn by Dependents")
dependents_churn = (pd.crosstab(df["Dependents"],
                                df["Churn"],normalize="index") * 100)

print(dependents_churn.round(2))


# Service-level churn analysis
service_columns = ["PhoneService", "MultipleLines", "OnlineSecurity",
                   "OnlineBackup","DeviceProtection", "TechSupport","StreamingTV","StreamingMovies"]

print("\nService-level Churn Analysis")

for column in service_columns:

    churn_rate = (pd.crosstab(df[column],
            df["Churn"],normalize="index") * 100)

    print(f"\n{column}")
    print(churn_rate.round(2))


print("\nExploratory analysis completed.")

