import unittest

from models.horario import Horario


class HorarioTest(unittest.TestCase):
    def test_consultar_horario_completo(self):
        # Esta consulta fallaba porque faltaban los getters de las horas
        horario = Horario("lunes", "07:00", "09:00", "101")
        self.assertEqual(
            horario.mostrar_horario(),
            "Lunes de 07:00 a 09:00 en el salón 101",
        )

    def test_rechazar_cambios_invalidos_sin_perder_los_datos(self):
        horario = Horario("lunes", "07:00", "09:00", "101")
        cambios = [
            (horario.set_dia, "festivo"),
            (horario.set_hora_inicio, "24:00"),
            (horario.set_hora_fin, "09:60"),
            (horario.set_salon, "   "),
        ]
        # Si un cambio falla, el horario anterior debe seguir disponible
        for actualizar, dato in cambios:
            with self.subTest(campo=actualizar.__name__):
                with self.assertRaises(ValueError):
                    actualizar(dato)
                self.assertEqual(
                    horario.mostrar_horario(),
                    "Lunes de 07:00 a 09:00 en el salón 101",
                )


if __name__ == "__main__":
    unittest.main()
