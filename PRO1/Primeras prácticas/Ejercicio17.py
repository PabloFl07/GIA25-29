
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

def sumar_matrices(matriz1, matriz2):
    matriz_suma = [ [0, 0], [0, 0] ]
    for i in range(2):
        for j in range(2):
            matriz_suma[i][j] = matriz1[i][j] + matriz2[i][j]
    return matriz_suma

rellenar_matriz(matriz_1)
rellenar_matriz(matriz_2)
matriz_suma = sumar_matrices(matriz_1, matriz_2)
print(f"{matriz_suma[0]}\n{matriz_suma[1]}")