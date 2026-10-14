class PersonaController:
    # Compartimos las operaciones que sirven para cualquier persona
    def __init__(self, personas, vista):
        self.personas = personas
        self.vista = vista

    def actualizar_correo(self):
        persona = self.seleccionar_persona(self.personas)
        if persona is None:
            return
        self.vista.mostrar_mensaje(f"Correo actual: {persona.get_email()}")
        nuevo_correo = self.vista.pedir_correo()
        try:
            persona.set_email(nuevo_correo)
        except ValueError as error:
            self.vista.mostrar_mensaje(f"Cambio rechazado: {error}")
        else:
            self.vista.mostrar_mensaje(f"Correo actualizado: {persona.get_email()}")

    def seleccionar_persona(self, disponibles):
        # Mostramos las identificaciones que se pueden usar en esta operación
        self.vista.mostrar_opciones_personas(disponibles)
        identificacion = self.vista.pedir_identificacion()
        for persona in disponibles:
            if persona.get_identification() == identificacion:
                return persona
        self.vista.mostrar_mensaje("No se encontró esa identificación entre las opciones disponibles")
        return None

    def actualizar_nombre(self):
        persona = self.seleccionar_persona(self.personas)
        if persona is None:
            return
        self.vista.mostrar_mensaje(f"Nombre actual: {persona.get_name()}")
        nombre = self.vista.pedir_nombre()
        try:
            persona.set_name(nombre)
        except ValueError as error:
            self.vista.mostrar_mensaje(f"Cambio rechazado: {error}")
        else:
            self.vista.mostrar_mensaje(f"Nombre actualizado: {persona.get_name()}")
