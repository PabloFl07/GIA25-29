from array import array

array = array("b")       # Creamos el array de tipo enteros

while len(array) < 10:   # Mientras el número de elementos sea < 10 , podemos seguir metiendo
    array.append(int(input("Número: ")))
print(array)