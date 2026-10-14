class PersonaController:
    def __init__(self, personas, estudiantes, docentes, vista):
        self.personas = personas
        self.estudiantes = estudiantes
        self.docentes = docentes
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
                elif opcion == "3":
                    self.actualizar_nombre()
                elif opcion == "4":
                    self.actualizar_semestre()
                elif opcion == "5":
                    self.actualizar_horas()
                elif opcion == "0":
                    self.vista.mostrar_mensaje("Hasta luego")
                    break
                else:
                    self.vista.mostrar_mensaje("Opción inválida, selecciona un número del 0 al 5")
        except (EOFError, KeyboardInterrupt):
            self.vista.mostrar_mensaje("\nPrograma finalizado")

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

    def actualizar_semestre(self):
        estudiante = self.seleccionar_persona(self.estudiantes)
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

    def actualizar_horas(self):
        docente = self.seleccionar_persona(self.docentes)
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
