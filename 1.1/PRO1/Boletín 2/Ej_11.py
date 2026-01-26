n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))


if n1 == n2 == n3:
    print("El triángulo es equilátero")
elif n1 == n2:
    print(f"El triángulo es isósceles")
elif n1 == n3:
    print(f"El triángulo es isósceles")
elif n2 == n3:
    print(f"El triángulo es isósceles")
else:
    print("El triángulo es escaleno")