import matplotlib.pyplot as plt
import pandas as pd
import numpy  as np
from pyod.models.knn import KNN

iris = pd.read_csv("iris.csv")

#com outliers
#plt.boxplot(iris.iloc[:, 1])

#sem outliers
plt.boxplot(iris.iloc[:, 1], showfliers = False)

#buscar outliers

outliers = iris[(iris["sepal width"] > 4) | (iris["sepal width"] < 2.1)]

sepal_width = iris.iloc[:, 1].values

sepal_width = sepal_width.reshape(-1, 1)

detector = KNN()

detector.fit(sepal_width)

previsoes = detector.labels_




