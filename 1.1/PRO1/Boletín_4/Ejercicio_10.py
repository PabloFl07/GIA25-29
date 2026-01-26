lista = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]

elemento = "q"

i = 0
while i < len(lista):  # Al usar un bucle podemos controlar cuanto le sumamos al índice
# Al añadir un elemento a la lista, los índices siguientes se modifican ( se les suma 1 ) por eso cada iteración debe ir de 2 en 2.
    lista.insert(i , elemento)
    i += 2


print(lista)