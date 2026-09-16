import time
import math


MAX_OVERFLOW = 2**31
PHI = (1 + math.sqrt(5)) / 2

def fib1(n):
    if n<2:
        return n
    else:
        return fib1(n-1) + fib1(n-2)



def fib2(n):
    i, j = 1, 0
    for _ in range(1, n+1):
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
    return time.perf_counter_ns()//1000


def test(*args):

    algoritmos = args
    secuencias = {}
    for alg in algoritmos:
        secuencias.update({alg.__name__ : [alg(i) for i in range(15)]})

    for alg, sec in secuencias.items():
        print(f"Secuencia de {alg}: {sec}")

    print(f"Comprobación 'fib1' con 'fib2': {secuencias['fib1'] == secuencias['fib2']}")
    print(f"Comprobación 'fib1' con 'fib3': {secuencias['fib1'] == secuencias['fib3']}")
    print(f"Comprobación 'fib2' con 'fib3': {secuencias['fib2'] == secuencias['fib3']}")


def ejecucion(algoritmo, v):
    t1 = microsegundos()
    algoritmo(v)
    t2 = microsegundos()
    t = t2-t1
    return t

def mediciones():
    valores = (2, 4, 8, 16, 32)
    valores2 = (1000, 10_000, 100_000, 1_000_000, 10_000_000 )

    print("Medición 'fib1'")
    for n in valores:
        t = ejecucion(fib1, n)
        x = t / math.pow(1.1, n)
        y = t / (PHI**n)
        z = t / math.pow(2, n)

        print(f"{n:12d}{t:15.4f}{x:15.8f}{y:15.8f}{z:15.8f}")

    print("Medición 'fib2'")
    for n in valores2:
        t = ejecucion(fib2, n)
        x = t / math.pow(n, 0.8)
        y = t / n
        z = t / (n*math.log(n))

        print(f"{n:12d}{t:15.4f}{x:15.8f}{y:15.8f}{z:15.8f}")


    print("Medición 'fib3'")
    for n in valores2:
        t = ejecucion(fib3, n)
        x = t / math.sqrt(math.log(n)) 
        y = t / math.log(n)           
        z = t / math.pow(n, 0.5) 

        print(f"{n:12d}{t:15.4f}{x:15.8f}{y:15.8f}{z:15.8f}")           



if __name__ == "__main__":
    mediciones()






