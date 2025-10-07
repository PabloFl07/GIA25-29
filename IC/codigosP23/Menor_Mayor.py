#!/usr/bin/env python3

print("\n****************************************************")
print("Resolver la suma de una serie con la mayor precisión")
print("****************************************************\n")

serie = [j for j in range(10)]

for j in range(10):
    serie.append(1.0 / (2.5 ** j))

serie.sort()
print("**** La serie ordenada de menor a mayor es: ****")
print(serie)

suma = 0.0
for i in range(20):
    suma +=  serie[i]

print("\nSumando de menor a mayor: %.12f (con 12 decimales) o %.20f (con 20 decimales)" % (suma, suma))

suma2 = 0.0
for i in range(20):
    suma2 += serie[-(1 + i)]

print("\nSumando de mayor a menor: %.12f (con 12 decimales) o %.20f (con 20 decimales)\n" % (suma2, suma2))

