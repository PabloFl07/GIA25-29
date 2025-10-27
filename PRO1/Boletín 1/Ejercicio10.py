
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
num_hijos = int(input("Ingrese el número de hijos: "))
sueldo_anual = float(input("Ingrese su sueldo anual: "))

sueldo_mensual = sueldo_anual / 12

representacion = {
    "Nombre: " : nombre,
    "Edad: " : edad,
    "Número de hijos: " : num_hijos,
    "Sueldo mensual: " : f"{sueldo_mensual:.2f} €"    
}

print("| Datos |")
for key, value in representacion.items():
    print(f"{key}{value}")