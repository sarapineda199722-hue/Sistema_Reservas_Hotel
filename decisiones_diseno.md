# Universidad de Manizales

## Facultad de Ciencias e Ingenierías
## Ingeniería Analítica de Datos

# Documento de Decisiones de Diseño
## Sistema de Reservas de Hotel

**Asignatura:** Programación I  
**Actividad:** Actividad Colaborativa N.º 3 — Proyecto Final  
**Elaborado por:** Sara Liliana Pineda Castro  
**Fecha:** Octubre de 2026  

---

## 1. Introducción

El proyecto aborda la organización de reservas de un hotel que
ofrece habitaciones individuales, dobles y suites. El problema
consiste en calcular el valor de las estadías y evitar reservas
con fechas inválidas, cantidades de huéspedes superiores a la
capacidad o cruces con reservas confirmadas.

El propósito es aplicar los conceptos de programación orientada
a objetos mediante una solución en Python. El sistema funciona
en consola y mantiene los objetos en memoria durante la ejecución.

## 2. Descripción general de la solución

La solución separa las responsabilidades entre habitaciones,
huéspedes, reservas y detalles de estadía.

Las habitaciones conocen sus características y calculan su precio.
Los huéspedes contienen la información de identificación.
Los detalles de estadía administran las fechas y calculan las noches.
Las reservas relacionan estos objetos y comprueban la disponibilidad
antes de confirmarse.

El proyecto utiliza seis clases concretas, una clase abstracta
y tres excepciones personalizadas.

## 3. Organización y responsabilidades de las clases

### 3.1. Habitacion

Habitacion es la clase abstracta del sistema. Contiene el número,
la capacidad y la tarifa por noche, además del método validar_noches.

Define los métodos abstractos calcular_precio y describir.
No debe instanciarse porque representa un concepto general:
para calcular un precio y obtener una descripción se necesita
un tipo concreto de habitación.

### 3.2. Tipos de habitaciones

HabitacionIndividual representa una habitación para una persona.
Su atributo incluye_desayuno determina si se agrega un cargo
de 15 por noche a la tarifa base.

HabitacionDoble representa una habitación para dos personas.
Guarda el tipo de camas y el atributo tiene_balcon.
Cuando tiene balcón, agrega un cargo de 20 por noche.

Suite representa una habitación para cuatro personas.
Guarda una lista de servicios y un cargo_extra_por_noche.
Este cargo se suma a la tarifa base antes de multiplicar
por la cantidad de noches.

Los cargos y las capacidades son reglas elegidas para
la demostración académica.

### 3.3. Huesped

Huesped almacena el nombre y la identificación de quien realiza
la reserva. Su constructor rechaza textos vacíos y su método
describir presenta los datos de la persona.

### 3.4. DetalleEstadia

DetalleEstadia contiene la fecha de entrada, la fecha de salida
y la cantidad de huéspedes.

Su constructor comprueba que las fechas sean objetos date,
que la salida sea posterior a la entrada y que la cantidad
de huéspedes sea un entero positivo.

El método calcular_noches obtiene la diferencia entre las fechas.
El método describir presenta los datos de la estadía.

### 3.5. Reserva

Reserva guarda un código, un huésped, una habitación,
un detalle de estadía y un estado de confirmación.

Su constructor valida los objetos recibidos y comprueba
que la cantidad de huéspedes no supere la capacidad.

calcular_total solicita a la habitación el precio correspondiente
a las noches de la estadía. confirmar revisa los cruces con otras
reservas confirmadas. describir presenta la información completa.

## 4. Abstracción, herencia y especialización

Se eligió Habitacion como clase abstracta porque los tres tipos
comparten datos, pero tienen características y reglas de precio
diferentes.

HabitacionIndividual, HabitacionDoble y Suite heredan de Habitacion.
La relación representa “es un”: una suite es una habitación,
al igual que una habitación individual o doble.

Las clases hijas comparten número, capacidad, tarifa por noche
y el método validar_noches. Sus constructores utilizan super()
para inicializar los atributos comunes.

Los atributos particulares permiten especializar cada clase:
desayuno en la individual, camas y balcón en la doble,
y servicios y cargo adicional en la suite.

Reserva y Huesped no heredan de Habitacion porque representan
entidades con responsabilidades diferentes.

## 5. Encapsulamiento

Los atributos de las entidades se almacenan con doble guion bajo
y se consultan mediante propiedades.

Las validaciones de los constructores permiten controlar
los datos con los que se crean los objetos. Las propiedades
no incluyen setters, por lo que no permiten asignar directamente
nuevos valores por esa vía.

Suite devuelve una copia de su lista de servicios. De esta manera,
modificar la lista obtenida no modifica directamente la lista interna.

El doble guion bajo ayuda a evitar accesos accidentales,
pero no constituye una barrera de seguridad absoluta en Python.

## 6. Sobreescritura y polimorfismo

Las tres clases hijas sobrescriben calcular_precio y describir.

calcular_precio mantiene el mismo nombre, pero aplica el cargo
particular de cada habitación. describir presenta los atributos
propios de cada tipo.

En main.py se crea una única lista que contiene una habitación
individual, una doble y una suite. Un único ciclo llama
a describir y calcular_precio sobre todos los objetos.

No se utilizan condicionales para seleccionar un método
según el tipo de habitación. Cada objeto responde con
la implementación de su clase.

Para dos noches, los resultados son 190.00 para la individual
con desayuno, 280.00 para la doble con balcón y 500.00
para la suite con cargo adicional.

## 7. Asociaciones y composición

Reserva mantiene dos asociaciones: una con Huesped
y otra con Habitacion. Estos objetos tienen identidad propia,
pueden existir sin una reserva y participar en distintas reservas.

La relación con DetalleEstadia se implementó como composición.
El constructor de Reserva crea un detalle exclusivo a partir
de las fechas y la cantidad de huéspedes.

Ese detalle forma parte de la estructura de la reserva
y no se comparte con otras reservas. La composición permite
separar los cálculos de fechas de las reglas de confirmación.

No se resolvió mediante herencia porque una reserva contiene
un detalle de estadía; no es un detalle de estadía.

En Python es posible conservar una referencia al detalle.
La pertenencia exclusiva corresponde al diseño del sistema,
no a una garantía de eliminación automática del objeto.

## 8. Disponibilidad y confirmación

confirmar recibe la lista de reservas existentes y revisa
las que están confirmadas y corresponden a la misma habitación.

La habitación se identifica por su número, considerado único
dentro del hotel.

Existe un cruce cuando la entrada de una reserva es anterior
a la salida de la otra y su salida es posterior a la entrada
de la otra.

Esta regla permite que una reserva comience el mismo día
en que termina otra. Las reservas pendientes no bloquean
la disponibilidad.

La comprobación requiere recibir la lista completa
de reservas existentes. main.py mantiene esa lista y agrega
las reservas después de confirmarlas correctamente.

## 9. Manejo de excepciones

Se definieron tres excepciones personalizadas que heredan
de Exception.

FechasInvalidasError se lanza desde el constructor de
DetalleEstadia cuando la salida es igual o anterior a la entrada.

CapacidadExcedidaError se lanza desde el constructor de Reserva
cuando la cantidad de huéspedes supera la capacidad.

HabitacionNoDisponibleError se lanza desde confirmar
cuando existe una reserva confirmada de la misma habitación
con fechas cruzadas.

main.py provoca y captura cada situación mediante try y except.
Después muestra un mensaje claro y continúa ejecutándose.

Las validaciones generales, como nombres vacíos o cantidades
no positivas, conservan ValueError.

## 10. Evolución de las decisiones de diseño

La primera versión implementó los tipos de habitaciones
y una demostración de precios.

Después se incorporaron DetalleEstadia y Reserva para separar
la información de la estadía de la confirmación.

Inicialmente las situaciones anormales del dominio utilizaban
ValueError. Durante la integración se sustituyeron por las tres
excepciones personalizadas para distinguir los errores de fechas,
capacidad y disponibilidad.

También se incorporó Huesped y se agregó la validación de su tipo
en Reserva. Esto evita aceptar un objeto que no corresponda
a la entidad esperada.

main.py se amplió para demostrar reservas válidas, errores
controlados y una reserva consecutiva. Finalmente se actualizaron
el README y el UML para reflejar las clases implementadas.

## 11. Herramientas utilizadas

Se utilizó Visual Studio Code para editar los archivos y una
terminal con Python 3.13 para ejecutar la demostración.

El diagrama de clases se escribió con Mermaid en un archivo
Markdown. Git y GitHub se utilizan para administrar las versiones
y alojar el repositorio del proyecto.

ChatGPT se utilizó como apoyo para explicar conceptos,
proponer y elaborar fragmentos de código, revisar la estructura
y preparar la documentación.

Las propuestas se ajustaron durante la integración:
se reemplazó el uso provisional de ValueError en los errores
del dominio, se incorporó la validación de Huesped y se amplió
la demostración inicial para incluir reservas y excepciones.

La verificación se realizó ejecutando el programa y comparando
sus resultados con las reglas definidas. También se revisó
que las clases, los métodos y las relaciones correspondieran
con los conceptos solicitados en la actividad.

## 12. Verificación del funcionamiento

Se ejecutó python main.py y se observaron los siguientes resultados:

- Los precios por dos noches fueron 190.00, 280.00 y 500.00.
- Se mostraron los datos de tres huéspedes.
- Se confirmaron tres reservas iniciales en habitaciones diferentes.
- Se capturó el error de fechas inválidas.
- Se capturó el error de capacidad excedida.
- Se capturó el error de habitación no disponible.
- El programa continuó después de cada excepción.
- Se confirmó una reserva consecutiva sin cruce de fechas.
- El total final fue de cuatro reservas confirmadas.
- La ejecución llegó a FIN DE LA DEMOSTRACIÓN.

La demostración crea más de ocho objetos: tres habitaciones,
tres huéspedes y cuatro reservas válidas, además de sus detalles
de estadía y la reserva cuya confirmación se rechaza.

La revisión del código permite identificar una clase abstracta,
seis clases concretas, tres clases hijas con dos métodos
sobrescritos, una colección heterogénea, dos asociaciones,
una composición y tres excepciones personalizadas.

La ejecución realizada verifica los casos incluidos en main.py;
no constituye una prueba de todas las entradas posibles.

## 13. Conclusiones

El sistema distribuye las responsabilidades entre habitaciones,
huéspedes, reservas y detalles de estadía.

La herencia permite compartir atributos y especializar
los comportamientos. El polimorfismo permite utilizar los tres
tipos de habitaciones mediante las mismas llamadas.

Una dificultad de la integración fue conectar las clases
de reservas con los huéspedes y sustituir los errores generales
por excepciones del dominio. Estas modificaciones permitieron
demostrar los casos excepcionales sin detener el programa.

El proceso permitió aplicar la diferencia entre herencia,
asociación y composición, así como comprobar la importancia
de mantener la documentación de acuerdo con el código.

El alcance es una demostración en consola con datos en memoria.
Una ampliación futura podría incorporar almacenamiento permanente
y una interfaz para registrar reservas.

## 14. Referencias

Universidad de Manizales. Actividad colaborativa N.º 3:
Proyecto Final. Material de la asignatura Programación I.

Python Software Foundation. Documentación de Python 3.13.
https://docs.python.org/es/3.13/

OpenAI. ChatGPT. Herramienta de apoyo para el desarrollo
y la documentación.
https://chatgpt.com/