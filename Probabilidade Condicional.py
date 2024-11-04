def calcular_probabilidade_condicional():
    # Solicitar o número total de casos
    total = int(input("Digite o número total de casos: "))

    # Solicitar as categorias de eventos e suas frequências
    eventos = {}
    print("Para cada evento, insira o nome e a quantidade de casos. Digite 'fim' para encerrar.")

    while True:
        nome_evento = input("Nome do evento (ou 'fim' para finalizar): ")
        if nome_evento.lower() == "fim":
            break
        qtd_evento = int(input(f"Quantidade de casos para {nome_evento}: "))
        eventos[nome_evento] = qtd_evento

    # Solicitar pares de eventos para calcular probabilidade condicional
    probabilidades_condicionais = {}
    print("\nAgora, insira pares de eventos para calcular a probabilidade condicional P(A|B).")
    print("Para cada par, insira o número de casos onde ambos os eventos ocorrem. Digite 'fim' para encerrar.")

    while True:
        evento_a = input("Evento A (ou 'fim' para finalizar): ")
        if evento_a.lower() == "fim":
            break
        evento_b = input("Evento B: ")

        # Verificar se ambos os eventos existem nos dados fornecidos
        if evento_a in eventos and evento_b in eventos:
            qtd_conjunta = int(input(f"Quantidade de casos em que {evento_a} e {evento_b} ocorrem simultaneamente: "))

            # Calcular a probabilidade condicional P(A|B) = P(A e B) / P(B)
            probabilidade_b = eventos[evento_b] / total
            probabilidade_condicional = qtd_conjunta / total / probabilidade_b
            probabilidades_condicionais[f"P({evento_a}|{evento_b})"] = probabilidade_condicional
        else:
            print("Um ou ambos os eventos não foram definidos. Tente novamente.")

    # Exibir as probabilidades condicionais
    print("\nProbabilidades condicionais:")
    for condicao, probabilidade in probabilidades_condicionais.items():
        print(f"{condicao} = {probabilidade:.2%}")

# Chamada da função
calcular_probabilidade_condicional()
