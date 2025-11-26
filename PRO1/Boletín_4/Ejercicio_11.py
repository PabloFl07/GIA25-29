lista =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

n = 5

def split_lista(lista, n):
    lista2 = []  # Lista auxiliar
    for i in range(0, len(lista), n):  # 
        bloque = lista[i:i+n]  # Bloque es una lista que contiene desde los elementos [0:n] [n:2n] [2n:3n]
        lista2.append(bloque)  # Memos el bloque en la lista auxiliar
    return lista2



print(lista)
print(split_lista(lista,n))

