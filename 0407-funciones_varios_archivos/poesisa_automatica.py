import random

def sujeto():
    num = random.randint(1,3)
    if num == 1:
        texto = "El gato"
    elif num == 2:
        texto = "El perro"
    elif num == 3:
        texto = "El carro"
    return texto

def verbo():
    num = random.randint(1,3)
    if num == 1:
        texto = "es"
    elif num == 2:
        texto = "tiene"
    elif num == 3:
        texto = "no es"
    return texto

def objeto():
    num = random.randint(1,3)
    if num == 1:
        texto = "de color rojo"
    elif num == 2:
        texto = "de tamaño grande"
    elif num == 3:
        texto = "pequeño"
    return texto

print(sujeto(),verbo(),objeto())
