import math

def menu():
    print("1. Calcular área de un rectángulo")
    print("2. Calcular área de un triangulo")
    print("3. Calcular área de un cuadrado")
    print("4. Calcular área de un circulo")
    print("5. Salir")
    print("")

def area_circulo(radio):
    return math.pi * (radio ** 2)

def area_rectangulo(base, altura):
    return base * altura

opcion_menu = 0

while opcion_menu != 5:
    menu()
    opcion_menu = eval(input("Opción: "))

    if   opcion_menu == 1:
        base = eval(input("Escribe el valor de la base: "))
        altura = eval(input("Escribe el valor de la altura: "))
        area = area_rectangulo(base, altura)
        print("El área es: ", area)
    elif opcion_menu == 2:
        base = eval(input("Escribe el valor de la base: "))
        altura = eval(input("Escribe el valor de la altura: "))
        area = area_rectangulo(base, altura)/2
        print("El área es: ", area)

    elif opcion_menu == 3:
        lado = eval(input("Escribe el valor de lado: "))
        area = area_rectangulo(lado, lado)
        print("El área es:", area)
    elif opcion_menu == 4:
        radio = eval(input("Escribe el valor del radio: "))
        area = area_circulo(radio)
        print("El área es: ", area)
