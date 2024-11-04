import random

def cara_ou_coroa()
    return random.choice([Cara, Coroa])

# Inicializando contadores
cara_count = 0
coroa_count = 0

# Simulando 100 jogadas
for _ in range(1000)
    resultado = cara_ou_coroa()
    if resultado == Cara
        cara_count += 1
    else
        coroa_count += 1

# Imprimindo os resultados
print(Resultados após 100 jogadas)
print(Cara, cara_count)
print(Coroa, coroa_count)

# Verificando se deu o mesmo número de caras e coroas
if cara_count == coroa_count
    print(Ambos Cara e Coroa caíram o mesmo número de vezes!)
else
    print(Não deu ambos.)
