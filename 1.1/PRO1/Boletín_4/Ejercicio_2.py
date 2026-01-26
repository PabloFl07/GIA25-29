from array import array

array = array("f")       # Creamos el array de tipo enteros


def rsum(array, summ = 0):  # Opción sin función `sum`
    for i in array:
        summ += i
    return summ

lenght = int(input("Cuantos número vas a introducir? ( < 30 ): "))

while len(array) < lenght:   # Mientras el número de elementos sea < 10 , podemos seguir metiendo
    array.append(int(input("Número: ")))

print(sum(array))
print(rsum(array))

