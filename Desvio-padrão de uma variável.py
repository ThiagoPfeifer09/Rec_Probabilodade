import math

notas = [6, 7, 8, 10, 6, 5, 9, 7, 8, 6]
n = len(notas)

# Cálculo da média
soma = sum(notas)
media = soma / n

# Cálculo da variância
variancia = sum((nota - media) ** 2 for nota in notas) / n

# Cálculo do desvio padrão
desvio_padrao = math.sqrt(variancia)

print(f"O desvio padrão das notas é: {desvio_padrao:.2f}")
