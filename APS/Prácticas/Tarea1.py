from machine import Pin
import time

led = Pin(13, Pin.OUT)

estado = 0

while True:
    try:
        estado = not estado
        led.value(estado)
    
        time.sleep(1)
    except KeyboardInterrupt:
        led.value(0)
    