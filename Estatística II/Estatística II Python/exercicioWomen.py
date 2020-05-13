import pandas as pd
from sklearn.linear_model import LinearRegression

base = pd.read_csv("women.csv")
base = base.drop(["Unnamed: 0"], axis = 1)

x = base.iloc[:, 0].values
x = x.reshape(-1, 1)
y = base.iloc[:, 1].values

modelo = LinearRegression()
modelo.fit(x, y)

m = modelo.coef_
b = modelo.intercept_

ph_70 = 70 * m + b


