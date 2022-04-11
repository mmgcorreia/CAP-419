# Exercício 02. Escreva um programa em Python que leia o tamanho dos lados de um triângulo, 
# avalie se esses valores realmente formam um triângulo,
# e em caso positivo, classifique o triângulo em isósceles, escaleno ou equilátero.

from stringprep import c22_specials
from xml.etree.ElementTree import C14NWriterTarget


print("Digite o tamanho dos 3 lados do triângulo:")
a = float(input("Primeiro lado:"))
b = float(input("Segundo nlado:"))
c = float(input("Terceiro lado:"))

'''
Condição de existência de um triãngulo

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

'''
c1 = abs(b - c) < a < (b + c)
c2 = abs(a - c) < b < (a + c)
c3 = abs(a - b) < c < (a + b)

if (c1 == True and c2 == True and c3 == True):
    print("Estes valores formam um triângulo: ")
    if ( a == b == c):
        print("\t Equilátero.")
    elif ( a != b != c):
        print("\t Escaleno.")
    else:
        print("\t Isósceles.")
else:
    print("Estes valores não formam um triângulo.")            
