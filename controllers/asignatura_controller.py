from controllers.busquedas import buscar_asignatura_por_codigo


class AsignaturaController:
    def __init__(self, asignaturas, vista):
        self.asignaturas = asignaturas
        self.vista = vista

    def iniciar(self):
        # Repetimos el menú hasta que el usuario decida volver
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                self.vista.mostrar_asignaturas(self.asignaturas)
            elif opcion == "2":
                self.actualizar_creditos()
            elif opcion == "3":
                asignatura = self.seleccionar_asignatura()
                if asignatura is not None:
                    self.vista.mostrar_asignaturas([asignatura])
            elif opcion == "0":
                return
            else:
                self.vista.mostrar_mensaje(
                    "Opción inválida, selecciona del 0 al 3"
                )

    def seleccionar_asignatura(self):
        if not self.asignaturas:
            self.vista.mostrar_mensaje("No hay asignaturas registradas")
            return None

        # Mostramos los códigos para elegir una materia
        self.vista.mostrar_opciones_asignaturas(self.asignaturas)
        codigo = self.vista.pedir_codigo()
        # La misma búsqueda sirve para consultar y para seleccionar una actualización
        return buscar_asignatura_por_codigo(self.asignaturas, codigo)

    def actualizar_creditos(self):
        asignatura = self.seleccionar_asignatura()

        if asignatura is None:
            return

        self.vista.mostrar_mensaje(
            f"Créditos actuales: {asignatura.get_number_credits()}"
        )
        entrada = self.vista.pedir_creditos()

        # Convertimos el texto a entero antes de pasarlo al modelo
        try:
            creditos = int(entrada)
        except ValueError:
            self.vista.mostrar_mensaje(
                "Escribe un número entero de créditos, por ejemplo 3"
            )
            return

        try:
            # El modelo valida que los créditos sean mayores que cero
            asignatura.set_number_credits(creditos)
        except ValueError as error:
            self.vista.mostrar_mensaje(f"Cambio rechazado: {error}")
            self.vista.mostrar_mensaje(
                f"Se conservan los créditos anteriores: "
                f"{asignatura.get_number_credits()}"
            )
        else:
            self.vista.mostrar_mensaje(
                f"Créditos actualizados: {asignatura.get_number_credits()}"
            )
