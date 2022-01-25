import csv
import productos
import os

# Nombre de los archivos para abrir
ARCHIVO_CARRITO="carrito.csv"

def inicializar():
    archivo = open(ARCHIVO_CARRITO,"w")
    archivo.write("Producto, Precio, Cantidad\n")
    archivo.close()


def mostrar():
    archivo = open(ARCHIVO_CARRITO,"r")
    lector = csv.reader(archivo)
    contador = 1
    print("----  Carrito ----------")
    print("{:<5s}{:<15s}{:>8s}{:>10s}".format("No.", "Nombre", "Precio", "Cantidad"))
    for fila in lector:
        if fila[0] == "Producto":
            continue
        print("{:<5d}{:<15s}{:>8.2f}{:>10d}".format(contador, fila[0], float(fila[1]), int(fila[2])))
        contador = contador + 1
    archivo.close()


def agregar (num_producto, cantidad):
    nombre_producto = productos.buscar_nombre(num_producto)
    precio_producto = productos.buscar_precio(num_producto)
    archivo = open(ARCHIVO_CARRITO,"a")
    archivo.write(nombre_producto + ", " + precio_producto + ", "+ str(cantidad) + "\n")
    archivo.close()

def calcular_total():
    archivo = open(ARCHIVO_CARRITO,"r")
    lector = csv.reader(archivo)
    total = 0
    for fila in lector:
        if fila[0] == "Producto":
            continue
        total = total + float(fila[1]) * float(fila[2])
    archivo.close()
    return total


def borrar(numero):
    archivo = open(ARCHIVO_CARRITO,"r")
    archivo_temporal = open("temporal.csv","w", newline="")

    lector = csv.reader(archivo)
    escritor = csv.writer(archivo_temporal)

    contador = 0
    for fila in lector:
        if numero == contador:
            contador = contador + 1
            continue
        escritor.writerow(fila)
        contador = contador + 1

    archivo.close()
    archivo_temporal.close()
    os.remove(ARCHIVO_CARRITO)
    os.rename("temporal.csv", ARCHIVO_CARRITO)

