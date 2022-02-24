import math

x1 = eval(input("Escribe el numero x1: "))
y1 = eval(input("Escribe el numero y1: "))
x2 = eval(input("Escribe el numero x2: "))
y2 = eval(input("Escribe el numero y2: "))

distancia = math.sqrt( (x1-x2)**2 + (y1 -y2)**2 )

print("El resultado la distancia es ", distancia)
