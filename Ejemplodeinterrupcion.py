
'''
Author : Seetha Akella
Purpose : Hardware interrupt - Glow an LED when button is pressed
Language : MicroPython
Hardware : ESP8266
'''
 
'''
A pin object is used to control I/O pins 
(also known as GPIO - general-purpose input/output). 
Pin objects are commonly associated with a physical
pin that can drive an output voltage and read input
voltages. The pin class has methods to set the mode 
of the pin (IN, OUT, etc) and methods to get and set
the digital logic level. For analog control of a pin,
see the ADC class.
'''
from machine import Pin
 
'''
The sleep() function suspends execution of the 
current thread for a given number of seconds.
'''
from time import sleep_ms
 
# A global variable
press = False
led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN,Pin.PULL_UP)
 
def handle_interrupt(pin):
  global press
  press = True
  global interrupt_pin
  interrupt_pin = pin
 
 
button.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)
 
while True:
  if press:
    print('Press detected! Interrupt caused by:', interrupt_pin)
    led.value(1)
    press = False
    
  sleep_ms(10)
  led.value(0)