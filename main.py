from models.estudiante import Student
from models.docente import Teacher


def mostrar_personas(personas):
    # Recorremos estudiantes y docentes juntos en una misma colección
    for persona in personas:
        # Aquí usamos polimorfismo porque llamamos los mismos métodos
        # y cada objeto responde según su clase sin tener que usar un if
        print(persona.show_info())
        print(persona.perform_main_activity())
        print()

def main():
    print("Sistema de Gestión Académica")
    print("Demostración inicial de la actividad 1\n")

    # Creamos dos estudiantes con datos ficticios usando el constructor
    # Por ahora Student recibe el programa como texto
    estudiante_1 = Student(
        identification="P001",
        name="Ana Torres",
        email="ana@example.com",
        id_student="EST001",
        academic_program="Ingeniería de Sistemas",
        semester=1,
        cumulative_GPA=4.2,
    )

    estudiante_2 = Student(
        identification="P002",
        name="Luis Rojas",
        email="luis@example.com",
        id_student="EST002",
        academic_program="Administración de Empresas",
        semester=2,
        cumulative_GPA=3.8,
    )

    # Los docentes comparten los datos de Person pero tienen sus propios datos
    docente_1 = Teacher(
        identification="P003",
        name="Carlos Ruiz",
        email="carlos@example.com",
        id_employee="DOC001",
        deparment="Ciencias e Ingenierías",
        employment_type="Tiempo completo",
        weekly_hours=40,
    )

    docente_2 = Teacher(
        identification="P004",
        name="Marta Gil",
        email="marta@example.com",
        id_employee="DOC002",
        deparment="Ciencias Contables, Económicas y Administrativas",
        employment_type="Medio tiempo",
        weekly_hours=20,
    )

    # Consultamos el correo mediante un método sin acceder al atributo privado
    print("Cambio válido de correo")
    print("Correo anterior:", estudiante_1.get_email())
    estudiante_1.set_email("ana.torres@example.com")
    print("Correo actualizado:", estudiante_1.get_email())

    # Intentamos guardar un correo vacío para comprobar la validación
    # try ejecuta el intento y except captura el error para poder continuar
    print("\nIntento de cambio con un correo vacío")
    try:
        estudiante_1.set_email("")
    except ValueError as error:
        print("Cambio rechazado:", error)

    print("Correo después del intento:", estudiante_1.get_email())

    # Guardamos los objetos en una lista y la pasamos al recorrido común
    # Mezclamos estudiantes y docentes para demostrar el polimorfismo
    # Faltan los dos administrativos para completar las seis personas
    personas = [estudiante_1, docente_1, estudiante_2, docente_2]
    print("\nInformación y actividades de las personas")
    mostrar_personas(personas)

if __name__ == "__main__":
    main()
