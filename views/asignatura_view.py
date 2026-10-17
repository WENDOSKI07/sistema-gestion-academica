class AsignaturaView:
    def mostrar_menu(self):
        print("\nÁrea de asignaturas")
        print("1. Consultar asignaturas")
        print("2. Actualizar créditos")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def mostrar_asignaturas(self, asignaturas):
        if not asignaturas:
            print("No hay asignaturas registradas")
            return
        for asignatura in asignaturas:
            print(asignatura.mostrar_informacion())

    def mostrar_opciones_asignaturas(self, asignaturas):
        for asignatura in asignaturas:
            print(f"{asignatura.get_code()} - {asignatura.get_name()}")

    def pedir_codigo(self):
        return input("Código de la asignatura: ").strip()

    def pedir_creditos(self):
        return input("Nuevo número de créditos: ").strip()

    def mostrar_mensaje(self, mensaje):
        print(mensaje)