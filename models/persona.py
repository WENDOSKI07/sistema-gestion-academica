class Person:
    
    def __init__(self, identification, name, email):
        self.set_identification(identification)
        
    def get_identification(self):
        return self.__identification
    
    def set_identification(self, identification):
        if(identification is not None and isinstance(identification, str) and len(identification.strip()) > 0):
            self.__identification = identification
            
        else:
            raise ValueError("Identificación no válida. Debe ser una cadena de texto no vacía.")
        