Algoritmo calcular_determinante
	// Pedimos los números al usuario
	Escribir "Escribe el número a11: "
	Leer a11
	
	Escribir "Escribe el número a22: "
	Leer a22
	
	Escribir "Escribe el número a12: "
	Leer a12
	
	Escribir "Escribe el número a21: "
	Leer a21
	
	// Calculamos el determinante
	determinante <- a11*a22 - a12*a21
	
	// Imprimo resultado
	Escribir "El determinate es: ", determinante
	
FinAlgoritmo
