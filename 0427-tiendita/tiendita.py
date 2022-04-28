
ARCHIVO_PRODUCTOS="productos.csv"
ARCHIVO_CARRITO="carrito.csv"

def menu_principal():
    print("------ Menu principal ------")
    print("1. Mostrar productos.")
    print("2. Mostrar carrito.")
    print("3. Mostrar ofertas.")
    print("4. Salir")
    print("")
    opcion = int(input("Opción: "))
    return opcion


def menu_productos():
    print("------ Menu productos ------")
    print("1. Mostrar botanas.")
    print("2. Mostrar refrescos.")
    print("3. Mostrar bebidas alcoholicas.")
    print("4. Mostrar lacteos.")
    print("5. Salir")
    print("")
    opcion = int(input("Opción: "))
    return opcion


def carrito_agregar(producto, cantidad):
    pass


def carrito_agregar_oferta(producto, cantidad):
    pass


def carrito_mostrar():
    pass


def producto_mostrar(la_categoria):
    archivo = open(ARCHIVO_PRODUCTOS, "r")
    lista_de_productos = []
    numero = 1

    print("{:<5s}{:<15s}{:>8s}{:>20s}".format("No.", "Nombre", "Precio", "Cantidad en almacen"))
    for linea in archivo:
        lista = linea.split(",")
        if la_categoria.lower() == lista[0].strip().lower():
            lista_de_productos.append(lista[1])
            print("{:<5d}{:<15s}{:>8.2f}{:^20d}".format(numero,lista[1],float(lista[2]),int(lista[3])))
            numero += 1

    archivo.close()

    print("-----------------------------------------------")
    print("¿Cúal producto desear agregar al carrito?")
    print("Nota: puedes ponder 0 para salir")
    producto = input("Producto: ")

    if producto.isnumeric():
        num_prod = int(producto)
        if num_prod != 0:
            cantidad = eval(input("¿Cuantos articulos?: "))
            carrito_agregar(lista_de_productos[num_prod-1], cantidad)
    else:
        if producto.title() in lista_de_productos:
            cantidad = eval(input("¿Cuantos articulos?: "))
            carrito_agregar(producto.title(), cantidad)
        else:
            print("-------------------------------")
            print("| Error: No existe el producto|")
            print("-------------------------------")

    print("-----------------------------------------------")


def producto_mostrar_ofertas():
    archivo = open(ARCHIVO_PRODUCTOS, "r")
    lista_de_productos = []
    numero = 1

    print("{:<5s}{:<15s}{:>8s}{:>20s}".format("No.", "Nombre", "Precio", "Cantidad en almacen"))
    for linea in archivo:
        lista = linea.split(",")
        if la_categoria.lower() == lista[0].strip().lower():
            lista_de_productos.append(lista[1])
            print("{:<5d}{:<15s}{:>8.2f}{:^20d}".format(numero,lista[1],float(lista[4]),int(lista[3])))
            numero += 1

    archivo.close()

    print("-----------------------------------------------")
    print("¿Cúal producto desear agregar al carrito?")
    print("Nota: puedes ponder 0 para salir")
    producto = input("Producto: ")

    if producto.isnumeric():
        num_prod = int(producto)
        if num_prod != 0:
            cantidad = eval(input("¿Cuantos articulos?: "))
            carrito_agregar_oferta(lista_de_productos[num_prod-1], cantidad)
    else:
        if producto.title() in lista_de_productos:
            cantidad = eval(input("¿Cuantos articulos?: "))
            carrito_agregar_oferta(producto.title(), cantidad)
        else:
            print("-------------------------------")
            print("| Error: No existe el producto|")
            print("-------------------------------")

    print("-----------------------------------------------")


### Programa principal ####

opcion_menu_principal = 0

while opcion_menu_principal != 4:
    opcion_menu_principal = menu_principal()

    if   opcion_menu_principal == 1:
        opcion_menu_productos = 0:

        while opcion_menu_productos != 5:
            if   opcion_menu_productos == 1:
                producto_mostrar("botanas")
            elif opcion_menu_productos == 2:
                producto_mostrar("refrescos")
            elif opcion_menu_productos == 3:
                producto_mostrar("bebidas")
            elif opcion_menu_productos == 4:
                producto_mostrar("lacteos")
            elif opcion_menu_productos == 5:
                pass
            else:
                print("--------------------------")
                print("| Error: Opción inválida |")
                print("--------------------------")

    elif opcion_menu_principal == 2:
        carrito_mostrar()
    elif opcion_menu_principal == 3:
        producto_mostrar_ofertas()
    elif opcion_menu_principal == 4:
        pass
    else:
        print("--------------------------")
        print("| Error: Opción inválida |")
        print("--------------------------")
