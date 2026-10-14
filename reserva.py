from habitacion import Habitacion
from huesped import Huesped
from detalle_estadia import DetalleEstadia
from excepciones import (
    CapacidadExcedidaError,
    HabitacionNoDisponibleError,
)


class Reserva:
    """Relaciona un huésped con una habitación y su estadía."""

    def __init__(
        self, codigo, huesped, habitacion,
        fecha_entrada, fecha_salida, cantidad_huespedes
    ):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código de reserva no puede estar vacío.")

        if not isinstance(huesped, Huesped):
            raise ValueError("Debe proporcionar un huésped válido.")

        if not isinstance(habitacion, Habitacion):
            raise ValueError("Debe proporcionar una habitación válida.")

        # Composición: cada reserva crea su propio detalle de estadía.
        self.__detalle = DetalleEstadia(
            fecha_entrada, fecha_salida, cantidad_huespedes
        )

        if cantidad_huespedes > habitacion.capacidad:
            raise CapacidadExcedidaError(
                "La cantidad de huéspedes supera la capacidad "
                "de la habitación."
            )

        self.__codigo = codigo.strip()
        self.__huesped = huesped
        self.__habitacion = habitacion
        self.__confirmada = False

    @property
    def codigo(self):
        return self.__codigo

    @property
    def huesped(self):
        return self.__huesped

    @property
    def habitacion(self):
        return self.__habitacion

    @property
    def detalle(self):
        return self.__detalle

    @property
    def confirmada(self):
        return self.__confirmada

    def calcular_total(self):
        noches = self.__detalle.calcular_noches()
        return self.__habitacion.calcular_precio(noches)

    def confirmar(self, reservas_existentes):
        """Comprueba la disponibilidad antes de confirmar."""
        for reserva in reservas_existentes:
            if reserva is self or not reserva.confirmada:
                continue

            misma_habitacion = (
                reserva.habitacion.numero == self.__habitacion.numero
            )

            fechas_cruzadas = (
                self.__detalle.fecha_entrada < reserva.detalle.fecha_salida
                and self.__detalle.fecha_salida > reserva.detalle.fecha_entrada
            )

            if misma_habitacion and fechas_cruzadas:
                raise HabitacionNoDisponibleError(
                    "La habitación ya está reservada para esas fechas."
                )

        self.__confirmada = True

    def describir(self):
        estado = "Confirmada" if self.__confirmada else "Pendiente"
        return (
            f"Reserva {self.__codigo} - {estado}\n"
            f"Huésped: {self.__huesped.nombre}\n"
            f"{self.__habitacion.describir()}\n"
            f"{self.__detalle.describir()}\n"
            f"Total: {self.calcular_total():.2f}"
        )