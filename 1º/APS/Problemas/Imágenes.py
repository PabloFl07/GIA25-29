import matplotlib.pyplot as plt
import numpy as np
from skimage import io
#Módulo skcikit-image

# Leer la imagen
# AÑADIR LÍNEA DE LEER IMAGEN

imagen = io.imread("/home/pablo/Dev/Uni/GIA25-29/APS/Problemas/peppers.png")

print("- Dimensiones de la imagen:")
print(imagen.shape)

# Mostrar la imagen en RGB
plt.figure()
plt.imshow(imagen)
plt.title("Imagen RGB")  
plt.axis("off")  
plt.show()

#==================================================
# Extraer y reprsentar cada componente
Ir = imagen[:, :, 0]
Ig = imagen[:, :, 1]
Ib = imagen[:, :, 2]

# Mostrar cada canal
plt.figure()
plt.imshow(Ir, cmap="gray")
plt.colorbar()
plt.title("Canal rojo")  
plt.axis("off")

plt.figure()
plt.imshow(Ig, cmap="gray")
plt.colorbar()
plt.title("Canal verde")  
plt.axis("off")

plt.figure()
plt.imshow(Ib, cmap="gray")
plt.colorbar()
plt.title("Canal azul")  
plt.axis("off")
plt.show()

#==================================================
# Convertir a luminancia
kb = 0.114
kr = 0.299
Y = kr*Ir + (1-kb-kr)*Ig + kb*Ib

plt.figure()
plt.imshow(Y, cmap="gray")
plt.title("Luminancia")
plt.axis("off")
plt.show()

#==================================================
# Submuestreo
N = 2
n_filas = Y.shape[0]
n_columnas = Y.shape[1]

#AÑADIR LAS LÍNEAS DEL SUBMUESTREO

Y_sub2 = Y[0:n_columnas:N]

plt.figure()
plt.imshow(Y_sub2, cmap="gray")
plt.title("Y submuestreada")
#plt.axis("off")
plt.show()


