def mayor(*numeros):
    lista = list(numeros)
    lista.sort()
    print("El número mayor es", lista[-1])

mayor(10,20,8, 12,15,30, 70,1,2,3,4,5,6)