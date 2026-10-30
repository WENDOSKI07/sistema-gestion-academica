from exceptions.academicas import AsignaturaInexistenteError, ProgramaInexistenteError


def limpiar_codigo(codigo):
    # Quitamos espacios y pasamos a mayúsculas para que "pro1" y "PRO1" sean iguales
    codigo = str(codigo).strip().upper()
    # Si el usuario no escribe nada no tiene sentido buscar
    if codigo == "":
        raise ValueError("El código a buscar no puede estar vacío.")
    return codigo


def buscar_asignatura_por_codigo(asignaturas, codigo):
    codigo_buscado = limpiar_codigo(codigo)
    # Recorremos la lista y comparamos con el código de cada asignatura
    for asignatura in asignaturas:
        if asignatura.get_code().strip().upper() == codigo_buscado:
            # Devolvemos el mismo objeto para poder usarlo después en el grupo
            return asignatura
    # Si terminamos de recorrer y no apareció, lanzamos la excepción en vez de devolver None
    raise AsignaturaInexistenteError(codigo)


def buscar_programa_por_codigo(programas, codigo):
    codigo_buscado = limpiar_codigo(codigo)
    # Hacemos lo mismo que con las asignaturas, pero con los programas
    for programa in programas:
        if programa.get_code().strip().upper() == codigo_buscado:
            return programa
    raise ProgramaInexistenteError(codigo)
