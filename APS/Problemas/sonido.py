import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

valini = 0 # Valor inicial
duracion = 44100  # Num muestras
fs = 44100  # Hz

f = 440

n = np.arange(valini,duracion)/fs
Na = 10

xcos = np.cos(2 * np.pi * f * n)

#======================================
#for i in range(2,Na+1):
    #xcos += np.cos(2*np.pi*f*i*n)
#======================================

   # sd.play(xcos/np.max(np.abs(xcos)), fs)

# =====================================

for k in [2.02, 2.97, 3.86]:
    xcos += np.cos(2*np.pi*f*k*n)

    sd.play(xcos/np.max(np.abs(xcos)), fs)



plt.stem(n[0:1000], xcos[0:1000], '-.')
plt.xlabel('tiempo')
plt.ylabel('amplitud')
plt.show()
