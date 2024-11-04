# Definindo o número total de lados do dado
num_lados = 10

# Definindo os resultados que correspondem ao evento A (maior que 7)
event_A_outcomes = [8, 9, 10]  # Números maiores que 7

# Calculando a probabilidade do evento A
prob_evento_A = len(event_A_outcomes) / num_lados

# Calculando a probabilidade do evento complementar A' (menor ou igual a 7)
prob_evento_A_complementar = 1 - prob_evento_A

# Exibindo os resultados
prob_evento_A, prob_evento_A_complementar, prob_evento_A + prob_evento_A_complementar
