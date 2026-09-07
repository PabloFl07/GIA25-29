from machine import Pin , ADC
import time
from math import log10

adc = ADC(Pin(33))
adc.atten(ADC.ATTN_11DB) # Voltaje referencia a 3.3V
vref = 3.3
F = 20 # Frecuencia

while True:
    val = adc.read() # Valor medido por el ADC
    volt = (val * vref) / 4096 # Calculo del voltaje
    try:
        res = ((vref * 10 / volt) - 10) # Calculo de la resistencia
        K = (1 / ((1/298.15) + (log10(res/10))/3950)) # Calculo de la temperatura
        C = K - 273.15 # Conversion a Celsius
    
        print(f"{volt:.5f} V | ADC {val} | {C:.5f}º ")
        
    except ZeroDivisionError:
        print("!Err: 0V!")
    
    time.sleep(1/F)
    
# P1 : Si permanece estable, Se debe a que medimos con mas frecuencia y obtenemos un resultado mas preciso

