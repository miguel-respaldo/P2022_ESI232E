Algoritmo menu_operaciones
	
	opcion_menu <- 0
	Mientras opcion_menu <> 5 Hacer
		Escribir "1. Suma"
		Escribir "2. Resta"
		Escribir "3. Multiplicaci�n"
		Escribir "4. Divisi�n"
		Escribir "5. Salir"
		Escribir ""
		Escribir "Opcion"
		Leer opcion_menu
		
		Si opcion_menu <> 5 Entonces
			Escribir "Escribe el primer n�mero:"
			Leer num1
			Escribir "Escribe el segundo n�mero:"
			Leer num2
		FinSi
		
		Si opcion_menu = 1 Entonces
			resultado <- num1 + num2
		Fin Si
		Si opcion_menu = 2 Entonces
			resultado <- num1 - num2
		Fin Si
		Si opcion_menu = 3 Entonces
			resultado <- num1 * num2
		Fin Si
		Si opcion_menu = 4 Entonces
			Si num2 = 0 Entonces
				Escribir "No se puede dividir entre cero"
				resultado <- 0
			SiNo
				resultado <- num1 / num2
			FinSi			
		Fin Si
		
		Si opcion_menu <> 5 Entonces
			Escribir "El resultado es ", resultado
			Escribir "------------------------------"
		FinSi
		
	Fin Mientras
	
FinAlgoritmo
