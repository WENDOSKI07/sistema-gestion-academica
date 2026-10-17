class AcademicProgram:
    """Programa académico con código, nombre, facultad y número de semestres."""

    def __init__(self, code, name, faculty, number_semesters):
        self.set_code(code)
        self.set_name(name)
        self.set_faculty(faculty)
        self.set_number_semesters(number_semesters)

    def get_code(self):
        return self.__code

    def set_code(self, code):
        if(code is not None and isinstance(code, str) and len(code.strip()) > 0):
            self.__code = code

        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe el código del programa.")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if(name is not None and isinstance(name, str) and len(name.strip()) > 0):
            self.__name = name

        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe el nombre del programa.")

    def get_faculty(self):
        return self.__faculty

    def set_faculty(self, faculty):
        if(faculty is not None and isinstance(faculty, str) and len(faculty.strip()) > 0):
            self.__faculty = faculty

        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe la facultad del programa.")

    def get_number_semesters(self):
        return self.__number_semesters

    def set_number_semesters(self, number_semesters):
        if(number_semesters is not None and isinstance(number_semesters, int) and number_semesters > 0):
            self.__number_semesters = number_semesters

        else:
            raise ValueError("Este campo no puede estar vacío. El número de semestres debe ser mayor que cero.")

    def mostrar_informacion(self):
        return f"Código: {self.get_code()} | Programa: {self.get_name()} | Facultad: {self.get_faculty()} | Semestres: {self.get_number_semesters()}"