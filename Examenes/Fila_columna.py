def eliminar_fila_columna(matriz, fila_idx, columna_idx):
    matriz2 = [fila.copy() for fila in matriz]


    if fila_idx not in range(len(matriz)) or columna_idx not in range(len(matriz[0])):
        return 
    
    matriz2.pop(fila_idx)

    for fila in matriz2:
        fila.pop(columna_idx)

    return matriz2

def main():
    matriz = [
        [1 ,2 ,3 ],
        [ 4 ,5 , 6],
        [7 , 8 , 9]
    ]


    fila = int(input("Fila a eliminar (índice): "))
    columna = int(input("Columna a eliminar(índice): "))

    matriz2 = eliminar_fila_columna(matriz, fila, columna)

    if matriz2 is not None:

        print("Matriz original: ")
        for f in matriz:
            print(f)

        print(f"Matriz después de eliminar fila {fila} y columna {columna}")
        for f2 in matriz2:
            print(f2)    
    else:
        print("Índices incorrectos")



if __name__ == "__main__":
    main()