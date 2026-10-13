from models.persona import Person

class Student(Person):
    def __init__(self, identification, name, email, id_student, academic_program, semester,cumulative_GPA):
        super().__init__(identification, name, email)
        self.set_id_student(id_student)
        self.set_academic_program(academic_program)
        
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
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe un programa académico")