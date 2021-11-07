#El programa genera una secuencia de led controlada por un boton
#librerias
from machine import Pin
from time import sleep_ms

#Definiendo pines
led = [Pin(0,Pin.OUT),Pin(1,Pin.OUT),Pin(2,Pin.OUT),Pin(3,Pin.OUT)]
boton = Pin(4, Pin.IN,Pin.PULL_UP)

desplazamiento = 0

def inter (pin):
    sleep_ms(30)
    if boton.value()==0:
        boton.irq(handler=None)#asignacion de funcion vacia a interrupcion
        print("interrupt")
        global desplazamiento
        desplazamiento+=1
        if desplazamiento == 4:
            desplazamiento=0
        for i in range(4):
            led[i].off()
        led[desplazamiento].on()
        boton.irq(handler=inter)#asignacion de funcion original a la interrupcion
       
boton.irq(trigger=Pin.IRQ_FALLING, handler=inter)