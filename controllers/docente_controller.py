from controllers.persona_controller import PersonaController


class DocenteController(PersonaController):
    # Cada área trabaja solo con las personas que recibe
    def iniciar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "1":
                self.vista.mostrar_personas(self.personas)
            elif opcion == "2":
                self.actualizar_correo()
            elif opcion == "3":
                self.actualizar_nombre()
            elif opcion == "4":
                self.actualizar_horas()
            elif opcion == "0":
                return
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona del 0 al 4")

    def actualizar_horas(self):
        docente = self.seleccionar_persona(self.personas)
        if docente is None:
            return
        self.vista.mostrar_mensaje(f"Horas actuales: {docente.get_weekly_hours()}")
        entrada = self.vista.pedir_horas()
        try:
            horas = int(entrada)
        except ValueError:
            self.vista.mostrar_mensaje("Escribe las horas en números enteros, por ejemplo 20")
            return
        try:
            docente.set_weekly_hours(horas)
        except ValueError as error:
            self.vista.mostrar_mensaje(f"Cambio rechazado: {error}")
        else:
            self.vista.mostrar_mensaje(f"Horas actualizadas: {docente.get_weekly_hours()}")
