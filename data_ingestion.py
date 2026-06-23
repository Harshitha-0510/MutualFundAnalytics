import pandas as pd
import os

folder_path = r"data\raw\Bluestock_MF_Datasets"

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

print("="*60)
print("MUTUAL FUND DATA INGESTION")
print("="*60)

for file in csv_files:

    print("\n")
    print("="*60)
    print(f"Dataset : {file}")
    print("="*60)

    file_path = os.path.join(folder_path, file)

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())