class MenuController:
    def __init__(self, personas, vista, estudiantes_controller, docentes_controller, programas_controller, asignaturas_controller, comprobar_persona=None, grupos_controller=None):
        self.personas = personas
        self.vista = vista
        self.estudiantes_controller = estudiantes_controller
        self.docentes_controller = docentes_controller
        self.programas_controller = programas_controller
        self.asignaturas_controller = asignaturas_controller
        self.comprobar_persona = comprobar_persona
        self.grupos_controller = grupos_controller

    def iniciar(self):
        # El menú principal dirige a cada área sin manejar sus actualizaciones
        try:
            while True:
                opcion = self.vista.mostrar_menu()
                if opcion == "1":
                    self.iniciar_personas()
                elif opcion == "2":
                    self.programas_controller.iniciar()
                elif opcion == "3":
                    self.asignaturas_controller.iniciar()
                elif opcion == "4":
                    if self.grupos_controller is not None:
                        self.grupos_controller.iniciar()
                elif opcion == "5":
                    self.iniciar_comprobaciones()
                elif opcion == "0":
                    self.vista.mostrar_mensaje("Hasta luego")
                    return
                else:
                    self.vista.mostrar_mensaje("Opción inválida, selecciona del 0 al 5")
        except (EOFError, KeyboardInterrupt):
            self.vista.mostrar_mensaje("\nPrograma finalizado")

    def iniciar_personas(self):
        # Reunimos las consultas de personas para no mezclar las áreas del sistema
        while True:
            opcion = self.vista.mostrar_menu_personas()
            if opcion == "1":
                self.estudiantes_controller.iniciar()
            elif opcion == "2":
                self.docentes_controller.iniciar()
            elif opcion == "3":
                self.vista.mostrar_personas(self.personas)
                self.vista.esperar_continuar()
            elif opcion == "0":
                return
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona del 0 al 3")

    def iniciar_comprobaciones(self):
        while True:
            opcion = self.vista.mostrar_menu_comprobaciones()
            if opcion == "1":
                if self.comprobar_persona is not None:
                    self.comprobar_persona()
                    self.vista.esperar_continuar()
            elif opcion == "0":
                return
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona 1 o 0")
