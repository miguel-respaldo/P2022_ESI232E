f = open("demo2.txt", "a")
f.write("Hola como estas\n")
f.close()

f = open("demo2.txt","r")
print(f.read())
f.close()