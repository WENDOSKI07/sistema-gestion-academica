from controllers.busquedas import buscar_programa_por_codigo


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
            elif opcion == "3":
                programa = self.seleccionar_programa()
                if programa is not None:
                    self.vista.mostrar_programas([programa])
            elif opcion == "0":
                return
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona del 0 al 3")

    def seleccionar_programa(self):
        if not self.programas:
            self.vista.mostrar_mensaje("No hay programas registrados")
            return None

        # Mostramos los códigos para que el usuario elija un programa existente
        self.vista.mostrar_opciones_programas(self.programas)
        codigo = self.vista.pedir_codigo()
        # Reutilizamos la búsqueda de Silvana y dejamos que main capture el error
        return buscar_programa_por_codigo(self.programas, codigo)

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
