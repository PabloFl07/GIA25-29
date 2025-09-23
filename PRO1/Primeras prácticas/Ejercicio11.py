v1 = [ int(input("Primera componente del vector 1: ")), int(input("Segunda componente del vector 1: ")), int(input("Primera componente del vector 1: ")) ]
print("---------------------------------------------------------------------------------------")
v2 = [int(input("Primera componente del vector 2: ")),int(input("Segunda componente del vector 2: ")),int(input("Primera componente del vector 2: "))]


if len(v1) == len(v2):
    producto_escalar = 0
    for i in range(len(v1)):
        producto_escalar += v1[i] * v2[i]
    print(f"[+] Producto escalar de los vectores: {producto_escalar}")