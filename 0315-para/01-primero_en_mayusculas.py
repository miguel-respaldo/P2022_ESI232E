frase = input("Escribe una frase: ")

frase_final = ""
mayusculas = True
for letra in frase:
   if mayusculas == True:
     frase_final += letra.upper()
   else:
     frase_final += letra.lower()
   if letra == " ":
       mayusculas = True
   else:
       mayusculas = False

print("En mayusculas:", frase_final)
print("en python", frase.title())