import pandas as pd
import glob

# Step 1: Load all CSV files from the data folder
files = glob.glob("data/*.csv")
dfs = []

for file in files:
    df = pd.read_csv(file)

    # Step 2: Filter only Pink Morsels (case-insensitive)
    df = df[df["product"].str.lower() == "pink morsel"].copy()

    # Step 3: Clean price and calculate sales
    df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)
    df["Sales"] = df["quantity"] * df["price"]

    # Step 4: Keep required columns
    df = df[["Sales", "date", "region"]]

    dfs.append(df)

# Step 5: Combine and save
if dfs:
    final_df = pd.concat(dfs, ignore_index=True)
    final_df.to_csv("output.csv", index=False)
    print("✅ Done! Your output.csv file has been created.")
else:
    print("❌ No files found. Check your folder paths!")
