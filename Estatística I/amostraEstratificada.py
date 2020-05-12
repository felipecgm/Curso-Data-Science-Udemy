import pandas as pd
from sklearn.model_selection import train_test_split

#train_test_split é uma função que divide a base de dados
#sklearn é uma biblioteca para aprendizado de máquina

iris = pd.read_csv('iris.csv')

iris['Species'].value_counts()

x, _, y, _ = train_test_split(iris.iloc[:, 0:5], iris.iloc[:, 5], 
                              test_size = 0.5, stratify = iris.iloc[:, 5])

#iris.iloc[:, 0:5] retorna 5 colunas (coluna 0 até 4), sem contar o índice
#iris.iloc[:, 5] retorna a 5 coluna
#test_size = função que retorna a quantidade complementar da população
#strafify = retorna o estrato
#y.value_counts() retorna a qtde de cada estrato

infert = pd.read_csv('infert.csv')

#infert['education'].value_counts()

infert['education'].value_counts()

education = pd.Series(infert.iloc[:, 1])

frequencia = infert['education'].value_counts()

"""
x, _, y, _ = o caractere _ é utilizado para trazer apenas a amostra da base de dados. 
Por exemplo, a amostra iris tem 150 valores. Quis apenas 50% (test_size = 0.5) = 75 valores.
Em x foi criado um dataframe com 5 colunas e 75 linhas e em y foi criada uma série com 1 coluna e 75 linhas.
train_test_split(x = iris.iloc[:, 0:5], y = iris.iloc[:, 5])
"""

x1, _, y1, _ = train_test_split(infert.iloc[:, 2: 9], infert.iloc[:, 1],
                                test_size = 0.6, stratify = infert.iloc[:, 1])

frequencia_amostra = y1.value_counts()

"""
x1, _, y1, _ = (x1 = dataframe com 99 valores da colunas 2 até 9 (não inclui o 9), y1 = série com 99 valores
da coluna 1, test_size*, estratificar a coluna 1)
*Quero uma amostra com 100 elementos. Preciso usar a porcentagem complementar:
    1 - 100/248 = 0.6 aproximadamente. 1 - qtde_amostra / total_população.
"""


