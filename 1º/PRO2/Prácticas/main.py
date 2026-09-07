"""
Pablo Fernández Lema | p.fernandezl@udc.es Raúl Pita Seoane | raul.pita.seoane@udc.es

Simulación de la evolución de SimCiudad mediante eventos aleatorios
"""

import sys
import random
import pandas as pd
from ciudad import Ciudad
from viviendas import Viviendas
from oficinas import Oficinas
from equipamientos import Equipamiento

# Configuración de la simulación
NUM_MESES = None
NOMBRE_CIUDAD = None
HABITANTES_INICIALES = None
PRESUPUESTO_INICIAL = None

# Configuración de semilla para reproducibilidad (opcional)
random.seed(191)


class Simulacion:
    """
    Clase que incorpora métodos estáticos relacionados con la simulación para favorecer la estructura y métodos necesarios para la misma.

    Attributes
    ---

    ciudad : Ciudad

    """
    def __init__(self, ciudad: Ciudad):
        self.ciudad = ciudad

    @property
    def ciudad(self) -> Ciudad:
        return self._ciudad

    @ciudad.setter
    def ciudad(self, valor) -> None:
        if not isinstance(valor, Ciudad):
            raise TypeError("Error: Debe ser de tipo Ciudad")

        self._ciudad = valor

    @staticmethod
    def random_viviendas() -> Viviendas:
        """Genera una vivienda aleatoria"""
        nombres = ["Casa", "Piso", "Chalet", "Mansion, Residencia, Rascacielos"]

        return Viviendas(
            random.choice(nombres),
            random.randint(500000, 1000000),
            random.randint(1000, 5000),
            random.randint(3, 6),
            random.randint(90, 140),
            random.randint(15, 40),
        )

    @staticmethod
    def random_oficinas() -> Oficinas:
        """Genera una oficina aleatoria"""
        nombres = ["Inditex", "Coworking", "La Xunta"]

        return Oficinas(
            random.choice(nombres),
            random.randint(700000, 1200000),
            random.randint(5000, 12000),
            random.randint(2, 3),
            random.randint(5, 12),
            random.randint(3000, 9000),
        )

    @staticmethod
    def random_equipamiento() -> Equipamiento:
        """Genera un equipamiento aleatorio"""
        nombres = ["Estación", "Parque", "Clínica", "Comisaría"]

        return Equipamiento(
            random.choice(nombres),
            random.randint(300000, 2300000),
            random.randint(9000, 14000),
            random.randint(2, 4),
            random.choice(
                ["servicios", "transporte", "hospital", "policia", "bomberos", "parque"]
            ),
            random.randint(10, 50),
        )

    @staticmethod
    def estructura_inicial( ciudad) -> None:
        """ 
        Construye los cuatro edificios iniciales
        """
        ciudad.construir_edificio(Simulacion.random_viviendas())
        ciudad.construir_edificio(Simulacion.random_viviendas())
        ciudad.construir_edificio(Simulacion.random_oficinas())
        ciudad.construir_edificio(Simulacion.random_equipamiento())

    def inmigracion(self) -> bool:
        """
        Con una probabilidad del 40%, calcula la llegada de nuevos habitantes a la ciudad

        Returns
        ---
        bool
        """
        if random.randint(0, 100) <= 40:
            inmigrantes = random.randint(5, 200)
            self.ciudad.habitantes += inmigrantes
            print(f"Han inmigrado {inmigrantes} habitantes")
            return True
        return False

    def emigracion(self) -> bool:
        """
        Con una probabilidad del 20% con felicidad alta y 35% con felicidad baja, calcula la salida de habitantes de la ciudad

        Returns
        ---
        bool
        """
        probabilidad = 20 if self.ciudad.felicidad > 40 else 35

        if random.randint(0, 100) <= probabilidad:
            if self.ciudad.habitantes > 5: # Tiene que haber mínimo 5 habitantes para poder eliminar
                emigrantes = random.randrange(5, min(self.ciudad.habitantes, 200))
                if self.ciudad.habitantes < emigrantes:
                    self.ciudad.habitantes = 0
                self.ciudad.habitantes -= emigrantes

                print(f"Han emigrado {emigrantes} habitantes")
                return True
        return False

    def creacion_empresas(self) -> bool:
        """
        Con una probabilidad del 30%, si hay capacidad, crea empresas y las asigna a las oficinas de la ciudad

        Returns
        ---
        bool
        """
        if random.randint(0, 100) <= 30:
            empresas = random.randint(1, 5)

            if self.ciudad.obtener_capacidad_oficinas() == 0:
                print("No hay capacidad para ninguna empresa")
                return False

            creadas = 0
            while empresas > 0 and self.ciudad.obtener_capacidad_oficinas() > 0: # Tiene que haber empresas para asignar y capacidad disponible
                for edificio in self.ciudad.edificios:
                    if isinstance(edificio, Oficinas):
                        asignadas = edificio.asignar_empresas(empresas) 
                        empresas -= asignadas
                        creadas += asignadas
            print(f"Se han creado {creadas} empresas")
            return True
        return False

    def cierre_empresas(self) -> bool:
        """ 
        Con una probabilidad del 15%, si hay empresas, las cierra

        Returns
        ---
        bool
        """
        if random.randint(0, 100) < 15:
            empresas = random.randint(1, 3)

            cerradas = 0
            if self.ciudad.obtener_empresas_actuales() >= empresas:
                while empresas > 0:
                    for edificio in self.ciudad.edificios:
                        if isinstance(edificio, Oficinas):
                            asignadas = edificio.eliminar_empresas(empresas)
                            empresas -= asignadas
                            cerradas += asignadas
                print(f"Han cerrado {cerradas} empresas")
                return True
        return False

    def construccion(self, fue_creada=False) -> bool:
        """
        En base a 4 condiciones, intenta construir un edificio de cada tipo

        Returns
        ---
        bool
        """

        capacidad = self.ciudad.obtener_capacidad_viviendas()

        if capacidad > 0 and self.ciudad.habitantes / capacidad > 0.9:
            self.ciudad.construir_edificio(Simulacion.random_viviendas())
            print("Se ha construido una vivienda")
            return True
        elif self.ciudad.obtener_capacidad_oficinas() < 5 and fue_creada:
            self.ciudad.construir_edificio(Simulacion.random_oficinas())
            print("Se ha construido una oficina")
            return True
        elif self.ciudad.felicidad < 40:
            self.ciudad.construir_edificio(Simulacion.random_equipamiento())
            print("Se ha construido un equipamiento")
            return True
        
        elif self.ciudad.presupuesto >= 3000000:
            self.ciudad.construir_edificio(
                random.choice([Simulacion.random_viviendas(),Simulacion.random_equipamiento(), Simulacion.random_oficinas(),]))
            print("Se ha construido un edificio aleatorio")
            return True
        return False
    
    @staticmethod
    def simulacion(ciudad: Ciudad) -> None:
        """
        Flujo principal de la simulación, inicia los eventos, imprime los resultados y finalmente calcula un resumen estadístico
        """
        data = [0] * NUM_MESES # Lista vacía que rellenaremos con los datos


        sim = Simulacion(ciudad)

        Simulacion.estructura_inicial(ciudad)

        for m in range(NUM_MESES): # Llamamos a cada evento
            print(f"\n\t==============  MES {m} =============\n")
            print(
                f"[!] HABITANTES: {ciudad.habitantes} | FELICIDAD: {ciudad.felicidad} | PRESUPUESTO: {ciudad.presupuesto}\n"
            )

            sim.emigracion()
            sim.inmigracion()
            fue_creada = sim.creacion_empresas()
            sim.cierre_empresas()
            sim.construccion(fue_creada)

            # Actualizamos los valores principales
            ciudad.actualizar_presupuesto()
            ciudad.actualizar_felicidad()

            data[m] = [ciudad.habitantes, ciudad.felicidad, ciudad.presupuesto]
        # Crea el dataframe de los datos de Habitantes, Felicidad y presupuesto recopilados mes a mes
        pdata = pd.DataFrame(data, columns=["Habitantes", "Felicidad", "Presupuesto"])

        return pdata
        
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

    # Instanciamos la ciudad base de la simulación
    ciudad = Ciudad(NOMBRE_CIUDAD, HABITANTES_INICIALES, PRESUPUESTO_INICIAL)

    datos = Simulacion.simulacion(ciudad)

    print(" ==================== RESULTADOS ===================")
    # .describe() genera un nuevo DataFrame con las filas  "count", "mean", "std". De las cuales solo queremos la media, dt, ... por lo que lo especificamos con loc
    stats = datos.describe().loc[["mean", "std", "max", "min"]]
    print("\n", stats)


    print("\nSIMULACIÓN COMPLETADA")
