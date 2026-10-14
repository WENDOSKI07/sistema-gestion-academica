from views.persona_view import PersonaView


class DocenteView(PersonaView):
    def mostrar_menu(self):
        print("\nÁrea de docentes")
        print("1. Consultar docentes")
        print("2. Actualizar correo")
        print("3. Actualizar nombre")
        print("4. Actualizar horas semanales")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def pedir_horas(self):
        return input("Nuevas horas semanales: ").strip()
