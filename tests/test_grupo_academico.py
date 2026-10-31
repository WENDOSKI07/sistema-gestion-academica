import unittest

from exceptions.academicas import (
    EstudianteDuplicadoError, EstudianteNoMatriculadoError, GrupoLlenoError,
)
from models.asignatura import Asignatura
from models.docente import Teacher
from models.estudiante import Student
from models.grupo_academico import GrupoAcademico
from models.programa_academico import AcademicProgram


class GrupoAcademicoTest(unittest.TestCase):
    def setUp(self):
        # Creamos los datos directamente sin depender del menú ni de main
        programa = AcademicProgram("SIS", "Sistemas", "Ingenierías", 10)
        self.asignatura = Asignatura("PRO1", "Programación I", programa, 3)
        self.docente = Teacher("D1", "Docente", "docente@example.com", "DOC1", "Sistemas", "Completo", 40)
        self.ana = self.crear_estudiante("P1", "EST001", "Ana")
        self.luis = self.crear_estudiante("P2", "EST002", "Luis")
        self.grupo = self.crear_grupo()

    def crear_estudiante(self, identificacion, codigo, nombre):
        return Student(identificacion, nombre, "prueba@example.com", codigo, "Sistemas", 1, 4.0)

    def crear_grupo(self, capacidad=2):
        return GrupoAcademico("G1", self.asignatura, self.docente, capacidad,
                              "lunes", "07:00", "09:00", "101")

    def test_matricular_guarda_el_objeto_original(self):
        self.grupo.matricular_estudiante(self.ana)
        self.assertIs(self.grupo.get_estudiantes_matriculados()[0], self.ana)

    def test_rechazar_otro_objeto_con_el_mismo_codigo(self):
        self.grupo.matricular_estudiante(self.ana)
        otra_ana = self.crear_estudiante("P3", "EST001", "Otra Ana")
        with self.assertRaises(EstudianteDuplicadoError):
            self.grupo.matricular_estudiante(otra_ana)
        self.assertEqual(self.grupo.get_estudiantes_matriculados(), [self.ana])

    def test_duplicado_se_informa_aunque_el_grupo_este_lleno(self):
        grupo = self.crear_grupo(1)
        grupo.matricular_estudiante(self.ana)
        with self.assertRaises(EstudianteDuplicadoError):
            grupo.matricular_estudiante(self.ana)

    def test_cupo_lleno_conserva_los_matriculados(self):
        grupo = self.crear_grupo(1)
        grupo.matricular_estudiante(self.ana)
        with self.assertRaises(GrupoLlenoError):
            grupo.matricular_estudiante(self.luis)
        self.assertEqual(grupo.get_estudiantes_matriculados(), [self.ana])

    def test_retirar_por_codigo_estudiantil_libera_el_cupo(self):
        grupo = self.crear_grupo(1)
        grupo.matricular_estudiante(self.ana)
        grupo.retirar_estudiante("EST001")
        grupo.matricular_estudiante(self.luis)
        self.assertEqual(grupo.get_estudiantes_matriculados(), [self.luis])

    def test_retiro_inexistente_no_elimina_a_otro_estudiante(self):
        self.grupo.matricular_estudiante(self.ana)
        with self.assertRaises(EstudianteNoMatriculadoError):
            self.grupo.retirar_estudiante("EST999")
        self.assertEqual(self.grupo.get_estudiantes_matriculados(), [self.ana])

    def test_rechazar_matricula_de_un_docente(self):
        with self.assertRaises(ValueError):
            self.grupo.matricular_estudiante(self.docente)
        self.assertEqual(self.grupo.get_estudiantes_matriculados(), [])

    def test_rechazar_capacidad_invalida_al_crear_el_grupo(self):
        for capacidad in [0, -1, 1.5, "2", None, True, False]:
            with self.subTest(capacidad=capacidad):
                with self.assertRaises(ValueError):
                    self.crear_grupo(capacidad)

    def test_no_reducir_capacidad_por_debajo_de_los_matriculados(self):
        self.grupo.matricular_estudiante(self.ana)
        self.grupo.matricular_estudiante(self.luis)
        with self.assertRaises(ValueError):
            self.grupo.set_capacidad_maxima(1)
        self.assertEqual(self.grupo.get_capacidad_maxima(), 2)

    def test_rechazar_nombres_en_lugar_de_objetos(self):
        for actualizar, dato in [(self.grupo.set_asignatura, "Programación I"),
                                 (self.grupo.set_docente, "Docente")]:
            with self.subTest(campo=actualizar.__name__):
                with self.assertRaises(ValueError):
                    actualizar(dato)
        self.assertIs(self.grupo.get_asignatura(), self.asignatura)
        self.assertIs(self.grupo.get_docente(), self.docente)

    def test_consultar_estudiantes_antes_y_despues_de_matricular(self):
        self.assertIn("No hay estudiantes matriculados", self.grupo.mostrar_estudiantes())
        self.grupo.matricular_estudiante(self.ana)
        self.assertIn("Ana", self.grupo.mostrar_estudiantes())

    def test_las_matriculas_de_un_grupo_no_modifican_otro(self):
        otro = self.crear_grupo()
        self.grupo.matricular_estudiante(self.ana)
        self.assertEqual(otro.get_estudiantes_matriculados(), [])
        self.assertIsNot(self.grupo.get_horario(), otro.get_horario())


if __name__ == "__main__":
    unittest.main()
