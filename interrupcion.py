import machine
import utime
import urandom
led = machine.Pin(1, machine.Pin.OUT)
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
def button_handler(pin):
 button.irq(handler=None)
 print(pin)
led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
