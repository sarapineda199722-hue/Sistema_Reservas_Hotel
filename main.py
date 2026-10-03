from habitacion_individual import HabitacionIndividual
from habitacion_doble import HabitacionDoble
from suite import Suite


def main():
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

    noches = 2

    print("=== HABITACIONES DEL HOTEL ===")

    for habitacion in habitaciones:
        print(habitacion.describir())
        print(f"Precio por {noches} noches: {habitacion.calcular_precio(noches):.2f}")
        print()

    print("=== FIN DE LA PRUEBA ===")


if __name__ == "__main__":
    main()
    