import math

a = eval(input("Escribe en número a: "))
b = eval(input("Escribe en número b: "))
c = eval(input("Escribe en número c: "))

discriminante = b**2 - 4*a*c

x1 = (-b + math.sqrt(discriminante)) / (2*a)
x2 = (-b - math.sqrt(discriminante)) / (2*a)

print("X1 es:",x1)
print("X1 es:",x2)
