import unittest
import random
from ciudad import Ciudad
from viviendas import Viviendas
from oficinas import Oficinas
from equipamientos import Equipamiento
from main import Simulacion

class TestEdificios(unittest.TestCase):
    def setUp(self):

        self.vivienda = Viviendas("Casa de Pablo", 400000, 1000, 5, 100, 20)
        self.oficina = Oficinas("Coworking La Grela", 500000, 2000, 4, 120, 1200)
        self.equipamiento = Equipamiento(
            "Estación de bus", 1000000, 3000, 6, "Transporte", 1000
        )

    def test_crear_edificios(self):
        self.assertEqual(self.vivienda.nombre, "Casa de Pablo")
        self.assertEqual(self.oficina.nombre, "Coworking La Grela")
        self.assertEqual(self.equipamiento.nombre, "Estación de bus")
        self.assertEqual(self.vivienda.coste_construccion, 400000)
        self.assertEqual(self.oficina.coste_construccion, 500000)
        self.assertEqual(self.equipamiento.coste_construccion, 1000000)
        self.assertEqual(self.vivienda.coste_mantenimiento, 1000)
        self.assertEqual(self.oficina.coste_mantenimiento, 2000)
        self.assertEqual(self.equipamiento.coste_mantenimiento, 3000)
        self.assertEqual(self.vivienda.impacto_felicidad, 5)
        self.assertEqual(self.oficina.impacto_felicidad, 4)
        self.assertEqual(self.equipamiento.impacto_felicidad, 6)

    def test_crear_vivienda(self):
        """Test creación de edificio de viviendas usando datos del setUp."""
        self.assertEqual(self.vivienda.nombre, "Casa de Pablo")
        self.assertEqual(self.vivienda.coste_construccion, 400000)
        self.assertEqual(self.vivienda.coste_mantenimiento, 1000)
        self.assertEqual(self.vivienda.impacto_felicidad, 5)
        self.assertEqual(self.vivienda.capacidad, 100)
        self.assertEqual(self.vivienda.num_hogares, 20)

    def test_crear_oficina(self):
        """Test creación de edificio de oficinas usando datos del setUp."""
        self.assertEqual(self.oficina.nombre, "Coworking La Grela")
        self.assertEqual(self.oficina.capacidad_oficinas, 120)
        self.assertEqual(self.oficina.empresas_actuales, 0)
        self.assertEqual(self.oficina.alquiler_por_oficina, 1200)

    def test_crear_equipamiento(self):
        """Test creación de edificio de equipamiento (corregido parque por equipamiento)."""
        self.assertEqual(self.equipamiento.nombre, "Estación de bus")
        self.assertEqual(self.equipamiento.tipo, "Transporte")
        self.assertEqual(self.equipamiento.capacidad_uso, 1000)
        self.assertEqual(self.equipamiento.impacto_felicidad, 6)

    def test_atributos_especiales(self):
        self.assertEqual(self.oficina.capacidad_oficinas, 120)
        self.assertEqual(self.oficina.alquiler_por_oficina, 1200)
        self.assertEqual(self.equipamiento.tipo, "Transporte")
        self.assertEqual(self.equipamiento.capacidad_uso, 1000)
        self.assertEqual(self.vivienda.num_hogares, 20)
        self.assertEqual(self.vivienda.capacidad, 100)

    # ========================== CALCULAR INGRESOS =========================== #

    def test_calcular_ingresos(self):
        self.oficina.empresas_actuales = 3
        self.assertEqual(self.vivienda.calcular_ingresos(), 6000)
        self.assertEqual(self.oficina.calcular_ingresos(), 3600)
        self.assertEqual(self.equipamiento.calcular_ingresos(), 0)

    def test_vivienda_calcular_ingresos(self):
        """Test cálculo de ingresos de viviendas."""
        self.assertEqual(self.vivienda.calcular_ingresos(), 6000)

    def test_oficina_calcular_ingresos(self):
        """Test cálculo de ingresos de oficinas."""
        self.oficina.empresas_actuales = 3
        self.assertEqual(self.oficina.calcular_ingresos(), 3600)

    def test_equipamiento_calcular_ingresos(self):
        """Test cálculo de ingresos de equipamiento."""
        self.assertEqual(self.equipamiento.calcular_ingresos(), 0)

    # ========================== CAPACIDAD DISPONIBLE =========================== #

    def test_obtener_capacidad_disponible(self):
        self.assertEqual(self.vivienda.obtener_capacidad_disponible(), 0)
        self.assertEqual(self.oficina.obtener_capacidad_disponible(), 120)
        self.assertEqual(self.equipamiento.obtener_capacidad_disponible(), 1000)

    def test_obtener_capacidad_disponible_vivienda(self):
        self.assertEqual(self.vivienda.obtener_capacidad_disponible(), 0)

    def test_obtener_capacidad_disponible_oficina(self):
        self.assertEqual(self.oficina.obtener_capacidad_disponible(), 120)

    def test_obtener_capacidad_disponible_equipamiento(self):
        self.assertEqual(self.equipamiento.obtener_capacidad_disponible(), 1000)

    # ========================== ASIGNAR/ELIMINAR EMPRESAS =========================== #

    def test_asignar_empresas(self):
        self.assertEqual(self.oficina.asignar_empresas(70), 70)
        self.assertEqual(self.oficina.obtener_capacidad_disponible(), 50)

        self.assertEqual(self.oficina.asignar_empresas(10), 10)
        self.assertEqual(self.oficina.obtener_capacidad_disponible(), 40)

        self.assertEqual(self.oficina.asignar_empresas(50), 40)
        self.assertEqual(self.oficina.obtener_capacidad_disponible(), 0)

    def test_eliminar_empresas(self):
        # 120
        self.assertEqual(self.oficina.asignar_empresas(90), 90)

        self.assertEqual(self.oficina.eliminar_empresas(50), 50)
        self.assertEqual(self.oficina.obtener_capacidad_disponible(), 80)

        self.assertEqual(self.oficina.eliminar_empresas(10), 10)
        self.assertEqual(self.oficina.obtener_capacidad_disponible(), 90)

        self.assertEqual(self.oficina.eliminar_empresas(50), 30)
        self.assertEqual(self.oficina.obtener_capacidad_disponible(), 120)

    # ========================== VALORES NEGATIVOS =========================== #

    def test_vivienda_valores_negativos(self):

        with self.assertRaises(ValueError):
            self.vivienda.coste_construccion = -1

        with self.assertRaises(ValueError):
            self.vivienda.coste_mantenimiento = -1

        with self.assertRaises(ValueError):
            self.vivienda.impacto_felicidad = -1

        with self.assertRaises(ValueError):
            self.vivienda.capacidad = -1

        with self.assertRaises(ValueError):
            self.vivienda.num_hogares = -1

    def test_oficina_valores_negativos(self):

        with self.assertRaises(ValueError):
            self.oficina.coste_construccion = -1

        with self.assertRaises(ValueError):
            self.oficina.coste_mantenimiento = -1

        with self.assertRaises(ValueError):
            self.oficina.impacto_felicidad = -1

        with self.assertRaises(ValueError):
            self.oficina.capacidad_oficinas = -1

        with self.assertRaises(ValueError):
            self.oficina.alquiler_por_oficina = -1

    def test_equipamiento_valores_negativos(self):
        with self.assertRaises(ValueError):
            self.equipamiento.coste_construccion = -1

        with self.assertRaises(ValueError):
            self.equipamiento.coste_mantenimiento = -1

        with self.assertRaises(ValueError):
            self.equipamiento.impacto_felicidad = -1

        with self.assertRaises(ValueError):
            self.equipamiento.capacidad_uso = -1

    def test_str_vacias(self):

        with self.assertRaises(ValueError):
            self.vivienda.nombre = ""

        with self.assertRaises(ValueError):
            self.oficina.nombre = ""

        with self.assertRaises(ValueError):
            self.equipamiento.nombre = ""

        with self.assertRaises(ValueError):
            self.equipamiento.tipo = ""

    #  ========================== ERROR DE TIPADO =========================== #

    def test_tipos_incorrectos(self):

        with self.assertRaises(TypeError):
            self.vivienda.nombre = 0

        with self.assertRaises(TypeError):
            self.vivienda.coste_construccion = "2"

        with self.assertRaises(TypeError):
            self.vivienda.coste_mantenimiento = "3"

        with self.assertRaises(TypeError):
            self.vivienda.impacto_felicidad = "4"

    def test_tipos_vivienda(self):
        with self.assertRaises(TypeError):
            self.vivienda.capacidad = "2"

        with self.assertRaises(TypeError):
            self.vivienda.num_hogares = "3"

    def test_tipos_oficina(self):
        with self.assertRaises(TypeError):
            self.oficina.capacidad_oficinas = "2"

        with self.assertRaises(TypeError):
            self.oficina.empresas_actuales = "3"

    def test_tipos_equipamiento(self):
        with self.assertRaises(TypeError):
            self.equipamiento.tipo = 0

        with self.assertRaises(TypeError):
            self.equipamiento.capacidad_uso = "3"

# ==================================================================================
# ==================================================================================
# ==================================================================================
# ==================================================================================

class TestCiudad(unittest.TestCase):

    def setUp(self):
        self.ciudad = Ciudad("A Coruña", 2000000, 14000000)

        self.vivienda = Viviendas("Casa de Pablo", 400000, 1000, 5, 100, 20)
        self.oficina = Oficinas("Coworking La Grela", 500000, 2000, 4, 145, 1200)
        self.equipamiento = Equipamiento("Estación de bus", 1000000, 3000, 6, "Transporte", 1000)

    def test_crear_ciudad(self):

        self.assertEqual(self.ciudad.nombre, "A Coruña")
        self.assertEqual(self.ciudad.habitantes, 2000000)
        self.assertEqual(self.ciudad.presupuesto, 14000000)

#  ========================== CONSTRUIR EDIFICIOS =========================== #

    def test_construir_edificios_completo(self):
        """Test construcción de edificios, dos con presupesto y el tercero sin presupuesto"""

        self.assertTrue(self.ciudad.construir_edificio(self.vivienda))
        self.assertEqual(self.ciudad.presupuesto, 13600000)
        self.assertTrue(self.ciudad.construir_edificio(self.oficina))
        self.assertEqual(self.ciudad.presupuesto, 13100000)
        self.ciudad.presupuesto = 1000
        self.assertFalse(self.ciudad.construir_edificio(self.equipamiento))

        self.assertIn(self.vivienda, self.ciudad.edificios)
        self.assertIn(self.oficina, self.ciudad.edificios)
        self.assertNotIn(self.equipamiento, self.ciudad.edificios)


    def test_construir_edificio_con_presupuesto(self):
        """Test construcción de edificio con presupuesto suficiente."""
        edificio = Viviendas("Casa Pepe", 300000, 1300, 2, 60, 15)
        
        self.assertTrue(self.ciudad.construir_edificio(edificio))
        self.assertIn(edificio, self.ciudad.edificios)
        self.assertEqual(self.ciudad.presupuesto, 13700000)
    
    def test_construir_edificio_sin_presupuesto(self):
        """Test construcción de edificio sin presupuesto suficiente."""
        edificio = Viviendas("Casa Pepe", 300000, 1300, 2, 60, 15)
        
        self.ciudad.presupuesto = 1000
        self.assertFalse(self.ciudad.construir_edificio(edificio))
        self.assertNotIn(edificio, self.ciudad.edificios)
        self.assertEqual(self.ciudad.presupuesto, 1000)

    #  ========================== ACTUALIZAR PRESUPUESTO/FELICIDAD =========================== #

    def test_actualizar_presupuesto(self):
        self.ciudad.actualizar_presupuesto()
        self.assertEqual(self.ciudad.presupuesto, 1014000000)

    def test_actualizar_felicidad(self):
        """Test actualización de felicidad"""
        self.ciudad.habitantes = 20
        
        vivienda = Viviendas("Casa Raul", 150000, 1300, 5, 100, 30)
        equipamiento = Equipamiento("Parque", 100000, 1200, 15, "Parque", 150)
        
        self.ciudad.construir_edificio(vivienda)
        self.ciudad.construir_edificio(equipamiento)
        
        self.ciudad.actualizar_felicidad()
        
        self.assertGreater(self.ciudad.felicidad, 0)

    #  ========================== OBTENER CAPACIDAD =========================== #

    def test_obtener_capacidad_completo(self):
        self.assertEqual(self.ciudad.obtener_capacidad_viviendas(), 0)
        self.assertEqual(self.ciudad.obtener_capacidad_oficinas(), 0)

        vivienda2 = Viviendas("Casa Xabi", 150000, 1100, 3, 80, 30)
        oficina = Oficinas("Oficina", 200000, 1400, 2, 10, 800)
        
        self.ciudad.construir_edificio(vivienda2)
        self.ciudad.construir_edificio(oficina)

        self.assertEqual(self.ciudad.obtener_capacidad_viviendas(), 80) 

        self.assertEqual(self.ciudad.obtener_capacidad_oficinas(), 10)


    def test_obtener_capacidad_viviendas(self):
        """Test obtención de capacidad total de viviendas."""

        vivienda = Viviendas("Casa Xabi", 150000, 1100, 3, 80, 30)

        self.ciudad.construir_edificio(vivienda)
        
        capacidad = self.ciudad.obtener_capacidad_viviendas()
        self.assertEqual(capacidad, 80)  
    
    def test_obtener_capacidad_oficinas(self):
        """Test obtención de capacidad de oficinas."""

        oficina = Oficinas("Oficina", 200000, 1400, 2, 10, 800)
        
        self.ciudad.construir_edificio(oficina)
  
        self.assertEqual(self.ciudad.obtener_capacidad_oficinas(), 10) 


    #  ========================== OBTENER CAPACIDAD =========================== #
    
    def test_limites_felicidad(self):
        """Test rango de la felicidad"""
        self.ciudad.felicidad = 200
        self.assertEqual(self.ciudad.felicidad, 100)

        self.ciudad.felicidad = -1
        self.assertEqual(self.ciudad.felicidad, 0)
        
        self.ciudad.felicidad = 50
        self.assertEqual(self.ciudad.felicidad, 50)

    #  ========================== OBTENER EMPRESAS =========================== #

    def test_obtener_empresas_actuales(self):
        oficina1 = Oficinas("Coworking Los Rosales", 50000, 2000, 30, 145, 1200)
        oficina2 = Oficinas("Coworking Matogrande", 62000, 2700, 36, 170, 1470)

        ciudad = Ciudad("A Coruña", 20000, 500000)

        oficina1.asignar_empresas(50)
        oficina2.asignar_empresas(20)

        ciudad.construir_edificio(oficina1)

        self.assertEqual(ciudad.obtener_empresas_actuales(), 50)

        ciudad.construir_edificio(oficina2)

        self.assertEqual(ciudad.obtener_empresas_actuales(), 70)


    #  ========================== ERROR DE TIPADO =========================== #

    def test_tipos_incorrectos(self):
        with self.assertRaises(TypeError):
            self.ciudad.nombre = 0

        with self.assertRaises(TypeError):
            self.ciudad.habitantes = "2"

        with self.assertRaises(TypeError):
            self.ciudad.presupuesto = "5"

        with self.assertRaises(TypeError):
            self.ciudad.felicidad = "3"

        with self.assertRaises(TypeError):
            self.ciudad.edificios = "4"

    # ========================== VALORES NEGATIVOS =========================== #

    def test_valores_negativos(self):

        with self.assertRaises(ValueError):
            self.ciudad.nombre = " "

        with self.assertRaises(ValueError):
            self.ciudad.habitantes = -1

        with self.assertRaises(ValueError):
            self.ciudad.presupuesto = -1


class TestSimulacion(unittest.TestCase):

    def setUp(self):
        self.ciudad = Ciudad("Fic city", 250 , 15000000)
        self.sim = Simulacion(self.ciudad)

    def test_estructura_inicial(self):

        self.sim.estructura_inicial(self.ciudad)

        self.assertEqual(len(self.ciudad.edificios), 4)
        self.ciudad.actualizar_felicidad
        self.assertGreater(self.ciudad.felicidad, 0)

        self.assertLess(self.ciudad.presupuesto, 15000000)
        
    # ========================== EMIGRACION / INMIGRACION =========================== #

    def test_inmigracion(self):
        random.seed(42) 
        self.sim.inmigracion()
        self.assertGreater(self.ciudad.habitantes, 0)
        

    def test_emigracion_poca_felicidad(self):
        random.seed(47) # 81 , 14
        self.ciudad.habitantes = 50
        self.ciudad.felicidad = 20
        self.sim.emigracion() # No ocurre
        self.assertEqual(self.ciudad.habitantes, 50)

        self.sim.emigracion() # Ocurre
        self.assertLess(self.ciudad.habitantes, 50)

        # Ocurre

    def test_emigracion_mucha_felicidad(self):
        random.seed(47) 
        self.ciudad.habitantes = 50
        self.ciudad.felicidad = 50
        self.sim.emigracion() # No ocurre
        self.assertEqual(self.ciudad.habitantes, 50)

        self.sim.emigracion() # Ocurre
        self.assertLess(self.ciudad.habitantes, 50) 

    def test_emigracion_sin_habitantes(self):
        random.seed(43)  

        self.ciudad.habitantes = 0
        self.ciudad.felicidad = 20 

        self.assertFalse(self.sim.emigracion())

        self.assertEqual(self.ciudad.habitantes, 0)

    # ========================== CREACION / CIERRE EMPRESAS =========================== #

    def test_creacion_empresas(self):
        random.seed(43)

        self.ciudad.construir_edificio(Oficinas("Proa", 1000,100,2,10,500))

        self.assertTrue(self.sim.creacion_empresas())

        self.assertLess(self.ciudad.obtener_capacidad_oficinas(), 10)
        self.assertGreater(self.ciudad.obtener_empresas_actuales(), 0)


    def test_creacion_empresas_sin_capacidad(self):
        random.seed(43)

        oficina = Oficinas("Proa", 1000,100,2,10,500)

        oficina.asignar_empresas(10)

        self.assertEqual(oficina.obtener_capacidad_disponible(), 0)

        self.ciudad.construir_edificio(oficina)

        self.assertFalse(self.sim.creacion_empresas())

        self.assertEqual(self.ciudad.obtener_empresas_actuales(), 10)
        self.assertEqual(self.ciudad.obtener_capacidad_oficinas(), 0)

    def test_no_creacion_empresas(self):
        random.seed(47) # 45

        self.assertFalse(self.sim.creacion_empresas())

    def test_cierre_empresas(self):
        random.seed(2)

        oficina = Oficinas("Proa", 1000,100,2,10,500)
        oficina.asignar_empresas(6)
        self.ciudad.construir_edificio(oficina)
        self.assertEqual(self.ciudad.obtener_empresas_actuales(), 6)

        self.assertTrue(self.sim.cierre_empresas())

        self.assertLess(self.ciudad.obtener_empresas_actuales(), 6)


    def test_cierre_empresas_sin_empresas(self):
        random.seed(2)

        oficina = Oficinas("Proa", 1000,100,2,10,500)
        self.ciudad.construir_edificio(oficina)
        self.assertEqual(self.ciudad.obtener_empresas_actuales(), 0)

        self.assertFalse(self.sim.cierre_empresas())

        self.assertEqual(self.ciudad.obtener_empresas_actuales(), 0)


    # ========================== CONSTRUCCION =========================== #

    def test_construccion_vivienda(self):
        self.ciudad.presupuesto = 2900000

        vivienda = Viviendas("Casa Adri", 1000, 100, 3, 90, 30)
        self.ciudad.construir_edificio(vivienda)
        self.ciudad.habitantes = 100 

        self.assertTrue(self.sim.construccion())

        self.assertIsInstance(self.ciudad.edificios[1], Viviendas)
        
        self.ciudad.edificios.clear()

    def test_construccion_equipamiento(self):
        self.ciudad.presupuesto = 2900000

        vivienda = Viviendas("Casa Adri", 1000, 100, 3, 120, 30)
        self.ciudad.construir_edificio(vivienda)
        self.ciudad.habitantes = 10
        self.ciudad.felicidad = 30 # Para que construya un equipamiento

        self.assertTrue(self.sim.construccion())

        self.assertIsInstance(self.ciudad.edificios[1], Equipamiento)
        
        self.ciudad.edificios.clear()

    def test_construccion_oficina(self):
        self.ciudad.presupuesto = 2900000

        vivienda = Viviendas("Casa Adri", 1000, 100, 3, 120, 30)
        oficina = Oficinas("Proa", 10000, 1000, 4, 4 , 400)
        self.ciudad.construir_edificio(vivienda)
        self.ciudad.construir_edificio(oficina)
        self.ciudad.habitantes = 10
        
        fue_creada = True

        self.assertTrue(self.sim.construccion(fue_creada))

        self.assertIsInstance(self.ciudad.edificios[2], Oficinas)
        
        self.ciudad.edificios.clear()

def suite():
    """Crea una suite de tests."""
    loader = unittest.TestLoader()
    return unittest.TestSuite([
        loader.loadTestsFromTestCase(TestEdificios),
        loader.loadTestsFromTestCase(TestCiudad),
        loader.loadTestsFromTestCase(TestSimulacion),
    ])

if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())