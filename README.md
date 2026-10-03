# Sistema de Reservas de Hotel

Proyecto desarrollado para la Actividad Colaborativa N.º 3
de Programación I.

## Integrantes

- Sara Liliana Pineda Castro
- Julián Loaiza Botero

## Descripción

El sistema representa habitaciones individuales, dobles y suites,
calcula el precio de una estadía y permite crear y confirmar reservas.

Las reservas incluyen fechas de entrada y salida y una cantidad
de huéspedes. El sistema comprueba las fechas, la capacidad de
la habitación y los cruces con otras reservas confirmadas.

El proyecto funciona en consola y almacena los objetos en memoria,
sin utilizar una base de datos.

## Clases del proyecto

- Habitacion: clase abstracta con los datos comunes de las habitaciones.
- HabitacionIndividual: habitación para una persona, con desayuno opcional.
- HabitacionDoble: habitación para dos personas, con tipo de camas y balcón opcional.
- Suite: habitación para cuatro personas, con servicios y un cargo adicional.
- DetalleEstadia: guarda las fechas y la cantidad de huéspedes y calcula las noches.
- Reserva: relaciona al huésped con la habitación y crea su detalle de estadía.
- Huesped: clase pendiente de incorporación para representar al huésped.

## Conceptos de programación utilizados

- Abstracción mediante la clase Habitacion.
- Herencia en los tres tipos de habitaciones.
- Encapsulación de atributos mediante propiedades.
- Polimorfismo al recorrer una lista de habitaciones y llamar
  a los mismos métodos.
- Asociación de Reserva con un huésped y una habitación.
- Composición: cada reserva crea su propio DetalleEstadia.

## Archivos del proyecto

- habitacion.py
- habitacion_individual.py
- habitacion_doble.py
- suite.py
- detalle_estadia.py
- reserva.py
- main.py
- README.md
- diagrama_uml.md
- decisiones_diseno.md

Los archivos huesped.py y excepciones.py están pendientes
de incorporación.

## Requisitos

- Python 3.13, versión utilizada durante el desarrollo.
- No requiere instalar bibliotecas externas.

## Cómo ejecutar

Abre una terminal ubicada en la carpeta del proyecto y ejecuta:

```bash
python main.py
```

El programa principal actual muestra los tres tipos de habitaciones
y calcula sus precios para una estadía de dos noches.

## Resultados de la demostración actual

- Habitación individual con desayuno: 190.00 por dos noches.
- Habitación doble con balcón: 280.00 por dos noches.
- Suite con cargo adicional: 500.00 por dos noches.

Los cargos y las capacidades son reglas de la demostración académica
y no representan las tarifas de un hotel real.

## Verificaciones realizadas

Se ejecutó el programa principal y se revisaron los cálculos
de los tres tipos de habitaciones.

También se comprobó que:

- DetalleEstadia calcula correctamente la cantidad de noches.
- Se rechazan fechas de salida iguales o anteriores a la entrada.
- Se rechaza una cantidad de huéspedes superior a la capacidad.
- Una reserva confirmada impide confirmar otra de la misma habitación
  con fechas que se cruzan.
- Se permiten reservas consecutivas cuando una comienza el día
  en que termina la anterior.
- Las reservas de habitaciones diferentes no se bloquean entre sí.
- Las reservas pendientes no bloquean la disponibilidad.
- Cada reserva crea un detalle de estadía independiente.
- Consultar y modificar la copia de los servicios de una suite
  no modifica su lista interna.

En la revisión de una copia del repositorio se realizaron
32 comprobaciones satisfactorias con apoyo de ChatGPT.
Para probar Reserva se utilizó un objeto temporal con un nombre,
porque la clase Huesped todavía no está incorporada.
Estas pruebas deberán repetirse con la clase definitiva.

Actualmente los errores de fechas, capacidad y disponibilidad
utilizan ValueError. La captura de las tres excepciones personalizadas
en main.py sigue pendiente.

## Documentación

- [Diagrama UML](diagrama_uml.md): muestra las clases y sus relaciones.
- [Decisiones de diseño](decisiones_diseno.md): explica la estructura,
  las decisiones adoptadas, las pruebas y el trabajo pendiente.

Ambos documentos son versiones provisionales y se actualizarán
después de la integración final.

## Estado actual y trabajo pendiente

El repositorio incluye las habitaciones, DetalleEstadia, Reserva,
la demostración inicial, el diagrama UML y el borrador del documento
de decisiones de diseño.

Para completar el proyecto falta:

- Incorporar la clase Huesped.
- Incorporar FechasInvalidasError, CapacidadExcedidaError
  y HabitacionNoDisponibleError.
- Validar que Reserva reciba un objeto Huesped válido.
- Sustituir los ValueError correspondientes por las excepciones
  personalizadas.
- Ampliar main.py con al menos ocho objetos y demostraciones
  de reservas válidas.
- Capturar las tres excepciones en el programa principal,
  mostrar mensajes claros y continuar la ejecución.
- Repetir las pruebas con todos los componentes integrados.
- Actualizar el UML y el documento de decisiones de diseño.
- Verificar que cada integrante tenga un commit de su aporte real.

El proyecto todavía no está listo para la entrega final.

## Uso de inteligencia artificial

Se utilizó ChatGPT como herramienta de apoyo para explicar conceptos,
orientar la estructura del proyecto y ayudar con fragmentos de código,
documentación y comprobaciones.

Los integrantes son responsables de revisar, comprender y validar
la versión final del proyecto.
