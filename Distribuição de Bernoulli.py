def distribuicao_bernoulli():
    print("Cálculo da probabilidade para uma Distribuição de Bernoulli.")

    # Solicitar ao usuário a probabilidade de sucesso
    p = float(input("Digite a probabilidade de sucesso (p) entre 0 e 1: "))

    # Validar se a probabilidade está entre 0 e 1
    if p < 0 or p > 1:
        print("A probabilidade deve estar entre 0 e 1.")
        return

    # Solicitar ao usuário o valor de x (0 para fracasso, 1 para sucesso)
    x = int(input("Digite o valor de x (0 para fracasso, 1 para sucesso): "))

    # Calcular a probabilidade usando a fórmula da distribuição de Bernoulli
    if x == 1:
        probabilidade = p
    elif x == 0:
        probabilidade = 1 - p
    else:
        print("O valor de x deve ser 0 ou 1.")
        return

    # Exibir o resultado
    print(f"\nA probabilidade de que X = {x} é: {probabilidade:.2%}")

# Chamada da função
distribuicao_bernoulli()
