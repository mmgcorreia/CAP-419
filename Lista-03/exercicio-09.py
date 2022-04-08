# Exercício 09. Escreva um programa em Python que avalie se dois segmentos de reta se interceptam ou não.

import numpy as np

print("Informe as coordenadas X e Y dos pontos, P1 e P2, que formam o primeiro segmento de reta, S.")
print("Ponto P1:")
x1 = float(input("\t Coordenada X: "))
y1 = float(input("\t Coordenada Y: "))
print("Ponto P2:")
x2 = float(input("\t Coordenada X: "))
y2 = float(input("\t Coordenada Y: "))

print("Informe as coordenadas X e Y dos pontos, P3 e P4, que formam o segundo segmento de reta, T.")
print("Ponto P3:")
x3 = float(input("\t Coordenada X: "))
y3 = float(input("\t Coordenada Y: "))
print("Ponto P4:")
x4 = float(input("\t Coordenada X: "))
y4 = float(input("\t Coordenada Y: "))

# Usando da forma normal de Hessean

h3 = ((y2 - y1) * (x3 - x1) - (x2 - x1) * (y3 - y1)) / (np.sqrt((x2 - x1)**2 + (y2 - y1)**2))

h4 = ((y2 - y1) * (x4 - x1) - (x2 - x1) * (y4 - y1)) / (np.sqrt((x2 - x1)**2 + (y2 - y1)**2))

if(h3 == 0 or h4 == 0 or h3 * h4 < 0):
    print("\nOs seguimentos de reta S e T se interceptam.")
else:
    print("\nOs seguimentos de reta S e T não se interceptam.")


