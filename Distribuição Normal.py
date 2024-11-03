from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da distribuição normal
mu = 170       # média
sigma = 10     # desvio padrão

# Alturas que queremos calcular a probabilidade entre
lower_bound = 160
upper_bound = 180

# Calculando a probabilidade entre 160 e 180 cm
probabilidade = norm.cdf(upper_bound, mu, sigma) - norm.cdf(lower_bound, mu, sigma)
print(f"A probabilidade de uma pessoa ter altura entre 160 cm e 180 cm é {probabilidade:.4f}")

# Gerando dados para o gráfico da distribuição normal
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Distribuição Normal", color='blue')
plt.fill_between(x, y, where=(x >= lower_bound) & (x <= upper_bound), color='skyblue', alpha=0.5)
plt.xlabel("Altura (cm)")
plt.ylabel("Densidade de Probabilidade")
plt.title("Distribuição Normal de Alturas em uma População de Adultos")
plt.legend()
plt.grid(True)
plt.show()
