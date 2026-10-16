# Sistema de Gestión Académica

Proyecto colaborativo de Programación I de la Universidad de Manizales, desarrollado en Python para aplicar los fundamentos de la programación orientada a objetos.

## Descripción

El sistema tiene como objetivo organizar la información de estudiantes, docentes, administrativos, programas académicos y asignaturas.

La actividad 1 se enfoca en representar estas entidades, consultar y modificar sus datos con validaciones y demostrar herencia, sobreescritura y polimorfismo. En la actividad 2 se ampliará el mismo proyecto con grupos académicos, horarios, matrícula y retiro de estudiantes, clases abstractas y excepciones personalizadas.

## Organización del proyecto

Se utiliza la arquitectura Modelo–Vista–Controlador (MVC) para separar los datos y las reglas académicas de la presentación y de la coordinación de las acciones del usuario.

## Estructura

```text
sistema-gestion-academica/
├── main.py
├── models/
├── views/
├── controllers/
├── docs/
├── README.md
└── requirements.txt
```

- `models/`: entidades académicas y reglas del sistema.
- `views/`: presentación e interfaz de usuario.
- `controllers/`: coordinación entre las vistas y los modelos.
- `docs/`: propuesta inicial y documentación de diseño.
- `main.py`: punto de entrada de la aplicación.
- `requirements.txt`: registro de las dependencias externas del proyecto.

## Ejecución

Desde la carpeta del proyecto, con Python 3:

```bash
python main.py
```

El programa abre un menú de consola con las áreas de estudiantes y docentes y una opción para consultar todas las personas. No requiere instalar librerías externas para estas funciones.

## Uso del menú

- **Estudiantes:** consultar información y actualizar nombre, correo o semestre
- **Docentes:** consultar información y actualizar nombre, correo u horas semanales
- **Consultar todas las personas:** mostrar los datos y las actividades de dos estudiantes, dos docentes y dos administrativos
- **Volver o salir:** usar la opción 0 para regresar desde un área o cerrar el programa desde el menú principal

Para actualizar un dato, seleccionar la opción del área e ingresar una de las identificaciones que muestra la consola. Los estudiantes de ejemplo tienen las identificaciones `P001` y `P002`; los docentes, `P003` y `P004`.

Los registros iniciales son ficticios. Las actualizaciones se mantienen en memoria mientras el programa está abierto y se pierden al cerrarlo. Todavía no se registran personas nuevas desde el menú.

### Comprobaciones manuales

1. Entrar a estudiantes y cambiar el correo de `P001` por `ana.nueva@example.com`
2. Intentar cambiarlo por una cadena vacía o por `hola` y comprobar que se rechaza
3. Consultar los estudiantes para verificar que se conserva el último correo válido
4. Intentar asignar un semestre en cero o escribir texto cuando se pide un número
5. Entrar a docentes e intentar asignar horas semanales negativas
6. Consultar todas las personas para observar los datos y las actividades de cada clase

Estas comprobaciones describen las funciones actuales. Para completar la actividad también se deben integrar programas y asignaturas y verificar los semestres de un programa y los créditos de una asignatura.

## Integrantes

Pendiente de completar con los nombres de todos los integrantes del equipo.

## Conceptos de programación orientada a objetos

En las clases de personas se aplican estos conceptos:

- **Encapsulamiento:** los atributos privados se consultan y modifican mediante getters y setters. El modelo rechaza datos inválidos antes de guardarlos
- **Herencia:** `Student`, `Teacher` y `Administrative` heredan de `Person` y reutilizan su constructor para inicializar identificación, nombre y correo
- **Sobreescritura:** las clases hijas implementan sus propias versiones de `show_info()` y `perform_main_activity()` para presentar sus datos y actividades
- **Polimorfismo:** la consulta general recorre una colección con los seis objetos usando un único ciclo que llama a los mismos métodos sin identificar su tipo

Los nombres actuales de los métodos están en inglés. El equipo está coordinando su ajuste a `mostrar_informacion()` y `realizar_actividad_principal()`, como solicita el enunciado.

## Uso de inteligencia artificial

Se utilizó ChatGPT/Codex como apoyo para interpretar los requisitos, preparar la propuesta de diseño y la estructura inicial, generar y revisar bloques de integración y de interacción por consola, corregir errores y elaborar documentación. También se utilizó Claude como apoyo para proponer la distribución de tareas.

El uso de esta herramienta se declara de acuerdo con las orientaciones de la actividad. Cada integrante es responsable de revisar, comprender y poder explicar los aportes que incorpore al proyecto. Se registrarán aquí los usos adicionales durante el desarrollo.
