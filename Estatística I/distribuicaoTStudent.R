#mean = 75 reais por hora amostra n = 9, st = 10
#< 80 reais por hora
#t = (x-mean)/(s/raiz(n))

t = (80 - 75) / (10 / sqrt(9))

pstud1 = pt(t, 8)

#> 80 reais

pstud2 = 1 - pstud1

#ou pt(t, 8, lower.tail = F)

