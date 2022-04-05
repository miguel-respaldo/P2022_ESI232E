f = open("demo.txt","r")
contador = 1
for linea in f:
    print(contador, linea, end="")
    contador += 1
