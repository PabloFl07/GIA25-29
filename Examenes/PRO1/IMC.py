
def personaes_extremos_imc(lista_personas):
    imcs = []
    for d in lista_personas:
        if d["peso"] <= 0 or d["altura"] <= 0:
            return None
        imc = d["peso"] / ( d["altura"]**2)
        imcs.append(imc)
        d["imc"] = imc

    imcs.sort()
    max = imcs[-1]
    min = imcs[0]

    return  min , max  



def main():
    lista_personas = [ {"nombre": "ana", "peso": 50, "altura": 1.52}, {"nombre": "luis", "peso": 78, "altura": 1.72}, {"nombre": "marta", "peso": 60, "altura": 1.62}]

    for d in lista_personas:
        print(f"{d["nombre"]} pesa {d["peso"]}kg y mide {d["altura"]}m")

    extremos = personaes_extremos_imc(lista_personas)

    if extremos is not None:
        imc_min , imc_max = extremos
        for i in range(len(lista_personas)):
            if lista_personas[i]["imc"] == imc_min:
                print("La persona con el IMC más bajo es",lista_personas[i]["nombre"], "imc: ", lista_personas[i]["imc"] )
                
        for i in range(len(lista_personas)):
            if lista_personas[i]["imc"] == imc_max:
                print("La persona con el IMC más alto es",lista_personas[i]["nombre"], "imc: ", lista_personas[i]["imc"] )
    else:
        print("Datos de peso y altura inválidos")

main()