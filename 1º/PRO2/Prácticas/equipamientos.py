"""
Pablo Fernández Lema | p.fernandezl@udc.es Raúl Pita Seoane | raul.pita.seoane@udc.es

Archivo para la declaración de la clase Equipamiento

"""


from edificios import Edificio


class Equipamiento(Edificio):
    """
    Subclase de Edificio, incorpora atributos de tipo y capacidad.

    Attributes
    ---

    nombre : str

    coste_construccion : int

    coste_mantenimiento : int

    impacto_felicidad : int

    tipo : str

    capacidad_uso : int

    Methods
    ---

    calcular_ingresos():
        Siempre es 0

    obtener_capacidad_disponible():
        Calcula la capacidad como la capacidad de uso

    """

    def __init__(
        self,
        nombre: str,
        coste_construccion: int,
        coste_mantenimiento: int,
        impacto_felicidad: int,
        tipo: str,
        capacidad_uso: int,
    ):
        super().__init__(
            nombre, coste_construccion, coste_mantenimiento, impacto_felicidad
        )
        self.tipo = tipo
        self.capacidad_uso = capacidad_uso

    def __str__(self):
        return super().__str__()

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def capacidad_uso(self) -> int:
        return self._capacidad_uso

    @tipo.setter
    def tipo(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise TypeError("Error: Debe ser un dato tipo str")

        if not valor.strip():
            raise ValueError("Error: Debe ser una str no vacía")

        self._tipo = valor

    @capacidad_uso.setter
    def capacidad_uso(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Debe ser un dato tipo int")
        if valor < 0:
            raise ValueError("Error: valor negativo")
        self._capacidad_uso = valor

    def calcular_ingresos(self) -> int:
        """
        Siempre es 0

        Returns
        ---
        int
            0

        """
        return 0

    def obtener_capacidad_disponible(self) -> int:
        """
        Calcula la capacidad como la capacidad de uso

        Returns
        ---
        int
            Capacidad de uso
        """
        return self.capacidad_uso
