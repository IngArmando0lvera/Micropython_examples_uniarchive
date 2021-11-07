'''
17 10 2021
este programa hace una secuencia con 4 leds
'''
#importar libreria

from machine import Pin
from time import sleep_ms


#definicion de puertos
led=[0,1,2,3]
for i in range(4):
    led[i]=Pin(i,Pin.OUT)
#funcion principal

def main():
    while 1:
        for i in range (4):
            led[i].on()
            sleep_ms (50)
            led[i].off()
            sleep_ms (100)
main()