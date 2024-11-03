import math

# Definindo os parâmetros do problema
lambd = 5   # média de chamadas por minuto
k = 3       # número exato de chamadas que queremos calcular

# Função para calcular a probabilidade usando a distribuição de Poisson
def poisson_probability(lambd, k):
    probability = (lambd ** k) * math.exp(-lambd) / math.factorial(k)
    return probability

# Calculando a probabilidade de exatamente 3 chamadas em um minuto
probabilidade = poisson_probability(lambd, k)
print(f"A probabilidade de que o centro receba exatamente 3 chamadas em um minuto é {probabilidade:.4f}")
