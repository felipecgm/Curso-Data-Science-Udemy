tratamento = read.csv(file.choose(), sep = ";", head  = T)
fix(tratamento)

boxplot(tratamento$Horas ~ tratamento$Remedio)

#analise de variancia de um fator

an = aov(Horas ~ Remedio, data = tratamento)
summary(an)

#analise de variancia de dois fatores

an2 = aov(Horas ~ Remedio * Sexo, data = tratamento)
summary(an2)

tukey = TukeyHSD(an)
summary(an)
plot(tukey)
