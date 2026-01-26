def calcular_promedio_horas(lista_estudiantes: list):
    suma = 0
    c = 0
    for i in lista_estudiantes:
        for v in i.values():
            suma += sum(v)
            c += len(v)

    promedio = suma / c
    return promedio


def main():
    lista = [{"ana": [ 2 , 1.5 , 0]} , { "juan": [ 1 , 0 , 3]} ]

    for f in lista:
        print(f)

    print(f"Promedio de horas estudiadas: {calcular_promedio_horas(lista)}")


if __name__ == "__main__":
    main()