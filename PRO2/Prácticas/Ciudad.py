from edificios import Edificio, Viviendas, Oficinas, Equipamiento

class Ciudad:

    _IMPUESTO_POR_HABITANTE = 500
    _UMBRAL_OCUPACION = 0.85
    _RATIO_EQUIPAMIENTO = 0.01
    _FELICIDAD_MEDIA = 50

    def __init__(self, nombre : str, habitantes : int, presupuesto: int, felicidad: int, edificios: list):
        self._nombre = nombre
        self._habitantes = habitantes
        self._presupuesto = presupuesto
        self._felicidad = felicidad
        self._edificios = edificios


    def __str__(self):
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
    def presupuesto(self, valor):
        self._presupuesto = valor
    

    def construir_edificio(self, edificio : Edificio):
        coste = edificio.coste_construccion

        if self.presupuesto > coste:
            self.edificios.append(edificio) # !
            self.presupuesto = self.presupuesto - coste
            return True
        
        return False
    

    def actualizar_presupuesto(self):
        ingresos = 0
        gastos = 0
        for edificio in self.edificios:
            ingresos += edificio.calcular_ingresos()
            gastos += edificio.coste_mantenimiento

        ingresos += self._IMPUESTO_POR_HABITANTE * self.habitantes


        self.presupuesto = ingresos - gastos
    

    def actualizar_felicidad(self): # !!

        if self.habitantes <= 0:
            self.felicidad = self.FELICIDAD_MEDIA

        felicidad_total = 0
        num_viviendas = 0
        num_equipamientos = 0


        for edificio in self.edificios:
            if isinstance(edificio, Equipamiento):
                num_equipamientos += 1

            elif isinstance(edificio, Viviendas):
                num_viviendas += 1

            felicidad_total += edificio.impacto_felicidad

        if len(self.edificios) != 0:
            capacidad_total = self.obtener_capacidad_oficinas() + self.obtener_capacidad_viviendas()

        if self.habitantes / capacidad_total > self.UMBRAL_OCUPACION:
            felicidad_total -= 10
        else:
            felicidad_total += 1

        if num_viviendas == 0:
            felicidad_total -= 30

        if num_equipamientos / 100 > self.RATIO_EQUIPAMIENTO:
            felicidad_total += 1
        else:
            felicidad_total -= 1


        self.felicidad = felicidad_total

    def obtener_capacidad_viviendas(self) -> int:
        capacidad_viviendas = 0
        for edificio in self.edificios:
            if isinstance(edificio, Viviendas):
                capacidad_viviendas += edificio.capacidad

        return capacidad_viviendas
    
    def obtener_capacidad_oficinas(self) -> int:
        capacidad_oficinas = 0
        for edificio in self.edificios:
            if isinstance(edificio, Oficinas):
                capacidad_oficinas += edificio.capacidad

        return capacidad_oficinas

    def obtener_empresas_actuales(self) -> int:
        empresas_totales = 0
        for edificio in self.edificios:
            if isinstance(edificio, Oficinas):
                empresas_totales += edificio.empresas_actuales

        return empresas_totales





if __name__ == "__main__":
    pass