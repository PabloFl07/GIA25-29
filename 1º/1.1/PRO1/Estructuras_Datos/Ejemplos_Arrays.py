
from array import array

ar = array('i', [1, 2, 2, 4, 2])


def elim(ar, v ):
    for i in range(len(ar)):
        if ar[i] == v:  # Comparamos cada elemento del array con el valor a eliminar
            del ar[i]
            return ar  # Con el return nos aseguramos de que, si el valor no está en el array, se imprime el mensaje, y si está, no se imprime ( A diferenccia de si usamos un break)
    print("No se ha encontrado el valor")

#print(elim(ar,3))

#ar = array('i', [1, 2, 3, 4, 5])

def elim_mejor(ar, v):
    if v in ar:
        for i in range(len(ar)):
            if ar[i] == v:  # Comparamos cada elemento del array con el valor a eliminar
                del ar[i]
                return ar  # Con el return nos aseguramos de que, si el valor no está en el array, se imprime el mensaje, y si está, no se imprime ( A diferenccia de si usamos un break)
    return "No se ha encontrado el valor"

#print(elim_mejor(ar, 3))



def elim_todos(ar,v):
    if v in ar:
        return [ x for x in ar if x != v]
    else:
        return "No se ha encontrado el valor"

print(elim_todos(ar, 2))