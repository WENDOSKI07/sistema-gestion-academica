import unittest
from types import SimpleNamespace

from controllers.busquedas import (
    buscar_asignatura_por_codigo,
    buscar_programa_por_codigo,
)
from exceptions.academicas import (
    EXCEPCIONES_ACADEMICAS,
    AsignaturaInexistenteError,
    ProgramaInexistenteError,
)


class AsignaturaConPropiedad:
    def __init__(self, codigo, nombre):
        self.__codigo = codigo
        self.nombre = nombre

    @property
    def codigo(self):
        return self.__codigo


class ProgramaConGetter:
    def __init__(self, codigo, nombre):
        self.__codigo = codigo
        self.nombre = nombre

    def get_code(self):
        return self.__codigo


class TestBuscarAsignatura(unittest.TestCase):
    def setUp(self):
        self.programacion = AsignaturaConPropiedad("PROG1", "Programación I")
        self.calculo = AsignaturaConPropiedad("CALC1", "Cálculo I")
        self.asignaturas = [self.programacion, self.calculo]

    def test_encuentra_y_devuelve_el_mismo_objeto(self):
        encontrada = buscar_asignatura_por_codigo(self.asignaturas, "CALC1")
        self.assertIs(encontrada, self.calculo)

    def test_ignora_mayusculas_y_espacios(self):
        encontrada = buscar_asignatura_por_codigo(self.asignaturas, "  prog1 ")
        self.assertIs(encontrada, self.programacion)

    def test_funciona_con_diccionario_por_codigo(self):
        por_codigo = {"PROG1": self.programacion, "CALC1": self.calculo}
        self.assertIs(buscar_asignatura_por_codigo(por_codigo, "calc1"), self.calculo)

    def test_funciona_con_atributo_publico(self):
        fisica = SimpleNamespace(codigo="FIS1", nombre="Física I")
        self.assertIs(buscar_asignatura_por_codigo([fisica], "FIS1"), fisica)

    def test_acepta_codigo_numerico(self):
        estadistica = SimpleNamespace(codigo=301, nombre="Estadística")
        self.assertIs(buscar_asignatura_por_codigo([estadistica], 301), estadistica)
        self.assertIs(buscar_asignatura_por_codigo([estadistica], "301"), estadistica)

    def test_lanza_excepcion_propia_si_no_existe(self):
        with self.assertRaises(AsignaturaInexistenteError) as contexto:
            buscar_asignatura_por_codigo(self.asignaturas, "XYZ999")
        self.assertEqual(contexto.exception.codigo, "XYZ999")
        self.assertIn("XYZ999", str(contexto.exception))

    def test_lanza_excepcion_propia_si_la_coleccion_esta_vacia(self):
        with self.assertRaises(AsignaturaInexistenteError):
            buscar_asignatura_por_codigo([], "PROG1")


class TestBuscarPrograma(unittest.TestCase):
    def setUp(self):
        self.analitica = ProgramaConGetter("IAD", "Ingeniería en Analítica de Datos")
        self.sistemas = ProgramaConGetter("ISC", "Ingeniería de Sistemas")
        self.programas = [self.analitica, self.sistemas]

    def test_encuentra_programa_con_get_code(self):
        self.assertIs(buscar_programa_por_codigo(self.programas, "isc"), self.sistemas)

    def test_lanza_excepcion_propia_si_no_existe(self):
        with self.assertRaises(ProgramaInexistenteError) as contexto:
            buscar_programa_por_codigo(self.programas, "MED")
        self.assertEqual(contexto.exception.codigo, "MED")

    def test_no_confunde_las_dos_excepciones(self):
        with self.assertRaises(ProgramaInexistenteError):
            buscar_programa_por_codigo(self.programas, "NADA")
        try:
            buscar_programa_por_codigo(self.programas, "NADA")
        except AsignaturaInexistenteError:
            self.fail("Se lanzó la excepción de asignatura en vez de la de programa")
        except ProgramaInexistenteError:
            pass


class TestEntradasInvalidas(unittest.TestCase):
    def setUp(self):
        self.asignaturas = [SimpleNamespace(codigo="PROG1")]

    def test_codigo_vacio(self):
        for codigo in ("", "   "):
            with self.subTest(codigo=repr(codigo)), self.assertRaises(ValueError):
                buscar_asignatura_por_codigo(self.asignaturas, codigo)

    def test_codigo_de_tipo_invalido(self):
        for codigo in (None, 3.5, True, ["PROG1"]):
            with self.subTest(codigo=repr(codigo)), self.assertRaises(TypeError):
                buscar_asignatura_por_codigo(self.asignaturas, codigo)

    def test_coleccion_invalida(self):
        for coleccion in (None, "PROG1", 42):
            with self.subTest(coleccion=repr(coleccion)), self.assertRaises(TypeError):
                buscar_programa_por_codigo(coleccion, "PROG1")

    def test_elemento_sin_codigo(self):
        with self.assertRaises(TypeError):
            buscar_asignatura_por_codigo([SimpleNamespace(nombre="Sin código")], "X")


class TestFlujoContinuaTrasLasExcepciones(unittest.TestCase):
    def test_busquedas_seguidas_con_errores_intermedios(self):
        asignaturas = [SimpleNamespace(codigo="PROG1"), SimpleNamespace(codigo="CALC1")]
        programas = [SimpleNamespace(codigo="IAD")]
        pedidos = [
            (buscar_asignatura_por_codigo, asignaturas, "PROG1"),
            (buscar_asignatura_por_codigo, asignaturas, "XYZ999"),
            (buscar_programa_por_codigo, programas, "MED"),
            (buscar_programa_por_codigo, programas, "IAD"),
        ]
        resultados = []
        for funcion, coleccion, codigo in pedidos:
            try:
                resultados.append(funcion(coleccion, codigo).codigo)
            except EXCEPCIONES_ACADEMICAS as error:
                resultados.append(type(error).__name__)

        self.assertEqual(
            resultados,
            ["PROG1", "AsignaturaInexistenteError", "ProgramaInexistenteError", "IAD"],
        )


if __name__ == "__main__":
    unittest.main()