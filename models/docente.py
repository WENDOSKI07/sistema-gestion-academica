from  models.persona import Person

class Teacher(Person):
    def __init__(self, identification, name, email, id_employee, deparment, employment_type, weekly_hours):
        super().__init__(identification, name, email)
        self.set_id_employee(id_employee)
        self.set_deparment(deparment)
        self.set_employment_type(employment_type)
        
    def get_id_employee(self):
        return self.__id_employee
    
    def set_id_employee(self, id_employee):
        if(id_employee is not None and isinstance(id_employee, str) and len(id_employee.strip()) > 0 ):
            self.__id_employee = id_employee
            
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe un ID de empleado.")
        
    def get_deparment(self):
        return self.__deparment
    
    def set_deparment(self, deparment):
        if(deparment is not None and isinstance(deparment, str) and len(deparment.strip()) > 0):
            self.__deparment = deparment
        
        else:
            raise ValueError("Este campo no puede estar vacío, Por favor, escribe  tu facultad.")
        
    def get_employment_type(self):
        return self.__employment_type
    
    def set_employment_type(self, employment_type):
        if(employment_type is not None and isinstance(employment_type, str) and len(employment_type.strip()) > 0):
            self.__employment_type = employment_type
            
        else:
            raise ValueError("Este campo no puede estar vacío, Por favor, escribe  tu tipo de contratación.")