import os

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
    archivo_prod = open(ARCHIVO_PRODUCTOS, "r")
    archivo_carr = open(ARCHIVO_CARRITO,"a")

    # Buscamos el precio del prodcuto
    for linea in archivo_prod:
        lista = linea.split(",")
        # Al encontrar el producto lo gardamos en carrito
        if producto.lower() == lista[1].lower():
            archivo_carr.write(lista[1] + "," + lista[2] + "," + str(cantidad))
            break

    archivo_prod.close()
    archivo_carr.close()


def carrito_agregar_oferta(producto, cantidad):
    archivo_prod = open(ARCHIVO_PRODUCTOS, "r")
    archivo_carr = open(ARCHIVO_CARRITO,"a")

    # Buscamos el precio del prodcuto
    for linea in archivo_prod:
        lista = linea.split(",")
        # Al encontrar el producto lo gardamos en carrito
        if producto.lower() == lista[1].lower():
            archivo_carr.write(lista[1] + "," + lista[4].strip() + "," + str(cantidad))
            break

    archivo_prod.close()
    archivo_carr.close()


def carrito_mostrar():
    archivo = open(ARCHIVO_CARRITO,"r")
    total = 0.0
    numero = 1

    print("{:<5s}{:<15s}{:>8s}{:>8s}".format("No.", "Nombre", "Precio", "Cantidad"))
    for linea in archivo:
        lista = linea.split(",")
        # Nos saltamos la primera linea, que es la de los titulos.
        if lista[0] == "Producto":
            continue
        print("{:<5d}{:<15s}{:>8.2f}{:^8d}".format(numero,lista[0],float(lista[1]),int(lista[2])))
        numero += 1
        total += float(lista[1]) * float(lista[2])

    archivo.close()

    print("-----------------------------------------------")
    print("{:>30s}{:>8.2f}".format("Total:", total))


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
        if  lista[4].strip().lower() =! "0":
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

# Primero nos aseguramos si existe un carrito anterior
if os.path.exists(ARCHIVO_CARRITO):
    print("Un archivo de carrito existe")
    usar = input("¿Gustas usar este archivo? [S/n]:")
    if usar.lower() == "n":
        archivo = open(ARCHIVO_CARRITO,"w")
        archivo.write("Producto,Precio,Cantidad\n")
        archivo.close()
else:
    archivo = open(ARCHIVO_CARRITO,"w")
    archivo.write("Producto,Precio,Cantidad\n")
    archivo.close()


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
