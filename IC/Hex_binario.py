equivalencias = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def hex_binario(hexadecimal: str) -> str:
    for digito in hexadecimal:
        if digito.upper() not in equivalencias:
            raise ValueError(f"Dígito inválido en hexadecimal: {digito}")
        elif digito.upper() in equivalencias:
            return ''.join(equivalencias[digito.upper()] for digito in hexadecimal)

if __name__ == "__main__":
    hexadecimal = input("[16] Número en hexadecimal: ")
    binario = hex_binario(hexadecimal)
    print(f"\n[2] Número en binario: {binario}")