class ProgramaController:
    def __init__(self, programas, vista):
        self.programas = programas
        self.vista = vista

    def iniciar(self):
        # Usamos los mismos programas durante toda la sesión
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "1":
                self.vista.mostrar_programas(self.programas)
            elif opcion == "2":
                self.actualizar_semestres()
            elif opcion == "0":
                return
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona 1, 2 o 0")

    def seleccionar_programa(self):
        if not self.programas:
            self.vista.mostrar_mensaje("No hay programas registrados")
            return None

        # Mostramos los códigos para que el usuario elija un programa existente
        self.vista.mostrar_opciones_programas(self.programas)
        codigo = self.vista.pedir_codigo().upper()
        for programa in self.programas:
            if programa.get_code().upper() == codigo:
                return programa

        self.vista.mostrar_mensaje("No se encontró un programa con ese código")
        return None

    def actualizar_semestres(self):
        programa = self.seleccionar_programa()
        if programa is None:
            return

        self.vista.mostrar_mensaje(
            f"Semestres actuales: {programa.get_number_semesters()}"
        )
        entrada = self.vista.pedir_semestres()
        # input entrega texto y necesitamos convertirlo a un número entero
        try:
            semestres = int(entrada)
        except ValueError:
            self.vista.mostrar_mensaje("Escribe un número entero de semestres, por ejemplo 8")
            return

        try:
            # El modelo comprueba que sea mayor que cero antes de guardar
            programa.set_number_semesters(semestres)
        except ValueError as error:
            self.vista.mostrar_mensaje(f"Cambio rechazado: {error}")
            self.vista.mostrar_mensaje(
                f"Se conservan los semestres anteriores: {programa.get_number_semesters()}"
            )
        else:
            self.vista.mostrar_mensaje(
                f"Semestres actualizados: {programa.get_number_semesters()}"
            )