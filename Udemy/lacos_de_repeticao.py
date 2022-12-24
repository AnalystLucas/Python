"""
######################
# Laços de Repeticão #
######################

while
For

Laços de repetição são usados para executar parte do codigo algumas vezes, ou varias vezes
podendo ser controlado ou durar enquanto for necessário, so vai parar de executar o codigo quando a condição não for mais verdadeira

argumento range no for podemos controlar o quanto queremos imprimir
range(5) - sera retornado a contagem de 0 até 4
range(5,10) - sera retornado a contagem de 5 até 9 pois quando colocado 2 numeros dentro do range você esta dizendo quando começar e onde terminar
range(10,20,2) - sera retornado a contagem de 10 a 19 porém contando de 2 em 2, pois colocando 3 numeros dentro do range você controla onde começa, onde termina e como ele vai contar.

"""
#Usando o While
# x = 1
# while x < 10:
#     print(x)
#     x += 1

#Usando For
# for i in range(5):
#     print(i)

#Usando For
# for i in range(5,10):
#     print(i)

# Usando For
for i in range(10,20,2):
    print(i)

#Usando for para percorer uma lista (Array)
# lista1 = [1,2,3,4,5]
# lista2 = ["ola","mundo","!"]
# lista3 = [0,"ola","biscoito","bolacha",9.99,True]

# for i in lista1:
#     print(i)

# for i in lista2:
#     print(i)

# for i in lista3:
#     print(i)