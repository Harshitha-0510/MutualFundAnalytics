import pandas as pd

df = pd.read_csv(
    r"data\raw\Bluestock_MF_Datasets\01_fund_master.csv"
)

print("\nUNIQUE FUND HOUSES")
print(df["fund_house"].unique())

print("\nUNIQUE CATEGORIES")
print(df["category"].unique())

print("\nUNIQUE SUB CATEGORIES")
print(df["sub_category"].unique())

print("\nUNIQUE RISK CATEGORIES")
print(df["risk_category"].unique())

print("\nTOTAL FUND HOUSES")
print(df["fund_house"].nunique())

print("\nTOTAL CATEGORIES")
print(df["category"].nunique())