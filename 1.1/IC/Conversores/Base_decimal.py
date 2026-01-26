from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
    print("\n[!] Saliendo...")
    exit(0)
signal(SIGINT, handler)

def hex_decimal(hexadecimal: str) -> int:
    equivalencias = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    decimal = 0
    for i, digito in enumerate(reversed(hexadecimal)):
        if digito.isdigit():
            decimal += int(digito) * (16 ** i)
        elif digito.upper() in equivalencias:
            decimal += equivalencias[digito.upper()] * (16 ** i)
        else:
            raise ValueError(f"Dígito inválido en hexadecimal: {digito}")
    return decimal

def binario_decimal(original: str) -> int:
    return sum(int(bit) * 2**i for i, bit in enumerate(reversed(original)))

def base_decimal(original: str, base: int) -> int:
    match base:
        case 2: return binario_decimal(original)
        case 10: return int(original)
        case 16: return hex_decimal(original)
    return sum(int(digito) * base**i for i, digito in enumerate(reversed(original)))


def main():
    while True:
        base = int(input("Base del número (1 - 16): "))
        if base < 1 or base > 16:
            print("[!] Base inválida. Intente de nuevo.")
            continue
        num = input(f"[{base}] Número en base {base}: ")
        print(f"\n[10] Número en decimal: {base_decimal(num, base)}")

if __name__ == "__main__":
    main()


