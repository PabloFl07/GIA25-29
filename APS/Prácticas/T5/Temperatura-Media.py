import numpy as np
import matplotlib.pyplot as plt


c = np.loadtxt('datos.txt', delimiter=",")


plt.xlabel("Media")
plt.ylabel("Celsius")
plt.title('Señal')
plt.plot(c) 
plt.show()