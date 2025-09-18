
T = int(input("Ingrese el peso total que puede transportar el camión (kg): "))

B = int(input("Ingrese el peso de cada baldosa (kg): "))



num_baldosas = T // B
print(f"El camión puede transportar {num_baldosas} baldosas.")
