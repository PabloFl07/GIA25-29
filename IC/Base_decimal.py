from signal import signal, SIGINT
from sys import exit
from fractions import Fraction

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

def pd_decimal_binario(parte_decimal: float, max_bits: int = 50) -> str:
    """
    Versión con Fraction: usa fracciones exactas para evitar problemas de precisión
    
    Args:
        parte_decimal: La parte decimal del número (debe ser 0 <= x < 1)
        max_bits: Número máximo de bits a generar como medida de seguridad
    
    Returns:
        String con la representación binaria. Si hay ciclo, se muestra como "bits(ciclo)"
    """
    # Convertir float a fracción exacta
    # limit_denominator() encuentra la fracción más simple que representa el float
    # Esto elimina los problemas de precisión de punto flotante
    frac = Fraction(parte_decimal).limit_denominator()
    
    bits = []  # Lista para almacenar los bits resultantes
    seen = {}  # Diccionario: fracción_como_string -> posición donde la vimos
    position = 0  # Posición actual en la secuencia de bits
    
    while frac > 0 and position < max_bits:
        # Crear clave única para esta fracción
        # Usamos "numerador/denominador" como identificador único
        frac_str = f"{frac.numerator}/{frac.denominator}"
        
        # ¿Ya vimos esta fracción antes?
        if frac_str in seen:
            # ¡Encontramos un ciclo! La fracción se repite
            cycle_start = seen[frac_str]  # Posición donde empezó el ciclo
            
            # Separar la parte antes del ciclo y el ciclo mismo
            pre_cycle = "".join(bits[:cycle_start])  # Bits antes del ciclo
            cycle = "".join(bits[cycle_start:])      # Bits del ciclo
            
            # Retornar con notación de ciclo: "parte_fija(parte_repetida)"
            return f"{pre_cycle}{cycle}" if cycle else pre_cycle
        
        # Guardar esta fracción y su posición para detectar futuros ciclos
        seen[frac_str] = position
        
        # Algoritmo estándar de conversión decimal->binario:
        frac *= 2           # Multiplicar por 2
        bit = int(frac)     # La parte entera es el próximo bit (0 o 1)
        bits.append(str(bit))  # Agregar bit al resultado
        frac -= bit         # Quedarnos solo con la parte decimal
        
        position += 1
    
    # Si salimos del while sin encontrar ciclo, retornar todos los bits
    return "".join(bits) if bits else "0"

def pd_binario_decimal():
    pass



def parte_decimal_base(parte_decimal: float, base: int, max_digitos: int = 50) -> str:
    match base:
        case 2: return pd_binario_decimal()
        case 10: return pd_decimal_binario(parte_decimal, max_digitos)
    pass

def base_decimal(original: str, base: int) -> int:
    match base:
        case 2: return binario_decimal(original)
        case 10: return int(original)
        case 16: return hex_decimal(original)
    return sum(int(digito) * base**i for i, digito in enumerate(reversed(original)))

if __name__ == "__main__":
    while True:
        base = int(input("Base del número (1 - 16): "))
        if base < 1 or base > 16:
            print("[!] Base inválida. Intente de nuevo.")
            continue
        original = input(f"[{base}] Número en base {base}: ")
        print(f"\n[10] Número en decimal: {base_decimal(original, base)}")


