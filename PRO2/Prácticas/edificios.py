from abc import ABC, abstractmethod


class Edificio(ABC):
    def __init__(
        self,
        nombre: str,
        coste_construccion: int,
        coste_mantenimiento: int,
        impacto_felicidad: int,
    ):
        self._nombre = nombre
        self._coste_construccion = coste_construccion
        self._coste_mantenimiento = coste_mantenimiento
        self._impacto_felicidad = impacto_felicidad

    def obtener_informacion(self):
        return f"Nombre: {self._nombre}, Coste de construcción: {self._coste_construccion}, Coste de mantenimiento: {self._coste_mantenimiento}, Impacto en felicidad: {self._imacto_felicidad}"

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
        self._nombre = valor

    @coste_construccion.setter
    def coste_construccion(self, valor: int) -> None:
        self._coste_construccion = valor

    @coste_mantenimiento.setter
    def coste_mantenimiento(self, valor: int) -> None:
        self._coste_mantenimiento = valor

    @impacto_felicidad.setter
    def impacto_felicidad(self, valor: int) -> None:
        self._impacto_felicidad = valor

    @abstractmethod
    def calcular_ingresos(self) -> int:
        pass

    @abstractmethod
    def obtener_capacidad_disponible() -> int:
        pass


class Viviendas(Edificio):
    _PRECIO_ALQUILER = 300

    def __init__(
        self,
        nombre : str,
        coste_construccion : int,
        coste_mantenimiento : int,
        impacto_felicidad : int,
        capacidad : int,
        num_hogares : int,
    ):
        super().__init__(
            nombre, coste_construccion, coste_mantenimiento, impacto_felicidad
        )
        self._capacidad = capacidad
        self._num_hogares = num_hogares


    def __str__(self):
        return f"{self.nombre}"
    

    @property
    def capacidad(self) -> int:
        return self._capacidad
    
    @property
    def num_hogares(self) -> int:
        return self._num_hogares
    
    @capacidad.setter
    def capacidad(self, valor : int) -> int:
        self._capacidad = valor

    @num_hogares.setter
    def num_hogares(self, valor) -> int:
        self._num_hogares = valor

    def calcular_ingresos(self):
        return self._PRECIO_ALQUILER * self.num_hogares

    def obtener_capacidad_disponible(self):
        return 0


class Oficinas(Edificio):
    def __init__(
        self,
        nombre : str,
        coste_construccion : int,
        coste_mantenimiento : int,
        impacto_felicidad : int,
        capacidad_oficinas : int,
        alquiler_por_oficina : int,
    ):
        super().__init__(
            nombre, coste_construccion, coste_mantenimiento, impacto_felicidad
        )
        self._capacidad_oficinas = capacidad_oficinas
        self._empresas_actuales = 0  # ! 0 por defecto
        self._alquiler_por_oficina = alquiler_por_oficina

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
    def capacidad_oficinas(self, valor : int) -> int:
        self._capacidad_oficinas = valor

    @empresas_actuales.setter
    def empresas_actuales(self, valor : int) -> int:
        self._empresas_actuales = valor

    @alquiler_por_oficina.setter
    def alquiler_por_oficina(self, valor) -> int:
        self._alquiler_por_oficina = valor

    def __str__(self):
        return super().__str__()

    def calcular_ingresos(self):
        """
        Esta funcion hace esto:
        """
        return self._alquiler_por_oficina * self.empresas_actuales

    def obtener_capacidad_disponible(self):
        return self.capacidad_oficinas - self.empresas_actuales

    def asignar_empresas(self, cantidad: int) -> int:
        disponibles = self.obtener_capacidad_disponible()

        if cantidad > disponibles:
            self.empresas_actuales = self.capacidad_oficinas
            sobran = cantidad - disponibles

            return f"Empresas asignadas: {cantidad - sobran}"

        self.empresas_actuales = self._empresas_actuales + cantidad

        return f"Empresas asignadas: {cantidad}"

    def eliminar_empresas(self, cantidad: int) -> int:

        if cantidad > self.empresas_actuales:
            sobran = -(self.empresas_actuales - cantidad)
            self.empresas_actuales = 0

            return f"Empresas asignadas: {cantidad - sobran}"

        self.empresas_actuales = self.empresas_actuales - cantidad

        return f"Empresas tras la incorporación: {cantidad}"


class Equipamiento(Edificio):
    _PRECIO_ALQUILER = 0

    def __init__(
        self,
        nombre,
        coste_construccion,
        coste_mantenimiento,
        impacto_felicidad,
        tipo,
        capacidad_uso,
    ):
        super().__init__(
            nombre, coste_construccion, coste_mantenimiento, impacto_felicidad
        )
        self._tipo = tipo
        self._capacidad_uso = capacidad_uso

    @property
    def tipo(self):
        return self._tipo
    
    @property
    def capacidad_uso(self) -> int:
        return self._capacidad_uso
    
    @tipo.setter
    def tipo(self, valor : str) -> None:
        self._tipo = valor

    @capacidad_uso.setter
    def capacidad_uso(self, valor : int) -> None:
        self._capacidad_uso = valor

    def __str__(self):
        return super().__str__()

    def calcular_ingresos(self):
        return 0

    def obtener_capacidad_disponible(self):
        return self.capacidad_uso
