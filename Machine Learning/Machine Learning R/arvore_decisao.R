install.packages("rpart", dependencies = T)

library(rpart)

credito = read.csv(file.choose(), sep = ",", header = T)
fix(credito)
dim(credito)

amostra = sample(2, 1000, replace = T, prob = c(0.7, 0.3))
credito_treino = credito[amostra == 1, ]
credito_teste = credito[amostra == 2, ]
dim(credito_teste)
dim(credito_treino)

arvore = rpart(class ~ ., data = credito_treino, method = "class")
print(arvore)

plot(arvore)
text(arvore, use.n = T, all = T, cex = .8)

teste = predict(arvore, newdata = credito_teste)

teste

cred = cbind(credito_teste, teste)
fix(cred)

cred['Result'] = ifelse(cred$bad >= 0.5, "bad", "good")
fix(cred)

confusao = table(cred$class, cred$Result)
confusao

taxa_acerto = (confusao[1] + confusao[4]) / sum(confusao)
taxa_acerto
taxa_erro
