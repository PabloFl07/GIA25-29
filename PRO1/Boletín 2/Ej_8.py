'''
Plantee e implemente un programa que implemente el algoritmo necesario para
calcular la edad de una persona suponiendo que se le pide al usuario que introduzca su
fecha de nacimiento por teclado y a la salida muestra por pantalla su edad con
respecto a la fecha actual. Tenga en cuenta el cumpleaños de la persona para realizar
el cálculo.
'''

año = 2025
mes = 10
dia = 3


año_n = int(input("Introduce el año de nacimiento: "))
mes_n = int(input("Introduce el mes de nacimiento: "))
dia_n = int(input("Introduce el día de nacimiento: "))

if año != año_n :
    if mes < mes_n:
        print(f"Tu edad es: {año-año_n -1}")
    elif dia > dia_n:
        print(f"Tu edad es: {año-año_n -1 }")
    else:
        print(f"Tu edad es: {año-año_n }")
else:
    print(f"Tu edad es inferior a un año")
