# Diagrama UML — Sistema de Reservas de Hotel

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
        +describir() str
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
        -huesped: Huesped
        -habitacion: Habitacion
        -detalle: DetalleEstadia
        -confirmada: bool
        +calcular_total() float
        +confirmar(reservas_existentes)
        +describir() str
    }

    class Exception {
        <<exception>>
    }

    class FechasInvalidasError {
        <<exception>>
    }

    class CapacidadExcedidaError {
        <<exception>>
    }

    class HabitacionNoDisponibleError {
        <<exception>>
    }

    Habitacion <|-- HabitacionIndividual
    Habitacion <|-- HabitacionDoble
    Habitacion <|-- Suite

    Reserva "0..*" --> "1" Huesped : corresponde a
    Reserva "0..*" --> "1" Habitacion : reserva
    Reserva "1" *-- "1" DetalleEstadia : crea y contiene

    Exception <|-- FechasInvalidasError
    Exception <|-- CapacidadExcedidaError
    Exception <|-- HabitacionNoDisponibleError

    DetalleEstadia ..> FechasInvalidasError : lanza
    Reserva ..> CapacidadExcedidaError : lanza
    Reserva ..> HabitacionNoDisponibleError : lanza
```

## Relaciones del sistema

- **Herencia:** HabitacionIndividual, HabitacionDoble y Suite
  heredan de la clase abstracta Habitacion.
- **Asociación:** cada Reserva se relaciona con un Huesped
  y una Habitacion. Estos objetos pueden existir independientemente
  de la reserva.
- **Composición:** cada Reserva crea y contiene un DetalleEstadia
  exclusivo que forma parte de su estructura.
- **Herencia de excepciones:** las tres excepciones personalizadas
  heredan de Exception, una clase incorporada de Python.
- **Dependencia:** las flechas discontinuas indican qué clases
  lanzan las excepciones personalizadas.

## Reglas de disponibilidad

Una habitación puede participar en varias reservas,
pero sus reservas confirmadas no pueden tener fechas cruzadas.

Se permite que una reserva comience el mismo día
en que termina otra. Las reservas pendientes no bloquean
la disponibilidad.

## Encapsulamiento

El signo menos representa los atributos privados.
El signo más representa los métodos públicos.

El código utiliza propiedades para consultar los atributos
de las entidades.