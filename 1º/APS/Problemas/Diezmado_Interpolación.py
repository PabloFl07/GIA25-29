import matplotlib.pyplot as plt
import numpy as np

valini = 0 # Valor inicial
duracion = 22100 # Num muestras
fs = 44100  # Hz

f = 100
N= 2

n = np.arange(valini,duracion)/fs

xcos = np.cos(2* np.pi * f * n)

xd = xcos[0:duracion:N]

#LINEAS DE DIEZMADO DE x

xd = xcos[0:duracion:N]


#LINEAS DE INTERPOLACION DE x

xi = np.zeros(N*duracion)
xi[0:N*duracion:N] = xcos


plt.subplot(311)
plt.title("coseno")
plt.stem(n[0:200], xcos[0:200], '-.')
plt.subplot(312)
plt.title("diezmado")
plt.stem(n[0:200], xd[0:200], '-.')
plt.subplot(313)
plt.title("interpolacion")
plt.stem(n[0:200], xi[0:200], '-.')
plt.xlabel('tiempo')
plt.ylabel('amplitud')
plt.show()
