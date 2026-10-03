from habitacion import Habitacion


class HabitacionIndividual(Habitacion):
    """Habitación para una persona con desayuno opcional."""

    def __init__(self, numero, tarifa_por_noche, incluye_desayuno=False):
        super().__init__(numero, 1, tarifa_por_noche)

        if type(incluye_desayuno) is not bool:
            raise ValueError("Incluye desayuno debe ser True o False.")

        self.__incluye_desayuno = incluye_desayuno

    @property
    def incluye_desayuno(self):
        return self.__incluye_desayuno

    def calcular_precio(self, noches):
        self.validar_noches(noches)
        costo_desayuno = 15 if self.__incluye_desayuno else 0
        return (self.tarifa_por_noche + costo_desayuno) * noches

    def describir(self):
        desayuno = "con desayuno" if self.__incluye_desayuno else "sin desayuno"
        return (
            f"Habitación individual {self.numero}: "
            f"capacidad para {self.capacidad} persona, {desayuno}."
        )
    