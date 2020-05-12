 boxplot(iris$Sepal.Width, outline = F)
 
 boxplot.stats(iris$Sepal.Width)$out

install.packages('outliers')  
library(outliers)

#superior
outlier(iris$Sepal.Width)

#inferior
outlier(iris$Sepal.Width, T)
