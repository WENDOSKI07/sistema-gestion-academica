from models.persona import Person

class Administrative(Person):
    
    def __init__(self, identification, name, email, id_employee, deparment, possition, work_schedule):
        super().__init__(identification, name, email)
        self.set_id_employee(id_employee)
        self.set_deparment(deparment)
        self.set_possition(possition)
        self.set_work_schedule(work_schedule)
        
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
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe tu dependencia.")
        
    def get_possition(self):
        return (self.__position)
    
    def set_possition(self, possition):
        if(possition is not None and isinstance(possition, str) and len(possition.strip()) > 0):
            self.__possition = possition
            
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe tu cargo.")
    
    def get_work_schedule(self):
        return self.__work_schedule
    
    def set_work_schedule(self, work_schedule):
        if(work_schedule is not None and isinstance(work_schedule, str) and len(work_schedule.strip()) > 0):
            self.__work_schedule = work_schedule
            
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe tu jornada.")

    
    