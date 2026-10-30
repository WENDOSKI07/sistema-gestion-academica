from models.estudiante import Estudiante
from models.asignatura import Asignatura
from models.horario import Horario
from models.docente import Docente
from models.programa_academico import AcademicProgram

from exceptions.academicas import (
    EstudianteDuplicadoError,
    GrupoLlenoError,
    EstudianteNoMatriculadoError,
)

class GrupoAcademico:
    """Clase que representa un grupo académico con código, asignatura, docente, horario y estudiantes matriculados."""

    def __init__(self, code, asignatura, docente, capacidad_maxima, horario):
        self.set_code(code)
        self.set_asignatura(asignatura)
        self.set_docente(docente)
        self.__capacidad_maxima = capacidad_maxima
        self.set_horario(horario)
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
            raise ValueError("La asignatura debe ser una instancia de la clase Asignatura.")

    def get_docente(self):
        return self.__docente

    def set_docente(self, docente):
        if(isinstance(docente, Docente)):
            self.__docente = docente
        else:
            raise ValueError("El docente debe ser una instancia de la clase Docente.")

    def set_capacidad_maxima(self, capacidad_maxima):
        if isinstance(capacidad_maxima, int) and capacidad_maxima > 0:
            self.__capacidad_maxima = capacidad_maxima
        else:
            raise ValueError("La capacidad máxima debe ser un número entero positivo.")

    def get_capacidad_maxima(self):
        return self.__capacidad_maxima
        
    def get_horario(self):
        return self.__horario

    def set_horario(self, horario):
        if(isinstance(horario, Horario)):
            self.__horario = horario
        else:
            raise ValueError("El horario debe ser una instancia de la clase Horario.")

    def get_estudiantes_matriculados(self):
        return self.__estudiantes_matriculados
    
    def mostrar_informacion_grupo(self):
        return f"Código: {self.get_code()} 
        | Asignatura: {self.get_asignatura().get_nombre()} 
        | Docente: {self.get_docente().get_name()} 
        | Capacidad máxima: {self.get_capacidad_maxima()} 
        | Estudiantes matriculados: {len(self.get_estudiantes_matriculados())}
        | Horario: {self.get_horario().mostrar_informacion()}"
    
    def matricular_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise ValueError("El estudiante debe ser una instancia de la clase Estudiante.")

        if estudiante in self.__estudiantes_matriculados:
            raise EstudianteDuplicadoError(f"El estudiante {estudiante.get_name()} ya está matriculado en este grupo.")

        if len(self.__estudiantes_matriculados) >= self.__capacidad_maxima:
            raise GrupoLlenoError("No se puede matricular al estudiante. El grupo académico ha alcanzado su capacidad máxima.")

        self.__estudiantes_matriculados.append(estudiante)
    
    def retirar_estudiante(self, code_estudiante):
        estudiante_a_retirar = None
        for estudiante in self.__estudiantes_matriculados:
            if estudiante.get_identification() == code_estudiante:
                estudiante_a_retirar = estudiante
                break

        if estudiante_a_retirar is None:
            raise EstudianteNoMatriculadoError(f"El estudiante con código {code_estudiante} no está matriculado en este grupo.")

        self.__estudiantes_matriculados.remove(estudiante_a_retirar)

    def mostrar_estudiantes_matriculados(self):
        if not self.__estudiantes_matriculados:
            return "No hay estudiantes matriculados en este grupo académico."

        info_estudiantes = []
        for estudiante in self.__estudiantes_matriculados:
            info_estudiantes.append(estudiante.mostrar_informacion())
        
        return "\n".join(info_estudiantes)
