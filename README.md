# Projeto de Ciência de Dados: Previsão Renda 

Este projeto de ciência de dados foi desenvolvido como um dos requisito para a conclusão do curso "Profissão: Cientista de Dados" oferecido pela EBAC (Escola Britânica de Artes Criativas). O objetivo principal deste projeto foi explorar técnicas de análise de dados e previsão de renda utilizando um conjunto de dados simulando uma base real.

## Descrição do Projeto
Neste projeto, utilizamos um conjunto de dados que contém informações socioeconômicas de indivíduos, como idade, nível de escolaridade, ocupação, estado civil, entre outros. A partir desses dados, buscamos construir um modelo de previsão de renda, ou seja, um algoritmo capaz de estimar a renda mensal de uma pessoa com base em suas características.

No projeto também consta a criação de uma aplicação web para análise exploratória da base de dados utilizando o Streamlit.

## Metodologia e Ferramentas
Para atingir nosso objetivo, seguimos uma metodologia CRISP-DM (Cross Industry Standard Process for Data Mining) composta devárias etapas. 

Primeiramente, realizamos uma análise exploratória dos dados, buscando compreender a distribuição das variáveis, identificar possíveis correlações e verificar a presença de valores faltantes.

Em seguida, realizamos o pré-processamento dos dados, tratando os dados faltantes, retirando variáveis desnecessárias e separando as bases de treino e teste para serem usados nos modelos preditivos.

Utilizamos técnicas de aprendizado de máquina para construir um modelo de previsão de renda. Experimentamos  alguns modelos de regressão linear e árvores de decisão, e avaliamos o desempenho de cada um deles utilizando o coeficiente de determinação.

As principais ferramentas utilizadas neste projeto foram a linguagem de programação Python, juntamente com bibliotecas populares de ciência de dados, como Pandas, Matplotlib, Statsmodels e Scikit-learn. Também utilizamos o Jupyter Notebook como ambiente de desenvolvimento para facilitar a análise e visualização dos dados. Foi utilizado também o Streamlit para desenvolver uma aplicação para análise exploratória dos dados.

## Resultados e Conclusões

Os modelos desenvolvidos apresentaram um coeficiente de determinação (R²) máximo de 0,33, indicando um valor relativamente baixo de ajuste aos dados. Esse baixo coeficiente pode ser atribuído a uma série de fatores, como a complexidade do problema em questão, a qualidade dos dados disponíveis, a escolha inadequada das variáveis independentes ou a existência de variáveis relevantes não consideradas.

Salienta-se que, foram utilizadas as técnicas e etratégias vistas até este ponto do curso de Cientista de Dados da EBAC ( Módulo 15). Novas técnicas poderão  ser aplicadas posteriormente para melhorar o resultado deste projeto.

### Aplicação para análise exploratória dos dados:


[Streamlit-Projeto 2_.webm](https://github.com/provietti/EBAC_Projeto_2_Previsao_Renda/assets/66576156/80167a84-7942-4cd9-afcc-83e1b5f0ddc3)


A aplicação inclui as seguintes funções:

- Upload da base de dados a ser analisada em csv;
- Análise exploratória  das variáveis da base de dados a escolha do usuário;
- Filtro dos dados pela faixa de renda;
- Análise temporal dos dados, interativa, podendo escolher as categorias das variáveis que serão plotadas nos gráficos;
- Download do dataframe e gráficos gerados;

