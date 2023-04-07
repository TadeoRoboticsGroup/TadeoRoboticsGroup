.. _python:

Python Básico
#############

Este documento es una introducción básica a Python. Cubriremos varios temas fundamentales, incluyendo variables, comentarios, operadores lógicos, loops (for, while), tuplas, listas y más.

Variables
*********

En Python, las variables se definen con un nombre y un valor. Los nombres de variables deben comenzar con una letra y pueden contener letras, números y guiones bajos. El valor de una variable se puede cambiar en cualquier momento.

Ejemplo de variables:

.. code:: python

   x = 5
   y = "Hola, mundo!"


Comentarios
***********

Los comentarios son una forma de agregar notas explicativas al código de Python. Los comentarios comienzan con el símbolo "#" y se ignoran por completo por el intérprete de Python.

Ejemplo de comentarios:

.. code:: python

    # Esto es un comentario en Python
    print("Hola, mundo!") # Esto también es un comentario

.. code:: python

    """Esto es
    un comentario 
    de multiples 
    líneas"""

Operadores lógicos
******************

Los operadores lógicos se utilizan para realizar operaciones booleanas en Python. Los operadores más comunes son "and", "or" y "not".

Ejemplo de operadores lógicos:

.. code:: python

   x = 5
   y = 10
   if x == 5 and y == 10:
       print("Ambas condiciones son verdaderas")
   if x == 5 or y == 20:
       print("Al menos una condición es verdadera")
   if not(x == 5 and y == 10):
       print("La condición es falsa")

Loops (for, while)
******************

Los loops for se utilizan para iterar sobre una secuencia de elementos en Python. Los loops while se utilizan para repetir una sección de código mientras se cumple una condición determinada.

Ejemplo de loops:

.. code:: python

   # Loop for
   for i in range(5):
       print(i)

   # Loop while
   x = 0
   while x < 5:
       print(x)
       x += 1

Case
****

En Python, se utiliza el condicional "if-elif-else" para implementar el equivalente a un "switch-case" en otros lenguajes de programación.

Ejemplo de case:

.. code:: python

   x = 5
   if x == 1:
       print("El valor es 1")
   elif x == 2:
       print("El valor es 2")
   elif x == 3:
       print("El valor es 3")
   else:
       print("El valor no es ni 1, ni 2, ni 3")



Listas
******

Las listas son una estructura de datos en Python que contienen una secuencia ordenada de elementos. A diferencia de las tuplas, las listas son mutables, lo que significa que se pueden agregar, eliminar o modificar elementos después

Ejemplo de listas:

Crear una lista

.. code:: python
    
    lista = ["manzana", "banana", "cereza"]
    print(lista)

Acceder a un elemento de la lista

.. code:: python
    
    print(lista[1])

Cambiar un elemento de la lista

.. code:: python
    
    lista[1] = "kiwi"
    print(lista)

Recorrer una lista con un ciclo for

.. code:: python

    for fruta in lista:
        print(fruta)

Verificar si un elemento está en la lista

.. code:: python
    
    if "banana" in lista:
        print("Sí, banana está en la lista")

Obtener la longitud de la lista

.. code:: python
    
    print(len(lista))

Agregar un elemento a la lista

.. code:: python
    
    lista.append("naranja")
    print(lista)

Eliminar un elemento de la lista

.. code:: python
    
    lista.remove("cereza")
    print(lista)

Ordenar la lista
.. code:: python
    
    lista.sort()
    print(lista)

Invertir el orden de la lista

.. code:: python
    
    lista.reverse()
    print(lista)


Tuplas
******
Las tuplas son similares a las listas, pero no se pueden modificar una vez creadas. Las tuplas se crean utilizando paréntesis en lugar de corchetes.

Ejemplo de tuplas:

Crear una tupla

.. code:: python

    tupla = ("manzana", "banana", "cereza")

Imprimir el valor de una tupla

.. code:: python

    print(tupla)

Acceder a un elemento de la tupla

.. code:: python

    print(tupla[1]) # Imprime "banana"

Las tuplas no se pueden modificar
Esto dará un error: tupla[1] = "kiwi"


Diccionarios
************
Los diccionarios son una colección no ordenada de elementos que se almacenan en pares de clave-valor. Cada clave en un diccionario debe ser única.

Ejemplo de diccionarios:

.. code:: python

    Crear un diccionario
    diccionario = {
        "marca": "Ford",
        "modelo": "Mustang",
        "año": 1964
    }

Imprimir el valor de un diccionario

.. code:: python

    print(diccionario)

Acceder a un valor en el diccionario

.. code:: python

    print(diccionario["modelo"]) # Imprime "Mustang"

Cambiar el valor de un elemento en el diccionario

.. code:: python

    diccionario["año"] = 2022
    print(diccionario) # Imprime {"marca": "Ford", "modelo": "Mustang", "año": 2022}


Funciones
*********

Las funciones son bloques de código que se pueden llamar varias veces desde diferentes partes de un programa. Las funciones pueden tomar argumentos y devolver valores.

Ejemplo de funciones:

Definir una función

.. code:: python

    def saludo(nombre):
        print("Hola, " + nombre)

Llamar a la función

.. code:: python

    saludo("Juan") # Imprime "Hola, Juan"

La función puede devolver un valor

.. code:: python

    def suma(num1, num2):
        return num1 + num2

    resultado = suma(3, 5)
    print(resultado) # Imprime 8

Módulos
*******

Los módulos son archivos que contienen funciones y variables relacionadas que se pueden importar y usar en otros programas.

Ejemplo de módulos:

    Importar un módulo
    
.. code:: python

    from math import sqrt

Usar una función del módulo

.. code:: python

    raiz_cuadrada = math.sqrt(25)
    print(raiz_cuadrada)

También es posible importar todas las funciones de un módulo con el uso del carácter "*". Sin embargo, es recomendable no hacerlo, ya que esto puede dificultar la lectura del código y llevar a conflictos de nombres.

Importar todas las funciones de un módulo

.. code:: python

    from math import *

Uso de la función importada

.. code:: python

    seno = sin(45)
    print(seno)

Usar la función importada

.. code:: python

    num_aleatorio = randint(1, 10)

Excepciones
***********

Las excepciones son errores que se producen durante la ejecución de un programa. Pueden ser manejados mediante el uso de bloques try-except.


Manejo de excepcione

.. code:: python

    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

Manejo de excepciones con else

.. code:: python

    try:
        resultado = 10 / 2
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    else:
        print("La división fue exitosa")

Manejo de excepciones con finally

.. code:: python

    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("La ejecución se ha completado")

Conclusiones
Python es un lenguaje de programación popular debido a su facilidad de uso y su amplia gama de aplicaciones. 
En este documento se han cubierto algunos de los conceptos básicos de Python, como variables, comentarios, 
operadores lógicos, bucles, listas, tuplas, diccionarios, funciones, módulos y excepciones. Con práctica y 
experiencia, podrás utilizar Python para crear programas útiles y eficientes.



