def teorema_de_bayes():
    print("Calcule a probabilidade de um evento (A) dado que outro evento (B) ocorreu, usando o Teorema de Bayes.")

    # Entrada dos dados
    p_a = float(input("Digite a probabilidade a priori de A (P(A)): "))  # Probabilidade de A
    p_na = 1 - p_a  # Probabilidade de não A

    p_b_dado_a = float(input("Digite a probabilidade de B dado A (P(B|A)): "))  # Probabilidade de B dado A
    p_b_dado_na = float(input("Digite a probabilidade de B dado não A (P(B|¬A)): "))  # Probabilidade de B dado não A

    # Calculo de P(B)
    p_b = p_b_dado_a * p_a + p_b_dado_na * p_na

    # Cálculo de P(A|B) usando o Teorema de Bayes
    p_a_dado_b = (p_b_dado_a * p_a) / p_b

    # Exibir o resultado
    print(f"\nA probabilidade de A dado que B ocorreu (P(A|B)) é: {p_a_dado_b:.2%}")

# Chamada da função
teorema_de_bayes()
