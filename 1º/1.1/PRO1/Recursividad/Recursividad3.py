

def linea(n: int, c= "x"):  # Función que imprime una linea de n caracteres.
    if n == 0:
        print()
        return
    print(c , end="")
    linea(n-1, c)

def rec(m , n , c="x",):
    if m == 0 :
        return
    linea(n,c)
    rec(m-1 , n, c)

        
rec(3, 5)

