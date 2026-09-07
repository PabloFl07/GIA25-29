d1 = {'a': 100, 'b': 200, 'c': 300 , 'g': 500}
d2 = {'a': 300, 'b': 200, 'd': 400}



for k in d1.keys():
    if k in d2.keys():
        print(f"{k} existe en los dos diccionarios")