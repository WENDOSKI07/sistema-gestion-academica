from views.persona_view import PersonaView


class MenuView(PersonaView):
    def mostrar_menu(self):
        print("\nSistema de Gestión Académica")
        print("1. Estudiantes")
        print("2. Docentes")
        print("3. Consultar todas las personas")
        print("4. Programas académicos")
        print("5. Asignaturas")
        print("6. Comprobar por qué Persona es abstracta")
        print("7. Grupos académicos")
        print("0. Salir")
        return input("Selecciona un área: ").strip()
