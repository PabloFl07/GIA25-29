dic = {}

while len(dic) < 10:
    n = int(input("Introduce un número: "))
    dic.update({ n : n*n })

print(dic)


