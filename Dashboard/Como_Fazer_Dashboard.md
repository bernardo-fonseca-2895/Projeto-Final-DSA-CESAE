**PREPARAR A DASHBOARD EM EXCEL**

1. **Obter Dados -> Texto/CSV** 'data/processed/vgsales_processed.csv' -> *Carregar*.
2. **Transformar Dados** abre o Power Query para fazer ultimas limpezas simples para simplificar consulta e construção do dashboard.
3. **Substiruir Valores** Substituir . por , nas colunas sales (NA, EU, JP, Other, Global, Global_Verified).
4. Alterar os Tipos para os correctos. Todas as colunas vao estar como geral. Passar as colunas Rank e Year para número inteiro e as colunas sales para número decimal.
5. **Base -> Fechar e Carregar -> Fechar e Carregar para... -> (CHECK BOX)Apenas criar ligação e Adicionar estes dados ao Modelo de Dados -> OK**.
6. **Power Pivot** Gerir Modelo de dados.
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
    -KPIs Usando as 6 medidas de Power Pivot na sceçâo Valores;
    -Gener usando Gener como linhas e as medidas Vendas Totais e Total Entradas como valores. Filtrar como top 5(Filtros de valores -> 10 mais... -> inserir '5' na segunda box -> OK);
    -Platform usando Platform como linhas e as medidas Vendas Totais e Total Entradas como valores.Filtrar como top 5(Filtros de valores -> 10 mais... -> inserir '5' na segunda box -> OK);
    -Manufacturer usando Manufacturer como linhas e as medidas Vendas Totais e Total Entradas como valores;
    -Publisher usando Publisher como linhas e as medidas Vendas Totais e Total Entradas como valores. Filtrar como top 10(Filtros de valores -> 10 mais... -> OK);
    -Name usando Name como linhas e as medidas Vendas Totais como valores. Filtrar como top 3(Filtros de valores -> 10 mais... -> inserir '3' na segunda box -> OK);
    -Tabelas ordenadas por Vendas Totais do maior ao mais pequeno excepto Tabela KPIs.
11. **Inserir -> Segmentação de Dados** Selecione a tabela dinâmica KPIs e insira 3 segmentações de Dados:
    -Gener;
    -Manufacturer;
    -Decade;
    -Segmentações Ordenadas de A a Z;
12. **Inserir -> Gráfico Dinâmico** Foram usados 4 gráficos. Cada um deles é criado a partir de uma das tabelas dinâmicas:
    -Selecionando a tabela Platform criar um grafico de Colunas Agrupadas 3d;    
    -Selecionando a tabela Gener criar um grafico de Colunas Agrupadas 3d;
    -Selecionando a tabela Publisher criar um grafico de Barras Agrupadas 3d;
    -Selecionando a tabela Manufacturer criar um grafico de Barras Agrupadas 3d.
13. Estilizar a gosto.
14. **Guardar** Como Projeto Final Excel.xlsx