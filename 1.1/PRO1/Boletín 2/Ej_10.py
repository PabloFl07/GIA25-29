n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

# Esto es una mierda, hay una función específica para ordenar elementos

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(f"Cociente: {n1 / n3} - resto: {n1 % n3}") if n3 !=0 else print("Error al dividir entre 0")
    else:
        print(f"Cociente: {n1 / n2} - resto: {n1 % n2}") if n2 !=0 else print("Error al dividir entre 0")
elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print(f"Cociente: {n2 / n3} - resto: {n2 % n3}") if n3 !=0 else print("Error al dividir entre 0")
    else:
        print(f"Cociente: {n2 / n1} - resto: {n2 % n1}") if n1 !=0 else print("Error al dividir entre 0")
else:
    if n1 >= n2:
        print(f"Cociente: {n3 / n2} - resto: {n3 % n2}") if n2 !=0 else print("Error al dividir entre 0")
    else:
        print(f"Cociente: {n3 / n1} - resto: {n3 % n1}") if n1 !=0 else print("Error al dividir entre 0")