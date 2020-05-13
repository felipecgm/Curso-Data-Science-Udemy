import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

base = pd.read_csv("Eleicao.csv", sep = ";")
plt.scatter(base.DESPESAS, base.SITUACAO)

#base.describe() - fornece resumo estatístico descritivo

correlacao = np.corrcoef(base.DESPESAS, base.SITUACAO)

x = base.iloc[:, 2].values
x1 = x[:, np.newaxis]
y = base.iloc[:, 1].values

modelo = LogisticRegression()
modelo.fit(x1, y)

plt.scatter(x1, y)

#linspace gera números aleatórios. (min, max, qtde)
x1_teste = np.linspace(10, 3000, 100)

def model(x):
    return 1/(1 + np.exp(-x))

#erro
result = model(x1_teste * modelo.coef_ + modelo.intercept_).ravel()
plt.plot(x1_teste, result, color = "red")

base_previsoes = pd.read_csv("NovosCandidatos.csv", sep = ";")

despesas = base_previsoes.iloc[:, 1].values

despesas = despesas.reshape(-1, 1)

previsoes_teste = modelo.predict(despesas)

#concatena os valores
base_previsoes = np.colum_stack((base_previsoes, previsoes_teste))



