 

lista = [ 8, 1 , 2 , 3 , 5 , 2 , 4 , 2 , 1 , 2 , 7]
elementos = [ ]

for i in range(len(lista)):
    if lista[i] not in elementos:   # Añadimos cada elemento de la lista a una nueva lista vacía si en esta aún no está
        elementos.append(lista[i])

print(elementos)