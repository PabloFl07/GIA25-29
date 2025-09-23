
T = int(input("Peso total que puede transportar el camión (kg): "))

B = int(input("Peso de cada baldosa (kg): "))

num_baldosas = T // B
print(f"El camión puede transportar {num_baldosas} baldosas.")
