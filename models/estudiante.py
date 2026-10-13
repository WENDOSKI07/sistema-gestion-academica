from models.persona import Person

class Student(Person):
    def __init__(self, identification, name, email, id_student, academic_program, semester,cumulative_GPA):
        super().__init__(identification, name, email)
        self.set_id_student(id_student)
        
    def get_id_student(self):
            return self.__id_student
        
    def set_id_student(self, id_student):
        if(id_student is not None and isinstance(id_student, str) and len(id_student.strip()) > 0):
                self.__id_student = id_student
                
        else:
                raise ValueError("Este campo no puede estar vacío. Por favor, escribe un ID de estudiante")