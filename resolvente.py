print("vamos a hacer la resolvente")
print("escoge los valores")
b= (int(input("cuanto vale b")))
a= (int(input("cuanto vale a")))
c= (int(input("cuanto vale c")))

from math import sqrt

d= b*b
print(d, "d")

e= -4*a*c
print(e, "e")

z= d+e
print(z, "z")

if z<0:
 print("el resultado de la raiz es un numero imaginario")
else:
 f= sqrt(z)

 g= -b + f

 x=2*a

 h= g/x

 i= -b - f
 j= i/x

 print("Los resultados son", h, "y", j)
