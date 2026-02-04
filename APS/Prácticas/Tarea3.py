from machine import Pin , ADC
import time

adc = ADC(Pin(33))
#adc.atten(ADC.ATTN_11DB) # Voltaje referencia a 3.3V
adc.atten(ADC.ATTN_6DB) # Voltaje referencia a 2V

#vref = 3.3
vref = 2


while True:
    val = adc.read() # Valor medido por el ADC
    volt = (val * vref) / 4096 # Calculo del voltaje
    print(f"{volt} V -- {val}")
    time.sleep(0.1)


# P1 : 4095, el maximo, porque el ADC calcula valores desde 0 hasta 2^n -1 (n bits de resolucion), que con 12 bits es 4095.
# P2 : 12 porque el valor maximo que mide es 4095 ( 2^12 -1 ) .  255 ( 2^8 -1 )
# P3 : A partir de la mitad. 1.999 . 3.3 V, el voltaje real se mantiene en 3.3 V pero el ADC solo mide hasta 2 V