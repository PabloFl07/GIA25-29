from machine import Pin , ADC
import time
from math import log

adc = ADC(Pin(33))
adc.atten(ADC.ATTN_11DB) # Voltaje referencia a 3.3V

vref = 3.3
VENTANA = 50
cola = []
current_sum = 0.0  

while True:
    try:   
        val = adc.read() # Valor medido por el ADC
        volt = (val * vref) / 4096 # Calculo del voltaje
        res = ((vref * 10 / volt) - 10) # Calculo de la resistencia
        K = (1 / ((1/298.15) + (log(res/10))/3950)) # Calculo de la temperatura
        C = K - 273.15 # Conversion a Celsius
            
        if len(cola) == VENTANA:
            old = cola.pop(0) # Elimina y guarda el ultimo (por antiguedad) de la cola
            current_sum -= old
    
        cola.append(C)
        current_sum += C
    
        media = current_sum / len(cola)
        print(f"{volt:.5f} V | ADC {val} | {C:.5f}º | {media:.5f}")
    except ZeroDivisionError:
        print("!Err: 0V!")
    
    time.sleep(0.05)
    
# La media movil suaviza la señal y la reduce.

