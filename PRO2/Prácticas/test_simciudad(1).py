"""
Módulo test_simciudad.py
Tests unitarios para SimCiudad usando unittest
"""

import unittest
from edificios import Edificios
from viviendas import Viviendas
from oficinas import Oficinas
from equipamiento import Equipamiento
from ciudad import Ciudad


class TestEdificios(unittest.TestCase):
    """Tests para las clases de edificios."""
    
    def test_crear_vivienda(self):
        """Test creación de edificio de viviendas."""
        vivienda = Viviendas("Apartamentos Central", 20000, 400, 3, 100, 30)
        
        self.assertEqual(vivienda.nombre, "Apartamentos Central")
        self.assertEqual(vivienda.coste_construccion, 20000)
        self.assertEqual(vivienda.coste_mantenimiento, 400)
        self.assertEqual(vivienda.impacto_felicidad, 3)
        self.assertEqual(vivienda.capacidad, 100)
        self.assertEqual(vivienda.num_hogares, 30)
    
    def test_vivienda_calcular_ingresos(self):
        """Test cálculo de ingresos de viviendas."""
        vivienda = Viviendas("Residencial", 15000, 300, 2, 50, 15)
        
        ingresos = vivienda.calcular_ingresos()
        self.assertEqual(ingresos, 15*Viviendas._PRECIO_ALQUILER)  
    
    def test_vivienda_capacidad_disponible(self):
        """Test capacidad disponible en viviendas."""
        vivienda = Viviendas("Torre", 30000, 500, 4, 150, 50)
        
        disponible = vivienda.obtener_capacidad_disponible()
        self.assertEqual(disponible, 0)
    
    
    def test_vivienda_validacion_capacidad_negativa(self):
        """Test validación de capacidad negativa."""
        vivienda = Viviendas("Test", 10000, 200, 1, 50, 15)
        
        with self.assertRaises(ValueError):
            vivienda.capacidad = -10
    
    def test_crear_oficina(self):
        """Test creación de edificio de oficinas."""
        oficina = Oficinas("Centro Empresarial", 35000, 700, 2, 10, 800)
        
        self.assertEqual(oficina.nombre, "Centro Empresarial")
        self.assertEqual(oficina.capacidad_oficinas, 10)
        self.assertEqual(oficina.empresas_actuales, 0)
        self.assertEqual(oficina.alquiler_por_oficina, 800)
    
    def test_oficina_calcular_ingresos(self):
        """Test cálculo de ingresos de oficinas."""
        oficina = Oficinas("Torre Corporativa", 50000, 1000, 3, 15, 750)
        oficina.empresas_actuales = 8
        
        ingresos = oficina.calcular_ingresos()
        self.assertEqual(ingresos, 6000)  # 8 * 750
    
    def test_oficina_asignar_empresas(self):
        """Test asignación de empresas a oficinas."""
        oficina = Oficinas("Plaza Negocios", 30000, 600, 2, 12, 700)
        
        asignadas = oficina.asignar_empresas(5)
        self.assertEqual(asignadas, 5)
        self.assertEqual(oficina.empresas_actuales, 5)
        
        # Asignar más empresas
        asignadas = oficina.asignar_empresas(10)
        self.assertEqual(asignadas, 7)  # Solo quedan 7 espacios
        self.assertEqual(oficina.empresas_actuales, 12)
    
    def test_oficina_eliminar_empresas(self):
        """Test eliminación de empresas de oficinas."""
        oficina = Oficinas("Business Center", 40000, 800, 2, 20, 680)
        oficina.empresas_actuales = 15
        
        eliminadas = oficina.eliminar_empresas(5)
        self.assertEqual(eliminadas, 5)
        self.assertEqual(oficina.empresas_actuales, 10)
        
        # Intentar eliminar más de las que hay
        eliminadas = oficina.eliminar_empresas(20)
        self.assertEqual(eliminadas, 10)  # Solo hay 10
        self.assertEqual(oficina.empresas_actuales, 0)
    
    def test_crear_equipamiento(self):
        """Test creación de edificio de equipamiento."""
        parque = Equipamiento("Parque Central", 15000, 250, 10, "parque", 200)
        
        self.assertEqual(parque.nombre, "Parque Central")
        self.assertEqual(parque.tipo, "parque")
        self.assertEqual(parque.capacidad_uso, 200)
        self.assertEqual(parque.impacto_felicidad, 10)
    
    def test_equipamiento_no_genera_ingresos(self):
        """Test que equipamiento no genera ingresos."""
        hospital = Equipamiento("Hospital Regional", 40000, 800, 15, "hospital", 500)
        
        ingresos = hospital.calcular_ingresos()
        self.assertEqual(ingresos, 0)
    
    def test_edificio_validacion_coste_negativo(self):
        """Test validación de coste de construcción negativo."""
        vivienda = Viviendas("Test", 10000, 200, 1, 50, 15)
        
        with self.assertRaises(ValueError):
            vivienda.coste_construccion = -5000
    
    def test_edificio_validacion_nombre_vacio(self):
        """Test validación de nombre vacío."""
        vivienda = Viviendas("Test", 10000, 200, 1, 50, 15)
        
        with self.assertRaises(ValueError):
            vivienda.nombre = ""


class TestCiudad(unittest.TestCase):
    """Tests para la clase Ciudad."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.ciudad = Ciudad("Ciudad Test", 100, 50000)
    
    def test_crear_ciudad(self):
        """Test creación de ciudad."""
        self.assertEqual(self.ciudad.nombre, "Ciudad Test")
        self.assertEqual(self.ciudad.habitantes, 100)
        self.assertEqual(self.ciudad.felicidad, 50)
        self.assertEqual(self.ciudad.presupuesto, 50000)
        self.assertEqual(len(self.ciudad.edificios), 0)
    
    def test_construir_edificio_con_presupuesto(self):
        """Test construcción de edificio con presupuesto suficiente."""
        vivienda = Viviendas("Apartamentos", 15000, 300, 2, 80, 25)
        resultado = self.ciudad.construir_edificio(vivienda)
        
        self.assertTrue(resultado)
        self.assertEqual(len(self.ciudad.edificios), 1)
        self.assertEqual(self.ciudad.presupuesto, 35000)  # 50000 - 15000
    
    def test_construir_edificio_sin_presupuesto(self):
        """Test construcción de edificio sin presupuesto suficiente."""
        ciudad_pobre = Ciudad("Pobre", 50, 5000)
        oficina = Oficinas("Torre Cara", 60000, 1000, 2, 15, 800)
        
        resultado = ciudad_pobre.construir_edificio(oficina)
        
        self.assertFalse(resultado)
        self.assertEqual(len(ciudad_pobre.edificios), 0)
        self.assertEqual(ciudad_pobre.presupuesto, 5000)  # Sin cambios
    
    def test_orden_construccion_edificios(self):
        """Test que los edificios mantienen orden de construcción."""
        vivienda1 = Viviendas("Primera", 10000, 200, 1, 50, 15)
        oficina = Oficinas("Segunda", 20000, 400, 2, 10, 700)
        vivienda2 = Viviendas("Tercera", 15000, 300, 2, 80, 25)
        
        self.ciudad.construir_edificio(vivienda1)
        self.ciudad.construir_edificio(oficina)
        self.ciudad.construir_edificio(vivienda2)
        
        self.assertEqual(self.ciudad.edificios[0].nombre, "Primera")
        self.assertEqual(self.ciudad.edificios[1].nombre, "Segunda")
        self.assertEqual(self.ciudad.edificios[2].nombre, "Tercera")
    
    def test_actualizar_presupuesto(self):
        """Test actualización de presupuesto."""
        presupuesto_inicial = self.ciudad.presupuesto
        
        vivienda = Viviendas("Residencial", 10000, 200, 2, 80, 25)
        self.ciudad.construir_edificio(vivienda)
        
        # Presupuesto tras construcción: 50000 - 10000 = 40000
        self.ciudad.actualizar_presupuesto()
        
        # Ingresos: 25*300+100*500= 7500+50000=57500, Gastos: 200
        # Nuevo presupuesto: 40000 + 57500 - 200 = 97300
        self.assertEqual(self.ciudad.presupuesto, 97300)
    
    def test_obtener_capacidad_viviendas(self):
        """Test obtención de capacidad total de viviendas."""
        vivienda1 = Viviendas("Primera", 10000, 200, 1, 50, 15)
        vivienda2 = Viviendas("Segunda", 15000, 300, 2, 80, 25)
        oficina = Oficinas("Oficina", 20000, 400, 2, 10, 700)
        
        self.ciudad.construir_edificio(vivienda1)
        self.ciudad.construir_edificio(vivienda2)
        self.ciudad.construir_edificio(oficina)
        
        capacidad = self.ciudad.obtener_capacidad_viviendas()
        self.assertEqual(capacidad, 130)  # 50 + 80
    
    def test_obtener_capacidad_oficinas(self):
        """Test obtención de capacidad de oficinas."""
        oficina1 = Oficinas("Primera", 20000, 400, 2, 10, 700)
        oficina2 = Oficinas("Segunda", 30000, 600, 3, 15, 750)
        
        self.ciudad.construir_edificio(oficina1)
        self.ciudad.construir_edificio(oficina2)
        
        capacidad = self.ciudad.obtener_capacidad_oficinas()
        self.assertEqual(capacidad, 25)  # 10 + 15
    
    def test_obtener_empresas_actuales(self):
        """Test obtención de empresas actuales."""
        oficina1 = Oficinas("Primera", 20000, 400, 2, 10, 700)
        oficina1.empresas_actuales = 7
        oficina2 = Oficinas("Segunda", 30000, 600, 3, 15, 750)
        oficina2.empresas_actuales = 12
        
        self.ciudad.construir_edificio(oficina1)
        self.ciudad.construir_edificio(oficina2)
        
        empresas = self.ciudad.obtener_empresas_actuales()
        self.assertEqual(empresas, 19)  # 7 + 12
    
   
    def test_actualizar_felicidad_con_edificios(self):
        """Test actualización de felicidad con edificios."""
        self.ciudad.habitantes = 50
        
        # Construir viviendas con capacidad suficiente
        vivienda = Viviendas("Residencial", 15000, 300, 5, 100, 30)
        equipamiento = Equipamiento("Parque", 10000, 200, 15, "parque", 150)
        
        self.ciudad.construir_edificio(vivienda)
        self.ciudad.construir_edificio(equipamiento)
        
        self.ciudad.actualizar_felicidad()
        
        # Felicidad debe ser superior a la base (50)
        self.assertGreater(self.ciudad.felicidad, 50)
    
    def test_felicidad_limites(self):
        """Test que felicidad se mantiene en rango 0-100."""
        # Test límite superior
        self.ciudad.felicidad = 150
        self.assertEqual(self.ciudad.felicidad, 100)
        
        # Test límite inferior
        self.ciudad.felicidad = -20
        self.assertEqual(self.ciudad.felicidad, 0)
        
        # Test valor válido
        self.ciudad.felicidad = 75.5
        self.assertEqual(self.ciudad.felicidad, 75.5)
    
    def test_validacion_habitantes_negativos(self):
        """Test validación de habitantes negativos."""
        with self.assertRaises(ValueError):
            self.ciudad.habitantes = -10
    
    def test_validacion_nombre_ciudad_vacio(self):
        """Test validación de nombre de ciudad vacío."""
        with self.assertRaises(ValueError):
            self.ciudad.nombre = ""
    
    def test_construir_edificio_tipo_invalido(self):
        """Test construcción con tipo inválido."""
        with self.assertRaises(TypeError):
            self.ciudad.construir_edificio("no es un edificio")


class TestIntegracion(unittest.TestCase):
    """Tests de integración del sistema completo."""
    
    def test_funcion_X(self):
        """Test de las funciones del módulo main.
           Requiere esfuerzo pero es útil para ver dónde fallan las cosas cuando s ehacen cambios.
           No es obligatorio entregarlo"""
        pass
    
    def test_simulacion_completa_basica(self):
        """Test de una simulación básica completa.
           Requiere esfuerzo pero es útil para ver dónde fallan las cosas cuando s ehacen cambios.
           No es obligatorio entregarlo"""
        pass


def suite():
    """Crea una suite de tests."""
    loader = unittest.TestLoader()
    return unittest.TestSuite([
        loader.loadTestsFromTestCase(TestEdificios),
        loader.loadTestsFromTestCase(TestCiudad),
        loader.loadTestsFromTestCase(TestIntegracion),
    ])

if __name__ == '__main__':
    # Ejecutar tests con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
