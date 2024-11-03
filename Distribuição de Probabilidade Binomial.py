import math

# Função para calcular a probabilidade binomial
def probabilidade_binomial(n, k, p):
    # Cálculo do coeficiente binomial
    coeficiente_binomial = math.comb(n, k)
    # Cálculo da probabilidade
    probabilidade = coeficiente_binomial * (p ** k) * ((1 - p) ** (n - k))
    return probabilidade

# Exemplo do problema
n = 10  # número de lançamentos
k = 6   # número de sucessos (caras)
p = 0.5 # probabilidade de sucesso (cara)

# Calculando a probabilidade
resultado = probabilidade_binomial(n, k, p)
print(f"A probabilidade de obter exatamente {k} caras em {n} lançamentos é {resultado:.4f}")