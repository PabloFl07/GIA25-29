import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("/home/pablo/Dev/Uni/GIA25-29/APS/Prácticas/T5/datos.txt", delimiter=",")


plt.title('Señal de temperatura')
plt.plot(data) 
plt.legend(['Temperatura (ºC)', "Media móvil (50 muestras)"])
plt.show()

