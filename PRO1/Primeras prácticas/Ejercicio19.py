
nombre = input("Introduce tu nombre: ")
apellidos = input("Introduce tus apellidos: ")
sueldo_mensual = float(input("Introduce tu sueldo mensual (€): "))
gasto_ocio = float(input("¿Cuánto gastas diariamente en ocio (€)?: "))
gasto_comida = float(input("¿Cuánto gastas diariamente en comida (€)?: "))
gasto_transporte = float(input("¿Cuánto gastas diariamente en transporte (€)?: "))

ocio_semana = gasto_ocio * 7
comida_semana = gasto_comida * 7
transporte_semana = gasto_transporte * 7
gasto_semana = ocio_semana + comida_semana + transporte_semana

porc_ocio = (ocio_semana / sueldo_mensual) * 100
porc_comida = (comida_semana / sueldo_mensual) * 100
porc_transporte = (transporte_semana / sueldo_mensual) * 100

print("*********************************************")
print("****\t\t{nombre} {apellidos}\t\t****")