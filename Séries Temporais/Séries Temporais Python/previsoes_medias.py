import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose

base = pd.read_csv("AirPassengers.csv")

dateparse = lambda dates: pd.datetime.strptime(dates, "%Y-%m")

base = pd.read_csv("AirPassengers.csv", parse_dates= ["Month"],
                   index_col = "Month", date_parser = dateparse)

ts = base['#Passengers']

media = ts.mean()

media_1960 = ts["1960-01-01" : "1960-12-01"].mean()

media_movel = ts.rolling(window = 12).mean()

#ts[0:12].mean()

plt.figure(0)
plt.plot(ts)
plt.plot(media_movel, color = "red")

previsoes = []

for i in range(1, 13):
    superior = len(media_movel) - i
    inferior = superior - 11
    previsoes.append(media_movel[inferior:superior].mean())

previsoes = previsoes[: : -1]

plt.figure(1)
plt.plot(previsoes)

