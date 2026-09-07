import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io.wavfile import read
import sounddevice as sd

tipocanal = 6
tiposenal = 0 #1:coseno 2:audio
# ===== CANAL =====
if tipocanal == 1:
    nombre_canal = "Golpe real"

    fh, h = read('h_golpe.wav')
    amplitude = np.iinfo(np.int16).max
    if h.ndim > 1:
        h = h[:,0]
    Lh = len(h)
    nh = np.arange(Lh)/fh

elif tipocanal == 2:
    nombre_canal = "Golpe con eco (archivo)"

    fh, h = read('h_golpe_eco.wav')
    if h.ndim > 1:
        h = h[:,0]
    Lh = len(h)
    nh = np.arange(Lh)/fh

elif tipocanal == 3:
    nombre_canal = "Delta retardada"

    a = 0.5
    n1 = 0.2
    Lh = 22050
    fh = 22050
    nh = np.arange(Lh)/fh
    h = a * (nh == n1)

elif tipocanal == 4:
    nombre_canal = "Exponencial decreciente"

    a = 0.999
    Lh = 22050
    fh = 22050
    nh = np.arange(Lh)/fh # EJE X
    h = a ** np.arange(Lh) # a ^ 1, 2 ...

elif tipocanal == 5:
    nombre_canal = "Eco múltiple (3 deltas)"
    a1, a2, a3 = 1, 0.4, 0.2   # AMPLITUD DEL IMPULSO
    n1, n2, n3 = 0.1, 0.5, 0.7 # INSTANTES DE TIEMPO DONDE HAY IMPULSO
    fh = 22050
    Lh = 22050
    nh = np.arange(Lh)/fh # EJE X
    h = a1 * (nh == n1) + a2 * (nh == n2) + a3 * (nh == n3)

elif tipocanal == 6:
    nombre_canal = "Conexión en serie" 
    a1, a2, a3 = 1, 0.4, 0.2
    n1, n2, n3 =  0.1, 0.5, 0.7
    fh = 22050
    Lh = 22050
    nh = np.arange(Lh)/fh
    h1 = a1 * (nh == n1) + a2 * (nh == n2) + a3 * (nh == n3)
    a = -0.9995
    h2 = a ** np.arange(Lh) # Lo elevamos a tiempo discreto para evitar N Complejos

    h = np.convolve(h1, h2)

    nh = np.arange(len(h))/fh
     
    # COMPLETAR
    
elif tipocanal == 7:
    nombre_canal = "Conexión en paralelo"
    a1, a2, a3 = 1, 0.4, 0.2
    n1, n2, n3 =  0.1, 0.5, 0.7
    fh = 22050
    Lh = 22050
    a = -0.9995

    nh = np.arange(Lh)/fh

    h1 = a1 * (nh == n1) + a2 * (nh == n2) + a3 * (nh == n3)

    h2 = a ** np.arange(Lh)

    h = h1 + h2

    nh = np.arange(len(h))/fh


    # TAREA PROPUESTA
    
# ===== PLOT h =====

plt.figure(1)
plt.stem(nh, h)
plt.title(f"Respuesta al impulso h[n] — {nombre_canal}")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# ===== AUDIO =====
if tiposenal == 1:
    f = 440 #Usa nh definida anteriormente
    fs = fh
    x = np.cos(2 * np.pi * f * nh)
elif tiposenal == 2:
    fs, x  = read('hola_22050.wav')
    amplitude = np.iinfo(np.int16).max
    x = x/amplitude




# normalizamos para evitar saturación al convolucionar
# Convertir a float y normalizar
if h.dtype == np.int16:
    h = h.astype(np.float32) / np.iinfo(np.int16).max
elif h.dtype == np.int32:
    h = h.astype(np.float32) / np.iinfo(np.int32).max
else:
    h = h.astype(np.float32)
h /= (np.max(np.abs(h)) + 1e-12)


"""
# COMPLETAR
plt.figure(2)
plt.stem(nh[0:10000], y[0:10000])
plt.title(f"Salida del sistema LTI — {nombre_canal}")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

sd.play(y, fs)

"""

