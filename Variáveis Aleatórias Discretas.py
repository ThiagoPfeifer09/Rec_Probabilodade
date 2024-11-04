# Definindo os valores possíveis de X e suas respectivas probabilidades
valores_X = [3, 4, 5, 6, 7, 8, 9]
probabilidades_X = [1/10, 1/10, 2/10, 2/10, 2/10, 1/10, 1/10]

# Calculando a esperança matemática E(X)
esperanca_X = sum(x * p for x, p in zip(valores_X, probabilidades_X))

# Calculando a probabilidade de X > 6
probabilidade_X_maior_6 = sum(p for x, p in zip(valores_X, probabilidades_X) if x > 6)

esperanca_X, probabilidade_X_maior_6
