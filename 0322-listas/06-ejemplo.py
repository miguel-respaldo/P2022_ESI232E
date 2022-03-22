lista = ["manzana", "plátano", "limón", "cereza", "kiwi", "mango", "melón"]
print(lista)
lista.sort()
print(lista)

numeros = [100, 50, 65, 82, 23]
numeros.sort()
print(numeros)

lista.sort(reverse=True)
print(lista)
numeros.sort(reverse=True)
print(numeros)

lista = ["manzana", "Plátano", "Limón", "cereza", "Kiwi", "Mango", "melón"]
lista.sort()
print(lista)
lista.sort(key=str.lower)
print(lista)

