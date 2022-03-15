Algoritmo tiendita_v1
	
	opcion_menu_principal <- 0
	opcion_menu_productos <- 0
	
	Mientras opcion_menu_principal != 4 Hacer
		Escribir " ------- Menu principal --------- "
		Escribir "1. Mostrar productos"
		Escribir "2. Mostrar carrito de compras"
		Escribir "3. Mostrar descuentos"
		Escribir "4. Salir"
		Escribir ""
		Escribir "Opcion:"
		Leer opcion_menu_principal
		
		Si opcion_menu_principal = 1 Entonces
			Mientras opcion_menu_productos != 4 Hacer
				Escribir " ------- Menu Productos --------- "
				Escribir "1. Ropa"
				Escribir "2. Accesorios"
				Escribir "3. Electrodomoesticos"
				Escribir "4. Salir"
				Escribir ""
				Escribir "Opcion:"
				Leer opcion_menu_productos
				
				Si opcion_menu_productos = 1 Entonces
					Escribir "Ropa"
				FinSi
				Si opcion_menu_productos = 2 Entonces
					Escribir "Accesorios"
				FinSi
				Si opcion_menu_productos = 3 Entonces
					Escribir "Eletrodomesticos"
				FinSi
			Fin Mientras
		FinSi
		Si opcion_menu_principal = 2 Entonces
			Escribir "Carrito de compras"
		FinSi
		Si opcion_menu_principal = 3 Entonces
			Escribir "Descuentos"
		FinSi
		
	Fin Mientras
	
FinAlgoritmo
