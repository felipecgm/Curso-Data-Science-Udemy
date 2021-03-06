#Calculo da distribui��o normal
#qnorm(valor procurado, mean, standard deviation)

#1� exemplo: mean = 8, sd = 2, x < 6

x1 = pnorm(6,8,2)

#2� exemplo: mean = 8, sd = 2, x > 6

x2 = pnorm(6,8,2, lower.tail = F)

#ou 1 - pnorm(6,8,2)

#3� exemplo: mean = 8, sd = 2, x  < 6 ou x > 10

x3 = pnorm(6,8,2) + pnorm(10,8,2, lower.tail = F)

#4� exemplo: mean = 8, sd = 2, x  < 10 ou x > 8

X4 = pnorm(10,8,2) - pnorm(8,8,2)

#teste para verificar se � normal

#gerar numeros distribuidos normalmente

x5 = rnorm(100)

#gerar grafico de probabilidade normal

qqnorm(x5)
qqline(x5)

shapiro.test(x5)

