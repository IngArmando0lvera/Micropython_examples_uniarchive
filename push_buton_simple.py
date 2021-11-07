#librerias
from machine import Pin
from time import sleep_ms

#declaracion de pines
boton = Pin(4, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

#declaracion de funcion principal
def main():
    while 1:
        sleep_ms(10)
        if boton.value() == 0:
            led.on()
            print("boton presionado")
        else:
            led.off()
            print("boton pull up ")

main()