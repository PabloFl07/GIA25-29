


def binario_a_decimal(binario: str) -> int:
    return sum(int(bit) * 2**i for i, bit in enumerate(reversed(binario)))



if __name__ == "__main__":
    binario = input("[2] Número en binario: ")
    decimal = binario_a_decimal(binario)
    print(f"\n[10] Número en decimal: {decimal}")


