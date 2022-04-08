# Exercício 03. Escreva um programa em Python que pergunte ao usuário um número entre 0 e 10, e diga se ele é ímpar ou par.

n = int(input("Digite um número inteiro entre 0 e 10.\n"))

if(0 <= n <= 10):
    if (n % 2 == 0):
        print("O número é Par!")
    else: 
        print("O número é Ímpar!")    
else:
    print("Número fora do intervalo pedido, tente novamente.")        