# Documento de Decisiones de Diseño

Sistema de Gestión Académica · Actividad colaborativa 2  
Universidad de Manizales · Programación I  
Integrantes: Silvana, Kelly, Oscar, Stefanny y Lizeth

**Versión para revisión del equipo.** Describe los componentes integrados en Oscar. Antes de la entrega cada integrante debe revisar su aporte y completar la declaración de uso de IA.

## Introducción

La segunda actividad amplía el sistema construido en la primera entrega. Conservamos los modelos y la aplicación de consola y agregamos la abstracción de personas, los horarios y las excepciones académicas. El objetivo es incorporar la oferta de grupos y la matrícula sin crear otro proyecto.

## Solución implementada y organización

Mantenemos la organización MVC. Los modelos representan las entidades y validan sus datos, las vistas reciben entradas y muestran mensajes y los controladores coordinan las acciones. `main.py` prepara los objetos, conecta las áreas y captura las excepciones académicas. Las búsquedas compartidas están en `controllers/busquedas.py` y las clases de excepción en `exceptions/academicas.py` para evitar repetirlas.

Los datos se mantienen en memoria durante la sesión. Cuando una búsqueda falla, main muestra el mensaje y permite regresar al menú principal sin reconstruir los objetos ni perder los cambios anteriores.

## Abstracción de las personas

`Person`, en `models/persona.py`, hereda de la clase `ABC` del módulo `abc`. Su método `realizar_actividad_principal()` usa el decorador `@abstractmethod`. Así se impide crear una persona genérica sin establecer su rol y se exige que cada clase especializada implemente su actividad.

`Student`, `Teacher` y `Administrative` conservan los datos comunes y aportan su propia implementación de la actividad. El estudiante describe su actividad académica, el docente la enseñanza en su departamento y el administrativo su trabajo según su cargo y dependencia. La información particular también se presenta mediante la sobreescritura de `mostrar_informacion()`.

La opción 1 de Prueba de diseño para la actividad, accesible desde la opción 5 del menú principal, llama a `comprobar_persona_abstracta()` en main. Allí se intenta crear un objeto de Person y se captura el TypeError esperado, mostrando una explicación antes de continuar. Esta comprobación se ejecuta cuando el usuario la selecciona.

## Conservación del polimorfismo

`crear_personas_ejemplo()` prepara una colección con dos estudiantes, dos docentes y dos administrativos. `PersonaView.mostrar_personas()` recorre esa colección con un único ciclo y llama a `mostrar_informacion()` y `realizar_actividad_principal()` sin comprobar el tipo de cada objeto. Python ejecuta la implementación de cada clase hija.

Las listas por área contienen referencias a los mismos objetos de la colección general. Por eso, al actualizar un estudiante desde su área, el cambio también aparece en la consulta de todas las personas.

## Grupos, horarios y composición

`Horario`, en `models/horario.py`, almacena día, hora de inicio, hora de finalización y salón mediante atributos privados. Los setters verifican el día, el formato de las horas y que el salón tenga contenido. Los getters permiten consultar los datos y `mostrar_horario()` devuelve una descripción legible.

`GrupoAcademico` recibe objetos existentes de Asignatura y Teacher. Su lista de matriculados guarda objetos Student. Estas referencias permiten consultar información actualizada sin copiar los nombres de las entidades. `crear_grupos_ejemplo()` prepara G1 y G2 desde main y los entrega a GrupoController junto con los estudiantes disponibles.

El constructor de GrupoAcademico crea su propio Horario a partir del día, las horas y el salón recibidos. La relación es de composición: el horario forma parte de la organización del grupo. Un grupo contiene un horario y no es una especialización de Horario, por lo que no corresponde usar herencia. Asignaturas y docentes se reciben ya creados y pueden existir independientemente de un grupo.

`GrupoView` muestra las opciones y recoge los códigos. `GrupoController` selecciona los objetos y llama a `matricular_estudiante()`, `retirar_estudiante()` y `mostrar_estudiantes()`. Las reglas de cupos y duplicados permanecen en el modelo, para que no dependan de la interfaz de consola.

## Excepciones personalizadas y búsquedas

Las cinco excepciones heredan de `Exception` y construyen mensajes con los códigos involucrados. `EXCEPCIONES_ACADEMICAS` las reúne en una tupla que permite capturarlas con un solo except en main.

`buscar_asignatura_por_codigo()` y `buscar_programa_por_codigo()` recorren las listas y consultan `get_code()`. Antes de comparar limpian espacios y convierten los códigos a mayúsculas. Si no encuentran el registro, lanzan `AsignaturaInexistenteError` o `ProgramaInexistenteError`. Se eligió lanzar una excepción en lugar de devolver None para que la operación interrumpida tenga un tratamiento explícito y no se utilice después un objeto inexistente.

Los controladores de programas y asignaturas usan estas funciones tanto para buscar como para seleccionar el objeto que se actualizará. Las excepciones llegan a main, donde se muestran sus mensajes y se retoma el menú. Un código vacío genera ValueError, que también se captura.

`matricular_estudiante()` compara el código estudiantil con los matriculados y lanza EstudianteDuplicadoError si ya existe. Después comprueba la capacidad y lanza GrupoLlenoError si no queda cupo. Solo agrega el estudiante cuando ambas comprobaciones se cumplen. `retirar_estudiante()` busca por código estudiantil y lanza EstudianteNoMatriculadoError si no lo encuentra. Estas excepciones pasan por el controlador hasta main, que informa el problema y permite continuar sin reconstruir los grupos.

## Verificación

Las pruebas con unittest comprueban la abstracción, el recorrido polimórfico, la consulta del horario y la conservación de los datos tras cambios inválidos. Las pruebas de integración ejecutan main con entradas simuladas y verifican búsquedas correctas, códigos inexistentes, códigos vacíos y continuidad después de los errores.

Las pruebas de integración también ejecutan el área de grupos desde main con entradas simuladas. Comprueban los dos grupos y sus horarios, la matrícula y el retiro correctos, los tres errores de matrícula y la continuidad posterior. Tras una excepción verifican que se conserva la matrícula anterior y que un retiro libera el cupo. Otra prueba comprueba que los grupos conservan las referencias a los objetos originales y que tienen horarios distintos. Las pruebas no se ejecutan automáticamente al abrir la aplicación.

## Uso de inteligencia artificial

Durante el desarrollo utilizamos ChatGPT/Codex y Claude de Anthropic como herramientas de apoyo para comprender los requisitos y conceptos de programación orientada a objetos, organizar las tareas, revisar errores y preparar documentación. También se usó ChatGPT/Codex para generar y ajustar bloques de código de la interfaz de consola y de la integración de los componentes.

Las pruebas unitarias y de integración incorporadas en la carpeta `tests/` fueron generadas con apoyo de inteligencia artificial. ChatGPT/Codex escribió las pruebas de personas, horarios, grupos y navegación por consola, y las ejecutó para comprobar los resultados. Estas pruebas permitieron detectar errores como los getters faltantes de Horario y las validaciones de capacidad de GrupoAcademico. Las correcciones de capacidad y sus pruebas también se elaboraron con esta herramienta. Silvana declaró el uso de Claude para escribir su código de excepciones y búsquedas y compartió las pruebas que acompañan ese aporte.

Steffany declaró apoyo de IA para comprender el módulo abc y preparar las expresiones regulares de Horario. Stefania utilizó inteligencia artificial como apoyo para desarrollar la vista y el controlador de grupos académicos, organizar el menú de consola y comprender cómo conectar las consultas, la matrícula y el retiro con el modelo. Este apoyo incluyó la generación de los bloques de código de ambos archivos.

El uso de estas herramientas no sustituye la responsabilidad de cada integrante de revisar, comprender y poder explicar el código, las pruebas y las decisiones de diseño que incorpora a la entrega. Antes de entregar, cada integrante debe confirmar que esta declaración refleje el uso realizado y completar cualquier apoyo adicional que no esté registrado aquí.

## Conclusiones

La integración conserva el sistema anterior y permite incorporar grupos sin duplicar las entidades académicas. La abstracción mantiene las actividades específicas de cada rol, la composición organiza el horario del grupo y las excepciones comunican los problemas sin finalizar el programa. La separación entre modelo, vista y controlador permite probar las reglas y la interacción por consola. Los datos se mantienen en memoria, por lo que no se conservan al cerrar la aplicación.
