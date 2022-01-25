Funcion python(nombre_funcion)
	Escribir 'Funcion de Python(',nombre_funcion,')'
FinFuncion

Funcion op_menu <- menu ()
	Escribir '---------------------'
	Escribir '1. Mostrar productos'
	Escribir '2. Mostrar carrito'
	Escribir '3. Agregar al carrito'
	Escribir '...'
	Escribir '6. Salir'
	Escribir ' Opcion: ' Sin Saltar
	Leer op_menu
FinFuncion

Funcion mostrar_productos (l_productos,l_precios)
	python('open')
	python('cvs.reader')
	tamano <- 5
	Escribir 'No.    Nombre     Precio'
	Para i<-1 Hasta tamano Hacer
		python('lector')
	FinPara
FinFuncion

Funcion mostrar_carrito (l_productos,l_precios,c_producto,c_cantidad)
	Escribir '--------  Carrito  ----------'
	Escribir 'No.    Nombre     Precio    Cantidad'
	Para i<-1 Hasta cantidad Hacer
		Escribir i,'   ',l_productos[c_producto[i]],'      ',l_precios[c_producto[i]],'   ',c_cantidad[i]
	FinPara
FinFuncion

Funcion agregar_carrito(l_productos,l_precios,c_producto,c_cantidad,cant)
	mostrar_productos(l_productos,l_precios)
	Escribir '-----------------------------'
	Escribir 'Ingresa el número de producto: ' Sin Saltar
	Leer num_producto
	Escribir 'Cuantos articulos quieres de este producto ' Sin Saltar
	Leer cant_producto
	Si num_producto>tamano Entonces
		Escribir 'No existe el producto'
	SiNo
		cant <- cant+1
		c_producto[cant] <- num_producto
		c_cantidad[cant] <- cant_producto
	FinSi
FinFuncion

Algoritmo tiendita
	Dimension lista_productos[5]
	Dimension lista_precios[5]
	Dimension carrito_producto[10]
	Dimension carrito_cantidad[10]
	cantidad <- 0
	lista_productos[1] <- 'papas'
	lista_productos[2] <- 'refrescos'
	lista_productos[3] <- 'tortillas'
	lista_productos[4] <- 'jamon'
	lista_productos[5] <- 'mazapan'
	lista_precios[1] <- 12.0
	lista_precios[2] <- 10.5
	lista_precios[3] <- 20.0
	lista_precios[4] <- 40.0
	lista_precios[5] <- 5.0
	opcion_menu <- 0
	Mientras opcion_menu<>6 Hacer
		opncion_menu <- menu()
		Segun opcion_menu  Hacer
			1:
				mostrar_productos(lista_productos,lista_precios)
			2:
				mostrar_carrito(lista_productos,lista_precios,carrito_producto,carrito_cantidad)
			3:
				agregar_carrito(lista_productos,lista_precios,carrito_producto,carrito_cantidad,cantidad)
			6:
				Escribir 'Gracias por usar el programa'
			De Otro Modo:
				Escribir 'La opcion no existe'
		FinSegun
	FinMientras
FinAlgoritmo
