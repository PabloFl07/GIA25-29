import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io.wavfile import read
import sounddevice as sd

tipocanal = 4

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
    nh = np.arange(Lh)/fh
    h = a ** np.arange(Lh)


elif tipocanal == 5:
    nombre_canal = "Eco múltiple (3 deltas)"


# ===== PLOT h =====
plt.figure(1)
plt.stem(nh, h)
plt.title(f"Respuesta al impulso h[n] — {nombre_canal}")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

