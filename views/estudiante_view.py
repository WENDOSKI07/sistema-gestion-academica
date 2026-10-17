from views.persona_view import PersonaView


class EstudianteView(PersonaView):
    def mostrar_menu(self):
        print("\nÁrea de estudiantes")
        print("1. Consultar estudiantes")
        print("2. Actualizar correo")
        print("3. Actualizar nombre")
        print("4. Actualizar semestre")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def pedir_semestre(self):
        return input("Nuevo semestre: ").strip()
