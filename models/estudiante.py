from models.persona import Person

class Student(Person):
    def __init__(self, identification, name, email, id_student, academic_program, semester,cumulative_GPA):
        super().__init__(identification, name, email)

