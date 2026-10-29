import unittest

from controllers.busquedas import buscar_asignatura_por_codigo, buscar_programa_por_codigo
from exceptions.academicas import AsignaturaInexistenteError, ProgramaInexistenteError
from models.asignatura import Asignatura
from models.programa_academico import AcademicProgram


class TestBusquedas(unittest.TestCase):
    def setUp(self):
        # Creamos los mismos datos de ejemplo que usa main.py
        self.sistemas = AcademicProgram(
            code="SIS",
            name="Ingeniería de Sistemas",
            faculty="Ciencias e Ingenierías",
            number_semesters=10,
        )
        self.administracion = AcademicProgram(
            code="ADM",
            name="Administración de Empresas",
            faculty="Ciencias Contables, Económicas y Administrativas",
            number_semesters=8,
        )
        self.programacion = Asignatura(
            code="PRO1",
            name="Programación I",
            academic_program=self.sistemas,
            number_credits=3,
        )
        self.programas = [self.sistemas, self.administracion]
        self.asignaturas = [self.programacion]

    def test_encuentra_asignatura(self):
        encontrada = buscar_asignatura_por_codigo(self.asignaturas, "PRO1")
        # Debe ser el mismo objeto que está en la lista
        self.assertIs(encontrada, self.programacion)

    def test_encuentra_asignatura_en_minusculas_y_con_espacios(self):
        encontrada = buscar_asignatura_por_codigo(self.asignaturas, "  pro1 ")
        self.assertIs(encontrada, self.programacion)

    def test_asignatura_inexistente_lanza_excepcion(self):
        with self.assertRaises(AsignaturaInexistenteError):
            buscar_asignatura_por_codigo(self.asignaturas, "XYZ")

    def test_encuentra_programa(self):
        encontrado = buscar_programa_por_codigo(self.programas, "adm")
        self.assertIs(encontrado, self.administracion)

    def test_programa_inexistente_lanza_excepcion(self):
        with self.assertRaises(ProgramaInexistenteError):
            buscar_programa_por_codigo(self.programas, "MED")

    def test_codigo_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            buscar_asignatura_por_codigo(self.asignaturas, "   ")

    def test_el_programa_sigue_despues_de_las_excepciones(self):
        # Simulamos lo que hará main.py: buscar, atrapar el error y seguir
        mensajes = []
        for codigo in ["XYZ", "PRO1"]:
            try:
                asignatura = buscar_asignatura_por_codigo(self.asignaturas, codigo)
                mensajes.append(asignatura.get_name())
            except AsignaturaInexistenteError as error:
                mensajes.append(str(error))
        self.assertEqual(len(mensajes), 2)
        self.assertEqual(mensajes[1], "Programación I")


if __name__ == "__main__":
    unittest.main()
