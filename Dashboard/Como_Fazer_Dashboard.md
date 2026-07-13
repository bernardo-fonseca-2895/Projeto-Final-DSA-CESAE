**PREPARAR A DASHBOARD EM EXCEL**

1. **Obter Dados -> Texto/CSV** 'data/processed/vgsales_processed.csv' -> *Carregar*.
2. **Transformar Dados:** Abrir o PowerQuery para fazer últimas limpezas (O PowerQuery não assume os tipos corretos nas colunas "-Sales", "Year" e "Rank")
3. **Substiruir Valores** Substituir . por , nas colunas "Sales" (NA, EU, JP, Other, Global, Global_Verified).
4. Passar as colunas Rank e Year para Número Inteiro e as colunas Sales para número decimal.
5. **Base -> Fechar e Carregar -> Fechar e Carregar para... -> (CHECK BOX)Apenas criar ligação e Adicionar estes dados ao Modelo de Dados -> OK**.
6. **Power Pivot -> Gerir Modelo de dados**.
7. Criar 6 medidas:
    -Vendas Totais:=SUM([Global_Sales_Verified]);
    -Vendas NA:=SUM([NA_Sales]);
    -Vendas EU:=SUM([EU_Sales]);
    -Vendas JP:=SUM([JP_Sales]);
    -Vendas Other:=SUM([Other_Sales]);
    -Total Entradas:=COUNTROWS(Trabalho_Final_Processed_vgsales).
8. Fechar Power Pivot.
9. Possiveis visuais para responder as questões iniciais.
10. **Inserir -> Tabela Dinâmica -> A partir do Modelo de Dados** -Criar 6 tabelas dinâmicas a partir do modelo de dados:
    -"KPIs" Usando as 6 medidas de Power Pivot no campo "Valores";
    -"Genres" usando Genre no campo "Linhas" e as medidas Vendas Totais e Total Entradas no campo "Valores". Filtrar como Top 5 (Filtros de valores -> 10 mais... -> inserir '5' na segunda box -> OK);
    -"Platform" usando Platform no campo "Linhas" e as medidas Vendas Totais e Total Entradas no campo "Valores". Filtrar como Top 5(Filtros de valores -> 10 mais... -> inserir '5' na segunda box -> OK);
    -"Manufacturer" usando Manufacturer no campo "Linhas" e as medidas Vendas Totais e Total Entradas no campo "Valores";
    -"Publisher" usando Publisher no campo "Linhas" e as medidas Vendas Totais e Total Entradas no campo "Valores". Filtrar como Top 10(Filtros de valores -> 10 mais... -> OK);
    -"Name" usando Name no campo "Linhas" e a medida Vendas Totais no campo "Valores". Filtrar como Top 3(Filtros de valores -> 10 mais... -> inserir '3' na segunda box -> OK);
    -Tabelas ordenadas por Vendas Totais do maior ao mais pequeno excepto Tabela KPIs.
11. **Inserir -> Segmentação de Dados** Selecione a tabela dinâmica KPIs e insira 3 segmentações de Dados:
    -Genre;
    -Manufacturer;
    -Decade;
    -Segmentações Ordenadas de A a Z;
12. **Inserir -> Gráfico Dinâmico** Foram usados 4 gráficos. Cada um deles é criado a partir de uma das tabelas dinâmicas:
    -Selecionando a tabela Platform, criar um gráfico de Colunas Agrupadas 3D;    
    -Selecionando a tabela Genre, criar um gráfico de Colunas Agrupadas 3D;
    -Selecionando a tabela Publisher, criar um gráfico de Barras Agrupadas 3D;
    -Selecionando a tabela Manufacturer, criar um gráfico Pie.
13. Estilizar a gosto.
14. **Guardar como:** Projeto Final Excel.xlsx