from controllers.persona_controller import PersonaController


class EstudianteController(PersonaController):
    # Cada área trabaja solo con las personas que recibe
    def iniciar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "1":
                self.vista.mostrar_personas(self.personas)
                self.vista.esperar_continuar()
            elif opcion == "2":
                self.actualizar_correo()
            elif opcion == "3":
                self.actualizar_nombre()
            elif opcion == "4":
                self.actualizar_semestre()
            elif opcion == "0":
                return
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona del 0 al 4")

    def actualizar_semestre(self):
        estudiante = self.seleccionar_persona(self.personas)
        if estudiante is None:
            return
        self.vista.mostrar_mensaje(f"Semestre actual: {estudiante.get_semester()}")
        entrada = self.vista.pedir_semestre()
        # Primero convertimos el texto a entero y luego el modelo valida el valor
        try:
            semestre = int(entrada)
        except ValueError:
            self.vista.mostrar_mensaje("Escribe un semestre en números enteros, por ejemplo 2")
            return
        try:
            estudiante.set_semester(semestre)
        except ValueError as error:
            self.vista.mostrar_mensaje(f"Cambio rechazado: {error}")
        else:
            self.vista.mostrar_mensaje(f"Semestre actualizado: {estudiante.get_semester()}")

