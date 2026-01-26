#!/usr/bin/env python3

import time

inicio = time.perf_counter()





print("\n************************************************")
print("Error cometido al operar con el flotante 0.1")
print("************************************************\n")

suma = 0.0
for i in range(10_000_000):
    suma = suma + 0.1
error = 10_000_000 / 10 - suma

print("\n***********************************************************************")
print("Sumándolo 10 millones de veces, el error absoluto cometido es: %.6f" % error)
print("***********************************************************************\n")

suma = 0.0
for i in range(100_000_000):
    suma = suma + 0.1
error2 = 100_000_000 / 10 - suma

print("\n************************************************************************")
print("Sumándolo 100 millones de veces, el error absoluto cometido es: %.6f" % error2)
print("************************************************************************\n")

fin = time.perf_counter()
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")