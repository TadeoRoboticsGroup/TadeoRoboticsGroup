"""
modo
   sensores: y
   control rc: z
laser: soltar l
   x izquierda j
   x derecha k
   y arriba    h
   y abajo     i
disparos: acorde al numumero

direccion: soltar: g
avanzar c
retroceder f
derecha e
izquierda d
stop g
"""


import utime
from machine import Pin, UART, PWM

#Comunicacion Serial  UART_PORT_1  GP4_TX  GP5_TX
uart = UART(1,9600)

#Entradas digitales sensores
sensor1 = Pin(0, Pin.IN, Pin.PULL_DOWN) #izquierda
sensor2 = Pin(2, Pin.IN, Pin.PULL_DOWN) #derecha

#Salidas pines puente H
M1A = Pin(28)   #motorDerechaGiroAdelnate
M1B = Pin(27)   #motorDerechaGiroAtras
M2A = Pin(15)   #motorIzquierdaGiroAdelante
M2B = Pin(14)   #motorIzquierdaGiroAtras

pwmDerechadelante       = PWM(M1A)  #PWM_motorDerechaGiroAdelnate
pwmDerechatras          = PWM(M1B)  #PWM_motorDerechaGiroAtras
pwmIzquierdaAdelante    = PWM(M2A)  #PWM_motorIzquierdaGiroAdelante
pwmIzquierdAtras        = PWM(M2B)  #PWM_motorIzquierdaGiroAtras

inMin = 0           #minimoVelocidad 0 %
inMax = 100         #maximoVelocidad 100 %
outMin = 0          #minimoVelocidad 0 PWM
outMax = 65535      #maximoVelocidad 65535 PWM

#modo de contro
modo=True #Control RC

#Funcion map para conversion Porcentaje a PWM
def Map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#Funcion que controla los puente H
def move(m1a, m1b, m2a, m2b):
    pwmDerechadelante.duty_u16(m1a)
    pwmDerechatras.duty_u16(m1b)
    pwmIzquierdaAdelante.duty_u16(m2a)
    pwmIzquierdAtras.duty_u16(m2b)

#Funciones para el contro de giro y navegacion
def adelante(vel):
    move(vel , 0, vel , 0)
    
def atras(vel):
    move(0, vel , 0, vel )
    
def derecha(vel):
    move(0, vel , vel , 0)
    
def izquierda(vel):
    move(vel , 0, 0, vel )
    
def giroderecha(vel):
    move(0 , 0, 0, vel )
    
def giroizquierda(vel):
    move(vel , 0, 0, 0 )
    
def detenerme(vel):
    move(0, 0, 0, 0)


def autonomo():
    print("autnomo")
    s1_estado = sensor1.value() #izquierda
    s2_estado = sensor2.value() #derecha  
    #Validaciones modo autonomo
    if modo == False and s1_estado==1 and s2_estado==0:
        print("S1")
        velocidad = Map(45, inMin, inMax, outMin, outMax)
        derecha(velocidad)
        utime.sleep(0.05)
                        
    if modo == False and s1_estado==0 and s2_estado==1:
        print("S2")
        velocidad = Map(45, inMin, inMax, outMin, outMax)
        izquierda(velocidad)
        utime.sleep(0.05)
                        
    if modo == False and s1_estado==1 and s2_estado==1:
        print("S4")
        velocidad = Map(13, inMin, inMax, outMin, outMax)
        adelante(velocidad)
        utime.sleep(0.01)

    if modo == False and s1_estado==0 and s2_estado==0:
        print("S4")
        velocidad = Map(13, inMin, inMax, outMin, outMax)
        adelante(velocidad)
        utime.sleep(0.01)






#Bucle infinito
while True:
    
    #lectura del señal Bluetooth 
    if uart.any():
        command = uart.readline()
        print("Esto llega del celular", command)
        
        #Adecuamos el modo de acuerdo a la entrada desde la interfaz    
        if command == b'z':
            modo = True #Cambiando a modo rc
            print("Modo actual ",modo)
            print("parar")
            velocidad = Map(0, inMin, inMax, outMin, outMax)
            print("PWM", velocidad)
            detenerme(velocidad)
            utime.sleep(0.01)
            
        elif command == b'y':
            modo = False#Cambiando a modo sensores
            print("Modo actual ",modo)
            print("parar")
            velocidad = Map(0, inMin, inMax, outMin, outMax)
            print("PWM", velocidad)
            detenerme(velocidad)
            utime.sleep(0.01)
     
        #Validaciones de control remoto
        if modo == True and command == b'c':
            print("adelante")
            velocidad = Map(50, inMin, inMax, outMin, outMax)
            adelante(velocidad)
            utime.sleep(0.1)

        if modo == True and command == b'f':
            print("atras")
            velocidad = Map(50, inMin, inMax, outMin, outMax)
            atras(velocidad)
            utime.sleep(0.1)
            
        if modo == True and command == b'e':
            print("derecha")
            velocidad = Map(40, inMin, inMax, outMin, outMax)
            izquierda(velocidad)
            utime.sleep(0.1)

        if modo == True and command == b'd':
            print("izquierda")
            velocidad = Map(40, inMin, inMax, outMin, outMax)
            derecha(velocidad)
            utime.sleep(0.1)
            
        if modo == True and command == b'g':
            print("parar")
            velocidad = Map(0, inMin, inMax, outMin, outMax)
            print("PWM", velocidad)
            detenerme(velocidad)
            utime.sleep(0.1)
            
    if modo == False:
        autonomo()
        utime.sleep(0.05)

        



        utime.sleep(0.01)