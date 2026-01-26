"""
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Resultado esperado: {'a': 400, 'b': 400, 'c': 300, 'd': 400}
"""

d1 = {'a': 100, 'b': 200, 'c': 300 , 'g': 500}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = {}


for k in d1.keys():
    if k in d2.keys():
        d3.update({k : d1[k] + d2[k]})
    d3.update({k : d1[k]})
        
for k2 in d2.keys():
    if k2 not in d3.keys():
        d3.update({k2 : d2[k2]})

print(d3)

