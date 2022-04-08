# Exercício 08. Escreva um programa que calcule a menor distância entre um ponto e uma reta, 
# possibilitando que o usuário entre com as informações de dois pontos pertencentes à reta, 
# bem como o ponto para o qual deva ser avaliada a distância.

import numpy as np

print("Vamos calcular a menor distância entre um ponto e uma reta;")
print("Para isto, primeiro passe as coordenadas X e Y do ponto P.")
print("Ponto P:")
x = float(input("\t Coordenada X: "))
y = float(input("\t Coordenada Y: "))

print("\nAgora para a reta;")
print("Informe as coordenadas X e Y dos pontos, P1 e P2, que formam o segmento de reta.")
print("Ponto P1:")
x1 = float(input("\t Coordenada X: "))
y1 = float(input("\t Coordenada Y: "))
print("Ponto P2:")
x2 = float(input("\t Coordenada X: "))
y2 = float(input("\t Coordenada Y: "))

# Usando da forma normal de Hessean

h = ((y2 - y1) * (x - x1) - (x2 - x1) * (y - y1)) / (np.sqrt((x2 - x1)**2 + (y2 - y1)**2))

# Temos a distância 

dist = abs(h)

print("\nA menor distância entre o ponto P(", x,",",y,") e o " \
"segmento de reta formado pelos pontos P1(", x1,",",y1,") e P2(", x2,",",y2,"):  ", dist)