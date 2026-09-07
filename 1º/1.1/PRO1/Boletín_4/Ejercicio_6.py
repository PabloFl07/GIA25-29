frase = str(input("Frase: "))
palabras = frase.split(" ")    # Dividimos es string frase en strings, separadas por " "


max = palabras[0] # Base de la comparación

for i in range(len(palabras)):
    if len(palabras[i]) > len(max):
        max = palabras[i]

print(max)