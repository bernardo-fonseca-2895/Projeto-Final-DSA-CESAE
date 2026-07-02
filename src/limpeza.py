import pandas as pd
import numpy as np

#================= ESTAÇÃO 1: IMPORTAÇÃO DE DADOS EM BRUTO =================

#LER DADOS DE CSV PARA UM DATAFRAME
df = pd.read_csv("data/1stCleaningPhase/Trabalho_final_Clean_vgsales.csv", sep=";", encoding="utf-8")

#INFORMAÇÕES DO FICHEIRO IMPORTADO
print("\n--- DATAFRAME INFO ---")
print(f"\nPrimeiras linhas:\n{df.head()}")
print(f"\nValores nulos por coluna:\n{df.isna().sum()}")
print(f"\nDescrição estatística:\n{df.describe()}")
print(f"\nEstrutura do DataFrame:\n{df.shape}")
print(f"\nInformações do DataFrame:\n")
df.info()




# ================= ESTAÇÃO 2: LIMPEZA DE DADOS =================
#LISTAGEM DOS NULOS EM PUBLISHER
print(f"\nNulos em PUBLISHER:\n{df['Publisher'].isna().sum()}") #contagem
#IMPRIMIR OS NULOS
print(f"\nLinhas com nulos em PUBLISHER:\n{df[df['Publisher'].isna()]}") #imprimir os nulos
#DROPPAR OS NULOS EM PUBLISHER
df = df.dropna(subset=['Publisher'])
#LISTAGEM DOS NULOS EM PUBLISHER APÓS DROPPAR
print(f"\nNulos em PUBLISHER após droppar:\n{df['Publisher'].isna().sum()}") #contagem

#CONTAGEM DE LINHAS EM PUBLISHER COM UNKNOWN
print(f"\nLinhas com PUBLISHER = 'Unknown':\n{df[df['Publisher'] == 'Unknown'].shape[0]}") #contagem

#LISTAGEM
print(f"\nLinhas com PUBLISHER = 'Unknown':\n{df[df['Publisher'] == 'Unknown']}") #imprimir as linhas

