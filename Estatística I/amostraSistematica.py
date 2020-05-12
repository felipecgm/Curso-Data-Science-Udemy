import numpy as np
import pandas as pd
from math import ceil

#quero uma amostra com 10% da população
populacao = 150
amostra = 15

#arredonda para o maior inteiro
k = ceil(populacao / amostra)
np.random.seed(23)

#aleatoriedade
r = np.random.randint(1, k + 1, 1)

acumulador = r[0]

sorteados = []

for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k

#associar o índice da lista sorteados aos índices da base iris

base = pd.read_csv('iris.csv')
    
base_final = base.loc[sorteados]


