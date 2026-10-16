class ProgramaController:
    def _init_(self, programas, vista):
        self.programas = programas
        self.vista = vista

    def iniciar(self):
        # Usamos los mismos programas durante toda la sesión
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "1":
                self.vista.mostrar_programas(self.programas)
            elif opcion == "0":
                return
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona 1 o 0")