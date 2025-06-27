import pandas as pd
import os

def load_combined_data():
    base = r"C:\Users\niyim\Downloads\gender-gap-dash\data"
    files = ["Employment.csv", "innovation.csv", "Senior_Management.csv", "Entrepreneurship.csv"]
    dfs = []
    for f in files:
        df = pd.read_csv(os.path.join(base, f))
        df["Source"] = f.split(".")[0].capitalize().replace("_", " ")
        dfs.append(df)
    combined = pd.concat(dfs, ignore_index=True)
    return combined

