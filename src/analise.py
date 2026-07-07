import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#IMPORTAR O DATAFRAME LIMPO
df_vgsales = pd.read_csv("data/processed/Trabalho_Final_Processed_vgsales.csv")

#VERIFICAR A IMPORTAÇÃO
df_vgsales.info()
print(df_vgsales.head())

#INFO RELEVANTE: ESTES DADOS NÃO CONTAM COM REGISTOS PÓS NINTENDO SWITCH/SWITCH 2 E PLAYSTAION 5

# ================ ESTAÇÃO 3: ANÁLISE DE DADOS =================
#ANÁLISE EXPLORATÓRIA DE DADOS (EDA)

print("\n--- ANÁLISE EXPLORATÓRIA DE DADOS (EDA) ---")
print("\nVENDAS GLOBAIS POR MANUFACTURER:")
print(df_vgsales.groupby("Manufacturer")["Global_Sales Revised (M)"].sum().sort_values(ascending=False))

print("\nVENDAS GLOBAIS POR MANUFACTURER AO LONGO DAS DÉCADAS:") #COM PIVOT TABLE
