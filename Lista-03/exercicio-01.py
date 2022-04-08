# Exercício 01. Faça um programa em Python que leia três números reais e escreva o valor do maior e do menor deles. 
# Para resolver este exercício, não utilizar as funções min/max.

print("Digite 3 números reais.")
n1 = float(input("Primeiro número:"))
n2 = float(input("Segundo número:"))
n3 = float(input("Terceiro número:"))
m = sorted([n1, n2, n3])

print("O menor e maior número dado, respectivamente são:", m[0], " e ", m[2])
