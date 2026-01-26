lista = [ "p", "q" ]

n = 5

lista2 = []
for n in range(n):
    lista2.append( lista[0] + str(n + 1))
    lista2.append( lista[1] + str(n + 1))


print(lista2)