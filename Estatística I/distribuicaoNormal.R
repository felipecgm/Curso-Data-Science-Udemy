#Calculo da distribuição normal
#qnorm(valor procurado, mean, standard deviation)

#1º exemplo: mean = 8, sd = 2, x < 6

x1 = pnorm(6,8,2)

#2º exemplo: mean = 8, sd = 2, x > 6

x2 = pnorm(6,8,2, lower.tail = F)

#ou 1 - pnorm(6,8,2)

#3º exemplo: mean = 8, sd = 2, x  < 6 ou x > 10

x3 = pnorm(6,8,2) + pnorm(10,8,2, lower.tail = F)

#4º exemplo: mean = 8, sd = 2, x  < 10 ou x > 8

X4 = pnorm(10,8,2) - pnorm(8,8,2)

#teste para verificar se é normal

#gerar numeros distribuidos normalmente

x5 = rnorm(100)

#gerar grafico de probabilidade normal

qqnorm(x5)
qqline(x5)

shapiro.test(x5)

