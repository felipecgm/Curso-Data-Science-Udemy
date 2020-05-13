import numpy as np
from scipy.stats import chi2_contingency

novela = np.array([[19,6], [43,32]])

qui = chi2_contingency(novela)

#segundo parametro >> pvalue = 0,15
#0,15 > 0,05. Portanto não podemos rejeitar a ho
#Ho - não há variação significativa entre os grupos

 





