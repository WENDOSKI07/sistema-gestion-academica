from  models.persona import Person

class Teacher(Person):
    def __init__(self, identification, name, email, id_employee, deparment, employment_type, weekly_hours):
        super().__init__(identification, name, email)