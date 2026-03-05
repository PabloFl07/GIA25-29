"""
Pablo Fernández Lema | p.fernandezl@udc.es Raúl Pita Seoane | raul.pita.seoane@udc.es

Archivo para la declaración de la clase Viviendas

"""


from edificios import Edificio


class Viviendas(Edificio):
    """
    Subclase de Edificio, incorpora atributos de capacidad y número de hogares.

    Attributes
    ---

    nombre : str

    coste_construccion : int

    coste_mantenimiento : int

    impacto_felicidad : int

    capacidad : int

    num_hogares : int

    Methods
    ---

    calcular_ingresos():
        Calcula los ingresos en función del número de hogares y el precio del alquiler

    obtener_capacidad_disponible():
        Siempre es 0

    """

    _PRECIO_ALQUILER = 300

    def __init__(
        self,
        nombre: str,
        coste_construccion: int,
        coste_mantenimiento: int,
        impacto_felicidad: int,
        capacidad: int,
        num_hogares: int,
    ):
        super().__init__(
            nombre, coste_construccion, coste_mantenimiento, impacto_felicidad
        )
        self.capacidad = capacidad
        self.num_hogares = num_hogares

    def __str__(self):
        return super().__str__()

    @property
    def capacidad(self) -> int:
        return self._capacidad

    @property
    def num_hogares(self) -> int:
        return self._num_hogares

    @capacidad.setter
    def capacidad(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Debe ser un dato tipo int")
        if valor < 0:
            raise ValueError("Error: valor negativo")
        self._capacidad = valor

    @num_hogares.setter
    def num_hogares(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Debe ser un dato tipo int")

        if valor < 0:
            raise ValueError("Error: valor negativo")
        self._num_hogares = valor

    def calcular_ingresos(self):
        return self._PRECIO_ALQUILER * self.num_hogares

    def obtener_capacidad_disponible(self):
        return 0
