
def guess_impar(resto):
    match resto:
        case 1:
            return 1
        case 3:
            return 3
        case 5:
            return 5 
        case 2:
            return 7 
        case 4:
            return 9
        case _:
            return "[!] Caso imposible [!]"

def guess_par(resto):
    match resto:
        case 2:
            return 2
        case 4:
            return 4
        case 1:
            return 6 
        case 3:
            return 8 
        case 0:
            return 10
        case _:
            return "[!] Caso imposible [!]"


print("[-] PIENSA EN UN NÚMERO DEL 1-10 [-]")
while True:
    paridad = int(input("\n[+] Número par (2) o impar (1): "))
    resto = int(input("Resto de dividir entre 5: "))
    
    if paridad == 2:
        print(f"Tu número es el {guess_par(resto)}")
    elif paridad == 1:
        print(f"Tu número es el {guess_impar(resto)}")