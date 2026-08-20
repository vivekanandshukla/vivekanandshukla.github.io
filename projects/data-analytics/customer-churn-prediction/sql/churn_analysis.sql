---- Create Database
CREATE DATABASE CustomerChurnAnalytics;
GO
USE CustomerChurnAnalytics;
GO

--- Creating Table
CREATE TABLE dbo.CustomerChurn
(
    customerID NVARCHAR(50) NOT NULL,
    gender NVARCHAR(20) NOT NULL,
    SeniorCitizen TINYINT NOT NULL,
    Partner NVARCHAR(20) NOT NULL,
    Dependents NVARCHAR(20) NOT NULL,
    tenure INT NOT NULL,
    PhoneService NVARCHAR(30) NOT NULL,
    MultipleLines NVARCHAR(50) NOT NULL,
    InternetService NVARCHAR(50) NOT NULL,
    OnlineSecurity NVARCHAR(50) NOT NULL,
    OnlineBackup NVARCHAR(50) NOT NULL,
    DeviceProtection NVARCHAR(50) NOT NULL,
    TechSupport NVARCHAR(50) NOT NULL,
    StreamingTV NVARCHAR(50) NOT NULL,
    StreamingMovies NVARCHAR(50) NOT NULL,
    Contract NVARCHAR(50) NOT NULL,
    PaperlessBilling NVARCHAR(20) NOT NULL,
    PaymentMethod NVARCHAR(100) NOT NULL,
    MonthlyCharges FLOAT NOT NULL,
    TotalCharges FLOAT NOT NULL,
    Churn NVARCHAR(10) NOT NULL
);
GO

---checking total rows (need to be 0)
SELECT COUNT(*) AS TotalRows
FROM dbo.CustomerChurn;

USE CustomerChurnAnalytics;
GO

--- insert data from file
-- Update the file path below according to your local environment.
-- Do not use a user-specific path in the public repository.

BULK INSERT dbo.CustomerChurn
FROM 'C:\Path\To\customer-churn-prediction\data\processed_telco_churn.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    TABLOCK
);
GO

--- checking all reccords
SELECT COUNT(*) AS TotalCustomers
FROM dbo.CustomerChurn;

--- Checking top 10 records
SELECT TOP 10 *
FROM dbo.CustomerChurn;

--- Checking Total Customer
SELECT
    COUNT(*) AS TotalCustomers,
    COUNT(DISTINCT customerID) AS UniqueCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS RetainedCustomers
FROM dbo.CustomerChurn;

--- Checking Churn Rate
SELECT
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS RetainedCustomers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2) AS ChurnRate
FROM dbo.CustomerChurn;

---Contract-wise Churn Analysis
SELECT
    Contract,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS RetainedCustomers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS ChurnRate
FROM dbo.CustomerChurn
GROUP BY Contract
ORDER BY ChurnRate DESC;

---Tenure-wise Churn
SELECT
    CASE
        WHEN tenure <= 6 THEN '0-6 Months'
        WHEN tenure <= 12 THEN '7-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END AS TenureGroup,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS RetainedCustomers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2) AS ChurnRate
FROM dbo.CustomerChurn
GROUP BY
    CASE
        WHEN tenure <= 6 THEN '0-6 Months'
        WHEN tenure <= 12 THEN '7-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END
ORDER BY
    MIN(tenure);


	--- Internet Service × Contract
	SELECT
    InternetService,
    Contract,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS RetainedCustomers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2) AS ChurnRate
FROM dbo.CustomerChurn
GROUP BY
    InternetService,
    Contract
ORDER BY
    ChurnRate DESC;

	--- Payment Method × Contract
	SELECT
    PaymentMethod,
    Contract,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS RetainedCustomers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2) AS ChurnRate
FROM dbo.CustomerChurn
GROUP BY PaymentMethod, Contract
ORDER BY
    ChurnRate DESC;

	-- Monthly charges and churn analysis

SELECT
    CASE
        WHEN MonthlyCharges < 30 THEN 'Below $30'
        WHEN MonthlyCharges < 60 THEN '$30-$59'
        WHEN MonthlyCharges < 90 THEN '$60-$89'
        ELSE '$90+'
    END AS MonthlyChargeGroup,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS RetainedCustomers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2) AS ChurnRate
FROM dbo.CustomerChurn
GROUP BY
    CASE
        WHEN MonthlyCharges < 30 THEN 'Below $30'
        WHEN MonthlyCharges < 60 THEN '$30-$59'
        WHEN MonthlyCharges < 90 THEN '$60-$89'
        ELSE '$90+'
    END
ORDER BY
    MIN(MonthlyCharges);


	-- Customer profile and churn analysis

SELECT
    SeniorCitizen,
    Partner,
    Dependents,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS RetainedCustomers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2) AS ChurnRate
FROM dbo.CustomerChurn
GROUP BY
    SeniorCitizen,
    Partner,
    Dependents
ORDER BY
    ChurnRate DESC;


	-- Service usage and churn analysis

SELECT
    'PhoneService' AS Service,
    PhoneService AS ServiceValue,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END) AS RetainedCustomers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2) AS ChurnRate
FROM dbo.CustomerChurn
GROUP BY PhoneService

UNION ALL

SELECT
    'InternetService',
    InternetService,
    COUNT(*),
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END),
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END),
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2)
FROM dbo.CustomerChurn
GROUP BY InternetService

UNION ALL

SELECT
    'OnlineSecurity',
    OnlineSecurity,
    COUNT(*),
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END),
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END),
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2)
FROM dbo.CustomerChurn
GROUP BY OnlineSecurity

UNION ALL

SELECT
    'TechSupport',
    TechSupport,
    COUNT(*),
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END),
    SUM(CASE WHEN Churn = 'No' THEN 1 ELSE 0 END),
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2)
FROM dbo.CustomerChurn
GROUP BY TechSupport

ORDER BY ChurnRate DESC;


	-- High-risk customer identification

SELECT
    customerID,
    Contract,
    tenure,
    MonthlyCharges,
    InternetService,
    PaymentMethod,
    Churn,

    CASE
        WHEN Contract = 'Month-to-month'
             AND tenure <= 12
             AND MonthlyCharges >= 70
            THEN 'High Risk'

        WHEN Contract = 'Month-to-month'
             AND (tenure <= 12
                 OR MonthlyCharges >= 70)
            THEN 'Medium Risk'

        ELSE 'Low Risk'
    END AS RiskLevel

FROM dbo.CustomerChurn
ORDER BY
    CASE
        WHEN Contract = 'Month-to-month'
             AND tenure <= 12
             AND MonthlyCharges >= 70
            THEN 1

        WHEN Contract = 'Month-to-month'
             AND (tenure <= 12
                 OR MonthlyCharges >= 70)
            THEN 2

        ELSE 3
    END,
    MonthlyCharges DESC;


