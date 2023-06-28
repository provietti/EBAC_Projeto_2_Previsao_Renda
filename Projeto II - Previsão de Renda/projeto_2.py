import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

#Listas e Dicionários 

dict_vars = {'Quantidade de Filhos': 'qtd_filhos', 
                  'Idade': 'idade', 
                  'Tempo no Emprego': 'tempo_emprego',
                  'Quantidade de pessoas na resiência': 'qt_pessoas_residencia', 
                  'Renda': 'renda',
                  'Sexo': 'sexo',
                  'Posse de Veículo' : 'posse_de_veiculo', 
                  'Posse de imóvel' : 'posse_de_imovel', 
                  'Tipo de Renda' : 'tipo_renda',
                  'Escolaridade' : 'educacao', 
                  'Estado Civil' : 'estado_civil',
                  'Tipo de Residência' : 'tipo_residencia'
                  }


# Função para ler os dados
@st.cache_data()
def load_data(file_data):
    return pd.read_csv(file_data, sep=',')

# Função para filtrar por categorias
@st.cache_data()
def filtra_por_categorias(dados, var, categorias_selec):
    
    if 'tudo' in categorias_selec:
        return dados
    else:
        return dados[dados[var].isin(categorias_selec)].reset_index(drop=True)
    
# Função para converter o df para csv
@st.cache_data()
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# Função que Plota gráficos das variáveis quantitativas
@st.cache_data()
def plot_var_quant(var,data):
     plt.rc('figure', figsize=(20, 5))
     fig, axes = plt.subplots(1, 2)
     plt.subplots_adjust(hspace= 0.3)
     #histograma
     chart = sns.histplot(data = data,                  
                 alpha = .25, 
                 x = dict_vars[var],
                 bins = 20,
                 element = 'step',
                 kde = True, 
                 ax=axes[0])
     chart.set_xlabel(dict_vars[var], fontsize=12)
     chart.set_ylabel('Frequência',  fontsize=12)
     chart.set_title('Histograma - ' + var, fontsize=16)
     #boxplot
     chart2 = sns.boxplot(y= dict_vars[var], data = data, width = 0.3 ,ax=axes[1]) 
     chart2.set_ylabel(var,fontsize=12)
     chart2.set_title('Boxplot - ' + var, fontsize=16)
     st.pyplot(plt)
     plt.savefig('output/graph.png', bbox_inches = 'tight', transparent =  False)
     

# Função que Plota gráficos das variáveis qualitativas
def plot_var_quali(var,data):
      plt.rc('figure', figsize=(10,4))
     
      plt.subplots_adjust(hspace= 0.3)
      chart = sns.countplot(x = dict_vars[var], data = data)
      chart.set_xlabel(var, fontsize=12)
      chart.set_ylabel('Frequência',  fontsize=12)
      chart.set_title('Frequência - ' + var, fontsize=16)
      st.pyplot(plt)
      plt.savefig('output/graph.png', bbox_inches = 'tight', transparent =  False)

# Função que Plota gráficos das Renda x variavel (bivarida)
def  plot_biv(var,data):
      plt.rc('figure', figsize=(10,4))
      plt.subplots_adjust(hspace= 0.3)
      chart = sns.scatterplot(x = dict_vars[var], y = 'renda', data = data, alpha = .5)
      chart.set_xlabel(var, fontsize=12)
      chart.set_ylabel('Renda',  fontsize=12)
      chart.set_title('Renda x ' + var, fontsize=16)
      st.pyplot(plt)
      plt.savefig('output/graph.png', bbox_inches = 'tight', transparent =  False)

# Função que Plota gráficos  das amostras ao longo do tempo
@st.cache_data()
def plot_tempo(var,data):
      plt.rc('figure', figsize=(10,4))
      fig, axes = plt.subplots(1, 2)
      plt.subplots_adjust(hspace= 0.3, wspace = 0.3)
      var_ = dict_vars[var]

      #gráfico dos perfis de renda ao longo do tempo
      chart = sns.pointplot(x="data_ref", y = 'renda', hue = var_, data = data, dodge=True, ci = 95, ax = axes[1])
      chart.set_xlabel('Data', fontsize=12)
      chart.set_ylabel('Renda',  fontsize=12)
      
      chart.set_xticklabels(labels = data['data_ref'].unique(), rotation=90)
      chart.set_xticklabels(data['data_ref'].unique(), rotation=90)

      #gráfico da frequencia das variáveis qualitativas ao longo do tempo

      chart = sns.countplot(x='data_ref', hue = var_, data = data, ax = axes[0])
      chart.set_xlabel('Data', fontsize=12)
      chart.set_ylabel('Frequencia',  fontsize=12)
      
      chart.set_xticklabels(labels = data['data_ref'].unique(), rotation=90)
      chart.set_xticklabels(data['data_ref'].unique(), rotation=90)
     
      st.pyplot(plt)
      plt.savefig('output/graph.png', bbox_inches = 'tight', transparent =  False)
 
# Função principal da aplicação

def main():
    # Configuração inicial da página da aplicação
    st.set_page_config(
        page_title = "Dados Previsão de Renda", \
        page_icon = "💵",
        layout="wide",
        initial_sidebar_state='expanded'
    )

    list_quantitativas = list(dict_vars.keys())[:5]
    list_qualitativas = list(dict_vars.keys())[5:]
    list_vars_todas = list(dict_vars.keys())

    

    # Título principal da aplicação
    st.write('# Análise Exploratória dos Dados de Previsão de Renda')
    st.markdown("---")   
    
    # Apresenta a imagem na barra lateral da aplicação
    image = Image.open("img/bank.png")
    st.sidebar.image(image)

    # Botão para carregar arquivo na aplicação
    data_file_1 = st.sidebar.file_uploader("Upload dos dados dos clientes", type = ['csv'])
    
    # Se há conteúdo carregado na aplicação ela prossegue senão nada acontece
    if (data_file_1 is not None):
          df_renda = load_data(data_file_1 )
          # SELECIONA O TIPO DE GRÁFICO
          
          graph_type = st.sidebar.radio('Escolha a análise gráfica:', ('Variáveis Quantitativas', 'Variáveis Qualitativas', 'Bivariada', 'Análise Temporal'))
          max_renda = int(df_renda.renda.max())+1
          min_renda = int(df_renda.renda.min())-1
          faixa_renda= st.sidebar.slider(label='Filtrar pela faixa de renda', 
                                        min_value = min_renda,
                                        max_value = max_renda, 
                                        value = (min_renda, max_renda),
                                        step = 1000)
          st.sidebar.write('Renda Mínima: ', faixa_renda[0]) 
          st.sidebar.write('Renda Máxima: ', faixa_renda[1]) 
          df_renda = df_renda.query("renda >= @faixa_renda[0] and renda <= @faixa_renda[1]")
          
          # PLOTS    
          if graph_type == 'Variáveis Quantitativas':
                    st.write('## Análise - Variáveis Quantitativas')
                    st.write('### Descritiva')
                    st.write(df_renda.iloc[:,3:].describe(), use_container_width = True)
                    df_csv = convert_df(df_renda.iloc[:,3:].describe())
                    st.download_button(label='📥 Download tabela descritiva em CSV', data=df_csv, file_name= 'bank_filtered.csv')
                    st.markdown("---")
                    
                    var_quant = st.radio('Escolha a variável:', options = list_quantitativas, horizontal = True)
                    plot_var_quant(var_quant,df_renda)
                                        
                    
                    

          elif graph_type == 'Variáveis Qualitativas':
                    
                    st.write('## Análise - Variáveis Qualitativas')
                    var_quali = st.radio('Escolha a variável:', list_qualitativas, horizontal = True)
                    plot_var_quali(var_quali,df_renda)
                    filename = var_quali + '.png'

          elif graph_type == 'Bivariada':
                    
                    list_sem_renda = list_vars_todas[:4] + list_vars_todas[5:]
                    var_biv = st.radio('Escolha a variável:', list_sem_renda, horizontal = True)
                    plot_biv(var_biv,df_renda)
                    filename = var_biv + '.png'
          
          elif graph_type == 'Análise Temporal':
                   var_tempo_qual = st.radio('Escolha a variável:', list_qualitativas, horizontal = True)
                   st.write('## Análise das amostras ao longo do tempo - ' + var_tempo_qual) 
                   var_ = dict_vars[var_tempo_qual]
                   list_options = list(df_renda[var_].unique())
                   list_options.append('tudo')
                   categ_selec = st.multiselect('Escolha a categoria:', list_options,['tudo'])
                   df_filtrado = filtra_por_categorias(df_renda, var_, categ_selec)
                   if len(categ_selec) != 0 : plot_tempo(var_tempo_qual,df_filtrado)
                               
          
          st.download_button(label= '📥 Download do  Gráfico', data=open('output/graph.png', 'rb').read(),file_name='output/graph.png', mime='image/png')           
          
    else :
          st.write('## Faça Upload dos dados dos clientes')


main()








