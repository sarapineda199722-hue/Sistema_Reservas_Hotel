from habitacion import Habitacion


class HabitacionDoble(Habitacion):
    """Habitación para dos personas con tipo de camas y balcón opcional."""

    def __init__(
        self, numero, tarifa_por_noche,
        tipo_camas="matrimonial", tiene_balcon=False
    ):
        super().__init__(numero, 2, tarifa_por_noche)

        if tipo_camas not in ("matrimonial", "dos individuales"):
            raise ValueError(
                "El tipo de camas debe ser 'matrimonial' o 'dos individuales'."
            )

        if type(tiene_balcon) is not bool:
            raise ValueError("Tiene balcón debe ser True o False.")

        self.__tipo_camas = tipo_camas
        self.__tiene_balcon = tiene_balcon

    @property
    def tipo_camas(self):
        return self.__tipo_camas

    @property
    def tiene_balcon(self):
        return self.__tiene_balcon

    def calcular_precio(self, noches):
        self.validar_noches(noches)
        cargo_balcon = 20 if self.__tiene_balcon else 0
        return (self.tarifa_por_noche + cargo_balcon) * noches

    def describir(self):
        balcon = "con balcón" if self.__tiene_balcon else "sin balcón"
        return (
            f"Habitación doble {self.numero}: "
            f"capacidad para {self.capacidad} personas, "
            f"camas: {self.__tipo_camas}, {balcon}."
        )
    