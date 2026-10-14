"""Punto de entrada del Sistema de Gestión Académica."""


def mostrar_personas(personas):
    """Presenta la información y la actividad de cada persona."""
    # Cada objeto decide qué versión de estos métodos ejecutar.
    # No necesitamos preguntar si es estudiante, docente o administrativo.
    for persona in personas:
        print(persona.show_info())
        print(persona.perform_main_activity())
        print()


def main():
    """Inicia la aplicación; funcionalidad pendiente de implementación."""
    pass


if __name__ == "__main__":
    main()
