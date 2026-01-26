

# Una función recursiva que devuelva una cadena de texto con todos los números pares desde 0 hasta n separados por espacios.

def texto(n):
    if n == 0:
        return "0"                        # Caso base: cuando n sea 0, la función se cierra y devolvemos "0" | Se seguirán ejecutando las funciones previas
    if n%2 == 0:
        return texto(n-2) + " " + str(n)  # Si n es par, llamamos a la función con n-2 para obtener los siguientes pares y añadimos el actual
    else:
        return texto(n-1)+" "             #  Si n es impar, llamamos a la función con n-1 para llegar al par más cercano
    

print(texto(6))
