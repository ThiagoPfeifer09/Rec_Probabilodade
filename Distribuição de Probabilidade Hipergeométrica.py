import math

# Função para calcular a probabilidade hipergeométrica
def probabilidade_hipergeometrica(N, K, n, k):
    # Cálculo da probabilidade hipergeométrica
    parte1 = math.comb(K, k)          # Combinações de sucessos (bolas vermelhas)
    parte2 = math.comb(N - K, n - k)  # Combinações de fracassos (bolas azuis)
    total_combinacoes = math.comb(N, n)  # Total de combinações possíveis

    probabilidade = (parte1 * parte2) / total_combinacoes
    return probabilidade

# Exemplo do problema
N = 30  # total de bolas
K = 10  # bolas vermelhas
n = 5   # bolas retiradas
k = 2   # bolas vermelhas desejadas

# Calculando a probabilidade
resultado = probabilidade_hipergeometrica(N, K, n, k)
print(f"A probabilidade de retirar exatamente {k} bolas vermelhas é {resultado:.4f}")