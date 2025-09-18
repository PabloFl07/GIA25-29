segundos = int(input("Introduce una cantidad de segundos: "))

segundos_utiles = segundos % 60
minutos_totales = segundos / 60
minutos_utiles = minutos_totales % 60
horas = minutos_totales / 60


print(f" {segundos} segundos son {int(horas)}h:{int(minutos_utiles)}m:{segundos_utiles}s")