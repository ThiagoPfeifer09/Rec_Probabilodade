import math

# Definindo os parâmetros do problema
n = 50      # número total de consoles no lote
p = 0.1     # probabilidade de um console ser defeituoso
k = 3       # número de consoles defeituosos para o qual queremos calcular a probabilidade

# Função para calcular a probabilidade binomial
def binomial_probability(n, k, p):
    comb = math.comb(n, k)                # Cálculo da combinação C(n, k)
    probability = comb * (p ** k) * ((1 - p) ** (n - k))  # Aplicando a fórmula da distribuição binomial
    return probability

# Calculando a probabilidade de exatamente 3 consoles serem defeituosos
probabilidade = binomial_probability(n, k, p)
print(f"A probabilidade de exatamente 3 consoles serem defeituosos em um lote de 50 é {probabilidade:.4f}")
