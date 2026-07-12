import pandas as pd


#================= ESTAÇÃO 1: IMPORTAÇÃO DE DADOS EM BRUTO =================

#LER DADOS DE CSV PARA UM DATAFRAME
df_vgsales = pd.read_excel("data/1stCleaningPhase/vgsales_fase1.xlsx", sheet_name="vgsales")

#INFORMAÇÕES DO FICHEIRO IMPORTADO
print("\n--- DATAFRAME INFO ---")
print(f"\nPrimeiras linhas:\n{df_vgsales.head()}")
print(f"\nValores nulos por coluna:\n{df_vgsales.isna().sum()}")
print(f"\nDescrição estatística:\n{df_vgsales.describe()}")
print(f"\nEstrutura do DataFrame:\n{df_vgsales.shape}")
print(f"\nInformações do DataFrame:\n")
df_vgsales.info()




# ================= ESTAÇÃO 2: LIMPEZA DE DADOS =================
#PARTE DA LIMPEZA FEITA EM EXCEL POWER QUERY POIS EXISTEM DETALHES MAIS SIMPLES DE FAZER LÁ
#EX: CRIAÇÃO DA COLUNA DECADE A PARTIR DE EXEMPLO

#FORÇAR A COLUNA "NAME" A SER DO TIPO STRING (IMPORTADA COMO TIPO OBJECT)
df_vgsales["Name"] = df_vgsales["Name"].astype(str)


#CRIAR COLUNA MANUFACTURER A PARTIR DE PLATFORM
#IMPRIMIR VALORES UNICOS DE PLATFORM
print(f"\nValores únicos de PLATFORM:\n{df_vgsales['Platform'].unique()}") #imprimir os valores únicos

#LISTAS DE MANUFACTURERS
nintendo = ["Wii", "WiiU", "GC", "3DS", "DS", "N64", "NES", "SNES", "GB", "GBA"]
sony = ["PS", "PS2", "PS3", "PS4", "PSP", "PSV"]
microsoft = ["X360", "XOne", "XB"]
sega = ["DC", "GG", "SAT", "GEN", "SCD"]
atari = ["2600"]
other_manufacturers = ["TG16", "PCFX", "NG", "3DO", "WS"]

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
df_vgsales.to_csv("data/processed/vgsales_processed.csv",sep=";", index=False)