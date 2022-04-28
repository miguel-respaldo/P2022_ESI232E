Funcion regresa <- python (nombre)
	Escribir nombre
	regresa <- 0
Fin Funcion

Funcion la_opcion <- menu_principal ()
	Escribir "------ Menu principal ------"
	Escribir "1. Mostrar productos."
	Escribir "2. Mostrar carrito."
	Escribir "3. Mostrar ofertas."
	Escribir "4. Salir"
	Escribir ""
	Escribir "Opcion:"
	Leer la_opcion
Fin Funcion

Funcion la_opcion <- menu_productos ()
	Escribir "------ Menu productos ------"
	Escribir "1. Mostrar botanas."
	Escribir "2. Mostrar refrescos."
	Escribir "3. Mostrar bebidas alcoholicas."
	Escribir "4. Mostrar lacteos."
	Escribir "5. Salir"
	Escribir ""
	Escribir "Opcion:"
	Leer la_opcion
Fin Funcion

Algoritmo tiendita

	opcion_menu_principal <- 0

	Si python("os.path.exist(ARCHIVO_CARRITO)") Entonces
		Escribir "Un archivo de carrito existe"
		Escribir "Gustas usar este archivo:"
		Leer usar
		Si usar = "n" Entonces
			archivo = python("open(ARCHIVO_CARRITO,w)")
			archivo = python("write(Producto,Precio,Cantidad)")
			archivo = python("close()")
		Fin Si
	SiNo
		archivo = python("open(ARCHIVO_CARRITO,w)")
		archivo = python("write(Producto,Precio,Cantidad)")
		archivo = python("close()")
	Fin Si

	Mientras opcion_menu_principal != 4 Hacer
		opcion_menu_principal = menu_principal()
	Fin Mientras
	
FinAlgoritmo
