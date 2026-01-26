#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pablo Fernández Lema
"""

def estudiantes_bajo_media(lista_estudiantes):
    sumatorio = 0
    validos = [ ]
    
    c = 0
    for d in lista_estudiantes:
        if d["nota"] in range(11):
            sumatorio += d["nota"]
            c += 1
        
    if c == 0: # Ninguno es válido
        return 0 , []
    else:
        media = sumatorio / c
    
    for d in lista_estudiantes:
        if d["nota"] < media and d["nota"] != -1:
            validos.append(d["nombre"])
            
    return media, validos
    




def main():
    lista_estudiantes=[
        {
            "nombre": "Ana",
            "nota": 7
         },
        {
            "nombre": "Luis",
            "nota" : 4
            },
        {
            "nombre": "Marta",
            "nota": 9
         },
        {
            "nombre": "Pedro",
            "nota": -1
         },
        ]
    
    
    media , validos = estudiantes_bajo_media(lista_estudiantes)
    
    print("Estudiantes: ")
    for d in lista_estudiantes:
        print(f"\t{d["nombre"]} : nota {d["nota"]}")
    
    print(f"\nMedia de la clase: {media:.2f}\n")
    print("Estudiantes por debajo de la media:")
    
    for d in lista_estudiantes:
        if d["nota"] < media and d["nombre"] in validos:
            print(f"\t{d["nombre"]}: nota {d["nota"]}")
        
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

