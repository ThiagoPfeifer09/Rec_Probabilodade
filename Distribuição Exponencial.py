import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
lambd = 1 / 15    # taxa média de chegada do ônibus por minuto
x = 10            # tempo máximo de espera em minutos

# Calculando a probabilidade de esperar menos de 10 minutos
probabilidade = 1 - np.exp(-lambd * x)
print(f"A probabilidade de esperar menos de 10 minutos pelo próximo ônibus é {probabilidade:.4f}")

# Gerando dados para o gráfico da distribuição exponencial
x_values = np.linspace(0, 60, 500)  # intervalo de 0 a 60 minutos
y_values = 1 - np.exp(-lambd * x_values)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="CDF da Distribuição Exponencial", color='blue')
plt.fill_between(x_values, y_values, where=(x_values <= x), color='skyblue', alpha=0.5)
plt.xlabel("Tempo de Espera (minutos)")
plt.ylabel("Probabilidade Acumulada")
plt.title("Distribuição Exponencial: Tempo de Espera pelo Próximo Ônibus")
plt.legend()
plt.grid(True)
plt.show()
