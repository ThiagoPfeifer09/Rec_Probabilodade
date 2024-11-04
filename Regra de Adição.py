# Parâmetros do problema
num_ases = 4
num_reis = 4
num_total_cartas = 52
num_ases_ou_reis = num_ases + num_reis

# Calcula a probabilidade
probabilidade = num_ases_ou_reis / num_total_cartas

# Exibe o resultado
print(f"A probabilidade de tirar um Ás ou um Rei é de {probabilidade * 100:.2f}%")
