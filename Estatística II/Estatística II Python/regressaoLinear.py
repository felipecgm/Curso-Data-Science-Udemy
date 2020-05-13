import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

carros = pd.read_csv("cars.csv")

#deletar uma coluna
carros = carros.drop(["Unnamed: 0"], axis = 1)

#verificar se existe uma correlação

#criam-se dois vetores, x e y. Col 1: dist, col 0: speed
x = carros.iloc[:, 1].values
x_reshape = x.reshape(-1, 1)
y = carros.iloc[:, 0].values

#verificando a correlação
correlacao = np.corrcoef(x, y)

#0,86 >> correlacao forte. Pode fazer a regressao linear

#criando o modelo
modelo = LinearRegression()
modelo.fit(x_reshape, y)

#y  = ax + b
b = modelo.intercept_
a = modelo.coef_

#gráfico de dispersão
plt.scatter(x_reshape, y)

#criando a reta da regressão linear
plt.plot(x_reshape, modelo.predict(x_reshape), color = "red")

#previsão da velocidade, sendo a distancia 22 pés

vel22 = b + a * 22
#ou modelo.predict(22)

residuais = modelo._residues

visualizador = ResidualsPlot(modelo)
c = visualizador.fit(x_reshape, y)
d = visualizador.poof()





