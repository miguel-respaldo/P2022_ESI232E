Algoritmo piensa_un_numero_aleatorio
	
	// azar regesa un número entre 0 y el número que le dicen
	num_compu <- azar(10+1)
	// Solo en PseInt se suma +1
	usuario <- 20
	Mientras num_compu <> usuario Hacer
		Escribir "En que número estoy pensando"
		Leer usuario
		
		Si num_compu <> usuario Entonces
			Escribir "No, ese no es el numero "
		FinSi
	Fin Mientras
	
	Escribir "Felicidades adivinaste"
	
FinAlgoritmo
