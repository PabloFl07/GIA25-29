print("A.Bebé\nB.Adolescente\nC.Mujer\nD.Hombre")

sel = input("Selecciona una opción ( A - B - C - D): ")

if sel.lower() == "a": # lower por si el usuario introduce la letra en minúscula, se siga verificando la condición
    print("Bebé")
elif sel.lower() == "b":
    print("Adolescente")
elif sel.lower() == "c":
    print("Mujer")
else:
    print("Hombre")