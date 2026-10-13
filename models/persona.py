class Person:
    
    def __init__(self, identification, name, email):
        self.set_identification(identification)
        self.set_name(name)
        
    def get_identification(self):
        return self.__identification
    
    def set_identification(self, identification):
        if(identification is not None and isinstance(identification, str) and len(identification.strip()) > 0):
            self.__identification = identification
            
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe una identificación")
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if(name is not None and isinstance(name, str) and len(name.strip()) > 0):
            self.__name = name
            
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe un nombre.")