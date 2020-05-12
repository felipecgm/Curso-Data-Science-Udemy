mean(AirPassengers)
sd(AirPassengers)

mean(window(AirPassengers, start = c(1960,1), end = c(1960,12)))

install.packages("forecast")
library(forecast)

mediamovel = ma(AirPassengers, order = 12)
mediamovel
previsao = forecast(mediamovel, h = 12)
previsao
plot(previsao)

arrima = auto.arima(AirPassengers)

previsao_2 = forecast(arrima, h = 12)
plot(previsao_2)
