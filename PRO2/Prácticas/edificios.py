from abc import ABC, abstractmethod


class Edificio(ABC):
    """
    Clase abstracta, base de Viviendas, Oficinas y Equipamiento, que aporta atributos y métodos comunes a estas clases.

    Attributes
    ---

    nombre : str

    coste_construccion : int

    coste_mantenimiento : int

    impacto_felicidad : int

    Methods
    ---

    obtener_informacion():
        Muestra la información de todos los atributos

    calcular_ingresos():
        Método abstracto, calcula los ingresos según el tipo de edificio

    obtener_capacidad_disponible():
        Método abstracto, calcula la cantidad disponible según el tipo de edificio

    """

    def __init__(
        self,
        nombre: str,
        coste_construccion: int,
        coste_mantenimiento: int,
        impacto_felicidad: int,
    ) -> None:
        # Asignamos los valores llamando al setter para aplicar las comprobaciones en el iniciador
        self.nombre = nombre
        self.coste_construccion = coste_construccion
        self.coste_mantenimiento = coste_mantenimiento
        self.impacto_felicidad = impacto_felicidad

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.nombre}"

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def coste_construccion(self) -> int:
        return self._coste_construccion

    @property
    def coste_mantenimiento(self) -> int:
        return self._coste_mantenimiento

    @property
    def impacto_felicidad(self) -> int:
        return self._impacto_felicidad

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise TypeError("Error: Debe ser un dato tipo str")

        if not valor.strip():
            raise ValueError("Error: cadena vacía")
        self._nombre = valor

    @coste_construccion.setter
    def coste_construccion(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Deve ser un dato tipo int")

        if valor < 0:
            raise ValueError("Error: valor negativo")
        self._coste_construccion = valor

    @coste_mantenimiento.setter
    def coste_mantenimiento(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Deve ser un dato tipo int")

        if valor < 0:
            raise ValueError("Error: valor negativo")
        self._coste_mantenimiento = valor

    @impacto_felicidad.setter
    def impacto_felicidad(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Deve ser un dato tipo int")

        if valor < 0:
            raise ValueError("Error: valor negativo")
        self._impacto_felicidad = valor

    def obtener_informacion(self) -> str:
        """Muestra la información de todos los atributos"""
        return f"Nombre: {self.nombre}, Coste de construcción: {self.coste_construccion}, Coste de mantenimiento: {self.coste_mantenimiento}, Impacto en felicidad: {self.impacto_felicidad}"

    # Al ser métodos abstractos, se definene en cada clase
    @abstractmethod
    def calcular_ingresos(self) -> int:
        """Método abstracto, calcula los ingresos según el tipo de edificio"""
        pass

    @abstractmethod
    def obtener_capacidad_disponible(self) -> int:
        """Método abstracto, calcula la cantidad disponible según el tipo de edificio"""
        pass
