def calcular_probabilidade_marginal():
    # Solicitar o número total de casos
    total = int(input("Digite o número total de casos: "))

    # Solicitar as categorias de eventos e suas frequências
    eventos = {}
    print("Para cada categoria de evento, insira o nome e a quantidade de casos. Digite 'fim' para encerrar.")

    while True:
        nome_evento = input("Nome do evento (ou 'fim' para finalizar): ")
        if nome_evento.lower() == "fim":
            break
        qtd_evento = int(input(f"Quantidade de casos para {nome_evento}: "))
        eventos[nome_evento] = qtd_evento

    # Calcular a probabilidade marginal para cada evento
    probabilidades = {evento: qtd / total for evento, qtd in eventos.items()}

    # Exibir as probabilidades marginais
    print("\nProbabilidades marginais:")
    for evento, probabilidade in probabilidades.items():
        print(f"Probabilidade de {evento}: {probabilidade:.2%}")

# Chamada da função
calcular_probabilidade_marginal()
