# En este archivo están las cinco excepciones del sistema
# Las tres de matrícula las usa el grupo académico y las dos de búsqueda las usa busquedas.py


# Todas heredan de Exception, así se pueden lanzar con raise y atrapar con except
class EstudianteDuplicadoError(Exception):
    # Se lanza cuando el estudiante ya está matriculado en el grupo
    def __init__(self, codigo_estudiantil, codigo_grupo):
        self.codigo_estudiantil = codigo_estudiantil
        self.codigo_grupo = codigo_grupo
        # Con super() le pasamos el mensaje a Exception para que se vea con print(error)
        super().__init__(
            f"El estudiante con código {codigo_estudiantil} ya está "
            f"matriculado en el grupo {codigo_grupo}."
        )


class GrupoLlenoError(Exception):
    # Se lanza cuando el grupo ya llegó a su capacidad máxima
    def __init__(self, codigo_grupo, capacidad_maxima):
        self.codigo_grupo = codigo_grupo
        self.capacidad_maxima = capacidad_maxima
        super().__init__(
            f"El grupo {codigo_grupo} alcanzó su capacidad máxima de "
            f"{capacidad_maxima} estudiantes. No quedan cupos disponibles."
        )


class EstudianteNoMatriculadoError(Exception):
    # Se lanza cuando se quiere retirar a alguien que no está en el grupo
    def __init__(self, codigo_estudiantil, codigo_grupo):
        self.codigo_estudiantil = codigo_estudiantil
        self.codigo_grupo = codigo_grupo
        super().__init__(
            f"No se puede retirar al estudiante con código {codigo_estudiantil} "
            f"porque no está matriculado en el grupo {codigo_grupo}."
        )


class AsignaturaInexistenteError(Exception):
    # Se lanza cuando se busca una asignatura con un código que no existe
    def __init__(self, codigo):
        self.codigo = codigo
        super().__init__(
            f"No existe ninguna asignatura registrada con el código {codigo}."
        )


class ProgramaInexistenteError(Exception):
    # Se lanza cuando se busca un programa con un código que no existe
    def __init__(self, codigo):
        self.codigo = codigo
        super().__init__(
            f"No existe ningún programa académico registrado con el código {codigo}."
        )


# Las juntamos en una tupla para atraparlas todas con un solo except en main.py
EXCEPCIONES_ACADEMICAS = (
    EstudianteDuplicadoError,
    GrupoLlenoError,
    EstudianteNoMatriculadoError,
    AsignaturaInexistenteError,
    ProgramaInexistenteError,
)
