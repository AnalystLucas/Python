"""

###############
# EXCERCICIOS #
###############

Praticar

1 - Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade. 
2 - Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   
3 - Escreva um programa que resolva uma equação de segundo grau.   
4 - Escreva um programa que ordene uma lista numérica com três elementos.   
5 - Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   


"""

# 1
# idade = int(input("Por favor informar sua Idade ?"))
# if (idade >= 18):
#     print("Você já é maior de idade")
# else:
#     print("Você é menor de idade")
#-----------------------------------------------------
# 2
# nota1 = int(input("Por favor inserir nota 1: "))
# nota2 = int(input("Por favor inserir nota 2: "))

# media = (nota1 + nota2) / 2

# if(media >= 6):
#     print("Aluno Aprovado")
# else:
#     print("Aluno Reprovado")
#-----------------------------------------------------
# 3
# from math import sqrt
# a = int(input("Digite o valor de A: "))
# b = int(input("Digite o valor de B: "))
# c = int(input("Digite o valor de C: "))
 
# delta = b**2 - 4*a*c
 
# if delta < 0:
#     print("Delta negativo")
# else:
#     raiz_delta = sqrt(delta)
#     x1 = (-b + raiz_delta)/2*a
#     x2 = (-b - raiz_delta)/2*a
 
#     print("As raízes são", x1, "e", x2)
#-----------------------------------------------------
# 4 
# l = [15,5,10]
# l.sort()
# print(l)
#-----------------------------------------------------
# 5
n1 = int(input("Inserir valor1: "))
n2 = int(input("Inserir valor2: "))
op = input("Inserir sinal (+, -, *, / ): ")
aux = 0

if(op == "+"):
    aux = n1 + n2
    print(aux)
elif(op == "-"):
    aux = n1 - n2
    print(aux)
elif(op == "*"):
    aux = n1 * n2
    print(aux)
elif(op == "/"):
    aux = n1 / n2
    print(aux)
else:
    print("Opção invalida !!") 
#-----------------------------------------------------


 