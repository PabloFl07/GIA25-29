
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, SympifyError
from utils import determinar_dominio , interval_to_numpy

# Definir variable simbólica
x = symbols('x')

def graficar_fnc(fnc, f, der, d):
    try:
        x_vals = interval_to_numpy(determinar_dominio(fnc), steps = 10000, upper_limit=10)  # Definir dominio a graficar a partir del dominio Total

        y_vals = f(x_vals) # Evaluar con numpy 
        y_der = d(x_vals) # Evaluar la derivada

        # Marcar los ejes x e y
        plt.axhline(0, color='black', linewidth=0.8)
        plt.axvline(0, color='black', linewidth=0.8)

# Colores diferenciados y estilos
        plt.plot(x_vals, y_vals, label=f"f(x) = {fnc}", color='blue')
        plt.plot(x_vals, y_der, label=f"f'(x) = {der}", color='orange', linestyle='--')

# Mejorar el layout general
        plt.tight_layout()
        plt.grid(True, linestyle=':', linewidth=0.5)
        plt.legend(loc='upper right', fontsize=9)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
    except (SympifyError, SyntaxError):
        print("❌ Error: La función ingresada no es válida.")
    except Exception as e:
        print(f"⚠️ Error durante la evaluación: {e}")