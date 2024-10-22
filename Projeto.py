import pandas as pd
import matplotlib.pyplot as plt

# Função para ler e transformar os dados do arquivo Excel
def transformar_dados(arquivo_excel):
    # Lê a planilha Excel, definindo a linha 1 (índice 0) como cabeçalho
    df = pd.read_excel(arquivo_excel, header=1)

    # Exibe as primeiras linhas do dataframe original
    print("Dados originais:")
    print(df.head())

    # Remover espaços e caracteres de nova linha dos nomes das colunas
    df.columns = df.columns.str.strip().str.replace('\n', ' ')

    # Exibe os nomes reais das colunas após a limpeza
    print("\nNomes das colunas após a limpeza:")
    print(df.columns.tolist())

    # Exibe todas as colunas que foram carregadas
    print("\nTodas as colunas disponíveis:")
    print(df.columns)

    # Selecionar apenas as colunas relevantes
    colunas_relevantes = ['Unnamed: 2', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7']
    
    # Seleciona as colunas relevantes e renomeia-as
    df = df[colunas_relevantes]
    
    # Renomeando as colunas
    df.columns = ['Item', 'Quantidade', 'Preço por unidade', 'Preço total', 'Local']

    # Remove linhas que contêm texto nas colunas numéricas
    df = df[pd.to_numeric(df['Preço total'], errors='coerce').notnull()]

    # Converte a coluna 'Preço total' para numérico
    df['Preço total'] = pd.to_numeric(df['Preço total'], errors='coerce')

    # Exibe os dados com as colunas renomeadas
    print("\nDados com colunas renomeadas e limpas:")
    print(df.head())

    # Agrupa os dados pela coluna 'Local' e soma os valores da coluna 'Preço total'
    dados_transformados = df.groupby('Local')['Preço total'].sum().reset_index()

    # Exibe os dados transformados
    print("\nDados transformados:")
    print(dados_transformados)

    return dados_transformados

def plotar_grafico(dados_transformados):
    plt.figure(figsize=(10, 6)) # Define o tamanho da figura do gráfico

    # Cria o gráfico de barras com o total de preços por local
    plt.bar(dados_transformados['Local'], dados_transformados['Preço total'], color='skyblue')

    # Adiciona título e rótulos aos eixos
    plt.title('Valores por Local')
    plt.xlabel('Local')
    plt.ylabel('Preço total')
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo X para melhor visualização
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição
    plt.show() # Exibe o gráfico

# Caminho para o arquivo Excel
arquivo_excel = 'C:/Users/alana/Downloads/Book.xlsx'

# Se os dados foram transformados corretamente, plota o gráfico
dados = transformar_dados(arquivo_excel)
if dados is not None:
    plotar_grafico(dados)
