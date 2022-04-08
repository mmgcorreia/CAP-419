 # Exercício 04. Escreva um programa em Python que pergunte ao usuário um número qualquer (> 0), 
 # e diga se ele é divisível apenas por 2, apenas por 3, por 2 e por 3, ou se não é divisível nem por 2 nem por 3.

n = int(input("Digite um número inteiro maior que zero.\n"))

if (n > 0):
    if (n % 2 == 0 and n % 3 == 0):
        print("O número é divisível por 2 e 3.")
    elif (n % 2 == 0):
        print("O número é divisível por 2.")
    elif (n % 3 == 0):
        print("O número é divisível por 3.")
    else:
        print("O número não é divisível por 2 nem por 3.")
else:
    print("Número fora do intervalo pedido, tente novamente.")                     