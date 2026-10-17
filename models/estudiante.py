from models.persona import Person

# La clase Student representa al estudiante dentro del sistema académico.
# Hereda las características principales de una persona, como su identificación, nombre y correo electrónico.
class Student(Person):
    # El constructor recibe los datos iniciales del estudiante y los guarda en atributos propios de la clase.
    def __init__(self, identification, name, email, id_student, academic_program, semester, cumulative_GPA):
        # Se invoca el constructor de la clase padre para reutilizar la información general de la persona.
        super().__init__(identification, name, email)
        # Cada dato del estudiante se valida antes de ser asignado.
        self.set_id_student(id_student)
        self.set_academic_program(academic_program)
        self.set_semester(semester)
        self.set_cumulative_GPA(cumulative_GPA)

    # Este método devuelve el código o identificación del estudiante.
    def get_id_student(self):
        return self.__id_student

    # Este setter guarda el ID del estudiante solo si es un texto válido y no está vacío.
    def set_id_student(self, id_student):
        if (id_student is not None and isinstance(id_student, str) and len(id_student.strip()) > 0):
            self.__id_student = id_student
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe un ID de estudiante")

    # Este método devuelve el programa académico que cursa el estudiante.
    def get_academic_program(self):
        return self.__academic_program

    # Este setter valida que el programa académico sea una cadena con contenido útil.
    def set_academic_program(self, academic_program):
        if (academic_program is not None and isinstance(academic_program, str) and len(academic_program.strip()) > 0):
            self.__academic_program = academic_program
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe un programa académico.")

    # Este método devuelve el semestre actual del estudiante.
    def get_semester(self):
        return self.__semester

    # Este setter permite guardar el semestre solo si es un número entero positivo.
    def set_semester(self, semester):
        if (semester is not None and isinstance(semester, int) and semester > 0):
            self.__semester = semester
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe el número del semestre que estás cursando.")

    # Este método devuelve el promedio acumulado del estudiante.
    def get_cumulative_GPA(self):
        return self.__cumulative_GPA

    # Este setter valida que el promedio esté dentro del rango permitido entre 0.0 y 5.0.
    def set_cumulative_GPA(self, cumulative_GPA):
        if (cumulative_GPA is not None and isinstance(cumulative_GPA, float) and 0.0 <= cumulative_GPA <= 5.0):
            self.__cumulative_GPA = cumulative_GPA
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe tu promedio acumulado (debe ser un número entre 0.0 a 5.0).")

    # Este método presenta la información del estudiante junto con los datos heredados de la persona.
    def show_info(self):
        return f"{super().show_info()} | ID Estudiante: {self.get_id_student()} | Programa Académico: {self.get_academic_program()} | Semestre: {self.get_semester()} | Promedio acumulado: {self.get_cumulative_GPA()}"

    # Este método describe la actividad principal que realiza el estudiante durante su formación académica.
    def perform_main_activity(self):
        return f"Estudio el programa de {self.get_academic_program()} y me encuentro en el semestre {self.get_semester()}."