import unittest

from exceptions.academicas import (
    EXCEPCIONES_ACADEMICAS,
    AsignaturaInexistenteError,
    EstudianteDuplicadoError,
    EstudianteNoMatriculadoError,
    GrupoLlenoError,
    ProgramaInexistenteError,
)


class TestExcepciones(unittest.TestCase):
    def test_todas_heredan_de_exception(self):
        # Revisamos que las cinco sean clases hijas de Exception
        for excepcion in EXCEPCIONES_ACADEMICAS:
            self.assertTrue(issubclass(excepcion, Exception))

    def test_mensaje_estudiante_duplicado(self):
        error = EstudianteDuplicadoError("EST001", "G1")
        self.assertEqual(
            str(error),
            "El estudiante con código EST001 ya está matriculado en el grupo G1.",
        )

    def test_mensaje_grupo_lleno(self):
        error = GrupoLlenoError("G1", 30)
        self.assertIn("capacidad máxima de 30", str(error))

    def test_mensaje_estudiante_no_matriculado(self):
        error = EstudianteNoMatriculadoError("EST009", "G1")
        self.assertIn("No se puede retirar", str(error))

    def test_mensaje_asignatura_inexistente(self):
        error = AsignaturaInexistenteError("XYZ")
        self.assertEqual(error.codigo, "XYZ")
        self.assertIn("asignatura", str(error))

    def test_mensaje_programa_inexistente(self):
        error = ProgramaInexistenteError("MED")
        self.assertEqual(error.codigo, "MED")
        self.assertIn("programa académico", str(error))

    def test_se_pueden_lanzar_y_atrapar(self):
        # Lanzamos cada una y comprobamos que el except la atrapa
        errores = [
            EstudianteDuplicadoError("EST001", "G1"),
            GrupoLlenoError("G1", 30),
            EstudianteNoMatriculadoError("EST009", "G1"),
            AsignaturaInexistenteError("XYZ"),
            ProgramaInexistenteError("MED"),
        ]
        atrapadas = 0
        for error in errores:
            try:
                raise error
            except EXCEPCIONES_ACADEMICAS:
                atrapadas = atrapadas + 1
        # Si llegamos aquí el programa siguió después de cada excepción
        self.assertEqual(atrapadas, 5)


if __name__ == "__main__":
    unittest.main()
