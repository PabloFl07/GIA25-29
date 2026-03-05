"""
Pablo Fernández Lema | p.fernandezl@udc.es Raúl Pita Seoane | raul.pita.seoane@udc.es

Archivo para la declaración de la clase Oficinas

"""

from edificios import Edificio

class Oficinas(Edificio):
    """
    Subclase de Edificio, incorpora atributos de capacidad y alquiler por oficina.

    Attributes
    ---

    nombre : str

    coste_construccion : int

    coste_mantenimiento : int

    impacto_felicidad : int

    capacidad_oficinas : int

    alquiler_por_oficina : int

    Methods
    ---

    calcular_ingresos():
        Calcula los ingresos en función del número de hogares y el precio del alquiler

    obtener_capacidad_disponible():
        Calcula la capacidad como la diferencia entre la capacidad de las oficinas y el número de empresas actuales

    asignar_empresas():
        Si hay capacidad, asigna una empresa a una oficina, devuelve la cantidad que se han asignado

    eliminar_empresas():
        Elimina una empresa de una oficina, devuelve la cantidad que se han eliminado

    """

    def __init__(
        self,
        nombre: str,
        coste_construccion: int,
        coste_mantenimiento: int,
        impacto_felicidad: int,
        capacidad_oficinas: int,
        alquiler_por_oficina: int,
    ):
        super().__init__(
            nombre, coste_construccion, coste_mantenimiento, impacto_felicidad
        )
        self.capacidad_oficinas = capacidad_oficinas
        self.empresas_actuales: int = 0
        self.alquiler_por_oficina = alquiler_por_oficina

    def __str__(self):
        return super().__str__()

    @property
    def capacidad_oficinas(self) -> int:
        return self._capacidad_oficinas

    @property
    def empresas_actuales(self) -> int:
        return self._empresas_actuales

    @property
    def alquiler_por_oficina(self) -> int:
        return self._alquiler_por_oficina

    @capacidad_oficinas.setter
    def capacidad_oficinas(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Debe ser un dato tipo int")
        if valor < 0:
            raise ValueError("Error: valor negativo")
        self._capacidad_oficinas = valor

    @empresas_actuales.setter
    def empresas_actuales(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Debe ser un dato tipo int")
        if valor < 0:
            raise ValueError("Error: valor negativo")
        self._empresas_actuales = valor

    @alquiler_por_oficina.setter
    def alquiler_por_oficina(self, valor) -> None:
        if not isinstance(valor, int):
            raise TypeError("Error: Debe ser un dato tipo int")
        if valor < 0:
            raise ValueError("Error: valor negativo")
        self._alquiler_por_oficina = valor

    def calcular_ingresos(self) -> int:
        """
        Calcula los ingresos en función de el alquiler por oficina y el número de empresas actuales
        
        Returns
        ---
        int
            Ingresos
        """
        return self.alquiler_por_oficina * self.empresas_actuales

    def obtener_capacidad_disponible(self) -> int:
        """
        Calcula la capacidad como la diferencia entre la capacidad de las oficinas y el número de empresas actuales
        
        Returns
        ---
        inf
            Capacidad
        """
        return self.capacidad_oficinas - self.empresas_actuales

    def asignar_empresas(self, cantidad: int) -> int:
        """
        Si hay capacidad, asigna una empresa a una oficina, devuelve la cantidad que se han asignado

        Returns
        ---
        int
            Cantidad de empresas asignadas
        """
        disponibles = self.obtener_capacidad_disponible()

        if cantidad > disponibles:
            self.empresas_actuales = self.capacidad_oficinas
            sobran = cantidad - disponibles

            return cantidad - sobran

        self.empresas_actuales += cantidad
        return cantidad

    def eliminar_empresas(self, cantidad: int) -> int:
        """
        Elimina una empresa de una oficina, devuelve la cantidad que se han eliminado
        
        Returns
        ---
        int 
            Cantidad de empresas eliminadas
        """
        if cantidad > self.empresas_actuales:
            sobran = -(self.empresas_actuales - cantidad)
            self.empresas_actuales = 0

            return cantidad - sobran

        self.empresas_actuales = self.empresas_actuales - cantidad

        return cantidad
