import matplotlib.pyplot as plt
import numpy as np

" Señal distribucion uniforme"
valini = 0 # Valor inicial
duracion = 1000000
media = 0
sigma = 1
n = np.arange(valini,duracion)

xr = np.random.normal(media, sigma, duracion)

plt.xlabel('tiempo')
plt.ylabel('amplitud')
plt.title('Señal aleaotria gaussiana')
plt.stem(n, xr, '-.')

plt.figure(2)
plt.hist(xr, bins=100) 
plt.show()
