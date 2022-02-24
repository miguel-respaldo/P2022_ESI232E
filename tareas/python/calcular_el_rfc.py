nombre = input("Escribe tu nombre: ")
apellido_paterno = input("Escribe tu apellido paterno: ")
apellido_materno = input("Escribe tu apellido materno: ")
dia = eval(input("Escribe tu dia de nacimiento: "))
mes = eval(input("Escribe tu mes de nacimiento: "))
anio = eval(input("Escribe tu año de nacimiento: "))

RFC = apellido_paterno[:2].upper() + apellido_materno[0].upper() + nombre[0].upper()

if anio > 1000:
    RFC = RFC + str(anio)[2:]
else:
    RFC = RFC + str(anio)

if mes < 10:
    RFC = RFC + "0" + str(mes)
else:
    RFC = RFC + str(mes)

if dia < 10:
    RFC = RFC + "0" + str(dia)
else:
    RFC = RFC + str(dia)

print("El RFC es:", RFC)