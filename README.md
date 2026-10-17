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

Se necesita Python 3. La versión actual utiliza únicamente su biblioteca estándar, así que no hace falta instalar paquetes con pip.

Para obtener el proyecto:

```bash
git clone https://github.com/WENDOSKI07/sistema-gestion-academica.git
cd sistema-gestion-academica
```

Durante el desarrollo, la integración revisada está en la rama `Oscar`. Para probar esa versión:

```bash
git switch Oscar
```

Desde la carpeta del proyecto:

```bash
python main.py
```

En Windows también se puede utilizar `py main.py` si Python está disponible mediante el lanzador `py`.

El programa abre un menú de consola con las áreas de estudiantes, docentes, programas académicos y asignaturas y una opción para consultar todas las personas. Las operaciones se seleccionan desde el menú, sin un modo de demostración automática.

## Uso del menú

- **Estudiantes:** consultar información y actualizar nombre, correo o semestre
- **Docentes:** consultar información y actualizar nombre, correo u horas semanales
- **Consultar todas las personas:** mostrar los datos y las actividades de dos estudiantes, dos docentes y dos administrativos
- **Programas académicos:** consultar los programas SIS y ADM y actualizar su número de semestres
- **Asignaturas:** consultar las materias PRO1 y FUN1, su programa y sus créditos y actualizar el número de créditos
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
7. Entrar a programas académicos y consultar los dos programas de ejemplo

8. En programas elegir actualizar semestres, seleccionar SIS y cambiar el valor de 10 a 9. Intentar después 0 y -2 y consultar para comprobar que conserva 9
9. En asignaturas consultar PRO1 y FUN1. Actualizar PRO1 de 3 a 4 créditos, intentar después 0 y -2 y consultar para comprobar que conserva 4
10. Probar texto, decimales y entradas vacías al pedir semestres o créditos. Debe aparecer un mensaje y el programa debe continuar sin modificar el dato

Estas operaciones permiten comprobar las siete pruebas mínimas: creación de programas y asignaturas, seis personas, consulta de información, cambios válidos, al menos tres intentos inválidos, información particular y recorrido polimórfico. Las asignaturas reciben objetos AcademicProgram ya creados.

## Colaboración

Cada integrante trabaja en su propia rama y registra sus aportes con commits que describen los cambios realizados. Los aportes se integran conservando su autoría y se revisan antes de preparar la entrega en `main`.

La rama `main` requiere un Pull Request y una aprobación. La rama `Oscar` es de integración durante el desarrollo; tener un cambio allí no significa que ya forme parte de la versión final entregada.

La primera entrega se identificará con una etiqueta acordada por el equipo. El nombre `Entrega_AC2` está reservado por el enunciado para la segunda actividad.

## Integrantes

- Silvana Arenas
- Kelly Martinez
- Oscar Ricaurte
- Stefanny Muñoz
- Lizeth Lopez

## Conceptos de programación orientada a objetos

En las clases de personas se aplican estos conceptos:

- **Encapsulamiento:** los atributos privados se consultan y modifican mediante getters y setters. El modelo rechaza datos inválidos antes de guardarlos
- **Herencia:** `Student`, `Teacher` y `Administrative` heredan de `Person` y reutilizan su constructor para inicializar identificación, nombre y correo
- **Sobreescritura:** las clases hijas implementan sus propias versiones de `mostrar_informacion()` y `realizar_actividad_principal()` para presentar sus datos y actividades
- **Polimorfismo:** la consulta general recorre una colección con los seis objetos usando un único ciclo que llama a los mismos métodos sin identificar su tipo

La consulta general utiliza los nombres solicitados en el enunciado y llama ambos métodos sobre los seis objetos mediante un único ciclo en la vista. Los menús por área no sustituyen ese recorrido común.

## Uso de inteligencia artificial

Se utilizó ChatGPT/Codex como apoyo para interpretar los requisitos, preparar la propuesta de diseño y la estructura inicial, generar y revisar bloques de integración y de interacción por consola, corregir errores y elaborar documentación. También se utilizó Claude como apoyo para proponer la distribución de tareas.

El uso de esta herramienta se declara de acuerdo con las orientaciones de la actividad. Cada integrante es responsable de revisar, comprender y poder explicar los aportes que incorpore al proyecto. Se registrarán aquí los usos adicionales durante el desarrollo.
