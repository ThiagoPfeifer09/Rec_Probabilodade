# Função para calcular a probabilidade em uma distribuição uniforme
def probabilidade_uniforme(a, b, x1, x2):
    if x1 < a or x2 > b:
        return 0  # fora do intervalo
    return (x2 - x1) / (b - a)

# Exemplo do problema
a = 10  # início do intervalo
b = 20  # fim do intervalo
x1 = 12 # tempo mínimo
x2 = 18 # tempo máximo

# Calculando a probabilidade
resultado = probabilidade_uniforme(a, b, x1, x2)
print(f"A probabilidade de o ônibus chegar entre {x1} e {x2} minutos é {resultado:.4f}")