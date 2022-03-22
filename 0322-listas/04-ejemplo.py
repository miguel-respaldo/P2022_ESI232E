frutas = ["manzana", "plátano", "naranja"]

print("len(frutas) =",len(frutas))

for i in range( len( frutas)):
    print( frutas[i] )

print("----------------")
i=0
while i < len(frutas):
    print(frutas[i])
    i = i + 1
    # i += 1
print("----------------")

[print(x) for x in frutas]