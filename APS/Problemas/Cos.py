import matplotlib.pyplot as plt
import numpy as np

valini = -20 # Valor inicial
duracion = 40  # Num muestras
f = 200
fs = 1000
A = 1

n = np.arange(valini,valini + duracion)

x = A * np.cos(2 * np.pi * n )

plt.xlabel('tiempo')
plt.ylabel('amplitud')
plt.title('Señal')
plt.stem(n, x, '-.')
plt.show()
