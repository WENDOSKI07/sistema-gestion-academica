from models.persona import Person

class Student(Person):
    def __init__(self, identification, name, email, id_student, academic_program, semester,cumulative_GPA):
        super().__init__(identification, name, email)
        self.set_id_student(id_student)
        self.set_academic_program(academic_program)
        self.set_semester(semester)
        self.set_cumulative_GPA(cumulative_GPA)
        
    def get_id_student(self):
        return self.__id_student
        
    def set_id_student(self, id_student):
        if(id_student is not None and isinstance(id_student, str) and len(id_student.strip()) > 0):
            self.__id_student = id_student
                
        else:
                raise ValueError("Este campo no puede estar vacío. Por favor, escribe un ID de estudiante")
            
    def get_academic_program(self):
        return self.__academic_program
    
    def set_academic_program(self, academic_program):
        if(academic_program is not None and isinstance(academic_program, str) and len(academic_program.strip()) > 0):
            self.__academic_program = academic_program
        
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe un programa académico.")
        
    def get_semester(self):
        return self.__semester
    
    def set_semester(self, semester):
        if(semester is not None and isinstance(semester, int) and semester > 0):
            self.__semester = semester
        
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe el número del semestre que estás cursando.")
        
    def get_cumulative_GPA(self):
        return self.__cumulative_GPA
    
    def set_cumulative_GPA(self, cumulative_GPA):
        if(cumulative_GPA is not None and isinstance(cumulative_GPA, float) and 0.0 <= cumulative_GPA <= 5.0):
            self.__cumulative_GPA = cumulative_GPA

        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe tu promedio acumulado (debe ser un número entre 0.0 a 5.0).")
        
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} | ID Estudiante: {self.get_id_student()} | Programa Académico: {self.get_academic_program()} | Semestre: {self.get_semester()} | Promedio acumulado: {self.get_cumulative_GPA()}"
    
    def realizar_actividad_principal(self):
        return f"Estudio el programa de {self.get_academic_program()} y me encuentro en el semestre {self.get_semester()}."