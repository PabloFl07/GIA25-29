#!/usr/bin/env python3

print("\n***************************************************")
print(" Comprobar que 0.2 + 0.1 != 0.3 en nuestro computador")
print("****************************************************\n")

a = 0.1
b = 0.2
c = 0.3

suma = a + b

if suma == c:
    print("LO QUE ESPERAMOS ES QUE:  0.1 + 0.2 == 0.3\n")
else:
    print("¡SORPRESA!    0.1 + 0.2 != 0.3\n")
    print("ya que 0.1 = %.20f,\n y por tanto la suma es %.20f\n" % (0.1, suma))

