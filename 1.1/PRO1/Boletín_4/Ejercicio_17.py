dic = {
    1 : 10,
    2 : 20,
    3 : 30,
    5 : 40
}

k = input("Introduce una clave: ")

if k in dic.keys() or int(k) in dic.keys():
    print("Esa clave existe")