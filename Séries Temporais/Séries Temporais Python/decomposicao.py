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

decomposicao = seasonal_decompose(ts)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
aleatorio = decomposicao.resid

plt.figure(0)
plt.plot(ts)

plt.figure(1)
plt.plot(tendencia)

plt.figure(2)
plt.plot(sazonal)

plt.figure(3)
plt.plot(aleatorio)

plt.figure(4)
plt.subplot(4,1,1)
plt.plot(ts, label = "Original")
plt.legend(loc = "best")

plt.subplot(4,1,2)
plt.plot(tendencia, label = "Tendência")
plt.legend(loc = "best")

plt.subplot(4,1,3)
plt.plot(sazonal, label = "Sazonalidade")
plt.legend(loc = "best")

plt.subplot(4,1,4)
plt.plot(aleatorio, label = "Aleatório")
plt.legend(loc = "best")
plt.tight_layout()
