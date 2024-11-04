from scipy.stats import norm

def fdp_normal():
    print("Cálculo da probabilidade para um intervalo de uma variável com distribuição normal.")

    # Solicitar ao usuário a média e o desvio padrão
    mu = float(input("Digite a média (µ): "))
    sigma = float(input("Digite o desvio padrão (σ): "))

    # Solicitar ao usuário os limites do intervalo
    a = float(input("Digite o limite inferior do intervalo (a): "))
    b = float(input("Digite o limite superior do intervalo (b): "))

    # Calcular a probabilidade acumulada entre a e b usando a CDF da normal
    probabilidade = norm.cdf(b, mu, sigma) - norm.cdf(a, mu, sigma)

    # Exibir o resultado
    print(f"\nA probabilidade de que a variável esteja entre {a} e {b} é: {probabilidade:.2%}")

# Chamada da função
fdp_normal()
