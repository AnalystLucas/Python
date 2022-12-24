"""
######################
# NUMEROS ALEATORIOS #
######################

Trabalhar com numeros randomicos.
usando random

"""

import random

lista = [2, 9, 16]
numero = random.choice(lista) # dessa forma conseguimos escolher aleatoriamente um valor dentro de um array(Lista)
# numero = random.randint(0, 10) # dessa forma conseguimos controlar de onde começa até onde termina o intervalo que será usado para sorte o numero aleatorio
print(numero)
