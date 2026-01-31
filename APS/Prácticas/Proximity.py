from machine import Pin , ADC
import time

led = Pin(13, Pin.OUT)
adc = ADC(Pin(33))
adc.atten(ADC.ATTN_11DB) # Voltaje referencia a 3.3V
vref = 3.3
led.value(0)


def calibrar():
    print("Calibrando el sensor")
    mean = 0
    for i in range(1000):
        mean += adc.read()
    umbral = mean/1000
    print("Fin")

    return umbral + 100

umbral = calibrar() - 200
print(umbral)
while True:
    while adc.read() < umbral:
        time.sleep(adc.read()/10000)
        led.toggle()
    led.value(0)
    