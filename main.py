from datetime import date

from habitacion_individual import HabitacionIndividual
from habitacion_doble import HabitacionDoble
from suite import Suite
from huesped import Huesped
from reserva import Reserva
from excepciones import (
    FechasInvalidasError,
    CapacidadExcedidaError,
    HabitacionNoDisponibleError,
)


def main():
    # Colección heterogénea para demostrar polimorfismo.
    habitaciones = [
        HabitacionIndividual("101", 80, incluye_desayuno=True),
        HabitacionDoble(
            "201", 120,
            tipo_camas="dos individuales",
            tiene_balcon=True
        ),
        Suite(
            "301", 200,
            servicios=["Jacuzzi", "Sala privada"],
            cargo_extra_por_noche=50
        ),
    ]

    print("=== HABITACIONES DEL HOTEL ===")

    for habitacion in habitaciones:
        print(habitacion.describir())
        print(
            f"Precio por 2 noches: "
            f"{habitacion.calcular_precio(2):.2f}"
        )
        print()

    huespedes = [
        Huesped("Sara Pineda", "1001"),
        Huesped("Ana Castro", "1002"),
        Huesped("Emiliano Osorio", "1003"),
    ]

    print("=== HUÉSPEDES ===")

    for huesped in huespedes:
        print(huesped.describir())

    # Tres habitaciones, tres huéspedes y tres reservas:
    # nueve objetos, además de los detalles creados por composición.
    reservas = []

    print("\n=== RESERVAS VÁLIDAS ===")

    for indice in range(3):
        reserva = Reserva(
            f"R00{indice + 1}",
            huespedes[indice],
            habitaciones[indice],
            date(2026, 10, 20),
            date(2026, 10, 22),
            indice + 1
        )
        reserva.confirmar(reservas)
        reservas.append(reserva)
        print(reserva.describir())
        print()

    print("=== PRUEBA DE FECHAS INVÁLIDAS ===")

    try:
        Reserva(
            "R004",
            huespedes[0],
            habitaciones[0],
            date(2026, 10, 22),
            date(2026, 10, 20),
            1
        )
    except FechasInvalidasError as error:
        print(f"Error controlado: {error}")

    print("El programa continúa.\n")

    print("=== PRUEBA DE CAPACIDAD EXCEDIDA ===")

    try:
        Reserva(
            "R005",
            huespedes[1],
            habitaciones[1],
            date(2026, 10, 24),
            date(2026, 10, 26),
            3
        )
    except CapacidadExcedidaError as error:
        print(f"Error controlado: {error}")

    print("El programa continúa.\n")

    print("=== PRUEBA DE HABITACIÓN NO DISPONIBLE ===")

    try:
        reserva_cruzada = Reserva(
            "R006",
            huespedes[2],
            habitaciones[0],
            date(2026, 10, 21),
            date(2026, 10, 23),
            1
        )
        reserva_cruzada.confirmar(reservas)
        reservas.append(reserva_cruzada)
    except HabitacionNoDisponibleError as error:
        print(f"Error controlado: {error}")

    print("El programa continúa.\n")

    print("=== RESERVA CONSECUTIVA VÁLIDA ===")

    reserva_consecutiva = Reserva(
        "R007",
        huespedes[1],
        habitaciones[0],
        date(2026, 10, 22),
        date(2026, 10, 24),
        1
    )
    reserva_consecutiva.confirmar(reservas)
    reservas.append(reserva_consecutiva)
    print(reserva_consecutiva.describir())

    print(f"\nTotal de reservas confirmadas: {len(reservas)}")
    print("=== FIN DE LA DEMOSTRACIÓN ===")


if __name__ == "__main__":
    main()