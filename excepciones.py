class FechasInvalidasError(Exception):
    """La fecha de salida no es posterior a la entrada."""
    pass


class CapacidadExcedidaError(Exception):
    """La cantidad de huéspedes supera la capacidad."""
    pass


class HabitacionNoDisponibleError(Exception):
    """La habitación ya tiene una reserva en esas fechas."""
    pass