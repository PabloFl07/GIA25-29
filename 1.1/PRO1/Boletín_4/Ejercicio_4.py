string = str(input("Introduce una cadena: "))
# Hacemos las comprobaciones sobre los caracteres en minúscula siempre
caracter = string[0].lower()  # Obtenemos el primer caracter 

def subs(string , caracter):
    for i in range(1 , len(string)): # Iteramos sobre cada caracter y comprobamos si hay una coincidencia
        if caracter == string[i].lower():
            return string[:i] + "$" + string[i+1:]  # Juntamos: la cadena previa a ese caracter, el caracter de remplazo , y el resto a partir de la siguiente posición

print(subs(string, caracter))