import pandas as pd
from scipy import stats
import statsmodels.api as sma
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

tratamento = pd.read_csv("anova.csv", sep = ";")

tratamento.boxplot(by = "Remedio", grid = False)

#método anova com 1 fator
modelo1 = ols("Horas ~ Remedio", data = tratamento).fit()

resultados1 = sma.stats.anova_lm(modelo1)

#método anova com 2 fatores

modelo2 = ols("Horas ~ Remedio * Sexo", data = tratamento).fit()

resultados2 = sma.stats.anova_lm(modelo2)

mc = MultiComparison(tratamento["Horas"], tratamento["Remedio"])

resultado_teste = mc.tukeyhsd()
print(resultado_teste)

resultado_teste.plot_simultaneous()









