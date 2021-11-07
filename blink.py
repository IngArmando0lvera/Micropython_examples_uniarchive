#librerias 
from machine import Pin, Timer

#Declarando pin para led
led  = Pin(25, Pin.OUT)

#Inicializacion de timer

timer0 = Timer()

#funcion a ejecutar el timer

def repeticion(timer):
    global led #usamos variable global
    led.toggle()#blink de led
    

#definimos la funcion timer0
timer0.init(freq=20, mode=Timer.PERIODIC,callback=repeticion)

