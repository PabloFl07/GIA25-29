
max_f = float(input("Introduce la temperatura máxima en Fahrenheit: "))
min_f = float(input("Introduce la temperatura mínima en Fahrenheit: "))

max_c = (max_f - 32) * 5 / 9
min_c = (min_f - 32) * 5 / 9


print("-------------------------Lugo 18/9/2025--------------------------")
print(f"T Max (ºF)\tT Min (ºF)\tT Max (ºC)\tT Min (ºC)\n{max_f:.2f}ºF\t\t{min_f:.2f}ºF\t\t{max_c:.2f}ºC\t\t{min_c:.2f}ºC")
print("-----------------------------------------------------------------")