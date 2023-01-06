#se pide por teclado ingresar n y p 
p=int(input('Ingrese un numero: '))
n=int(input('Ingrese otro numero: '))
#  se implementa la funcion con un blucle while 
def recur(n,p,acumulado):
  while n>0 :            #el bucle while preguntara si el numero n es mallor q 0
    acumulado+=n*p
    n-=1
    recur(n,p,acumulado)
  return acumulado       # al final retorna el acumulado que seria el resultado entre la muntiplicacion de n y p
 
print(recur(n,p,0))