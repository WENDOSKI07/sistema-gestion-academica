from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

from exceptions.academicas import AsignaturaInexistenteError, ProgramaInexistenteError

__all__ = [
    "ATRIBUTOS_CODIGO",
    "buscar_asignatura_por_codigo",
    "buscar_programa_por_codigo",
]

ATRIBUTOS_CODIGO: tuple[str, ...] = (
    "codigo",
    "get_codigo",
    "obtener_codigo",
    "code",
    "get_code",
)

_NO_ENCONTRADO = object()


def _normalizar(codigo: object) -> str:
    return str(codigo).strip().upper()


def _validar_codigo(codigo: object) -> str:
    if isinstance(codigo, bool) or not isinstance(codigo, (str, int)):
        raise TypeError(
            f"El código a buscar debe ser texto o número; se recibió "
            f"{type(codigo).__name__}."
        )
    normalizado = _normalizar(codigo)
    if not normalizado:
        raise ValueError("El código a buscar no puede estar vacío.")
    return normalizado


def _validar_coleccion(coleccion: object, descripcion: str) -> None:
    if coleccion is None or isinstance(coleccion, (str, bytes)):
        raise TypeError(f"La colección de {descripcion} no es válida.")
    if not isinstance(coleccion, Iterable):
        raise TypeError(
            f"La colección de {descripcion} debe ser una lista o un "
            f"diccionario; se recibió {type(coleccion).__name__}."
        )


def _leer_codigo(objeto: object) -> Any:
    for nombre in ATRIBUTOS_CODIGO:
        if hasattr(objeto, nombre):
            valor = getattr(objeto, nombre)
            return valor() if callable(valor) else valor
    raise TypeError(
        f"El objeto {objeto!r} no tiene un código reconocible. Se buscó en: "
        f"{', '.join(ATRIBUTOS_CODIGO)}."
    )


def _buscar_por_codigo(coleccion: Iterable[Any], codigo_buscado: str) -> Any:
    if isinstance(coleccion, Mapping):
        for clave, valor in coleccion.items():
            if _normalizar(clave) == codigo_buscado:
                return valor
        elementos: Iterable[Any] = coleccion.values()
    else:
        elementos = coleccion

    for elemento in elementos:
        if _normalizar(_leer_codigo(elemento)) == codigo_buscado:
            return elemento
    return _NO_ENCONTRADO


def buscar_asignatura_por_codigo(asignaturas: Iterable[Any], codigo: str | int) -> Any:
    codigo_buscado = _validar_codigo(codigo)
    _validar_coleccion(asignaturas, "asignaturas")
    resultado = _buscar_por_codigo(asignaturas, codigo_buscado)
    if resultado is _NO_ENCONTRADO:
        raise AsignaturaInexistenteError(codigo)
    return resultado


def buscar_programa_por_codigo(programas: Iterable[Any], codigo: str | int) -> Any:
    codigo_buscado = _validar_codigo(codigo)
    _validar_coleccion(programas, "programas académicos")
    resultado = _buscar_por_codigo(programas, codigo_buscado)
    if resultado is _NO_ENCONTRADO:
        raise ProgramaInexistenteError(codigo)
    return resultado