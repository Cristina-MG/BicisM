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

    try:
        opcion = int(input("Introduzca una opción del menú entre 1 y 3 "))

        estacion = None

        if opcion == 3:

            break

        elif opcion == 1:

            respNombre = input("Introduce el nombre de la estación ")

            estacion = Estacion(name = respNombre)
            estacion = comunidad.busca_estacion(estacion,'name')

            if estacion:
                print('Nombre:',estacion.name)
                print('id:', estacion.identificador)
                print('Número de bicis:', estacion.num_bicis)
                print('Direccion:', estacion.addres)
                print('Longitud geográfica:', estacion.longitude)
                print('Latitud geográfica:', estacion.latitude,'\n')

            else:

                print("No se han obtenido resultados\n")

        elif opcion == 2:
            try:
                est1 = int(input("Introduce el indentificador (número entero) de la primera estación "))
                est2 = int(input("Introduce el indentificador (número entero) de la segunda estación "))

                print("La distancia entre estación con id", est1, "y", est2, "es:")
                print(funciones.dist_estaciones(est1, est2, comunidad))

            except:
                print("Hay que introducir un número entero para identificar la estación ")
        else:
            print("Hay que introducir un número entero entre el 1 y el 3 para ejecutar una opción del menú ")
    except:
        print("Hay que introducir un número entero entre el 1 y el 3 para ejecutar una opción del menú ")
