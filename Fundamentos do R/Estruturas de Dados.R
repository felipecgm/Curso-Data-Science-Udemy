#vetores

x <- c(1,2,3,4,5,6)
x
x[1]
x[1] <- 10
x[1]
x


#outros tipos de vetores

y = c("a","b","c","d")
y
z = c(1L,2L,3L)
z

#matrizes
VADeaths
colnames(VADeaths)
rownames(VADeaths)

#S� coluna 1
VADeaths[,1]

#S� linha 1
VADeaths[1,]

#Linhas de 1 a 3
VADeaths[1:3,]

#Data frame
longley

#funciona como matriz
longley[,1:3]

$acessar coluna com $
longley$Unemployed
#ou nome
longley ['Unemployed']

#listas
ability.cov
#acessando elementos
ability.cov$cov
ability.cov[1]
#verificando que s�o objetos diferentes
class(ability.cov$cov)
class(ability.cov$center)

#acessando elemento dentro da lista
ability.cov$cov[,1:3]

#fatores, vari�veis categ�ricas com um n�mero limitado de valores diferentes
#s�o armazenados como inteiros
state.region

