.. _raspberrypico:

Raspberry Pico
==============

Ejemplos de Raspberry Pi Pico en MicroPython
____________________________________________

En este documento se presentan algunos ejemplos de cómo utilizar la placa Raspberry Pi Pico con MicroPython.


Salida y entradas de señales analógicas y digitales
___________________________________________________

ejemplo 1: encender un led
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este ejemplo describe cómo encender un LED que parpadea cada segundo utilizando una placa de desarrollo con 
MicroPython y el siguiente circuito conectado al pin 20:

 .. figure:: ../img/circuitos/led_RPi.PNG
  :alt: RPi_pico
  :height: 200
  :align: center

Para este ejemplo, es necesario conectar el cátodo del LED al pin 20 de la placa y el ánodo del LED a tierra.
Una vez que se ha establecido la conexión, se puede utilizar el siguiente código para hacer parpadear el LED:

.. code:: python

   from machine import Pin
   import utime

   led = Pin(20, Pin.OUT)

   while True:
       led.toggle()
       utime.sleep(1)

encuentra la simulación `aquí. <https://wokwi.com/projects/362662447039866881>`__



ejemplo 2: lectura de boton
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Este ejemplo describe cómo leer el estado de un botón utilizando una placa de desarrollo con MicroPython y 
el siguiente circuito conectado al pin 18:

 .. figure:: ../img/circuitos/boton_RPi.PNG
  :alt: RPi_pico
  :height: 200
  :align: center

Para este ejemplo, es necesario conectar un extremo del botón al pin 18 de la placa y el otro extremo del
botón a tierra. Una vez que se ha establecido la conexión, se puede utilizar el siguiente código para leer 
el estado del botón:

.. code:: python

   import machine
   import utime

   button = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)

   while True:
      print(button.value())
      utime.sleep(1)

      if button.value() == 0:
         print("El botón está presionado")
         
      else:
         print("El botón está suelto")

encuentra la simulación `aquí. <https://wokwi.com/projects/362665684610599937>`__



ejemplo 3: lectura de una señal anloga ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para leer el valor de un sensor analógico conectado a la placa Pico en el pin 26 como se ve en el circuito:

 .. figure:: ../img/circuitos/analog_RPi.PNG
  :alt: RPi_pico
  :height: 200
  :align: center

Para este ejemplo, donde tenemos conectado un potenciómetro, es necesario conectar los extremos
al ánodo y cátodo respectivamente, y el centro del potenciómetro a una entrada ADC de la placa,
que en este caso es el 26. Finalmente, se debe utilizar el siguiente código.

.. code:: python

   import machine
   import utime

   sensor = machine.ADC(26)

   while True:
      valor = sensor.read_u16()
      print("valor: ", valor)
      utime.sleep_ms(200)

encuentra la simulación `aquí. <https://wokwi.com/projects/362929326950329345>`__


Señales PWM
___________

Para el control de una señal PWM vamos necesitamos conectar un led con una resistencia al pin 18 de la placa como en el siguiente circuito:

 .. figure:: ../img/circuitos/pwm_RPi.PNG
  :alt: RPi_pico
  :height: 200
  :align: center

despues podemos varia la salida de coltaje de la placa utilizando el siguiente código:

.. code:: python

   import machine
   import time

   led_pin = machine.Pin(18)
   led_pwm = machine.PWM(led_pin)

   while True:
      time.sleep(2)
      for duty_cycle in range(0, 65535, 100):
         led_pwm.duty_u16(duty_cycle)
         print("valor:", duty_cycle)
         time.sleep(0.007)
      time.sleep(2)
      for duty_cycle in range(65535, 0, -100):
         led_pwm.duty_u16(duty_cycle)
         print("valor:", duty_cycle)
         time.sleep(0.007)

encuentra la simulación `aquí. <https://wokwi.com/projects/362930680085257217>`__


Controlar un servo motor
________________________

Para controlar un servo motor conectado a la placa Pico en el pin 22 para controlar su posición mediante MicroPython.

 .. figure:: ../img/circuitos/servo_RPi.PNG
  :alt: RPi_pico
  :height: 200
  :align: center

El circuito consiste en conectar la señal del servomotor al pin 22 de la placa, el pin positivo al pin de 5V y el pin 
negativo al pin de tierra. El código necesario para establecer la posición del servomotor en un ángulo específico es el siguiente:

.. code:: python

   import machine
   import utime

   servo_pin = machine.Pin(22, machine.Pin.OUT)
   servo_pwm = machine.PWM(servo_pin, freq=50)

   def set_servo_angle(angle):
      duty = int((angle / 180) * 65000) + 2500
      servo_pwm.duty_u16(duty)

   while True:
      for angle in range(0, 181, 10):
         set_servo_angle(angle)
         utime.sleep_ms(100)

encuentra la simulación `aquí. <https://wokwi.com/projects/362939249855076353>`__


.. Conectar una pantalla 16x2 con módulo I2C
******************************************

.. Para conectar una pantalla 16x2 con módulo I2C a la placa Pico, puedes utilizar el siguiente código:

..  code:: python

..   import machine
   import utime
   from lcd_api import LcdApi
   from pico_i2c_lcd import I2cLcd
   
..   i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
   lcd_api = LcdApi(16, 2)
   lcd = I2cLcd(i2c, 0x27, lcd_api)
   
..   lcd.putstr("Hola, mundo!")
   utime.sleep(2)
   lcd.clear()
   lcd.putstr("Raspberry Pi Pico")


Conclusión
**********

Estos son solo algunos ejemplos de cómo utilizar la placa Raspberry Pi Pico con MicroPython. Esperamos que esta documentación te haya 
sido útil y que puedas utilizarla como base para crear tus propios proyectos. Si tienes alguna duda o consulta, no dudes en consultarlo 
en la comunidad o foro correspondiente. ¡Que tengas éxito en tus proyectos!