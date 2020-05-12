modelo = lm(speed ~ dist, data=cars)

plot(modelo)

plot(speed ~ dist, data=cars)

abline(modelo)
modelo$coefficients

modelo$coefficients[1] + modelo$coefficients[2] * 22

predict(modelo, data.frame(dist=22))

summary(modelo)

modelo$residuals

carros = cars

modelo$fitted.values

plot(modelo$fitted.values, cars$dist)
