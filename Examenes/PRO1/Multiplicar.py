# -*- coding: utf-8 -*-
"""
Pablo Fernández Lema
"""
def multiplicar_matriz_vector(matriz, vector):
    if len(matriz[0]) != len(vector):
        return None
        
    resultado = [0] * len(matriz)
        
    for f in range(len(matriz)):
        for c in range(len(vector)):
            resultado[f] += matriz[f][c] * vector[c]
           
    return resultado

def main():
    matriz = [
        [1 , 2 ,3],
        [4 , 5 ,6]
        ]
    
    # Pedimos el vector
    vector = []
    dim = int(input("Número de componentes del vector: "))
    while len(vector) < dim:
        vector.append(int(input("Introduce una componente: ")))
        
        
    resultado = multiplicar_matriz_vector(matriz, vector)
    
    if resultado is not None:
        print("\nMatriz :")
        for f in matriz:
            print(f)
        print(f"\nVector:\n{vector}\n")
        print(f"Resultado de la multiplicación:\n{resultado}")
        
    else: 
        print("\n! No se puede realizar la multiplicación: Las dimensiones son incompatibles")
        
        
if __name__ == "__main__":
    main()