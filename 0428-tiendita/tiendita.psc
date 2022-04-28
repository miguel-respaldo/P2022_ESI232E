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

Funcion carrito_agregar (producto, cantidad)
	archivo_prod <- python("open(ARCHIVO_PRODUCTOS, r)")
	archivo_carr <- python("open(ARCHIVO_CARRITO, a)")

	Para linea<-1 Hasta 3 Hacer
		lista <- python("liena.split")
		Si producto = python("lista[1].lower()") Entonces
			archivo_carr <- python("write(lista[1], lista[2], cantidad)")
		Fin Si
	Fin Para

	archivo_prod <- python("close()")
	archivo_carr <- python("close()")
Fin Funcion

Funcion carrito_agregar_oferta (producto, cantidad)
	archivo_prod <- python("open(ARCHIVO_PRODUCTOS, r)")
	archivo_carr <- python("open(ARCHIVO_CARRITO, a)")

	archivo_prod <- python("close()")
	archivo_carr <- python("close()")
Fin Funcion

Funcion carrito_mostrar ()
	archivo <- python("open(ARCHIVO_CARRITO, r)")

	archivo <- python("close()")
Fin Funcion

Funcion producto_mostrar (la_categoria)
	archivo <- python("open(ARCHIVO_CARRITO, r)")

	archivo <- python("close()")
Fin Funcion

Funcion producto_mostrar_ofertas ()
	archivo <- python("open(ARCHIVO_CARRITO, r)")

	archivo <- python("close()")
Fin Funcion

Algoritmo tiendita

	opcion_menu_principal <- 0

	Si python("os.path.exist(ARCHIVO_CARRITO)") Entonces
		Escribir "Un archivo de carrito existe"
		Escribir "Gustas usar este archivo:"
		Leer usar
		Si usar = "n" Entonces
			archivo <- python("open(ARCHIVO_CARRITO,w)")
			archivo <- python("write(Producto,Precio,Cantidad)")
			archivo <- python("close()")
		Fin Si
	SiNo
		archivo <- python("open(ARCHIVO_CARRITO,w)")
		archivo <- python("write(Producto,Precio,Cantidad)")
		archivo <- python("close()")
	Fin Si

	Mientras opcion_menu_principal <> 4 Hacer
		opcion_menu_principal = menu_principal()
		Si opcion_menu_principal = 1  Entonces
			opcion_menu_productos <- 0
			opcion_menu_productos = menu_productos()
			Segun opcion_menu_productos Hacer
				1:
					producto_mostrar("botanas")
				2:
					producto_mostrar("refresco")
				3:
					producto_mostrar("bebidas")
				4:
					producto_mostrar("lacteos")
				5:
					Escribir "Salir del menu"
				De Otro Modo:
					Escribir "--------------------------"
					Escribir "| Error: Opcion invalida |"
					Escribir "--------------------------"
			Fin Segun
		Fin Si
		Si opcion_menu_principal = 2  Entonces
			carrito_mostrar()
		Fin Si
		Si opcion_menu_principal = 3  Entonces
			producto_mostrar_ofertas()
		Fin Si
		Si opcion_menu_principal < 1 o opcion_menu_principal > 4  Entonces
			Escribir "--------------------------"
			Escribir "| Error: Opcion invalida |"
			Escribir "--------------------------"
		Fin Si
	Fin Mientras
FinAlgoritmo
