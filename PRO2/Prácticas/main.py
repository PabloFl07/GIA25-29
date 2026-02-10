from abc import ABC, abstractmethod

class Ciudad:

    def __init__():
        raise NotImplementedError()


class Edificio(ABC):


    def __init__(self, nombre, coste_construcción, coste_mantenimiento, impacto_felicidad):
        self.nombre = nombre
        self.coste_construcción = coste_construcción 
        self.coste_mantenimiento = coste_mantenimiento
        self.imacto_felicidad = impacto_felicidad

    @abstractmethod
    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Coste de construcción: {self.coste_construcción}, Coste de mantenimiento: {self.coste_mantenimiento}, Impacto en felicidad: {self.imacto_felicidad}"

    def calcular_ingresos(self) -> int:
        raise NotImplementedError()
    
    def obtener_capacidad_disponible() -> int:
        raise NotImplementedError()

class Viviendas(Edificio):
    
    def __init__(self, capacidad, num_hogares):
        super().__init__(self.nombre, self.coste_construcción, self.coste_mantenimiento, self.impacto_felicidad)
        self.capacidad = capacidad
        self.num_hogares = num_hogares



class Oficinas(Edificio):

    
    
    def __init__(self, nombre, coste_construcción, coste_mantenimiento, impacto_felicidad, capacidad_oficinas, empresas_actuales, alquiler_por_oficina):
        super().__init__(nombre, coste_construcción, coste_mantenimiento, impacto_felicidad)
        self.capacidad_oficinas = capacidad_oficinas
        self.empresas_actuales = empresas_actuales
        self.alquiler_por_oficina = alquiler_por_oficina


    def asignar_empresas(self, cantidad:int) -> int:
        disponibles = self.capacidad_oficinas - self.empresas_actuales

        if cantidad > disponibles:
            self.empresas_actuales = self.capacidad_oficinas
            sobran = cantidad - disponibles

            return f"Sobran: {sobran}"

        self.empresas_actuales += cantidad
        
        return f"Empresas tras la incorporación: {self.empresas_actuales}"
    
    def eliminar_empresas(self, cantidad:int) -> int:

        if cantidad > self.empresas_actuales:
            sobran = -(self.empresas_actuales - cantidad)
            self.empresas_actuales = 0

            return f"Sobran: {sobran}"

        self.empresas_actuales -= cantidad
        
        return f"Empresas tras la incorporación: {self.empresas_actuales}"
        
    
    

class Equipamiento(Edificio):

    _PRECIO_ALQUILER = 0
    
    def __init__(self, nombre, coste_construcción, coste_mantenimiento, impacto_felicidad, tipo, capacidad_uso):
        super().__init__(nombre, coste_construcción, coste_mantenimiento, impacto_felicidad)
        self.tipo = tipo
        self.capacidad_uso = capacidad_uso



Oficina1 = Oficinas("Oficina1", 1000, 100, 40, 100, 10, 50)


print(Oficina1.eliminar_empresas(5))

