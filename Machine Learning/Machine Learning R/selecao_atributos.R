library(e1071)

modelo = svm(class ~ ., credito_treino)
modelo

previsao = predict(modelo, credito_teste)
previsao

confusao = table(credito_teste$class,  previsao)
confusao

taxa_acerto = (confusao[1] + confusao[4])/ sum(confusao)
taxa_acerto

taxa_erro = 1 - taxa_acerto
taxa_erro

install.packages("FSelector", dependencies = T)
library(FSelector)

random.forest.importance(class ~  ., credito)

modelo = svm(class ~ checking_status + duration + credit_history + purpose, credito_treino)
previsao = predict(modelo, credito_teste)

confusao = table(credito_teste$class, previsao)
confusao

taxa_acerto2 = (confusao[1] + confusao[4])/ sum(confusao)
taxa_acerto2               
