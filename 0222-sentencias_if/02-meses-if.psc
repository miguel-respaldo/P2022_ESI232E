Algoritmo meses_del_anio
	
	Escribir "Introduce un numero de mes del año"
	Leer mes
	
	si mes = 1 Entonces
		Escribir "Enero"
	FinSi
	si mes = 2 Entonces
		Escribir "Febrero"
	FinSi
	si mes = 3 Entonces
		Escribir "Marzo"
	FinSi
	si mes = 4 Entonces
		Escribir "Abril"
	FinSi
	si mes = 5 Entonces
		Escribir "Mayo"
	FinSi
	si mes = 6 Entonces
		Escribir "Junio"
	FinSi
	si mes = 7 Entonces
		Escribir "Julio"
	FinSi
	si mes = 8 Entonces
		Escribir "Agosto"
	FinSi
	si mes = 9 Entonces
		Escribir "Septiembre"
	FinSi
	si mes = 10 Entonces
		Escribir "Octubre"
	FinSi
	si mes = 11 Entonces
		Escribir "Noviembre"
	FinSi
	si mes = 12 Entonces
		Escribir "Diciembre"
	FinSi
	
	si mes < 1 o  mes > 12 Entonces
		Escribir "Error: el mes no existe"
	FinSi
	
FinAlgoritmo
