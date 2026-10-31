# Sistema de Gestión Académica

Proyecto colaborativo de Programación I de la Universidad de Manizales, desarrollado en Python para aplicar los fundamentos de la programación orientada a objetos.

## Descripción

El sistema tiene como objetivo organizar la información de estudiantes, docentes, administrativos, programas académicos y asignaturas.

La actividad 1 representa estas entidades, permite consultar y modificar sus datos y demuestra herencia, sobreescritura y polimorfismo. La actividad 2 amplía el mismo sistema con grupos académicos, horarios, matrícula y retiro de estudiantes, clases abstractas y excepciones personalizadas.

## Organización del proyecto

Se utiliza la arquitectura Modelo–Vista–Controlador (MVC) para separar los datos y las reglas académicas de la presentación y de la coordinación de las acciones del usuario.

## Estructura

```text
sistema-gestion-academica/
├── main.py
├── models/
├── views/
├── controllers/
├── exceptions/
├── tests/
├── docs/
├── README.md
└── requirements.txt
```

- `models/`: entidades académicas y reglas del sistema.
- `views/`: presentación e interfaz de usuario.
- `controllers/`: coordinación entre las vistas y los modelos.
- `exceptions/`: excepciones personalizadas de búsqueda y matrícula.
- `tests/`: pruebas de búsquedas, excepciones e integración.
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

El repositorio utiliza `main` como rama principal. Después de clonarlo, ejecutar desde la carpeta del proyecto:

```bash
python main.py
```

En Windows también se puede utilizar `py main.py` si Python está disponible mediante el lanzador `py`.

El programa abre un menú de consola con las áreas de estudiantes, docentes, programas académicos y asignaturas y una opción para consultar todas las personas. Las operaciones se seleccionan desde el menú, sin un modo de demostración automática.

## Uso del menú

- **Estudiantes:** consultar información y actualizar nombre, correo o semestre
- **Docentes:** consultar información y actualizar nombre, correo u horas semanales
- **Consultar todas las personas:** mostrar los datos y las actividades de dos estudiantes, dos docentes y dos administrativos
- **Comprobar por qué Persona es abstracta:** la opción 6 intenta crear una Persona y muestra el rechazo esperado sin cerrar el programa
- **Grupos académicos:** la opción 7 permite consultar grupos y matriculados, matricular y retirar usando el código estudiantil
- **Programas académicos:** consultar los programas SIS y ADM, buscar por código y actualizar su número de semestres
- **Asignaturas:** consultar las materias PRO1 y FUN1, buscar por código y actualizar el número de créditos
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

## Pruebas automáticas

Desde la carpeta del proyecto ejecutar `python -m unittest discover -s tests -t . -v`.
Las pruebas simulan entradas de consola sin cambiar el funcionamiento interactivo del programa.

En programas y asignaturas, la opción 3 busca por código sin distinguir mayúsculas y admite espacios alrededor. Si el código no existe o está vacío, se muestra el aviso y se vuelve al menú principal conservando los cambios de la sesión. Las excepciones se capturan en `main.py`.

### Grupos y composición

El programa prepara dos grupos vacíos: G1 ofrece PRO1 con capacidad para 1 estudiante y G2 ofrece FUN1 con capacidad para 2. Cada grupo recibe los objetos de asignatura y docente existentes. La matrícula agrega el objeto Student, no solo su nombre.

GrupoAcademico crea un objeto Horario dentro de su constructor. Esta relación es composición porque el horario forma parte de la organización del grupo y describe su día, horas y salón. Un grupo contiene un horario; no es un tipo de horario, así que no corresponde usar herencia. Las asignaturas, docentes y estudiantes existen de forma independiente y se comparten mediante referencias.

### Comprobar matrícula y retiro

1. Elegir 7 y después 1 para consultar los dos grupos y sus horarios
2. Elegir 3, grupo G1 y estudiante EST001 para matricular a Ana
3. Repetir la matrícula de EST001 en G1 para comprobar el error de duplicado
4. Entrar nuevamente con 7 e intentar matricular EST002 en G1 para comprobar el cupo lleno
5. Entrar nuevamente con 7 y elegir 2 y G1 para comprobar que Ana sigue matriculada
6. Elegir 4, G1 y EST001 para retirar a Ana
7. Repetir el retiro para comprobar el error de estudiante no matriculado
8. Entrar nuevamente con 7 y matricular EST002 en G1 para comprobar que se liberó el cupo

Las tres excepciones de matrícula se generan en el modelo y se capturan en main. Tras cada error se muestra un mensaje y se vuelve al menú principal. Los cambios de matrícula permanecen hasta cerrar la sesión.

Para comprobar la abstracción desde la consola, elegir 6 en el menú principal. Debe aparecer la explicación de que Persona no puede crearse directamente. Después se puede elegir 3 para consultar las clases hijas y confirmar que el programa continúa.

El documento de decisiones de la segunda actividad está en [docs/decisiones-diseno-ac2.md](docs/decisiones-diseno-ac2.md). El equipo debe revisar su contenido y completar las declaraciones de uso de IA antes de la entrega.

## Colaboración

Cada integrante trabaja en su propia rama y registra sus aportes con commits que describen los cambios realizados. Los aportes se integran conservando su autoría y se revisan antes de preparar la entrega en `main`.

La rama `main` requiere un Pull Request y una aprobación antes de incorporar nuevos cambios.

La primera entrega se conserva en la etiqueta `Entrega_AC1`. Al aprobar la segunda entrega se creará `Entrega_AC2` sobre la versión final revisada.

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
- **Abstracción:** `Person` hereda de `ABC` y declara `realizar_actividad_principal()` como abstracto. Solo se crean objetos de las clases hijas que implementan ese comportamiento
- **Sobreescritura:** las clases hijas implementan sus propias versiones de `mostrar_informacion()` y `realizar_actividad_principal()` para presentar sus datos y actividades
- **Polimorfismo:** la consulta general recorre una colección con los seis objetos usando un único ciclo que llama a los mismos métodos sin identificar su tipo

La consulta general utiliza los nombres solicitados en el enunciado y llama ambos métodos sobre los seis objetos mediante un único ciclo en la vista. Los menús por área no sustituyen ese recorrido común.

## Uso de inteligencia artificial

Se utilizó ChatGPT/Codex como apoyo para interpretar los requisitos, preparar la propuesta de diseño y la estructura inicial, generar y revisar bloques de integración y de interacción por consola, corregir errores y elaborar documentación. También se utilizó Claude como apoyo para proponer la distribución de tareas.

El uso de esta herramienta se declara de acuerdo con las orientaciones de la actividad. Cada integrante es responsable de revisar, comprender y poder explicar los aportes que incorpore al proyecto. Se registrarán aquí los usos adicionales durante el desarrollo.
