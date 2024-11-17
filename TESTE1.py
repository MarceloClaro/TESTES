import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar dados
def load_data(file):
    try:
        data = pd.read_csv(file)
        return data
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

# Função para plotar gráfico
def plot_graph(data, x_col, y_col):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data[x_col], data[y_col], marker='o')
        plt.title(f'{y_col} vs {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Erro ao plotar o gráfico: {e}")

# Título da aplicação
st.title('Análise de Dados Interativa com Streamlit')

# Upload de arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Carregar dados
    data = load_data(uploaded_file)
    
    if data is not None:
        # Exibir dados
        st.write("Visualização dos primeiros registros do arquivo:")
        st.dataframe(data.head())
        
        # Seleção das colunas para plotagem
        columns = data.columns.tolist()
        x_column = st.selectbox('Selecione a coluna para o eixo X', columns)
        y_column = st.selectbox('Selecione a coluna para o eixo Y', columns)
        
        # Plotar gráfico
        if st.button('Plotar Gráfico'):
            plot_graph(data, x_column, y_column)
