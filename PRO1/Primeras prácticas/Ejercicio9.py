
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
gasto_cervezas = float(input("¿Cuánto has gastado en cervezas esta semana? "))
gasto_transporte = float(input("¿Cuánto has gastado en transporte esta semana? "))

gasto_total = gasto_cervezas + gasto_transporte



representacion = {
    "Nombre: " : nombre,
    "Edad: " : edad,
    "Gasto en cervezas: " : f"{gasto_cervezas:.2f} €",
    "Gasto en transporte: " : f"{gasto_transporte:.2f} €",
    "Gasto total: " : f"{gasto_total:.2f} €"    
}

print("| Datos |")
for key, value in representacion.items():
    print(f"{key}{value}")