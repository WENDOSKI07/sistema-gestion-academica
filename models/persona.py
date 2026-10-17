import re


class Person:

    # Esta clase reúne los datos y comportamientos que tienen en común las personas.
    def __init__(self, identification, name, email):
        # Se usan los métodos set para validar los datos antes de guardarlos.
        self.set_identification(identification)
        self.set_name(name)
        self.set_email(email)

    # Los métodos get permiten consultar los atributos privados de la persona.
    def get_identification(self):
        return self.__identification

    def set_identification(self, identification):
        # La identificación debe ser texto y no puede quedar vacía.
        if(identification is not None and isinstance(identification, str) and len(identification.strip()) > 0):
            self.__identification = identification

        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe una identificación.")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        # Se valida el nombre para evitar guardar valores nulos o solo espacios.
        if(name is not None and isinstance(name, str) and len(name.strip()) > 0):
            self.__name = name

        else:
            raise ValueError("Este campo no puede estar vacío. Por favor, escribe un nombre.")

    def get_email(self):
        return self.__email

    def set_email(self, email):
        # Primero se revisa que el correo sea texto y tenga algún contenido.
        if not isinstance(email, str) or not email.strip():
            raise ValueError("El correo no puede estar vacío")

        email = email.strip()
        # Esta expresión regular comprueba que tenga una estructura básica
        # de correo, con un usuario, un dominio y al menos una extensión.
        # Esto no comprueba que la dirección exista ni que reciba mensajes
        if not re.fullmatch(r"[^\s@]+@[^\s@.]+(?:\.[^\s@.]+)+", email):
            raise ValueError("Escribe un correo con formato nombre@dominio.com")

        self.__email = email

    def mostrar_informacion(self):
        # Se arma una sola cadena con los datos para mostrarla en pantalla.
        return f"Identificación: {self.get_identification()} | Nombre: {self.get_name()} | Email: {self.get_email()}"

    def realizar_actividad_principal(self):
        # Este método puede ser redefinido por clases más específicas.
        return "Realizando una actividad general de la institución."
