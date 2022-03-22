frutas = ["manzana", "plátano", "naranja"]

nueva_lista = [x.upper() for x in frutas]

print(frutas)
print(nueva_lista)

nueva_lista = ["hola" for x in frutas]
print(nueva_lista)

nueva_lista = [x if x != "plátano" else "naranja" for x in frutas]
print(nueva_lista)
