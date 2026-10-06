import time
import math

MAX_OVERFLOW = 2**31
PHI = (1 + math.sqrt(5)) / 2


def fib1(n):
    if n < 2:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


# Para cada operación de estas dos implementaciones aplicamos el módulo 2³¹
# para no superar los 32 bits en los enteros
def fib2(n):
    i, j = 1, 0
    for _ in range(1, n + 1):
        j += i % MAX_OVERFLOW
        i = (j - i) % MAX_OVERFLOW
    return j


def fib3(n):
    i, j, k, h, t = 1, 0, 0, 1, 0

    while n > 0:
        if n % 2 != 0:
            t = (j * h) % MAX_OVERFLOW
            j = (i * h + j * k + t) % MAX_OVERFLOW
            i = (i * k + t) % MAX_OVERFLOW

        t = (h**2) % MAX_OVERFLOW
        h = (2 * k * h + t) % MAX_OVERFLOW
        k = (k**2 + t) % MAX_OVERFLOW
        n = (n // 2) % MAX_OVERFLOW

    return j


def microsegundos():
    return time.perf_counter_ns() // 1000


def test(*args):
    """
    Test que muestra los primeros 15 números de las secuencias calculadas
    y las comprueba lógicamente
    """
    print("Ejecución de test:")
    algoritmos = args
    secuencias = {}
    for alg in algoritmos:
        secuencias.update({alg.__name__: [alg(i) for i in range(15)]})

    for alg, sec in secuencias.items():
        print(f"Secuencia de {alg}: {sec}")

    print(f"'fib1' con 'fib2': {secuencias['fib1'] == secuencias['fib2']}")
    print(f"'fib1' con 'fib3': {secuencias['fib1'] == secuencias['fib3']}")
    print(f"'fib2' con 'fib3': {secuencias['fib2'] == secuencias['fib3']}")


def ejecucion(algoritmo, n):
    """
    Ejecución y cálculo de los microsegundos con un n dado
    """
    t1 = microsegundos()
    algoritmo(n)
    t2 = microsegundos()
    t = t2 - t1
    # Si el tiempo es menor a 1000 microsegundos
    if t < 1000: 
        t1 = microsegundos()
        for _ in range(1000):  # se repite la ejecución 1000 veces
            algoritmo(n)
        t2 = microsegundos()
        t = (t2 - t1) / 1000   # y se calcula el promedio
        return t, True
    return t, False


def mediciones():
    """
    Realiza todas las mediciones para cada algoritmo, mostrando los resultados
    """
    valores = (2, 4, 8, 16, 32)
    valores2 = (1000, 10_000, 100_000, 1_000_000, 10_000_000)
    print(
        "\n",
        "\t" * 2,
        "VALOR".center(10),
        "COTA SUBESTIMADA".center(16),
        "COTA AJUSTADA".center(16),
        "COTA SOBREESTIMADA".center(16),
        end="",
    )

    # kt indica si se ha realizado el bucle de 1000 repeticiones
    print("\nMedición 'fib1'")
    for n in valores:
        t, kt = ejecucion(fib1, n)
        x = t / math.pow(1.1, n)
        y = t / (PHI**n)
        z = t / math.pow(2, n)
        marca = "*" if kt else " "
        print(f"{n:12d}{t:15.4f}{marca}{x:15.8f}{y:15.8f}{z:15.8f}")

    print("Medición 'fib2'")
    for n in valores2:
        t, kt = ejecucion(fib2, n)
        x = t / math.pow(n, 0.8)
        y = t / n
        z = t / (n * math.log(n))
        print(f"{n:12d}{t:15.4f}{marca}{x:15.8f}{y:15.8f}{z:15.8f}")

    print("Medición 'fib3'")
    for n in valores2:
        t, kt = ejecucion(fib3, n)
        x = t / math.sqrt(math.log(n))
        y = t / math.log2(n)
        z = t / math.pow(n, 0.5)
        print(f"{n:12d}{t:15.4f}{marca}{x:15.8f}{y:15.8f}{z:15.8f}")


if __name__ == "__main__":
    test(fib1, fib2, fib3)
    for _ in range(3):
        mediciones()
