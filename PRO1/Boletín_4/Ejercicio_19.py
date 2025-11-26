frase = input("Frase: ")

palabras = frase.split(" ")
palabras2 = []

# Creamos una lista auxiliar para almacenar cada palabra individualmente para que count no devuelva el mismo resultado para las palabras repetidas
for i in palabras:
    if i not in palabras2:
        palabras2.append(i) 

for i in palabras2:
    print(f"{i} : {palabras.count(i)}")