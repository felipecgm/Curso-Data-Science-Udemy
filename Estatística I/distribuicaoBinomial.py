from scipy.stats import binom

#jogar moeda 5x, obter cara 3x

prob = binom.pmf(3, 5, 0.5)

"""
Passar por 4 sinais de 4 tempos, qual a probabilidade
de pegar sinal verde: nenhum, 1, 2, 3, 4 vezes seguidas
"""

vetorProb = []

for i in range(5):
    vetorProb.append(binom.pmf(i, 4, 0.25))
    
#cumulativa

cumulativa = binom.cdf(4, 4, 0.25)
 
    
    