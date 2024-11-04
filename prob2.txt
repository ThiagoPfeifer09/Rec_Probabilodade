import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Dados do problema
total_violao = 30
total_cantar = 20
violao_e_cantar = 10

# Calculando as respostas do exercício
apenas_violao = total_violao - violao_e_cantar  # Apenas sabem tocar violão
apenas_cantar = total_cantar - violao_e_cantar  # Apenas sabem cantar

# Diagrama de Venn para ilustrar os conjuntos
plt.figure(figsize=(6, 6))
venn = venn2(subsets=(apenas_violao, apenas_cantar, violao_e_cantar), set_labels=('Tocam Violão', 'Cantam'))
plt.title("Diagrama de Venn das Habilidades")
plt.show()
