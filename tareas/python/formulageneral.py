import math

a = eval(input("Escribe el numero a: "))
b = eval(input("Escribe el numero b: "))
c = eval(input("Escribe el numero c: "))

discriminante = b**2 - 4*a*c

x1 = (-b + math.sqrt(discriminante) ) / (2*a)
x2 = (-b - math.sqrt(discriminante) ) / (2*a)

print("El resultado de x1 es ", x1)
print("El resultado de x2 es ", x2)
