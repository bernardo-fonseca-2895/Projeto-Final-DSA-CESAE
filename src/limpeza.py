import pandas as pd
import numpy as np

#================= ESTAÇÃO 1: IMPORTAÇÃO DE DADOS EM BRUTO =================

#LER DADOS DE CSV PARA UM DATAFRAME
df_vgsales = pd.read_excel("data/1stCleaningPhase/Trabalho_Final_Clean_vgsales_Excel.xlsx", sheet_name="Trabalho_Final_Clean_vgsales_Ex")

print("--- DATAFRAME INFO ---")
print(df.head())
print(df.info())
print(df.isna().sum())
print(df.describe())