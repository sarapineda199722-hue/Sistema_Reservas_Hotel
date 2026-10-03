from habitacion import Habitacion


class Suite(Habitacion):
    """Habitación para cuatro personas con servicios adicionales."""

    def __init__(
        self, numero, tarifa_por_noche,
        servicios, cargo_extra_por_noche
    ):
        super().__init__(numero, 4, tarifa_por_noche)

        if (
            not isinstance(servicios, list)
            or not servicios
            or any(
                not isinstance(servicio, str) or not servicio.strip()
                for servicio in servicios
            )
        ):
            raise ValueError("Los servicios deben ser una lista de textos no vacíos.")

        if (
            type(cargo_extra_por_noche) not in (int, float)
            or cargo_extra_por_noche < 0
        ):
            raise ValueError("El cargo extra debe ser un número no negativo.")

        self.__servicios = [servicio.strip() for servicio in servicios]
        self.__cargo_extra_por_noche = cargo_extra_por_noche

    @property
    def servicios(self):
        return self.__servicios.copy()

    @property
    def cargo_extra_por_noche(self):
        return self.__cargo_extra_por_noche

    def calcular_precio(self, noches):
        self.validar_noches(noches)
        return (
            self.tarifa_por_noche + self.__cargo_extra_por_noche
        ) * noches

    def describir(self):
        servicios = ", ".join(self.__servicios)
        return (
            f"Suite {self.numero}: "
            f"capacidad para {self.capacidad} personas, "
            f"servicios: {servicios}, "
            f"cargo extra por noche: {self.__cargo_extra_por_noche:.2f}."
        )
    