import random

num_lancamentos = 1000000
face_desejada = 3
contagem_face = 0

# Simula os lançamentos do dado
for _ in range(num_lancamentos):
    resultado = random.randint(1, 6)  # Gera um número entre 1 e 6
    if resultado == face_desejada:
        contagem_face += 1

# Calcula e exibe a probabilidade
probabilidade = (contagem_face / num_lancamentos) * 100
print(f"A probabilidade de sair a face {face_desejada} é aproximadamente {probabilidade:.2f}%")
