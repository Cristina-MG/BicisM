from clases import *
import funciones
import pandas as pd

df = pd.read_excel("2018_Julio_Bases_Bicimad_EMT.xlsx")

tot_est = []

for index, row in df.iterrows():
    estacion = Estacion(row[0], row[3], row[1], row[6], row[4], row[5])
    tot_est.append(estacion)

comunidad = ComunidadMadrid(tot_est)

while True:
    print("1. Busca estacion (nombre)")
    print("2. Calcula distancia (entre ids)")
    print("3. Salir del programa")

    opcion = int(input("Introduzca una opción del menú "))
    estacion =None

    if opcion == 3:
        break
    elif opcion ==1:
        respNombre = input("Introduce el nombre d ela estación")

        estacion = Estacion (name = respNombre)
        estacion = comunidad.busca_estacion(estacion,'name')
        print(estacion.name)
    elif opcion ==2:
        est1 = int(input("Introduce el indentificador de la primera estación"))
        est1 = int(input("Introduce el indentificador de la primera estación"))
