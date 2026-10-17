from models.programa_academico import AcademicProgram


class Subject:
    """Clase que representa una asignatura con código, nombre, programa académico y número de créditos."""

    def __init__(self, code, name, academic_program, number_credits):
        self.set_code(code)
        self.set_name(name)
        self.set_academic_program(academic_program)
        self.set_number_credits(number_credits)

    def get_code(self):
        return self.__code

    def set_code(self, code):
        if(code is not None and isinstance(code, str) and len(code.strip()) > 0):
            self.__code = code

        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe el código de la asignatura.")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if(name is not None and isinstance(name, str) and len(name.strip()) > 0):
            self.__name = name

        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe el nombre de la asignatura.")

    def get_academic_program(self):
        return self.__academic_program

    def set_academic_program(self, academic_program):
        if(isinstance(academic_program, AcademicProgram)):
            self.__academic_program = academic_program
        else:
            raise ValueError("El programa académico debe ser una instancia de la clase AcademicProgram.")

    def get_number_credits(self):
        return self.__number_credits

    def set_number_credits(self, number_credits):
        if(number_credits is not None and isinstance(number_credits, int) and number_credits > 0):
            self.__number_credits = number_credits

        else:
            raise ValueError("Este campo no puede estar vacío. El número de créditos debe ser mayor que cero.")

    def mostrar_informacion(self):
        return f"Código: {self.get_code()} | Asignatura: {self.get_name()} | Programa Académico: {self.get_academic_program().get_name()} | Créditos: {self.get_number_credits()}"