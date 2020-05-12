novela = matrix(c(41,34,18,7), nrow = 2, byrow = T)
fix(novela)
rownames(novela) = c("Masculino", "Feminino")
colnames(novela) = c("Assiste", "Não Assiste")
fix(novela)

chisq.test(novela)
