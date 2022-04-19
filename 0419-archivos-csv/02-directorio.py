import os

def menu():
    print(" -- Menu --")
    print("1. Listar el directorio.")
    print("2. Agregar al directorio.")
    print("3. Elimintar del directorio.")
    print("4. Modificar del directorio.")
    print("5. Mostrar a favoritos.")
    print("6. Salir")
    print("")

def mostrar_directorio(archivo):
    for linea in archivo:
        # split crea una lista a base de una cadena
        lista = linea.split(",")
        # strip quita el enter de una cadena
        #print(lista[0], " ", lista[1], " ", lista[2].strip())
        print("{:<20s}{:>17s}   {:<40s}".format(lista[1], lista[2], lista[3].strip()))


def mostrar_favoritos_directorio(archivo):
    for linea in archivo:
        # split crea una lista a base de una cadena
        lista = linea.split(",")
        if lista[0] == "*":
            # strip quita el enter de una cadena
            print("{:<20s}{:>17s}   {:<40s}".format(lista[1], lista[2], lista[3].strip()))


def agregar_al_directorio(archivo):
    nombre = input("Escribe el nombre: ")
    telefono = input("Escribe el telefono: ")
    direccion = input("Escribe la dirección: ")
    favorito = input("Es favorito S/N: ")
    fav = ""
    if favorito.lower() == "s":
        fav = "*"
    archivo.write(fav + "," + nombre + "," + telefono + "," + direccion + "\n")


def eliminar_del_directorio(nombre_archivo):
    temporal = open("temporal.csv","w")
    archivo = open(nombre_archivo, "r")

    nombre = input("Escribe el nombre a borrar: ")

    for linea in archivo:
        lista = linea.split(",")
        if nombre.lower() == lista[1].lower():
            print("El nombre", nombre, "fue eliminado.")
            continue
        temporal.write(linea)

    archivo.close()
    temporal.close()
    os.remove(nombre_archivo)
    # rename renombra los archivos
    os.rename("temporal.csv", nombre_archivo)

def modificar_del_directorio(nombre_archivo):
    temporal = open("temporal.csv","w")
    archivo = open(nombre_archivo, "r")

    nombre = input("Escribe el nombre a modificar: ")

    for linea in archivo:
        lista = linea.split(",")
        if nombre.lower() == lista[1].lower():
            agregar_al_directorio(temporal)
        else:
            temporal.write(linea)

    archivo.close()
    temporal.close()
    os.remove(nombre_archivo)
    # rename renombra los archivos
    os.rename("temporal.csv", nombre_archivo)


opcion = 1
nombre_archivo = "directorio.csv"

if not os.path.exists(nombre_archivo):
    archivo = open(nombre_archivo, "w")
    archivo.write("F,Nombre,Telefono,Dirección\n")
    archivo.close()

while opcion != 6:
    menu()
    opcion = eval(input("Opcion: "))
    if opcion == 1:
        archivo = open(nombre_archivo, "r")
        mostrar_directorio(archivo)
        archivo.close()
    elif opcion == 2:
        archivo = open(nombre_archivo, "a")
        agregar_al_directorio(archivo)
        archivo.close()
    elif opcion == 3:
        eliminar_del_directorio(nombre_archivo)
    elif opcion == 4:
        modificar_del_directorio(nombre_archivo)
    elif opcion == 5:
        archivo = open(nombre_archivo, "r")
        mostrar_favoritos_directorio(archivo)
        archivo.close()
    elif opcion == 6:
        pass
    else:
        print(" *** Opcion Invalida ***")

