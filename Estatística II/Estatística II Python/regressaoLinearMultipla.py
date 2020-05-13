import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf

base = pd.read_csv("mt_cars.csv")
base = base.drop(["Unnamed: 0"], axis = 1)

#Regressao Linear Simples

x = base.iloc[:, 2].values
#reshape (-1: não vou mexer nas linhas, 1: adicionar uma coluna)
x_rs = x.reshape(-1, 1)
y = base.iloc[:, 0].values

#verificando a correlacao
correlacao = np.corrcoef(x, y)

#criando o modelo

modeloSimples = LinearRegression()
modeloSimples.fit(x_rs, y)

b_simples = modeloSimples.intercept_
a_simples = modeloSimples.coef_

#R² >> score
r2_simples = modeloSimples.score(x_rs, y)
previsoes = modeloSimples.predict(x_rs)

modeloSimplesAjustado = smf.ols(formula = 'mpg ~ disp', data = base)
modeloSimplesAjustadoTreinado = modeloSimplesAjustado.fit()
resumoSimples = modeloSimplesAjustadoTreinado.summary()

plt.scatter(x_rs, y)
plt.plot(x_rs, previsoes, color = "red")

#Regressão linear multipla

x1 = base.iloc[:, 1:4].values
#reshape (-1: não vou mexer nas linhas, 1: adicionar uma coluna)
#x_rs_1 = x1.reshape(-1, 1)
y1 = base.iloc[:, 0].values

#verificando a correlacao
#correlacao = np.corrcoef(x1, y1)

#criando o modelo

modeloMultiplo = LinearRegression()
modeloMultiplo.fit(x1, y1)
r2_multiplo = modeloMultiplo.score(x1, y1)

modeloMultiploAjustado = smf.ols(formula = 'mpg ~ cyl + disp + hp', data = base)
modeloMultiploAjustadoTreinado = modeloMultiploAjustado.fit()
resumoMultiplo = modeloMultiploAjustadoTreinado.summary()

novo = np.array([4, 200, 100])
novo = novo.reshape(1 , -1)

previsao = modeloMultiplo.predict(novo)












