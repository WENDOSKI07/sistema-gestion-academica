class GrupoController:
    def __init__(self, grupos, estudiantes, vista):
        # Recibimos los objetos que prepara main para trabajar con los mismos datos
        self.grupos = grupos
        self.estudiantes = estudiantes
        self.vista = vista

    def iniciar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "1":
                self.vista.mostrar_grupos(self.grupos)
                self.vista.esperar_continuar()
            elif opcion == "2":
                grupo = self.seleccionar_grupo()
                if grupo is not None:
                    self.vista.mostrar_estudiantes(grupo)
                    self.vista.esperar_continuar()
            elif opcion == "3":
                self.matricular_estudiante()
            elif opcion == "4":
                self.retirar_estudiante()
            elif opcion == "0":
                return
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona del 0 al 4")

    def seleccionar_grupo(self):
        if not self.grupos:
            self.vista.mostrar_mensaje("No hay grupos registrados")
            return None

        self.vista.mostrar_opciones_grupos(self.grupos)
        codigo = self.vista.pedir_codigo_grupo().strip().upper()
        if not codigo:
            self.vista.mostrar_mensaje("Escribe el código del grupo")
            return None

        for grupo in self.grupos:
            if grupo.get_code().strip().upper() == codigo:
                return grupo

        self.vista.mostrar_mensaje("No se encontró un grupo con ese código")
        return None

    def seleccionar_estudiante(self):
        if not self.estudiantes:
            self.vista.mostrar_mensaje("No hay estudiantes registrados")
            return None

        self.vista.mostrar_opciones_estudiantes(self.estudiantes)
        codigo = self.vista.pedir_codigo_estudiante().strip().upper()
        if not codigo:
            self.vista.mostrar_mensaje("Escribe el código estudiantil")
            return None

        for estudiante in self.estudiantes:
            if estudiante.get_id_student().strip().upper() == codigo:
                return estudiante

        self.vista.mostrar_mensaje("No se encontró un estudiante con ese código")
        return None

    def matricular_estudiante(self):
        grupo = self.seleccionar_grupo()
        if grupo is None:
            return

        estudiante = self.seleccionar_estudiante()
        if estudiante is None:
            return

        # El modelo revisa duplicados y cupos y main captura las excepciones
        # Solo mostramos que salió bien si la matrícula realmente se completó
        grupo.matricular_estudiante(estudiante)
        self.vista.mostrar_mensaje("Estudiante matriculado correctamente")

    def retirar_estudiante(self):
        grupo = self.seleccionar_grupo()
        if grupo is None:
            return

        codigo = self.vista.pedir_codigo_estudiante().strip().upper()
        if not codigo:
            self.vista.mostrar_mensaje("Escribe el código estudiantil")
            return

        # Pasamos el código al grupo para que compruebe si está matriculado
        # No buscamos primero en la lista general porque el grupo controla el retiro
        grupo.retirar_estudiante(codigo)
        self.vista.mostrar_mensaje("Estudiante retirado correctamente")
