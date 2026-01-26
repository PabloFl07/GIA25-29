n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

max = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3

print(f"El número {max} es el mayor de los tres")

