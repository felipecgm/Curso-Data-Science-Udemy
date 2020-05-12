#nome das colunas do cj de dados mtcars
colnames(mtcars)
#32 veículos com 11 características
dim(mtcars)
#correlação dos valores das colunas 1: mpg, 2: cyl, 3: disp, 4: hp
cor(mtcars[1:4])

#mpg vai ser a variável de resposta

modelo = lm(mpg ~ disp, data=mtcars)
summary(modelo)$r.squared
summary(modelo)$adj.r.squared
plot(mpg ~ disp, data=mtcars)
abline(modelo)
predict(modelo, data.frame(disp=200))

#acima, regressão linear simples

#abaixo, regressão linear múltipla

modelo = lm(mpg ~ disp + hp + cyl, data=mtcars)

summary(modelo)$r.squared
summary(modelo)$adj.r.squared

predict(modelo, data.frame(disp=200, hp=100, cyl=4))
