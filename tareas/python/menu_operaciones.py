opcion_menu = 0
while opcion_menu != 5:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("")
    opcion_menu = eval(input("Opción:"))

    if opcion_menu > 0 and opcion_menu < 5:
        num1 = eval(input("Escribe un número: "))
        num2 = eval(input("Escribe otro número: "))

    if opcion_menu == 1:
        resultado = num1 + num2
    elif opcion_menu == 2:
        resultado = num1 - num2
    elif opcion_menu == 3:
        resultado = num1 * num2
    elif opcion_menu == 4:
        if num2 == 0:
            print("No se puede dividir entre cero")
            resultado = 0
        else:
            resultado = num1 / num2

    if opcion_menu > 0 and opcion_menu < 5:
        print("El resultado es:", resultado)
        print("-------------------------")

