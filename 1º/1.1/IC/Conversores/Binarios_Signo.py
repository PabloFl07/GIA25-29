from Decimal_binario import decimal_binario

def signo_magnitud(decimal, n_bits):
    upper_limit = 2**(n_bits - 1) - 1
    lower_limit = -2**(n_bits - 1)
    rango = [x for x in range(lower_limit, upper_limit + 1)]

    if decimal not in rango:
        print(f"[!] El número {decimal} está fuera del rango para {n_bits} bits.")
        print(f"Rango válido: [{rango[0]}, {rango[-1]}]")
        return None

    if decimal >= 0:
        return decimal_binario(decimal).rjust(n_bits, '0')
    else:
        return decimal_binario(abs(decimal)).rjust(n_bits - 1, '0').rjust(n_bits, '1')


def c_1(decimal, n_bits):
    upper_limit = 2**(n_bits - 1) - 1
    lower_limit = -2**(n_bits - 1)
    rango = [x for x in range(lower_limit, upper_limit + 1)]

    if decimal not in rango:
        print(f"[!] El número {decimal} está fuera del rango para {n_bits} bits.")
        print(f"Rango válido: [{rango[0]}, {rango[-1]}]")
        return None

    binario = decimal_binario(abs(decimal)).rjust(n_bits, '0')

    if decimal >= 0:
        return binario
    else:
        return ''.join('1' if bit == '0' else '0' for bit in binario)


def c_2(decimal, n_bits):
    upper_limit = 2**(n_bits - 1) - 1
    lower_limit = -2**(n_bits - 1)

    if decimal < lower_limit or decimal > upper_limit:
        print(f"[!] El número {decimal} está fuera del rango para {n_bits} bits.")
        print(f"Rango válido: [{lower_limit}, {upper_limit}]")
        return None

    if decimal >= 0:
        return format(decimal, f'0{n_bits}b')
    else:
        return format((1 << n_bits) + decimal, f'0{n_bits}b')


def decimal_cod(decimal, n_bits, cod):
    match int(cod):
        case 1: return signo_magnitud(decimal, n_bits)
        case 2: return c_1(decimal, n_bits)
        case 3: return c_2(decimal, n_bits)
        case _: return "[!] Código de método no válido."


def main():
    decimal = int(input('|------------------------------------------------------|\n\t[10] Número decimal a codificar: '))
    n_bits = int(input("\t[n] Número de bits: "))
    print('|------------------------------------------------------|')
    cod = int(input("ELIGE EL MÉTODO DE CODIFICACIÓN\n1. Signo-Magnitud\n2. Complemento a-1\n3. Complemento a-2\n>> "))
    print(f"--------------------------------------------------------\n[{cod}] Resultado en binario: {decimal_cod(decimal, n_bits, cod)}")


if __name__ == "__main__":
    main()
