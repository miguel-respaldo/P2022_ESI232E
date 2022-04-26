Funcion resultado <- funcion_de_python ( nombre_funcion )
	Escribir "Funcion de Python (" + nombre_funcion + ")"
	resultado <- 0
Fin Funcion


Algoritmo archivos_en_python
	
	archivo <- funcion_de_python("open(directorio.csv,w)")
	
	Escribir "Cuantos datos vas a ingresar:"
	Leer datos
	
	Para x<-1 Hasta datos Con Paso 1 Hacer
		Escribir "Escribe tu nombre:"
		Leer nombre
		
		Escribir "Escribe tu telefono:"
		Leer telefono
		
		Escribir "Escribe tu dirección"
		Leer direccion
		
		archivo <- funcion_de_python("archivo.write(nombre, telefono, direccion)")
		
		Escribir  "------------------------"
		
	Fin Para
	
	archivo <- funcion_de_python("archivo.close()")
	Escribir "Los datos fueron guardados"
FinAlgoritmo
