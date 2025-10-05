nombre = input("¿Cómo te llamas?: ")
edad = int(input("Cuantos años tienes?: "))

if edad < 25:
    print(f"{nombre} es joven")
elif edad > 75:
    print(f"{nombre} es anciano/a")
else:
    print(f"{nombre} es adulto/a")