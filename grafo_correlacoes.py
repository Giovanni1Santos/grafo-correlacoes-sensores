# PROVA FINAL - Teoria dos Grafos
# Engenharia da Computação
# Docente: Florêncio Filho

# 1. Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from networkx.algorithms import tree
from networkx.drawing.nx_pylab import draw

# 2. Leitura do arquivo LM_Data.txt
arquivo = '/content/LM_data.txt'

# Lendo o arquivo usando pandas
dados = pd.read_csv(arquivo, sep=",", header=None)

# 3. Tratamento dos dados
# Eliminar a coluna do tempo (primeira coluna) e as colunas dos canais 27, 28, 29 e 30
dados_tratados = dados.drop(columns=[0, 27, 28, 29, 30])

# Atualizando os nomes das colunas para os canais 1 ao 26
dados_tratados.columns = [f'Canal {i}' for i in range(1, 27)]

# 4. Cálculo da matriz de correlação usando o coeficiente de Pearson
# Criando a matriz de adjacência (correlações)
n_canais = dados_tratados.shape[1]
matriz_correlacao = np.zeros((n_canais, n_canais))

for i in range(n_canais):
    for j in range(n_canais):
        if i != j:
            # Calcula a correlação entre as colunas i e j
            matriz_correlacao[i, j], _ = pearsonr(dados_tratados.iloc[:, i], dados_tratados.iloc[:, j])

# Exibindo a matriz de correlação
print("Matriz de Adjacência (Correlação de Pearson):")
print(pd.DataFrame(matriz_correlacao, columns=dados_tratados.columns, index=dados_tratados.columns))

# 5. Criação do grafo com base na matriz de correlação
# O grafo será gerado com todas as correlações
G = nx.Graph()

# Adiciona os vértices (nós)
for canal in dados_tratados.columns:
    G.add_node(canal)

# Adiciona as arestas (conexões) com pesos baseados na matriz de correlação
for i in range(n_canais):
    for j in range(i + 1, n_canais):  # Evita duplicar as conexões
        peso = matriz_correlacao[i, j]
        if peso > 0:  # Apenas conexões significativas
            G.add_edge(dados_tratados.columns[i], dados_tratados.columns[j], weight=peso)

# Desenhando o grafo com cores para as arestas e nós
plt.figure(figsize=(10, 8))
pos = nx.circular_layout(G)  # Layout do grafo

# Arestas coloridas conforme o peso
edges = G.edges(data=True)
weights = [edge[2]['weight'] for edge in edges]

# Mapeando cores para as arestas com base no peso
edge_colors = [plt.cm.Blues(weight) for weight in weights]

# Desenho do grafo
nx.draw(
    G, pos, with_labels=True, node_size=500, font_weight='bold',
    edge_color=weights, edge_cmap=plt.cm.Blues, width=2
)
plt.title("Grafo com todas as Correlações")
plt.show()

# 6. Grafo com correlações entre 0.0 e 0.5
G_05 = nx.Graph()
for i in range(n_canais):
    for j in range(i + 1, n_canais):
        peso = matriz_correlacao[i, j]
        if 0.0 <= peso <= 0.5:
            G_05.add_edge(dados_tratados.columns[i], dados_tratados.columns[j], weight=peso)

# Desenhando o grafo
plt.figure(figsize=(10, 8))
nx.draw(
    G_05, pos, with_labels=True, node_size=500, font_weight='bold',
    edge_color='orange', width=2
)
plt.title("Grafo com Correlações entre 0.0 e 0.5")
plt.show()

# 7. Grafo com correlações entre 0.51 e 1.0
G_1 = nx.Graph()
for i in range(n_canais):
    for j in range(i + 1, n_canais):
        peso = matriz_correlacao[i, j]
        if 0.51 <= peso <= 1.0:
            G_1.add_edge(dados_tratados.columns[i], dados_tratados.columns[j], weight=peso)

plt.figure(figsize=(10, 8))
nx.draw(
    G_1, pos, with_labels=True, node_size=500, font_weight='bold',
    edge_color='green', width=2
)
plt.title("Grafo com Correlações entre 0.51 e 1.0")
plt.show()

# 8. Algoritmo de Prim usando matriz de correlação
mst_prim = tree.minimum_spanning_tree(G, algorithm="prim")

plt.figure(figsize=(10, 8))
nx.draw(
    mst_prim, pos, with_labels=True, node_size=500, font_weight='bold',
    edge_color='purple', width=2
)
plt.title("Árvore Geradora Mínima - Algoritmo de Prim")
plt.show()

# 9. Algoritmo de Kruskal usando matriz de correlação
mst_kruskal = tree.minimum_spanning_tree(G, algorithm="kruskal")

plt.figure(figsize=(10, 8))
nx.draw(
    mst_kruskal, pos, with_labels=True, node_size=500, font_weight='bold',
    edge_color='red', width=2
)
plt.title("Árvore Geradora Mínima - Algoritmo de Kruskal")
plt.show()

# 10. Comparação lado a lado entre Prim e Kruskal
fig, axs = plt.subplots(1, 2, figsize=(15, 7))

plt.sca(axs[0])
nx.draw(
    mst_prim, pos, with_labels=True, node_size=500, font_weight='bold',
    edge_color='purple', width=2
)
plt.title("Algoritmo de Prim")

plt.sca(axs[1])
nx.draw(
    mst_kruskal, pos, with_labels=True, node_size=500, font_weight='bold',
    edge_color='red', width=2
)
plt.title("Algoritmo de Kruskal")

plt.show()

# Conclusão
print("""
Conclusão:
O algoritmo de Prim constrói a árvore de forma incremental, escolhendo as arestas de menor peso que não formem ciclos.
Já o algoritmo de Kruskal seleciona as arestas em ordem crescente de peso e conecta os componentes. Ambos têm o mesmo resultado,
mas o método de seleção e construção da árvore é diferente.
""")
