
def decimal_binario(decimal: int) -> str:
    bits = []
    while decimal > 0:
        bits.append(str(decimal % 2))
        decimal //= 2
    return "".join(reversed(bits)) if bits else "0"



if __name__ == "__main__":
    while True:
        decimal = int(input("[10] Número en decimal: "))
        binario = decimal_binario(decimal)
        print(f"\n[2] Número en binario: {binario}")