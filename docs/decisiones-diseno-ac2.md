# Documento de Decisiones de Diseño

Sistema de Gestión Académica · Actividad colaborativa 2  
Universidad de Manizales · Programación I  
Integrantes: Silvana, Kelly, Oscar, Stefanny y Lizeth

**Borrador parcial para revisión del equipo.** Describe los componentes integrados en Oscar. Las relaciones y operaciones de GrupoAcadémico deben completarse cuando esté disponible su implementación.

## Introducción

La segunda actividad amplía el sistema construido en la primera entrega. Conservamos los modelos y la aplicación de consola y agregamos la abstracción de personas, los horarios y las excepciones académicas. El objetivo es incorporar la oferta de grupos y la matrícula sin crear otro proyecto.

## Solución implementada y organización

Mantenemos la organización MVC. Los modelos representan las entidades y validan sus datos, las vistas reciben entradas y muestran mensajes y los controladores coordinan las acciones. `main.py` prepara los objetos, conecta las áreas y captura las excepciones académicas. Las búsquedas compartidas están en `controllers/busquedas.py` y las clases de excepción en `exceptions/academicas.py` para evitar repetirlas.

Los datos se mantienen en memoria durante la sesión. Cuando una búsqueda falla, main muestra el mensaje y permite regresar al menú principal sin reconstruir los objetos ni perder los cambios anteriores.

## Abstracción de las personas

`Person`, en `models/persona.py`, hereda de la clase `ABC` del módulo `abc`. Su método `realizar_actividad_principal()` usa el decorador `@abstractmethod`. Así se impide crear una persona genérica sin establecer su rol y se exige que cada clase especializada implemente su actividad.

`Student`, `Teacher` y `Administrative` conservan los datos comunes y aportan su propia implementación de la actividad. El estudiante describe su actividad académica, el docente la enseñanza en su departamento y el administrativo su trabajo según su cargo y dependencia. La información particular también se presenta mediante la sobreescritura de `mostrar_informacion()`.

La opción 6 del menú llama a `comprobar_persona_abstracta()` en main. Allí se intenta crear un objeto de Person y se captura el TypeError esperado, mostrando una explicación antes de continuar. Esta comprobación se ejecuta cuando el usuario la selecciona.

## Conservación del polimorfismo

`crear_personas_ejemplo()` prepara una colección con dos estudiantes, dos docentes y dos administrativos. `PersonaView.mostrar_personas()` recorre esa colección con un único ciclo y llama a `mostrar_informacion()` y `realizar_actividad_principal()` sin comprobar el tipo de cada objeto. Python ejecuta la implementación de cada clase hija.

Las listas por área contienen referencias a los mismos objetos de la colección general. Por eso, al actualizar un estudiante desde su área, el cambio también aparece en la consulta de todas las personas.

## Horarios y relaciones pendientes de integración

`Horario`, en `models/horario.py`, almacena día, hora de inicio, hora de finalización y salón mediante atributos privados. Los setters verifican el día, el formato de las horas y que el salón tenga contenido. Los getters permiten consultar los datos y `mostrar_horario()` devuelve una descripción legible.

Falta documentar sobre el código final cómo GrupoAcadémico recibe los objetos existentes de Asignatura y Docente, conserva los estudiantes y crea su Horario como parte del grupo. La relación prevista es de composición: un grupo contiene un horario que describe cuándo y dónde se desarrolla. Un grupo no es una especialización de Horario, por lo que no corresponde usar herencia. Esta decisión debe verificarse en la implementación y explicarse también en el README.

## Excepciones personalizadas y búsquedas

Las cinco excepciones heredan de `Exception` y construyen mensajes con los códigos involucrados. `EXCEPCIONES_ACADEMICAS` las reúne en una tupla que permite capturarlas con un solo except en main.

`buscar_asignatura_por_codigo()` y `buscar_programa_por_codigo()` recorren las listas y consultan `get_code()`. Antes de comparar limpian espacios y convierten los códigos a mayúsculas. Si no encuentran el registro, lanzan `AsignaturaInexistenteError` o `ProgramaInexistenteError`. Se eligió lanzar una excepción en lugar de devolver None para que la operación interrumpida tenga un tratamiento explícito y no se utilice después un objeto inexistente.

Los controladores de programas y asignaturas usan estas funciones tanto para buscar como para seleccionar el objeto que se actualizará. Las excepciones llegan a main, donde se muestran sus mensajes y se retoma el menú. Un código vacío genera ValueError, que también se captura.

`EstudianteDuplicadoError`, `GrupoLlenoError` y `EstudianteNoMatriculadoError` ya están definidas y probadas de forma aislada. Falta integrar su lanzamiento desde matrícula y retiro en GrupoAcadémico. No se considera terminada esa funcionalidad hasta comprobar las operaciones reales desde el programa principal.

## Verificación

Las pruebas con unittest comprueban la abstracción, el recorrido polimórfico, la consulta del horario y la conservación de los datos tras cambios inválidos. Las pruebas de integración ejecutan main con entradas simuladas y verifican búsquedas correctas, códigos inexistentes, códigos vacíos y continuidad después de los errores.

Quedan pendientes las pruebas de al menos dos grupos, matrícula correcta, duplicados, capacidad máxima, retiro correcto y retiro de un estudiante no matriculado. También falta mostrar los horarios de los grupos desde la aplicación.

## Uso de inteligencia artificial

Se utilizó ChatGPT/Codex para apoyar la interpretación de requisitos, revisar código, generar y ajustar bloques de integración, pruebas y documentación. Steffany declaró apoyo de IA para comprender abc y las expresiones regulares de Horario. Silvana declaró el uso de Claude de Anthropic como apoyo para escribir el código de excepciones y búsquedas. El equipo debe completar esta declaración con los usos de las demás integrantes y revisar y comprender el contenido antes de entregar.

## Conclusiones parciales

La integración actual conserva el sistema anterior y permite incorporar nuevas reglas sin duplicar las entidades. La abstracción mantiene las actividades específicas de cada rol y las búsquedas comunican los errores sin finalizar el programa. La entrega requiere completar los grupos, la composición y las operaciones de matrícula y retiro, actualizar este documento con el resultado y verificar todos los casos solicitados.
