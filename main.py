from models.estudiante import Student
from models.docente import Teacher
from controllers.persona_controller import PersonaController
from views.persona_view import PersonaView


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

    estudiantes = [estudiante_1, estudiante_2]
    docentes = [docente_1, docente_2]
    # Las listas específicas apuntan a los mismos objetos del reporte general
    # Sirven para elegir a quién actualizar, el reporte sigue usando una sola lista
    personas = [estudiante_1, docente_1, estudiante_2, docente_2]
    return personas, estudiantes, docentes


def main():
    # Añadimos la consola para que el usuario pueda consultar personas
    # y actualizar sus datos sin tener que modificar el código
    # Todavía usamos personas de ejemplo, no registramos personas nuevas
    # Los cambios se mantienen en memoria hasta cerrar el programa
    # main prepara los objetos y conecta el modelo con la vista y el controlador
    # Las preguntas quedan en la vista y las acciones se coordinan en el controlador
    personas, estudiantes, docentes = crear_personas_ejemplo()
    vista = PersonaView()
    controlador = PersonaController(personas, estudiantes, docentes, vista)
    controlador.iniciar()


if __name__ == "__main__":
    main()
