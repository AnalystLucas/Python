"""
#################
# LISTA (ARRAY) #
#################

Lista - conhecidos como array/vetores, são  basicamente uma variavel que tem varios espaços dentro para ser utilizado para armazenar informações/dados.
Podem ser de numeros, texto ou com os dois.

"""

my_list = ["abacaxi","melancia","abacate"] # Lista somente de string
my_list2 = [1,2,3,4,5] # Lista somente de numeros
my_list3 = ["abacaxi",2,9.89,True] # Lista com string, numeros e valor boleano (True), varios dados na mesma lista

#Para exibir toda uma lista basta somente colocar o nome da lista dentro do print
# print(my_list)

#Para exibir uma possição expecifica de uma lista, precisa informar junto com o nome da lista
# print(my_list2[3])

#Para percorer uma lista podemos usar o for para isso
# for item in my_list3:
#     print(item)

#Para saber o tamanho da lista usa a função len()
# t = len(my_list)
# print(t)

#Manipular Lista com metodos especificos, usamos o append()
# my_list.append("limão")
# print(my_list)

#Validar se tem algum dado especifico na lista, usando o if
# if 3 in my_list2:
#     print("3 esta na lista")

#deletar algum valor item da lista

# del my_list[2:] # estou dizendo para deletar apartir da posicão 2 até o final da lista
# print(my_list)

#Criar uma lista em branco, e podemos adicionar itens na mesma com o metodo append()
# my_list4 = []
# my_list4.append(57)
# print(my_list4)


# lista = [121,218,310,5,42,9,75]
#Usar o metodo sort vai colocar a lista em ordem crescente.
# lista.sort()
# print(lista)
#Usar o metodo reverse coloca a lista revertida
# lista.reverse()
# print(lista)





