import numpy as np
import scipy.stats as stats

# Parâmetros da distribuição normal
mu = 170  # média
sigma = 10  # desvio padrão

# 1. Probabilidade de uma pessoa ter altura entre 160 cm e 180 cm
a = 160
b = 180
prob_160_180 = stats.norm.cdf(b, mu, sigma) - stats.norm.cdf(a, mu, sigma)

# 2. Altura correspondente ao percentil 90
percentil_90 = stats.norm.ppf(0.90, mu, sigma)

# 3. Probabilidade de uma pessoa ter altura superior a 185 cm
c = 185
prob_above_185 = 1 - stats.norm.cdf(c, mu, sigma)

prob_160_180, percentil_90, prob_above_185
