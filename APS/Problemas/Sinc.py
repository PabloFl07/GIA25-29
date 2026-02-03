import matplotlib.pyplot as plt
import numpy as np

valini = -20 # Valor inicial
duracion = 40  # Num muestras
f = 200
fs = 1000
A = 1

n = np.arange(valini,valini + duracion)
F = f/fs
x = (A * np.sin(np.pi * n * F) / (np.pi * n))
x[n == 0] = A * F  # Definir el valor en n=0 para evitar división por cero

plt.xlabel('tiempo')
plt.ylabel('amplitud')
plt.title('Señal')
plt.stem(n, x, '-.')
plt.show()
