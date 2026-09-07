def power(x : int , n : int) -> float:
    if n == 0:
        return 1.0                  # Escribirmos el caso base como float para que el resultado lo sea
    elif n < 0:
        return  1 / power(x , -n)   # Si el exponente es negativo, calculamos la potencia 1/|n|
    else:
        return x * power(x ,n-1)    # Si el exponente es positivo, multiplicamos x por x⁽ⁿ⁻¹⁾ , reduciendo n en 1 cada vez hasta llegar a 0.
    
def fact(k):
    if k ==0 or k== 1:
        return 1
    else:
        return k * fact(k-1)