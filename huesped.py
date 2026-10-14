class Huesped:
    """Representa a la persona que realiza una reserva."""

    def __init__(self, nombre, identificacion):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not isinstance(identificacion, str) or not identificacion.strip():
            raise ValueError("La identificación no puede estar vacía.")

        self.__nombre = nombre.strip()
        self.__identificacion = identificacion.strip()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def identificacion(self):
        return self.__identificacion

    def describir(self):
        return (
            f"Huésped: {self.__nombre}, "
            f"identificación: {self.__identificacion}."
        )