# Exercício 07. Escreva um programa em Python que simule uma calculadora com as 04 funções básicas (, , , ). 
# O programa deve pedir ao usuário para entrar com os operandos (números reais) e o tipo de operação (+, -, /, *)
# e, a seguir, deverá escrever o resultado.

print("Entre com dois operandos.")
op1 = float(input("Primeiro operando: "))
op2 = float(input("Segundo operando: "))


print("Lembrando que as operações são: \n + => Adição \n - => Subtração \n * => Multiplicação \n / => Divisão \n")
calc = input("Agora entre com a operação que deseja fazer. ")

if(calc == "+"):
    print("Adição: ", op1, "+", op2, "=",  "%.2f" % (op1 + op2))
elif(calc == "-"):
    print("Subtração: ", op1, "-", op2, "=",  "%.2f" % (op1 - op2))
elif(calc == "*"):
    print("Multiplicação: ", op1, "*", op2, "=",  "%.2f" % (op1 * op2))
elif(calc == "/"):
    print("Divisão: ", op1, "/", op2, "=",  "%.2f" % (op1 / op2))
else:
    print("Operação inválida.")                  