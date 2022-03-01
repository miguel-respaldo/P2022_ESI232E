Algoritmo tablas_de_multiplicar
	Escribir "Cual tabla de multiplicar quieres: "
	Leer tabla
	
	contador <- 1
	
	Mientras contador <= 10 Hacer
		Escribir contador, " x ", tabla, " = ", contador*tabla 
		contador <- contador + 1
	FinMientras
	
FinAlgoritmo
