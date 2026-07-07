import pandas as pd
import numpy as np

#================= ESTAÇÃO 1: IMPORTAÇÃO DE DADOS EM BRUTO =================

#LER DADOS DE CSV PARA UM DATAFRAME
df_vgsales = pd.read_excel("data/1stCleaningPhase/Trabalho_Final_Clean_vgsales_Excel.xlsx", sheet_name="Trabalho_Final_Clean_vgsales_Ex")

#INFORMAÇÕES DO FICHEIRO IMPORTADO
print("\n--- DATAFRAME INFO ---")
print(f"\nPrimeiras linhas:\n{df_vgsales.head()}")
print(f"\nValores nulos por coluna:\n{df_vgsales.isna().sum()}")
print(f"\nDescrição estatística:\n{df_vgsales.describe()}")
print(f"\nEstrutura do DataFrame:\n{df_vgsales.shape}")
print(f"\nInformações do DataFrame:\n")
df_vgsales.info()




# ================= ESTAÇÃO 2: LIMPEZA DE DADOS =================
#LISTAGEM DOS NULOS EM PUBLISHER
print(f"\nNulos em PUBLISHER:\n{df_vgsales['Publisher'].isna().sum()}") #contagem
#IMPRIMIR OS NULOS
print(f"\nLinhas com nulos em PUBLISHER:\n{df_vgsales[df_vgsales['Publisher'].isna()]}") #imprimir os nulos
#DROPPAR OS NULOS EM PUBLISHER
df_vgsales = df_vgsales.dropna(subset=['Publisher'])
#LISTAGEM DOS NULOS EM PUBLISHER APÓS DROPPAR
print(f"\nNulos em PUBLISHER após droppar:\n{df_vgsales['Publisher'].isna().sum()}") #contagem

#CONTAGEM DE LINHAS EM PUBLISHER COM UNKNOWN
print(f"\nLinhas com PUBLISHER = 'Unknown':\n{df_vgsales[df_vgsales['Publisher'] == 'Unknown'].shape[0]}") #contagem

#LISTAGEM
print(f"\nLinhas com PUBLISHER = 'Unknown':\n{df_vgsales[df_vgsales['Publisher'] == 'Unknown']}") #imprimir as linhas

#PARTE DA LIMPEZA FEITA EM EXCEL POWER QUERY POIS EXISTEM DETALHES MAIS SIMPLES DE FAZER LÁ
#EX.: SUBSITUIÇÃO DE VALORES NAS COLUNAS "CONSOLE" E "PUBLISHER"

#FORÇAR A COLUNA "NAME" A SER DO TIPO STRING
df_vgsales["Name"] = df_vgsales["Name"].astype(str)

#ELIMINAR LINHAS ONDE YEAR = 2020, POIS SÃO OUTLIERS
print(f"\nLinhas com YEAR = 2020:\n{df_vgsales[df_vgsales['Year'] == 2020]}") #imprimir as linhas
df_vgsales = df_vgsales.drop(df_vgsales[df_vgsales['Year'] == 2020].index) #dropar as linhas
print(f"\nLinhas com YEAR = 2020 após droppar:\n{df_vgsales[df_vgsales['Year'] == 2020]}") #imprimir as linhas

#CRIAR COLUNA MANUFACTURER A PARTIR DE PLATFORM
#IMPRIMIR VALORES UNICOS DE PLATFORM
print(f"\nValores únicos de PLATFORM:\n{df_vgsales['Platform'].unique()}") #imprimir os valores únicos

#LISTAS DE MANUFACTURERS
nintendo = ["Wii", "WiiU", "Game Cube", "Nintendo 3DS", "Nintendo DS", "Nintendo 64", "NES", "Super NES", "Game Boy", "Game Boy Advance"]
sony = ["PS", "PS2", "PS3", "PS4", "PSP", "PS Vita"]
microsoft = ["Xbox 360", "Xbox One", "Xbox"]
sega = ["DreamCast", "Sega Game Gear", "Sega Saturn", "Sega Genesis", "Sega MegaDrive"]
atari = ["Atari 2600"]
other_manufacturers = ["TurboGrafx-16", "PCFX", "Neo Geo", "3DO", "Wonder Swan"]

df_vgsales["Manufacturer"] = df_vgsales["Platform"].apply(lambda platform: 
                                                        "Nintendo" if platform in nintendo
                                                        else "Sony" if platform in sony
                                                        else "Microsoft" if platform in microsoft
                                                        else "Sega" if platform in sega
                                                        else "Atari" if platform in atari
                                                        else "Others" if platform in other_manufacturers
                                                        else "PC"
)

df_vgsales.info()
print(df_vgsales.head())

#ORDERNAR DADOS POR RANK
df_vgsales = df_vgsales.sort_values(by="Rank", ascending=True)
print(df_vgsales.head())

#EXPORTAR O DATAFRAME LIMPO PARA CSV
df_vgsales.to_csv("data/processed/Trabalho_Final_Processed_vgsales.csv", index=False)