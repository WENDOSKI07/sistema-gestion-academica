from  models.persona import Person

class Teacher(Person):
    def __init__(self, identification, name, email, id_employee, deparment, employment_type, weekly_hours):
        super().__init__(identification, name, email)
        self.set_id_employee(id_employee)
        self.set_deparment(deparment)
        self.set_employment_type(employment_type)
        self.set_weekly_hours(weekly_hours)
        
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
            raise ValueError("Este campo no puede estar vacío, Por favor, escribe tu facultad.")
        
    def get_employment_type(self):
        return self.__employment_type
    
    def set_employment_type(self, employment_type):
        if(employment_type is not None and isinstance(employment_type, str) and len(employment_type.strip()) > 0):
            self.__employment_type = employment_type
            
        else:
            raise ValueError("Este campo no puede estar vacío, Por favor, escribe tu tipo de contratación.")
        
    def get_weekly_hours(self):
        return self.__weekly_hours
    
    def set_weekly_hours(self, weekly_hours):
        if(weekly_hours is not None and isinstance(weekly_hours, int) and weekly_hours  > 0):
            self.__weekly_hours = weekly_hours
        
        else:
            raise ValueError("Este campo no puede estar vacío, Por favor, escribe tus horas semanales.")
        
    def show_info(self):
        return f"{super().show_info()} | ID Empleado: {self.get_id_employee()} | Departamento: {self.get_department()} | Tipo de Empleo: {self.get_employment_type()} | Horas Semanales: {self.get_weekly_hours()}"
    
    def perform_main_activity(self):
        return f"Oriento clases en la facultad de {self.get_depatment()}."