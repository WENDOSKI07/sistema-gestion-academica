class GrupoView:
    # La vista muestra las opciones y recibe lo que escribe el usuario
    # Las reglas de matrícula y retiro quedan en el modelo del grupo
    def mostrar_menu(self):
        print("\nÁrea de grupos académicos")
        print("1. Consultar grupos")
        print("2. Ver estudiantes de un grupo")
        print("3. Matricular estudiante")
        print("4. Retirar estudiante")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def mostrar_grupos(self, grupos):
        if not grupos:
            print("No hay grupos registrados")
            return
        for grupo in grupos:
            print(grupo.mostrar_informacion_grupo())

    def mostrar_opciones_grupos(self, grupos):
        # Mostramos los códigos para que sepa qué grupo puede seleccionar
        for grupo in grupos:
            print(f"{grupo.get_code()} - {grupo.get_asignatura().get_name()}")

    def pedir_codigo_grupo(self):
        return input("Código del grupo: ").strip()

    def mostrar_opciones_estudiantes(self, estudiantes):
        # Usamos el código estudiantil que también recibe el método de retiro
        for estudiante in estudiantes:
            print(f"{estudiante.get_id_student()} - {estudiante.get_name()}")

    def pedir_codigo_estudiante(self):
        return input("Código estudiantil: ").strip()

    def mostrar_estudiantes(self, grupo):
        # El grupo prepara la información y la vista se encarga de mostrarla
        print(grupo.mostrar_estudiantes())

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def esperar_continuar(self):
        input("\nPresiona Enter para volver: ")
