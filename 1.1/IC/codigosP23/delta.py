#!/usr/bin/env python3

print("\n************************************************")
print("Resolver x = 1.0 + sumatorio de deltas pequeños")
print("************************************************\n")

print("\n******************************************************************")
print("Si delta es tan pequeño como 2^(-53) su valor se pierde en la suma")
print("*******************************************************************\n")

pow20 = 1 << 20
pow53 = 1 << 53

x = 1.0
delta = 1.0 / pow53
for i in range(pow20):
    x = x + delta

x2 = 1.0 + (1.0 / (1 << 33))
print("Esperamos que x sea: %.15f\n" % x2)
print("Sin embargo es: %.15f\n" % x)

print("\n************************************************************")
print("Si sumamos el 1.0 al final de todo, se acaba el problema")
print("************************************************************\n")

x = 0.0
delta = 1.0 / pow53
for i in range(pow20):
    x = x + delta
x = x + 1.0

x2 = 1.0 + (1.0 / (1 << 33))
print("Esperamos que x sea: %.15f\n" % x2)
print("Y efectivamente es: %.15f\n" % x)

