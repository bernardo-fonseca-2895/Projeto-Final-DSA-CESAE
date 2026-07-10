import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

Path("reports").mkdir(exist_ok=True)

#IMPORTAR O DATAFRAME LIMPO
df_vgsales = pd.read_csv("data/processed/vgsales_processed.csv")

#VERIFICAR A IMPORTAÇÃO
df_vgsales.info()
print(df_vgsales.head())

#INFO RELEVANTE: ESTES DADOS NÃO CONTAM COM REGISTOS PÓS NINTENDO SWITCH/SWITCH 2 E PLAYSTATION 5
#INFO RELEVANTE: FORAM REMOVIDOS OS DADOS DA DÉCADA DE 2020 POIS APENAS CONTINHAM UM REGISTO, SENDO CLASSIFICADO COMO OUTLIER
#INFO RELEVANTE: MENÇÕES DE POPULARIDADE PODEM SER RELACIONADAS COM O VALOR DAS VENDAS, JÁ QUE POR NORMA OS VIDEOJOGOS COSTUMAM TER O MESMO PREÇO

# ================ ESTAÇÃO 3: ANÁLISE DE DADOS =================
#--- ANÁLISE EXPLORATÓRIA DE DADOS (EDA) ---
#DADOS GERAIS
media_vendas_globais = df_vgsales["Global_Sales Revised (M)"].mean()
mediana_vendas_globais = df_vgsales["Global_Sales Revised (M)"].median()
print(f"\nMEDIA DE VENDAS GLOBAIS (MILHÕES): {media_vendas_globais}")
print(f"\nMEDIANA DAS VENDAS GLOBAIS (MILHÕES): {mediana_vendas_globais}")

#A MÉDIA É MAIS ALTA QUE A MEDIANA, A MÉDIA GERAL É BAIXA MAS HÁ ALGUNS VALORES COM VENDAS MUITO ALTAS A PUXAR A MÉDIA PARA CIMA

maior_venda_total = df_vgsales["Global_Sales Revised (M)"].max()
menor_venda_total = df_vgsales["Global_Sales Revised (M)"].min()
desvio_padrao = df_vgsales["Global_Sales Revised (M)"].std()
print(f"\nMAIOR VENDA GLOBAL (MILHÕES): {maior_venda_total}")
print(f"\nMENOR VENDA TOTAL (MILHÕES): {menor_venda_total}")
print(f"\nDESVIO PADRÃO: {desvio_padrao}")

#NO GERAL OS DADOS NÃO SE DESVIAM MUITO DA NORMA

#TOP 10 JOGOS ALL TIME
top10_jogos_alltime = (df_vgsales.groupby("Name")["Global_Sales Revised (M)"].sum().sort_values(ascending=False).head(10))
print(f"\nTOP 10 JOGOS ALL TIME:\n{top10_jogos_alltime}")

#NO DATASET CRU, NÃO EXISTE GTA V NO TOP10, NO ENTANTO, GTA V TEM MULTIPLAS ENTRADAS DEVIDO A SER PUBLICADO EM PLATAFORMAS DIFERENTES, 
#LOGO, AO ACUMULAR, ESTE ATINGE VALORES SUFICIENTES PARA ENTRAR NO TOP 10

top10_jogos_alltime.plot(kind="barh")
plt.xlabel("Total Vendas (Milhões)")
plt.ylabel("Nome")
plt.tight_layout()
plt.savefig("reports/top10_jogos_alltime_barh", dpi=120)
plt.show()
plt.close()

#TOP 5 PUBLISHERS POR VENDAS GLOBAIS
top5_publishers = (df_vgsales.groupby("Publisher")["Global_Sales Revised (M)"].sum().sort_values(ascending=False).head(5))
print(f"\nTOP 5 PUBLISHERS POR TOTAL DE VENDAS:\n{top5_publishers}")

#AVALIA O DESEMPENHO DOS PUBLISHERS E MOSTRA APENAS OS 5 MELHORES, JÁ QUE SÃO IMENSOS

top5_publishers.plot(kind="barh")
plt.xlabel("Total Vendas (Milhões)")
plt.ylabel("Publisher")
plt.tight_layout()
plt.savefig("reports/top5_publishers_barh", dpi=120)
plt.show()
plt.close()


#ANÁLISE ORIENTADA A GENRE
#TOP 5 GENRES POR VENDAS
top5_genres = (df_vgsales.groupby("Genre")["Global_Sales Revised (M)"].sum().sort_values(ascending=False).head(5))
print(f"\nTOP 5 GENRES POR TOTAL DE VENDAS:\n{top5_genres}")

#AVALIA OS GENRES MAIS POPULARES HISTORICAMENTE

top5_genres.plot(kind="barh")
plt.xlabel("Total Vendas (Milhões)")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("reports/top5_genres_barh", dpi=120)
plt.show()
plt.close()

#FREQUÊNCIA DE CADA GENRE
frequencia_genres = df_vgsales["Genre"].value_counts()
print(f"\nFREQUÊNCIA DE CADA GENRE: {frequencia_genres}")

#AVALIA A QUANTIDADE DE ENTRADAS PARA CADA GENRE
#TAMBÉM PODE SER UMA MÉTRICA DE POPULARIDADE, JÁ QUE SE É SABIDO QUE UM GENRE É POPULAR, PODE SER IDEAL INVESTIR EM JOGOS DESSE MESMO GENRE

frequencia_genres.plot(kind="bar")
plt.title("Frequência por Genre")
plt.xlabel("Genre")
plt.ylabel("Nº de Entradas")
plt.tight_layout()
plt.savefig("reports/frequencia_genre_bars", dpi=120)
plt.show()
plt.close()

#VENDAS GLOBAIS POR GÉNERO AO LONGO DAS DÉCADAS COM PIVOT TABLE
vendas_genero_decada = df_vgsales.pivot_table(values="Global_Sales Revised (M)",
                                             index="Decade",
                                             columns="Genre",
                                             aggfunc="sum")

print(f"\nVENDAS POR GENRE AO LONGO DAS DÉCADAS:\n{vendas_genero_decada}")

#AVALIA A EVOLUÇÃO DE CADA GENRE AO LONGO DAS DÉCADAS
    
# vendas_genero_decada.plot(kind="line")
# plt.title("Vendas Globais Por Género Ao Longo Das Décadas")
# plt.xlabel("Decadas")
# plt.ylabel("Soma das Vendas Globais")
# plt.show()

plt.figure(figsize=(12, 6))
sns.heatmap(vendas_genero_decada, annot=True, fmt='.0f',
            cmap='YlOrRd', linewidths=0.5)
plt.title("Vendas globais por género e década (Milhões)")
plt.ylabel("Décadas")
plt.tight_layout()
plt.savefig("reports/heatmap_genero_decada.png", dpi=120)
plt.show()
plt.close()


#ANÁLISE ORIENTADA A MANUFACTURER
#VENDAS POR MANUFACTURER
vendas_manufacturer = df_vgsales.groupby("Manufacturer")["Global_Sales Revised (M)"].sum().sort_values(ascending=False)
print(f"\nTOTAL DE VENDAS POR MANUFACTURER:\n{vendas_manufacturer}")

#AVALIA O DESEMPENHO DE CADA MANUFACTURER NO MERCADO

vendas_manufacturer.plot(kind="bar")
plt.title("Vendas Globais por Manufacturer (Milhões)")
plt.xlabel("Manufacturer")
plt.ylabel("Vendas Globais (Milhões)")
plt.tight_layout()
plt.savefig("reports/vendas_manufacturer_bars", dpi=120)
plt.show()
plt.close()

#PERCENTAGEM QUE CADA MANUFACTURER OCUPA NOS DADOS
frequencia_manufacturer_percent = df_vgsales["Manufacturer"].value_counts(normalize=True)*100
print(f"\nPERCENTAGEM QUE CADA MANUFACTURER OCUPA NOS DADOS:\n{frequencia_genres}")

#AVALIA A PRESENÇA DE CADA MANUFACTURER NO MERCADO

frequencia_manufacturer_percent.plot(kind="pie", autopct = "%1.1f%%")
plt.title("Frequência de entradas por Manufacturer (%)")
plt.tight_layout()
plt.savefig("reports/frequencia_manufacturer_percent_pie", dpi=120)
plt.show()
plt.close()

#EVOLUÇÃO DE CADA MANUFACTURER AO LONGO DO TEMPO
evolucao_manufacturer = df_vgsales.pivot_table(
    values="Name",
    index="Decade",
    columns="Manufacturer",
    aggfunc="count"
)
print(f"\nEVOLUÇÃO DE CADA MANUFACTURER AO LONGO DO TEMPO:\n{evolucao_manufacturer}")

#AVALIA A EVOLUÇÃO DE CADA MANUFACTURER NO MERCADO, IDEAL PARA VER OS CICLOS DE VIDA DE CADA UM

evolucao_manufacturer.plot(kind="line")
plt.title("Evolução dos Manufacturers ao longo do tempo")
plt.ylabel("Total de Entradas")
plt.tight_layout()
plt.savefig("reports/evolucao_manufacturer_lines", dpi=120)
plt.show()
plt.close()

#EVOLUÇÃO POR TOTAL DE VENDAS
evolucao_manufacturer_vendas = df_vgsales.pivot_table(
    values="Global_Sales Revised (M)",
    index="Decade",
    columns="Manufacturer",
    aggfunc="sum"
)
print(f"\nEVOLUÇÃO DE CADA MANUFACTURER AO LONGO DO TEMPO POR TOTAL DE VENDAS:\n{evolucao_manufacturer_vendas}")

#MESMO DO GRAFICO ANTERIOR, MAS PARA O TOTAL DE VENDAS (MESMA CONCLUSÃO)

evolucao_manufacturer_vendas.plot(kind="line")
plt.title("Evolução dos Manufacturers ao longo do tempo (Vendas)")
plt.ylabel("Total de Vendas (Milhões)")
plt.tight_layout()
plt.savefig("reports/evolucao_manufacturer_vendas_lines", dpi=120)
plt.show()
plt.close()

#ANÁLISE ORIENTADA ÀS REGIÕES
#TOTAL DE VENDAS POR REGIÃO
total_vendas_NA = df_vgsales["NA_Sales (M)"].sum()
total_vendas_EU = df_vgsales["EU_Sales (M)"].sum()
total_vendas_JP = df_vgsales["JP_Sales (M)"].sum()
total_vendas_Others = df_vgsales["Other_Sales (M)"].sum()

print("\n=====TOTAL VENDAS POR REGIÃO:=====")
print(f"\nNA: {total_vendas_NA}")
print(f"EU: {total_vendas_EU}")
print(f"JP: {total_vendas_JP}")
print(f"Outros: {total_vendas_Others}")

#AVALIA GENERICAMENTE VENDAS POR REGIÃO

#RESPETIVO GRÁFICO
regioes = {
    "NA": total_vendas_NA,
    "EU": total_vendas_EU,
    "JP": total_vendas_JP,
    "Outras": total_vendas_Others
}

df_regioes = pd.Series(regioes)

df_regioes.plot(kind="bar")
plt.title("Total de Vendas por região (Milhões)")
plt.xlabel("Região")
plt.ylabel("Total de Vendas (Milhões)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("reports/vendas_regiao_bar", dpi=120)
plt.show()
plt.close()

#GENRES MAIS POPULARES POR REGIÃO
vendas_genero_regiao = df_vgsales.pivot_table(
    values=["NA_Sales (M)", "EU_Sales (M)", "JP_Sales (M)", "Other_Sales (M)"],
    index="Genre",
    aggfunc="sum"
)

print(f"\nPOPULARIDADE DE CADA GENRE POR REGIÃO:\n{vendas_genero_regiao}")

#AVALIA O DESEMPENHO DE CADA GENRE POR REGIÃO

#RESPETIVO GRÁFICO
plt.figure(figsize=(10, 6))
sns.heatmap(vendas_genero_regiao, annot=True, fmt='.0f',
            cmap='YlOrRd', linewidths=0.5)
plt.title('Vendas por género e região (M)')
plt.xlabel("Regiões")
plt.tight_layout()
plt.savefig("reports/vendas_genero_regiao_heatmap", dpi=120)
plt.show()
plt.close()

#TOP 5 JOGOS NA REGIÃO NA
top5_NA = (df_vgsales.groupby("Name")["NA_Sales (M)"].sum().sort_values(ascending=False).head(5))
print(f"\nTOP 5 JOGOS NA REGIÃO NA:\n{top5_NA}")

top5_NA.plot(kind="barh")
plt.xlabel("Vendas NA (Milhões)")
plt.ylabel("Título")
plt.tight_layout()
plt.savefig("reports/top5_NA_barh", dpi=120)
plt.show()
plt.close()

#TOP 5 JOGOS NA REGIÃO EU
top5_EU = (df_vgsales.groupby("Name")["EU_Sales (M)"].sum().sort_values(ascending=False).head(5))
print(f"\nTOP 5 JOGOS NA REGIÃO EU:\n{top5_EU}")

top5_EU.plot(kind="barh")
plt.xlabel("Vendas EU (Milhões)")
plt.ylabel("Título")
plt.tight_layout()
plt.savefig("reports/top5_EU_barh", dpi=120)
plt.show()
plt.close()

#TOP 5 JOGOS NA REGIÃO JP
top5_JP = (df_vgsales.groupby("Name")["JP_Sales (M)"].sum().sort_values(ascending=False).head(5))
print(f"\nTOP 5 JOGOS NA REGIÃO JP:\n{top5_JP}")

top5_JP.plot(kind="barh")
plt.xlabel("Vendas JP (Milhões)")
plt.ylabel("Título")
plt.tight_layout()
plt.savefig("reports/top5_JP_barh", dpi=120)
plt.show()
plt.close()

#TOP 5 JOGOS NOUTRAS REGIÕES
top5_Others = (df_vgsales.groupby("Name")["Other_Sales (M)"].sum().sort_values(ascending=False).head(5))
print(f"\nTOP 5 JOGOS NOUTRAS REGIÕES:\n{top5_Others}")

top5_Others.plot(kind="barh")
plt.xlabel("Vendas Noutras Regiões (Milhões)")
plt.ylabel("Título")
plt.tight_layout()
plt.savefig("reports/top5_others_barh", dpi=120)
plt.show()
plt.close()

print("\n==== FIM DA ANÁLISE ====")
print("\nGRÁFICOS CARREGADOS PARA A PASTA REPORTS")