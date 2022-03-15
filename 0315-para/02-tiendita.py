opcion_menu_principal = 0
opcion_menu_productos = 0

while opcion_menu_principal != 4:
    print("------ Menu principal -----")
    print("1. Mostrar productos")
    print("2. Mostrar carrito de compras")
    print("3. Mostrar descuentos")
    print("4. Salir")
    print("")
    opcion_menu_principal = eval(input("Opcion: "))

    if opcion_menu_principal == 1:
        while opcion_menu_productos != 4:
            print("------ Menu Productos -----")
            print("1. Ropa")
            print("2. Accesorios de Ropa")
            print("3. Eletrodomesticos")
            print("4. Salir menu anterior")
            print("")
            opcion_menu_productos = eval(input("Opcion: "))

            if opcion_menu_productos == 1:
                print("Ropa")
            elif opcion_menu_productos == 2:
                print("Accesorios")
            elif opcion_menu_productos == 3:
                print("Electrodomesticos")

    elif opcion_menu_principal == 2:
        print("Aqui va la impresión de carrito de compras")
    elif opcion_menu_principal == 3:
        print("aqui va los productos con Descueto")