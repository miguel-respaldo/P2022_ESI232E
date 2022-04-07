import area
import menu

opcion_menu = 0

while opcion_menu != 5:
    menu.mostrar()
    opcion_menu = eval(input("Opción: "))

    if   opcion_menu == 1:
        base = eval(input("Escribe el valor de la base: "))
        altura = eval(input("Escribe el valor de la altura: "))
        Area = area.rectangulo(base, altura)
        print("El área es: ", Area)
    elif opcion_menu == 2:
        base = eval(input("Escribe el valor de la base: "))
        altura = eval(input("Escribe el valor de la altura: "))
        Area = area.triangulo(base, altura)
        print("El área es: ", Area)

    elif opcion_menu == 3:
        lado = eval(input("Escribe el valor de lado: "))
        Area = area.rectangulo(lado, lado)
        print("El área es:", Area)
    elif opcion_menu == 4:
        radio = eval(input("Escribe el valor del radio: "))
        Area = area.circulo(radio)
        print("El área es: ", Area)
