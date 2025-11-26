notas = [{'id' : 1, 
          'asignatura' : 'FP1', 
          "nota1": 7.5 , 
          'nota2' : 8.5},
        
        {'id' : 2, 
         'asignatura' : 'FP1', 
         "nota1": 6.5 , 
         'nota2' : 6.5},

        {'id' : 3, 
         'asignatura' : 'FP1', 
         "nota1": 7.5 , 
         'nota2' : 8.0}
         ]
"""
notas = [{'id' : 1, 'asignatura' : 'FP1', nota1: 7.5 , 'nota2' : 8.5, media: 8.0},
{'id' : 2, 'asignatura' : 'FP1', nota1: 6.5 , 'nota2' : 6.5, media: 6.5},
{'id' : 3, 'asignatura' : 'FP1', nota1: 7.5 , 'nota2' : 8.0, media: 7.75}]
"""


for i in range(len(notas)):
    media = (notas[i]["nota1"] + notas[i]["nota2"]) / 2
    notas[i].update({"media" : media})

print(notas)

