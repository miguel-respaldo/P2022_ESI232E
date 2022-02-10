Algoritmo calcular_varianza
	// Pedimos los números al usuario
	Escribir "Escribe el primer número: "
	Leer num1
	
	Escribir "Escribe el segundo número: "
	Leer num2
	
	Escribir "Escribe el tercer número: "
	Leer num3
	
	Escribir "Escribe el cuarto número: "
	Leer num4
	
	Escribir "Escribe el quinto número: "
	Leer num5
	
	suma <- num1 + num2 + num3 + num4 + num5
	promedio <- suma / 5
	varianza <- ((num1 - promedio)^2 + (num2 - promedio)^2 + (num3 - promedio)^2 + (num4 - promedio)^2 + (num5 - promedio)^2) / (5-1)
	
	// Escribimos el resulado
	Escribir "La varianza es: ", varianza
	
FinAlgoritmo
