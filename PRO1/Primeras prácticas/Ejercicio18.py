
matriz_1 = [ 
    [ ],
    [ ]
]

matriz_2 = [ 
    [],
    []
]

def rellenar_matriz(matriz):
    for i in range(2):  # 2 filas
        while len(matriz[i]) < 2:
            matriz[i].append(int(input(f"Ingrese el valor para la fila {i+1}, columna {len(matriz[i])+1} de la matriz: ")))
    print("-------------------------Matriz 2------------------------")

def producto_matrices(matriz_1,matriz_2):
    matriz_producto = [
        [0, 0],
        [0, 0]
    ]
    for i in range(2): # Fila
        for j in range(2): # Columna
            matriz_producto[i][j] = matriz_1[i][0] * matriz_2[0][j] + matriz_1[i][1] * matriz_2[1][j]
    return matriz_producto


rellenar_matriz(matriz_1)
rellenar_matriz(matriz_2)
matriz_suma = producto_matrices(matriz_1, matriz_2)
print(f"{matriz_suma[0]}\n{matriz_suma[1]}")