import pandas as pd

# Load dataset
file_path = r"data\raw\Bluestock_MF_Datasets\07_scheme_performance.csv"
df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check for missing numeric values
print("\nMissing Numeric Values:")
print(df[return_columns].isnull().sum())

# Check expense ratio range
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nFunds with Invalid Expense Ratio:")
print(len(invalid_expense))

# Flag anomalies in returns
anomalies = df[
    (df["return_1yr_pct"] < -100) |
    (df["return_5yr_pct"] > 100)
]

print("\nReturn Anomalies:")
print(len(anomalies))

# Save cleaned dataset
output_path = r"data\processed\clean_scheme_performance.csv"
df.to_csv(output_path, index=False)

print("\nCleaned file saved successfully.")
print("Final Shape:", df.shape)