# Exercício 05. Faça um programa em Python que pergunte ao usuário qual a série que ele deseja calcular 
# e em seguida imprima o nome da série escolhida. 
# Veja o exemplo do que deve ser escrito na tela:

'''
0 Lucas
1 Pell
2 Triangular
3 Square
4 Pentagonal

Qual série você deseja computar? 3

Você escolheu computar a série "Square"!

'''
print(" 0 Lucas \n 1 Pell \n 2 Triangular \n 3 Square \n 4 Pentagonal \n")
n = int(input("Qual série você deseja computar? "))

if(n == 0):
    print('\nVocê escolheu computar a série "Lucas"!\n')
elif(n == 1):
    print('\nVocê escolheu computar a série "Pell"!\n')
elif(n == 2):
    print('\nVocê escolheu computar a série "Triangular"!\n')    
elif(n == 3):
    print('\nVocê escolheu computar a série "Square"!\n')
elif(n == 4):
    print('\nVocê escolheu computar a série "Pentagonal"!\n')
else:
    print("O número dado não equivale a nenhuma série acima.")        



