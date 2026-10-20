class PersonaView:
    # La vista se encarga de las preguntas y los mensajes en consola
    # Usamos input para recibir los datos del usuario y el controlador
    # los envía al modelo donde se validan antes de guardar el cambio
    def mostrar_personas(self, personas):
        for persona in personas:
            # Usamos los mismos métodos para estudiantes y docentes
            print(persona.mostrar_informacion())
            print(persona.realizar_actividad_principal())
            print()

    def pedir_identificacion(self):
        return input("Identificación de la persona: ").strip()

    def pedir_correo(self):
        return input("Nuevo correo: ").strip()

    def mostrar_opciones_personas(self, personas):
        for persona in personas:
            print(f"{persona.get_identification()} - {persona.get_name()}")

    def pedir_nombre(self):
        return input("Nuevo nombre: ").strip()

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
