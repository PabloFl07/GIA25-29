"""
Pablo Fernández Lema | p.fernandezl@udc.es Raúl Pita Seoane | raul.pita.seoane@udc.es

Archivo para la declaración de la clase Ciudad

"""


from viviendas import Viviendas
from oficinas import Oficinas
from equipamientos import Equipamiento
from edificios import Edificio


class Ciudad:
    """
    Clase para los objetos `Ciudad`

    Attributes
    ---

    nombre : str

    habitantes : int

    presupuesto : int

    felicidad : int

    edificios : list

    Methods
    ---

    construir_edificio(edificio):
        Construye edificio

    actualizar_presupuesto():
        Actualiza el presupuesto de la ciudad según el balance de ingresos y gastos

    actualizar_felicidad():
        Actualiza la felicidad en base a unos baremos

    obtener_capacidad_viviendas():
        Calcula la capacidad total entre todas las viviendas contruídas

    obtener_capacidad_oficinas():
        Calcula la capacidad total entre todas las oficinas construídas

    obtener_empresas_actuales():
        Calcula el número de empresas totales entre todas las oficinas de la ciudad
    """

    _IMPUESTO_POR_HABITANTE = 500
    _UMBRAL_OCUPACION = 0.85
    _RATIO_EQUIPAMIENTO = 0.01
    _FELICIDAD_MEDIA = 50

    def __init__(self, nombre: str, habitantes: int, presupuesto: int):
        """
        Asigna los atributos a los objetos `Ciudad`

        Parameters
        ---
        nombre: str
            Nombre de la ciudad

        habitantes: int
            Número de habitantes

        presupuesto: int
            Cantidad de presupuesto

        """
        self.nombre = nombre
        self.habitantes = habitantes
        self.presupuesto = presupuesto
        self.felicidad: int = 50
        self.edificios: list[Edificio] = []

    def __str__(self):
        """
        Representación de los objetos de la clase Ciudad

        Returns
        ---
        str
        """
        return f"{self.nombre}: {self.habitantes}:{self.presupuesto}: {self.felicidad}"

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def habitantes(self) -> int:
        return self._habitantes

    @property
    def presupuesto(self) -> int:
        return self._presupuesto

    @property
    def felicidad(self) -> int:
        return self._felicidad

    @property
    def edificios(self) -> int:
        return self._edificios

    @presupuesto.setter
    def presupuesto(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Debe ser un dato de tipo int")

        if valor < 0:
            raise ValueError("Error: Valor negativo")
        self._presupuesto = valor

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise TypeError("Error: Debe ser un dato de tipo str")

        if not valor.strip():
            raise ValueError("Error: No puede esta vacío")
        self._nombre = valor

    @habitantes.setter
    def habitantes(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Debe ser un dato de tipo int")

        if valor < 0:
            raise ValueError("Error: Valor negativo")
        self._habitantes = valor

    @felicidad.setter
    def felicidad(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Debe ser un dato de tipo int")
        if valor > 100:
            valor = 100
        elif valor < 0:
            valor = 0
        self._felicidad = valor

    @edificios.setter
    def edificios(self, valor: list[Edificio]) -> None:
        if not isinstance(valor, list):
            raise TypeError("Error: Debe ser un dato de tipo lista")
        self._edificios = valor

    def construir_edificio(self, edificio: Edificio) -> bool:
        """
        Intenta construir un edificio para la ciudad tras comprobar que hay presupuesto suficiente.

        Parameters
        ---
        edificio: Edificio
            Edificio a construir

        Returns
        ---
        True
            Si se ha podido construído un edificio
        False
            Si no se ha podido construir
        """

        if not isinstance(edificio, Edificio):
            raise TypeError("Error: Intentando construir algo que no es un edificio")

        coste = edificio.coste_construccion

        if self.presupuesto >= coste:
            self.edificios.append(edificio)
            self.presupuesto = self.presupuesto - coste
            return True

        return False

    def actualizar_presupuesto(self) -> None:
        """
        Actualiza el presupuesto de la ciudad según el balance de ingresos y gastos

        Returns
        ---
        None
        """
        ingresos = 0
        gastos = 0
        for edificio in self.edificios:
            ingresos += edificio.calcular_ingresos()
            gastos += edificio.coste_mantenimiento

        ingresos += self._IMPUESTO_POR_HABITANTE * self.habitantes

        self.presupuesto = self.presupuesto + (ingresos - gastos)

    def actualizar_felicidad(self) -> None:
        """
        Actualiza la felicidad en base a unos baremos y condiciones.

        Returns
        ---
        None
        """

        if self.habitantes <= 0:
            self.felicidad = self._FELICIDAD_MEDIA

        felicidad_total = self.felicidad
        num_viviendas = 0
        num_equipamientos = 0

        for edificio in self.edificios:
            if isinstance(edificio, Equipamiento):
                num_equipamientos += 1

            elif isinstance(edificio, Viviendas):
                num_viviendas += 1

            felicidad_total += edificio.impacto_felicidad

        if len(self.edificios) != 0:
            capacidad_total = (
                self.obtener_capacidad_oficinas() + self.obtener_capacidad_viviendas()
            )

        if capacidad_total > 0 and self.habitantes / capacidad_total > self._UMBRAL_OCUPACION:
            felicidad_total -= 10
            print("[] UMBRAL OCUPACIÓN []") 
        else:
            felicidad_total += 1

        if num_viviendas == 0:
            felicidad_total -= 30
            print("NO VIVIENDAS")

        if self.habitantes > 0 and num_equipamientos / self.habitantes > self._RATIO_EQUIPAMIENTO:
            felicidad_total += 1
            
        else:
            felicidad_total -= 1
            print("RATIO EQUIPAMIENTOS")

        self.felicidad = felicidad_total

    def obtener_capacidad_viviendas(self) -> int:
        """
        Calcula la capacidad total entre todas las viviendas contruídas

        Returns
        ---
        int
            Capacidad total de las viviendas
        """
        capacidad_viviendas = 0
        for edificio in self.edificios:
            if isinstance(edificio, Viviendas):
                capacidad_viviendas += edificio.capacidad

        return capacidad_viviendas

    def obtener_capacidad_oficinas(self) -> int:
        """
        Calcula la capacidad total entre todas las oficinas de la ciudad

        Returns
        ---
        int
            Capacidad total de las oficinas
        """
        capacidad_total = 0
        for edificio in self.edificios:
            if isinstance(edificio, Oficinas):
                capacidad_total += edificio.obtener_capacidad_disponible()

        return capacidad_total

    def obtener_empresas_actuales(self) -> int:
        """
        Calcula el número de empresas totales entre todas las oficinas de la ciudad

        Returns
        ---
        int
            Numero de empresas totales en la ciudad
        """
        empresas_totales = 0
        for edificio in self.edificios:
            if isinstance(edificio, Oficinas):
                empresas_totales += edificio.empresas_actuales

        return empresas_totales


if __name__ == "__main__":
    pass
