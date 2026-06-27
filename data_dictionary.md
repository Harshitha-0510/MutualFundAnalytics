\# Mutual Fund Analytics Platform - Data Dictionary



\## 1. dim\_fund

\*\*Source:\*\* 01\_fund\_master.csv



| Column | Data Type | Description |

|--------|-----------|-------------|

| amfi\_code | INTEGER | Unique AMFI scheme code |

| fund\_house | TEXT | Mutual fund company |

| scheme\_name | TEXT | Name of the mutual fund scheme |

| category | TEXT | Fund category (Equity, Debt, etc.) |

| sub\_category | TEXT | Scheme sub-category |

| plan | TEXT | Direct or Regular plan |

| benchmark | TEXT | Benchmark index |

| expense\_ratio\_pct | REAL | Expense ratio (%) |

| exit\_load\_pct | REAL | Exit load (%) |

| min\_sip\_amount | INTEGER | Minimum SIP amount |

| min\_lumpsum\_amount | INTEGER | Minimum lump sum investment |

| fund\_manager | TEXT | Fund manager |

| risk\_category | TEXT | Risk level |

| sebi\_category\_code | TEXT | SEBI category code |



\---



\## 2. fact\_nav

\*\*Source:\*\* clean\_nav\_history.csv



| Column | Data Type | Description |

|--------|-----------|-------------|

| amfi\_code | INTEGER | AMFI scheme code |

| date | DATE | NAV date |

| nav | REAL | Net Asset Value |



\---



\## 3. fact\_transactions

\*\*Source:\*\* clean\_investor\_transactions.csv



| Column | Data Type | Description |

|--------|-----------|-------------|

| investor\_id | TEXT | Investor identifier |

| transaction\_date | DATE | Transaction date |

| amfi\_code | INTEGER | Fund code |

| transaction\_type | TEXT | SIP, Lumpsum or Redemption |

| amount\_inr | REAL | Transaction amount |

| state | TEXT | Investor state |

| city | TEXT | Investor city |

| city\_tier | TEXT | Tier classification |

| age\_group | TEXT | Investor age group |

| gender | TEXT | Gender |

| annual\_income\_lakh | REAL | Annual income (Lakhs) |

| payment\_mode | TEXT | Payment method |

| kyc\_status | TEXT | KYC verification status |



\---



\## 4. fact\_performance

\*\*Source:\*\* clean\_scheme\_performance.csv



| Column | Data Type | Description |

|--------|-----------|-------------|

| amfi\_code | INTEGER | Fund code |

| return\_1yr\_pct | REAL | 1-year return |

| return\_3yr\_pct | REAL | 3-year return |

| return\_5yr\_pct | REAL | 5-year return |

| benchmark\_3yr\_pct | REAL | Benchmark return |

| alpha | REAL | Alpha |

| beta | REAL | Beta |

| sharpe\_ratio | REAL | Sharpe Ratio |

| sortino\_ratio | REAL | Sortino Ratio |

| std\_dev\_ann\_pct | REAL | Annualized standard deviation |

| max\_drawdown\_pct | REAL | Maximum drawdown |

| expense\_ratio\_pct | REAL | Expense ratio |

| aum\_crore | REAL | Assets under management |

| morningstar\_rating | INTEGER | Morningstar rating |



\---



\## 5. fact\_aum

\*\*Source:\*\* 03\_aum\_by\_fund\_house.csv



| Column | Data Type | Description |

|--------|-----------|-------------|

| date | DATE | AUM reporting date |

| fund\_house | TEXT | Mutual fund company |

| aum\_lakh\_crore | REAL | AUM in lakh crore |

| aum\_crore | REAL | AUM in crore |

| num\_schemes | INTEGER | Number of schemes |

