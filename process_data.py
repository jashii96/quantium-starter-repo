import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

csv_files = list(DATA_DIR.glob("*.csv"))

dfs = []

for file in csv_files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # Clean price column
    df["price"] = (
        df["price"]
        .replace(r"[\$,]", "", regex=True)
        .astype(float)
    )

    # Calculate sales
    df["sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["sales", "date", "region"]]

    dfs.append(df)

final_df = pd.concat(dfs, ignore_index=True)

final_df.to_csv(
    "formatted_sales_data.csv",
    index=False
)

print("Output file created successfully")
print(final_df.head())