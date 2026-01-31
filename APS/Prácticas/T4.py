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
        print(f"{volt:.5f} V | {res:.2f}  kΩ\t-- {val}")
    except ZeroDivisionError:
        print("!Err: 0V!")
    
    time.sleep(0.1)
 
# P3 :  Para un valor de ADC 1, V = 8x10^-4 -> RL = 41250kΩ. Pues no podemos dividir entre 0 | 0.0 ( Con V = Vref ) 
