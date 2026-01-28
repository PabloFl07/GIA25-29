import matplotlib.pyplot as plt
import numpy as np

valini = -10 # Valor inicial
duracion = 20  # Num muestras

n = np.arange(valini,valini + duracion)

#x = (n == 0) # tuple comprehension, valores para los que n == 0, 1 ...
#x = (n >= 0) #Escalón unitario
#x = (n *(n >= 0)) # Rampa unitaria

a = [ -0.9, 0.9, 1.1 , -1.1] # Tipos de exponenciales

x = (a[1]**n  * (n>=0))# Al multiplicar por el escalón unitario, se anula para n<0




plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.title('Señal')
plt.stem(n, x, '-.') 
plt.show()
