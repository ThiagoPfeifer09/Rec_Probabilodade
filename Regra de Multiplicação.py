import random

# Parâmetros do problema
total_camisetas = 40
camisetas_defeituosas = 5
camisetas_boas = total_camisetas - camisetas_defeituosas
num_simulacoes = 1000000
sucesso = 0

# Simula as escolhas de camisetas
for _ in range(num_simulacoes):
    # Escolhe a primeira camiseta
    primeira_camiseta = random.randint(0, total_camisetas - 1)

    # Verifica se a primeira camiseta é boa
    if primeira_camiseta < camisetas_boas:
        # Reduz o número de camisetas boas e o total de camisetas
        camisetas_boas_restantes = camisetas_boas - 1
        total_camisetas_restantes = total_camisetas - 1

        # Escolhe a segunda camiseta
        segunda_camiseta = random.randint(0, total_camisetas_restantes - 1)

        # Verifica se a segunda camiseta também é boa
        if segunda_camiseta < camisetas_boas_restantes:
            sucesso += 1

# Calcula e exibe a probabilidade
probabilidade = (sucesso / num_simulacoes) * 100
print(f"A probabilidade de escolher duas camisetas sem defeito é aproximadamente {probabilidade:.2f}%")


