from views.persona_view import PersonaView


class MenuView(PersonaView):
    def mostrar_menu(self):
        print("\nSistema de Gestión Académica")
        print("1. Personas")
        print("2. Programas académicos")
        print("3. Asignaturas")
        print("4. Grupos y matrículas")
        print("5. Prueba de diseño para la actividad")
        print("0. Salir")
        return input("Selecciona un área: ").strip()

    def mostrar_menu_personas(self):
        print("\nPersonas")
        print("1. Estudiantes")
        print("2. Docentes")
        print("3. Consultar todas las personas")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def mostrar_menu_comprobaciones(self):
        print("\nPrueba de diseño para la actividad")
        print("Esta sección permite comprobar una regla del proyecto")
        print("1. Demostrar que Persona es abstracta")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()
