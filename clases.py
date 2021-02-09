
import math


class Estacion:

    def __init__(self,  name = None ,  identificador = 0, num_bicis = None , address = None , longitude = None , latitude= None ):
        self.name = name
        self.identificador = identificador
        self.num_bicis = num_bicis
        self. addres = address
        self.longitude = longitude
        self.latitude = latitude

    def distancia(self, latitude, longitude):
        lat1, lon1 = self.latitude, self.longitude
        lat2, lon2 = latitude, longitude
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        return d


class ComunidadMadrid:

    def __init__(self, estaciones ):
        self.estaciones = estaciones


    def get_ids(self):
        lista_identificadores = []
        for estacion in self.estaciones:
            lista_identificadores.append(estacion.identificador)
        return lista_identificadores

    def busca_estacion(self, estacion, tipo_busqueda):

        if tipo_busqueda == 'id':
            estacionResp = None

            for item in self.estaciones:
              if item.identificador == estacion.identificador:
                  estacionResp = item
                  break

            return estacionResp
        else:
            estacionResp = None

            for item in self.estaciones:
              if estacion.name.lower() in item.name.lower():
                  estacionResp = item
                  break

            return estacionResp



