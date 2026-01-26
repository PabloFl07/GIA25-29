lista = [ 1 , 2 , 4 , 5 , 6 , 7 , 9 , 12 , 2 , 3 , 45 , 5, 6 , 2, 3 , 4 , 5 ]

n = int(input("Número: "))


lista3 = []
for i in lista:
    if i > n and i not in lista3:  # Evitamos meter duplicados
        lista3.append(i)


print(lista3)

"""
lista2 = [lista[i] for i in range(len(lista)) if lista[i] > n]
print(lista2)
"""
