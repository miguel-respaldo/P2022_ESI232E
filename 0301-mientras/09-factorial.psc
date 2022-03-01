Algoritmo calcular_factorial
	
	Escribir "Escribe un numero: "
	Leer num
	
	contador <- 1
	factorial <- 1
	Mientras contador <= num Hacer
		factorial <- factorial * contador
		contador <- contador + 1
	Fin Mientras
	
	Escribir "El factorial es ", factorial
	
FinAlgoritmo
