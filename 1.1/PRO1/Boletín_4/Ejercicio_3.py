from array import array

array = array("b")
c = 0

while len(array) < 7:
    c +=1
    array.append(int(input(f"Horas del día {c}: ")))


# Opción con sorted ( Ordenamos de menor a mayor y cogemos el primer y último elemento)
# MEDIA
print(f"Media: {sum(array)/2}")

# Mejor día
print("Mejor día:", sorted(array)[-1])

# Peor día
print("Peor día:", sorted(array)[0])

print( )

# Algoritmo de "ordenación"
max = array[0]
for i in range(len(array)):
    if array[i] > max:
        max = array[i]
print("Mejor día:" , max)



min = array[0]
for i in range(len(array)):
    if array[i] < min:
        min = array[i]
print("Peor día:" , min)