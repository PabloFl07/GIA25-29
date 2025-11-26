lista =  [(), (), ('',) , ('a', 'b'), ('a', 'b', 'c'), ('d',)]
lista2 = []

"""
for t in lista:
    if t:  # Las tuplas vacías se evaluan como `False` y las no vacías como `True`
        lista2.append(t)
"""

for t in lista:
    if len(t) > 0:  # Si la longitud es mayor que 0
        lista2.append(t)


print(lista2)
