opcion_menu = 0
lista = [] # lista vacia

while opcion_menu != 9:
    print("1. Iniciarlizar lista")
    print("2. Agregar elemento")
    print("3. Eliminar elemento")
    print("4. Remplazar elemento")
    print("5. Buscar elemento")
    print("6. Número de elementos")
    print("7. Ordenar la lista")
    print("8. Imprimir la lsita")
    print("9. Salir")
    print("")
    opcion_menu = eval(input("Opción:"))

    if   opcion_menu == 1:
        lista = []
    elif opcion_menu == 2:
        elemento = input("Qué elemento quieres agregar: ")
        lista.append(elemento)
    elif opcion_menu == 3:
        elemento = input("Qué elemento quieres eliminar: ")
        if elemento in lista:
            lista.remove(elemento)
        else:
            print("el elemento", elemento, "NO esta en la lista")
    elif opcion_menu == 4:
        elemento = input("Qué elemento quieres remplazar: ")
        if elemento in lista:
            nuevo = input("Escribe el nuevo elemento: ")
            posicion = lista.index(elemento)
            lista[posicion] = nuevo
        else:
            print("el elemento", elemento, "NO esta en la lista")
    elif opcion_menu == 5:
        elemento = input("Qué elemento quieres buscar: ")
        if elemento in lista:
            print("El elemento", elemento, "si esta en la lista")
            posicion = lista.index(elemento)
            print("y tiene la posición", posicion)
        else:
            print("el elemento", elemento, "NO esta en la lsita")
    elif opcion_menu == 6:
        print("La lsita tiene", len(lista), "elementos")
    elif opcion_menu == 7:
        lista.sort()
    elif opcion_menu == 8:
        print(lista)

