import matplotlib.pyplot as plt
import networkx as nx

# Dados do problema
total_violao = 30
total_cantar = 20
violao_e_cantar = 10

# Calculando as respostas do exercício
apenas_violao = total_violao - violao_e_cantar  # Apenas sabem tocar violão
apenas_cantar = total_cantar - violao_e_cantar  # Apenas sabem cantar

# Diagrama de Árvore para ilustrar a estrutura de habilidades
# Criando o grafo
G = nx.Graph()

# Adicionando os nós e arestas
G.add_edges_from([
    ("Pessoas", "Tocam Violão"),
    ("Pessoas", "Cantam"),
    ("Tocam Violão", "Apenas Violão"),
    ("Tocam Violão", "Violão e Cantar"),
    ("Cantam", "Apenas Cantar"),
    ("Cantam", "Violão e Cantar"),
])

# Adicionando quantidades aos nós
node_labels = {
    "Apenas Violão": apenas_violao,
    "Apenas Cantar": apenas_cantar,
    "Violão e Cantar": violao_e_cantar,
}

# Desenhando o diagrama de árvore
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightgreen", font_size=10, font_weight="bold", edge_color="gray")
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color="red")
plt.title("Diagrama de Árvore das Habilidades")
plt.show()
