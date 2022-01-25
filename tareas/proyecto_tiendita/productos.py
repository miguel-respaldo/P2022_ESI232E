import csv

# Nombre de los archivos para abrir
ARCHIVO_PRODUCTOS="productos.csv"

def mostrar():
    archivo = open(ARCHIVO_PRODUCTOS,"r")
    lector = csv.reader(archivo)
    contador = 1
    print("{:<5s}{:<15s}{:>8s}".format("No.", "Nombre", "Precio"))
    for fila in lector:
        if fila[0] == "Producto":
            continue
        print("{:<5d}{:<15s}{:>8.2f}".format(contador, fila[0], float(fila[1])))
        contador = contador + 1
    archivo.close()

def buscar_nombre(numero):
    archivo = open(ARCHIVO_PRODUCTOS,"r")
    lector = csv.reader(archivo)
    contador = 1
    producto_a_buscar = ""
    for fila in lector:
        if fila[0] == "Producto":
            continue
        if contador == numero:
            producto_a_buscar = fila[0]
            break
        contador = contador + 1
    archivo.close()
    return producto_a_buscar

def buscar_precio(numero):
    archivo = open(ARCHIVO_PRODUCTOS,"r")
    lector = csv.reader(archivo)
    contador = 1
    precio_a_buscar = ""
    for fila in lector:
        if fila[0] == "Producto":
            continue
        if contador == numero:
            precio_a_buscar = fila[1]
            break
        contador = contador + 1
    archivo.close()
    return precio_a_buscar

