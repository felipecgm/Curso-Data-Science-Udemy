from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

#Calculo da distribuição normal
#qnorm(valor procurado, mean, standard deviation)

#1º exemplo: mean = 8, sd = 2, x < 6

p1 = norm.cdf(6, 8, 2)

#2º exemplo: mean = 8, sd = 2, x > 6

p2 = norm.sf(6, 8, 2)

#3º exemplo: mean = 8, sd = 2, x  < 6 ou x > 10

p3 = norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

#4º exemplo: mean = 8, sd = 2, x  < 10 ou x > 8

p4 = norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)

#teste para verificar se é normal

#gerar numeros distribuidos normalmente

dados = norm.rvs(size = 100)        
stats.probplot(dados, plot = plt)

shapiro = stats.shapiro(dados)



