class MenuController:
    def __init__(self, personas, vista, estudiantes_controller, docentes_controller, programas_controller, asignaturas_controller, comprobar_persona=None):
        self.personas = personas
        self.vista = vista
        self.estudiantes_controller = estudiantes_controller
        self.docentes_controller = docentes_controller
        self.programas_controller = programas_controller
        self.asignaturas_controller = asignaturas_controller
        self.comprobar_persona = comprobar_persona

    def iniciar(self):
        # El menú principal dirige a cada área sin manejar sus actualizaciones
        try:
            while True:
                opcion = self.vista.mostrar_menu()
                if opcion == "1":
                    self.estudiantes_controller.iniciar()
                elif opcion == "2":
                    self.docentes_controller.iniciar()
                elif opcion == "3":
                    # El reporte conserva la colección mezclada y el polimorfismo
                    self.vista.mostrar_personas(self.personas)
                elif opcion == "4":
                    self.programas_controller.iniciar()
                elif opcion == "5":
                    self.asignaturas_controller.iniciar()
                elif opcion == "6":
                    # main prepara esta comprobación y aquí solo la ejecutamos
                    if self.comprobar_persona is not None:
                        self.comprobar_persona()
                elif opcion == "0":
                    self.vista.mostrar_mensaje("Hasta luego")
                    return
                else:
                    self.vista.mostrar_mensaje("Opción inválida, selecciona del 0 al 6")
        except (EOFError, KeyboardInterrupt):
            self.vista.mostrar_mensaje("\nPrograma finalizado")
