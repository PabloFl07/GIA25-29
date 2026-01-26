def ident(n):
    matriz = [ ]
    for i in range(n):
        fila = [0] * n
        #fila = list(0 for n in range(n))
        fila[i] = 1
        matriz.append(fila)
    print(matriz)

ident(4)


def ident_2(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]


ident_2(4)