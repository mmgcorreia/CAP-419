# Importar bibliotecas necessárias
import numpy as np
import math

print("O programa irá pedir as coordenadas de dois pontos quaisquer da esfera terrestre. \n")

# Inicializar as listas das latitudes e longitudes
la = [] #latitude
lo = [] #longitude

# 1 radiano * 180/pi = aprox. 57º
la.append(math.radians(float(input("\t Latitude do primeiro ponto:\t"))))
lo.append(math.radians(float(input("\n\t Longitude do primeiro ponto:\t"))))
la.append(math.radians(float(input("\n\t Latitude do segundo ponto:\t"))))
lo.append(math.radians(float(input("\n\t Longitude do segundo ponto:\t"))))


# raio da esfera = r = aprox. 6371 km
r = 6371

# Usando a fórmula de Haversine
def distancia(r, la, lo):
    sin_la = math.sin((la[1] - la[0])/2)
    sin_lo = math.sin((lo[1] - lo[0])/2)
    arc_sin = sin_la**2 + math.cos(la[0]) * math.cos(la[1]) * sin_lo**2
    return 2 * r * np.arcsin(math.sqrt(arc_sin))

print("\nA distância entre os dois pontos dados é:\t", distancia(r, la, lo), "\n")    