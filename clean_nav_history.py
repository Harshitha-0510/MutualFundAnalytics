import pandas as pd
import os

# Load dataset
file_path = r"data\raw\Bluestock_MF_Datasets\02_nav_history.csv"
df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort values
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Validate NAV > 0
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV Records:", len(invalid_nav))

# Save cleaned file
output_path = r"data\processed\clean_nav_history.csv"
df.to_csv(output_path, index=False)

print("Cleaned file saved successfully.")
print("Final Shape:", df.shape)