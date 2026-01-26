
lista = [ 2 , 3, 5, 6, 1, 23, 3, 6, 2, 3, 5, 2]


def rsum(array, summ = 0):  # Opción sin función `sum`
    for i in array:
        summ += i
    return summ

print(rsum(lista))