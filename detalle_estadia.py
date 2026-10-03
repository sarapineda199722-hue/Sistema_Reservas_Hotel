from datetime import date


class DetalleEstadia:
    """Guarda las fechas y la cantidad de huéspedes de una reserva."""

    def __init__(self, fecha_entrada, fecha_salida, cantidad_huespedes):
        if type(fecha_entrada) is not date or type(fecha_salida) is not date:
            raise ValueError("Las fechas deben ser objetos de tipo date.")

        if fecha_salida <= fecha_entrada:
            raise ValueError("La salida debe ser posterior a la entrada.")

        if type(cantidad_huespedes) is not int or cantidad_huespedes <= 0:
            raise ValueError("La cantidad de huéspedes debe ser un entero positivo.")

        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida
        self.__cantidad_huespedes = cantidad_huespedes

    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @property
    def cantidad_huespedes(self):
        return self.__cantidad_huespedes

    def calcular_noches(self):
        return (self.__fecha_salida - self.__fecha_entrada).days

    def describir(self):
        return (
            f"Entrada: {self.__fecha_entrada.isoformat()}, "
            f"salida: {self.__fecha_salida.isoformat()}, "
            f"huéspedes: {self.__cantidad_huespedes}, "
            f"noches: {self.calcular_noches()}."
        )
    