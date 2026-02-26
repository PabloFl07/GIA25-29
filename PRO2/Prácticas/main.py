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
random.seed(42)


# Completar las con las funciones que realizan la simulación

def random_viviendas():
    nombres = ["Casa", "Piso", "Chalet", "Mansion"]
    
    return Viviendas(random.choice(nombres), random.randint(500000, 1000000), random.randint(1000 , 5000), random.randint(3 , 6), random.randint( 90 , 140), random.randint( 15, 40))

def random_oficinas():
    nombres = ["Mercadona", "Arenal", "Sanbrandan"]

    return Oficinas(random.choice(nombres), random.randint(700000, 1200000), random.randint(5000 , 12000), random.randint(2 , 3), random.randint( 5 , 12), random.randint( 3000, 9000))

def random_equipamiento():
    nombres = ["Guarida", "Mausoleo", "Pene"]

    return Equipamiento(random.choice(nombres), random.randint(300000, 2300000), random.randint(9000 , 14000), random.randint(2 , 4), random.choice(["servicios", "transporte"]), random.randint( 10, 50))
    
def estructura_inicial(ciudad):
    ciudad.construir_edificio(random_viviendas())
    ciudad.construir_edificio(random_viviendas())
    ciudad.construir_edificio(random_oficinas())
    ciudad.construir_edificio(random_equipamiento())
    


# LISTA DE LISTA -> DATAFRAME


def Simulacion(ciudad):

    data = []

    for m in range(NUM_MESES):
        emigracion(ciudad)
        inmigracion(ciudad)
        fue_creada = creacion_empresas(ciudad)
        cierre_empresas(ciudad)
        construccion(ciudad, fue_creada)

        ciudad.actualizar_presupuesto()
        ciudad.actualizar_felicidad()

        print(f"\n\t============== RESULTADOS MES {m} =============\n")
        datos_mes = [ ciudad.habitantes, ciudad.felicidad, ciudad.presupuesto]

        data.append(datos_mes)
        print(f"[!] HABITANTES: {ciudad.habitantes} | FELICIDAD: {ciudad.felicidad} | PRESUPUESTO: {ciudad.presupuesto}")

    pdata = pd.DataFrame(data, columns=["Habitantes","Felicidad","Presupuesto"])

    print(f"====== Media ======\n{pdata.mean()}") # MEDIA DE CADA COLUMNA
    print(f"======   DT  ======:\n{pdata.std()}")
    print(f"====== Máximo ======:\n{pdata.max()}")
    print(f"====== Mínimo ======:\n{pdata.min()}")
    
def inmigracion(ciudad):
    if random.random() < 0.40:
        ciudad.habitantes = ciudad.habitantes + random.randint(5, 200)

def emigracion(ciudad):
    probabilidad = 0.20 if ciudad.felicidad > 40 else 0.35

    if random.random() <= probabilidad:
        emigrantes = random.randrange(5 , min(ciudad.habitantes, 200))
        ciudad.habitantes = ciudad.habitantes - emigrantes

def creacion_empresas(ciudad):
    if random.random() < 0.30:
        empresas = random.randint(1,5)

        if ciudad.obtener_capacidad_oficinas() == 0:
            print("No hay capacidad para ninguna empresa")
            return False

        while empresas > 0 and ciudad.obtener_capacidad_oficinas() > 0:
            for edificio in ciudad.edificios:
                if isinstance(edificio, Oficinas):
                    asignadas = edificio.asignar_empresas(empresas)
                    empresas -= asignadas
        return True

def cierre_empresas(ciudad):
    if random.random() < 0.15:
        empresas = random.randint(1,3)

        if ciudad.obtener_empresas_actuales() > empresas:
            while empresas > 0:
                for edificio in ciudad.edificios:
                    if isinstance(edificio, Oficinas):
                        asignadas = edificio.eliminar_empresas(empresas)
                        empresas -= asignadas


def construccion(ciudad, fue_creada = False):
    if ciudad.presupuesto >= 3000000:
        ciudad.construir_edificio(random.choice([random_viviendas(), random_equipamiento(),random_oficinas()]))
        return
    if ciudad.habitantes / ciudad.obtener_capacidad_viviendas() > 0.9:
        ciudad.construir_edificio(random_viviendas())
    elif ciudad.obtener_capacidad_oficinas() < 5 and fue_creada:
        ciudad.construir_edificio(random_oficinas())
    elif ciudad.felicidad < 40:
        ciudad.construir_edificio(random_equipamiento())
    


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

    ciudad = Ciudad(NOMBRE_CIUDAD, HABITANTES_INICIALES,PRESUPUESTO_INICIAL)

    estructura_inicial(ciudad)

    Simulacion(ciudad)


    # Completar el código con la llamada a la función que inicia la simulación
    
    print("SIMULACIÓN COMPLETADA")

 
