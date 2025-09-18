import math

radios = {
    "radio1": int(input("Ingrese el radio del círculo 1: ")),
    "radio2": int(input("Ingrese el radio del círculo 2: ")),
    "radio3": int(input("Ingrese el radio del círculo 3: "))   
}

perimetro1 = 2 * math.pi * radios["radio1"]
area1 = math.pi * radios["radio1"] ** 2

perimetro2 = 2 * math.pi * radios["radio2"]
area2 = math.pi * radios["radio2"] ** 2

perimetro3 = 2 * math.pi * radios["radio3"]
area3 = math.pi * radios["radio3"] ** 2


print(f"RADIO\tPERIMETRO\tAREA\n=====\t=====\t=====\n{radios['radio1']:.2f}\t{perimetro1:.2f}\t{area1:.2f}\n{radios['radio2']:.2f}\t{perimetro2:.2f}\t{area2:.2f}\n{radios['radio3']:.2f}\t{perimetro3:.2f}\t{area3:.2f}\n")