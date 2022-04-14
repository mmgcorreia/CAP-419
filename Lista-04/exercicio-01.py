# Exercício 01. Faça um programa para computar e apresentar a sequência de cada uma das seguintes séries numéricas, 
# depois de ler um número inteiro n>=0:

# Declaração das funções
def Lucas(n):
    if(n==0):
        return 2
    elif(n==1):
        return 1
    else:
        return (Lucas(n-1) + Lucas(n-2))   

def Pell(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (2*Pell(n-1) + Pell(n-2))

def Triangular(n):
        return int((n*(n+1))/2)

def Square(n):
        return (n**2)

def Pentagonal(n):
        return int((3*n**2-n)/2)

# Início das chamadas
n = int(input("\nInsira um número inteiro maior ou igual a zero:\t"))

if (n >= 0):
    seq_lucas = []
    seq_pell = []
    seq_triangular = []
    seq_square = []
    seq_pentagonal = []

    while(n >=0):
        seq_lucas.append(Lucas(n))
        seq_pell.append(Pell(n))
        seq_triangular.append(Triangular(n))
        seq_square.append(Square(n))
        seq_pentagonal.append(Pentagonal(n))
        n-=1
    
    print("\nLucas:\t", seq_lucas[::-1])
    print("\nPell:\t", seq_pell[::-1])
    print("\nTriangular:\t", seq_triangular[::-1])
    print("\nSquare:\t", seq_square[::-1])
    print("\nPentagonal:\t", seq_pentagonal[::-1], "\n")

else:
    print("\nO número inserido não corresponde ao pedido, tente novamente.\n")    