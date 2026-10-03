from abc import ABC, abstractmethod


class Habitacion(ABC):
    """Clase abstracta con los datos comunes de las habitaciones."""

    def __init__(self, numero, capacidad, tarifa_por_noche):
        if not isinstance(numero, str) or not numero.strip():
            raise ValueError("El número de habitación debe ser un texto no vacío.")

        if type(capacidad) is not int or capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero positivo.")

        if (
            type(tarifa_por_noche) not in (int, float)
            or tarifa_por_noche <= 0
        ):
            raise ValueError("La tarifa por noche debe ser positiva.")

        self.__numero = numero.strip()
        self.__capacidad = capacidad
        self.__tarifa_por_noche = tarifa_por_noche

    @property
    def numero(self):
        return self.__numero

    @property
    def capacidad(self):
        return self.__capacidad

    @property
    def tarifa_por_noche(self):
        return self.__tarifa_por_noche

    def validar_noches(self, noches):
        """Comprueba que la estancia tenga al menos una noche."""
        if type(noches) is not int or noches <= 0:
            raise ValueError("Las noches deben ser un entero positivo.")

    @abstractmethod
    def calcular_precio(self, noches):
        """Cada tipo de habitación define su cálculo del precio."""
        pass

    @abstractmethod
    def describir(self):
        """Cada tipo de habitación devuelve su descripción."""
        pass
    