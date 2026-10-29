class ProgramaView:
    # Dejamos aquí las opciones y los mensajes del área de programas
    def mostrar_menu(self):
        print("\nÁrea de programas académicos")
        print("1. Consultar programas")
        print("2. Actualizar número de semestres")
        print("3. Buscar programa por código")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def mostrar_programas(self, programas):
        if not programas:
            print("No hay programas registrados")
            return
        for programa in programas:
            print(programa.mostrar_informacion())

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_opciones_programas(self, programas):
        for programa in programas:
            print(f"{programa.get_code()} - {programa.get_name()}")

    def pedir_codigo(self):
        return input("Código del programa: ").strip()

    def pedir_semestres(self):
        return input("Nuevo número de semestres: ").strip()
