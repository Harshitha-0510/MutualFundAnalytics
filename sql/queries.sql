-- ==========================================
-- Query 1: Top 5 Fund Houses by AUM
-- ==========================================
SELECT fund_house, aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- ==========================================
-- Query 2: Average NAV by Fund
-- ==========================================
SELECT amfi_code,
       AVG(nav) AS average_nav
FROM fact_nav
GROUP BY amfi_code;

-- ==========================================
-- Query 3: Total Transactions by State
-- ==========================================
SELECT state,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- ==========================================
-- Query 4: Funds with Expense Ratio below 1%
-- ==========================================
SELECT amfi_code,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- ==========================================
-- Query 5: Average Investment Amount by Transaction Type
-- ==========================================
SELECT transaction_type,
       AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

-- ==========================================
-- Query 6: Highest 3-Year Return
-- ==========================================
SELECT amfi_code,
       return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

-- ==========================================
-- Query 7: Top 10 NAV Values
-- ==========================================
SELECT amfi_code,
       date,
       nav
FROM fact_nav
ORDER BY nav DESC
LIMIT 10;

-- ==========================================
-- Query 8: Transactions by KYC Status
-- ==========================================
SELECT kyc_status,
       COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;

-- ==========================================
-- Query 9: Average Alpha and Beta
-- ==========================================
SELECT AVG(alpha) AS avg_alpha,
       AVG(beta) AS avg_beta
FROM fact_performance;

-- ==========================================
-- Query 10: Average AUM
-- ==========================================
SELECT AVG(aum_crore) AS average_aum
FROM fact_aum;