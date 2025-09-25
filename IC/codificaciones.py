
from Decimal_binario import decimal_binario

def signo_magnitud(decimal, n_bits):
    upper_limit = 2**(n_bits - 1) - 1
    lower_limit = -2**(n_bits - 1) + 1

    rango = [x for x in range(lower_limit, upper_limit+1)]

    if decimal > 0:
        if decimal in rango:
            return decimal_binario(decimal).rjust(n_bits, '0')
        else:
            print(f"[!] El número {decimal} está fuera del rango para {n_bits} bits.")
            print(f"Rango válido: [{rango[0 ]} , {rango[-1]}]")
    else:
        if decimal in rango:
            return decimal_binario(abs(decimal)).rjust(n_bits - 1, '0').rjust(n_bits, '1') 
            # Transforma el número a positivo, lo convierte a binario,
            # Rellena con ceros a la izquierda para que ocupe n_bits - 1 bits, para dejar el último al signo
            # Finalmente, rellena con un 1 a la izquierda para indicar que es negativo
        else:
            print(f"[!] El número {decimal} está fuera del rango para {n_bits} bits.")
            print(f"Rango válido: [{rango[0 ]} , {rango[-1]}]")

def c_1(decimal,n_bits):
    upper_limit = 2**(n_bits - 1) - 1
    lower_limit = -2**(n_bits - 1) + 1

    rango = [x for x in range(lower_limit, upper_limit+1)]

    if decimal > 0:
        if decimal in rango:
            binario = decimal_binario(decimal).rjust(n_bits, '0')
            return binario
        else:
            print(f"[!] El número {decimal} está fuera del rango para {n_bits} bits.")
            print(f"Rango válido: [{rango[0 ]} , {rango[-1]}]")
    else:
        if decimal in rango:
            binario = decimal_binario(abs(decimal)).rjust(n_bits, '0')
            return ''.join('1' if bit == '0' else '0' for bit in binario)
            # Transforma el número a positivo, lo convierte a binario,
            # Rellena con ceros a la izquierda para que ocupe n_bits
            # SUstituye los 0 por 1
        else:
            print(f"[!] El número {decimal} está fuera del rango para {n_bits} bits.")
            print(f"Rango válido: [{rango[0 ]} , {rango[-1]}]")    

def c_2(decimal,n_bits):
    pass

if __name__ == "__main__":
    decimal = int(input("Número decimal: "))
    n_bits = int(input("Número de bits: "))
    print(f"Resultado: {c_1(decimal,n_bits)}")