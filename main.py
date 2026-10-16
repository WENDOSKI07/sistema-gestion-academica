from models.estudiante import Student
from models.docente import Teacher
from models.administrativo import Administrative
from controllers.menu_controller import MenuController
from controllers.estudiante_controller import EstudianteController
from controllers.docente_controller import DocenteController
from views.menu_view import MenuView
from views.estudiante_view import EstudianteView
from views.docente_view import DocenteView
from models.programa_academico import AcademicProgram


def crear_programas_ejemplo():
    # Usamos la clase de programa académico que ya está en el modelo
    # Cada objeto guarda su código, nombre, facultad y número de semestres
    sistemas = AcademicProgram(
        code="SIS",
        name="Ingeniería de Sistemas",
        faculty="Ciencias e Ingenierías",
        number_semesters=10,
    )

    administracion = AcademicProgram(
        code="ADM",
        name="Administración de Empresas",
        faculty="Ciencias Contables, Económicas y Administrativas",
        number_semesters=8,
    )

    # Devolvemos los dos objetos juntos para usarlos después en el área de programas
    return [sistemas, administracion]


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

    # Agregamos dos administrativos usando la clase que hizo nuestra compañera
    administrativo_1 = Administrative(
        identification="P005",
        name="Laura Díaz",
        email="laura@example.com",
        id_employee="ADM001",
        deparment="Registro Académico",
        possition="Auxiliar",
        work_schedule="Diurna",
    )

    administrativo_2 = Administrative(
        identification="P006",
        name="Pedro León",
        email="pedro@example.com",
        id_employee="ADM002",
        deparment="Bienestar Universitario",
        possition="Coordinador",
        work_schedule="Diurna",
    )

    estudiantes = [estudiante_1, estudiante_2]
    docentes = [docente_1, docente_2]
    # Las listas específicas apuntan a los mismos objetos del reporte general
    # Sirven para elegir a quién actualizar, el reporte sigue usando una sola lista
    # Reunimos los seis objetos para consultar sus datos y actividades
    # con los mismos métodos sin separarlos por tipo en el reporte
    personas = [
        estudiante_1, docente_1, administrativo_1,
        estudiante_2, docente_2, administrativo_2,
    ]
    return personas, estudiantes, docentes


def main():
    # Añadimos la consola para que el usuario pueda consultar personas
    # y actualizar sus datos sin tener que modificar el código
    # Todavía usamos personas de ejemplo, no registramos personas nuevas
    # Los cambios se mantienen en memoria hasta cerrar el programa
    # main prepara los objetos y conecta el modelo con la vista y el controlador
    # Las preguntas quedan en la vista y las acciones se coordinan en el controlador
    personas, estudiantes, docentes = crear_personas_ejemplo()
    estudiantes_controller = EstudianteController(estudiantes, EstudianteView())
    docentes_controller = DocenteController(docentes, DocenteView())
    controlador = MenuController(
        personas, MenuView(), estudiantes_controller, docentes_controller
    )
    controlador.iniciar()


if __name__ == "__main__":
    main()
