from models.estudiante import Student
from models.docente import Teacher
from controllers.persona_controller import PersonaController
from views.persona_view import PersonaView
import sys


def mostrar_personas(personas):
    # Recorremos estudiantes y docentes juntos en una misma colección
    for persona in personas:
        # Aquí usamos polimorfismo porque llamamos los mismos métodos
        # y cada objeto responde según su clase sin tener que usar un if
        print(persona.show_info())
        print(persona.perform_main_activity())
        print()

def crear_personas_ejemplo():
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

    return [estudiante_1, docente_1, estudiante_2, docente_2]


def demostrar_funcionamiento():
    print("Sistema de Gestión Académica")
    print("Demostración inicial de la actividad 1\n")
    personas = crear_personas_ejemplo()
    estudiante_1, docente_1, estudiante_2, docente_2 = personas

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

    # Probamos cambios válidos usando los métodos de las clases
    print("\nCambio válido de semestre")
    print("Semestre anterior:", estudiante_1.get_semester())
    estudiante_1.set_semester(2)
    print("Semestre actualizado:", estudiante_1.get_semester())

    print("\nCambio válido de horas semanales")
    print("Horas anteriores:", docente_1.get_weekly_hours())
    docente_1.set_weekly_hours(35)
    print("Horas actualizadas:", docente_1.get_weekly_hours())

    # Cada intento tiene su propio try para que un error no impida probar el otro
    # La validación está en el modelo y aquí mostramos el resultado
    print("\nIntento de asignar un semestre en cero")
    try:
        estudiante_1.set_semester(0)
    except ValueError as error:
        print("Cambio rechazado:", error)

    print("Semestre después del intento:", estudiante_1.get_semester())

    print("\nIntento de asignar horas semanales negativas")
    try:
        docente_1.set_weekly_hours(-5)
    except ValueError as error:
        print("Cambio rechazado:", error)

    print("Horas después del intento:", docente_1.get_weekly_hours())

    # Guardamos los objetos en una lista y la pasamos al recorrido común
    # Mezclamos estudiantes y docentes para demostrar el polimorfismo
    # Faltan los dos administrativos para completar las seis personas
    personas = [estudiante_1, docente_1, estudiante_2, docente_2]
    print("\nInformación y actividades de las personas")
    mostrar_personas(personas)

def main():
    # Añadimos la consola para que el usuario pueda consultar personas
    # y escribir un nuevo correo sin tener que modificar el código
    # Todavía usamos personas de ejemplo, no registramos personas nuevas
    # Los cambios se mantienen en memoria hasta cerrar el programa
    # Conservamos la demostración automática para revisar las pruebas
    if "--demo" in sys.argv[1:]:
        demostrar_funcionamiento()
    else:
        personas = crear_personas_ejemplo()
        vista = PersonaView()
        controlador = PersonaController(personas, vista)
        controlador.iniciar()


if __name__ == "__main__":
    main()
