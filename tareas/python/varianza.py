num1 = eval(input("Escribe el primer numero: "))
num2 = eval(input("Escribe el segundo numero: "))
num3 = eval(input("Escribe el tercer numero: "))
num4 = eval(input("Escribe el cuarto numero: "))
num5 = eval(input("Escribe el quinto numero: "))


suma = num1 + num2 + num3 + num4 + num5
promedio = suma / 5

varianza = ( (num1 - promedio)**2 + (num2 - promedio)**2 + (num3 - promedio)**2 + (num4 - promedio)**2 + (num5 - promedio)**2 )  / (5 - 1)

print("El resultado de la varianza es ", varianza)
