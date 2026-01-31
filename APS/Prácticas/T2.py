from machine import Pin
import time

p13 = Pin(13, Pin.OUT)
p2 = Pin(2, Pin.IN) 

parp = False
estado = 0
cont = 0
try:
    while True:
        estado = p2.value() # Recoge el estado de el boton 
        if estado == 1: # Si lo presionamos, activa o desactiva el parpadeo
            parp = not parp 
            if not parp:
                p13.value(0) 
            time.sleep(0.2)

        if parp:
            if time.ticks_ms() - cont > 1000: # Si ha pasado mas de 1 segundo, parpadea
                p13.toggle()
                cont = time.ticks_ms() # Reiniciamos el contador del segundo
except KeyboardInterrupt:
    p13.value(0)