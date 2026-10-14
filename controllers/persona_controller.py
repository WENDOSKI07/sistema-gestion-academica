class PersonaController:
    def __init__(self, personas, vista):
        self.personas = personas
        self.vista = vista

    def iniciar(self):
        # Repetimos el menú hasta que el usuario decida salir
        try:
            while True:
                opcion = self.vista.mostrar_menu()
                if opcion == "1":
                    self.vista.mostrar_personas(self.personas)
                elif opcion == "2":
                    self.actualizar_correo()
                elif opcion == "0":
                    self.vista.mostrar_mensaje("Hasta luego")
                    break
                else:
                    self.vista.mostrar_mensaje("Opción inválida, selecciona 1, 2 o 0")
        except (EOFError, KeyboardInterrupt):
            self.vista.mostrar_mensaje("\nPrograma finalizado")

    def actualizar_correo(self):
        identificacion = self.vista.pedir_identificacion()
        # Buscamos por identificación sin preguntar por el tipo de persona
        for persona in self.personas:
            if persona.get_identification() == identificacion:
                self.vista.mostrar_mensaje(f"Correo actual: {persona.get_email()}")
                nuevo_correo = self.vista.pedir_correo()
                try:
                    # El modelo valida antes de guardar el nuevo correo
                    persona.set_email(nuevo_correo)
                except ValueError as error:
                    self.vista.mostrar_mensaje(f"Cambio rechazado: {error}")
                else:
                    self.vista.mostrar_mensaje(f"Correo actualizado: {persona.get_email()}")
                return

        self.vista.mostrar_mensaje("No se encontró una persona con esa identificación")
