from machine import Pin , ADC
import time
from math import log10

adc = ADC(Pin(33))
adc.atten(ADC.ATTN_11DB) # Voltaje referencia a 3.3V
#adc.atten(ADC.ATTN_6DB) # Voltaje referencia a 2V

vref = 3.3
#vref = 2

suma_total = 0
array = []

while True:
    val = adc.read() # Valor medido por el ADC
    volt = (val * vref) / 4096 # Calculo del voltaje
    try:
        res = ((vref * 10 / volt) - 10) # Calculo de la resistencia
        K = (1 / ((1/298.15) + (log10(res/10))/3950))
        C = K - 273.15
        
        if len(array) < 200: # Ejemplo con 5 para probar rápido
            array.append(C)
            suma_total += C
            media = suma_total / len(array)
        else:
            break
    
        print(f"{volt:.5f} V | ADC {val} | {C:.5f}º | M{len(array)} = {media:.5f}")
        
    except ZeroDivisionError:
        print("!Err: 0V!")
    
    time.sleep(0.05)
    
    
# P1 : Si permanece estable, Se debe a que medimos con mas frecuencia y obtenemos un resultado mas preciso

