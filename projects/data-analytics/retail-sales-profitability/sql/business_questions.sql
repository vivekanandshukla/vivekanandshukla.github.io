-- Retail Sales & Profitability Analytics
-- SQL Server Business Analysis


-- Overall Business Performance

SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Total_Customers,
    COUNT(DISTINCT Product_ID) AS Total_Products,
    SUM(Quantity) AS Total_Quantity
FROM dbo.retail_sales;


-- Yearly Sales & Profit

SELECT
    Order_Year AS Year,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin,
    COUNT(DISTINCT Order_ID) AS Orders
FROM dbo.retail_sales
GROUP BY Order_Year
ORDER BY Year;


-- Year-over-Year Growth

WITH yearly_sales AS (
    SELECT
        Order_Year AS Year,
        SUM(Sales) AS Sales,
        SUM(Profit) AS Profit
    FROM dbo.retail_sales
    GROUP BY Order_Year
)
SELECT
    Year,
    ROUND(Sales, 2) AS Sales,
    ROUND(Profit, 2) AS Profit,
    ROUND(
        (Sales - LAG(Sales) OVER (ORDER BY Year))
        / NULLIF(LAG(Sales) OVER (ORDER BY Year), 0) * 100,
        2
    ) AS Sales_Growth,
    ROUND(
        (Profit - LAG(Profit) OVER (ORDER BY Year))
        / NULLIF(LAG(Profit) OVER (ORDER BY Year), 0) * 100,
        2
    ) AS Profit_Growth
FROM yearly_sales
ORDER BY Year;


-- Monthly Sales & Profit

SELECT
    Order_Year AS Year,
    Order_Month AS Month,
    Order_Month_Name AS Month_Name,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin
FROM dbo.retail_sales
GROUP BY
    Order_Year,
    Order_Month,
    Order_Month_Name
ORDER BY
    Year,
    Month;


-- Category Performance

SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin,
    SUM(Quantity) AS Quantity,
    COUNT(DISTINCT Order_ID) AS Orders
FROM dbo.retail_sales
GROUP BY Category
ORDER BY Profit DESC;


-- Sub-category Profitability

SELECT
    Category,
    Sub_Category,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin
FROM dbo.retail_sales
GROUP BY
    Category,
    Sub_Category
ORDER BY Profit;


-- Loss-making Sub-categories

SELECT
    Category,
    Sub_Category,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin
FROM dbo.retail_sales
GROUP BY
    Category,
    Sub_Category
HAVING SUM(Profit) < 0
ORDER BY Profit;


-- Top 10 Most Profitable Products

SELECT TOP 10
    Product_ID,
    Product_Name,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin
FROM dbo.retail_sales
GROUP BY
    Product_ID,
    Product_Name
ORDER BY Profit DESC;


-- Bottom 10 Products by Profit

SELECT TOP 10
    Product_ID,
    Product_Name,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin
FROM dbo.retail_sales
GROUP BY
    Product_ID,
    Product_Name
ORDER BY Profit;


-- Regional Performance

SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin,
    COUNT(DISTINCT Order_ID) AS Orders
FROM dbo.retail_sales
GROUP BY Region
ORDER BY Profit DESC;


-- Region × Category Performance

SELECT
    Region,
    Category,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin
FROM dbo.retail_sales
GROUP BY
    Region,
    Category
ORDER BY Profit;


-- Customer Segment Performance

SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin,
    COUNT(DISTINCT Order_ID) AS Orders,
    COUNT(DISTINCT Customer_ID) AS Customers
FROM dbo.retail_sales
GROUP BY Segment
ORDER BY Profit DESC;


-- Top 10 Customers by Profit

SELECT TOP 10
    Customer_ID,
    Customer_Name,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin,
    COUNT(DISTINCT Order_ID) AS Orders
FROM dbo.retail_sales
GROUP BY
    Customer_ID,
    Customer_Name
ORDER BY Profit DESC;


-- Discount Level Analysis

SELECT
    Discount,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin,
    COUNT(*) AS Records
FROM dbo.retail_sales
GROUP BY Discount
ORDER BY Discount;


-- Loss-making Transactions by Discount

SELECT
    Discount,
    COUNT(*) AS Total_Records,
    SUM(
        CASE
            WHEN Profit < 0 THEN 1
            ELSE 0
        END
    ) AS Loss_Records,
    ROUND(
        SUM(
            CASE
                WHEN Profit < 0 THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Loss_Rate
FROM dbo.retail_sales
GROUP BY Discount
ORDER BY Discount;


-- Central × Furniture Performance

SELECT
    Region,
    Category,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin
FROM dbo.retail_sales
WHERE Region = 'Central'
  AND Category = 'Furniture'
GROUP BY
    Region,
    Category;


-- Negative Profit Transactions

SELECT
    COUNT(*) AS Loss_Making_Records,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit
FROM dbo.retail_sales
WHERE Profit < 0;


-- Product Profit Ranking

WITH product_profit AS (
    SELECT
        Product_ID,
        SUM(Profit) AS Profit
    FROM dbo.retail_sales
    GROUP BY Product_ID
),
ranked_products AS (
    SELECT
        Product_ID,
        Profit,
        ROW_NUMBER() OVER (
            ORDER BY Profit DESC
        ) AS Profit_Rank
    FROM product_profit
)
SELECT
    Profit_Rank,
    Product_ID,
    ROUND(Profit, 2) AS Profit
FROM ranked_products
WHERE Profit_Rank <= 20
ORDER BY Profit_Rank;


-- High Discount Transactions

SELECT
    Discount,
    COUNT(*) AS Records,
    ROUND(SUM(Sales), 2) AS Sales,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin
FROM dbo.retail_sales
WHERE Discount > 0.20
GROUP BY Discount
ORDER BY Discount;
