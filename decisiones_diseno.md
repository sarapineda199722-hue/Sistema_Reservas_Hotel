# Documento de decisiones de diseño

## Sistema de Reservas de Hotel

Actividad Colaborativa N.º 3 — Programación I

Integrantes: Sara Liliana Pineda Castro y Julián Loaiza Botero.

Estado del documento: borrador del diseño y del avance actual.

## Introducción

El proyecto representa un sistema de reservas de hotel mediante
programación orientada a objetos. Su propósito es organizar los datos
de las habitaciones, los huéspedes y las estadías, calcular precios
y evitar reservas que incumplan las reglas del hotel.

El alcance previsto incluye habitaciones individuales, dobles y
suites. El programa funcionará en consola y utilizará objetos
almacenados en memoria, sin base de datos.

## Organización de las clases

La clase abstracta Habitacion reúne el número, la capacidad y la tarifa
por noche. También valida la cantidad de noches y establece los métodos
calcular_precio y describir. No se crean objetos directamente de esta
clase porque el sistema necesita un tipo concreto de habitación.

HabitacionIndividual representa una habitación para una persona.
Su atributo específico indica si incluye desayuno. Cuando se incluye,
el cálculo incorpora un cargo de 15 por noche.

HabitacionDoble representa una habitación para dos personas. Guarda
el tipo de camas y la disponibilidad de balcón. El balcón agrega
un cargo de 20 por noche.

Suite representa una habitación para cuatro personas. Guarda una lista
de servicios y un cargo adicional por noche. El precio incorpora ese
cargo a la tarifa base.

Estas capacidades y cargos son reglas elegidas para la demostración
académica; no representan tarifas de un hotel real.

Huesped tendrá la responsabilidad de guardar el nombre y la
identificación de la persona que realiza una reserva. Su implementación
está pendiente de incorporación.

DetalleEstadia guarda la fecha de entrada, la fecha de salida y la
cantidad de huéspedes. Calcula las noches como la diferencia entre
las fechas y comprueba que la salida sea posterior a la entrada.

Reserva relaciona un huésped con una habitación y crea su detalle
de estadía. Guarda un código y un estado de confirmación, calcula
el total y comprueba los cruces de fechas antes de confirmar.

## Abstracción y herencia

Se eligió Habitacion como clase abstracta porque los tres tipos
comparten datos, pero calculan y describen sus características
de manera diferente.

La herencia corresponde a una relación “es un”: una habitación
individual, una habitación doble y una suite son habitaciones.
Reserva y Huesped tienen responsabilidades diferentes, por lo que
se relacionan con otros objetos mediante asociaciones.

Cada clase hija sobrescribe calcular_precio y describir. Así,
la estructura común permanece en Habitacion y las reglas particulares
se encuentran en la clase que las necesita.

## Encapsulación y validación

Los atributos se guardan con doble guion bajo y se consultan mediante
propiedades. Esto permite controlar el acceso a los datos y evitar
modificaciones directas accidentales. El doble guion bajo no constituye
una barrera de seguridad absoluta en Python.

Los constructores comprueban los datos antes de completar la creación
de los objetos. Por ejemplo, la capacidad debe ser un entero positivo
y la tarifa debe ser mayor que cero.

La propiedad servicios de Suite devuelve una copia de la lista.
Así, modificar la lista recibida no cambia directamente los servicios
guardados dentro del objeto.

## Polimorfismo

El programa principal contiene una lista con objetos
HabitacionIndividual, HabitacionDoble y Suite.

Un único ciclo llama a describir y calcular_precio para cada objeto.
Python ejecuta la implementación correspondiente a cada habitación,
sin que el ciclo tenga que preguntar cuál es su tipo.

En la prueba inicial de dos noches, los resultados esperados son
190 para la habitación individual con desayuno, 280 para la doble
con balcón y 500 para la suite con cargo adicional.

## Asociaciones y composición

Reserva mantiene asociaciones con Huesped y Habitacion. Estos objetos
tienen identidad propia y pueden participar en distintas reservas.

La relación entre Reserva y DetalleEstadia se diseñó como composición.
El constructor de Reserva crea un detalle exclusivo a partir de las
fechas y la cantidad de huéspedes. Ese detalle forma parte de la reserva
y no se comparte entre reservas.

Esta decisión permite separar los cálculos de fechas de las reglas
de confirmación. Aunque Python permite conservar una referencia al
detalle, el diseño del sistema lo considera una parte de su reserva.

## Confirmación y disponibilidad

Antes de confirmar una reserva, se revisan las reservas confirmadas
de la misma habitación. La habitación se identifica por su número,
que se considera único dentro del hotel.

Existe un cruce cuando la entrada de una reserva es anterior a la
salida de la otra y su salida es posterior a la entrada de la otra.

Con esta regla, una reserva puede comenzar el mismo día en que termina
otra. Las reservas pendientes no bloquean la disponibilidad.

La comprobación depende de recibir la lista completa de reservas
existentes. El programa principal deberá mantener y proporcionar
esa lista.

## Excepciones personalizadas previstas

Se prevén tres excepciones del dominio: FechasInvalidasError,
CapacidadExcedidaError y HabitacionNoDisponibleError.

DetalleEstadia lanzará FechasInvalidasError cuando la salida no sea
posterior a la entrada. Reserva lanzará CapacidadExcedidaError cuando
la cantidad de huéspedes supere la capacidad de la habitación.
El método confirmar lanzará HabitacionNoDisponibleError cuando
encuentre una reserva confirmada con fechas que se crucen.

Actualmente estas situaciones utilizan ValueError. La integración
pendiente sustituirá esos errores por las excepciones personalizadas.
Las validaciones generales de datos podrán conservar ValueError.

El programa principal deberá capturar cada excepción, mostrar
un mensaje claro y continuar con las demás demostraciones.

## Evolución de las decisiones

Primero se implementaron los tipos de habitaciones y una prueba
de precios. Después se incorporaron DetalleEstadia y Reserva,
separando los datos de la estadía de la confirmación.

Se decidió crear DetalleEstadia dentro de Reserva para representar
la composición de forma explícita. También se mantuvo el cálculo
del precio en las habitaciones para que Reserva pueda solicitarlo
sin conocer las reglas de cada tipo.

El README y el UML describen el avance actual. Se actualizarán cuando
se incorporen Huesped y las excepciones, y cuando se amplíe main.py.

## Uso de inteligencia artificial

Se utilizó ChatGPT para apoyar la propuesta de clases, generar
fragmentos de código, explicar conceptos y preparar borradores
de documentación.

Durante esta etapa se ajustó la distribución del trabajo para dejar
a Julián la clase Huesped, las excepciones y la revisión del código.
También se dejó explícito en la documentación qué partes siguen
pendientes, evitando presentar el sistema como terminado.

Se mantuvo temporalmente ValueError en las reglas del dominio mientras
se incorpora el archivo de excepciones. Esta decisión deberá revisarse
durante la integración.

Todavía falta registrar los cambios o correcciones que surjan al revisar
las sugerencias de la IA y ejecutar el sistema completo. Los integrantes
deberán comprender y poder explicar todo el código antes de entregar.

## Verificación y trabajo pendiente

Se ejecutó la prueba inicial de habitaciones en Python. La salida
compartida mostró 280 para la habitación doble y 500 para la suite,
además del mensaje de finalización. El diagrama UML se visualizó
correctamente en GitHub.

Aún falta verificar las reservas y sus relaciones, incorporar Huesped
y las excepciones, y ampliar main.py para crear al menos ocho objetos.

La demostración final deberá incluir reservas válidas y los tres casos
de error previstos, comprobando que el programa continúe después
de capturarlos. También conviene comprobar reservas consecutivas
que no se crucen.

Cada integrante deberá registrar su aporte real mediante un commit
en el repositorio.

## Conclusiones provisionales

El diseño distribuye las responsabilidades entre habitaciones,
reservas, huéspedes y detalles de estadía. La herencia permite compartir
datos comunes y el polimorfismo permite utilizar los distintos tipos
de habitaciones desde un mismo ciclo.

La estructura inicial está implementada parcialmente. La conclusión
final sobre su funcionamiento se completará después de integrar
y verificar todos los componentes.

## Referencias

Universidad de Manizales. Actividad colaborativa N.º 3:
Proyecto Final. Material de la asignatura Programación I.

Python Software Foundation. Documentación de Python 3.13:
clases, abc, datetime y excepciones definidas por el usuario.
https://docs.python.org/es/3.13/

OpenAI. ChatGPT. Herramienta de apoyo utilizada durante
la elaboración del código y la documentación.
https://chatgpt.com/
