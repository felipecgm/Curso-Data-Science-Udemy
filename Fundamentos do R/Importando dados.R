#texto
x =  read.csv(file.choose(),header = TRUE, sep = ";")
x

#odbc
install.packages("RODBC")
library(RODBC)

#planilha
install.packages("xlsx")
library(xlsx)
dados = read.xlsx(file.choose(),sheetIndex = 1)
dados

install.packages("foreign")