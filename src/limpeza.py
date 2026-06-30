import pandas as pd
import numpy as np

df = pd.read_csv("data/raw/vgsales.csv")

print("--- DATAFRAME INFO ---")
print(df.head())
print(df.info())
print(df.isna().sum())
print(df.describe())