import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///database/bluestock_mf.db")

# Load CSVs
fund = pd.read_csv(r"data\raw\Bluestock_MF_Datasets\01_fund_master.csv")
nav = pd.read_csv(r"data\processed\clean_nav_history.csv")
transactions = pd.read_csv(r"data\processed\clean_investor_transactions.csv")
performance = pd.read_csv(r"data\processed\clean_scheme_performance.csv")
aum = pd.read_csv(r"data\raw\Bluestock_MF_Datasets\03_aum_by_fund_house.csv")

# Save to SQLite
fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

print("SQLite Database Loaded Successfully!\n")

print("Row Counts")
print("dim_fund:", len(fund))
print("fact_nav:", len(nav))
print("fact_transactions:", len(transactions))
print("fact_performance:", len(performance))
print("fact_aum:", len(aum))