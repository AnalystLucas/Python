"""
######################
# Operadores Logicos #
######################

AND - usado para validar entre condições e retorna se é verdadeiro ou falso
OR  - usado para validar se entre as condições uma delas são verdadeira, retorna verdadeiro ou falso 
NOT - usado para inverte o valor entre as condições, também retorna verdadeiro ou falso (porém se era verdadeiro passa a ser falso e se falso passa a ser verdadeiro)

"""

#Exemplo

x = 10
y = 11

#Operador AND
print(x == y and x <= 10)

#Operador OR
print(x == y or x < y)

#Operador NOT
print(not x > y)