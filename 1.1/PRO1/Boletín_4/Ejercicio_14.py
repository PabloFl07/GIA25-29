lista = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

elemento= 100

#[(10, 20, 100), (40, 50, 100), (70, 80, 100)]

for i in range(len(lista)):
    lista[i] = list(lista[i])
    lista[i][2] = elemento
    lista[i] = tuple(lista[i])
    

print(lista)