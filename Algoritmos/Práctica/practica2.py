import random
import time

# --------------- AUXILIARES ---------------


def aleatorio(n):
    return [random.randint(-n, n) for _ in range(n)]


def ascendente(n):
    return list(range(n))


def descendente(n):
    return list(range(n, 0, -1))


def is_ordenado(vector_ordenado, vector_original):
    return f"Ordenado: {vector_ordenado == sorted(vector_original)}"

def microsegundos():
    return time.perf_counter_ns() // 1000


# ------------------------------------------


def ord_insercion(vector):
    """
    Ordena un vector utilizando el algoritmo de ordenamiento por inserción.
    """
    n = len(vector)
    for i in range(1, n):
        x = vector[i]
        j = i - 1
        while j >= 0 and vector[j] > x:
            vector[j + 1] = vector[j]
            j -= 1
        vector[j + 1] = x
    return vector


def test():
    vectores = {
        "aleatorio": aleatorio(10),
        "ascendente": ascendente(10),
        "descendente": descendente(10)
    }

    for nombre, vector in vectores.items():
        print(f"Vector {nombre}:\t{vector}")
        print(f"Vector ordenado:\t{ord_insercion(vector.copy())}")
        print(is_ordenado(ord_insercion(vector.copy()), vector), "\n")


def ejecucion(algoritmo, vector):
    """
    Ejecución y cálculo de los microsegundos con un vector dado
    """
    t1 = microsegundos()
    algoritmo(vector)
    t2 = microsegundos()
    t = t2 - t1
    # Si el tiempo es menor a 1000 microsegundos
    if t < 1000: 
        t1 = microsegundos()
        for _ in range(1000):  # se repite la ejecución 1000 veces
            algoritmo(vector)
        t2 = microsegundos()
        t = (t2 - t1) / 1000  # se calcula el tiempo promedio
    return t

def mediciones():
    """
    Realiza todas las mediciones para cada algoritmo, mostrando los resultados
    """

    n = 1000
    # kt indica si se ha realizado el bucle de 1000 repeticiones
    print("\nMedición 'fib1'")

    t = ejecucion(ord_insercion, aleatorio(n))


    print(f"{n:12d}{t:15.4f}")





if __name__ == "__main__":
    test()
    mediciones()
