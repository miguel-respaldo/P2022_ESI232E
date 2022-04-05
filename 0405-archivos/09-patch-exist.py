import os

if os.path.exists("ruta.txt"):
    f = open("ruta.txt")
    ruta = f.readline().strip()
    if os.path.exists(ruta):
        os.remove(ruta)
        print("Ya borre", ruta)
else:
    print("El archivo no existe")