#!/usr/bin/env python3



# La operación de la derecha es más rápida y precisa porque hace 2 sumas y un producto.

print("\n***************************************************")
print("Resolver (x² - y²) = (x + y)(x - y) con la mayor precisión")
print("***************************************************\n")

x = 1.023841858
print("x = %.10f" % x)
y = 1.011920929
print("y = %.10f\n" % y)

x2 = x * x
y2 = y * y

e1 = x2 - y2
print(f"(x² - y²) = {e1:.10f} (con 10 decimales) o {e1:.20f} (con 20 decimales)\n" )

s = x + y
d = x - y

e2 = s * d
print("(x + y)(x - y) = %.10f (con 10 decimales) o %.20f (con 20 decimales)\n" % (e2, e2))
