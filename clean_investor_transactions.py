import pandas as pd

# Load dataset
file_path = r"data\raw\Bluestock_MF_Datasets\08_investor_transactions.csv"
df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

# Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction_type values
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only expected transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]

invalid_types = df[~df["transaction_type"].isin(valid_types)]

print("Invalid Transaction Types:", len(invalid_types))

# Validate amount > 0
invalid_amount = df[df["amount_inr"] <= 0]

print("Invalid Amount Records:", len(invalid_amount))

# Check KYC values
print("\nUnique KYC Status Values:")
print(df["kyc_status"].unique())

# Save cleaned dataset
output_path = r"data\processed\clean_investor_transactions.csv"
df.to_csv(output_path, index=False)

print("\nCleaned file saved successfully.")
print("Final Shape:", df.shape)