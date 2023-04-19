import machine
import utime

uart = machine.UART(0, baudrate=9600) #Hace referencia a la inicialización de la comunicación serial via Bluetooth con el protocolo UART
uart.init(9600, bits=8, parity=None, stop=1)

while True: # bucle infinito
    data = uart.readline() # Leer la entrada desde uart
    if data:
        print(data.decode('utf-8')) # Imprimir el dato leído, presto para futuras diferenciaciones de funciones
    utime.sleep_ms(10)