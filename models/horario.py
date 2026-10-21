import re

class Horario:
    
    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.set_dia(dia)
        self.set_hora_inicio(hora_inicio)
        self.set_hora_fin(hora_fin)
        self.set_salon(salon)
        
    def get_dia(self):
        return self.__dia
    
    def set_dia(self, dia):
        
        # Se define la lista de opciones validas
        dias_validados = ["lunes", "martes", "miercoles","miércoles", "jueves", "viernes", "sabado", "sábado", "domingo"]
        
        # Se verifica que no esté vacío y sea un texto
        if dia is not None and isinstance(dia, str) and len(dia.strip()) > 0:
            
            # Se limpian espacios extra y convertimos a minúsculas para comparar fácilmente
            dia_limpio = dia.strip().lower()
            
            # Verificamos si lo que escribió el usuario está en nuestra lista permitida
            if dia_limpio in dias_validados:
                self.__dia = dia_limpio.capitalize()
            
            # Verificamos si lo que escribió el usuario está en nuestra lista permitida    
            else:
                raise ValueError("Día inválido. Debes elegir entre: Lunes, Martes, Miércoles, Jueves, Viernes, Sábado o Domingo.")
        
        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe un día válido.")
    
    def set_hora_inicio(self, hora_inicio):
        if hora_inicio is not None and isinstance(hora_inicio, str) and len(hora_inicio.strip()) > 0:
            hora_limpia = hora_inicio.strip()
            
            # La expresión regular comprueba que la hora vaya de 00 a 23 y los minutos de 00 a 59
            if re.fullmatch(r"([01]?[0-9]|2[0-3]):[0-5][0-9]", hora_limpia):
                self.__hora_inicio = hora_limpia
            else:
                raise ValueError("La hora de inicio debe tener un formato válido de 24 horas (HH:MM), por ejemplo: 07:00 o 14:30.")
        else:
            raise ValueError("La hora de inicio no puede estar vacía.")

    def set_hora_fin(self, hora_fin):
        if hora_fin is not None and isinstance(hora_fin, str) and len(hora_fin.strip()) > 0:
            hora_limpia = hora_fin.strip()
            
            # Comprobamos el mismo formato estricto para la hora de salida
            if re.fullmatch(r"([01]?[0-9]|2[0-3]):[0-5][0-9]", hora_limpia):
                self.__hora_fin = hora_limpia
            else:
                raise ValueError("La hora de finalización debe tener un formato válido de 24 horas (HH:MM), por ejemplo: 09:00 o 16:00.")
        else:
            raise ValueError("La hora de finalización no puede estar vacía.")
        
    def get_salon(self):
        return self.__salon

    def set_salon(self, salon):
        if salon is not None and isinstance(salon, str) and len(salon.strip()) > 0:
            self.__salon = salon
        else:
            raise ValueError("El salón no puede estar vacío. Por favor, asigna un salón.")

    # Método adicional para mostrar la información del horario de forma legible
    def mostrar_horario(self):
        return f"{self.get_dia()} de {self.get_hora_inicio()} a {self.get_hora_fin()} en el salón {self.get_salon()}"