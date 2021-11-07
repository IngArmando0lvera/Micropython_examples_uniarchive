
'''   Estructura de interrupcion


boton=Pin(1,Pin.OUT,Pin.Pull_UP)

def funcion_a_realizar(pin):
    codigo a ejecutar
    al detectar el cambio fisico


boton.irq(trigger=Pin.IRQ_RISING, handler=boton_inteerupt)
#            ^                             ^
#       Disparador                     Funcion a ejecutar


#     *INTERRUPT REQUEST*
#IRQ_RISING     ->FLANCO DE SUBIDA
#IRQ_FALLING    ->FLANCO DE BAJADA


'''
#librerias
from machine import Pin
from time import sleep_ms

#definicion de pines
boton=Pin(4,Pin.IN,Pin.PULL_UP)
led=Pin(1,Pin.OUT)


def interrupcion (pin):
    boton.irq(handler=None)#Desactiva funcion a ejecutar en interrupcion
    if boton.value()==0:
        led.on()
    else:
        led.off()
    boton.irq(handler=interrupcion)#vuelve a asignar funcion a interrupcion para el futuro
    
boton.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion)









