from abc import ABC, abstractmethod

class Edificio(ABC):
    def __init__(
        self, nombre, coste_construccion, coste_mantenimiento, impacto_felicidad
    ):
        self.nombre = nombre
        self._coste_construccion = coste_construccion
        self.coste_mantenimiento = coste_mantenimiento
        self.impacto_felicidad = impacto_felicidad

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Coste de construcción: {self.coste_construccion}, Coste de mantenimiento: {self.coste_mantenimiento}, Impacto en felicidad: {self.imacto_felicidad}"

    @abstractmethod
    def calcular_ingresos(self) -> int:
        pass

    @abstractmethod
    def obtener_capacidad_disponible() -> int:
        pass


class Viviendas(Edificio):
    _PRECIO_ALQUILER = 300

    def __init__(self, nombre, coste_construccion, coste_mantenimiento, impacto_felicidad, capacidad, num_hogares):
        super().__init__(nombre,coste_construccion,coste_mantenimiento,impacto_felicidad,)
        self.capacidad = capacidad
        self.num_hogares = num_hogares

    def calcular_ingresos(self):
        return self._PRECIO_ALQUILER * self.num_hogares

    def obtener_capacidad_disponible(self):
        return 0


class Oficinas(Edificio):
    def __init__(
        self,
        nombre,
        coste_construccion,
        coste_mantenimiento,
        impacto_felicidad,
        capacidad_oficinas,
        empresas_actuales ,
        alquiler_por_oficina,
    ):
        super().__init__(nombre, coste_construccion, coste_mantenimiento, impacto_felicidad)
        self.capacidad_oficinas = capacidad_oficinas
        self.empresas_actuales = empresas_actuales
        self.alquiler_por_oficina = alquiler_por_oficina

    def calcular_ingresos(self):
        return self.alquiler_por_oficina * self.empresas_actuales

    def obtener_capacidad_disponible(self):
        return self.capacidad_oficinas - self.empresas_actuales

    def asignar_empresas(self, cantidad: int) -> int:
        disponibles = self.obtener_capacidad_disponible()

        if cantidad > disponibles:
            self.empresas_actuales = self.capacidad_oficinas
            sobran = cantidad - disponibles

            return f"Empresas asignadas: {cantidad - sobran}"

        self.empresas_actuales += cantidad

        return f"Empresas asignadas: {cantidad}"

    def eliminar_empresas(self, cantidad: int) -> int:

        if cantidad > self.empresas_actuales:
            sobran = -(self.empresas_actuales - cantidad)
            self.empresas_actuales = 0

            return f"Empresas asignadas: {cantidad - sobran}"

        self.empresas_actuales -= cantidad

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
        super().__init__(nombre, coste_construccion, coste_mantenimiento, impacto_felicidad)
        self.tipo = tipo
        self.capacidad_uso = capacidad_uso

    def calcular_ingresos(self):
        return 0

    def obtener_capacidad_disponible(self):
        return self.capacidad_uso
