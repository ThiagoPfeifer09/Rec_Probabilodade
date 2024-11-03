import math

# Função para calcular a probabilidade binomial, média e desvio-padrão
def distribuicao_binomial_com_media_desvio(n, k, p):
    # Cálculo da probabilidade binomial
    coeficiente_binomial = math.comb(n, k)
    probabilidade = coeficiente_binomial * (p ** k) * ((1 - p) ** (n - k))

    # Cálculo da média e desvio-padrão
    media = n * p
    desvio_padrao = math.sqrt(n * p * (1 - p))

    return probabilidade, media, desvio_padrao

# Exemplo do problema
n = 50  # número de parafusos
k = 45  # número de sucessos (parafusos sem defeito)
p = 0.9 # probabilidade de sucesso (parafuso sem defeito)

# Calculando a probabilidade, média e desvio-padrão
probabilidade, media, desvio_padrao = distribuicao_binomial_com_media_desvio(n, k, p)
print(f"A probabilidade de obter exatamente {k} parafusos sem defeito é {probabilidade:.4f}")
print(f"Média da distribuição: {media:.2f}")
print(f"Desvio-padrão da distribuição: {desvio_padrao:.2f}")