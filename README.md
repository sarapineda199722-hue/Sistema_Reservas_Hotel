# Sistema de Reservas de Hotel

Proyecto desarrollado para la Actividad Colaborativa N.º 3
de Programación I.

## Integrantes

- Sara Liliana Pineda Castro
- Julián Loaiza Botero

## Descripción

El sistema permite representar habitaciones individuales, dobles
y suites, calcular el precio de una estadía y gestionar reservas.

Cada tipo de habitación tiene características propias y una forma
de calcular su precio.

## Clases del proyecto

- Habitacion: clase abstracta con los datos comunes de las habitaciones.
- HabitacionIndividual: habitación para una persona, con desayuno opcional.
- HabitacionDoble: habitación para dos personas, con tipo de camas y balcón opcional.
- Suite: habitación para cuatro personas, con servicios y un cargo adicional.
- DetalleEstadia: guarda las fechas y la cantidad de huéspedes.
- Reserva: relaciona al huésped con la habitación y crea su detalle de estadía.
- Huesped: clase pendiente de incorporación para representar al huésped.

## Conceptos de programación utilizados

- Abstracción mediante la clase Habitacion.
- Herencia en los tres tipos de habitaciones.
- Encapsulación de atributos mediante propiedades.
- Polimorfismo al recorrer una lista de habitaciones y llamar
  a los mismos métodos.
- Composición: cada reserva crea su propio DetalleEstadia.

## Requisitos

- Python 3.13.
- No requiere instalar bibliotecas externas.

## Cómo ejecutar

Desde una terminal ubicada en la carpeta del proyecto:

python main.py

## Estado actual

La prueba actual muestra los tres tipos de habitaciones y calcula
sus precios para una estadía de dos noches.

Queda pendiente integrar la clase Huesped, las tres excepciones
personalizadas y ampliar el programa principal con pruebas de reservas
y manejo de errores. También falta incorporar el diagrama UML y el
documento de decisiones de diseño.

## Uso de inteligencia artificial

Se utilizó ChatGPT como apoyo para proponer la estructura del proyecto,
explicar conceptos de programación orientada a objetos y generar
fragmentos de código.

La prueba inicial de habitaciones se ejecutó en Python. La revisión
y validación del sistema completo se realizarán al integrar las
partes pendientes.
