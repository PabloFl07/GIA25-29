

while True:
    char = input("[+] Introduce un caracter: ")
    if char.isdigit():
        print("Es un dígito")
    elif not char.isalnum():
        print("Es un caracter especial")
    elif char.lower() in ['a', "e", "i", "o", "u"]:
        print("Es una vocal")
    else:
        print("Es una consonante")


