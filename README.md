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

El archivo principal contiene únicamente la estructura de inicio; todavía no ejecuta funcionalidades académicas ni abre una interfaz gráfica.

## Integrantes

Pendiente de completar con los nombres de todos los integrantes del equipo.

## Conceptos de programación orientada a objetos

El diseño previsto para la primera actividad contempla:

- **Encapsulamiento:** proteger los atributos y controlar su consulta y modificación mediante métodos con validaciones.
- **Herencia:** compartir los datos generales de `Persona` con `Estudiante`, `Docente` y `Administrativo`.
- **Sobreescritura:** implementar versiones propias de `mostrar_informacion()` y `realizar_actividad_principal()` en cada clase hija.
- **Polimorfismo:** recorrer una colección de estudiantes, docentes y administrativos con un único ciclo que invoque los mismos métodos, sin condicionales por tipo.

Estas decisiones se documentarán conforme se implementen y verifiquen las clases.

## Uso de inteligencia artificial

Se utilizó ChatGPT/Codex como apoyo para interpretar los requisitos de las actividades, elaborar la propuesta inicial de diseño, preparar la estructura MVC y redactar la documentación y el archivo `.gitignore`.

El uso de esta herramienta se declara de acuerdo con las orientaciones de la actividad. Cada integrante es responsable de revisar, comprender y poder explicar los aportes que incorpore al proyecto. Se registrarán aquí los usos adicionales durante el desarrollo.
