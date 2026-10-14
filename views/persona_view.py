class PersonaView:
    # La vista se encarga de las preguntas y los mensajes en consola
    # Usamos input para recibir los datos del usuario y el controlador
    # los envía al modelo donde se validan antes de guardar el cambio
    def mostrar_menu(self):
        print("\nSistema de Gestión Académica")
        print("1. Consultar personas")
        print("2. Actualizar correo")
        print("3. Actualizar nombre")
        print("4. Actualizar semestre de un estudiante")
        print("5. Actualizar horas semanales de un docente")
        print("0. Salir")
        return input("Selecciona una opción: ").strip()

    def mostrar_personas(self, personas):
        for persona in personas:
            # Usamos los mismos métodos para estudiantes y docentes
            print(persona.show_info())
            print(persona.perform_main_activity())
            print()

    def pedir_identificacion(self):
        return input("Identificación de la persona: ").strip()

    def pedir_correo(self):
        return input("Nuevo correo: ").strip()

    def mostrar_opciones_personas(self, personas):
        for persona in personas:
            print(f"{persona.get_identification()} - {persona.get_name()}")

    def pedir_nombre(self):
        return input("Nuevo nombre: ").strip()

    def pedir_semestre(self):
        return input("Nuevo semestre: ").strip()

    def pedir_horas(self):
        return input("Nuevas horas semanales: ").strip()

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
