archivo = open("directorio1.csv","w")

datos = eval(input("Cuantos datos vas a ingresar: "))

for x in range(datos):
    nombre = input("Escribe el nombre: ")
    telefono = input("Escribe el telefono: ")
    direccion = input("Escribe la dirección: ")
    archivo.write(nombre + "," + telefono + "," + direccion + "\n")

archivo.close()
print("Los datos fueron guardados.")
