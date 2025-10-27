IVA = 0.24
precio_sin_iva = float(input("Precio sin IVA: "))
print(f"El precio con IVA es {round(precio_sin_iva*(1+IVA), 2)}€")