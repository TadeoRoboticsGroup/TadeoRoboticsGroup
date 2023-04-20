from machine import Pin, UART
import utime
#Prueba por Daniel Melo 19/04
# Configurar UART
uart = UART(0, 9600) #Caracterización del UART 
uart.init(9600, bits=8, parity=None, stop=1)

# Configurar pines de los motores
motor_left_1 = Pin(0, Pin.OUT)
motor_left_2 = Pin(1, Pin.OUT)
motor_right_1 = Pin(2, Pin.OUT)
motor_right_2 = Pin(3, Pin.OUT)

# Función para mover hacia adelante
def move_forward():
    motor_left_1.value(1)
    motor_left_2.value(0)
    motor_right_1.value(1)
    motor_right_2.value(0)

# Función para mover hacia atrás
def move_backward():
    motor_left_1.value(0)
    motor_left_2.value(1)
    motor_right_1.value(0)
    motor_right_2.value(1)

# Función para detenerse
def stop():
    motor_left_1.value(0)
    motor_left_2.value(0)
    motor_right_1.value(0)
    motor_right_2.value(0)

# Bucle principal
while True:
    # Leer los datos del módulo Bluetooth
    data = uart.readline()

    # Interpretar los datos recibidos
    if data:
        command = data.decode().strip()

        # Mover hacia adelante
        if command == "F":
            move_forward()

        # Mover hacia atrás
        elif command == "B":
            move_backward()

        # Detenerse
        elif command == "S":
            stop()

    # Pequeña pausa
    utime.sleep(0.1)