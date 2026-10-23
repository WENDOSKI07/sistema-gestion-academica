import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from main import crear_personas_ejemplo, crear_programas_ejemplo, main
from models.persona import Person
from views.persona_view import PersonaView


class IntegracionPersonasTest(unittest.TestCase):
    def setUp(self):
        programas = crear_programas_ejemplo()
        self.personas, self.estudiantes, self.docentes = crear_personas_ejemplo(programas)

    def test_persona_abstracta_no_se_puede_instanciar(self):
        # En la segunda actividad creamos personas desde sus clases hijas
        with self.assertRaises(TypeError):
            Person("P007", "Persona de prueba", "prueba@example.com")

    def test_consulta_general_mantiene_el_polimorfismo(self):
        # Probamos la vista real con las seis personas que prepara main
        # El mismo recorrido debe mostrar la información y la actividad de cada una
        salida = StringIO()
        with redirect_stdout(salida):
            PersonaView().mostrar_personas(self.personas)

        texto = salida.getvalue()
        for persona in self.personas:
            self.assertIn(persona.mostrar_informacion(), texto)
            self.assertIn(persona.realizar_actividad_principal(), texto)
        self.assertEqual(len(self.personas), 6)

    def test_cambio_desde_un_area_aparece_en_la_consulta_general(self):
        # Las áreas deben trabajar sobre los mismos objetos que usa el reporte
        estudiante = self.estudiantes[0]
        estudiante.set_name("Ana actualizada")
        salida = StringIO()
        with redirect_stdout(salida):
            PersonaView().mostrar_personas(self.personas)
        self.assertIn("Ana actualizada", salida.getvalue())

    def test_main_permite_consultar_personas_y_volver_al_menu(self):
        # Simulamos la entrada solo en la prueba, el programa sigue siendo interactivo
        salida = StringIO()
        with patch("builtins.input", side_effect=["3", "0"]) as entrada:
            with redirect_stdout(salida):
                main()
        self.assertEqual(entrada.call_count, 2)
        self.assertIn("Ana Torres", salida.getvalue())
        self.assertIn("Pedro León", salida.getvalue())
        self.assertIn("Hasta luego", salida.getvalue())


if __name__ == "__main__":
    unittest.main()
