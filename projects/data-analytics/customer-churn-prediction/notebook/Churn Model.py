# Customer Churn Model

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report


# Load model-ready data

DATA_PATH = "../data/model_ready_telco_churn.csv"

df = pd.read_csv(DATA_PATH)

print("Customer Churn Model")
print(f"Records: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")


# Separate target and features

X = df.drop(columns=["Churn", "customerID"])
y = df["Churn"].map({"No": 0, "Yes": 1})


# Identify feature types

categorical_features = X.select_dtypes(include=["object", "category"]).columns.tolist()
numerical_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

print("\nCategorical Features")
print(categorical_features)

print("\nNumerical Features")
print(numerical_features)


# Split data into training and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

print("\nTraining Records:", len(X_train))
print("Test Records:", len(X_test))


# Prepare categorical and numerical features

preprocessor = ColumnTransformer(
    transformers=[("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("numerical", StandardScaler(), numerical_features)])


# Build logistic regression pipeline

model = Pipeline(steps=[("preprocessing", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000, random_state=42))])


# Train model

model.fit(X_train, y_train)


# Generate predictions

y_pred = model.predict(X_test)
y_probability = model.predict_proba(X_test)[:, 1]


# Model evaluation

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_probability)

print("\nModel Performance")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC-AUC  : {roc_auc:.4f}")


# Detailed classification report

print("\nClassification Report")
print(classification_report(y_test, y_pred, target_names=["Retained", "Churned"]))


# Random Forest model

from sklearn.ensemble import RandomForestClassifier


random_forest = Pipeline(steps=[("preprocessing", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=300, random_state=42, class_weight="balanced"))])


# Train Random Forest

random_forest.fit(X_train, y_train)


# Generate Random Forest predictions

rf_pred = random_forest.predict(X_test)
rf_probability = random_forest.predict_proba(X_test)[:, 1]


# Random Forest evaluation

rf_accuracy = accuracy_score(y_test, rf_pred)
rf_precision = precision_score(y_test, rf_pred)
rf_recall = recall_score(y_test, rf_pred)
rf_f1 = f1_score(y_test, rf_pred)
rf_roc_auc = roc_auc_score(y_test, rf_probability)

print("\nRandom Forest Performance")
print(f"Accuracy : {rf_accuracy:.4f}")
print(f"Precision: {rf_precision:.4f}")
print(f"Recall   : {rf_recall:.4f}")
print(f"F1 Score : {rf_f1:.4f}")
print(f"ROC-AUC  : {rf_roc_auc:.4f}")

print("\nRandom Forest Classification Report")
print(classification_report(y_test, rf_pred, target_names=["Retained", "Churned"]))


# Gradient Boosting model

from sklearn.ensemble import GradientBoostingClassifier


gradient_boosting = Pipeline(
    steps=[("preprocessing", preprocessor),
        ("classifier", GradientBoostingClassifier(random_state=42))])


# Train Gradient Boosting

gradient_boosting.fit(X_train, y_train)


# Generate Gradient Boosting predictions

gb_pred = gradient_boosting.predict(X_test)
gb_probability = gradient_boosting.predict_proba(X_test)[:, 1]


# Gradient Boosting evaluation

gb_accuracy = accuracy_score(y_test, gb_pred)
gb_precision = precision_score(y_test, gb_pred)
gb_recall = recall_score(y_test, gb_pred)
gb_f1 = f1_score(y_test, gb_pred)
gb_roc_auc = roc_auc_score(y_test, gb_probability)

print("\nGradient Boosting Performance")
print(f"Accuracy : {gb_accuracy:.4f}")
print(f"Precision: {gb_precision:.4f}")
print(f"Recall   : {gb_recall:.4f}")
print(f"F1 Score : {gb_f1:.4f}")
print(f"ROC-AUC  : {gb_roc_auc:.4f}")

print("\nGradient Boosting Classification Report")
print(classification_report(y_test, gb_pred, target_names=["Retained", "Churned"]))


# Random Forest threshold analysis

import numpy as np


threshold_results = []

for threshold in np.arange(0.30, 0.71, 0.05):
    threshold_pred = (rf_probability >= threshold).astype(int)

    threshold_precision = precision_score(y_test, threshold_pred, zero_division=0)
    threshold_recall = recall_score(y_test, threshold_pred, zero_division=0)
    threshold_f1 = f1_score(y_test, threshold_pred, zero_division=0)

    threshold_results.append({
        "Threshold": round(threshold, 2),
        "Precision": round(threshold_precision, 4),
        "Recall": round(threshold_recall, 4),
        "F1 Score": round(threshold_f1, 4)
    })


threshold_results = pd.DataFrame(threshold_results)

print("\nRandom Forest Threshold Analysis")
print(threshold_results.to_string(index=False))

# Final Random Forest model with optimized threshold

final_threshold = 0.40

final_rf_pred = (rf_probability >= final_threshold).astype(int)


# Final model evaluation

final_accuracy = accuracy_score(y_test, final_rf_pred)
final_precision = precision_score(y_test, final_rf_pred)
final_recall = recall_score(y_test, final_rf_pred)
final_f1 = f1_score(y_test, final_rf_pred)
final_roc_auc = roc_auc_score(y_test, rf_probability)

print("\nFinal Random Forest Performance")
print(f"Threshold : {final_threshold:.2f}")
print(f"Accuracy  : {final_accuracy:.4f}")
print(f"Precision : {final_precision:.4f}")
print(f"Recall    : {final_recall:.4f}")
print(f"F1 Score  : {final_f1:.4f}")
print(f"ROC-AUC   : {final_roc_auc:.4f}")



# Final classification report

print("\nFinal Classification Report")
print(classification_report(y_test, final_rf_pred, target_names=["Retained", "Churned"]))


# Confusion matrix

from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_test, final_rf_pred)

print("\nConfusion Matrix")
print(confusion)

# Save final model

import joblib

MODEL_PATH = "../data/customer_churn_model.pkl"

joblib.dump(random_forest, MODEL_PATH)

print(f"\nFinal model saved to: {MODEL_PATH}")


# Save final model and prediction threshold

import joblib

MODEL_PATH = "../data/customer_churn_model.pkl"
THRESHOLD_PATH = "../data/churn_threshold.pkl"

joblib.dump(random_forest, MODEL_PATH)
joblib.dump(final_threshold, THRESHOLD_PATH)

print(f"\nFinal model saved to: {MODEL_PATH}")
print(f"Prediction threshold saved to: {THRESHOLD_PATH}")


# Save churn predictions

prediction_results = X_test.copy()

prediction_results.insert(0, "customerID", df.loc[X_test.index, "customerID"])
prediction_results["ActualChurn"] = y_test.map({0: "No", 1: "Yes"})
prediction_results["ChurnProbability"] = rf_probability
prediction_results["PredictedChurn"] = pd.Series(final_rf_pred, index=X_test.index).map({0: "No", 1: "Yes"})

prediction_results["RiskLevel"] = pd.cut(
    prediction_results["ChurnProbability"],
    bins=[-0.01, 0.40, 0.70, 1.00],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

PREDICTION_PATH = "../data/churn_predictions.csv"

prediction_results.to_csv(PREDICTION_PATH, index=False)

print(f"\nChurn predictions saved to: {PREDICTION_PATH}")
print(f"Prediction records: {len(prediction_results):,}")