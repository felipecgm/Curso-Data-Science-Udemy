install.packages("e1071", dependencies = TRUE)

library(e1071)

credito = read.csv(file.choose(), sep = ",", header = T)

fix(credito)

dim(credito)

amostra = sample(2, 1000, replace = T, prob = c(0.7, 0.3))
amostra

credito_treino = credito[amostra == 1,]
credito_teste = credito[amostra == 2,]

dim(credito_teste)
fix(credito_treino)

modelo = naiveBayes(class ~ . , credito_treino)
fix(modelo)

class(modelo)

previsao = predict(modelo, credito_teste)
 
confusao = table(credito_teste$class, previsao)
confusao

taxa_acerto= ((confusao[1] + confusao[4]))/ sum(confusao)
taxa_acerto
taxa_erro = 1 - taxa_acerto
taxa_erro

novocredito = read.csv(file.choose(), sep = ",", header = T)

fix(novocredito)
dim(novocredito)

novo = predict(modelo, novocredito)
novo
