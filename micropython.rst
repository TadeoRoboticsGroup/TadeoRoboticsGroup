.. _micropython:

MicroPython
===========


En este tutorial se describen los pasos básicos para programar la placa Raspberry Pi Pico utilizando el lenguaje MicroPython y el entorno de desarrollo integrado Thonny.

Requisitos
----------

Antes de comenzar, asegúrate de tener los siguientes elementos:

- Una placa Raspberry Pi Pico
- Un cable micro-USB
- Una computadora con Thonny instalado
- El firmware de MicroPython para Raspberry Pi Pico (disponible en el sitio web oficial de Raspberry Pi)

Conectar la placa
_________________

Conecta la placa Raspberry Pi Pico a tu computadora utilizando el cable micro-USB. 

Configurar Thonny
_________________

1. Abre Thonny en tu computadora.
2. Haz clic en `Tools` en la barra de menú y luego en `Options`.
3. Selecciona `Interpreter` en la barra lateral izquierda.
4. Haz clic en `MicroPython (Raspberry Pi Pico)` en la lista de intérpretes disponibles.
5. Haz clic en `OK` para guardar la configuración.

Escribir y cargar un programa
_____________________________

1. En Thonny, haz clic en `File` en la barra de menú y luego en `New`.
2. Escribe el código de tu programa en el editor de Thonny.
3. Haz clic en `Run` en la barra de herramientas o presiona F5 para ejecutar el programa.
4. Si todo funciona correctamente, podrás ver la salida del programa en la ventana `Shell` de Thonny.

¡Enhorabuena! Ahora ya sabes cómo programar Raspberry Pi Pico con MicroPython y Thonny. Si quieres seguir aprendiendo, te recomendamos que eches un vistazo a la documentación oficial de MicroPython para Raspberry Pi Pico. 





Ejemplos de Raspberry Pi Pico en MicroPython
____________________________________________

En este documento se presentan algunos ejemplos de cómo utilizar la placa Raspberry Pi Pico con MicroPython.


Salida y entradas de señales analógicas y digitales
___________________________________________________

ejemplo 1: encender un led
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para encender y apagar un LED conectado a la placa Pico en el pin 20, puedes utilizar el siguiente código:
 .. figure:: ./img/circuitos/led_RPi.PNG
  :alt: visitors
  :height: 200
  :align: center

.. code:: python

   from machine import Pin
   import utime

   led = Pin(20, Pin.OUT)

   while True:
       led.toggle()
       utime.sleep(1)

Para leer el valor de un sensor analógico conectado a la placa Pico en el pin 26, puedes utilizar el siguiente código:

.. code:: python

   from machine import ADC, Pin

   adc = ADC(Pin(26))
   valor = adc.read_u16()

Encender un LED con PWM
***********************

Para encender un LED conectado a la placa Pico en el pin 25 utilizando la técnica de PWM, puedes utilizar el siguiente código:

.. code:: python

   from machine import Pin, PWM
   import utime

   led = PWM(Pin(25))

   while True:
       for duty_cycle in range(0, 65535, 500):
           led.duty_u16(duty_cycle)
           utime.sleep_ms(10)

Conectar una pantalla 16x2 con módulo I2C
******************************************

Para conectar una pantalla 16x2 con módulo I2C a la placa Pico, puedes utilizar el siguiente código:

.. code:: python

   import machine
   import utime
   from lcd_api import LcdApi
   from pico_i2c_lcd import I2cLcd
   
   i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
   lcd_api = LcdApi(16, 2)
   lcd = I2cLcd(i2c, 0x27, lcd_api)
   
   lcd.putstr("Hola, mundo!")
   utime.sleep(2)
   lcd.clear()
   lcd.putstr("Raspberry Pi Pico")

Controlar un servo motor
*************************

Para controlar un servo motor conectado a la placa Pico en el pin 18, puedes utilizar el siguiente código:

.. code:: python

   import machine
   import utime
   from servo import Servo

   servo = Servo(machine.Pin(18))
   servo.angle(90)
   utime.sleep(2)
   servo.angle(0)



Conclusión
**********

Estos son solo algunos ejemplos de cómo utilizar la placa Raspberry Pi Pico con MicroPython. Esperamos que esta documentación te haya sido útil y que puedas utilizarla como base para crear tus propios proyectos. Si tienes alguna duda o consulta, no dudes en consultarlo en la comunidad o foro correspondiente. ¡Que tengas éxito en tus proyectos!
