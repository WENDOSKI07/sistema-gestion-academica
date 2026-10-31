import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from main import main


class IntegracionBusquedasTest(unittest.TestCase):
    def ejecutar_menu(self, opciones):
        salida = StringIO()
        with patch("builtins.input", side_effect=opciones) as entrada:
            with redirect_stdout(salida):
                main()
        self.assertEqual(entrada.call_count, len(opciones))
        self.assertIn("Hasta luego", salida.getvalue())
        return salida.getvalue()

    def test_buscar_programa_y_asignatura_con_espacios_y_minusculas(self):
        texto = self.ejecutar_menu(["2", "3", " sis ", "", "0", "3", "3", " pro1 ", "", "0", "0"])
        self.assertIn("Ingeniería de Sistemas", texto)
        self.assertIn("Programación I", texto)
        self.assertNotIn("Volviendo al menú principal", texto)

    def test_recuperarse_de_ambas_busquedas_inexistentes(self):
        # Cada error vuelve al menú principal y permite entrar otra vez a un área
        texto = self.ejecutar_menu([
            "2", "3", "NO_EXISTE", "3", "3", "NO_EXISTE",
            "3", "3", "PRO1", "", "0", "0",
        ])
        self.assertIn("No existe ningún programa académico", texto)
        self.assertIn("No existe ninguna asignatura", texto)
        self.assertIn("Programación I", texto)
        self.assertEqual(texto.count("Volviendo al menú principal"), 2)

    def test_rechazar_codigos_vacios_y_continuar(self):
        texto = self.ejecutar_menu(["2", "3", "   ", "3", "3", "", "0"])
        self.assertEqual(texto.count("El código a buscar no puede estar vacío"), 2)

    def test_conservar_actualizacion_despues_de_un_error(self):
        # Una excepción no debe volver a crear los programas con sus valores iniciales
        texto = self.ejecutar_menu([
            "2", "2", "SIS", "9", "3", "NO_EXISTE",
            "2", "2", "SIS", "8", "0", "0",
        ])
        self.assertIn("Semestres actuales: 9", texto)
        self.assertIn("Semestres actualizados: 8", texto)


if __name__ == "__main__":
    unittest.main()
