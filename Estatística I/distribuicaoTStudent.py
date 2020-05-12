from scipy.stats import t as tst
from math import sqrt

#mean = 75 reais por hora amostra n = 9, st = 10
#< 80 reais por hora
#t = (x-mean)/(s/raiz(n))

t = (80 - 75) / (10 / sqrt(9))

ptstud = tst.cdf(t, 8)

#< 80 reais por hora

ptstud2 = tst.sf(t, 8)






