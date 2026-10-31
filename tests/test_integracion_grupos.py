import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from main import (
    crear_asignaturas_ejemplo, crear_grupos_ejemplo,
    crear_personas_ejemplo, crear_programas_ejemplo, main,
)


class IntegracionGruposTest(unittest.TestCase):
    def ejecutar_menu(self, opciones):
        salida = StringIO()
        with patch("builtins.input", side_effect=opciones) as entrada:
            with redirect_stdout(salida):
                main()
        self.assertEqual(entrada.call_count, len(opciones))
        self.assertIn("Hasta luego", salida.getvalue())
        return salida.getvalue()

    def test_grupos_comparten_entidades_y_tienen_horarios_propios(self):
        programas = crear_programas_ejemplo()
        asignaturas = crear_asignaturas_ejemplo(programas)
        _, _, docentes = crear_personas_ejemplo(programas)
        grupos = crear_grupos_ejemplo(asignaturas, docentes)
        self.assertEqual(len(grupos), 2)
        for grupo, asignatura, docente in zip(grupos, asignaturas, docentes):
            self.assertIs(grupo.get_asignatura(), asignatura)
            self.assertIs(grupo.get_docente(), docente)
        self.assertIsNot(grupos[0].get_horario(), grupos[1].get_horario())
        asignaturas[0].set_name("Materia actualizada")
        self.assertIn("Materia actualizada", grupos[0].mostrar_informacion_grupo())

    def test_matricular_consultar_y_retirar_desde_main(self):
        texto = self.ejecutar_menu([
            "4", "1", "", "3", "g1", "est001", "2", "g1", "",
            "4", "g1", "est001", "2", "g1", "", "0", "0",
        ])
        self.assertIn("Estudiante matriculado correctamente", texto)
        self.assertIn("Ana Torres", texto)
        self.assertIn("Estudiante retirado correctamente", texto)
        self.assertIn("No hay estudiantes matriculados", texto)
        self.assertIn("Lunes de 07:00 a 09:00", texto)
        self.assertIn("Martes de 10:00 a 12:00", texto)

    def test_controlar_los_tres_errores_y_conservar_las_matriculas(self):
        # Tras cada excepción volvemos a entrar desde el menú principal
        texto = self.ejecutar_menu([
            "4", "3", "G1", "EST001", "3", "G1", "EST001",
            "4", "3", "G1", "EST002",
            "4", "4", "G1", "EST999",
            "4", "2", "G1", "", "4", "G1", "EST001",
            "3", "G1", "EST002", "2", "G1", "", "0", "0",
        ])
        self.assertIn("ya está matriculado en el grupo G1", texto)
        self.assertIn("alcanzó su capacidad máxima de 1", texto)
        self.assertIn("No se puede retirar al estudiante con código EST999", texto)
        self.assertEqual(texto.count("Volviendo al menú principal"), 3)
        self.assertEqual(texto.count("Estudiante matriculado correctamente"), 2)
        self.assertIn("Luis Rojas", texto)

    def test_selecciones_invalidas_no_interrumpen_el_submenu(self):
        texto = self.ejecutar_menu([
            "4", "3", "", "3", "OTRO", "3", "G1", "",
            "3", "G1", "EST999", "4", "G1", "", "0", "0",
        ])
        self.assertIn("Escribe el código del grupo", texto)
        self.assertIn("No se encontró un grupo", texto)
        self.assertIn("No se encontró un estudiante", texto)
        self.assertNotIn("Estudiante matriculado correctamente", texto)


if __name__ == "__main__":
    unittest.main()
