from graficar import graficar_fnc
from utils import fnc_input, determinar_dominio

# Traducir de LaTex a python y viceversa
#Arreglar la graficación de funciones con D(f): U o Intersecc
def main():
    f, fnc , der, d = fnc_input()
    graficar_fnc(fnc, f, der, d)


if __name__ == "__main__":
    main()