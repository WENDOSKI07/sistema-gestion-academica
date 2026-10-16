class ProgramaView:
    # Dejamos aquí las opciones y los mensajes del área de programas
    def mostrar_menu(self):
        print("\nÁrea de programas académicos")
        print("1. Consultar programas")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def mostrar_programas(self, programas):
        if not programas:
            print("No hay programas registrados")
            return
        for programa in programas:
            print(programa.show_info())

    def mostrar_mensaje(self, mensaje):
        print(mensaje)