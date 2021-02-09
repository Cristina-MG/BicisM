from clases import Estacion


def dist_estaciones(est1, est2, comunidad):

    estacion1 = Estacion( identificafor = est1)
    estacion2 = Estacion( identificafor = est2)

    estacion1 = comunidad.busca_estacion(estacion1, 'id')
    estacion2 = comunidad.busca_estacion(estacion2, 'id')

    distancia = estacion1.distancia(estacion2.latitude, estacion2.longitude)

    return distancia


