from models.estudiante import Student
from models.asignatura import Asignatura
from models.horario import Horario
from models.docente import Teacher

from exceptions.academicas import (
    EstudianteDuplicadoError,
    GrupoLlenoError,
    EstudianteNoMatriculadoError,
)

class GrupoAcademico:
    """Clase que representa un grupo académico con código, asignatura, docente, horario y estudiantes matriculados."""

    def __init__(self, code, asignatura, docente, capacidad_maxima,dia, hora_inicio, hora_fin, salon):
        self.set_code(code)
        self.set_asignatura(asignatura)
        self.set_docente(docente)
        self.set_capacidad_maxima(capacidad_maxima)
        self.__horario = Horario(dia, hora_inicio, hora_fin, salon)
        self.__estudiantes_matriculados = []

    def get_code(self):
        return self.__code

    def set_code(self, code):
        if(code is not None and isinstance(code, str) and len(code.strip()) > 0):
            self.__code = code

        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe el código del grupo académico.")

    def get_asignatura(self):
        return self.__asignatura

    def set_asignatura(self, asignatura):
        if(isinstance(asignatura, Asignatura)):
            self.__asignatura = asignatura
        else:
            raise ValueError("Selecciona una asignatura válida.")

    def get_docente(self):
        return self.__Teacher

    def set_docente(self, docente):
        if(isinstance(docente, Teacher)):
            self.__Teacher = docente
        else:
            raise ValueError("El docente seleccionado no existe. Selecciona un docente válido.")

    def set_capacidad_maxima(self, capacidad_maxima):
        if isinstance(capacidad_maxima, int) and capacidad_maxima > 0:
            self.__capacidad_maxima = capacidad_maxima
        else:
            raise ValueError("La capacidad máxima debe ser un número entero positivo.")

    def get_capacidad_maxima(self):
        return self.__capacidad_maxima
        
    def get_horario(self):
        return self.__horario

    
    def get_estudiantes_matriculados(self):
        return self.__estudiantes_matriculados

    def mostrar_informacion_grupo(self):
        return (
            f"Código: {self.get_code()} "
            f"| Asignatura: {self.get_asignatura().get_name()} "
            f"| Docente: {self.get_docente().get_name()} "
            f"| Capacidad máxima: {self.get_capacidad_maxima()} "
            f"| Estudiantes matriculados: {len(self.get_estudiantes_matriculados())} "
            f"| Horario: {self.get_horario().mostrar_horario()}"
        )
    
    def matricular_estudiante(self, estudiante):
        if not isinstance(estudiante, Student):
            raise ValueError("El estudiante no es válido.")

        for matriculado in self.__estudiantes_matriculados:
            if matriculado.get_id_student() == estudiante.get_id_student():
                raise EstudianteDuplicadoError(estudiante.get_id_student(), self.get_code())
    
        if len(self.__estudiantes_matriculados) >= self.__capacidad_maxima:
            raise GrupoLlenoError(self.get_code(), self.get_capacidad_maxima())

        self.__estudiantes_matriculados.append(estudiante)
    
    def retirar_estudiante(self, codigo_estudiantil):
        estudiante_a_retirar = None
        for estudiante in self.__estudiantes_matriculados:
            if estudiante.get_id_student() == codigo_estudiantil:
                estudiante_a_retirar = estudiante
                break

        if estudiante_a_retirar is None:
            raise EstudianteNoMatriculadoError(codigo_estudiantil, self.get_code())

        self.__estudiantes_matriculados.remove(estudiante_a_retirar)

    def mostrar_estudiantes(self):
        if not self.__estudiantes_matriculados:
            return "No hay estudiantes matriculados en este grupo académico."

        info_estudiantes = []
        for estudiante in self.__estudiantes_matriculados:
            info_estudiantes.append(estudiante.mostrar_informacion())
        
        return "\n".join(info_estudiantes)

