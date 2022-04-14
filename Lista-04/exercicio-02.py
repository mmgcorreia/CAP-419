# Exercício 02. Escrever um programa em Python que simule uma calculadora com as funções básicas (+, -, /, *). 
# O programa deve pedir ao usuário para entrar com os operandos (números reais) e o tipo de operação, 
# e a seguir escrever o resultado. Assim como uma calculadora, que ao final de uma operação pode ser utilizada novamente, 
# você deve simular este comportamento perguntando ao usuário se ele quer realizar uma nova operação.



def calculadora(op1, op2):
    print("Lembrando que as operações são: \n + => Adição \n - => Subtração \n * => Multiplicação \n / => Divisão \n")
    calc = input("Agora entre com a operação que deseja fazer: \t")

    if(calc == "+"):
        result = (op1 + op2)
        print("Adição: ", op1, "+", op2, "=",  "%.2f" % result)
    elif(calc == "-"):
        result = (op1 - op2)
        print("Subtração: ", op1, "-", op2, "=",  "%.2f" % result)
    elif(calc == "*"):
        result = (op1 * op2)
        print("Multiplicação: ", op1, "*", op2, "=", "%.2f" % result)
    elif(calc == "/"):
        if(op2 != 0.0):
            result = (op1 / op2)
            print("Divisão: ", op1, "/", op2, "=", "%.2f" % result)
        else: 
            print("ERRO!")
            return 'n', None    
    else:
        print("Operação inválida.")
        return 'n', None  
    
    cont = input("\nDeseja realizar uma nova operação ? \n\t 'y' - SIM | 'n' - NÃO \n")
    return  cont, result   
    
print("Entre com dois operandos.")
op1 = float(input("Primeiro operando: "))
op2 = float(input("Segundo operando: "))

# Continuação da função da calculadora
cont='y'

while(cont=='y'):
    cont, result = calculadora(op1, op2)
    if(cont=='n'): break
    op1 = result
    op2 = float(input("Entre com um novo operando: \t"))
