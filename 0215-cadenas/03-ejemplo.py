txt = "La casa es de color azul"
palabras = len(txt.split(" "))
print("La cadena tiene ", palabras, "palabras")

sin_espacios = txt.replace(" ","")
print(sin_espacios)
print(len(sin_espacios))