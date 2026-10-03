# Diagrama UML — Sistema de Reservas de Hotel

El diagrama representa el diseño previsto del sistema.
La clase Huesped está pendiente de incorporación.

```mermaid
classDiagram
    direction TB

    class Habitacion {
        <<abstract>>
        -numero: str
        -capacidad: int
        -tarifa_por_noche: float
        +validar_noches(noches)
        +calcular_precio(noches) float
        +describir() str
    }

    class HabitacionIndividual {
        -incluye_desayuno: bool
        +calcular_precio(noches) float
        +describir() str
    }

    class HabitacionDoble {
        -tipo_camas: str
        -tiene_balcon: bool
        +calcular_precio(noches) float
        +describir() str
    }

    class Suite {
        -servicios: list
        -cargo_extra_por_noche: float
        +calcular_precio(noches) float
        +describir() str
    }

    class Huesped {
        -nombre: str
        -identificacion: str
    }

    class DetalleEstadia {
        -fecha_entrada: date
        -fecha_salida: date
        -cantidad_huespedes: int
        +calcular_noches() int
        +describir() str
    }

    class Reserva {
        -codigo: str
        -confirmada: bool
        +calcular_total() float
        +confirmar(reservas_existentes)
        +describir() str
    }

    Habitacion <|-- HabitacionIndividual
    Habitacion <|-- HabitacionDoble
    Habitacion <|-- Suite

    Reserva "0..*" --> "1" Huesped : corresponde a
    Reserva "0..*" --> "1" Habitacion : reserva
    Reserva "1" *-- "1" DetalleEstadia : crea y contiene
```

## Relaciones

- Herencia: HabitacionIndividual, HabitacionDoble y Suite son tipos de Habitacion.
- Asociación: cada Reserva corresponde a un Huesped y a una Habitacion.
- Composición: Reserva crea y contiene su propio DetalleEstadia.
- Un huésped o una habitación pueden estar asociados a varias reservas.
- Las reservas confirmadas de una misma habitación no pueden tener fechas que se crucen.
