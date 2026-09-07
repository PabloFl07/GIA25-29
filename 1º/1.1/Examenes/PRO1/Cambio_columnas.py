def intercambiar_columnas(matriz, columna1_idx, columna2_idx):
    matriz2 = [fila.copy() for fila in matriz]

    if columna1_idx not in range(len(matriz)) or columna2_idx not in range(len(matriz)):
        return None
    
    for f in matriz2:
        temp = f[columna1_idx]
        f[columna1_idx] = f[columna2_idx]
        f[columna2_idx] = temp

    return matriz2

def main():
    matriz = []
    n = int(input("Introduce el rango de la matriz: "))
    for i in range(n):
        fila = []
        while len(fila) < n:
            fila.append(int(input(f"Valor de la fila {i}, posición {len(fila)}: ")))
        matriz.append(fila)

    columna1_idx = int(input("Intercambiar columna (índice): "))
    columna2_idx = int(input("Por la columna (índice): "))

    matriz2 = intercambiar_columnas(matriz, columna1_idx, columna2_idx)
    if matriz2 is not None:
        print("Matriz original:")
        for fila in matriz:
            print(fila)
        print(f"Matriz tras intercambiar las columnas {columna1_idx+1} y {columna2_idx+1}:")
        for fila2 in matriz2:
            print(fila2)
    else:
        print("[!] Índices incorrectos")
        
if __name__ == "__main__":
    main()
