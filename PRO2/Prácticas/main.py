"""
Simulación de la evolución de SimCiudad mediante eventos aleatorios
"""
import sys
import random
import pandas as pd
from Ciudad import Ciudad
from edificios import Viviendas , Oficinas , Equipamiento



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

def random_edificio(tipo : str):


    dispatch = {
        "viviendas" : (random.choice(["Hola" , "Juan"]), random.randint(500000, 1000000), random.randint(1000 , 5000), random.randint(10 , 20), random.randint( 90 , 140), random.randint( 15, 40)),
        "oficinas" : (random.choice(["mercadona" , "arenal"]), random.randint(700000, 1200000), random.randint(5000 , 12000), random.randint(5 , 10), random.randint( 5 , 12), random.randint( 3000, 9000)),
        "equipamiento" : (random.choice(["almacen" , "estacion"]), random.randint(300000, 2300000), random.randint(9000 , 14000), random.randint(20 , 30), random.choice(["servicios", "transporte"]), random.randint( 10, 50))
    }

    return dispatch[tipo]



def estructura_inicial(ciudad):
    lista = ["viviendas", "viviendas", "oficinas","equipamiento"]

    dispatch = {
        "viviendas" : Viviendas,
        "oficinas" : Oficinas,
        "equipamiento" : Equipamiento
    }

    for i in lista:
        a , b , c , d , e , f = random_edificio("viviendas")
        ciudad.construir_edificio(dispatch[i](a , b , c , d , e , f )) 
    


def Simulacion():
    pass
    



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


        if clave == "NUM_MESES":
            NUM_MESES = int(valor)
        elif clave == "NOMBRE_CIUDAD":
            NOMBRE_CIUDAD = valor.strip('"')
        elif clave == "HABITANTES_INICIALES":
            HABITANTES_INICIALES = int(valor)
        elif clave == "PRESUPUESTO_INICIAL":
            PRESUPUESTO_INICIAL = int(valor)


    # Ejecutar la simulación

    ciudad = Ciudad(NOMBRE_CIUDAD, HABITANTES_INICIALES,PRESUPUESTO_INICIAL, felicidad=0 ,  edificios=[])

    estructura_inicial(ciudad)

    for m in range(NUM_MESES):
        print(f"MES {m}")
        print(f"HABITANTES: {ciudad.habitantes} | FELICIDAD: {ciudad.felicidad} | PRESUPUESTO: {ciudad.presupuesto}")
        pass

    # Completar el código con la llamada a la función que inicia la simulación
    
    print("SIMULACIÓN COMPLETADA")

 
