import unittest
from Ciudad import Ciudad
from edificios import Viviendas, Oficinas, Equipamiento, Edificio

class TestEdificios(unittest.TestCase):

    def test_edificios(self):
        vivienda = Viviendas("Casa de Pablo", 400000 , 1000 , 50 , 100 , 20)
        oficina = Oficinas("Coworking La Grela", 500000, 2000, 30 , 145 , 12000)
        equipamiento = Equipamiento("Estación de bus", 1000000, 3000, 90 , "Transporte", 1000)

        self.assertEqual(vivienda.nombre, "Casa de Pablo")
        self.assertEqual(oficina.coste_construccion, 500000)
        self.assertEqual(equipamiento.coste_mantenimiento, 3000)
        self.assertEqual(vivienda.impacto_felicidad, 50)
        self.assertEqual(oficina.capacidad_oficinas, 145)
        self.assertEqual(equipamiento.tipo, "Transporte")
        self.assertEqual(vivienda.num_hogares, 20)

    def test_calcular_ingresos(self):
        vivienda = Viviendas("Casa de Pablo", 400000 , 1000 , 50 , 100 , 20)
        oficina = Oficinas("Coworking La Grela", 500000, 2000, 30 , 145 , 1200)
        equipamiento = Equipamiento("Estación de bus", 1000000, 3000, 90 , "Transporte", 1000)

        self.assertEqual(vivienda.calcular_ingresos(), 6000)
        self.assertEqual(oficina.calcular_ingresos(), 0 ) # !!!
        self.assertEqual(equipamiento.calcular_ingresos(), 0)

    def test_obtener_capacidad_disponible(self):
        vivienda = Viviendas("Casa de Pablo", 400000 , 1000 , 50 , 100 , 20)
        oficina = Oficinas("Coworking La Grela", 500000, 2000, 30 , 145 , 1200)
        equipamiento = Equipamiento("Estación de bus", 1000000, 3000, 90 , "Transporte", 1000)

        self.assertEqual(vivienda.obtener_capacidad_disponible(), 0 )
        self.assertEqual(oficina.obtener_capacidad_disponible(), 145) # !!!!
        self.assertEqual(equipamiento.obtener_capacidad_disponible(), 1000)

    def test_asignar_empresas(self):
        oficina = Oficinas("Coworking La Grela", 500000, 2000, 30 , 120 , 1200)

        self.assertEqual(oficina.asignar_empresas(80), 80)             # Añadimos 80 empresas
        self.assertEqual(oficina.obtener_capacidad_disponible(), 40)   # Medimos la capacidad
        self.assertEqual(oficina.asignar_empresas(50), 40)             # Intentamos añadir mas de la que caben
        self.assertEqual(oficina.obtener_capacidad_disponible(), 0)    # Comprobamos que no hay más capacidad

    def test_eliminar_empresas(self):
        oficina = Oficinas("Coworking La Grela", 500000, 2000, 30 , 120 , 1200)

        self.assertEqual(oficina.asignar_empresas(80), 80)              # Añadimos 80 empresas
        self.assertEqual(oficina.eliminar_empresas_empresas(50), 50)    # Eliminamos 50
        self.assertEqual(oficina.obtener_capacidad_disponible(), 90)    # Comprobamos la capacidad
        self.assertEqual(oficina.eliminar_empresas_empresas(50), 30)    # Intentamos eliminar más de las que hay
        self.assertEqual(oficina.obtener_capacidad_disponible(), 120)   # Comprobamos que la capacidad es total

    def test_ciudad(self):
        ciudad = Ciudad("A Coruña", 2000000, 14000000, 68 , [])

        self.assertEqual(ciudad.nombre, "A Coruña")
        self.assertEqual(ciudad.habitantes, 2000000)
        self.assertEqual(ciudad.presupuesto, 14000000)
        self.assertEqual(ciudad.felicidad, 68)
        self.assertEqual(ciudad.edificios, [ ])

    def test_crear_edificio(self):
        ciudad = Ciudad("A Coruña", 2000000, 1400000, 68 , [])

        vivienda = Viviendas("Casa de Pablo", 400000 , 1000 , 50 , 100 , 20)
        oficina = Oficinas("Coworking La Grela", 500000, 2000, 30 , 145 , 1200)
        equipamiento = Equipamiento("Estación de bus", 1000000, 3000, 90 , "Transporte", 1000)

        self.assertTrue(ciudad.construir_edificio(vivienda))
        self.assertEqual(ciudad.presupuesto, 1000000)
        self.assertTrue(ciudad.construir_edificio(oficina))
        self.assertEqual(ciudad.presupuesto, 500000)
        self.assertFalse(ciudad.construir_edificio(equipamiento))

        self.assertIn(vivienda,ciudad.edificios)
        self.assertIn(oficina,ciudad.edificios)
        self.assertNotIn(equipamiento,ciudad.edificios)


    def test_actualizar_presupuesto(self):
        vivienda = Viviendas("Casa de Pablo", 400000 , 1000 , 50 , 100 , 20)
        oficina = Oficinas("Coworking La Grela", 500000, 2000, 30 , 145 , 1200)
        equipamiento = Equipamiento("Estación de bus", 1000000, 3000, 90 , "Transporte", 1000)

        ciudad = Ciudad("A Coruña", 20000, 500000, 68 , [vivienda, oficina, equipamiento])

        self.assertEqual(ciudad.actualizar_presupuesto(), 10500000 )


    def test_actualizar_felicidad(self): # !!!!
        raise NotImplementedError()
    


    def test_obtener_capacidad(self):
        vivienda = Viviendas("Casa de Pablo", 400000 , 1000 , 50 , 100 , 20)
        oficina = Oficinas("Coworking La Grela", 500000, 2000, 30 , 145 , 1200)
        equipamiento = Equipamiento("Estación de bus", 1000000, 3000, 90 , "Transporte", 1000)

        ciudad = Ciudad("A Coruña", 20000, 500000, 68 , [vivienda, oficina, equipamiento])

        self.assertEqual(ciudad.obtener_capacidad_viviendas, 100)
        self.assertEqual(ciudad.obtener_capacidad_oficinas, 145)

    def test_obtener_empresas_actuales(self):
        oficina1 = Oficinas("Coworking La Grela", 500000, 2000, 30 , 145 , 1200)
        oficina2 = Oficinas("Coworking La Grela", 620000, 2700, 36 , 170 , 1470)

        oficina1.asignar_empresas(50)
        oficina2.asignar_empresas(20)

        ciudad = Ciudad("A Coruña", 20000, 500000, 68 , [oficina1, oficina2])

        self.assertEqual(ciudad.obtener_empresas_actuales(), 70)
















