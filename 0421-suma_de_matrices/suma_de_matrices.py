m1 = []  # Matriz A
m2 = []  # Matriz B
suma =[] # El resultado de la suma m1 + m2

def llenar_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            numero = eval(input("Escribe el valor ("+str(f+1)+","+str(c+1)+"): "))
            matriz[f].append(numero)
    return matriz

def imprimir_matriz(matriz):
    for f in range(len(matriz)):
        print("[ ", end="") # el end="" es para que no de una nueva linea
        for c in range(len(matriz[f])):
            print(matriz[f][c]," ", end="")
        print("]")

def sumar_matriz(m1, m2):
    matriz = []
    # Aqui hay que completar el código
    # Puedes usar parte de este codigo para completar lo que falta
    return matriz

filas = eval(input("¿Cuantas filas tiene la matriz?: "))
columnas = eval(input("¿Cuantas columnas tiene la matriz?: "))

print("Llenando la matriz 1")
m1 = llenar_matriz(filas, columnas)

print("Llenando la matriz 2")
m2 = llenar_matriz(filas, columnas)

print("La matriz 1 es: ")
imprimir_matriz(m1)

print("La matriz 2 es: ")
imprimir_matriz(m2)

suma = sumar_matriz(m1, m2)

print("La suma es:")
imprimir_matriz(suma)

