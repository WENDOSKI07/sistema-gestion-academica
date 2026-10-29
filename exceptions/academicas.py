from __future__ import annotations

__all__ = [
    "EXCEPCIONES_ACADEMICAS",
    "AsignaturaInexistenteError",
    "EstudianteDuplicadoError",
    "EstudianteNoMatriculadoError",
    "GrupoLlenoError",
    "ProgramaInexistenteError",
]


def _como_texto(valor: object) -> str:
    return str(valor).strip()


class EstudianteDuplicadoError(Exception):
    def __init__(self, codigo_estudiantil: object, codigo_grupo: object) -> None:
        self.codigo_estudiantil = _como_texto(codigo_estudiantil)
        self.codigo_grupo = _como_texto(codigo_grupo)
        super().__init__(
            f"El estudiante con código {self.codigo_estudiantil} ya está "
            f"matriculado en el grupo {self.codigo_grupo}."
        )


class GrupoLlenoError(Exception):
    def __init__(self, codigo_grupo: object, capacidad_maxima: int) -> None:
        self.codigo_grupo = _como_texto(codigo_grupo)
        self.capacidad_maxima = capacidad_maxima
        super().__init__(
            f"El grupo {self.codigo_grupo} alcanzó su capacidad máxima de "
            f"{self.capacidad_maxima} estudiantes. No quedan cupos disponibles."
        )


class EstudianteNoMatriculadoError(Exception):
    def __init__(self, codigo_estudiantil: object, codigo_grupo: object) -> None:
        self.codigo_estudiantil = _como_texto(codigo_estudiantil)
        self.codigo_grupo = _como_texto(codigo_grupo)
        super().__init__(
            f"No se puede retirar al estudiante con código "
            f"{self.codigo_estudiantil} porque no está matriculado en el "
            f"grupo {self.codigo_grupo}."
        )


class AsignaturaInexistenteError(Exception):
    def __init__(self, codigo: object) -> None:
        self.codigo = _como_texto(codigo)
        super().__init__(
            f"No existe ninguna asignatura registrada con el código {self.codigo}."
        )


class ProgramaInexistenteError(Exception):
    def __init__(self, codigo: object) -> None:
        self.codigo = _como_texto(codigo)
        super().__init__(
            f"No existe ningún programa académico registrado con el código "
            f"{self.codigo}."
        )


EXCEPCIONES_ACADEMICAS: tuple[type[Exception], ...] = (
    EstudianteDuplicadoError,
    GrupoLlenoError,
    EstudianteNoMatriculadoError,
    AsignaturaInexistenteError,
    ProgramaInexistenteError,
)