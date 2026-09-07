matriz = [[1 , 2], [3 , 4]]


def crear_padding(matriz, padding=0):
    matriz2 = [fila.copy() for fila in matriz ]

    fila_ceros = [0] * (len(matriz) + 2 * padding)

    for _ in range(padding):
        for f in matriz2:
            f.append(0)
            f.insert(0,0)

    for _ in range(padding): # Tenemos que esperar a añadir el relleno a las filas ya existente porque si no entra en conflicto
        matriz2.insert(0,fila_ceros)
        matriz2.append(fila_ceros)

    return matriz2


def main():
    matriz = [[1 , 2], [3 , 4]]
    padding = int(input("Padding: "))

    matriz2 = crear_padding(matriz, padding)

    print("Matriz original: ")
    for f in matriz:
        print(f)

    print("Matriz con padding: ")
    for f2 in matriz2:
        print(f2)
    

    
        

if __name__ == "__main__":
    main()