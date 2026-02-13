"""
Simulación de la evolución de SimCiudad mediante eventos aleatorios
"""
import sys
import random
import pandas as pd
from edificios import Edificios
from oficinas import Oficinas
from equipamiento import Equipamiento
from viviendas import Viviendas
from ciudad import Ciudad



# Configuración de la simulación
NUM_MESES = None
NOMBRE_CIUDAD = None
HABITANTES_INICIALES = None
PRESUPUESTO_INICIAL = None

# Configuración de semilla para reproducibilidad (opcional)
# random.seed(42)


# Completar las con las funciones que realizan la simulación
"""
a simulación comienza construyendo dos edificios de viviendas, un edificio de oficinas y un
equipamiento. A continuación, para cada mes, se mostrará el número de habitantes, el grado de
felicidad y el presupuesto final, así como los eventos generados, que pueden ser:

Llegada de habitantes (inmigración). Hay un 40% de probabilidad de recibir inmigrantes, cuyo
número será aleatorio entre 5 y 200.
Salida de habitantes (emigración). Hay un 20% de probabilidad de enviar emigrantes si la
felicidad es mayor de 40 puntos. En caso contrario la probabilidad aumenta al 35%. El número
de emigrantes será un número aleatorio entre 5 y 200 (siempre menor o igual al número de
habitantes).
Creación de empresas. Hay un 30% de probabilidad de que lleguen nuevas empresas, en un
número aleatorio entre 1 y 5, que se podrán instalar si hay oficinas disponibles (en caso de
que no haya oficinas para todas se instalarán las que quepan)
"""


def Simulacion():
    raise NotImplementedError()



if __name__ == "__main__":
	
	# Leer el archivo de configuración desde la línea de comandos o usar el predeterminado
    config_file = sys.argv[1] if len(sys.argv) > 1 else "ciudad1.txt"

    # Intentar abrir el archivo especificado
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: El archivo '{config_file}' no existe.", file=sys.stderr)
        sys.exit(1)

    # Leer los datos del  archivo
    print(f"Leyendo configuración desde: {config_file}")
	
    for linea in lines:
        clave, valor = linea.split(":", 1)
        clave = clave.strip()
        valor = valor.strip()

    dispatch = {
        "NUM_MESES" : NUM_MESES,
        "NOMBRE_CIUDAD" : NOMBRE_CIUDAD,
        "HABITANTES_INICIALES" : HABITANTES_INICIALES,
        "PRESUPUESTO_INICIAL" : PRESUPUESTO_INICIAL
    }

    dispatch[clave] = valor
            
    # Ejecutar la simulación
    # Completar el código con la llamada a la función que inicia la simulación
    
    print(" SIMULACIÓN COMPLETADA")
 
