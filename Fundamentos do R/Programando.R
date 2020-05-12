a = 10
b = 20

if(a > 10)
{
  print("A eh maior")
}else
{
  print("A nao eh menor")
}

x = ifelse(a > 10, "A eh maior", "A nao eh menor")
x

for(i in 1:10)
{
  print(i)
}

a = 1

while(a <= 10)
{
  print(a)
  a = a + 1
}

parouimpar <- function(x){
  return (ifelse(x %% 2 == 0, "Par", "Impar"))
}

parouimpar(5)
parouimpar(12)