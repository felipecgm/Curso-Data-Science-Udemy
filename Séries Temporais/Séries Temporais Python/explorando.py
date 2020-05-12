import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

base = pd.read_csv("AirPassengers.csv")

dateparse = lambda dates: pd.datetime.strptime(dates, "%Y-%m")

base = pd.read_csv("AirPassengers.csv", parse_dates= ["Month"],
                   index_col = "Month", date_parser = dateparse)

ts = base['#Passengers']

plt.figure(0)
plt.plot(ts)

ts_ano = ts.resample('A').sum()

plt.figure(1)
plt.plot(ts_ano)

ts_mes = ts.groupby([lambda x: x.month]).sum()

plt.figure(2)
plt.plot(ts_mes)

ts_datas = ts["1960-01-01" : "1960-12-01"]

plt.figure(3)
plt.plot(ts_datas)

