# Exercício 06. Faça um programa que pergunte ao usuário o seu conceito final em uma disciplina hipotética. 
# Dependendo do conceito digitado, diga o que ele significa (Excepcional, Bom, etc.). 
# Utilize a tabela de conceitos abaixo:

'''
 1. A+ Excepcional
 2. A  Excelente
 3. A- Excelente
 4. B+ Bom
 5. B  Bom
 6. B- Bom
 7. C+ Regular
 8. C  Regular
 9. C- Regular
10. D  Reprovação

'''

c = input("Qual o conceito final da disciplina?  ")

print("")

if (c == "A+"):
    print(c, "Excepcional")
elif(c == "A"):
    print(c, "Excelente")
elif(c == "A-"):
    print(c, "Excelente") 
elif(c == "B+"):
    print(c, "Bom")
elif(c == "B"):
    print(c, "Bom")
elif(c == "B-"):
    print(c, "Bom")
elif(c == "C+"):
    print(c, "Regular")            
elif(c == "C"):
    print(c, "Regular")
elif(c == "C-"):
    print(c, "Regular")
elif(c == "D"):
    print(c, "Reprovação")                         
else:
    print("Conceito desconhecido.")

print("")