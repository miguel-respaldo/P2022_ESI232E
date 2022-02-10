Algoritmo calcular_distancia
	// Pedimos los números al usuario
	Escribir "Escribe el número x1: "
	Leer x1
	
	Escribir "Escribe el número y1: "
	Leer y1
	
	Escribir "Escribe el número x2: "
	Leer x2
	
	Escribir "Escribe el número y2: "
	Leer y2
	
	// Calculamos la distancia
	distancia <-  rc( (x1 - x2)^2 + (y1 - y2)^2 )
	
	// Imprimo resultado
	Escribir "La distancia es: ", distancia
	
FinAlgoritmo
