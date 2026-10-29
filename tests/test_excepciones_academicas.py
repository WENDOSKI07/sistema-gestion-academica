import unittest

from exceptions.academicas import (
    EXCEPCIONES_ACADEMICAS,
    AsignaturaInexistenteError,
    EstudianteDuplicadoError,
    EstudianteNoMatriculadoError,
    GrupoLlenoError,
    ProgramaInexistenteError,
)


def _lanzar(error):
    raise error


class TestDefinicionDeExcepciones(unittest.TestCase):
    def test_hay_cinco_excepciones_distintas(self):
        self.assertEqual(len(EXCEPCIONES_ACADEMICAS), 5)
        self.assertEqual(len(set(EXCEPCIONES_ACADEMICAS)), 5)

    def test_cada_una_hereda_directamente_de_exception(self):
        for clase in EXCEPCIONES_ACADEMICAS:
            with self.subTest(excepcion=clase.__name__):
                self.assertIn(Exception, clase.__bases__)


class TestMensajesYAtributos(unittest.TestCase):
    def test_estudiante_duplicado(self):
        error = EstudianteDuplicadoError("2024001", "PROG1-G1")
        self.assertEqual(error.codigo_estudiantil, "2024001")
        self.assertEqual(error.codigo_grupo, "PROG1-G1")
        self.assertEqual(
            str(error),
            "El estudiante con código 2024001 ya está matriculado en el grupo PROG1-G1.",
        )

    def test_grupo_lleno(self):
        error = GrupoLlenoError("PROG1-G2", 2)
        self.assertEqual(error.capacidad_maxima, 2)
        self.assertIn("PROG1-G2", str(error))
        self.assertIn("capacidad máxima de 2", str(error))

    def test_estudiante_no_matriculado(self):
        error = EstudianteNoMatriculadoError("9999", "PROG1-G1")
        self.assertIn("No se puede retirar", str(error))
        self.assertIn("9999", str(error))
        self.assertIn("PROG1-G1", str(error))

    def test_asignatura_inexistente(self):
        error = AsignaturaInexistenteError("XYZ999")
        self.assertEqual(error.codigo, "XYZ999")
        self.assertIn("asignatura", str(error))

    def test_programa_inexistente(self):
        error = ProgramaInexistenteError("ING-000")
        self.assertEqual(error.codigo, "ING-000")
        self.assertIn("programa académico", str(error))

    def test_acepta_codigos_numericos_y_limpia_espacios(self):
        error = EstudianteDuplicadoError(2024001, "  G1  ")
        self.assertEqual(error.codigo_estudiantil, "2024001")
        self.assertEqual(error.codigo_grupo, "G1")


class TestLanzarCapturarYContinuar(unittest.TestCase):
    def test_se_lanzan_y_capturan_por_su_clase(self):
        casos = [
            (EstudianteDuplicadoError, ("1", "G1")),
            (GrupoLlenoError, ("G1", 30)),
            (EstudianteNoMatriculadoError, ("1", "G1")),
            (AsignaturaInexistenteError, ("A1",)),
            (ProgramaInexistenteError, ("P1",)),
        ]
        for clase, argumentos in casos:
            with self.subTest(excepcion=clase.__name__), self.assertRaises(clase):
                raise clase(*argumentos)

    def test_el_programa_continua_despues_de_cada_excepcion(self):
        operaciones = [
            lambda: _lanzar(EstudianteDuplicadoError("1", "G1")),
            lambda: "matrícula correcta",
            lambda: _lanzar(GrupoLlenoError("G1", 1)),
            lambda: _lanzar(ProgramaInexistenteError("P0")),
            lambda: "retiro correcto",
        ]
        mensajes = []
        for operacion in operaciones:
            try:
                mensajes.append(operacion())
            except EXCEPCIONES_ACADEMICAS as error:
                mensajes.append(f"Aviso: {error}")

        self.assertEqual(len(mensajes), len(operaciones))
        self.assertEqual(mensajes[1], "matrícula correcta")
        self.assertEqual(mensajes[4], "retiro correcto")
        self.assertTrue(mensajes[0].startswith("Aviso: "))


if __name__ == "__main__":
    unittest.main()