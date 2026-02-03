from machine import Pin , ADC
import time

adc = ADC(Pin(33))
adc.atten(ADC.ATTN_11DB) # Voltaje referencia a 3.3V
#adc.atten(ADC.ATTN_6DB) # Voltaje referencia a 2V

vref = 3.3
#vref = 2


while True:
    val = adc.read() # Valor medido por el ADC
    volt = (val * vref) / 4096 # Calculo del voltaje
    try:
        res = ((vref * 10 / volt) - 10) # Calculo de la resistencia
        print(f"{volt:.5f} V | {res}  kΩ\t-- {val}")
    except ZeroDivisionError:
        print("!Err: 0V!")
    
    time.sleep(0.1)
    
    
# P1 : Aproximadamente 3500 | 1.43 - kΩ aprox.
# P2 : Aproximadamente 1400 | 20 kΩ aprox.
# P3 : Para un valor de ADC 1, V = 8x10^-4 -> RL = 40950kΩ. Pues no podemos dividir entre 0 | 0.00244 ( Con V = Vref ) 
