dic1 = {1:10, 2:20}
dic2 = {3:30 , 4:40}
dic3 = {5:50 , 6:60}

dic4 = {}

diccionarios = [ dic1 , dic2 , dic3 ]

for dic in diccionarios:  # iteramos sobre cada diccionario de la lista que creamos
    for v in dic.keys():  # iteramos sobre las claves de cada diccionario
        dic4.update({v : dic[v]} )  # Al diccionario final le añadimos el par clave-valor de cada diccionario

print(dic4)