num = eval(input("Escribe un número: "))

contador = 1
factorial = 1

while contador <= num:
    factorial = factorial * contador
    #factorial *= contador
    contador = contador + 1

print("El factorial es", factorial)

