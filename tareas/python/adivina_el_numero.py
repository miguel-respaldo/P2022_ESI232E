import random

computadora = random.randint(1,10)

usuario = eval(input("Ingresa un número: "))

while computadora != usuario:
    print("No, ese no es el número, intenta de nuevo")
    usuario = eval(input("Ingresa un número: "))

print("Felicidades Adivinaste")
