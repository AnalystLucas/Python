"""
##########################
# LIST MAP (PY AVANÇADO) #
##########################

"""
#função map recebe uma função mais um valor podem ser uma lista, nessa questão era irar interagir cada elemento da lista com a função.

def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5]

vd = (map(dobro, valor))

# for v in vd:
#     print(v)

# convertendo em uma lista 
vd = list(vd);
print(vd)