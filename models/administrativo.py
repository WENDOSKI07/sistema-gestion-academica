from models.persona import Person

class Administrative(Person):
    
    def __init__(self, identification, name, email, id_employee, department, position, work_schedule):
        super().__init__(identification, name, email)