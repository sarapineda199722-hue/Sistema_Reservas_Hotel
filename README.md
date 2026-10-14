# Sistema de Reservas de Hotel

Proyecto de la Actividad Colaborativa N.º 3: Proyecto Final,
de la asignatura Programación I de la Universidad de Manizales.

## Descripción

El sistema permite representar diferentes tipos de habitaciones,
registrar huéspedes y crear reservas con fechas de entrada y salida.

Calcula el precio de las estadías y controla fechas inválidas,
capacidad excedida y habitaciones no disponibles por cruces
con reservas confirmadas.

Funciona en consola y almacena los objetos en memoria.
No utiliza una base de datos ni guarda las reservas al cerrar
el programa.

## Clases del sistema

| Clase | Responsabilidad |
|---|---|
| Habitacion | Clase abstracta que reúne los datos comunes y define los métodos de las habitaciones. |
| HabitacionIndividual | Representa una habitación para una persona con desayuno opcional. |
| HabitacionDoble | Representa una habitación para dos personas con tipo de camas y balcón opcional. |
| Suite | Representa una habitación para cuatro personas con servicios y un cargo adicional. |
| Huesped | Guarda el nombre y la identificación de quien realiza la reserva. |
| DetalleEstadia | Guarda las fechas y la cantidad de huéspedes y calcula las noches. |
| Reserva | Relaciona al huésped con la habitación, crea su detalle de estadía y controla la confirmación. |

El proyecto contiene seis clases concretas y una clase abstracta,
además de las tres clases de excepciones personalizadas.

## Conceptos de programación orientada a objetos

### Abstracción

Habitacion hereda de ABC y declara los métodos abstractos
calcular_precio y describir. No puede instanciarse directamente.

### Herencia y especialización

HabitacionIndividual, HabitacionDoble y Suite heredan de Habitacion.

Las tres comparten número, capacidad y tarifa por noche.
Cada una tiene atributos propios que intervienen en su descripción
y en el cálculo del precio.

### Encapsulamiento

Los atributos se almacenan con doble guion bajo y se consultan
mediante propiedades. Los constructores validan los datos recibidos.

La propiedad servicios de Suite devuelve una copia para evitar
modificar directamente la lista interna.

### Sobreescritura y polimorfismo

Las tres clases hijas sobrescriben calcular_precio y describir.

main.py crea una lista con los tres tipos de habitaciones.
Un único ciclo llama a los mismos métodos sobre cada objeto,
sin condicionales para seleccionar el comportamiento por su tipo.

### Asociaciones

Reserva se relaciona con un objeto Huesped y un objeto Habitacion.

Un huésped y una habitación pueden participar en distintas reservas
y existir independientemente de ellas.

### Composición

Cada Reserva crea su propio DetalleEstadia dentro del constructor.
El detalle forma parte de la reserva y no se comparte entre reservas.

No se utiliza herencia porque una reserva contiene un detalle
de estadía; no es un detalle de estadía.

## Excepciones personalizadas

| Excepción | Situación controlada | Método que la lanza |
|---|---|---|
| FechasInvalidasError | La salida es igual o anterior a la entrada. | Constructor de DetalleEstadia. |
| CapacidadExcedidaError | La cantidad de huéspedes supera la capacidad. | Constructor de Reserva. |
| HabitacionNoDisponibleError | Existen fechas cruzadas con una reserva confirmada de la misma habitación. | confirmar de Reserva. |

main.py captura cada excepción, muestra un mensaje claro
y continúa con las siguientes demostraciones.

Las validaciones generales de datos utilizan ValueError.

## Archivos del proyecto

- habitacion.py
- habitacion_individual.py
- habitacion_doble.py
- suite.py
- huesped.py
- detalle_estadia.py
- reserva.py
- excepciones.py
- main.py
- README.md
- diagrama_uml.md
- decisiones_diseno.md

## Requisitos

- Python 3.13, versión utilizada durante el desarrollo.
- No requiere instalar bibliotecas externas.

## Cómo ejecutar

Descarga o clona el repositorio y abre una terminal
dentro de la carpeta Sistema_Reservas_Hotel.

Ejecuta:

```bash
python main.py
```

En Windows, si python no está disponible, puedes utilizar:

```bash
py main.py
```

## Demostración del programa

El programa principal:

1. Muestra los tres tipos de habitaciones mediante polimorfismo.
2. Calcula sus precios para dos noches.
3. Crea y muestra tres huéspedes.
4. Crea y confirma tres reservas en habitaciones diferentes.
5. Captura una excepción por fechas inválidas.
6. Captura una excepción por capacidad excedida.
7. Captura una excepción por una habitación no disponible.
8. Confirma una reserva consecutiva válida.
9. Muestra el total de cuatro reservas confirmadas.

Se crean tres habitaciones, tres huéspedes y cuatro reservas válidas:
diez objetos de las entidades principales, además de sus detalles
de estadía y la reserva cuya confirmación se rechaza.

## Resultados esperados

| Habitación | Cálculo para dos noches | Total |
|---|---|---|
| Individual con desayuno | (80 + 15) × 2 | 190.00 |
| Doble con balcón | (120 + 20) × 2 | 280.00 |
| Suite con cargo adicional | (200 + 50) × 2 | 500.00 |

Los cargos y las capacidades son reglas elegidas
para la demostración académica.

Una reserva puede comenzar el mismo día en que termina otra.
Las reservas pendientes no bloquean la disponibilidad.

## Verificación realizada

Se ejecutó python main.py y se comprobó que:

- Los precios coinciden con los resultados esperados.
- Las tres reservas iniciales se confirman correctamente.
- Se capturan las tres excepciones personalizadas.
- El programa continúa después de cada error controlado.
- Se rechaza una reserva con fechas cruzadas.
- Se permite una reserva consecutiva.
- El total final es de cuatro reservas confirmadas.
- La ejecución llega a FIN DE LA DEMOSTRACIÓN sin errores
  no controlados.

Esta verificación corresponde a los casos incluidos en main.py.

## Documentación

- [Diagrama UML de clases](diagrama_uml.md).
- [Documento de Decisiones de Diseño](decisiones_diseno.md).

## Uso de inteligencia artificial

Se utilizó ChatGPT como apoyo en el desarrollo del código
y la documentación. Su uso se describe en el Documento
de Decisiones de Diseño.

## Alcance y limitaciones

El proyecto es una demostración académica en consola.

La comprobación de disponibilidad requiere proporcionar
la lista completa de reservas existentes al método confirmar.
El número de habitación se considera único dentro del hotel.

No incluye interfaz gráfica, pagos, base de datos
ni almacenamiento permanente.