import requests
import pandas as pd
import os

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

output_folder = r"data\processed"

os.makedirs(output_folder, exist_ok=True)

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_name = f"{name}.csv"

    nav_df.to_csv(
        os.path.join(output_folder, file_name),
        index=False
    )

    print(f"{name} saved successfully")