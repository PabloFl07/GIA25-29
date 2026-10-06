from Figuras import Circulo, Cuadrado, Rectangulo, Triangulo


if __name__ == "__main__":
    circulo = Circulo(4)

    rectangulo = Rectangulo(4, 2)

    cuadrado = Cuadrado(3)

    triangulo = Triangulo(2,5)

    figuras = [circulo, rectangulo, cuadrado, triangulo]

    total = 0
    for figura in figuras:
        total += figura.area()

    print(f"Suma de las areas: {total}")


