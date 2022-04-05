f = open("demo3.txt", "w")
f.write("Hola como estas\n")
f.close()

f = open("demo3.txt","r")
print(f.read())
f.close()
