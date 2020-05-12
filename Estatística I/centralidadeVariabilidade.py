import numpy as np
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000,
             140000, 300000, 40000, 800000]

media = np.mean(jogadores)
mediana = np.median(jogadores)

quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])

desvioPadrao = np.std(jogadores, ddof = 1)

#resumo das medidas de centralidade e variabilidade
stats.describe(jogadores)

