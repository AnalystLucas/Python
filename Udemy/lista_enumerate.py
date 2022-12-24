"""
################################
# LIST ENUMERATE (PY AVANÇADO) #
################################

"""

# Printando sem função enumerate, a possição do item, mais o item.
# lista = ["abacate","bola","cachorro" ]

# for i in range(len(lista)): #range é para informar até onde vamos buscar, como uma lista pode ter um tamanho indeterminado, passando a função len() para ler o tamanho da lista e assim saber o tamanho da mesma.
#     print(i, lista[i])

lista = ["abacate","bola","cachorro" ]
for i, nome in enumerate(lista):
    print(i, nome)
